"""H3: multi-pattern parity linear program.

Entries 0..k-1 correspond to shifts (e.g. n, n+2, n+6[, n+8]); entry i is an
x^eta-rough number with s_i prime factors, s_i in 1..R.  Masses are normalised
by the product model prod nu_{s_i} (singular series cancel, see notes).

Variables:
  c_{ij}            pair parity parameter, pair mass N_{ij}(s_i,s_j) = 1 + c_ij*sig_i*sig_j
  N_S(s)            normalised mass of sub-pattern S (|S|>=3), one per s in [1..R]^S
  beta_{S,i}(s_-i)  one-sided parity coefficient of entry i given the others
Constraints:
  N_S(s) = N_{S-i}(s_{-i}) + beta_{S,i}(s_{-i}) * sig_i      for every |S|>=3, i in S
  all N >= 0 (pairs: 1 + c*sig*sig >= 0)
Objective: minimise / maximise c_{01} (twin parameter: delta_twin - 1 = c_01).
usage: python parity_lp.py
"""
import itertools, json
import numpy as np
from scipy.optimize import linprog


def build_and_solve(k, R, sense):
    entries = list(range(k))
    idx = {}
    def var(key):
        if key not in idx:
            idx[key] = len(idx)
        return idx[key]
    pairs = list(itertools.combinations(entries, 2))
    for p in pairs:
        var(('c', p))
    subsets = [S for m in range(3, k + 1) for S in itertools.combinations(entries, m)]
    for S in subsets:
        for s in itertools.product(range(1, R + 1), repeat=len(S)):
            var(('N', S, s))
        for i in S:
            rest = tuple(j for j in S if j != i)
            for s in itertools.product(range(1, R + 1), repeat=len(rest)):
                var(('b', S, i, s))
    nv = len(idx)
    sig = lambda s: 1 if s % 2 == 0 else -1

    def N_expr(S, s):
        """Linear expression (coef dict, const) for normalised mass of S at s."""
        if len(S) == 2:
            return {idx[('c', S)]: sig(s[0]) * sig(s[1])}, 1.0
        return {idx[('N', S, s)]: 1.0}, 0.0

    A_eq, b_eq, A_ub, b_ub = [], [], [], []
    for S in subsets:
        for s in itertools.product(range(1, R + 1), repeat=len(S)):
            for pos, i in enumerate(S):
                rest = tuple(j for j in S if j != i)
                s_rest = tuple(v for p_, v in enumerate(s) if p_ != pos)
                row = np.zeros(nv)
                row[idx[('N', S, s)]] += 1.0
                coef, const = N_expr(rest, s_rest)
                for v_, c_ in coef.items():
                    row[v_] -= c_
                row[idx[('b', S, i, s_rest)]] -= sig(s[pos])
                A_eq.append(row); b_eq.append(const)
            # positivity N_S(s) >= 0
            row = np.zeros(nv); row[idx[('N', S, s)]] = -1.0
            A_ub.append(row); b_ub.append(0.0)
    bounds = [(None, None)] * nv
    for p in pairs:
        bounds[idx[('c', p)]] = (-1.0, 1.0)          # pair masses 1 +- c >= 0
    obj = np.zeros(nv); obj[idx[('c', (0, 1))]] = 1.0 if sense == 'min' else -1.0
    res = linprog(obj, A_ub=np.array(A_ub) if A_ub else None, b_ub=b_ub or None,
                  A_eq=np.array(A_eq), b_eq=b_eq, bounds=bounds, method='highs')
    val = res.x[idx[('c', (0, 1))]] if res.success else None
    return res.status, val, res, idx


def check_witness(k, R):
    """Explicit 'independent extension' of the extreme twin counterfeit:
    N_S(s) = (1 - sig_0 sig_1) if {0,1} subset S, else 1; pairs: c_01=-1, others 0."""
    sig = lambda s: 1 if s % 2 == 0 else -1
    def N(S, s):
        d = dict(zip(S, s))
        return (1 - sig(d[0]) * sig(d[1])) if (0 in d and 1 in d) else 1.0
    worst = 0.0
    for m in range(3, k + 1):
        for S in itertools.combinations(range(k), m):
            for s in itertools.product(range(1, R + 1), repeat=m):
                val = N(S, s)
                if val < -1e-12:
                    return False, 'negative mass'
                for pos, i in enumerate(S):
                    rest = tuple(j for j in S if j != i)
                    s_rest = tuple(v for p_, v in enumerate(s) if p_ != pos)
                    base = N(rest, s_rest)
                    # need beta(s_rest) with val = base + beta*sig(s_i), beta independent of s_i:
                    beta = (val - base) * sig(s[pos])
                    for t in range(1, R + 1):
                        s2 = list(s); s2[pos] = t
                        v2 = N(S, tuple(s2))
                        worst = max(worst, abs(v2 - (base + beta * sig(t))))
    return worst < 1e-12, worst


if __name__ == '__main__':
    out = []
    for k, R in [(3, 2), (3, 3), (3, 4), (3, 6), (4, 2), (4, 3), (4, 4)]:
        st_min, cmin, _, idx = build_and_solve(k, R, 'min')
        st_max, cmax, _, _ = build_and_solve(k, R, 'max')
        ok, err = check_witness(k, R)
        row = dict(entries=k, R=R, n_vars=len(idx), status_min=int(st_min), c_twin_min=cmin,
                   status_max=int(st_max), c_twin_max=cmax,
                   delta_twin_range=[None if cmin is None else 1 + cmin, None if cmax is None else 1 + cmax],
                   witness_ok=ok, witness_err=err)
        out.append(row)
        print(f"k={k} R={R} vars={len(idx)}: c_twin in [{cmin}, {cmax}]  ->  delta_twin in "
              f"[{row['delta_twin_range'][0]}, {row['delta_twin_range'][1]}];  witness(delta=0) ok={ok} err={err}")
    json.dump(out, open('parity_lp.json', 'w'), indent=1)
    print('wrote parity_lp.json')
