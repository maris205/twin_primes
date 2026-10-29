"""Stage 19 follow-up: is the (2|p)(2|q) signal in lambda(pq+2) a two-point effect?

For n = pq+2 (p, q primes in [P,2P], p != q) and for the one-point baseline (all odd n in the
same range), tabulate the mean of lambda(n) in cells (n mod 8, n is a sum of two squares,
optionally n z-rough).  The residual statistic subtracts the baseline cell mean from each
lambda(pq+2) and correlates the residual with (2|pq).  A one-point effect gives residual z ~ 0.

usage: python stage19_mod8.py P [z]
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

P = int(sys.argv[1]); ZR = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
pr = primes_upto(2 * P); pr = pr[pr >= P].astype(np.int64)
pp, qq = np.meshgrid(pr, pr, indexing="ij")
off = pp < qq                     # unordered pairs: y is symmetric in (p, q)
p, q = pp[off], qq[off]
r = p * q
XM = int(r.max()) + 4
om, _, spf = factor_info(1, XM + 1, primes_upto(int(XM ** 0.5) + 2))
lam = np.concatenate([[0], 1 - 2 * (om % 2)]).astype(float)
spf = np.concatenate([[0], spf])

def s2(v):
    v = v.copy(); ok = np.ones(len(v), bool)
    for t in primes_upto(int(math.isqrt(int(v.max()))) + 1):
        t = int(t); e = np.zeros(len(v), int)
        while True:
            d = v % t == 0
            if not d.any(): break
            v[d] //= t; e[d] += 1
        if t % 4 == 3:
            ok &= e % 2 == 0
    return ok & (v % 4 != 3)

n = r + 2
keep = spf[n] >= ZR
n, p, q = n[keep], p[keep], q[keep]
y = lam[n]
chi = np.where(((p % 8) == 1) | ((p % 8) == 7), 1, -1) * np.where(((q % 8) == 1) | ((q % 8) == 7), 1, -1)

base = np.arange(int(n.min()) | 1, int(n.max()) + 1, 2, dtype=np.int64)
base = base[spf[base] >= max(ZR, 3)]
lb = lam[base]
cell_b = (base % 8) * 2 + s2(base)
cell_y = (n % 8) * 2 + s2(n)
mb = np.zeros(16); cb = np.bincount(cell_b, minlength=16)
np.add.at(mb, cell_b, lb); mb = np.divide(mb, np.maximum(cb, 1))
res = y - mb[cell_y]
z_raw = float(np.sum((y - y.mean()) * chi) / math.sqrt(np.sum((y - y.mean()) ** 2)))
z_res = float(np.sum((res - res.mean()) * chi) / math.sqrt(np.sum((res - res.mean()) ** 2)))
cells = {}
for c in range(16):
    m = cell_y == c
    if m.sum() > 0:
        cells[f"n%8={c // 2},S2={c % 2}"] = dict(count=int(m.sum()), mean_y=float(y[m].mean()), baseline=float(mb[c]))
out = dict(P=P, z=ZR, pairs=int(len(y)), z_raw=z_raw, z_residual=z_res, cells=cells)
print(json.dumps(out, indent=1))
json.dump(out, open(f"stage19_mod8_P{P}_z{int(ZR)}.json", "w"), indent=1)
