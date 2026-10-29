"""Rough two-point Chowla at shift 2 (Tao's GEH-equivalent form of the parity node):
   C_R(x) = sum_{n<=x} mu(n)1_R(n) mu(n+2)1_R(n+2) / sum_{n<=x} 1_R(n)1_R(n+2),
R = {no prime factor <= x^eps} (Cesaro, absolute roughness) and
R_rel = {n : no prime factor <= n^eps} (needed for the logarithmic version; with absolute
roughness the small n are all primes and bias the log average).  Under GEH, HL <=> C_R(x) -> 0 (Bombieri; Tao 2016 notes).
Also the logarithmic version with weights 1/n."""
import json, math, sys
import numpy as np
XMAX = int(float(sys.argv[1])); top = XMAX + 2
spf = np.zeros(top + 1, dtype=np.int32)
for p in range(2, math.isqrt(top) + 1):
    if spf[p] == 0:
        blk = spf[p * p::p]; blk[blk == 0] = p
isp = spf == 0; isp[:2] = False; spf[isp] = np.nonzero(isp)[0]
n = np.arange(top + 1, dtype=np.int64)
m = n.copy(); Om = np.zeros(top + 1, dtype=np.int8); sqf = np.ones(top + 1, dtype=bool)
prev = np.zeros(top + 1, dtype=np.int64)
for _ in range(40):
    act = m > 1
    if not act.any(): break
    p = spf[np.where(act, m, 0)].astype(np.int64)
    sqf &= ~(act & (p == prev))
    prev = np.where(act, p, prev)
    m = np.where(act, m // np.maximum(p, 1), m)
    Om += act
mu = np.where(sqf, np.where(Om % 2 == 0, 1, -1), 0)
out = []
for eps in (0.1, 0.2):
    for k in range(4, int(round(math.log10(XMAX))) + 1):
        x = 10 ** k; z = x ** eps
        R = (spf > z)
        a, b = slice(3, x + 1), slice(5, x + 3)
        pair = R[a] & R[b]
        num = float((mu[a] * mu[b])[pair].sum()); den = float(pair.sum())
        nn = n[a].astype(float)
        Rrel = (spf[a] > nn ** eps) & (spf[b] > (nn + 2) ** eps) & (nn > 2 ** (1 / eps))
        w = 1.0 / nn
        numl = float(((mu[a] * mu[b]) * w)[Rrel].sum()); denl = float(w[Rrel].sum())
        row = {"eps": eps, "x": x, "rough_pairs": int(den), "C_R": num / den, "C_R_log": numl / denl,
               "1/sqrt(pairs)": 1 / math.sqrt(den)}
        out.append(row); print(json.dumps(row), flush=True)
json.dump(out, open("rough_chowla.json", "w"), indent=1)
