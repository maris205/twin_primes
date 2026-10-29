"""Stage 8: fast falsification tests for the numeric H-cards.

Data: pairs (m, m+2) with both entries x^eta-rough, m <= X, target y = lambda(m) lambda(m+2).
On rough integers lambda is (-1)^Omega, so y carries exactly the twin parity information of
Theorem C.  Split the pairs at random into train and test halves.

H10 (Braverman / bounded independence): can a function of the residues of m modulo small
     primes predict y?  (a) additive model: sum over primes q <= 97 of the centred train mean of
     y in the class of m mod q; (b) joint model: train mean of y in the class of m mod 30030,
     shrunk towards 0.  Report the held-out correlation and its z-score.
H16 ("AI search"): correlation of y with a dictionary of simple features (Legendre symbols of m
     and of m(m+2) mod primes q < 1000, digit-sum parities in bases 2..16, m mod k classes for
     k <= 30), Bonferroni threshold at the 1% level.
H15 (Hardy-Littlewood-Chowla transfer): share of the sum over primes p <= X of mu(p+2) that
     comes from x^eta-rough p+2, and its trend with X.
Positive control for H10 and H16: plant y' = y * s(m) on half of the train/test pairs, with
     s(m) = +1 or -1 according to m mod 7 (H10) or the Legendre symbol (m|101) (H16).

usage: python stage8_cards.py X eta
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); ETA = float(sys.argv[2])
Z = X ** ETA
rng = np.random.default_rng(8)
t0 = time.time()
plist = primes_upto(int((X + 4) ** 0.5) + 1)
lam = np.empty(X + 3, np.int8); rough = np.zeros(X + 3, bool); sqf = np.zeros(X + 3, bool); isp = np.zeros(X + 3, bool)
SEG = 10_000_000
for a in range(1, X + 3, SEG):
    b = min(a + SEG, X + 3)
    om, sq, spf = factor_info(a, b, plist)
    lam[a:b] = 1 - 2 * (om % 2); rough[a:b] = spf >= Z; sqf[a:b] = sq; isp[a:b] = (om == 1)
print(f"tables to {X:.0e}: {time.time()-t0:.0f}s", flush=True)

m = np.nonzero(rough[3:X + 1] & rough[5:X + 3])[0] + 3          # m and m+2 rough
m = m[m >= X // 10]
y = (lam[m] * lam[m + 2]).astype(np.float64)
N = len(m)
tr = rng.random(N) < 0.5; te = ~tr
out = dict(X=X, eta=ETA, pairs=int(N), mean_y=float(y.mean()))
print(f"rough pairs: {N}, mean y = {y.mean():+.4f}", flush=True)


def heldout(pred, target):
    p = pred[te] - pred[te].mean(); t = target[te] - target[te].mean()
    c = float((p * t).sum() / math.sqrt((p * p).sum() * (t * t).sum() + 1e-300))
    return c, c * math.sqrt(te.sum())


def additive_pred(target):
    pred = np.zeros(N)
    mu = target[tr].mean()
    for q in [int(p) for p in plist if 3 <= p <= 97]:
        r = m % q
        s = np.bincount(r[tr], weights=target[tr] - mu, minlength=q)
        c = np.bincount(r[tr], minlength=q)
        pred += np.where(c[r] > 0, s[r] / np.maximum(c[r], 1), 0.0)
    return pred


def joint_pred(target, M=30030, k=50.0):
    r = m % M
    mu = target[tr].mean()
    s = np.bincount(r[tr], weights=target[tr] - mu, minlength=M)
    c = np.bincount(r[tr], minlength=M)
    return s[r] / (c[r] + k)


# H10
plant7 = np.where(m % 7 < 3, 1.0, -1.0)
mask = rng.random(N) < 0.5
y_pc = np.where(mask, y * 0 + plant7, y)       # control: half of the targets replaced by a residue rule
res = {}
for name, f in [('additive', additive_pred), ('joint30030', joint_pred)]:
    c, z = heldout(f(y), y); cc, zc = heldout(f(y_pc), y_pc)
    res[name] = dict(corr=c, z=z, control_corr=cc, control_z=zc)
    print(f"H10 {name:10s}: held-out corr={c:+.5f} z={z:+.2f}   [control corr={cc:+.4f} z={zc:+.1f}]", flush=True)
out['H10'] = res


# H16 dictionary scan
def legendre_table(q):
    t = np.zeros(q, np.int8)
    sq = set((i * i) % q for i in range(1, q))
    for r in range(1, q):
        t[r] = 1 if r in sq else -1
    return t


yc = y - y.mean()
ycn = math.sqrt((yc * yc).sum())
best = []


def score(name, f):
    fc = f - f.mean()
    den = math.sqrt((fc * fc).sum()) * ycn
    if den > 0:
        c = float((fc * yc).sum() / den)
        best.append((abs(c) * math.sqrt(N), c, name))


for q in [int(p) for p in plist if 3 <= p < 1000]:
    L = legendre_table(q).astype(np.float64)
    a = L[m % q]
    score(f'(m|{q})', a)
    score(f'(m(m+2)|{q})', a * L[(m + 2) % q])
for base in range(2, 17):
    s = np.zeros(N, np.int64); v = m.copy()
    while (v > 0).any():
        s += v % base; v //= base
    score(f'digitsum_b{base}', (1 - 2 * (s % 2)).astype(np.float64))
    del s, v
for k in range(2, 31):
    rk = m % k
    for r in range(k):
        f = (rk == r).astype(np.float64)
        if 0 < f.sum() < N:
            score(f'm={r}mod{k}', f)
best.sort(reverse=True)
nf = len(best)
thr = math.sqrt(2) * 2.5758 if nf < 2 else math.sqrt(2 * math.log(nf / 0.01))
# control: plant Legendre (m|101) on half of the pairs and rescan only that feature
L101 = legendre_table(101)[m % 101].astype(np.float64)
y_pc16 = np.where(mask, L101, y); ycc = y_pc16 - y_pc16.mean(); fc = L101 - L101.mean()
zc16 = float((fc * ycc).sum() / math.sqrt((fc * fc).sum() * (ycc * ycc).sum())) * math.sqrt(N)
out['H16'] = dict(n_features=nf, bonferroni_threshold=thr, top=[dict(feature=n, corr=c, z=z) for z, c, n in best[:8]], control_z=zc16)
print(f"H16: {nf} features, Bonferroni |z| threshold {thr:.2f}; top: " + ", ".join(f"{n} z={z:.2f}" for z, c, n in best[:5]) + f"   [control z={zc16:.1f}]", flush=True)

# H15: share of sum_p mu(p+2) from rough p+2
res15 = []
for lim in [X // 100, X // 10, X]:
    p = np.nonzero(isp[3:lim + 1])[0] + 3
    mu2 = np.where(sqf[p + 2], lam[p + 2], 0).astype(np.float64)
    r2 = rough[p + 2]
    res15.append(dict(x=lim, primes=int(len(p)), sum_all=float(mu2.sum()), rough_share_of_primes=float(r2.mean()),
                      sum_rough=float(mu2[r2].sum()), mean_rough=float(mu2[r2].mean())))
    print(f"H15 x={lim:.0e}: sum mu(p+2)/pi = {mu2.sum()/len(p):+.5f}; share of p with p+2 rough = {r2.mean():.4f}; "
          f"mean mu(p+2) on rough p+2 = {mu2[r2].mean():+.4f}", flush=True)
out['H15'] = res15
json.dump(out, open(f'stage8_cards_{X:.0e}.json'.replace('+', ''), 'w'), indent=1)
print(f"done {time.time()-t0:.0f}s")
