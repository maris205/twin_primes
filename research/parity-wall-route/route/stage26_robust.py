"""Stage 26b: robustness (soundness) of the rough-pair parity code.

Equations: for each x^eta-rough pair (n, n+2), sum_{p^a || n(n+2), a odd} x_p = 1 over GF(2).
Codewords on the core are chi_3 and chi_4.  Robust rigidity would say: a completely multiplicative f at
weighted distance d from both chi_3 and chi_4 violates >= c*d of the equations.  lambda (f = -1 on primes)
is at weighted distance ~1/2 from both and violates ~1/2 of the equations.

Starting from f = chi_4 we flip primes in three orders and record (distance to {chi_3, chi_4}, violated
fraction):  random order;  greedy "cheap" order (primes in the fewest equations first, i.e. large primes);
and an adaptive greedy that at each step flips the prime with the smallest increase in violations.
Distances use the weight 1/p on primes in [z, X] (the pretentious-distance weight).

usage: python stage26_robust.py X eta
"""
import sys, json, math
import numpy as np
from collections import defaultdict
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); ETA = float(sys.argv[2])
rng = np.random.default_rng(26)
Z = X ** ETA
om, _, spf = factor_info(1, X + 4, primes_upto(int((X + 4) ** 0.5) + 1))
spf = np.concatenate([[0], spf]); lam = np.concatenate([[0], 1 - 2 * (om % 2)])
pairs = [n for n in range(3, X + 1) if spf[n] >= Z and spf[n + 2] >= Z]

def fac(n):
    d = defaultdict(int)
    while n > 1:
        p = int(spf[n]); d[p] += 1; n //= p
    return d
eqs = []
for n in pairs:
    d = fac(n)
    for p, a in fac(n + 2).items(): d[p] += a
    eqs.append([p for p, a in d.items() if a % 2])
primes = sorted(set(p for e in eqs for p in e)); pi = {p: i for i, p in enumerate(primes)}
E = len(eqs); P = len(primes)
inc = defaultdict(list)
for j, e in enumerate(eqs):
    for p in e: inc[pi[p]].append(j)
allp = [int(p) for p in primes_upto(X) if p >= Z]
W = sum(1 / p for p in allp)
chi3 = np.array([1 if p % 3 == 1 else -1 for p in primes]); chi4 = np.array([1 if p % 4 == 1 else -1 for p in primes])
w = np.array([1 / p for p in primes])

def status(f):
    viol = np.array([np.prod(f[[pi[p] for p in e]]) != -1 for e in eqs])
    d3 = float(np.sum(w * (f != chi3)) / W); d4 = float(np.sum(w * (f != chi4)) / W)
    return float(viol.mean()), min(d3, d4)

lamf = -np.ones(P, int)
out = dict(X=X, eta=ETA, rough_pairs=E, primes=P, weight_share_of_equation_primes=float(w.sum() / W),
           lambda_liouville=dict(zip(["violated", "distance"], status(lamf))), curves={})
def curve(order_fn, name, steps=40):
    f = chi4.copy(); viol = np.array([False] * E); pts = []
    order = order_fn()
    chunk = max(1, len(order) // steps)
    for k in range(0, len(order), chunk):
        for i in order[k:k + chunk]:
            f[i] = -f[i]
            for j in inc[i]: viol[j] = not viol[j]
        d3 = float(np.sum(w * (f != chi3)) / W); d4 = float(np.sum(w * (f != chi4)) / W)
        pts.append((round(min(d3, d4), 4), round(float(viol.mean()), 4)))
    out["curves"][name] = pts
    print(name, pts[:: max(1, len(pts) // 10)], flush=True)

curve(lambda: list(rng.permutation(P)), "random order")
curve(lambda: sorted(range(P), key=lambda i: (len(inc[i]), -primes[i])), "cheap primes first")
# adaptive greedy: flip the prime with the fewest currently satisfied incident equations (net increase)
def adaptive():
    f = chi4.copy(); viol = np.zeros(E, bool); done = np.zeros(P, bool); order = []
    for _ in range(P):
        best, bi = None, None
        cand = rng.choice(np.nonzero(~done)[0], size=min(400, int((~done).sum())), replace=False)
        for i in cand:
            delta = sum(-1 if viol[j] else 1 for j in inc[i])
            score = delta / (w[i] * 1e6)
            if best is None or score < best: best, bi = score, i
        done[bi] = True; order.append(bi)
        for j in inc[bi]: viol[j] = not viol[j]
    return order
curve(adaptive, "adaptive greedy (sampled)")
json.dump(out, open(f"stage26_robust_{X:.0e}_eta{ETA}.json", "w"), indent=1)
print("lambda:", out["lambda_liouville"], "equation-prime weight share:", round(out["weight_share_of_equation_primes"], 4))
