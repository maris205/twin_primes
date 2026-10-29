"""Numerical test of the parity node of the symbolic-dynamics route (route/ROUTE.md).

On the support of Lambda_2 = mu * log^2 (numbers with at most two distinct prime
factors), the parity symbol lambda(n) = (-1)^Omega(n) separates primes (-1)
from two-factor numbers (+1).  We compute, for x = 10^k:

  delta_x   = sum_{n<=x} Lambda(n) Lambda(n+2) / (2 Pi_2 x)        (HL <=> -> 1)
  s_x       = sum Lambda(n) log n Lambda(n+2) / sum Lambda_2(n) Lambda(n+2)
              (Bombieri: = delta_x/2 + o(1) under EH; FCP-1 <=> -> 1/2)
  shares    W[e1,e2] / sum W, W[e1,e2] = sum Lambda_2(n) Lambda_2(n+2)
              1[lambda(n)=e1, lambda(n+2)=e2]   (FCP-2: each -> 1/4)
"""
import json, math, sys
import numpy as np

XMAX = int(float(sys.argv[1]))
top = XMAX + 2
spf = np.zeros(top + 1, dtype=np.int32)
for p in range(2, math.isqrt(top) + 1):
    if spf[p] == 0:
        blk = spf[p * p::p]
        blk[blk == 0] = p
isp = spf == 0
isp[:2] = False
spf[isp] = np.nonzero(isp)[0]

n = np.arange(top + 1, dtype=np.int64)
p1 = spf.astype(np.int64)
m = n.copy()
a = np.zeros(top + 1, dtype=np.int8)
for _ in range(40):  # strip the smallest prime completely
    d = (m > 1) & (m % np.maximum(p1, 1) == 0)
    if not d.any():
        break
    m[d] //= p1[d]
    a[d] += 1
p2 = np.where(m > 1, spf[np.minimum(m, top)].astype(np.int64), 1)
m2 = m.copy()
b = np.zeros(top + 1, dtype=np.int8)
for _ in range(40):
    d = (m2 > 1) & (m2 % np.maximum(p2, 1) == 0)
    if not d.any():
        break
    m2[d] //= p2[d]
    b[d] += 1
del m
lp1 = np.log(np.maximum(p1, 1).astype(float))
lp2 = np.log(np.maximum(p2, 1).astype(float))
ppow = (n >= 2) & (b == 0)                    # prime power p^a
two = (n >= 2) & (b > 0) & (m2 == 1)          # p^a q^b
del m2
Lam = np.where(ppow, lp1, 0.0)
Lam2 = np.where(ppow, (2 * a.astype(float) - 1) * lp1 ** 2, 0.0) + np.where(two, 2 * lp1 * lp2, 0.0)
lam = np.where((a.astype(int) + b.astype(int)) % 2 == 0, 1, -1)   # valid on supp Lambda_2
logn = np.log(np.maximum(n, 1).astype(float))
del lp1, lp2, p1, p2, a, b

PI2 = 0.6601618158468696
out = []
for k in range(4, int(round(math.log10(XMAX))) + 1):
    x = 10 ** k
    s = slice(1, x + 1)
    s2 = slice(3, x + 3)
    L, L2, l = Lam[s], Lam2[s], lam[s]
    Lp, L2p, lp = Lam[s2], Lam2[s2], lam[s2]
    delta = float(L @ Lp) / (2 * PI2 * x)
    odd_share = float((L * logn[s]) @ Lp) / float(L2 @ Lp)
    W = {}
    for e1 in (-1, 1):
        for e2 in (-1, 1):
            W[f"{e1:+d}{e2:+d}"] = float(((L2 * (l == e1)) @ (L2p * (lp == e2))))
    tot = sum(W.values())
    row = {"x": x, "delta_x": delta, "odd_share_s_x": odd_share,
           "pattern_shares": {k_: v / tot for k_, v in W.items()},
           "M_over_8Pi2_x_log2x": tot / (8 * PI2 * x * math.log(x) ** 2)}
    out.append(row)
    print(json.dumps(row), flush=True)
json.dump(out, open("parity_patterns.json", "w"), indent=1)
