"""Certified lower bounds for the smallest missing even gap s(k) (Erdos #854).

Theorem 1.2 (STAGE1_GAPS.md): for even t < p_k, if
    pi(p_k) - pi(t) >= E(t) := sum_{0<i<t} prod_{q<t, q does not divide i(t-i)} (1 - 1/(q - nu_q(t))),
with nu_q(t) = 1 if q | t and 2 otherwise, then t is a gap of the reduced
residue system mod P_k. (E(t) is the mean of R(a) over admissible a, and
some a has R(a) <= E(t).)

This script computes, for each k, the largest T(k) such that every even
t <= T(k) passes the test (small t also pass through the trivial bound
R(a) <= t/2 - 1). Floating-point sums are compared with a margin of 1e-6.
"""
import json
import math
import sys

from stage1_gap_solver import primes_upto

PR = primes_upto(200000)


def expected_R(t):
    qs = [q for q in PR if q < t]
    tot = 0.0
    for i in range(1, t):
        if i % 2:  # a odd, so a + i even: always covered by 2
            continue
        prod = 1.0
        x = i * (t - i)
        for q in qs:
            if q == 2:
                continue
            if x % q:
                nu = 1 if t % q == 0 else 2
                prod *= 1.0 - 1.0 / (q - nu)
        tot += prod
    return tot


def certified_T(k, cache):
    pk = PR[k - 1]
    T = 0
    for t in range(2, pk, 2):
        avail = k - sum(1 for q in PR[:k] if q <= t)
        need = t // 2 - 1
        if avail >= need:
            T = t
            continue
        if t not in cache:
            cache[t] = expected_R(t)
        if avail >= cache[t] + 1e-6:
            T = t
        else:
            break
    return T


if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or [10, 20, 50, 100, 200, 400]
    cache = {}
    out = []
    for k in ks:
        T = certified_T(k, cache)
        pk = PR[k - 1]
        r = {"k": k, "p_k": pk, "certified_T": T, "ratio_T_over_pk": round(T / pk, 4)}
        out.append(r)
        print(r, flush=True)
    json.dump(out, open("stage1_certified_range.json", "w"), indent=1)
