"""Stage 19: phase cards for the twin bilinear form  sum a_p b_q lambda(pq+2)  (p, q primes in [P,2P]).

Proposition 7.8 shows that absolute-value arguments cannot give its Type II bound, so a route must
supply PHASE information: a structured function phi(p,q) correlated with y(p,q) = lambda(pq+2).
Each card proposes a family of phases; the test is the maximal normalised correlation over the
family against a Bonferroni threshold, with a planted positive control (y replaced by phi on a
random half of the entries).

H24  bilinear Legendre phases:  (p|q), (q|p), (-1)^{(p-1)(q-1)/4}, (2|p)(2|q), (p|q)(q+2|p)
H26  characters of large prime modulus Q <= Qmax evaluated at pq+2 (all chars, via FFT over classes)
H27  the Gaussian subfamily: mean of y on {pq+2 = x^2+y^2} versus its complement
H28  additive and quadratic phases e(alpha r), e(alpha r^2), r = pq, alpha = j/4096
H29  hybrid characters chi(r) r^{-i tau} (chi mod Q <= 61, tau on a grid up to 4P^2): the local,
     unconditional version of the Siegel-world mechanism (class 6)

usage: python stage19_phase_cards.py P Qmax [z]
   z > 1: keep only pairs with pq+2 z-rough (Theorem C setting); one-point baselines are reported for H24, H27.
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

P = int(sys.argv[1]); QMAX = int(sys.argv[2]); ZR = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
rng = np.random.default_rng(19)
pr = primes_upto(2 * P); pr = pr[pr >= P].astype(np.int64); k = len(pr)
pp, qq = np.meshgrid(pr, pr, indexing="ij")
off = pp < qq                     # unordered pairs: y is symmetric in (p, q)
p, q = pp[off], qq[off]
r = p * q
XM = int(r.max()) + 3
om, _, spf = factor_info(1, XM + 1, primes_upto(int(XM ** 0.5) + 2))
lam = np.concatenate([[0], 1 - 2 * (om % 2)]).astype(float)
spf = np.concatenate([[0], spf])
keep = spf[r + 2] >= ZR
p, q, r = p[keep], q[keep], r[keep]
y = lam[r + 2]
ybar = float(y.mean())
y = y - ybar                     # centre: pq+2 is not equidistributed in residue classes
n = len(y)
half = rng.random(n) < 0.5
out = dict(P=P, k=k, pairs=n, mean_y=ybar)

def legendre(a, m):
    """Legendre symbol (a|m) for odd prime m, vectorised."""
    return np.where(a % m == 0, 0, np.where(np.array([pow(int(ai), (int(mi) - 1) // 2, int(mi)) for ai, mi in zip(a, m)]) == 1, 1, -1))

def zscore(phi):
    phi = phi.astype(float)
    v = np.sum(phi * phi)
    return float(np.sum(y * phi) / math.sqrt(v)) if v > 0 else 0.0

def control(phi):
    yc = np.where(half, phi, y)
    return float(np.sum(yc * phi) / math.sqrt(np.sum(phi * phi)))

thr = lambda m: math.sqrt(2 * math.log(200 * m))        # real N(0,1) statistics, m tests, two-sided, 1% family-wise
thrc = lambda m: math.sqrt(math.log(100 * m))           # complex statistics with |z|^2 ~ Exp(1), m tests, 1% family-wise

# ---- H24 ----
Lpq = legendre(p, q); Lqp = legendre(q, p)
fam24 = {"(p|q)": Lpq, "(q|p)": Lqp, "(-1)^((p-1)(q-1)/4)": Lpq * Lqp,
         "(2|p)(2|q)": legendre(np.full(n, 2), p) * legendre(np.full(n, 2), q),
         "(p|q)(q+2|p)": Lpq * legendre(q + 2, p)}
res24 = {name: zscore(phi) for name, phi in fam24.items()}
out["H24"] = dict(z=res24, threshold=thr(len(fam24)), control_z=control(fam24["(p|q)"]))
print("H24", json.dumps(out["H24"]), flush=True)

# ---- H26: all characters mod prime Q via FFT over the index of (pq+2) ----
best = (0.0, None); m26 = 0
for Q in primes_upto(QMAX):
    Q = int(Q)
    if Q < 3:
        continue
    g = next(g for g in range(2, Q) if all(pow(g, (Q - 1) // f, Q) != 1 for f in range(2, Q) if (Q - 1) % f == 0 and all(f % d for d in range(2, int(f ** .5) + 1))))
    ind = np.full(Q, -1); x = 1
    for e in range(Q - 1):
        ind[x] = e; x = x * g % Q
    cls = ind[(r + 2) % Q]
    ok = cls >= 0
    S = np.bincount(cls[ok], weights=y[ok], minlength=Q - 1)
    F = np.fft.fft(S)[1:]                                  # nonprincipal characters
    z = np.abs(F) / math.sqrt(np.sum(y[ok] ** 2))
    m26 += Q - 2
    if z.max() > best[0]:
        jj = int(z.argmax()) + 1
        best = (float(z.max()), (Q, jj, jj * 2 == Q - 1))
# complex chars: |z| of complex Gaussian; threshold sqrt(log(m))-ish -> use thr on 2m real tests
out["H26"] = dict(chars=m26, max_abs_z=best[0], at_Q_j_real=best[1], threshold=thrc(m26), threshold_real_chars=thr(len([1 for Q in primes_upto(QMAX) if Q >= 3])))
print("H26", json.dumps(out["H26"]), flush=True)

# ---- H27: sums of two squares ----
def is_sum2sq(v):
    v = v.copy(); okm = np.ones(len(v), bool)
    for pp_ in primes_upto(int(math.isqrt(int(v.max()))) + 1):
        pp_ = int(pp_)
        if pp_ % 4 != 3:
            while True:
                d = v % pp_ == 0
                if not d.any(): break
                v[d] //= pp_
            continue
        e = np.zeros(len(v), int)
        while True:
            d = v % pp_ == 0
            if not d.any(): break
            v[d] //= pp_; e[d] += 1
        okm &= (e % 2 == 0)
    okm &= (v % 4 != 3)      # leftover prime > sqrt: must not be 3 mod 4
    return okm
s2 = is_sum2sq((r + 2).astype(np.int64))
phi27 = np.where(s2, 1.0 / max(s2.mean(), 1e-9), -1.0 / max(1 - s2.mean(), 1e-9))
out["H27"] = dict(frac_sum2sq=float(s2.mean()), mean_y_in=float(y[s2].mean()), mean_y_out=float(y[~s2].mean()),
                  z_in=float(y[s2].sum() / math.sqrt(np.sum(y[s2] ** 2))), threshold=thr(1))
nn = np.arange(P * P + 1, min(4 * P * P + 3, XM - 1), 2, dtype=np.int64)
nn = nn[spf[nn] >= max(ZR, 3)]
ln = lam[nn]
s2n = is_sum2sq(nn)
out["H27"]["baseline_all_n"] = dict(mean_in=float(ln[s2n].mean()), mean_out=float(ln[~s2n].mean()))
cls = (nn % 8)
g1 = np.isin(cls, [1, 3]); 
out["H24_baseline"] = dict(note="lambda(n) on odd n by n mod 8: classes {1,3} vs {5,7} (pq+2 mod 8 is 3 or 1 iff (2|p)(2|q)=+1)",
                           mean_13=float(ln[g1].mean()), mean_57=float(ln[~g1].mean()))
print("H27", json.dumps(out["H27"]), flush=True)
print("H24base", json.dumps(out["H24_baseline"]), flush=True)

# ---- H28: additive and quadratic phases ----
J = 4096
rr = r % J
r2 = (r * r) % J
S1 = np.bincount(rr, weights=y, minlength=J); S2 = np.bincount(r2, weights=y, minlength=J)
sd = math.sqrt(np.sum(y ** 2))
z1 = np.abs(np.fft.fft(S1))[1:] / sd; z2 = np.abs(np.fft.fft(S2))[1:] / sd
yc = np.where(half, np.cos(2 * np.pi * 37 * rr / J), y)
zc = np.abs(np.fft.fft(np.bincount(rr, weights=yc, minlength=J)))[37] / math.sqrt(n)
out["H28"] = dict(max_z_linear=float(z1.max()), max_z_quadratic=float(z2.max()), threshold=thrc(2 * J), control_z=float(zc))
print("H28", json.dumps(out["H28"]), flush=True)

# ---- H29: hybrid characters chi(r) r^{-i tau} ----
taus = np.linspace(0, 4.0 * P * P, 2001)
logr = np.log(r.astype(float))
best = (0.0, None); m29 = 0
for Q in [3, 4, 5, 7, 8, 11, 13, 61]:
    if Q == 4:
        chis = [("r4", np.array([0, 1, 0, -1], float))]
    elif Q == 8:
        chis = [("r8a", np.array([0, 1, 0, -1, 0, 1, 0, -1], float)), ("r8b", np.array([0, 1, 0, 1, 0, -1, 0, -1], float)),
                ("r8c", np.array([0, 1, 0, -1, 0, -1, 0, 1], float))]
    else:
        chis = []
        g = next(g for g in range(2, Q) if all(pow(g, (Q - 1) // f, Q) != 1 for f in range(2, Q) if (Q - 1) % f == 0))
        ind = np.zeros(Q, int); x = 1
        for e in range(Q - 1):
            ind[x] = e; x = x * g % Q
        for j in range(1, Q - 1):
            c = np.exp(2j * np.pi * j * ind / (Q - 1)); c[0] = 0
            chis.append((j, c))
    for j, chi in chis:
        w = y * chi[r % Q]
        nw = math.sqrt(np.sum(np.abs(w) ** 2))
        z = np.empty(len(taus))
        for a in range(0, len(taus), 200):
            z[a:a + 200] = np.abs(np.exp(-1j * np.outer(taus[a:a + 200], logr)) @ w) / nw
        z[0] = 0.0                                          # tau = 0 is H26's test
        m29 += len(taus)
        if z.max() > best[0]:
            best = (float(z.max()), (Q, j if isinstance(j, str) else int(j), float(taus[z.argmax()])))
out["H29"] = dict(tests=m29, max_abs_z=best[0], at=best[1], threshold=thrc(m29))
print("H29", json.dumps(out["H29"]), flush=True)
json.dump(out, open(f"stage19_phase_cards_P{P}_z{int(ZR)}.json", "w"), indent=1)
