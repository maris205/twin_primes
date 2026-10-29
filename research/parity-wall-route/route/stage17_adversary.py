"""Stage 17: adversarial test of the absolute-value Mellin barrier.

By Kronecker-Weyl (log p linearly independent over Q), the long t-average of any continuous
function of (p^{-it})_p equals its average over the torus with independent uniform phases
theta_p (Steinhaus variables).  So for a = b = 1 on k primes,
    J(c) = lim_T mean_{[0,T]} |A(t)|^2 |C(t)| = E_theta |A(theta)|^2 |C(theta)|,
    A = sum_p theta_p,  C = sum_{p<=q} c(pq) theta_p theta_q.
The barrier proposition says J(c) >= kappa k^2 for EVERY unimodular c.  Here we try to make
J(c)/k^2 small by gradient descent on the phases of c (fresh samples for evaluation), and
compare with c = random signs and c = 1.

usage: python stage17_adversary.py k samples steps
"""
import sys, json, math
import numpy as np

k = int(sys.argv[1]); N = int(sys.argv[2]); STEPS = int(sys.argv[3])
rng = np.random.default_rng(17)
iu = np.triu_indices(k)                      # pairs p <= q  <->  r = pq
m = len(iu[0])

def sample(n):
    th = np.exp(2j * np.pi * rng.random((n, k)))
    A = th.sum(1)
    mono = th[:, iu[0]] * th[:, iu[1]]       # theta^r for r = pq
    return np.abs(A) ** 2, mono

def J(c, U, mono):
    return float(np.mean(U * np.abs(mono @ c))) / k ** 2

Utr, Mtr = sample(N)
Ute, Mte = sample(N)
out = dict(k=k, samples=N, steps=STEPS)
out["c=1"] = J(np.ones(m, complex), Ute, Mte)
out["c=random signs"] = J(rng.choice([-1.0, 1.0], m).astype(complex), Ute, Mte)

best = None
for restart in range(3):
    phi = 2 * np.pi * rng.random(m)
    lr = 0.5
    for it in range(STEPS):
        c = np.exp(1j * phi)
        C = Mtr @ c
        w = Utr / np.maximum(np.abs(C), 1e-9)
        # d|C|/dphi_r = Re(conj(C)/|C| * i c_r mono_r)
        g = np.real((np.conj(C) * w) @ (1j * Mtr * c)) / N
        phi -= lr * g / (np.abs(g).max() + 1e-12)
    val = J(np.exp(1j * phi), Ute, Mte)
    best = val if best is None else min(best, val)
out["adversarial min (phases)"] = best
print(json.dumps(out))
json.dump(out, open(f"stage17_adversary_k{k}.json", "w"), indent=1)
