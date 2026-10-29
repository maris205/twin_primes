"""Channel 1': the t-family g_t(n) = t^{Omega(s(n))} lambda(r(n)).

y = X^eps, s(n) the y-smooth part, r(n) the y-rough part.  g_1 = lambda_{>y} (Teravainen),
g_{-1} = lambda (Tao), g_0 = lambda * 1[y-rough] (twin parity).  For each t we measure,
over n in [X/R, X] with weights 1/n:
    P(t)      = E g_t(n) g_t(n+2)
    m1, m2    = E g_t(n), E g_t(n+2)
    sig(t)    = E |g_t(n) g_t(n+2)|      (pair mass: the scale a result must resolve)
    rho(t)    = E |g_t(n)|^2             (the norm a certificate pays, Theorem A)
and the normalised two-point deviation Dn(t) = (P - m1 m2) / sig.

usage: python ter_tfamily.py X eps
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); EPS = float(sys.argv[2])
Y = X ** EPS
R = 100
SEG = 5_000_000
TS = [-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]
t0 = time.time()
plist = primes_upto(int((X + 4) ** 0.5) + 1)
small = [int(p) for p in plist if p < Y]

acc = {t: np.zeros(6) for t in TS}       # W, P, m1, m2, sig, rho
for a in range(X // R, X + 1, SEG):
    b = min(a + SEG, X + 1)
    om, _, _ = factor_info(a, b + 2, plist)
    L = b + 2 - a
    oms = np.zeros(L, np.int16)
    for p in small:
        pk = p
        while pk <= b + 2:
            oms[(-a) % pk::pk] += 1
            if pk > (b + 2) // p:
                break
            pk *= p
    lr = 1.0 - 2.0 * ((om - oms) % 2)
    m = L - 2
    wt = 1.0 / np.arange(a, a + m, dtype=np.float64)
    for t in TS:
        g = np.power(t, oms.astype(np.float64)) * lr        # 0.0**0 = 1
        g1, g2 = g[:m], g[2:m + 2]
        pr = g1 * g2
        acc[t] += [wt.sum(), (wt * pr).sum(), (wt * g1).sum(), (wt * g2).sum(),
                   (wt * np.abs(pr)).sum(), (wt * g1 * g1).sum()]
    print(f"to {b}: {time.time()-t0:.0f}s", flush=True)

rows = []
for t in TS:
    W, P, a1, a2, sg, rh = acc[t] / acc[t][0]
    rows.append(dict(t=t, P=P, m1=a1, m2=a2, D=P - a1 * a2, sig=sg, rho=rh, Dn=(P - a1 * a2) / sg))
out = dict(X=X, eps=EPS, y=Y, logy=math.log(Y), R=R, rows=rows)
json.dump(out, open(f'ter_tfamily_{X:.0e}_eps{EPS}.json'.replace('+', ''), 'w'), indent=1)
print(f"X={X:.0e} y={Y:.1f} log y={math.log(Y):.2f}")
print("   t        P         m1        D        sig       rho     D/sig")
for r in rows:
    print(f"{r['t']:+5.2f} {r['P']:+9.5f} {r['m1']:+9.5f} {r['D']:+9.5f} {r['sig']:9.5f} {r['rho']:9.5f} {r['Dn']:+8.4f}")
