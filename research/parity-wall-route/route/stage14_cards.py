"""Stage 14: fast falsification tests for cards that try to give structure to the
bilinear form  B(a,b) = sum_{m~P} sum_{n~P} a_m b_n lambda(mn+2)  (m, n primes).

H18 (spectral / low rank): the matrix A[m,n] = lambda(mn+2) has a large structured component.
     Test: singular values of A against random +-1 matrices of the same shape (null), with
     positive controls lambda(mn) = lambda(m)lambda(n) (rank 1) and chi_5(mn+2) (rank <= 5),
     and a planted control A + 0.15 * (rank-one sign pattern).
H17 (dispersion): after Cauchy-Schwarz in m, the inner sums C(n1,n2) = sum_m lambda(n1 m+2)
     lambda(n2 m+2) carry a bias in their average over pairs n1 != n2.
     Test: mean of C over pairs, as a z-score against the pairwise spread.
H21 (local pretentious model, "Siegel world"): lambda(mn+2) correlates with chi(mn+2) for
     some character chi of small modulus.  Test: max over primitive real and complex chars
     mod q <= 60, against the random-model threshold, with a Siegel-world fake (lambda replaced
     by chi_{-4} on half the entries) as positive control.
H23 (Mellin / multiplicative Hankel): Type II for c(r) = lambda(r+2) is equivalent to the
     absence of large values of C(t) = sum_{r<=x} lambda(r+2) r^{-it}.  Test: max |C(t)|/sqrt(x)
     over a grid of t in [x^{1/2}, x] against a random +-1 sequence, lambda(r) itself, and a
     planted control lambda(r+2) + 0.05 cos(t0 log r).

usage: python stage14_cards.py P xC
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

P = int(float(sys.argv[1])); XC = int(float(sys.argv[2]))
XMAX = max(4 * P * P + 3, XC + 3)
rng = np.random.default_rng(14)
t0 = time.time()
plist = primes_upto(int(XMAX ** 0.5) + 2)
lam = np.empty(XMAX + 1, np.int8)
SEG = 10_000_000
for a in range(1, XMAX + 1, SEG):
    b = min(a + SEG, XMAX + 1)
    om, _, _ = factor_info(a, b, plist)
    lam[a:b] = 1 - 2 * (om % 2)
print(f"lambda to {XMAX:.2e}: {time.time()-t0:.0f}s", flush=True)
out = dict(P=P, xC=XC)

pr = primes_upto(2 * P); pr = pr[pr >= P].astype(np.int64)
k = len(pr)
MN = np.outer(pr, pr)
A = lam[MN + 2].astype(np.float64)
out["matrix"] = k

def chi_table(q):
    """All Dirichlet characters mod prime-power-free small q via a generator (q prime only)."""
    g = next(g for g in range(2, q) if all(pow(g, (q - 1) // f, q) != 1 for f in range(2, q) if (q - 1) % f == 0 and all(f % d for d in range(2, int(f ** .5) + 1))))
    ind = np.zeros(q, np.int64); x = 1
    for e in range(q - 1):
        ind[x] = e; x = x * g % q
    return [(j, np.where(np.arange(q) % q == 0, 0, np.exp(2j * np.pi * j * ind / (q - 1)))) for j in range(1, q - 1)]

# ---- H18: singular values ----
def top_sv(M_, r=3):
    s = np.linalg.svd(M_, compute_uv=False)
    return s[:r] / math.sqrt(M_.shape[0] * M_.shape[1])
null = np.array([top_sv(rng.choice([-1.0, 1.0], size=A.shape))[0] for _ in range(20)])
chi5 = np.array([0, 1, -1, -1, 1], float)        # Legendre symbol mod 5
u = rng.choice([-1.0, 1.0], size=k); v = rng.choice([-1.0, 1.0], size=k)
res18 = dict(
    A=top_sv(A).tolist(),
    null_mean=float(null.mean()), null_max=float(null.max()), edge=2 / math.sqrt(k),
    ctrl_rank1=top_sv(lam[MN].astype(float))[:1].tolist(),
    ctrl_chi5=top_sv(chi5[(MN + 2) % 5])[:1].tolist(),
    ctrl_planted=top_sv(A + 0.15 * np.outer(u, v))[:1].tolist())
out["H18"] = res18
print("H18", json.dumps(res18), flush=True)

# ---- H17: dispersion inner sums over all m <= Mlen ----
Mlen = (XMAX - 3) // (2 * P)
mm = np.arange(1, Mlen + 1, dtype=np.int64)
sub = pr[:min(k, 120)]
rows = np.array([lam[n * mm + 2] for n in sub], dtype=np.float64)   # |sub| x Mlen
G = rows @ rows.T / Mlen
iu = np.triu_indices(len(sub), 1)
cvals = G[iu]
z17 = cvals.mean() / (cvals.std() / math.sqrt(len(cvals)))
res17 = dict(pairs=len(cvals), Mlen=int(Mlen), mean=float(cvals.mean()), sd=float(cvals.std()),
             random_sd=1 / math.sqrt(Mlen), z=float(z17))
# positive control: plant lambda(n m + 2) -> chi_{-4}(m) on half the rows' entries
chi4 = np.array([0, 1, 0, -1], float)[mm % 4]
rows_c = np.where(rng.random(rows.shape) < 0.5, rows, chi4)
Gc = rows_c @ rows_c.T / Mlen
res17["ctrl_mean"] = float(Gc[iu].mean())
res17["ctrl_z"] = float(Gc[iu].mean() / (Gc[iu].std() / math.sqrt(len(cvals))))
out["H17"] = res17
print("H17", json.dumps(res17), flush=True)

# ---- H21: characters of small prime modulus ----
vals = (MN + 2).ravel(); L = A.ravel()
best = (0.0, None)
nchar = 0
for q in [p for p in primes_upto(60) if p >= 3]:
    for j, tab in chi_table(int(q)):
        c = abs(np.mean(L * tab[vals % q])); nchar += 1
        if c > best[0]:
            best = (float(c), (int(q), j))
thr = math.sqrt(2 * math.log(4 * nchar) / len(L))
fake = np.where(rng.random(L.shape) < 0.5, L, np.array([0, 1, 0, -1], float)[vals % 4])
res21 = dict(chars=nchar, max_corr=best[0], at=best[1], threshold=thr,
             ctrl_corr_chi4=float(abs(np.mean(fake * np.array([0, 1, 0, -1], float)[vals % 4]))))
out["H21"] = res21
print("H21", json.dumps(res21), flush=True)

# ---- H23: large values of the shifted Dirichlet polynomial ----
r = np.arange(1, XC + 1, dtype=np.int64)
logr = np.log(r.astype(np.float64))
ranges = {"low t in [x^0.5, x^0.75]": (0.5, 0.75), "high t in [x/10, x]": (math.log(XC / 10) / math.log(XC), 1.0)}
seqs = {
    "lambda(r+2)": lam[r + 2].astype(np.float64),
    "lambda(r)": lam[r].astype(np.float64),
    "random": rng.choice([-1.0, 1.0], size=XC),
}
res23 = {}
for rname, (a_, b_) in ranges.items():
    ts = np.exp(rng.uniform(a_ * math.log(XC), b_ * math.log(XC), 300))
    tp = float(ts[123])
    cur = dict(seqs); cur["planted"] = seqs["lambda(r+2)"] + 0.05 * np.cos(tp * logr)
    mags = {}
    for name, c in cur.items():
        mg = np.empty(len(ts))
        for i, t in enumerate(ts):
            mg[i] = abs(np.sum(c * np.exp(-1j * t * logr)))
        mags[name] = mg / math.sqrt(XC)
    rr = {name: dict(max=float(m.max()), rms=float(math.sqrt((m ** 2).mean()))) for name, m in mags.items()}
    rr["corr |C| shifted vs unshifted"] = float(np.corrcoef(mags["lambda(r+2)"], mags["lambda(r)"])[0, 1])
    rr["planted at t"] = float(mags["planted"][123])
    res23[rname] = rr
out["H23"] = res23
print("H23", json.dumps(res23), flush=True)

json.dump(out, open("stage14_cards.json", "w"), indent=1)
print(f"done {time.time()-t0:.0f}s")
