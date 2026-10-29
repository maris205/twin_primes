"""Stage 18: the absolute-value barrier at finite T.

Proposition 7.8 is proved for the Bohr mean; the proof transfers to the window [T, 2T] (smooth
weight) once T >> (2P)^8 ~ x^4, by exact orthogonality of monomials of degree <= 8.  Below
that the moment transfer fails.  Here we test numerically whether the barrier survives at
T ~ x = 4P^2, the smallest T at which the Mellin identity for the bilinear form is exact:
    R(c, T) = mean_{t in [T,2T]} |A(t)|^2 |C(t)| / k^2      (a = b = 1),
for c = lambda(r+2), random signs, c = 1, and an adversarial c found by gradient descent on
the phases (fresh t-samples for evaluation).

usage: python stage18_finite_T.py P samples steps
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

P = int(sys.argv[1]); N = int(sys.argv[2]); STEPS = int(sys.argv[3])
rng = np.random.default_rng(18)
pr = primes_upto(2 * P); pr = pr[pr >= P].astype(np.int64); k = len(pr)
iu = np.triu_indices(k)
r = (pr[iu[0]] * pr[iu[1]]).astype(np.int64)
XM = int(r.max()) + 3
om, _, _ = factor_info(1, XM + 1, primes_upto(int(XM ** 0.5) + 2))
lam = np.concatenate([[0], 1 - 2 * (om % 2)]).astype(float)
x = 4 * P * P
logp, logr = np.log(pr.astype(float)), np.log(r.astype(float))

def sample(T, n):
    t = rng.uniform(T, 2 * T, n)
    U = np.abs(np.exp(-1j * np.outer(t, logp)).sum(1)) ** 2
    M = np.exp(-1j * np.outer(t, logr))
    return U, M

def R(c, U, M):
    return float(np.mean(U * np.abs(M @ c))) / k ** 2

out = dict(P=P, k=k, S=len(r), x=x, samples=N, steps=STEPS, rows=[])
for mult in [0.25, 1, 4, 1e4]:
    T = mult * x
    Utr, Mtr = sample(T, N); Ute, Mte = sample(T, N)
    row = dict(T_over_x=mult,
               lam=R(lam[r + 2].astype(complex), Ute, Mte),
               rand=R(rng.choice([-1.0, 1.0], len(r)).astype(complex), Ute, Mte),
               one=R(np.ones(len(r), complex), Ute, Mte))
    best = None
    for restart in range(2):
        phi = 2 * np.pi * rng.random(len(r))
        for it in range(STEPS):
            c = np.exp(1j * phi)
            C = Mtr @ c
            w = Utr / np.maximum(np.abs(C), 1e-9)
            g = np.real((np.conj(C) * w) @ (1j * Mtr * c)) / N
            phi -= 0.5 * g / (np.abs(g).max() + 1e-12)
        v = R(np.exp(1j * phi), Ute, Mte)
        best = v if best is None else min(best, v)
    row["adversarial"] = best
    out["rows"].append(row)
    print(json.dumps(row), flush=True)
json.dump(out, open(f"stage18_finite_T_P{P}.json", "w"), indent=1)
