"""Stage 32: how does the spectral norm of the HR operator restricted to rough support grow with V?

Window n in (N, 2N], z-rough vertices R.  Dilator set D (primes in [z, Dmax], or all z-rough d in [z, Dmax]),
V = sum_{d in D} 1/d.
  (A f)(n) = sum_{d in D, d | n} f(n+2d) + f(n-2d)          (divisibility edges; symmetric)
  (M f)(n) = sum_{d in D} (f(n+2d) + f(n-2d)) / d            (random comparison; FFT convolution)
  B = 1_X (A - M) 1_X,   X = R minus an exceptional set: q > 0 removes the top fraction q by full degree,
  q < 0 removes vertices whose full degree exceeds |q| times its mean 2V (an HR-style local condition).
We report V, the rough average degree d_R = <1_X, A 1_X>/|X|, ||B|| by power iteration on B^2, and the two
candidate scales: full-graph sqrt(2V) (HR, Pilatte form) and sparse sqrt(d_R).  The certificate resolution is
||B|| / d_R; the sparse scale would give 1/sqrt(d_R), the full-graph scale sqrt(2V)/d_R.

usage: python stage32_sparse_spectrum.py N z Dmax kind q [zD]   (kind = primes | rough)
  zD: roughness of the dilators (default z).  z = 2 with zD > 2 gives the full HR graph (all n) as a control.
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

N = int(float(sys.argv[1])); Z = int(sys.argv[2]); DMAX = int(float(sys.argv[3])); KIND = sys.argv[4]
Q = float(sys.argv[5]); ZD = int(sys.argv[6]) if len(sys.argv) > 6 else Z
pad = 2 * DMAX + 2
lo, hi = N + 1 - pad, 2 * N + 1 + pad                # index i <-> n = lo + i
om, _, spf = factor_info(lo, hi, primes_upto(int(hi ** 0.5) + 1))
n = np.arange(lo, hi); S = len(n)
R = (spf >= Z) & (n > N) & (n <= 2 * N)
if KIND == "primes":
    D = [int(p) for p in primes_upto(DMAX) if p >= ZD]
else:
    _, _, sd = factor_info(1, DMAX + 1, primes_upto(int(DMAX ** 0.5) + 1))
    D = [d for d in range(ZD, DMAX + 1) if sd[d - 1] >= ZD]
V = sum(1 / d for d in D)

deg = np.zeros(S)                                    # full degree: number of d in D dividing n
for d in D:
    deg[(-lo) % d::d] += 2
X = R.copy()
if Q > 0:                                            # remove the top fraction Q by full degree
    cut = np.quantile(deg[R], 1 - Q)
    X &= deg <= cut
elif Q < 0:                                          # remove full degree > |Q| * mean full degree (2V)
    X &= deg <= -Q * 2 * sum(1 / d for d in D)
mask = X.astype(float)

kern = np.zeros(2 * pad + 1)                         # M as a convolution
for d in D:
    kern[pad + 2 * d] += 1 / d; kern[pad - 2 * d] += 1 / d
L2 = 1 << int(math.ceil(math.log2(S + len(kern))))
kf = np.fft.rfft(kern, L2)
def M(v):
    c = np.fft.irfft(np.fft.rfft(v, L2) * kf, L2)
    return c[pad:pad + S]
# divisibility edges restricted to X x X (B only sees them), as index arrays
I_, J_ = [], []
for d in D:
    ids = np.arange((-lo) % d, S, d)
    for sh in (2 * d, -2 * d):
        j = ids + sh; ok = (j >= 0) & (j < S)
        i2, j2 = ids[ok], j[ok]; keep = X[i2] & X[j2]
        I_.append(i2[keep].astype(np.int32)); J_.append(j2[keep].astype(np.int32))
I_ = np.concatenate(I_); J_ = np.concatenate(J_)
def A(v):
    return np.bincount(I_, weights=v[J_], minlength=S)
def B(v):
    w = v * mask
    return (A(w) - M(w)) * mask

dR = float(mask @ A(mask) / mask.sum())
rng = np.random.default_rng(32); v = rng.standard_normal(S) * mask; v /= np.linalg.norm(v)
est = []
for it in range(40):
    w = B(B(v)); nw = np.linalg.norm(w)
    est.append(math.sqrt(nw)); v = w / nw
normB = est[-1]
out = dict(N=N, z=Z, zD=ZD, Dmax=DMAX, kind=KIND, q=Q, dilators=len(D), V=V, logz=math.log(Z),
           rough=int(R.sum()), kept=int(X.sum()), removed_frac=1 - X.sum() / R.sum(), maxdeg_kept=float(deg[X].max()), d_R=dR, normB=normB,
           conv=[round(e, 4) for e in est[-4:]], full_scale=math.sqrt(2 * V), sparse_scale=math.sqrt(dR),
           ratio_full=normB / math.sqrt(2 * V), ratio_sparse=normB / math.sqrt(dR), resolution=normB / dR)
print(json.dumps(out))
with open("stage32_results.jsonl", "a") as fh: fh.write(json.dumps(out) + "\n")
