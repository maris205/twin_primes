"""Stage 22: rough-pair classes in delta-language (reads rough_classes_1e08.json from stage 6/Cor. 4.7).

Theorem C (on GEH): N(s,r') = M(s,r') * (1 + (delta-1)(-1)^{s+r'}), i.e. even classes carry the factor
delta and odd classes the factor 2 - delta, delta in [0,2].
 - An UPPER bound N <= c M for an odd class gives delta >= 2 - c: useful only if c < 2.
 - A LOWER bound N >= c M for an even class gives delta >= c: useful for any c > 0.
 - Chen-type combinations  N(1,1) + N(1,2) = M11 delta + M12 (2 - delta)  are >= 2 min(M11, M12) for every
   delta in [0,2]: parity-neutral, hence provable by sieve methods.
For each class we print the measured ratio N / M (= delta_hat or 2 - delta_hat), the sieve limit
(2 for every class: the counterfeits delta = 0 and delta = 2 double one parity), and the Chen minimum.

usage: python stage22_classes.py
"""
import json

d = json.load(open("rough_classes_1e08.json"))
out = []
for res in d["results"]:
    eta = res["eta"]; A = res["A"]
    rows = {(r["s"], r["r"]): r for r in res["rows"]}
    print(f"eta = {eta}:")
    for (s, rr), r in sorted(rows.items()):
        par = "even" if (s + rr) % 2 == 0 else "odd"
        ratio = r["delta_hat"] if par == "even" else 2 - r["delta_hat"]
        print(f"  ({s},{rr}) {par:4s} N={r['N']:>8d}  N/M={ratio:.4f}  delta_hat={r['delta_hat']:.4f}  sieve limit 2.000")
        out.append(dict(eta=eta, s=s, r=rr, parity=par, N=r["N"], ratio=ratio, delta_hat=r["delta_hat"]))
    if (1, 1) in rows and (1, 2) in rows:
        n11, n12 = rows[(1, 1)]["N"], rows[(1, 2)]["N"]
        m11, m12 = n11 / rows[(1, 1)]["delta_hat"], n12 / (2 - rows[(1, 2)]["delta_hat"])
        print(f"  Chen combination N(1,1)+N(1,2) = {n11 + n12};  delta-free minimum 2 min(M11,M12) = {2 * min(m11, m12):.0f}"
              f"  (ratio {(n11 + n12) / (2 * min(m11, m12)):.3f})")
json.dump(out, open("stage22_classes.json", "w"), indent=1)
