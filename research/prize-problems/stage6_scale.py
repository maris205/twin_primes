"""Stage 6: does "delete and self-repair" keep producing a constant fraction
of gaps at larger k?

For k beyond the reach of exact maximal covers we use long greedy covers
(not maximal): odd primes in increasing order, each taking the class that
hits the most uncovered points among 1..m-1 while avoiding 0 and m.  For each
k the longest greedy cover found is used.

From that single cover, for each d in 1..m:
  level 0  deletion lemma: some x with no z in (x, x+d) having
           C(z) inside Q = C(x) | C(x+d);
  level 1  self-repair: the primes of Q, re-classed to avoid x and x+d,
           cover every such z.
At most TRIES values of x are tried per d (random order), so the fractions
are lower bounds.  Every reported gap is rigorous: the lemma is a proof.
"""
import json
import random
import sys

import numpy as np

from stage1_gap_solver import PR

sys.stdout.reconfigure(encoding="utf-8")
random.seed(2)
TRIES = 400


def primes_upto_count(k):
    out, q = [], 2
    while len(out) < k:
        if all(q % p for p in out if p * p <= q):
            out.append(q)
        q += 1
    return out


def greedy_cover(odd, m):
    unc = np.arange(1, m)
    cert = {}
    for p in odd:
        if len(unc) == 0:
            break
        cnt = np.bincount(unc % p, minlength=p)
        cnt[0] = -1
        cnt[m % p] = -1
        a = int(np.argmax(cnt))
        if cnt[a] <= 0:
            continue
        cert[p] = a
        unc = unc[unc % p != a]
    return cert if len(unc) == 0 else None


def self_repair(U, Q, x, y):
    """DFS: give primes of Q new classes (avoiding x, y) that cover all of U."""
    if not U:
        return True
    u = U[0]
    for q in Q:
        a = u % q
        if a == x % q or a == y % q:
            continue
        rest = [z for z in U if z % q != a]
        if self_repair(rest, [r for r in Q if r != q], x, y):
            return True
    return False


def analyse(k, odd, m, cert):
    C = [frozenset()] * (m + 1)
    for i in range(1, m):
        C[i] = frozenset(p for p, a in cert.items() if i % p == a)
    first = [min(c) if c else 0 for c in C]
    level = {}
    for d in range(1, m + 1):
        xs = list(range(m - d + 1))
        random.shuffle(xs)
        best = None
        for x in xs[:TRIES]:
            y = x + d
            Q = C[x] | C[y]
            if len(Q) > 6:
                continue
            U = set()
            for q in Q:
                z = x + (cert[q] - x) % q
                if z == x:
                    z += q
                while z < y:
                    if first[z] == q and C[z] <= Q:
                        U.add(z)
                    z += q
            if not U:
                best = 0
                break
            if best is None and len(U) <= 12 and self_repair(sorted(U), sorted(Q), x, y):
                best = 1
        level[d] = best
    l0 = sum(1 for v in level.values() if v == 0)
    l1 = sum(1 for v in level.values() if v is not None)
    fail = [d for d in range(1, m + 1) if level[d] is None]
    single = sum(1 for i in range(1, m) if len(C[i]) == 1)
    return {"k": k, "p_k": odd[-1], "cover_gap": 2 * m, "gap_over_p": round(2 * m / odd[-1], 2),
            "level0_fraction": round(l0 / m, 3), "level01_fraction": round(l1 / m, 3),
            "first_unreached_over_gap": round(fail[0] / m, 3) if fail else None,
            "unreached": len(fail), "singly_covered_fraction": round(single / (m - 1), 3)}


if __name__ == "__main__":
    rows = []
    for k in [int(a) for a in sys.argv[1:]] or [15, 20, 26, 40, 60, 80, 100, 150, 200, 300]:
        pr = primes_upto_count(k)
        odd = pr[1:]
        best = None
        for m in range(odd[-1] // 2, 3 * odd[-1]):
            cert = greedy_cover(odd, m)
            if cert:
                best = (m, cert)
        m, cert = best
        row = analyse(k, odd, m, cert)
        rows.append(row)
        print(row, flush=True)
        json.dump(rows, open("stage6_scale.json", "w"), indent=1)
