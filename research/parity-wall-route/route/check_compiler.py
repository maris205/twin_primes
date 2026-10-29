"""Numerical checks for route/COMPILER.md.

For x = 10^k:
  M  = sum Lambda_2(n)Lambda_2(n+2)                       (C1: ~ 8 Pi_2 x log^2 x on GEH)
  D1 = sum Lambda_2(n)lambda(n)Lambda_2(n+2),  D2 = ... lambda(n+2)   (C2: o(x log^2 x))
  D3 = sum Lambda_2(n)Lambda_2(n+2)lambda(n)lambda(n+2)   (parity node)
  T  = sum log n Lambda(n) log(n+2)Lambda(n+2)
  exact algebra check:  4T = M - D1 - D2 + D3  + (prime-power terms)
Logarithmic versions with weight w(n) = 1/(n log n log(n+2)):
  rho_log = D3_log / M_log,  and  sum Lambda(n)Lambda(n+2)/n  vs  2 Pi_2 log X (1 + rho_log).
Also: sum_{n<=x} mu(n) 1[P^-(n) > x^alpha] / (x/log x) for alpha in (1/3,1/2), against
  -1 + log((1-alpha)/alpha)  (shows mu 1_R is not o(x/log x) for fixed alpha).
"""
import json, math, sys
import numpy as np

XMAX = int(float(sys.argv[1])); top = XMAX + 2
spf = np.zeros(top + 1, dtype=np.int32)
for p in range(2, math.isqrt(top) + 1):
    if spf[p] == 0:
        blk = spf[p * p::p]; blk[blk == 0] = p
isp = spf == 0; isp[:2] = False; spf[isp] = np.nonzero(isp)[0]
n = np.arange(top + 1, dtype=np.int64)
p1 = spf.astype(np.int64); m = n.copy(); a = np.zeros(top + 1, np.int8)
for _ in range(40):
    d = (m > 1) & (m % np.maximum(p1, 1) == 0)
    if not d.any(): break
    m[d] //= p1[d]; a[d] += 1
p2 = np.where(m > 1, spf[np.minimum(m, top)].astype(np.int64), 1)
m2 = m.copy(); b = np.zeros(top + 1, np.int8)
for _ in range(40):
    d = (m2 > 1) & (m2 % np.maximum(p2, 1) == 0)
    if not d.any(): break
    m2[d] //= p2[d]; b[d] += 1
lp1 = np.log(np.maximum(p1, 1).astype(float)); lp2 = np.log(np.maximum(p2, 1).astype(float))
ppow = (n >= 2) & (b == 0); two = (n >= 2) & (b > 0) & (m2 == 1)
Lam = np.where(ppow, lp1, 0.0)
Lam2 = np.where(ppow, (2 * a.astype(float) - 1) * lp1 ** 2, 0.0) + np.where(two, 2 * lp1 * lp2, 0.0)
lam = np.where((a.astype(int) + b.astype(int)) % 2 == 0, 1.0, -1.0)
# squarefree part Lambda_2^flat = mu^2 Lambda_2: supported on primes and products pq (p != q)
sqf = np.where(ppow, a == 1, (a == 1) & (b == 1))
Lam2f = Lam2 * sqf
logn = np.log(np.maximum(n, 2).astype(float))
sqf_prime = isp
PI2 = 0.6601618158468696
out = {"cesaro": [], "log": [], "mu_rough": []}
for k in range(4, int(round(math.log10(XMAX))) + 1):
    x = 10 ** k
    s, s2 = slice(1, x + 1), slice(3, x + 3)
    A, B = Lam2[s], Lam2[s2]; la, lb = lam[s], lam[s2]
    M = float(A @ B); D1 = float((A * la) @ B); D2 = float(A @ (B * lb)); D3 = float((A * la) @ (B * lb))
    T = float((Lam[s] * logn[s]) @ (Lam[s2] * logn[s2]))
    Af, Bf = Lam2f[s], Lam2f[s2]
    Mf = float(Af @ Bf); D1f = float((Af * la) @ Bf); D2f = float(Af @ (Bf * lb)); D3f = float((Af * la) @ (Bf * lb))
    Tp = float((Lam[s] * logn[s] * isp[s]) @ (Lam[s2] * logn[s2] * isp[s2]))
    # restrict exact check to n, n+2 squarefree-type (not proper prime powers) via the identity
    out["cesaro"].append({"x": x, "M/(8Pi2 x log^2x)": M / (8 * PI2 * x * math.log(x) ** 2),
                          "D1/M": D1 / M, "D2/M": D2 / M, "D3/M": D3 / M,
                          "(4T-(M-D1-D2+D3))/M": (4 * T - (M - D1 - D2 + D3)) / M,
                          "flat: (4T_primes-(Mf-D1f-D2f+D3f))/Mf": (4 * Tp - (Mf - D1f - D2f + D3f)) / Mf,
                          "(M-Mf)/M": (M - Mf) / M})
    w = 1.0 / (n[s] * logn[s] * logn[s2])
    Ml = float((A * w) @ B); D3l = float((A * la * w) @ (B * lb))
    rho = D3l / Ml
    Tl = float((Lam[s] / n[s]) @ Lam[s2])
    out["log"].append({"X": x, "rho_log": rho, "M_log/(8Pi2 log X)": Ml / (8 * PI2 * math.log(x)),
                       "sum Lam Lam/n / (2Pi2 log X)": Tl / (2 * PI2 * math.log(x))})
    print(json.dumps(out["cesaro"][-1]), json.dumps(out["log"][-1]), flush=True)
# mu over rough numbers, alpha in (1/3, 1/2)
mu_ok = np.ones(top + 1, dtype=bool)
# squarefree check on numbers with omega<=2 suffices for alpha>1/3 (at most two prime factors)
for x in (10 ** 6, 10 ** 7):
    for alpha in (0.36, 0.4, 0.45):
        z = x ** alpha
        R = spf[2:x + 1] > z
        nn = slice(2, x + 1)
        # for alpha > 1/3 rough n <= x have Omega <= 2: prime (mu=-1) or p*q distinct (mu=+1) or p^2 (mu=0)
        is_p = isp[nn]
        is_pq = two[nn] & (a[nn] == 1) & (b[nn] == 1)
        S = float((-1.0 * (R & is_p)).sum() + (1.0 * (R & is_pq)).sum())
        out["mu_rough"].append({"x": x, "alpha": alpha, "sum/(x/log x)": S / (x / math.log(x)),
                                "prediction -1+log((1-a)/a)": -1 + math.log((1 - alpha) / alpha)})
        print(json.dumps(out["mu_rough"][-1]), flush=True)
json.dump(out, open("check_compiler.json", "w"), indent=1)
