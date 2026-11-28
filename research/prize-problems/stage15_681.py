"""Stage 15: numerics for Erdos #681 (and #680).

#681: for large n, is there k >= 1 with n+k composite and p(n+k) > k^2
(p = least prime factor)?  If n+1 is composite, k = 1 works, so only
n = p - 1 (p prime) matter.  OEIS A389680 uses the stricter variant with
i >= 2 for every n.

For every n in [N0, N1) we compute, by a segmented least-prime-factor sieve,
    V(n)   = least i >= 2 with n+i composite and p(n+i) > i^2   (A389680 variant)
    W680(n)= least k >= 1 with p(n+k) > k^2 + 1                  (#680; primes allowed)
For n = p - 1 the #681 witness is W(p-1) = V(p-1).

We record
  - the distribution of W(p-1) over primes p (P(W > K) for K <= KMAX),
  - record values of V(n) over all n, of W(p-1) over primes, and of W680(n),
  - any n in the range with no witness i <= IMAX (none is expected).
The last part estimates by Monte Carlo the limiting proportion
    delta(K) = P(every k in [2,K] has a prime q <= k^2 with q | n+k),
n+1 = p coprime to every q, residues of n mod q independent and uniform
among the q-1 classes != -1 (Theorem 15.2).

Usage: python -B stage15_681.py [N1] [N0].  Writes stage15_681.json.
"""
import json
import math
import sys
import time

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")

N1 = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9
N0 = int(float(sys.argv[2])) if len(sys.argv) > 2 else 2
SEG = 10**7
IMAX = 400
KMAX = 40


def small_primes(n):
    s = np.ones(n + 1, bool)
    s[:2] = False
    for q in range(2, int(n**0.5) + 1):
        if s[q]:
            s[q * q::q] = False
    return np.nonzero(s)[0]


PR = small_primes(int((N1 + SEG + IMAX) ** 0.5) + 2)


