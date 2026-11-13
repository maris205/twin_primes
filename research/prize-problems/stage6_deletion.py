"""Stage 6: the deletion lemma, tested on maximal-gap covers.

Sublattice model (as in stage 1): a gap t = 2m is a choice of classes c_p for
odd primes p <= p_k such that every i in 1..m-1 has i = c_p (mod p) for some p,
while 0 and m are hit by no class.  C(i) = set of primes whose class hits i.

Deletion lemma.  For 0 <= x < y <= m, if no z with x < z < y has
C(z) contained in C(x) | C(y), then 2(y - x) is a gap at the same level:
give every prime of C(x) | C(y) a new class avoiding x and y.

For each k this script takes one cover of the maximal gap J(k), lists all gaps
the lemma produces from it, and compares with the true gap set.
"""
import json
import sys

from stage1_gap_milp import gap_occurs_milp
from stage1_gap_solver import A048670, PR

sys.stdout.reconfigure(encoding="utf-8")


def cover_sets(k, m, cert):
    C = [frozenset() for _ in range(m + 1)]
    for i in range(1, m):
        C[i] = frozenset(p for p, c in cert.items() if i % p == c % p)
        assert C[i], i
    return C


def deletion_gaps(C):
    m = len(C) - 1
    out = set()
    for x in range(m):
        for y in range(x + 1, m + 1):
            Q = C[x] | C[y]
            if all(not C[z] <= Q for z in range(x + 1, y)):
                out.add(2 * (y - x))
    return out


if __name__ == "__main__":
    true = json.load(open("a389839_witnesses.json"))
    rows = []
    for k in range(5, 27):
        J = A048670[k - 1]
        ok, cert = gap_occurs_milp(k, J)
        assert ok
        cert = {int(p): int(c) for p, c in cert.items()}
        m = J // 2
        C = cover_sets(k, m, cert)
        D = deletion_gaps(C)
        G = {int(t) for t in true[str(k)]["witness_n"]}
        assert D <= G, (k, sorted(D - G))
        single = sum(1 for i in range(1, m) if len(C[i]) == 1)
        row = {"k": k, "p_k": PR[k - 1], "J": J, "true_gaps": len(G), "from_one_cover": len(D),
               "not_reached": sorted(G - D), "singly_covered": single, "points": m - 1,
               "unused_primes": [p for p in PR[1:k] if p not in cert]}
        rows.append(row)
        print(row, flush=True)
    json.dump(rows, open("stage6_deletion.json", "w"), indent=1)
