"""Channel 3: the class matrix N(s, r') of rough pairs (Theorem C).

For m in (X/10, X], z = X^eta: R_s = squarefree z-rough m with omega(m) = s.
N(s, r') = #{m : m in R_s, m+2 in R_r'}.  Normalise by the empirical marginals,
    Q(s, r') = N(s, r') * W / (|R_s| |R_r'|),
W = number of m in the window, so that Q = (pair factor) * (1 + u(s, r')).  Theorem C (on GEH)
says u(s, r') = (delta - 1)(-1)^{s+r'}: even classes carry delta, odd classes 2 - delta.  We fit
Q(s, r') = A (1 + c (-1)^{s+r'}) by weighted least squares and report c (= delta - 1) and the
per-class estimates of delta.

usage: python rough_classes.py X
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1]))
ETAS = [0.15, 0.2, 0.25]
SEG = 10_000_000
t0 = time.time()
plist = primes_upto(int((X + 4) ** 0.5) + 1)
SMAX = 7
cnt = {e: np.zeros((SMAX + 1, SMAX + 1)) for e in ETAS}
marg = {e: np.zeros(SMAX + 1) for e in ETAS}
W = 0
for a in range(X // 10 + 1, X + 1, SEG):
    b = min(a + SEG, X + 1)
    om, sqf, spf = factor_info(a, b + 2, plist)
    m = b - a
    W += m
    for e in ETAS:
        z = X ** e
        cls = np.where(sqf & (spf >= z), om, 0).astype(np.int64)
        cls = np.minimum(cls, SMAX)
        c1, c2 = cls[:m], cls[2:m + 2]
        marg[e] += np.bincount(c1, minlength=SMAX + 1)
        ok = (c1 > 0) & (c2 > 0)
        cnt[e] += np.bincount(c1[ok] * (SMAX + 1) + c2[ok], minlength=(SMAX + 1) ** 2).reshape(SMAX + 1, SMAX + 1)
    print(f"to {b}: {time.time()-t0:.0f}s", flush=True)

out = dict(X=X, window=[X // 10, X], results=[])
for e in ETAS:
    rmax = int(1 / e)
    rows = []
    for s in range(1, rmax + 1):
        for r in range(1, rmax + 1):
            N = cnt[e][s, r]
            if N < 50:
                continue
            Q = N * W / (marg[e][s] * marg[e][r])
            rows.append(dict(s=s, r=r, N=int(N), Q=Q, sign=(-1) ** (s + r), se=Q / math.sqrt(N)))
    # weighted least squares for Q = A + B * sign, with B = A c
    w = np.array([1 / r['se'] ** 2 for r in rows]); y = np.array([r['Q'] for r in rows]); sg = np.array([r['sign'] for r in rows])
    Xm = np.stack([np.ones_like(y), sg], 1)
    WX = Xm * w[:, None]
    cov = np.linalg.inv(Xm.T @ WX); beta = cov @ (WX.T @ y)
    A, B = beta; c = B / A
    sc = math.sqrt(cov[1, 1]) / A
    for r in rows:
        r['delta_hat'] = r['Q'] / A if r['sign'] > 0 else 2 - r['Q'] / A
    chi2 = float((w * (y - Xm @ beta) ** 2).sum())
    out['results'].append(dict(eta=e, A=A, c=c, c_se=sc, chi2=chi2, dof=len(rows) - 2, rows=rows))
    print(f"\neta={e}: A={A:.4f}  c=delta-1={c:+.4f} +- {sc:.4f}  chi2/dof={chi2:.1f}/{len(rows)-2}")
    for r in rows:
        print(f"  ({r['s']},{r['r']}) {'even' if r['sign']>0 else 'odd '}  N={r['N']:9d}  Q={r['Q']:.4f}+-{r['se']:.4f}  delta_hat={r['delta_hat']:.3f}")
json.dump(out, open(f'rough_classes_{X:.0e}.json'.replace('+', ''), 'w'), indent=1)
