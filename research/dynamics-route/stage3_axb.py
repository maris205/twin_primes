"""Dynamics route, stage 3: ax+b-invariant quadratic statistics on rough support.

(1) Primitive reduction.  For completely multiplicative f, f(m) f(m+h) = f(m') f(m'+h') where d = gcd(m, h)
    (a rough number when m is rough), m = d m', h = d h'.  We check it for f = lambda and count how much of the
    rough-pair mass at each gap h lies on primitive pairs.
(2) Averaged statistic.  T(f) = average over even h <= H of s(h) C_f(h), with s(h) = chi_4(n) chi_4(n+h) for odd n
    (+1 if 4 | h, -1 otherwise) and C_f(h) the normalized correlation of f on rough pairs at gap h.  For a
    family f_t of completely multiplicative functions with f_t(p) chi_4(p) = +1 with probability (1+t)/2
    (independently over rough primes) we compare T(f_t) with m_t^2, where m_t is the one-point mean of
    f_t chi_4 on rough integers (the pretentious data).  lambda and chi_4 are included.

usage: python stage3_axb.py N z H
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '../parity-wall-route/route')
from bilinear_probe import factor_info, primes_upto

N = int(float(sys.argv[1])); Z = int(sys.argv[2]); H = int(sys.argv[3])
L = N + H + 2                                     # arrays are indexed by the integer itself, 0..L
spf = np.zeros(L + 1, np.int64)
primes_all = primes_upto(L)
for p in primes_all:
    blk = spf[p::p]; blk[blk == 0] = p
n = np.arange(L + 1)
R = (spf >= Z) & (n >= Z)
chi4 = np.where(n % 2 == 0, 0, np.where(n % 4 == 1, 1, -1))

def mult_from_primes(vals):
    """Completely multiplicative f with f(p) = vals[i] for p = primes_all[i]."""
    tab = np.zeros(L + 1, np.int64); tab[primes_all] = vals
    f = np.ones(L + 1, np.int64); rem = n.copy()
    while np.any(rem > 1):
        live = rem > 1
        p = spf[np.where(live, rem, 0)]
        f[live] *= tab[p[live]]
        rem[live] //= p[live]
    return f
rng = np.random.default_rng(3)
lam = mult_from_primes(-np.ones(len(primes_all), np.int64))

idx = np.nonzero(R[: N + 1])[0]                   # rough integers m <= N
def corr(f, h):
    a = idx; ok = R[a + h]
    return float(np.mean(f[a[ok]] * f[a[ok] + h])) if ok.any() else 0.0
def T(f):
    hs = np.arange(2, H + 1, 2)
    return float(np.mean([(1 if h % 4 == 0 else -1) * corr(f, h) for h in hs]))
def mean_twist(f):
    return float(np.mean((f * chi4)[idx]))

out = dict(N=N, z=Z, H=H, rows=[])
c4 = np.where(primes_all % 4 == 1, 1, -1)
fams = [("chi4", c4), ("lambda", -np.ones(len(primes_all), np.int64))]
for t in (0.8, 0.5, 0.2, 0.0):
    eta = np.where(rng.random(len(primes_all)) < (1 + t) / 2, 1, -1)
    fams.append((f"f_t={t}", c4 * eta))
for name, vals in fams:
    f = mult_from_primes(vals)
    m = mean_twist(f); tt = T(f)
    row = dict(f=name, mean_f_chi4=m, mean_sq=m * m, T=tt, gap2=corr(f, 2), gap4=corr(f, 4))
    out["rows"].append(row); print(row, flush=True)

# primitive reduction check for lambda at gaps h = 2 d, d rough
check_om = factor_info(1, L + 1, primes_upto(int(L ** 0.5) + 1))[0]
assert np.all(lam[1:L + 1] == 1 - 2 * (check_om.astype(np.int64) % 2)), "lambda reconstruction"
chk = []
for h in (2, 2 * 31, 2 * 37, 2 * 31 * 37):
    a = idx[idx + h <= L]; a = a[R[a + h]]
    g = np.gcd(a, h); mp = a // g; hp = h // g
    lhs = lam[a] * lam[a + h]; rhs = lam[mp] * lam[mp + hp]
    chk.append(dict(h=h, pairs=int(len(a)), identity_holds=bool(np.all(lhs == rhs)),
                    primitive_fraction=float(np.mean(g == 1))))
out["primitive"] = chk; print(chk)
json.dump(out, open(f"stage3_axb_{N:.0e}_z{Z}.json", "w"), indent=1)
