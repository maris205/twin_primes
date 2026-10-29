"""Stage 24: monochromatic rough triples (n, n+2, n+6).

Part A (combinatorics).  Rough triples have n coprime to 6 with n = 5 mod 6.  A periodic counterfeit is a
colouring f of the residues coprime to 6 modulo M (6 | M).  We enumerate all such colourings and keep those
with NO monochromatic triple (f(a), f(a+2), f(a+6)) over a = 5 mod 6; for each we record the averaged pair
correlations (c2, c4, c6) and report the achievable set: in particular whether every mono-free colouring
kills twins (c2 = -1) and which gap it keeps.

Part B (real world).  On rough triples up to X: the monochromatic share by residue class of n mod 12 and
mod 60, and the correlation of lambda with the periodic counterfeit patterns (chi_4, and the mod-3 class
sign), which a periodic counterfeit would push to +-1.

usage: python stage24_mono.py X eta
"""
import sys, json, math, itertools
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); ETA = float(sys.argv[2])
out = dict(X=X, eta=ETA, partA={})

# ---- Part A ----
for M in [12, 24, 36, 48, 60]:
    res = [r for r in range(M) if math.gcd(r, 6) == 1]
    idx = {r: i for i, r in enumerate(res)}
    starts = [a for a in range(M) if a % 6 == 5]
    trip = np.array([[idx[a % M], idx[(a + 2) % M], idx[(a + 6) % M]] for a in starts])
    m = len(res)
    if m > 20:
        out["partA"][M] = "skipped (2^%d colourings)" % m
        continue
    cols = ((np.arange(2 ** m)[:, None] >> np.arange(m)) & 1) * 2 - 1      # all colourings, shape (2^m, m)
    s0, s2, s6 = cols[:, trip[:, 0]], cols[:, trip[:, 1]], cols[:, trip[:, 2]]
    mono = ((s0 == s2) & (s2 == s6)).any(1)
    free = ~mono
    c = np.stack([(s0 * s2).mean(1), (s2 * s6).mean(1), (s0 * s6).mean(1)], 1)[free]
    pts = sorted(set(tuple(np.round(v, 4)) for v in c))
    out["partA"][M] = dict(colourings=int(2 ** m), mono_free=int(free.sum()),
                          min_c2=float(c[:, 0].min()) if len(c) else None, max_c2=float(c[:, 0].max()) if len(c) else None,
                          points=[list(p) for p in pts][:40], n_points=len(pts))
    print(M, out["partA"][M]["mono_free"], "of", 2 ** m, "mono-free; c2 range",
          out["partA"][M]["min_c2"], out["partA"][M]["max_c2"], "points:", pts[:12], flush=True)

# ---- Part B ----
Z = X ** ETA
plist = primes_upto(int((X + 8) ** 0.5) + 1)
lam = np.empty(X + 8, np.int8); rough = np.zeros(X + 8, bool)
for a in range(1, X + 8, 10_000_000):
    b = min(a + 10_000_000, X + 8)
    om, _, spf = factor_info(a, b, plist)
    lam[a:b] = 1 - 2 * (om % 2); rough[a:b] = spf >= Z
n = np.nonzero(rough[:X] & rough[2:X + 2] & rough[6:X + 6])[0]
n = n[n >= X // 10]
S = np.stack([lam[n], lam[n + 2], lam[n + 6]], 1).astype(float)
mono = (S[:, 0] == S[:, 1]) & (S[:, 1] == S[:, 2])
byres = {}
for Mres in [12, 60]:
    r = n % Mres
    byres[Mres] = {int(v): round(float(mono[r == v].mean()), 4) for v in np.unique(r)}
chi4 = lambda v: np.where(v % 4 == 1, 1.0, -1.0)
sig3 = lambda v: np.where(v % 3 == 1, 1.0, -1.0)
pc = {f"E[s_{h} chi4(n+{h})]": float(np.mean(S[:, i] * chi4(n + h))) for i, h in enumerate([0, 2, 6])}
pc.update({f"E[s_{h} sigma3(n+{h})]": float(np.mean(S[:, i] * sig3(n + h))) for i, h in enumerate([0, 2, 6])})
out["partB"] = dict(triples=int(len(n)), P_mono=float(mono.mean()), mono_by_residue=byres, periodic_corr=pc,
                    z_scale=1 / math.sqrt(len(n)))
print(json.dumps(out["partB"], indent=1))
json.dump(out, open(f"stage24_mono_{X:.0e}.json", "w"), indent=1)
