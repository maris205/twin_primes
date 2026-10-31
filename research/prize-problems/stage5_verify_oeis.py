"""Witnesses and independent non-gap checks for OEIS A389839, n = 2..26 (stage 5).

For each k and each even t <= J(k) (J = A048670):
  - gap: store a witness n with gcd(n, P_k) = gcd(n+t, P_k) = 1 and
    gcd(n+j, P_k) > 1 for 0 < j < t (P_k = prime(k)#); n comes from the MILP
    certificate and is re-checked here;
  - non-gap: the covering program of Lemma 1.1 must be infeasible for two
    independent solvers, HiGHS (scipy) and CP-SAT (OR-Tools).
a(k) = smallest even non-gap; if every even t <= J(k) is a gap, a(k) = J(k) + 2,
which is not a gap because J(k) is the largest gap.
Output: a389839_witnesses.json (checked by the stdlib-only verify_a389839.py).
"""
import json
import math
import sys
import time

from ortools.sat.python import cp_model

from stage1_gap_milp import gap_occurs_milp
from stage1_gap_solver import A048670, PR

sys.stdout.reconfigure(encoding="utf-8")


def witness_from_cert(k, t, cert):
    m = t // 2
    odd = PR[1:k]
    P, n = 1, 0
    mods = [(2, 1)]
    for p in odd:
        c = cert.get(p)
        if c is None:
            c = next(x for x in range(1, p) if x != m % p)
        mods.append((p, (-2 * c) % p))
    for p, r in mods:
        while n % p != r:
            n += P
        P *= p
    return n, P


def is_gap_witness(n, t, P):
    return (math.gcd(n, P) == 1 and math.gcd(n + t, P) == 1
            and all(math.gcd(n + j, P) > 1 for j in range(1, t)))


def cpsat_feasible(k, t, time_limit=3600):
    m = t // 2
    pts = m - 1
    odd = PR[1:k]
    model = cp_model.CpModel()
    x = {}
    for p in odd:
        cls = [c for c in range(1, p) if c != m % p and c <= pts]
        for c in cls:
            x[p, c] = model.NewBoolVar(f"x{p}_{c}")
        if cls:
            model.AddAtMostOne([x[p, c] for c in cls])
    for i in range(1, pts + 1):
        lits = [x[p, i % p] for p in odd if (p, i % p) in x]
        model.AddBoolOr(lits)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_workers = 8
    st = solver.Solve(model)
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return True
    if st == cp_model.INFEASIBLE:
        return False
    return None


if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or list(range(2, 27))
    try:
        out = json.load(open("a389839_witnesses.json"))
    except Exception:
        out = {}
    for k in ks:
        t0 = time.time()
        J = A048670[k - 1]
        wit, nongap = {}, {}
        for t in range(2, J + 1, 2):
            ok, cert = gap_occurs_milp(k, t)
            if ok:
                n, P = witness_from_cert(k, t, cert)
                assert is_gap_witness(n, t, P), (k, t)
                wit[str(t)] = str(n)
            elif ok is False:
                cp = cpsat_feasible(k, t)
                nongap[str(t)] = {"highs": "infeasible",
                                  "cpsat": {False: "infeasible", True: "FEASIBLE", None: "timeout"}[cp]}
                assert cp is not True, ("solvers disagree", k, t)
            else:
                raise RuntimeError(("highs timeout", k, t))
        missing = sorted(int(t) for t in nongap)
        rec = {"k": k, "p_k": PR[k - 1], "J": J,
               "a": missing[0] if missing else J + 2,
               "missing_up_to_J": missing, "nongap_checks": nongap,
               "witness_n": wit, "seconds": round(time.time() - t0, 1)}
        out[str(k)] = rec
        print({kk: v for kk, v in rec.items() if kk != "witness_n"}, flush=True)
        json.dump(out, open("a389839_witnesses.json", "w"), indent=1)
