"""Dynamics route, stage 1: two quick numerical checks.

D1 (sieve encodings).  The exact count of n <= x with n, n+2 both coprime to every prime <= sqrt(x) is the
twin count (above sqrt(x)); a sieve-encoding model that treats the residue conditions as independent predicts
    E(x) = (x/2) * prod_{3 <= p <= sqrt(x)} (1 - 2/p),
whose asymptotic is 8 C2 e^{-2 gamma} x / log^2 x, a factor 4 e^{-2 gamma} = 1.2609 above the Hardy-Littlewood
value 2 C2 x / log^2 x.  We print pi_2(x) / E(x) (expected limit e^{2 gamma}/4 = 0.7931) and
pi_2(x) / (2 C2 Li_2(x)).

D3 (spectral side).  Short-interval variances of psi, the prime-side counterpart of the pair correlation of
zeros (Goldston-Montgomery), are Fejer averages of the gap correlations S(k) = sum_{n<=x} Lambda(n) Lambda(n+k)
(primes only).  We compute S(k) for k <= K and the Fejer averages V(h) = sum_{|k|<h} (1 - |k|/h) S(k) / x, and
report how much V(h) moves when S(2) is set to 0 (the twin counterfeit at the single gap 2).

usage: python stage1_clear.py X K
"""
import sys, json, math
import numpy as np

X = int(float(sys.argv[1])); K = int(sys.argv[2])
s = np.ones(X + K + 1, bool); s[:2] = False
for i in range(2, int((X + K) ** 0.5) + 1):
    if s[i]: s[i * i::i] = False
primes = np.nonzero(s)[0]
gamma, C2 = 0.5772156649015329, 0.6601618158468696
out = dict(X=X, K=K, d1=[], d3={})

for x in [10 ** e for e in range(4, int(math.log10(X)) + 1)]:
    tw = int(np.sum(s[3:x - 1] & s[5:x + 1]))                  # pairs (p, p+2) with p+2 <= x
    ps = primes[(primes >= 3) & (primes <= math.isqrt(x))]
    E = x / 2 * float(np.prod(1 - 2 / ps))
    t = np.linspace(2, x, 200001); li2 = float(np.trapz(1 / np.log(t) ** 2, t))
    row = dict(x=x, pi2=tw, sieve_product=E, ratio_to_product=tw / E, ratio_to_HL=tw / (2 * C2 * li2))
    out["d1"].append(row); print(row, flush=True)
out["limit_e2gamma_over_4"] = math.exp(2 * gamma) / 4

lam = np.zeros(X + K + 1); lam[primes] = np.log(primes)
S = np.array([float(lam[:X + 1] @ lam[k:X + 1 + k]) for k in range(K + 1)])
for h in [10, 30, 100, 300, 1000, K]:
    k = np.arange(-h + 1, h); w = 1 - np.abs(k) / h
    V = float(np.sum(w * S[np.abs(k)])) / X
    S0 = S.copy(); S0[2] = 0.0
    V0 = float(np.sum(w * S0[np.abs(k)])) / X
    out["d3"][h] = dict(V=V, V_without_gap2=V0, relative_change=(V - V0) / V, gap2_weight=float(2 * (1 - 2 / h) / np.sum(w)))
    print(h, out["d3"][h], flush=True)
out["S_small_k_over_x"] = {int(k): float(S[k] / X) for k in range(0, 13)}
json.dump(out, open(f"stage1_clear_{X:.0e}.json", "w"), indent=1)
