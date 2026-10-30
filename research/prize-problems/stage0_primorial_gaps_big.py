"""Segmented version of stage0_primorial_gaps.py for k = 10, 11.

Reduced residues mod P_k are the reduced residues mod P_9 shifted by
multiples of P_9 and filtered by the primes p_10, ..., p_k.
"""
import json
import sys

import numpy as np

from stage0_primorial_gaps import PRIMES, reduced_residues


def gap_counts(k, base=9):
    res9, m9 = reduced_residues(base)
    extra = PRIMES[base:k]
    mod = m9
    for p in extra:
        mod *= p
    blocks = mod // m9
    counts = {}
    prev = None
    for j in range(blocks):
        block = res9 + j * m9
        keep = np.ones(len(block), dtype=bool)
        for p in extra:
            keep &= block % p != 0
        block = block[keep]
        if prev is not None:
            g = int(block[0] - prev)
            counts[g] = counts.get(g, 0) + 1
        d = np.diff(block)
        v, c = np.unique(d, return_counts=True)
        for a, b in zip(v.tolist(), c.tolist()):
            counts[a] = counts.get(a, 0) + b
        prev = int(block[-1])
    g = int(mod + 1 - prev)
    counts[g] = counts.get(g, 0) + 1
    gmax = max(counts)
    t = 2
    while t in counts:
        t += 2
    return {
        "k": k,
        "p_k": PRIMES[k - 1],
        "P_k": mod,
        "phi": sum(counts.values()),
        "max_gap": gmax,
        "smallest_missing_even": t,
        "distinct_even_gaps": len(counts),
        "even_values_up_to_max": gmax // 2,
        "missing_even_up_to_max": [e for e in range(2, gmax + 1, 2) if e not in counts],
        "count_of_max_gap": counts[gmax],
    }


if __name__ == "__main__":
    out = []
    for k in [int(a) for a in sys.argv[1:]]:
        r = gap_counts(k)
        out.append(r)
        print(r, flush=True)
        json.dump(out, open("stage0_primorial_gaps_big.json", "w"), indent=1)
