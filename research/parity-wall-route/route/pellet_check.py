"""Check Pellet's formula over F_q[T] and its insensitivity to 'roughness'.

For monic squarefree f over F_q (q odd prime here):
    mu(f) = (-1)^{deg f} * chi(disc f),   chi = Legendre symbol mod q.
We verify it for all monic polynomials of degree <= DMAX, split by the minimal
degree of an irreducible factor (the function-field analogue of z-roughness).
usage: python pellet_check.py q DMAX
"""
import sys, itertools, json
from sympy import Poly, symbols, GF, discriminant

q = int(sys.argv[1]) if len(sys.argv) > 1 else 3
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 7
T = symbols('T')


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


res = {}
for d in range(1, DMAX + 1):
    for coeffs in itertools.product(range(q), repeat=d):
        f = Poly([1, *coeffs], T, modulus=q)
        fac = f.factor_list()[1]
        if any(e > 1 for _, e in fac):
            continue                        # not squarefree
        r = len(fac)
        mu = (-1) ** r
        mindeg = min(g.degree() for g, _ in fac)
        D = int(discriminant(Poly([1, *coeffs], T)).as_expr()) % q
        pred = (-1) ** d * legendre(D, q)
        key = (d, mindeg)
        ok, tot = res.get(key, (0, 0))
        res[key] = (ok + (mu == pred), tot + 1)

rows = []
for (d, m), (ok, tot) in sorted(res.items()):
    rows.append(dict(deg=d, min_factor_degree=m, matches=ok, total=tot))
    print(f"deg {d}, smallest irreducible factor degree {m}: Pellet holds {ok}/{tot}")
allok = all(r['matches'] == r['total'] for r in rows)
print("ALL MATCH" if allok else "MISMATCH FOUND")
json.dump(dict(q=q, dmax=DMAX, rows=rows, all_match=allok),
          open(f"pellet_check_q{q}_d{DMAX}.json", "w"), indent=1)
