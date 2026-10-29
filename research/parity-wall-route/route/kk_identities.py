"""4a: the K-weighted identities behind the quantitative Corollary C'.

L(n) = log^2 n on primes (= Lambda(n) log n), K(n) = 2 log p log q on squarefree n = pq
(= Lambda*Lambda on squarefree P2).  On the dyadic window n in (X/2, X]:
    S_AB = sum A(n) B(n+2),  A, B in {L, K}.
Bombieri's asymptotic sieve (k = (2)) applied to L(n+2), L(n-2), K(n+2) gives, with T0 the
common main term and delta the twin parity parameter (S_LL = delta T0):
    S_LL + S_KL = 2 T0,   S_LL + S_LK = 2 T0,   S_LK + S_KK = 2 T0'   (T0' = T0 (1 + O(1/log x)))
hence S_KK = S_LL + O((eps_B + 1/log x) T0).  We measure the four sums, the parity-free
combinations (I1) and the parity-tied identity (I2: S_KK / S_LL), and the size of the
deviations against 1/log X.

usage: python kk_identities.py X [X ...]
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

SEG = 10_000_000
out = []
for X in [int(float(a)) for a in sys.argv[1:]]:
    t0 = time.time()
    plist = primes_upto(int((X + 4) ** 0.5) + 1)
    S = dict(LL=0.0, LK=0.0, KL=0.0, KK=0.0)
    massL = massK = 0.0
    for a in range(X // 2 + 1, X + 1, SEG):
        b = min(a + SEG, X + 1)
        om, sqf, spf = factor_info(a, b + 2, plist)
        n = np.arange(a, b + 2, dtype=np.float64)
        ln = np.log(n)
        L = np.where(om == 1, ln * ln, 0.0)
        p = spf.astype(np.float64)
        K = np.where((om == 2) & sqf, 2 * np.log(p) * (ln - np.log(p)), 0.0)
        m = b - a
        S['LL'] += float((L[:m] * L[2:m + 2]).sum()); S['LK'] += float((L[:m] * K[2:m + 2]).sum())
        S['KL'] += float((K[:m] * L[2:m + 2]).sum()); S['KK'] += float((K[:m] * K[2:m + 2]).sum())
        massL += float(L[:m].sum()); massK += float(K[:m].sum())
    lx = math.log(X)
    Pi2 = 0.6601618158
    T_model = 2 * Pi2 * (X / 2) * lx ** 2            # HL size of S_LL on the window, leading order
    r = dict(X=X, logX=lx, **S, massL=massL, massK=massK, T_model=T_model)
    r['I1a'] = (S['LL'] + S['KL']) / (S['LK'] + S['KK'])     # parity-free: -> 1 (up to T0'/T0)
    r['I1b'] = (S['LL'] + S['KL']) / (S['LL'] + S['LK'])     # parity-free: -> 1
    r['I2'] = S['KK'] / S['LL']                              # parity-tied: delta / delta = 1
    r['T0_hat'] = (S['LL'] + S['KL']) / 2
    r['delta_hat'] = S['LL'] / r['T0_hat']
    r['KK_over_T0'] = S['KK'] / r['T0_hat']
    r['mass_ratio'] = massK / massL
    out.append(r)
    print(f"X={X:.0e}  S_LL/T0={S['LL']/r['T0_hat']:.4f}  S_KL/T0={S['KL']/r['T0_hat']:.4f}  S_LK/T0={S['LK']/r['T0_hat']:.4f}"
          f"  S_KK/T0={r['KK_over_T0']:.4f}  | I1a={r['I1a']:.4f} I1b={r['I1b']:.4f}  I2=S_KK/S_LL={r['I2']:.4f}"
          f"  massK/massL={r['mass_ratio']:.4f}  1/logX={1/lx:.4f}  ({time.time()-t0:.0f}s)", flush=True)
json.dump(out, open('kk_identities.json', 'w'), indent=1)
