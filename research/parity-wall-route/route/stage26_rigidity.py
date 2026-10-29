"""Stage 26: is there a twin rigidity theorem?  Multiplicative counterfeits by GF(2) peeling.

Question: if a completely multiplicative f: primes -> {+-1} satisfies f(n) f(n+2) = -1 on (almost) all
x^eta-rough pairs (n, n+2), must f pretend to be chi_3 or chi_4?
Writing f(p) = (-1)^{x_p}, the condition is a linear system over GF(2):
    sum_{p^a || n(n+2)} a * x_p = 1   (one equation per rough pair).
chi_3 and chi_4 are solutions, so the system is consistent.  We solve it by peeling (repeatedly use a
variable that occurs in exactly one remaining equation), assign all other primes at random, and check:
  - every rough pair satisfies f(n) f(n+2) = -1;
  - the weighted agreement of f with lambda, chi_3, chi_4 on primes in [z, X]:
        A(f, g) = sum (1/p) f(p) g(p) / sum 1/p,   D^2(f, g) = sum (1 - f(p) g(p)) / p.
If peeling succeeds with many free primes, extremal multiplicative functions far from every character
exist, and no rigidity theorem of the form "extremal => pretends to be a character" can hold on rough
support.

usage: python stage26_rigidity.py X eta seed
"""
import sys, json, math
import numpy as np
from collections import defaultdict
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); ETA = float(sys.argv[2]); SEED = int(sys.argv[3])
rng = np.random.default_rng(SEED)
Z = X ** ETA
om, _, spf = factor_info(1, X + 4, primes_upto(int((X + 4) ** 0.5) + 1))
spf = np.concatenate([[0], spf]); lam = np.concatenate([[0], 1 - 2 * (om % 2)])
rough = spf >= Z
pairs = [n for n in range(3, X + 1) if rough[n] and rough[n + 2]]

def factor(n):
    out = defaultdict(int)
    while n > 1:
        p = int(spf[n]) if spf[n] <= n else n
        if p > n: p = n
        out[p] += 1
        n //= p
    return out

eqs = []
for n in pairs:
    d = defaultdict(int)
    for p, a in factor(n).items(): d[p] += a
    for p, a in factor(n + 2).items(): d[p] += a
    eqs.append(frozenset(p for p, a in d.items() if a % 2))
primes = sorted(set(p for e in eqs for p in e))
occ = defaultdict(set)
for i, e in enumerate(eqs):
    for p in e: occ[p].add(i)
# peeling
alive = set(range(len(eqs))); deg = {p: len(occ[p]) for p in primes}
stack = [p for p in primes if deg[p] == 1]; order = []
while stack:
    p = stack.pop()
    if deg[p] != 1: continue
    i = next(iter(occ[p] & alive))
    order.append((p, i)); alive.discard(i)
    for q in eqs[i]:
        deg[q] -= 1
        if deg[q] == 1: stack.append(q)
peeled_ok = len(alive) == 0
# solve the remaining 2-core by Gaussian elimination over GF(2) (rows as Python int bitsets)
core = sorted(alive)
corevars = sorted(set(q for i in core for q in eqs[i]) - set(p for p, _ in order))
vidx = {q: j for j, q in enumerate(corevars)}
peeledset = set(p for p, _ in order)
x = {p: int(rng.integers(0, 2)) for p in primes}
rows = []
for i in core:
    m = 0; rhs = 1
    for q in eqs[i]:
        if q in vidx: m |= 1 << vidx[q]
    rows.append([m, rhs])
# peeled variables do not occur in core equations (they were removed with their equations)
piv = {}
for r in rows:
    m, b = r
    for j, (pm, pb) in piv.items():
        if m >> j & 1: m ^= pm; b ^= pb
    if m == 0:
        if b: raise SystemExit("inconsistent core")
        continue
    j = m.bit_length() - 1
    for k in list(piv):
        pm, pb = piv[k]
        if pm >> j & 1: piv[k] = (pm ^ m, pb ^ b)
    piv[j] = (m, b)
free_core = [j for j in range(len(corevars)) if j not in piv]
val = {j: int(rng.integers(0, 2)) for j in free_core}
for j in sorted(piv):
    m, b = piv[j]
    s_ = b
    mm = m & ~(1 << j)
    while mm:
        t = mm & -mm; k = t.bit_length() - 1; s_ ^= val.get(k, 0); mm ^= t
    val[j] = s_
for q, j in vidx.items(): x[q] = val[j]
core_info = dict(core_equations=len(core), core_vars=len(corevars), core_rank=len(piv), core_free=len(free_core))
for p, i in reversed(order):
    s = sum(x[q] for q in eqs[i] if q != p) % 2
    x[p] = (1 - s) % 2
f = {p: 1 - 2 * x[p] for p in primes}
sat = float(np.mean([np.prod([f[p] for p in e]) == -1 for e in eqs]))
chi3 = lambda p: 0 if p % 3 == 0 else (1 if p % 3 == 1 else -1)
chi4 = lambda p: 0 if p % 2 == 0 else (1 if p % 4 == 1 else -1)
allp = [int(p) for p in primes_upto(X) if p >= Z]
w = np.array([1 / p for p in allp]); W = w.sum()
fv = np.array([f.get(p, 1 - 2 * int(rng.integers(0, 2))) for p in allp])
def agree(g): return float(np.sum(w * fv * np.array([g(p) for p in allp])) / W)
def D2(g): return float(np.sum(w * (1 - fv * np.array([g(p) for p in allp]))))
res = dict(X=X, eta=ETA, seed=SEED, rough_pairs=len(eqs), primes_in_equations=len(primes),
           peeled=len(order), free_primes=len(primes) - len(order), peeling_complete=peeled_ok, core=core_info,
           fraction_pairs_extremal=sat,
           agreement=dict(lam=agree(lambda p: -1), chi3=agree(chi3), chi4=agree(chi4)),
           D2=dict(lam=D2(lambda p: -1), chi3=D2(chi3), chi4=D2(chi4)), D2_scale_log1_eta=math.log(1 / ETA),
           lambda_pairs_mean=float(np.mean([lam[n] * lam[n + 2] for n in pairs])))
print(json.dumps(res, indent=1))
json.dump(res, open(f"stage26_rigidity_{X:.0e}_eta{ETA}_s{SEED}.json", "w"), indent=1)
