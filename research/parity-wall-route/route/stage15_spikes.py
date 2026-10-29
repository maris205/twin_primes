"""Stage 15: which of Guth's two "distinguishing features" of the frequencies {log n}
survive on the supports relevant to twin primes?

Guth (arXiv:2503.07410, Sec. 5.5 and 7): near sigma = 1/2 any improvement on the mean value
bound must use (a) spikes of the difference set {log n1 - log n2} at log(p/q), |p|,|q| <~ T/N
(exact coincidences q n1 = p n2), or (b) "no birthday paradox": distinct differences are
>= ~1/N^2 apart.  The almost counterexample (frequencies sqrt(n/N)) has neither.

For supports S in [N, 2N] (all integers, z-rough integers, primes) we measure
  spike mass  = fraction of off-diagonal ordered pairs (n1,n2) whose ratio n1/n2 is shared by
                another pair (exact multiplicative coincidence; at scale 1/T with T/N >= 2N
                these are exactly the spikes),
  min gap     = smallest gap between distinct differences, times N^2,
and the same for the almost-counterexample frequencies sqrt(n/N) (spike mass by rounding to
1e-11, i.e. exact coincidences such as the squares' arithmetic progression).

usage: python stage15_spikes.py N
"""
import sys, math, json
import numpy as np
from math import gcd

N = int(sys.argv[1])
ns = np.arange(N, 2 * N + 1)
sieve = np.ones(2 * N + 1, bool); sieve[:2] = False
for i in range(2, int((2 * N) ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
primes_small = np.nonzero(sieve)[0]

def rough(n, z):
    return all(n % p for p in primes_small[primes_small < z])

supports = {
    "all integers": ns,
    "z-rough, z=N^0.25": np.array([n for n in ns if rough(n, N ** 0.25)]),
    "z-rough, z=N^0.5": np.array([n for n in ns if rough(n, N ** 0.5)]),
    "primes": ns[sieve[N:2 * N + 1]],
}

def stats(S):
    a = S.astype(np.int64)
    n1, n2 = np.meshgrid(a, a, indexing="ij")
    off = n1 != n2
    g = np.gcd(n1, n2)
    key = (n1 // g) * (4 * N + 1) + (n2 // g)
    key = key[off]
    _, inv, cnt = np.unique(key, return_inverse=True, return_counts=True)
    spike_frac = float((cnt[inv] > 1).mean())
    d = np.unique(np.log(a[:, None] / a[None, :])[off].round(14))
    gap = float(np.diff(d).min() * N * N)
    return dict(size=int(len(a)), spike_mass=spike_frac, min_gap_times_N2=gap)

out = {name: stats(S) for name, S in supports.items()}
# almost counterexample: frequencies sqrt(n/N); exact coincidences of differences (to 1e-11)
f = np.sqrt(ns / N)
dd = (f[:, None] - f[None, :])[~np.eye(len(f), dtype=bool)]
_, inv, cnt = np.unique(np.round(dd * 1e11).astype(np.int64), return_inverse=True, return_counts=True)
dsort = np.unique(dd.round(14))
out["almost counterexample sqrt(n/N)"] = dict(size=len(f), spike_mass=float((cnt[inv] > 1).mean()),
                                               min_gap_times_N2=float(np.diff(dsort).min() * N * N))
for k, v in out.items():
    print(f"{k:34s} size={v['size']:6d}  spike mass={v['spike_mass']:.4f}  min gap*N^2={v['min_gap_times_N2']:.3g}")
json.dump(out, open("stage15_spikes.json", "w"), indent=1)
