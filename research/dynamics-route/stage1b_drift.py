"""Stage 1 addendum (2026-11-24): what does the source paper's drift actually do?

Source paper 1 (Wang 2026, Res. Math. 13, 2684334), Sec. 3.3 and 4.2: the
non-autonomous map x_{n+1} = 1 - u_n x_n^2 with u_n = u_c - k/(ln n)^2 and
k = 12.7374 (value used in its fig9 notebook).

Along the drift u_n changes very slowly, so near step n the orbit samples the
invariant measure at the frozen parameter u_n (quasi-static approximation).
For each n we freeze u = u_n and measure the frequency of the words LRL and L
over many typical orbits. If the drift produced the Hardy-Littlewood decay, the
LRL frequency would be about k*mu_LRL/(ln n)^2; instead it tends to the positive
constant mu_LRL(u_c) = 0.1037. Writes stage1b_drift.json.
"""
import json
import math

import numpy as np

roots = np.roots([1, -2, 2, -2])
UC = float([z.real for z in roots if abs(z.imag) < 1e-12][0])
K = 12.7374
MU_LRL = 0.10368
M, BURN, T = 200_000, 2000, 1000

rng = np.random.default_rng(3)
rows = []
for e in [3, 4, 6, 8, 12, 20, 50, 100]:
    ln = e * math.log(10)
    u = UC - K / ln ** 2
    x = rng.uniform(-0.5, 0.5, M)
    for _ in range(BURN):
        x = 1 - u * x * x
    s0 = x < 0
    x = 1 - u * x * x
    s1 = x < 0
    cL = cLRL = 0
    for _ in range(T):
        x = 1 - u * x * x
        s2 = x < 0
        cL += int(s0.sum())
        cLRL += int((s0 & ~s1 & s2).sum())
        s0, s1 = s1, s2
    n = M * T
    rows.append({"log10_n": e, "u_n": round(u, 6), "LRL_freq": round(cLRL / n, 4),
                 "L_freq": round(cL / n, 4),
                 "HL_target_k_muLRL_over_ln2": float("%.3g" % (K * MU_LRL / ln ** 2))})
    print(rows[-1])

with open(__file__.replace(".py", ".json"), "w", encoding="utf-8") as fh:
    json.dump({"u_c": UC, "k": K, "samples_per_row": M * T, "rows": rows}, fh, indent=1)
