"""Stage 31: the Helfgott-Radziwill decomposition on rough support, numerically.

Shift-2 dilation: for p >= z, (pm, p(m+2)) is an edge n ~ n + 2p with p | n, and lambda*1_R is invariant up to
lambda(p)^2 = 1.  On n in (N, 2N] with f supported on z-rough n we compare, for f = lambda*1_R and the
counterfeit f = chi_4*1_R:
  C      normalized gap-2 correlation on rough pairs
  E      edge form   <f, A f> / <|f|, A |f|>,   (A f)(n) = sum_{p in P, p | n} f(n+2p) + f(n-2p)
  Mterm  mean form   <f, M f> / <|f|, M |f|>,   (M f)(n) = sum_{p in P} (f(n+2p) + f(n-2p)) / p
  and the spectral quantities of B = 1_R (A - M) 1_R:
  ||B|| (power iteration), the rough average degree d_R = <1_R, A 1_R> / |R|, and the HR scale sqrt(2L).
A dilation-spectral certificate resolves the edge form only up to res = ||B|| / d_R.

usage: python stage31_rough_hr.py N z K      (P = primes in [z, z^K])
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

N = int(float(sys.argv[1])); Z = int(sys.argv[2]); K = float(sys.argv[3])
H = int(Z ** K)
lo, hi = N - 2 * H - 2, 2 * N + 2 * H + 3          # padded window, index i <-> n = lo + i
om, _, spf = factor_info(lo, hi, primes_upto(int(hi ** 0.5) + 1))
n = np.arange(lo, hi)
R = spf >= Z
inside = (n > N) & (n <= 2 * N)
lam = 1 - 2 * (om.astype(np.int64) % 2)
chi4 = np.where(n % 2 == 0, 0, np.where(n % 4 == 1, 1, -1))
P = [int(p) for p in primes_upto(H) if p >= Z]
L = sum(1 / p for p in P)

def shift(v, s):
    out = np.zeros_like(v)
    if s > 0: out[:-s] = v[s:]
    else: out[-s:] = v[:s]
    return out
def A(v):
    out = np.zeros(len(v))
    for p in P:
        m = (n % p == 0)
        out += m * (shift(v, 2 * p) + shift(v, -2 * p))
    return out
def M(v):
    out = np.zeros(len(v))
    for p in P:
        out += (shift(v, 2 * p) + shift(v, -2 * p)) / p
    return out
mask = (R & inside).astype(float)
def B(v):
    w = v * mask
    return (A(w) - M(w)) * mask

res = dict(N=N, z=Z, K=K, H=H, primes=len(P), L=L, rough=int(mask.sum()))
pairs = (R[:-2] & R[2:] & inside[:-2])
for name, g in (("lambda", lam), ("chi4", chi4)):
    f = g * mask; a = np.abs(f)
    res[name] = dict(
        C=float((g[:-2] * g[2:])[pairs].mean()),
        E=float(f @ A(f) / (a @ A(a))),
        Mterm=float(f @ M(f) / (a @ M(a))),
        spectral_part=float((f @ B(f)) / (a @ A(a))))
dR = float(mask @ A(mask) / mask.sum())
rng = np.random.default_rng(31); v = rng.standard_normal(len(mask)) * mask
for _ in range(60):
    v = B(B(v)); v /= np.linalg.norm(v)
normB = float(math.sqrt(np.linalg.norm(B(B(v))) / np.linalg.norm(v)))
res.update(d_R=dR, normB=normB, sqrt_2L=math.sqrt(2 * L), sqrt_dR=math.sqrt(dR), resolution=normB / dR)
print(json.dumps(res, indent=1))
json.dump(res, open(f"stage31_rough_hr_{N:.0e}_z{Z}_K{K}.json", "w"), indent=1)
