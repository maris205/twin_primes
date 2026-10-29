"""Signal amplification checks (route/AMPLIFICATION.md).

Model (Bombieri one-dimensional parity, two-sided form "1D"):
  among x^eta-rough pairs (n, n+2), the (Omega(n), Omega(n+2)) = (r, r') mass is
      m(r, r') = I_r I_r' (1 + (delta - 1)(-1)^{r+r'})        (I_r: HL-model masses)
  so for weights w = lambda * |w| (lambda-signed) the delta-coefficient is the full |w|-mass
  (coherent signal), while the neutral term is (sum lambda-signed)^2.
Real world presumably delta = 1:  m(r,r') = I_r I_r'  (independence).

Part A: joint (r, r') table for rough pairs in (x/2, x]; test m(r,r') = row_r col_r' / total,
        and E[lambda lambda] = E[lambda]^2 (the delta = 1 prediction).
Part B: shift averaging: C(h) = E_rough-pairs-at-shift-h[lambda lambda] for h = 2 and h = 2p,
        p prime in [x^eta, x^{eta'}]; compare with E[lambda]^2.
"""
import json, math, sys
import numpy as np

X = int(float(sys.argv[1])); top = X + 2 * 400
spf = np.zeros(top + 1, dtype=np.int32)
for p in range(2, math.isqrt(top) + 1):
    if spf[p] == 0:
        blk = spf[p * p::p]; blk[blk == 0] = p
isp = spf == 0; isp[:2] = False; spf[isp] = np.nonzero(isp)[0]
n = np.arange(top + 1, dtype=np.int64)
mm = n.copy(); Om = np.zeros(top + 1, np.int8)
for _ in range(40):
    act = mm > 1
    if not act.any(): break
    p = spf[np.where(act, mm, 0)].astype(np.int64)
    mm = np.where(act, mm // np.maximum(p, 1), mm); Om += act
del mm
lam = np.where(Om % 2 == 0, 1.0, -1.0)
out = {"A": [], "B": []}
lo = X // 2 + 1
for eta in (0.12, 0.15, 0.2, 0.25):
    z = X ** eta
    R = spf > z
    a, b = slice(lo, X + 1), slice(lo + 2, X + 3)
    pair = R[a] & R[b]
    ra, rb = Om[a][pair].astype(int), Om[b][pair].astype(int)
    rmax = int(max(ra.max(), rb.max()))
    T = np.zeros((rmax + 1, rmax + 1))
    np.add.at(T, (ra, rb), 1)
    tot = T.sum(); row = T.sum(1); col = T.sum(0)
    E = np.outer(row, col) / tot
    mask = E > 50
    ratio = (T[mask] / E[mask])
    la = lam[a][pair]; lb = lam[b][pair]
    single = float(np.concatenate([lam[a][R[a]], lam[b][R[b]]]).mean())
    out["A"].append({"eta": eta, "x^eta": z, "pairs": int(tot), "max_r": rmax,
                     "cells_tested": int(mask.sum()),
                     "max |m/(row*col/tot) - 1|": float(np.abs(ratio - 1).max()),
                     "mean |m/(row*col/tot) - 1|": float(np.abs(ratio - 1).mean()),
                     "E[lam lam]": float((la * lb).mean()), "E[lam]^2 (rough singles)": single ** 2,
                     "table_rows": {int(r): [int(v) for v in T[r]] for r in range(rmax + 1) if T[r].sum() > 0}})
    print(json.dumps({k: v for k, v in out["A"][-1].items() if k != "table_rows"}), flush=True)
    # Part B: shift averages over h = 2p, p prime in (z, z^2] (cap at 400/2)
    ps = [int(q) for q in np.nonzero(isp[int(z) + 1: min(int(z ** 2), 199) + 1])[0] + int(z) + 1]
    Ch = []
    for h in [2] + [2 * q for q in ps]:
        bh = slice(lo + h, X + 1 + h)
        ph = R[a] & R[bh]
        Ch.append(float((lam[a][ph] * lam[bh][ph]).mean()))
    out["B"].append({"eta": eta, "C(2)": Ch[0], "mean_p C(2p)": float(np.mean(Ch[1:])) if len(Ch) > 1 else None,
                     "sd_p C(2p)": float(np.std(Ch[1:])) if len(Ch) > 1 else None, "n_p": len(Ch) - 1,
                     "E[lam]^2": single ** 2})
    print(json.dumps(out["B"][-1]), flush=True)
json.dump(out, open("amplification.json", "w"), indent=1)
