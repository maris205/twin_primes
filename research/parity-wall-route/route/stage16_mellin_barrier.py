"""Stage 16: does the multiplicative Sidon property of the primes help the twin bilinear form?

Setting (stage 14):  B(a,b) = sum_{p,q in [P,2P]} a_p b_q c(pq),  c(r) = lambda(r+2).
Mellin:  B = lim_T  mean_{t in [0,T]}  A(t) B_(t) conj(C(t)),
         A(t) = sum_p a_p p^{-it},  C(t) = sum_{r in supp} c(r) r^{-it}  (supp = products pq).
Any argument that uses only |A|, |B_|, |C| (moments, large values, Lambda(p)/Sidon bounds)
can at best prove |B| <= mean_t |A||B_||C|.  We estimate that "absolute Mellin bound" by Monte
Carlo over t and compare with the true |B| and the trivial bound sum|a||b|.

Also checks the Sidon/Lambda(4) property: mean |A|^4 = 2k^2 - k exactly for primes as T -> oo
(unique factorization), versus the integers.

usage: python stage16_mellin_barrier.py P samples
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

P = int(sys.argv[1]); S = int(float(sys.argv[2]))
rng = np.random.default_rng(16)
t0 = time.time()
XM = 4 * P * P + 3
om, _, _ = factor_info(1, XM + 1, primes_upto(int(XM ** 0.5) + 2))
lam = np.concatenate([[0], 1 - 2 * (om % 2)]).astype(np.float64)    # lam[n] for n >= 1
pr = primes_upto(2 * P); pr = pr[pr >= P].astype(np.int64); k = len(pr)
ints = np.arange(P, 2 * P + 1, dtype=np.int64)

def run(name, a, b, cfun):
    # d(r) = sum_{pq=r} a_p b_q on the support of products
    prod = np.outer(pr, pr).ravel(); w = np.outer(a, b).ravel()
    r, inv = np.unique(prod, return_inverse=True)
    d = np.bincount(inv, weights=w)
    c = cfun(r)
    B_true = float(np.sum(d * c))
    trivial = float(np.sum(np.abs(a)) * np.sum(np.abs(b)))
    logp, logr = np.log(pr.astype(float)), np.log(r.astype(float))
    acc_abs = 0.0; acc_par = 0.0 + 0.0j; acc_A4 = 0.0
    CH = 1000
    for s in range(0, S, CH):
        t = rng.uniform(0, 1e9, size=min(CH, S - s))
        Ep = np.exp(-1j * np.outer(t, logp))
        A = Ep @ a; Bv = Ep @ b
        C = np.exp(-1j * np.outer(t, logr)) @ c
        acc_abs += np.sum(np.abs(A) * np.abs(Bv) * np.abs(C))
        acc_par += np.sum(A * Bv * np.conj(C))
        acc_A4 += np.sum(np.abs(Ep @ np.ones(k)) ** 4)
    res = dict(B_true=B_true, trivial=trivial, ratio_true=abs(B_true) / trivial,
               abs_mellin=acc_abs / S, ratio_abs_mellin=acc_abs / S / trivial,
               parseval_check=float((acc_par / S).real),
               A4_over_2k2=float(acc_A4 / S / (2 * k * k - k)))
    print(name, json.dumps(res), flush=True)
    return res

out = dict(P=P, k=k, samples=S)
one = np.ones(k); sgn = rng.choice([-1.0, 1.0], size=k); sgn2 = rng.choice([-1.0, 1.0], size=k)
twin = lambda r: lam[r + 2]
rand_c = {}
def randc(r):
    return rng.choice([-1.0, 1.0], size=len(r))
out["lambda(r+2), a=b=1"] = run("lambda(r+2), a=b=1", one, one, twin)
out["lambda(r+2), random signs"] = run("lambda(r+2), random signs", sgn, sgn2, twin)
out["random c, a=b=1"] = run("random c, a=b=1", one, one, randc)
# integers for comparison: Lambda(4) constant of {log n}
logn = np.log(ints.astype(float)); acc = 0.0; S2 = 20000
for s in range(0, S2, 1000):
    t = rng.uniform(0, 1e9, size=1000)
    acc += np.sum(np.abs(np.exp(-1j * np.outer(t, logn)).sum(1)) ** 4)
n = len(ints)
out["integers mean|D|^4 / (2n^2-n)"] = float(acc / S2 / (2 * n * n - n))
print("integers mean|D|^4/(2n^2-n)", out["integers mean|D|^4 / (2n^2-n)"])
json.dump(out, open("stage16_mellin_barrier.json", "w"), indent=1)
print(f"done {time.time()-t0:.0f}s")
