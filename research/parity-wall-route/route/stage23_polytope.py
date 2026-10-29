"""Stage 23: sign geometry of rough admissible triples (n, n+2, n+6).

For triples with all three entries z-rough, s_i = lambda(n + h_i).  Pair correlations
    c2 = E[s0 s2],  c4 = E[s2 s6],  c6 = E[s0 s6]
lie in the cut polytope CUT(K3):  c2+c4+c6 >= -1,  c2-c4-c6 >= -1,  -c2+c4-c6 >= -1,  -c2-c4+c6 >= -1,
and P(monochromatic) = P(s0 = s2 = s6) = (1 + c2 + c4 + c6) / 4.
Twin parity extreme (delta(2) = 0) is the face c2 = -1, which forces c4 = -c6 (a segment).

We compute (c2, c4, c6, P_mono) for the real lambda, and for the same triples reweighted by
  Selberg counterfeit   w = (1 - s0 s2)/2              (kills twins only),
  mod-3 counterfeit     w = (1 - s0 s2)(1 - s2 s6)/4    (kills gaps 2 and 4, Polymath8b Sec. 8),
and check which linear inputs separate the counterfeit face from the real point.

usage: python stage23_polytope.py X eta
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); ETA = float(sys.argv[2]); Z = X ** ETA
plist = primes_upto(int((X + 8) ** 0.5) + 1)
lam = np.empty(X + 8, np.int8); rough = np.zeros(X + 8, bool)
SEG = 10_000_000
for a in range(1, X + 8, SEG):
    b = min(a + SEG, X + 8)
    om, _, spf = factor_info(a, b, plist)
    lam[a:b] = 1 - 2 * (om % 2); rough[a:b] = spf >= Z
n = np.nonzero(rough[:X] & rough[2:X + 2] & rough[6:X + 6])[0]
n = n[n >= X // 10]
s0, s2, s6 = lam[n].astype(float), lam[n + 2].astype(float), lam[n + 6].astype(float)

def stats(w):
    w = w / w.sum()
    c2, c4, c6 = float(np.sum(w * s0 * s2)), float(np.sum(w * s2 * s6)), float(np.sum(w * s0 * s6))
    mono = float(np.sum(w * ((s0 == s2) & (s2 == s6))))
    return dict(c2=c2, c4=c4, c6=c6, P_mono=mono, facet_sum=c2 + c4 + c6, facet_twin=c2 - c4 - c6)

out = dict(X=X, eta=ETA, triples=int(len(n)))
out["real"] = stats(np.ones(len(n)))
out["Selberg counterfeit"] = stats((1 - s0 * s2) / 2)
out["mod-3 counterfeit"] = stats((1 - s0 * s2) * (1 - s2 * s6) / 4)
out["mono-free counterfeit, c4=c6=0 point"] = stats((1 - s0 * s2) / 2 * (1 + 0 * s6))
for k, v in out.items():
    print(k, v if not isinstance(v, dict) else {a: round(b, 4) for a, b in v.items()})
json.dump(out, open(f"stage23_polytope_{X:.0e}_eta{ETA}.json", "w"), indent=1)
