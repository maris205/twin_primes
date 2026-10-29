"""H9+: is lambda a Dirichlet character, of line-dependent conductor, on some family of integer lines?

Function-field model (Sawin-Shusterman): on the line f = r + s^p, mu(f) = eps * chi_{r'}(f), a
quadratic character whose modulus r' depends on the line and is large compared with the line.
Integer candidates: lines n = r + m*s (m = 1: short intervals; m random) or n = r + s^2, with a
line-dependent odd modulus D(r) and test function chi(n) = (n | D) (Jacobi symbol).  For each
family we report z = sum lambda(n) chi(n) / sqrt(sum chi(n)^2) over all lines (null: N(0,1)), and
the RMS of the per-line z (null: about 1).  A positive control replaces lambda by a planted
model lambda~(n) = (n | D) on half of the lines, which the statistic must detect.

usage: python h9_lines.py X nlines L
"""
import sys, json, math, time
import numpy as np
from sympy import factorint
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); NL = int(sys.argv[2]); L = int(sys.argv[3])
rng = np.random.default_rng(7)
t0 = time.time()
plist = primes_upto(int((X + 4) ** 0.5) + 1)
lam = np.empty(X + 1, np.int8); lam[0] = 0
SEG = 10_000_000
for a in range(1, X + 1, SEG):
    b = min(a + SEG, X + 1)
    om, _, _ = factor_info(a, b, plist)
    lam[a:b] = 1 - 2 * (om % 2)
print(f"lambda table to {X:.0e}: {time.time()-t0:.0f}s", flush=True)


def jacobi(a, n):
    """Vectorised Jacobi symbol (a | n), n odd positive (scalar), a array of non-negative ints."""
    a = a % n
    n = np.full_like(a, n)
    res = np.ones_like(a)
    while True:
        done = (a == 0)
        if done.all():
            break
        # remove factors of 2 from a
        while True:
            ev = (a % 2 == 0) & (a != 0)
            if not ev.any():
                break
            r8 = n % 8
            flip = ev & ((r8 == 3) | (r8 == 5))
            res[flip] *= -1
            a[ev] //= 2
        # reciprocity and reduce
        act = a != 0
        sw = act & (a % 4 == 3) & (n % 4 == 3)
        res[sw] *= -1
        a2 = np.where(act, n % np.where(act, a, 1), 0)
        n = np.where(act, a, n)
        a = a2
    return np.where(n == 1, res, 0)


def arith_derivative(r):
    f = factorint(int(r))
    return int(sum(r // p * e for p, e in f.items()))


def odd_part(d):
    d = int(d)
    while d % 2 == 0 and d > 0:
        d //= 2
    return d


DFUNCS = {
    "r'": lambda r: arith_derivative(r),
    'r': lambda r: r,
    'r+1': lambda r: r + 1,
    '4r+1': lambda r: 4 * r + 1,
}
FAMILIES = [('interval', lambda r, m, s: r + s), ('AP', lambda r, m, s: r + m * s), ('r+s^2', lambda r, m, s: r + s * s)]

rows = []
s = np.arange(1, L + 1, dtype=np.int64)
for fam, gen in FAMILIES:
    for dname, Df in DFUNCS.items():
        num = den = num_pc = den_pc = 0.0
        zline = []
        used = 0
        for _ in range(NL):
            r = int(rng.integers(X // 10, X // 2))
            m = int(rng.integers(3, 2000)) | 1
            n = gen(r, m, s)
            if n.max() > X:
                continue
            D = odd_part(Df(r))
            if D <= 1:
                continue
            chi = jacobi(n.copy(), D).astype(np.float64)
            l = lam[n].astype(np.float64)
            c2 = float((chi * chi).sum())
            if c2 == 0:
                continue
            num += float((l * chi).sum()); den += c2
            zline.append(float((l * chi).sum()) / math.sqrt(c2))
            # positive control: plant lambda~ = chi on every other line (where chi != 0)
            if used % 2 == 0:
                lt = np.where(chi != 0, chi, l)
                num_pc += float((lt * chi).sum()); den_pc += c2
            used += 1
        z = num / math.sqrt(den) if den else float('nan')
        zpc = num_pc / math.sqrt(den_pc) if den_pc else float('nan')
        rms = float(np.sqrt(np.mean(np.square(zline)))) if zline else float('nan')
        rows.append(dict(family=fam, D=dname, lines=used, z=z, rms_line_z=rms, control_z=zpc))
        print(f"{fam:9s} D={dname:5s} lines={used:6d}  z={z:+7.2f}  per-line RMS={rms:.3f}  [control z={zpc:9.1f}]  ({time.time()-t0:.0f}s)", flush=True)
json.dump(dict(X=X, L=L, rows=rows), open(f'h9_lines_{X:.0e}.json'.replace('+', ''), 'w'), indent=1)
