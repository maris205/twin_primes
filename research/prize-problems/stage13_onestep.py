"""Stage 13: what does the last prime p_k do inside a maximal-gap cover?

Model of stage 1 (Lemma 1.1): a gap t = 2m at level k is a choice of classes
c_p (mod p) for the odd primes p <= p_k, at most one per prime, such that every
i in 1..m-1 has i = c_p (mod p) for some p, while 0 and m are hit by no class.

For each k we take one cover of the maximal gap t = J(k) (from the MILP of
stage 1) and delete p_k. The points no longer covered,
    E = { i in 1..m-1 : i is covered by p_k only },
all lie in one class mod p_k. They cut [0, m] into |E| + 1 segments; each
segment [x, y] is itself a gap of length 2(y - x) at level k - 1, so
2(y - x) <= J(k - 1). Hence the elementary bound
    J(k) <= (|E| + 1) J(k - 1).
We record |E| and the segment lengths as fractions of J(k - 1): a "jump"
J(k) >= C J(k-1) needs at least C segments, each a long (k-1)-level gap,
built from ONE class assignment of p_1..p_{k-1} and spaced along an
arithmetic progression of difference p_k.

Writes stage13_onestep.json.
"""
import json
import sys
import time

from stage1_gap_milp import gap_occurs_milp
from stage1_gap_solver import A048670, PR, check_certificate

sys.stdout.reconfigure(encoding="utf-8")

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 22
rows = []
for k in range(6, KMAX + 1):
    t = A048670[k - 1]
    Jprev = A048670[k - 2]
    m = t // 2
    pk = PR[k - 1]
    t0 = time.time()
    ok, cert = gap_occurs_milp(k, t, time_limit=1200)
    if not ok:
        print(k, "no certificate", ok)
        continue
    check_certificate(k, t, cert)
    cert = {int(p): int(c) for p, c in cert.items()}
    small = {p: c for p, c in cert.items() if p != pk}
    E = [i for i in range(1, m) if all(i % p != c % p for p, c in small.items())]
    assert all(i % pk == cert[pk] % pk for i in E), "E not in one class of p_k"
    cuts = [0] + E + [m]
    seg = [2 * (b - a) for a, b in zip(cuts, cuts[1:])]
    assert max(seg) <= Jprev, (k, seg, Jprev)
    rows.append({
        "k": k, "p_k": pk, "J": t, "J_prev": Jprev, "ratio": round(t / Jprev, 4),
        "E_size": len(E), "E": E,
        "segments": seg, "segments_over_Jprev": [round(s / Jprev, 3) for s in seg],
        "longest_over_Jprev": round(max(seg) / Jprev, 3),
        "second_longest_over_Jprev": round(sorted(seg)[-2] / Jprev, 3) if len(seg) > 1 else 0,
        "bound_(E+1)Jprev_over_J": round((len(E) + 1) * Jprev / t, 3),
        "seconds": round(time.time() - t0, 1),
    })
    r = rows[-1]
    print(k, pk, "J", t, "Jprev", Jprev, "ratio", r["ratio"], "|E|", len(E),
          "seg/Jprev", r["segments_over_Jprev"], "%.1fs" % r["seconds"], flush=True)

with open(__file__.replace(".py", ".json"), "w", encoding="utf-8") as fh:
    json.dump(rows, fh, indent=1)
