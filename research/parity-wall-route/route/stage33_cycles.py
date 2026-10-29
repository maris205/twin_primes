"""Stage 33: are the rough induced divisibility graphs locally tree-like, like a random vertex sample?

Full graph on n in (N, 2N]: n ~ n + 2d when d | n, d in D = z-rough integers in [z, Dmax].
Vertex sets: all n (full), z-rough n (rough), and a uniformly random subset with the same size as the rough
set (random).  For each induced graph we count edges, mean and max degree, 4-cycles (exactly, by 2-path
co-degrees) and 6-cycles (simple cycles through sampled start vertices).  If roughness were independent of
the cycle structure, the rough counts would equal pi^l times the full counts (pi = |rough| / |all|), as for the
random subset.  The ratio rough / (pi^l full) measures the arithmetic correlation between roughness and cycles.

usage: python stage33_cycles.py N z Dmax samples
"""
import sys, json, math
import numpy as np
from collections import defaultdict
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

N = int(float(sys.argv[1])); Z = int(sys.argv[2]); DMAX = int(float(sys.argv[3])); SMP = int(sys.argv[4])
rng = np.random.default_rng(33)
lo, hi = N + 1, 2 * N + 1
_, _, spf = factor_info(lo, hi, primes_upto(int(hi ** 0.5) + 1))
_, _, sd = factor_info(1, DMAX + 1, primes_upto(int(DMAX ** 0.5) + 1))
D = [d for d in range(Z, DMAX + 1) if sd[d - 1] >= Z]
V = sum(1 / d for d in D)
rough = set(int(lo + i) for i in np.nonzero(spf >= Z)[0])
allv = set(range(lo, hi))
randv = set(int(x) for x in rng.choice(np.arange(lo, hi), size=len(rough), replace=False))

def build(S):
    adj = defaultdict(list)
    for d in D:
        for n in range(((lo + d - 1) // d) * d, hi - 2 * d, d):
            m = n + 2 * d
            if n in S and m in S:
                adj[n].append(m); adj[m].append(n)
    return adj

def stats(S, adj):
    deg = np.array([len(adj[v]) for v in S]) if S else np.zeros(1)
    paths = defaultdict(int)
    for u, nb in adj.items():
        for i in range(len(nb)):
            for j in range(i + 1, len(nb)):
                a, b = nb[i], nb[j]
                paths[(a, b) if a < b else (b, a)] += 1
    c4 = sum(c * (c - 1) // 2 for c in paths.values()) / 2
    verts = list(adj.keys())
    starts = [verts[i] for i in rng.choice(len(verts), size=min(SMP, len(verts)), replace=False)] if verts else []
    c6 = 0
    for s in starts:
        stack = [(s, (s,))]
        while stack:
            v, path = stack.pop()
            for w in adj[v]:
                if len(path) == 6:
                    if w == s: c6 += 1
                elif w not in path:
                    stack.append((w, path + (w,)))
    c6_per_vertex = c6 / 2 / max(1, len(starts)) * len(verts) / max(1, len(S))   # cycles through a vertex of S
    return dict(vertices=len(S), edges=int(deg.sum() // 2), mean_deg=float(deg.mean()), max_deg=int(deg.max()),
                c4_total=c4, c4_per_vertex=c4 * 4 / len(S), c6_per_vertex=c6_per_vertex)

out = dict(N=N, z=Z, Dmax=DMAX, dilators=len(D), V=V)
for name, S in (("full", allv), ("rough", rough), ("random", randv)):
    out[name] = stats(S, build(S)); print(name, out[name], flush=True)
pi = len(rough) / len(allv)
out["pi"] = pi
for l, key in ((4, "c4_per_vertex"), (6, "c6_per_vertex")):
    pred = pi ** (l - 1) * out["full"][key]              # per-vertex: a cycle through v survives w.p. pi^(l-1)
    out[f"rough_over_pred_c{l}"] = out["rough"][key] / pred if pred else None
    out[f"random_over_pred_c{l}"] = out["random"][key] / pred if pred else None
print({k: out[k] for k in out if k.endswith(("c4", "c6")) or k == "pi"})
with open("stage33_cycles.jsonl", "a") as fh: fh.write(json.dumps(out) + "\n")
