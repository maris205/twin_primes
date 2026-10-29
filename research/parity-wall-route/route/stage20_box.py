"""Stage 20: twin parity needs NON-EXTREMALITY, which absolute-value (box-norm) data can detect.

Matrix y(p,q) = lambda(pq+2) * 1[pq+2 is z-rough], p, q primes in [P,2P] (symmetric, k x k), N = #nonzero.
On GEH, by Theorem C, the twin parameter delta_x = 0 exactly when (asymptotically) every rough entry
is -1, i.e. sum y = -N.  Since |1^T y 1| <= k ||y||_op <= k ||y||_{S4} = k R4^{1/4},
    R4 = sum_{p1,p2,q1,q2} y(p1,q1) y(p1,q2) y(p2,q1) y(p2,q2) = trace((y y^T)^2),
the normalised box norm beta = k R4^{1/4} / N < 1 - eps excludes the extreme world.  R4 is the
rectangle (four-point) correlation, i.e. an absolute-value (fourth-moment) quantity: on the torus,
E|sum y(p,q) theta_p theta'_q|^4 = 2 (sum|y|^2)^2 + 2 R4 - (diagonal terms).

We compute beta and the top singular value for: the real lambda; the delta = 0 counterfeit
(-1 on the rough support; this is also what the mod-3 counterfeit of Remark 7.2 gives on this class);
a rank-one sign counterfeit u_p u_q on the support; and random signs on the support.

usage: python stage20_box.py P z
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

P = int(sys.argv[1]); ZR = float(sys.argv[2])
rng = np.random.default_rng(20)
pr = primes_upto(2 * P); pr = pr[pr >= P].astype(np.int64); k = len(pr)
R = np.outer(pr, pr)
XM = int(R.max()) + 3
om, _, spf = factor_info(1, XM + 1, primes_upto(int(XM ** 0.5) + 2))
lam = np.concatenate([[0], 1 - 2 * (om % 2)]).astype(float)
spf = np.concatenate([[0], spf])
supp = (spf[R + 2] >= ZR).astype(float)
N = supp.sum()
u = rng.choice([-1.0, 1.0], k)
worlds = {
    "real lambda(pq+2)": lam[R + 2] * supp,
    "delta=0 counterfeit (-1)": -supp,
    "rank-one signs u_p u_q": np.outer(u, u) * supp,
    "random signs": np.triu(rng.choice([-1.0, 1.0], (k, k)), 1),
}
w = worlds["random signs"]; worlds["random signs"] = (w + w.T + np.diag(rng.choice([-1.0, 1.0], k))) * supp
out = dict(P=P, z=ZR, k=k, N=int(N), support_fraction=float(N / k ** 2), worlds={})
for name, y in worlds.items():
    G = y @ y.T
    R4 = float(np.sum(G * G))
    s = np.linalg.svd(y, compute_uv=False)
    out["worlds"][name] = dict(sum_over_N=float(y.sum() / N), beta=float(k * R4 ** 0.25 / N),
                               sigma1_over_N_over_k=float(s[0] * k / N))
    print(f"{name:28s} sum/N={y.sum()/N:+.4f}  beta={k*R4**0.25/N:.4f}  sigma1*k/N={s[0]*k/N:.4f}")
json.dump(out, open(f"stage20_box_P{P}_z{int(ZR)}.json", "w"), indent=1)
