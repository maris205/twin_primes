"""Dynamics route, stage 2: Furstenberg / Palm systems of lambda on rough pairs.

For n <= N and several z we report:
  density      fraction of n that are z-rough (Furstenberg systems of lambda*1_R see only this; -> 0)
  pairs        rough pairs (n, n+2)
  isolated_H   fraction of rough pairs with no other rough integer in [n-H, n+2+H]  (Palm system of isolated
               pairs: its shift dynamics is trivial when this -> 1)
  even         fraction of rough pairs in the even class (the single parameter the Palm system retains)
and, for one z, the dilation defect of three sign sequences g on rough integers:
  lambda, chi_4, and a random-pair counterfeit (chi_4 times an independent sign per rough pair): the fraction of
  rough pairs (m, m+2) and rough primes p <= P with g(pm) g(p(m+2)) = g(m) g(m+2).  Completely multiplicative
  sequences agree everywhere (dilation consistency, the rough form of strong stationarity).

usage: python stage2_furstenberg.py N P H
"""
import sys, json
import numpy as np
sys.path.insert(0, '../parity-wall-route/route')
from bilinear_probe import factor_info, primes_upto

N = int(float(sys.argv[1])); PMAX = int(sys.argv[2]); H = int(sys.argv[3])
om, _, spf = factor_info(1, N + 3, primes_upto(int((N + 3) ** 0.5) + 1))
n = np.arange(1, N + 3)
lam = 1 - 2 * (om.astype(np.int64) % 2)
out = dict(N=N, H=H, rows=[])
for z in [11, 30, 100, 300, 1000]:
    R = (spf >= z) & (n >= z)
    pr = R[:-2] & R[2:]
    idx = np.nonzero(pr)[0]
    c = np.concatenate([[0], np.cumsum(R)])
    lo = np.maximum(idx - H, 0); hi = np.minimum(idx + 3 + H, len(R))
    others = c[hi] - c[lo] - 2
    row = dict(z=z, density=float(R.mean()), pairs=int(len(idx)), isolated_H=float(np.mean(others == 0)),
               mean_others_H=float(others.mean()),
               even=float(np.mean(lam[idx] * lam[idx + 2] == 1)))
    out["rows"].append(row); print(row, flush=True)

z = 30
R = (spf >= z) & (n >= z)
pairs = np.nonzero(R[:-2] & R[2:])[0]
chi4 = np.where(n % 2 == 0, 0, np.where(n % 4 == 1, 1, -1))
rng = np.random.default_rng(2)
eps = np.zeros(len(n), int); eps[pairs] = rng.choice([-1, 1], size=len(pairs)); eps[pairs + 2] = eps[pairs]
g_rand = np.where(R, chi4 * np.where(eps == 0, rng.choice([-1, 1], size=len(n)), eps), 0)
P = [int(p) for p in primes_upto(PMAX) if p >= z]
def defect(g):
    """Pointwise dilation consistency: fraction of (m, p) with g(pm) g(p(m+2)) == g(m) g(m+2)."""
    agree, tot = 0, 0
    for p in P:
        m = pairs[(pairs + 3) * p <= N + 1]              # 0-based index i <-> integer i+1; pair (i+1, i+3)
        a = (m + 1) * p - 1                               # index of p*(i+1)
        agree += int(np.sum(g[a] * g[a + 2 * p] == g[m] * g[m + 2])); tot += len(m)
    return dict(edges=tot, agreement=agree / tot, gap2_mean=float(np.mean(g[pairs] * g[pairs + 2])))
out["dilation"] = {name: defect(g) for name, g in (("lambda", lam * R), ("chi4", chi4 * R), ("random_pair", g_rand))}
print(out["dilation"])
json.dump(out, open(f"stage2_furstenberg_{N:.0e}.json", "w"), indent=1)
