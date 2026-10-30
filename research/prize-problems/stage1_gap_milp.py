"""Decide the covering problem of Lemma 1.1 with a 0-1 integer program (scipy / HiGHS).

Variables x[p, c] for odd primes p <= p_k and classes c not in {0, m mod p}.
Each prime takes at most one class; each point i in [1, m-1] is covered by
some chosen class. Feasible <=> the gap t = 2m occurs. Feasible solutions are
returned as certificates and checked independently with check_certificate.
"""
import json
import sys
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

from stage1_gap_solver import A048670, PR, check_certificate


def gap_occurs_milp(k, t, time_limit=600):
    m = t // 2
    pts = m - 1
    if pts <= 0:
        return True, {}
    odd = PR[1:k]
    var = []
    for p in odd:
        for c in range(1, p):
            if c != m % p and c <= pts:
                var.append((p, c))
    nv = len(var)
    rows = len(odd) + pts
    A = lil_matrix((rows, nv))
    lo = np.zeros(rows)
    hi = np.zeros(rows)
    pidx = {p: j for j, p in enumerate(odd)}
    for v, (p, c) in enumerate(var):
        A[pidx[p], v] = 1
        i = c
        while i <= pts:
            A[len(odd) + i - 1, v] = 1
            i += p
    lo[:len(odd)] = 0
    hi[:len(odd)] = 1
    lo[len(odd):] = 1
    hi[len(odd):] = np.inf
    res = milp(c=np.zeros(nv), constraints=LinearConstraint(A.tocsr(), lo, hi),
               integrality=np.ones(nv), bounds=Bounds(0, 1),
               options={"time_limit": time_limit, "presolve": True})
    if res.status == 0 and res.x is not None:
        cert = {var[v][0]: var[v][1] for v in range(nv) if res.x[v] > 0.5}
        return True, cert
    if res.status == 2:  # infeasible
        return False, None
    return None, None


if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]]
    try:
        out = json.load(open("stage1_gap_sets.json"))
    except Exception:
        out = {}
    for k in ks:
        t0 = time.time()
        jac = A048670[k - 1]
        missing, unknown, beyond = [], [], None
        for t in range(2, jac + 3, 2):
            ok, cert = gap_occurs_milp(k, t)
            if t == jac + 2:
                beyond = ok
                continue
            if ok:
                assert check_certificate(k, t, cert), (k, t)
            elif ok is False:
                missing.append(t)
            else:
                unknown.append(t)
        rec = {"k": k, "p_k": PR[k - 1], "jacobsthal": jac,
               "smallest_missing_even": (missing[0] if missing else jac + 2) if not unknown else None,
               "missing_up_to_max": missing, "unknown": unknown,
               "jac_plus_2_is_gap": beyond, "method": "milp",
               "seconds": round(time.time() - t0, 1)}
        out[str(k)] = rec
        print(rec, flush=True)
        json.dump(out, open("stage1_gap_sets.json", "w"), indent=1)
