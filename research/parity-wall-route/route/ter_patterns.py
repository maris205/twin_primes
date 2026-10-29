"""Channel 1: split Teravainen's dense correlation by smooth parts.

For y = X^eps write n = s(n) r(n), s(n) the y-smooth part.  Teravainen (Forum Math.
Sigma 2018, Remark 1.12) proves the dense log-average of lambda(r(n)) lambda(r(n+h)) is
o_{eps->0}(1).  Group pairs (n, n+2) by (s1, s2) = (s(n), s(n+2)):
    dense = sum_{s1,s2} w(s1,s2) c(s1,s2),
where c(s1,s2) is the conditional log-correlation of the rough parities.  The twin
cell is (1,1).  For fixed eps Teravainen's Theorem 1.4 gives dense = m1*m2 + o(1) (product
of mean values), so we also report per-cell one-point means and the two-point deviation
D(s1,s2) = c - mu1*mu2.  n runs over [X/R, X] (Teravainen averages over [x/omega(x), x]).

usage: python ter_patterns.py X eps
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); EPS = float(sys.argv[2])
Y = X ** EPS
S = 64                      # record cells with s1, s2 <= S
R = 100
SEG = 5_000_000
t0 = time.time()
plist = primes_upto(int((X + 4) ** 0.5) + 1)
small = [int(p) for p in plist if p < Y]

K = (S + 1) ** 2
wsum = np.zeros(K); csum = np.zeros(K); cnt = np.zeros(K); m1 = np.zeros(K); m2 = np.zeros(K)
dense_w = dense_c = dense_1 = dense_2 = 0.0
for a in range(X // R, X + 1, SEG):
    b = min(a + SEG, X + 1)
    om, _, _ = factor_info(a, b + 2, plist)
    n = np.arange(a, b + 2, dtype=np.int64)
    s = np.ones(len(n), np.int64); oms = np.zeros(len(n), np.int16)
    for p in small:
        pk = p
        while pk <= b + 2:
            st = (-a) % pk
            s[st::pk] *= p; oms[st::pk] += 1
            if pk > (b + 2) // p:
                break
            pk *= p
    lr = 1 - 2 * ((om - oms) % 2).astype(np.int64)
    m = len(n) - 2
    prod = lr[:m] * lr[2:m + 2]
    wt = 1.0 / n[:m]
    dense_w += wt.sum(); dense_c += (wt * prod).sum()
    dense_1 += (wt * lr[:m]).sum(); dense_2 += (wt * lr[2:m + 2]).sum()
    s1 = s[:m]; s2 = s[2:m + 2]
    ok = (s1 <= S) & (s2 <= S)
    key = (s1[ok] * (S + 1) + s2[ok]).astype(np.int64)
    wsum += np.bincount(key, weights=wt[ok], minlength=K)
    csum += np.bincount(key, weights=(wt * prod)[ok], minlength=K)
    cnt += np.bincount(key, minlength=K)
    m1 += np.bincount(key, weights=(wt * lr[:m])[ok], minlength=K)
    m2 += np.bincount(key, weights=(wt * lr[2:m + 2])[ok], minlength=K)
    print(f"to {b}: {time.time()-t0:.0f}s", flush=True)

rows = []
for k in np.nonzero(cnt)[0]:
    s1, s2 = divmod(int(k), S + 1)
    c = csum[k] / wsum[k]; a1 = m1[k] / wsum[k]; a2 = m2[k] / wsum[k]
    rows.append(dict(s1=s1, s2=s2, count=int(cnt[k]), w=wsum[k] / dense_w,
                     c=c, mu1=a1, mu2=a2, D=c - a1 * a2, noise=1 / math.sqrt(cnt[k])))
rows.sort(key=lambda r: -r['w'])
d1 = dense_1 / dense_w; d2 = dense_2 / dense_w
out = dict(X=X, eps=EPS, y=Y, R=R, dense=dense_c / dense_w, dense_mean1=d1, dense_mean2=d2,
           dense_D=dense_c / dense_w - d1 * d2, cells=rows[:60],
           w_recorded=sum(r['w'] for r in rows),
           wD_recorded=sum(r['w'] * r['D'] for r in rows))
json.dump(out, open(f'ter_patterns_{X:.0e}_eps{EPS}.json'.replace('+', ''), 'w'), indent=1)
print(f"dense corr = {out['dense']:+.5f}  means {d1:+.5f} {d2:+.5f}  dense D = {out['dense_D']:+.5f}")
print(f"y = {Y:.1f}, recorded weight {out['w_recorded']:.3f}, sum w*D over recorded cells {out['wD_recorded']:+.5f}")
for r in rows[:25]:
    print(f"({r['s1']:3d},{r['s2']:3d})  w={r['w']:.5f}  c={r['c']:+.4f}  mu={r['mu1']:+.3f},{r['mu2']:+.3f}  D={r['D']:+.4f}  noise~{r['noise']:.4f}  n={r['count']}")
