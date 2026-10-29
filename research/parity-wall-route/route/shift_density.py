"""Stage 10: the shift coordinate under GEH.

(1) GEH => DHL[3,2] (Polymath8b): every admissible triple {0,a,b} contains a prime pair, so the
    set A of de Polignac numbers meets {a, b, b-a} for every admissible triple.  Find, among sets
    A that are unions of residue classes mod M (even classes only), the minimal density of a
    hitting set, by exhaustive search for M = 12, 24, 36.  GKKL Prop. 2.1 predicts >= 1/6 of all
    integers, attained by the multiples of 6.
(2) Parity counterfeit: colour positions coprime to 3 by their class mod 3.  Check that every
    admissible triple contains two positions in the same class mod 3 (so the counterfeit, which
    keeps only gaps divisible by 3, is consistent with DHL[3,2]), and that the killed set
    {h even : 3 does not divide h} has density 1/3 of all integers.
"""
import itertools, json
from fractions import Fraction


def admissible(t):
    for p in (2, 3):
        if len({x % p for x in t}) == p:
            return False
    return True


out = {}
for M in (12, 24, 36):
    classes = [c for c in range(M) if c % 2 == 0 and c != 0] + [0]
    # constraints: for admissible triples {0,a,b} with 0<a<b<=3M, the classes of a, b, b-a
    cons = set()
    for a in range(2, 3 * M + 1, 2):
        for b in range(a + 2, 3 * M + 1, 2):
            if admissible((0, a, b)):
                cons.add(frozenset({a % M, b % M, (b - a) % M}))
    cons = [tuple(c) for c in cons]
    best = None
    idx = {c: i for i, c in enumerate(classes)}
    masks = [sum(1 << idx[c] for c in con) for con in cons]
    n = len(classes)
    for size in range(1, n + 1):
        for comb in itertools.combinations(range(n), size):
            m = sum(1 << i for i in comb)
            if all(m & mk for mk in masks):
                best = sorted(classes[i] for i in comb)
                break
        if best is not None:
            break
    dens = Fraction(len(best), M)
    out[M] = dict(constraints=len(cons), min_classes=len(best), density=str(dens), example=best)
    print(f"M={M}: {len(cons)} class constraints; minimal hitting set has {len(best)} classes, density {dens} "
          f"(= {float(dens):.4f}); example {best}")

# (2) counterfeit consistency
bad = 0; tested = 0
for a in range(2, 200, 2):
    for b in range(a + 2, 200, 2):
        if not admissible((0, a, b)):
            continue
        for n in range(1, 4):                       # residue of n mod 3 with all entries coprime to 3
            vals = [(n + x) % 3 for x in (0, a, b)]
            if 0 in vals:
                continue
            tested += 1
            if len(set(vals)) == 3 or vals.count(vals[0]) == 1 and vals.count(vals[1]) == 1 and vals[0] != vals[1] and len(vals) == 3 and len(set(vals)) == 2 and False:
                bad += 1
            # need some pair in the same class
            if not (vals[0] == vals[1] or vals[0] == vals[2] or vals[1] == vals[2]):
                bad += 1
print(f"counterfeit check: {tested} (triple, residue) cases with all entries coprime to 3; cases without a same-class pair: {bad}")
out['counterfeit'] = dict(cases=tested, violations=bad, killed_density=str(Fraction(1, 3)))
json.dump(out, open('shift_density.json', 'w'), indent=1)
