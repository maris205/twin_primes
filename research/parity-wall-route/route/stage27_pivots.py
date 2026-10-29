"""Stage 27: where does a proof of exact rigidity need parity?  Triangular (pivot) structure of the
rough-pair parity system.

Equations as in stage 26: for each x^eta-rough pair (n, n+2), the set of primes with odd exponent in n(n+2).
A triangular proof of "rank = #vars - 1" orders the primes and needs, for every prime q except one, an
equation whose extreme prime (largest, or smallest) is q.  We measure:
  - which primes are max-pivots / min-pivots, by layer theta = log q / log X;
  - the bottom layer: pairs whose primes all lie in [z, z^(1+eps)] (Omega is nearly fixed by size, so these
    pairs are almost all lambda(n) lambda(n+2) = +1, i.e. even class);
  - the top layer: pairs whose primes are all >= X^theta (almost-prime twins);
  - the true rank (peeling + GF(2) elimination on the 2-core) against the triangular lower bounds.

usage: python stage27_pivots.py X eta [lo]   (pairs with lo*X < n <= X; default lo=0)
"""
import sys, json, math
import numpy as np
from collections import defaultdict, Counter
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); ETA = float(sys.argv[2]); LO = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
Z = X ** ETA
om, _, spf = factor_info(1, X + 4, primes_upto(int((X + 4) ** 0.5) + 1))
spf = np.concatenate([[0], spf]); om = np.concatenate([[0], om])
pairs = [n for n in range(max(3, int(LO * X) + 1), X + 1) if spf[n] >= Z and spf[n + 2] >= Z]

def fac(n):
    d = defaultdict(int)
    while n > 1:
        p = int(spf[n]) if spf[n] <= n else n
        d[p] += 1; n //= p
    return d
eqs, allp_of, lamlam = [], [], []
for n in pairs:
    a, b = fac(n), fac(n + 2)
    d = defaultdict(int)
    for p, e in a.items(): d[p] += e
    for p, e in b.items(): d[p] += e
    eqs.append(sorted(p for p, e in d.items() if e % 2))
    allp_of.append(sorted(set(a) | set(b)))
    lamlam.append(1 - 2 * ((int(om[n]) + int(om[n + 2])) % 2))
primes = sorted(set(p for e in eqs for p in e))
E, P = len(eqs), len(primes)
theta = lambda q: math.log(q) / math.log(X)

maxpiv = Counter(e[-1] for e in eqs if e); minpiv = Counter(e[0] for e in eqs if e)
bins = [ETA, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0001]
layer = []
for lo, hi in zip(bins, bins[1:]):
    qs = [q for q in primes if lo <= theta(q) < hi]
    if not qs: continue
    layer.append(dict(theta=[round(lo, 3), round(hi, 3)], primes=len(qs),
                      max_pivots=sum(1 for q in qs if maxpiv[q]), min_pivots=sum(1 for q in qs if minpiv[q])))
non_max = [q for q in primes if not maxpiv[q]]
non_min = [q for q in primes if not minpiv[q]]

def window(lo, hi):
    sel = [i for i in range(E) if all(lo <= p <= hi for p in allp_of[i])]
    if not sel: return dict(pairs=0)
    return dict(pairs=len(sel), even_class_fraction=float(np.mean([lamlam[i] == 1 for i in sel])),
                examples=[(pairs[i], pairs[i] + 2) for i in sel[:5]])
bottom = {f"[z, z^{1 + eps}]": window(Z, Z ** (1 + eps)) for eps in (0.25, 0.5, 1.0)}
top = {f"all primes >= X^{t}": window(X ** t, X) for t in (0.3, 0.35, 0.4, 0.45)}

# true rank: peeling + elimination on the 2-core
occ = defaultdict(set)
for i, e in enumerate(eqs):
    for p in e: occ[p].add(i)
alive = set(range(E)); deg = {p: len(occ[p]) for p in primes}
stack = [p for p in primes if deg[p] == 1]; peeled = 0; peeled_vars = set()
while stack:
    p = stack.pop()
    if deg[p] != 1: continue
    i = next(iter(occ[p] & alive)); alive.discard(i); peeled += 1; peeled_vars.add(p)
    for q in eqs[i]:
        deg[q] -= 1
        if deg[q] == 1: stack.append(q)
core = sorted(alive)
corevars = sorted(set(q for i in core for q in eqs[i]))
vidx = {q: j for j, q in enumerate(corevars)}
piv = {}
for i in core:
    m = 0
    for q in eqs[i]: m |= 1 << vidx[q]
    while m:
        j = m.bit_length() - 1
        if j in piv: m ^= piv[j]
        else: piv[j] = m; break
orphans = P - peeled - len(corevars)
rank = peeled + len(piv)
out = dict(X=X, eta=ETA, lo=LO, z=Z, rough_pairs=E, primes=P, rank=rank, nullity=P - rank,
           core_vars=len(corevars), core_nullity=len(corevars) - len(piv), orphans=orphans,
           max_pivot_bound=len(maxpiv), min_pivot_bound=len(minpiv),
           core_theta_range=[round(theta(corevars[0]), 3), round(theta(corevars[-1]), 3)] if corevars else None,
           smallest_non_max_pivots=non_max[:12], non_max_pivot_count=len(non_max),
           largest_non_min_pivots=non_min[-8:], non_min_pivot_count=len(non_min),
           layers=layer, bottom=bottom, top=top,
           even_class_fraction_all=float(np.mean([v == 1 for v in lamlam])))
print(json.dumps(out, indent=1))
json.dump(out, open(f"stage27_pivots_{X:.0e}_eta{ETA}_lo{LO}.json", "w"), indent=1)
