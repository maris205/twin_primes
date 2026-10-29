"""Stage 21: averaged non-extremality = worst-case bilinear non-extremality.

Absolute-value data of the bilinear Steinhaus form G = sum y(p,q) theta_p theta'_q are invariant under
y -> D_u y D_v (|u_p| = |v_q| = 1).  So an absolute-value certificate of |sum y| <= (1-eps) N must also
certify |sum u_p v_q y(p,q)| <= (1-eps) N for all signs u, v, i.e. it must bound the
infinity->1 (cut-type) norm  ||y||_{inf->1} = max_{u,v in {+-1}} u^T y v.
We estimate ||y||_{inf->1} / N by alternating sign maximisation (lower bound, many restarts) for:
the real lambda(pq+2) on rough pq+2, the delta = 0 counterfeit, a rank-one sign counterfeit (sum ~ 0),
and random signs; and report sum y / N and the spectral ratio sigma1 k / N.

usage: python stage21_cutnorm.py P z restarts
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

P = int(sys.argv[1]); ZR = float(sys.argv[2]); RS = int(sys.argv[3])
rng = np.random.default_rng(21)
pr = primes_upto(2 * P); pr = pr[pr >= P].astype(np.int64); k = len(pr)
R = np.outer(pr, pr)
XM = int(R.max()) + 3
om, _, spf = factor_info(1, XM + 1, primes_upto(int(XM ** 0.5) + 2))
lam = np.concatenate([[0], 1 - 2 * (om % 2)]).astype(float)
spf = np.concatenate([[0], spf])
supp = (spf[R + 2] >= ZR).astype(float)
N = supp.sum()
u0 = rng.choice([-1.0, 1.0], k)
rs = np.triu(rng.choice([-1.0, 1.0], (k, k)), 1)
worlds = {"real lambda(pq+2)": lam[R + 2] * supp, "delta=0 counterfeit": -supp,
          "rank-one signs": np.outer(u0, u0) * supp, "random signs": (rs + rs.T + np.diag(rng.choice([-1.0, 1.0], k))) * supp}

def cut_lower(y):
    best = -1e18
    for _ in range(RS):
        u = rng.choice([-1.0, 1.0], k)
        for _ in range(50):
            v = np.sign(y.T @ u); v[v == 0] = 1
            u2 = np.sign(y @ v); u2[u2 == 0] = 1
            if np.array_equal(u2, u):
                break
            u = u2
        best = max(best, float(u @ y @ v))
    return best

out = dict(P=P, z=ZR, k=k, N=int(N), restarts=RS, worlds={})
for name, y in worlds.items():
    c = cut_lower(y)
    s1 = float(np.linalg.svd(y, compute_uv=False)[0])
    out["worlds"][name] = dict(sum_over_N=float(y.sum() / N), cut_over_N=c / N, sigma1_k_over_N=s1 * k / N)
    print(f"{name:22s} sum/N={y.sum()/N:+.4f}  cut/N>={c/N:.4f}  sigma1*k/N={s1*k/N:.4f}", flush=True)
json.dump(out, open(f"stage21_cutnorm_P{P}_z{int(ZR)}.json", "w"), indent=1)
