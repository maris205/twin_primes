"""Numerical check of Theorem M (route/BARRIER.md) against exact counts.

For the rough class (a): S = R = z-rough numbers in (x/2, x], D = primes in (z, P2], h = 2.
  E_R  = #{(d, m): d in D, m in (x/(2d), x/d], m and m+2 z-rough}   (dilated rough pairs)
  bound: R-res >= |S| / (2 E_R)   (Lemma 1); compare with the Lanczos lam/avgdeg of L4_TEST.
For the smooth class (b): D = all z-smooth d <= Dmax (d >= 2), S = {d r : d in D u {1}, r z-rough} in (x/2, x].
  |S| counted exactly (smooth part of n is in D u {1} and rough part is z-rough), E_R as above;
  bound R-res >= |S| / (2 E_R), and the Theorem M(b) form  c * log z.
"""
import json, math, sys
import numpy as np

X = int(float(sys.argv[1]))
lo = X // 2 + 1
def primes_upto(m):
    s = np.ones(m + 1, dtype=bool); s[:2] = False
    for p in range(2, math.isqrt(m) + 1):
        if s[p]: s[p * p::p] = False
    return np.nonzero(s)[0]
PR = primes_upto(10 ** 6)
out = {"a": [], "b": []}
roughall = None
for eta in (0.15, 0.2):
    z = X ** eta
    small = PR[PR < z]
    # z-rough indicator on [1, X+2]
    rough = np.ones(X + 3, dtype=bool); rough[0] = False
    for p in small:
        rough[p::p] = False
    rough[1] = True
    pair = rough[1:X + 1] & rough[3:X + 3]          # index m-1: m and m+2 rough
    cpair = np.concatenate([[0], np.cumsum(pair)])  # cpair[k] = #m <= k
    S_R = int(rough[lo:X + 1].sum())
    for P2 in (10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5):
        D = PR[(PR > z) & (PR <= P2)]
        ER = sum(int(cpair[X // d] - cpair[X // (2 * d)]) for d in D)
        V = float(np.sum(1.0 / D))
        out["a"].append({"eta": eta, "z": z, "P2": P2, "|S|": S_R, "E_R": ER,
                         "R-res >= |S|/(2E_R)": S_R / (2 * ER), "V": V,
                         "x|S|-normalised: E_R*log^2 z/(x V)": ER * math.log(z) ** 2 / (X * V),
                         "|S| log z / x": S_R * math.log(z) / X})
        print("a", json.dumps(out["a"][-1]), flush=True)
    # class (b): D = z-smooth numbers in [2, Dmax]
    for Dmax in (10, 100, 1000, 10000):
        ds = np.arange(2, Dmax + 1)
        m = ds.copy()
        for p in small:
            while True:
                dv = m % p == 0
                if not dv.any(): break
                m[dv] //= p
        D = ds[m == 1]
        ER = sum(int(cpair[X // d] - cpair[X // (2 * d)]) for d in D)
        # |S|: n in window whose z-smooth part lies in D u {1} and rough part is z-rough
        Dset = np.zeros(Dmax + 1, dtype=bool); Dset[D] = True; Dset[1] = True
        S = 0
        for d in np.nonzero(Dset)[0]:
            a, b = (X // 2) // d + 1, X // d
            if b >= a:
                S += int(rough[a:b + 1].sum())
        V = float(np.sum(1.0 / D))
        out["b"].append({"eta": eta, "z": z, "Dmax": Dmax, "|D|": int(len(D)), "V": V, "|S|": S, "E_R": ER,
                         "R-res >= |S|/(2E_R)": S / (2 * ER), "log z": math.log(z)})
        print("b", json.dumps(out["b"][-1]), flush=True)
json.dump(out, open("barrier_check.json", "w"), indent=1)
