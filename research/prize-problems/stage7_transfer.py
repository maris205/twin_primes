"""Stage 7: numerical run of the construction behind Theorem 7.1.

Theorem 7.1 says: a covered interval at level j, plus the free primes
p_{j+1..k}, gives every even t up to (1 - eps) times its length as a gap at
level k.  The recipe, in the halved model:

  base    a greedy cover of 1..m-1 by classes of odd primes <= p_j
          (0 and m uncovered);
  target  d in 1..m, i.e. the gap 2d;
  choose  x, y = x + d whose covering primes Q are large;
  release Q (new classes avoiding x and y);
  repair  each exposed z in (x, y), i.e. C(z) inside Q, gets its own free
          prime l in (p_j, p_k] with class z mod l, where l divides neither
          z - x nor y - z.

Success for d is a proof that 2d is a gap of P_k: the final classes are built
explicitly and checked directly (x and y uncovered, every point between them
covered).  For each (k, j) we report the largest D such that every d <= D
succeeds.
"""
import json
import sys

import numpy as np

from stage6_scale import greedy_cover, primes_upto_count

sys.stdout.reconfigure(encoding="utf-8")
TRIES = 40


def match(U, free, x, y):
    """Bipartite matching: each exposed point gets its own admissible free prime."""
    owner = {}

    def augment(z, seen):
        for l in free:
            if l in seen or (z - x) % l == 0 or (y - z) % l == 0:
                continue
            seen.add(l)
            if l not in owner or augment(owner[l], seen):
                owner[l] = z
                return True
        return False

    return owner if all(augment(z, set()) for z in U) else None


def avoiding(p, x, y):
    return next(a for a in range(p) if a != x % p and a != y % p)


def check(cert, Q, free, owner, x, y):
    """Direct check of the final cover of the gap [x, y] at level k."""
    cls = {p: (avoiding(p, x, y) if p in Q else a) for p, a in cert.items()}
    for l in free:
        cls[l] = owner[l] % l if l in owner else avoiding(l, x, y)
    pts = np.arange(x + 1, y)
    covered = np.zeros(len(pts), dtype=bool)
    for p, a in cls.items():
        assert x % p != a and y % p != a, (p, x, y)
        covered |= pts % p == a
    assert covered.all(), (x, y)


def run(k, j):
    pr = primes_upto_count(k)
    odd, free = pr[1:j], pr[j:k]
    best = None
    for m in range(odd[-1] // 2, 3 * odd[-1]):
        cert = greedy_cover(odd, m)
        if cert:
            best = (m, cert)
    m, cert = best
    C = [frozenset()] * (m + 1)
    for i in range(1, m):
        C[i] = frozenset(p for p, a in cert.items() if i % p == a)
    w = [sum(1.0 / q for q in c) for c in C]
    first = [min(c) if c else 0 for c in C]
    ok = {}
    for d in range(1, m + 1):
        xs = sorted(range(m - d + 1), key=lambda x: w[x] + w[x + d])[:TRIES]
        ok[d] = False
        for x in xs:
            y = x + d
            Q = C[x] | C[y]
            U = []
            for q in Q:
                z = x + (cert[q] - x) % q
                if z == x:
                    z += q
                while z < y:
                    if first[z] == q and C[z] <= Q:
                        U.append(z)
                    z += q
            owner = match(U, free, x, y) if len(U) <= len(free) else None
            if owner is not None:
                check(cert, Q, free, owner, x, y)
                ok[d] = True
                break
    D = next((d - 1 for d in range(1, m + 1) if not ok[d]), m)
    return {"k": k, "p_k": pr[-1], "j": j, "p_j": pr[j - 1], "free_primes": len(free),
            "base_cover_gap": 2 * m, "all_even_t_up_to": 2 * D,
            "fraction_of_base": round(D / m, 3), "t_over_p_k": round(2 * D / pr[-1], 2),
            "reached": sum(ok.values()), "of": m}


if __name__ == "__main__":
    rows = []
    for k, j in [(60, 30), (60, 45), (100, 50), (100, 75), (100, 90), (200, 100), (200, 150),
                 (200, 180), (300, 150), (300, 225), (300, 270), (400, 300), (400, 360)]:
        row = run(k, j)
        rows.append(row)
        print(row, flush=True)
        json.dump(rows, open("stage7_transfer.json", "w"), indent=1)