def spf_segment(L, S):
    """a[j] = least prime factor of L+j if L+j is composite, else 0."""
    a = np.zeros(S, np.int64)
    hi = L + S
    for q in PR:
        q = int(q)
        if q * q >= hi:
            break
        first = max(q * q, ((L + q - 1) // q) * q)
        v = a[first - L::q]
        a[first - L::q] = np.where(v == 0, q, v)
    return a


def oeis_direct(n):
    """Definition of A389680 membership, for checking small n."""
    i = 2
    while i**4 < n + i:
        m = n + i
        d = 2
        lp = m
        while d * d <= m:
            if m % d == 0:
                lp = d
                break
            d += 1
        if lp != m and lp > i * i:
            return False
        i += 1
    return True


hist = np.zeros(IMAX + 2, np.int64)   # W(p-1) over primes p
nprimes = 0
recV, recW, rec680 = [], [], []
bestV = bestW = best680 = 0
nowit = []
bins_all = np.zeros(20, np.int64)
bins_p = np.zeros(20, np.int64)
exc_all = np.zeros(20, np.int64)
exc_p = np.zeros(20, np.int64)
last_exc_all, last_exc_p = [], []
t0 = time.time()
L = N0
while L < N1:
    S = min(SEG, N1 - L)
    a = spf_segment(L, S + IMAX + 1)   # index j <-> integer L + j
    V = np.zeros(S, np.int64)
    W6 = np.zeros(S, np.int64)
    openV = np.ones(S, bool)
    open6 = np.ones(S, bool)
    for i in range(1, IMAX + 1):
        m = a[i:i + S]                  # spf of n + i for n = L + j
        if i >= 2 and openV.any():
            hit = openV & (m > i * i)
            V[hit] = i
            openV &= ~hit
        if open6.any():
            hit = open6 & ((m == 0) | (m > i * i + 1))
            W6[hit] = i
            open6 &= ~hit
        if not openV.any() and not open6.any():
            break
    nv = np.nonzero(openV)[0]
    isprime_next = a[1:S + 1] == 0      # n + 1 prime  <=>  n = p - 1
    nn = np.arange(L, L + S)
    dec = np.floor(np.log10(nn)).astype(np.int64)
    np.add.at(bins_all, dec, 1)
    np.add.at(bins_p, dec[isprime_next], 1)
    np.add.at(exc_all, dec[openV], 1)
    np.add.at(exc_p, dec[openV & isprime_next], 1)
    if len(nv):
        last_exc_all = [int(L + j) for j in nv[-5:]]
        pe = np.nonzero(openV & isprime_next)[0]
        if len(pe):
            last_exc_p = [int(L + j) for j in pe[-5:]]
    if len(nowit) < 50:
        nowit.extend(int(L + j) for j in nv[:50 - len(nowit)])
    Wp = V[isprime_next]
    Wp = np.where(Wp == 0, IMAX + 1, Wp)
    hist += np.bincount(Wp, minlength=IMAX + 2)[:IMAX + 2]
    nprimes += int(isprime_next.sum())
    # records (first occurrence of a new maximum)
    for arr, mask, rec, name in ((V, np.ones(S, bool), recV, "V"),
                                 (V, isprime_next, recW, "W"),
                                 (W6, np.ones(S, bool), rec680, "W680")):
        best = {"V": bestV, "W": bestW, "W680": best680}[name]
        vals = np.where(mask, arr, 0)
        run = np.maximum.accumulate(np.concatenate(([best], vals)))
        for j in np.nonzero(np.diff(run) > 0)[0]:
            best = int(vals[j])
            n = int(L + j)
            rec.append({"n": n, "witness": best, "log_n": round(math.log(n), 3),
                        "witness_over_log_n": round(best / math.log(n), 3)})
        if name == "V":
            bestV = best
        elif name == "W":
            bestW = best
        else:
            best680 = best
    L += S
    print("upto %.3g  primes %d  maxV %d  maxW(p-1) %d  maxW680 %d  %.0fs" %
          (L, nprimes, bestV, bestW, best680, time.time() - t0), flush=True)

# A389680 check for small n: direct definition vs sieve
check = [n for n in range(1, 2001) if oeis_direct(n)]

# empirical tail P(W(p-1) > K)
cum = np.cumsum(hist)
tail_emp = {K: round(float(1 - cum[K] / nprimes), 6) for K in range(2, KMAX + 1)}

# Monte Carlo for delta(K)
rng = np.random.default_rng(15)
T = 10**6
qs = [int(q) for q in small_primes(KMAX * KMAX)]
res = {q: rng.integers(0, q - 1, T) for q in qs}   # classes 0..q-2, i.e. n != -1 (mod q)
blocked_all = np.ones(T, bool)
delta = {}
for k in range(2, KMAX + 1):
    b = np.zeros(T, bool)
    for q in qs:
        if q > k * k:
            break
        b |= res[q] == (-k) % q
    blocked_all &= b
    delta[k] = round(float(blocked_all.mean()), 6)

out = {
    "range": [N0, N1], "primes_p_with_p_minus_1_in_range": nprimes,
    "first_no_witness_n": nowit[:50],
    "per_decade": [{"decade": "[1e%d,1e%d)" % (d, d + 1), "n_count": int(bins_all[d]),
                    "no_witness_n (A389680 terms)": int(exc_all[d]),
                    "primes_p (n=p-1)": int(bins_p[d]), "no_witness_p (#681 exceptions)": int(exc_p[d]),
                    "fraction_p": round(float(exc_p[d] / bins_p[d]), 6) if bins_p[d] else None}
                   for d in range(20) if bins_all[d]],
    "largest_no_witness_n": last_exc_all, "largest_681_exceptions_n": last_exc_p,
    "A389680_direct_upto_2000_count": len(check),
    "records_V_all_n": recV, "records_W_p_minus_1": recW, "records_W680": rec680,
    "tail_empirical_P(W(p-1)>K)": tail_emp, "delta_montecarlo": delta,
    "seconds": round(time.time() - t0, 1),
}
print(json.dumps(out["per_decade"], indent=0))
print("largest exceptions:", last_exc_all, last_exc_p)
if N0 <= 2:
    first = [n for n in check if n >= N0][:len(nowit)]
    print("A389680 direct check: first %d sieve exceptions agree with the definition:" % len(nowit), first == nowit)
    out["A389680_first50_agree_with_definition"] = first == nowit
print("records W(p-1):", recW[-8:])
print("records V:", recV[-6:])
print("records W680:", rec680[-6:])
with open(__file__.replace(".py", ".json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print("tail vs delta:", [(K, tail_emp[K], delta[K]) for K in (3, 5, 7, 9, 11, 15, 21, 31, 40)])
