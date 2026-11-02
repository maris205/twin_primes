"""Longer CP-SAT re-check of the non-gaps that timed out in stage5_verify_oeis.py.

Model = cpsat_feasible in stage5_verify_oeis.py, plus two sound additions:
  * mirror symmetry break: c -> m - c (mod p) for every p maps solutions to
    solutions, so the largest prime q may be restricted to classes c with
    c <= (m - c) mod q (or left unused);
  * redundant counting constraint: the classes used must hit at least m - 1
    points in total.
Results are appended to stage5_cpsat_long.json.

Usage: python -B stage5_cpsat_long.py time_limit k:t [k:t ...]
"""
import json
import sys
import time

from ortools.sat.python import cp_model

from stage1_gap_solver import PR


def cpsat_long(k, t, time_limit, workers=16):
    m = t // 2
    pts = m - 1
    odd = PR[1:k]
    q = odd[-1]
    model = cp_model.CpModel()
    x, weight = {}, []
    for p in odd:
        cls = [c for c in range(1, p) if c != m % p and c <= pts]
        if p == q:
            cls = [c for c in cls if c <= (m - c) % q]
        for c in cls:
            x[p, c] = model.NewBoolVar(f"x{p}_{c}")
            weight.append((x[p, c], len(range(c, pts + 1, p))))
        if cls:
            model.AddAtMostOne([x[p, c] for c in cls])
    for i in range(1, pts + 1):
        model.AddBoolOr([x[p, i % p] for p in odd if (p, i % p) in x])
    model.Add(sum(w * v for v, w in weight) >= pts)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_workers = workers
    st = solver.Solve(model)
    return {cp_model.INFEASIBLE: "infeasible", cp_model.OPTIMAL: "feasible",
            cp_model.FEASIBLE: "feasible"}.get(st, "timeout")


if __name__ == "__main__":
    limit = float(sys.argv[1])
    path = "stage5_cpsat_long.json"
    try:
        out = json.load(open(path))
    except Exception:
        out = []
    for arg in sys.argv[2:]:
        k, t = map(int, arg.split(":"))
        t0 = time.time()
        res = cpsat_long(k, t, limit)
        rec = {"k": k, "t": t, "time_limit": limit, "cpsat": res,
               "seconds": round(time.time() - t0, 1)}
        print(rec, flush=True)
        if limit >= 3600:
            out.append(rec)
            json.dump(out, open(path, "w"), indent=1)
