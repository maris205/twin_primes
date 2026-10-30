"""Endpoint weight in step B of the #854 construction (stage 3).

Theorem 2.1 bounded the endpoint weight H(i-1) H(t+1-i) by its maximum,
(e^gamma loglog t + 3)^2. Theorem 3.1 (STAGE3_LOGLOSS.md) replaces this by
its average over i = mP (P prime > x/2), which is O(1). This script

  1. computes the constant C_f = prod_q (1 + (2q-1)/(q-1)^3) of Theorem 3.1;
  2. for sample (x, t, z) runs step A exactly, then evaluates
       - the exact expected number of step-B survivors
             sum_{i in S_A} prod_{q<=z, q not | (i-1)(t+1-i)} (1 - 1/(q - nu_q)),
       - the mean of H(i-1) H(t+1-i) over S_A and over its part S_pr,
       - the maximum weight used in Theorem 2.1.
"""
import json
import math
import sys

import numpy as np

from stage1_gap_solver import primes_upto

sys.stdout.reconfigure(encoding="utf-8")
GAMMA = 0.5772156649015329


def C_f(limit=10 ** 7):
    c = 1.0
    for q in primes_upto(limit):
        c *= 1 + (2 * q - 1) / (q - 1) ** 3
    # tail: sum_{q > limit} 2/q^2 < 2/limit
    return c, c * math.exp(2 / limit)


def H_array(N, z, primes):
    """H(n) = prod_{q | n, q <= z} (1 - 1/q)^{-1} for 0 <= n <= N (H(0) unused)."""
    H = np.ones(N + 1)
    for q in primes:
        if q > z:
            break
        H[0::q] *= q / (q - 1)
    return H


def run(x, lam, u):
    t = int(lam * x) // 2 * 2
    z = x ** (1 / u)
    P = primes_upto(t + 2)
    pos = np.arange(t + 2)
    # step A: class 0 for primes in (z, x/2] not dividing t+1
    alive = np.zeros(t + 2, dtype=bool)
    alive[2:t + 1] = True
    for p in P:
        if p > x / 2:
            break
        if p > z and (t + 1) % p:
            alive[0::p] = False
    alive[1] = alive[t + 1] = False
    SA = pos[alive]
    # S_pr: survivors with a prime factor > x/2
    big = np.zeros(t + 2, dtype=bool)
    for p in P:
        if p > x / 2:
            big[p::p] = True
    Spr = SA[big[SA]]
    # exact expectation in step B
    small = [q for q in P if q <= z]
    surv = np.ones(len(SA))
    for q in small:
        nu = 1 if (t + 1) % q == 1 % q else 2
        killed = ((SA - 1) % q == 0) | ((t + 1 - SA) % q == 0)
        surv *= np.where(killed, 1.0, 1 - 1 / (q - nu))
    H = H_array(t + 1, z, P)
    w = H[SA - 1] * H[t + 1 - SA]
    wpr = H[Spr - 1] * H[t + 1 - Spr]
    W = np.prod([1 - 1 / q for q in small])
    Wmax = (math.exp(GAMMA) * math.log(math.log(t)) + 3) ** 2
    N = sum(1 for p in P if x / 2 < p <= x)
    return {
        "x": x, "t": t, "lambda": round(t / x, 3), "u": u, "z": round(z, 1),
        "|S_A|": int(len(SA)), "|S_pr|": int(len(Spr)),
        "E_B_exact": round(float(surv.sum()), 1),
        "bound_avg": round(float(W * w.sum()), 1),
        "bound_max": round(float(W * Wmax * len(SA)), 1),
        "mean_w_SA": round(float(w.mean()), 3),
        "mean_w_Spr": round(float(wpr.mean()), 3),
        "max_w_used_in_thm21": round(Wmax, 2),
        "N_large": N,
    }


if __name__ == "__main__":
    cf, cf_up = C_f()
    print({"C_f": round(cf, 5), "C_f_upper": round(cf_up, 5),
           "c_thm31": round(math.exp(GAMMA) / (8 * cf_up), 5)}, flush=True)
    out = {"C_f": cf, "C_f_upper": cf_up, "rows": []}
    for x, lam, u in [(10 ** 5, 2, 3), (10 ** 5, 4, 3), (10 ** 6, 2, 3), (10 ** 6, 4, 3),
                      (10 ** 6, 4, 4), (10 ** 7, 2, 3)]:
        r = run(x, lam, u)
        print(r, flush=True)
        out["rows"].append(r)
    json.dump(out, open("stage3_endpoint_weight.json", "w"), indent=1)
