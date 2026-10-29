"""Stage 6 A: the three pairs inside the admissible triple (n, n+2, n+6).

For n in (X/10, X] count prime pairs in each position with the third entry z-rough:
    C2 = #{n, n+2 prime, n+6 z-rough},  C4 = #{n+2, n+6 prime, n z-rough},
    C6 = #{n, n+6 prime, n+2 z-rough},
and the unconditional pair counts.  Inside an admissible triple the 3-adic factor is the same for
all three positions, so the random model predicts C2 : C4 : C6 = 1 : 1 : 1, while the
unconditional gap-6 count is twice the gap-2 count (singular series).
Also reports E[#primes in triple | all three entries z-rough], the quantity that Maynard-Tao
weights must push above 1.

usage: python triple_pairs.py X
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1]))
ETAS = [0.1, 0.2, 0.3]
SEG = 10_000_000
t0 = time.time()
plist = primes_upto(int((X + 8) ** 0.5) + 1)
acc = {e: dict(C2=0, C4=0, C6=0, rough3=0, primes_in_rough3=0) for e in ETAS}
U = dict(P2=0, P4=0, P6=0)
for a in range(X // 10 + 1, X + 1, SEG):
    b = min(a + SEG, X + 1)
    om, sqf, spf = factor_info(a, b + 6, plist)
    m = b - a
    pr = (om == 1)
    p0, p2, p6 = pr[:m], pr[2:m + 2], pr[6:m + 6]
    U['P2'] += int((p0 & p2).sum()); U['P4'] += int((p2 & p6).sum()); U['P6'] += int((p0 & p6).sum())
    for e in ETAS:
        z = X ** e
        r = spf >= z
        r0, r2, r6 = r[:m], r[2:m + 2], r[6:m + 6]
        A = acc[e]
        A['C2'] += int((p0 & p2 & r6).sum()); A['C4'] += int((p2 & p6 & r0).sum()); A['C6'] += int((p0 & p6 & r2).sum())
        R3 = r0 & r2 & r6
        A['rough3'] += int(R3.sum())
        A['primes_in_rough3'] += int((p0.astype(np.int64) + p2 + p6)[R3].sum())
    print(f"to {b}: {time.time()-t0:.0f}s", flush=True)

out = dict(X=X, unconditional=U, rows=[])
print(f"unconditional pairs: gap2={U['P2']} gap4={U['P4']} gap6={U['P6']}  ratio 6/2={U['P6']/U['P2']:.3f} (model 2)")
for e in ETAS:
    A = acc[e]
    r = dict(eta=e, **A, ratio_4_2=A['C4'] / A['C2'], ratio_6_2=A['C6'] / A['C2'],
             mean_primes=A['primes_in_rough3'] / A['rough3'])
    out['rows'].append(r)
    print(f"eta={e}: C2={A['C2']} C4={A['C4']} C6={A['C6']}  C4/C2={r['ratio_4_2']:.4f}  C6/C2={r['ratio_6_2']:.4f}"
          f"  E[#primes | rough triple]={r['mean_primes']:.4f}")
json.dump(out, open(f'triple_pairs_{X:.0e}.json'.replace('+', ''), 'w'), indent=1)
