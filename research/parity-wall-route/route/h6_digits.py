"""H6: integer 'Pellet' test in a large base.

Write n = a_0 + a_1 p + ... + a_d p^d (p prime, a_d != 0) and attach the digit
polynomial f_n(T) = sum a_i T^i in F_p[T].  By Pellet's formula, the function-field
Moebius of f_n is G(n) = (-1)^d * chi_p(disc f_n) (0 if disc = 0).
Test: correlation of G(n) with lambda(n), mu(n), and lambda(n)*1[n is z-rough].

usage: python h6_digits.py d p
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

d = int(sys.argv[1]); p = int(sys.argv[2])
X = p ** (d + 1)
ETAS = [0.1, 0.15, 0.2]
SEG = 10_000_000
rng = np.random.default_rng(11)

# Legendre table mod p
leg = np.zeros(p, np.int64)
sq = set((i * i) % p for i in range(1, p))
for r in range(1, p):
    leg[r] = 1 if r in sq else -1


def disc(coeffs):
    """Discriminant mod p of a_d T^d + ... + a_0 for d = 2, 3 (vectorised)."""
    if d == 2:
        a0, a1, a2 = coeffs
        return (a1 * a1 - 4 * a2 * a0) % p
    if d == 3:
        a0, a1, a2, a3 = coeffs           # a=a3, b=a2, c=a1, dd=a0
        a, b, c, e = a3, a2, a1, a0
        D = (18 * a * b % p * c % p * e - 4 * pow3(b) % p * e - 0) % p
        D = (D + b * b % p * c % p * c - 4 * a % p * pow3(c) - 27 * a * a % p * e % p * e) % p
        return D
    raise ValueError


def pow3(v):
    return v % p * v % p * v % p


t0 = time.time()
plist = primes_upto(int((X + 4) ** 0.5) + 1)
zs = [X ** e for e in ETAS]
acc = {k: [0.0, 0.0, 0.0] for k in ['lambda', 'mu'] + [f'lambda_rough_{e}' for e in ETAS] + ['lambda_perm']}
lo = p ** d                                   # leading digit >= 1
for a in range(lo, X, SEG):
    b = min(a + SEG, X)
    om, sqf, spf = factor_info(a, b, plist)
    n = np.arange(a, b, dtype=np.int64)
    lam = (1 - 2 * (om % 2)).astype(np.int64)
    mu = np.where(sqf, lam, 0)
    digs = []
    m = n.copy()
    for _ in range(d + 1):
        digs.append(m % p); m //= p
    D = disc(digs)
    G = ((-1) ** d) * leg[D]
    Gp = rng.permutation(G)
    series = {'lambda': lam, 'mu': mu, 'lambda_perm': None}
    for e, z in zip(ETAS, zs):
        series[f'lambda_rough_{e}'] = lam * (spf >= z)
    for k, f in series.items():
        g = Gp if k == 'lambda_perm' else G
        f = lam if k == 'lambda_perm' else f
        acc[k][0] += float((f * g).sum()); acc[k][1] += float((f * f).sum()); acc[k][2] += float((g * g).sum())
    print(f"segment to {b}: {time.time()-t0:.0f}s", flush=True)

out = dict(d=d, p=p, X=X, n_count=X - lo, rows=[])
for k, (fg, ff, gg) in acc.items():
    corr = fg / math.sqrt(ff * gg)
    noise = 1 / math.sqrt(ff) if ff else float('nan')
    out['rows'].append(dict(series=k, corr=corr, noise=noise, z_score=corr / noise, support=ff))
    print(f"{k:22s} corr={corr:+.6f}  noise~{noise:.6f}  z={corr/noise:+.2f}  support={int(ff)}")
json.dump(out, open(f'h6_digits_d{d}_p{p}.json', 'w'), indent=1)
print('wrote', f'h6_digits_d{d}_p{p}.json', f'{time.time()-t0:.0f}s')
