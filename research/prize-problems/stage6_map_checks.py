"""Stage 6 checks that go with STAGE6_MAP.md.

(a) G(k-1) is a subset of G(k), and s(k) > J(k-1), on the exact data.
(b) Survivor set S of a maximal-gap cover: points hit by no prime <= p_k/2.
    Size of S, of its difference set, and where the missing differences are.
(c) Two rounds of the deletion lemma: each gap found from the maximal cover
    comes with a cover of its own, to which the lemma is applied again.
"""
import json
import random
import sys

from stage1_gap_milp import gap_occurs_milp
from stage1_gap_solver import A048670, PR
from stage6_deletion import cover_sets

sys.stdout.reconfigure(encoding="utf-8")
random.seed(1)


def admissible_pairs(C):
    m = len(C) - 1
    for x in range(m):
        for y in range(x + 1, m + 1):
            Q = C[x] | C[y]
            if all(not C[z] <= Q for z in range(x + 1, y)):
                yield x, y, Q


def derived_cover(cert, x, y, Q):
    d = y - x
    new = {}
    for p, c in cert.items():
        if p in Q:
            ok = [a for a in range(p) if a != 0 and a != d % p]
            new[p] = random.choice(ok)
        else:
            new[p] = (c - x) % p
    return new


if __name__ == "__main__":
    true = json.load(open("a389839_witnesses.json"))
    G = {int(k): {int(t) for t in r["witness_n"]} for k, r in true.items()}
    a = {int(k): r["a"] for k, r in true.items()}
    for k in range(3, 27):
        assert G[k - 1] <= G[k], k
    lag = {k: a[k] - A048670[k - 2] for k in range(6, 27)}
    assert all(v > 0 for v in lag.values())
    print("G(k-1) subset of G(k): k=3..26 ok;  s(k)-J(k-1), k=6..26:", list(lag.values()))
    rows = []
    for k in range(8, 27):
        J = A048670[k - 1]
        m = J // 2
        ok, cert = gap_occurs_milp(k, J)
        cert = {int(p): int(c) for p, c in cert.items()}
        C = cover_sets(k, m, cert)
        pk = PR[k - 1]
        S = [0] + [i for i in range(1, m) if min(C[i]) > pk / 2] + [m]
        diff = {y - x for x in S for y in S if y > x}
        miss = [2 * d for d in range(1, m + 1) if d not in diff]
        one, two = set(), set()
        for x, y, Q in admissible_pairs(C):
            one.add(2 * (y - x))
            if k <= 22:
                c2 = derived_cover(cert, x, y, Q)
                C2 = cover_sets(k, y - x, c2)
                two |= {2 * (v - u) for u, v, _ in admissible_pairs(C2)}
        two |= one
        assert two <= G[k]
        row = {"k": k, "p_k": pk, "J": J, "S": len(S), "S_minus_S": len(diff), "half_J": m,
               "missing_differences_of_S": miss, "one_round": len(one),
               "two_rounds": len(two) if k <= 22 else None, "true": len(G[k])}
        rows.append(row)
        print(row, flush=True)
    json.dump({"lag": lag, "rows": rows}, open("stage6_map_checks.json", "w"), indent=1)
