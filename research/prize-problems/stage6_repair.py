"""Stage 6, bridge two: deletion with repair, tested on maximal-gap covers.

Start from one cover of the maximal gap J(k) (sublattice model, m = J/2).
For a pair x < y, a set R of primes is released and given new classes that
avoid x and y; all other primes keep their classes.  2(y - x) is a gap if
the released primes can re-cover every point of (x, y) that the kept primes
miss.  Three choices of R, each containing the previous one:

  level 0  R = C(x) | C(y), new classes not used for covering (deletion lemma)
  level 1  R = C(x) | C(y)
  level 2  R = C(x) | C(y) | idle large primes, where a prime p > p_k/2 is
           idle for (x, y) if no z in (x, y) has C(z) inside C(x) | C(y) | {p}
  level 3  R = C(x) | C(y) | all primes > p_k/2

The small covering problems are solved with CP-SAT, 5 s each.  A sub-problem
that times out counts as not repaired; the number of timeouts is recorded.
"""
import json
import sys

from ortools.sat.python import cp_model

from stage1_gap_milp import gap_occurs_milp
from stage1_gap_solver import A048670, PR
from stage6_deletion import cover_sets

sys.stdout.reconfigure(encoding="utf-8")
TIMEOUTS = [0]


def repairable(C, x, y, R):
    """Can the primes of R, re-classed to avoid x and y, cover the exposed points?"""
    U = [z for z in range(x + 1, y) if C[z] <= R]
    if not U:
        return True
    model = cp_model.CpModel()
    hit = {z: [] for z in U}
    for p in R:
        cls = {}
        for z in U:
            a = z % p
            if a != x % p and a != y % p:
                if a not in cls:
                    cls[a] = model.NewBoolVar(f"{p}_{a}")
                hit[z].append(cls[a])
        if cls:
            model.AddAtMostOne(list(cls.values()))
    for z in U:
        if not hit[z]:
            return False
        model.AddBoolOr(hit[z])
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 5
    solver.parameters.num_workers = 1
    st = solver.Solve(model)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE, cp_model.INFEASIBLE):
        TIMEOUTS[0] += 1
        return False
    return st != cp_model.INFEASIBLE


def released(C, x, y, level, large):
    Q = C[x] | C[y]
    if level == 1:
        return Q
    if level == 3:
        return Q | large
    idle = {p for p in large - Q
            if all(not C[z] <= Q | {p} for z in range(x + 1, y))}
    return Q | idle


def run(k):
    J = A048670[k - 1]
    m = J // 2
    ok, cert = gap_occurs_milp(k, J)
    cert = {int(p): int(c) for p, c in cert.items()}
    C = cover_sets(k, m, cert)
    large = frozenset(p for p in PR[1:k] if p > PR[k - 1] / 2)
    reached = {}
    for d in range(1, m + 1):
        pairs = [(x, x + d) for x in range(m - d + 1)]
        lvl = None
        if any(all(not C[z] <= C[x] | C[y] for z in range(x + 1, y)) for x, y in pairs):
            lvl = 0
        else:
            for level in (1, 2, 3):
                if any(repairable(C, x, y, released(C, x, y, level, large)) for x, y in pairs):
                    lvl = level
                    break
        reached[2 * d] = lvl
    return J, reached


if __name__ == "__main__":
    true = json.load(open("a389839_witnesses.json"))
    rows = []
    for k in [int(a) for a in sys.argv[1:]] or range(8, 27):
        TIMEOUTS[0] = 0
        J, reached = run(k)
        G = {int(t) for t in true[str(k)]["witness_n"]}
        got = {t for t, l in reached.items() if l is not None}
        assert got <= G, (k, sorted(got - G))
        cum = [sum(1 for l in reached.values() if l is not None and l <= L) for L in range(4)]
        row = {"k": k, "p_k": PR[k - 1], "J": J, "true_gaps": len(G), "reached_up_to_level": cum,
               "true_gaps_not_reached": sorted(G - got), "timeouts": TIMEOUTS[0],
               "first_level": {str(t): l for t, l in reached.items()}}
        rows.append(row)
        print({a: b for a, b in row.items() if a != "first_level"}, flush=True)
        if len(rows) > 3:
            json.dump(rows, open("stage6_repair.json", "w"), indent=1)
