"""Stage 0 first look at Erdos #854 (JSP-000707).

For the k-th primorial P_k, list the gaps a_{i+1}-a_i between consecutive
integers coprime to P_k (one full period), then report the maximal gap
(Jacobsthal), the smallest even integer that is not a gap, the number of
distinct even gaps, and how often the maximal gap occurs.
"""
import json
import sys

import numpy as np

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def reduced_residues(k):
    """Integers in [1, P_k) coprime to P_k, built by lifting one prime at a time."""
    res = np.array([1], dtype=np.int64)
    mod = 1
    for p in PRIMES[:k]:
        lifted = (res[None, :] + mod * np.arange(p, dtype=np.int64)[:, None]).ravel()
        res = lifted[lifted % p != 0]
        mod *= p
    res.sort()
    return res, mod


def gap_stats(k):
    res, mod = reduced_residues(k)
    gaps = np.diff(np.concatenate([res, [mod + 1]]))
    values, counts = np.unique(gaps, return_counts=True)
    gmax = int(values[-1])
    present = set(int(v) for v in values)
    t = 2
    while t in present:
        t += 2
    missing = [e for e in range(2, gmax + 1, 2) if e not in present]
    return {
        "k": k,
        "p_k": PRIMES[k - 1],
        "P_k": mod,
        "phi": int(len(res)),
        "max_gap": gmax,
        "smallest_missing_even": t,
        "distinct_even_gaps": len(values),
        "even_values_up_to_max": gmax // 2,
        "missing_even_up_to_max": missing,
        "count_of_max_gap": int(counts[-1]),
    }


if __name__ == "__main__":
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    out = [gap_stats(k) for k in range(2, kmax + 1)]
    for r in out:
        print(r["k"], r["p_k"], r["max_gap"], r["smallest_missing_even"],
              r["distinct_even_gaps"], r["even_values_up_to_max"], r["count_of_max_gap"],
              r["missing_even_up_to_max"])
    json.dump(out, open(f"stage0_primorial_gaps_k{kmax}.json", "w"), indent=1)
