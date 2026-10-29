"""Stage 29: the roughness parameter.  How does the twin correlation of lambda on z-rough pairs behave as z
runs from fixed values through exp(sqrt(log x)) to x^eta, and where do the known reach thresholds sit?

For x and a list of z we report, over n <= x with n, n+2 both z-rough:
  pairs, the one-point mean m(z) of lambda on z-rough n (its square is the independence prediction
  for the pair correlation), normalized correlation c(z) = mean lambda(n) lambda(n+2), its z-score against 1/sqrt(pairs),
  the even-class count, rho = log log z / log log x, and D^2(z) = sum_{z<=p<=x} (1 + chi_4(p))/p
  (the pretentious distance from lambda to the counterfeit chi_4 on [z, x]) next to log(log x / log z).

usage: python stage29_reach.py X
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1]))
om, _, spf = factor_info(1, X + 3, primes_upto(int((X + 3) ** 0.5) + 1))
lam = 1 - 2 * (om.astype(np.int64) % 2)          # index i <-> n = i + 1
pr = primes_upto(X)
L = math.log(X)
zs = sorted(set([5, 11, 30, 100, round(math.exp(math.sqrt(L) / 2)), round(math.exp(math.sqrt(L))),
                 round(X ** 0.1), round(X ** 0.15), round(X ** 0.2), round(X ** 0.25)]))
rows = []
for z in zs:
    rough = spf >= z                               # spf of a prime > sqrt(X) is the large sentinel
    ok = rough[:-2] & rough[2:]                    # n and n+2 both z-rough, n = i + 1
    ok[:max(0, z - 2)] = False                     # keep n >= z so that n itself is not 1 or a small prime
    k = int(ok.sum()); s = int((lam[:-2] * lam[2:])[ok].sum())
    r1 = rough.copy(); r1[:max(0, z - 1)] = False
    m1 = float(lam[r1].mean())                     # one-point mean of lambda on z-rough n >= z
    ps = pr[pr >= z]
    d2 = float(np.sum((1 + np.where(ps % 4 == 1, 1, -1)) / ps))
    rows.append(dict(z=z, rho=round(math.log(math.log(z)) / math.log(L), 3), pairs=k,
                     corr=round(s / k, 5), mean1=round(m1, 4), mean1_sq=round(m1 * m1, 5), zscore=round(s / math.sqrt(k), 2), even=(k + s) // 2,
                     D2_chi4=round(d2, 3), log_logx_over_logz=round(math.log(L / math.log(z)), 3)))
    print(rows[-1], flush=True)
json.dump(dict(X=X, rows=rows), open(f"stage29_reach_{X:.0e}.json", "w"), indent=1)
