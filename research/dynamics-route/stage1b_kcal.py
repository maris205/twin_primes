"""Stage 1 addendum (2026-11-24): can the coupling constant k = 2C_2/mu_LRL be derived?

Map: f(x) = 1 - u x^2 at the first band-merging parameter u_c, the real root of
u^3 - 2u^2 + 2u - 2 = 0 (critical orbit 0 -> 1 -> -b -> b -> b, b = u_c - 1).
Symbols: L = {x < 0}, R = {x > 0}. mu = the absolutely continuous invariant
measure (ACIP), estimated by Birkhoff averages over many typical orbits.

Outputs (stage1b_kcal.json):
  mu_L, mu_LRL, k_fit = 2C_2/mu_LRL            (the calibration of the source paper)
  k_PNT = 1/mu_L^2                             (k fixed by the one-point law, i.e. the PNT)
  corr(h) = mu(L and f^-h L)/mu_L^2            (k-independent lag correlations)
  S(h) = Hardy-Littlewood singular series      (arithmetic counterpart)
The ratios corr(h)/corr(2) do not involve k at all, so they test the model
whatever k is.
"""
import json
import math

import numpy as np

C2 = 0.6601618158468696  # twin prime constant
roots = np.roots([1, -2, 2, -2])
u = float([z.real for z in roots if abs(z.imag) < 1e-12][0])
b = u - 1
f = lambda x: 1 - u * x * x

H = [1, 2, 3, 4, 6, 8, 10, 12, 30]
HM = max(H)
M, T, BURN = 1_000_000, 2500, 300

rng = np.random.default_rng(7)
x = rng.uniform(-b, 1, M)
for _ in range(BURN):
    x = f(x)
buf = [x]
for _ in range(HM):
    buf.append(f(buf[-1]))

nL = nLRL = n = 0
cnt = {h: 0 for h in H}
for _ in range(T):
    L0 = buf[0] < 0
    nL += int(L0.sum())
    nLRL += int((L0 & (buf[1] > 0) & (buf[2] < 0)).sum())
    for h in H:
        cnt[h] += int((L0 & (buf[h] < 0)).sum())
    n += M
    buf.pop(0)
    buf.append(f(buf[-1]))

muL, muLRL = nL / n, nLRL / n


def is_prime(p):
    return p > 1 and all(p % q for q in range(2, int(p ** 0.5) + 1))


def S(h):
    if h % 2:
        return 0.0
    s = 2 * C2
    for p in range(3, h + 1):
        if h % p == 0 and is_prime(p):
            s *= (p - 1) / (p - 2)
    return s


corr = {h: cnt[h] / n / muL ** 2 for h in H}
res = {
    "u_c": u, "b": b, "samples": n,
    "mu_L": round(muL, 6), "mu_LRL": round(muLRL, 6),
    "k_fit_2C2_over_muLRL": round(2 * C2 / muLRL, 4),
    "k_PNT_1_over_muL2": round(1 / muL ** 2, 4),
    "twin_constant_predicted_with_k_PNT": round(muLRL / muL ** 2, 4),
    "twin_constant_HL_2C2": round(2 * C2, 4),
    "absorbed_factor_2C2_over_prediction": round(2 * C2 / (muLRL / muL ** 2), 4),
    "lags": [{"h": h, "dyn_corr": round(corr[h], 4), "S(h)": round(S(h), 4),
              "dyn_ratio_to_h2": round(corr[h] / corr[2], 4),
              "S_ratio_to_h2": round(S(h) / S(2), 4)} for h in H],
}
with open(__file__.replace(".py", ".json"), "w", encoding="utf-8") as fh:
    json.dump(res, fh, indent=1)
for k, v in res.items():
    if k != "lags":
        print(k, v)
for row in res["lags"]:
    print(row)
