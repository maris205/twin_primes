"""Dynamics route, stage 5: Buium's p-derivation delta_p(x) = (x - x^p)/p on Z.

Checks:
 (1) translation: delta_p(x + c) - delta_p(x) = delta_p(c) + C_p(x, c) with
     C_p(x, c) = (x^p + c^p - (x + c)^p)/p, a polynomial of degree p-1 in x that is non-zero mod p for c != 0 mod p;
     we count the residues x mod p at which delta_p(x+2) = delta_p(x) mod p.
 (2) periodicity: delta_p(n) mod p^k depends only on n mod p^(k+1)  (checked for small p, k).
 (3) the Pellet analogue: for odd squarefree n = p_1...p_k,
        s(n) = prod_i ( delta_{p_i}(n) / p_i )  (Legendre symbols)
     equals (-1)^{binom(k_3, 2)}, k_3 = #{i : p_i = 3 mod 4} (quadratic reciprocity), so it is a function of the
     chi_4-values of the prime factors only; we verify this and compare s with lambda on rough pairs.

usage: python stage5_buium.py X z
"""
import sys, json, math
import numpy as np
sys.path.insert(0, '../parity-wall-route/route')
from bilinear_probe import primes_upto

X = int(float(sys.argv[1])); Z = int(sys.argv[2])
leg = lambda a, p: 0 if a % p == 0 else (1 if pow(a % p, (p - 1) // 2, p) == 1 else -1)
def delta_mod(n, p, k):
    """delta_p(n) mod p^k, computed exactly from n mod p^(k+1)."""
    m = p ** (k + 1)
    return ((n - pow(n, p, m)) % m) // p % (p ** k)
out = {}

tr = {}
for p in [3, 5, 7, 11, 13, 101]:
    eq = sum(1 for x in range(p) if delta_mod(x + 2, p, 1) == delta_mod(x, p, 1))
    tr[p] = dict(residues=p, translation_invariant_at=eq)
out["translation"] = tr; print("translation", tr)

per = {}
for p in [3, 5, 7]:
    for k in [1, 2]:
        M = p ** (k + 1)
        ok = all(((n - n ** p) // p) % p ** k == ((n % M - (n % M) ** p) // p) % p ** k for n in range(1, 4 * M))
        per[f"p={p},k={k}"] = ok
out["periodicity"] = per; print("periodicity", per)

spf = np.zeros(X + 3, np.int64)
for q in primes_upto(X + 2):
    blk = spf[q::q]; blk[blk == 0] = q
def factor(n):
    f = []
    while n > 1:
        q = int(spf[n]); e = 0
        while n % q == 0: n //= q; e += 1
        f.append((q, e))
    return f
agree = tot = 0
s_val = np.zeros(X + 3, np.int64); lam = np.zeros(X + 3, np.int64)
for n in range(3, X + 3, 2):
    f = factor(n)
    lam[n] = (-1) ** sum(e for _, e in f)
    if any(e > 1 for _, e in f): continue
    s = 1
    for q, _ in f:
        s *= leg(delta_mod(n, q, 1), q)
    k3 = sum(1 for q, _ in f if q % 4 == 3)
    s_val[n] = s
    tot += 1; agree += (s == (-1) ** (k3 * (k3 - 1) // 2))
out["pellet_analogue"] = dict(squarefree_odd=tot, reciprocity_identity_holds=agree)
print("pellet analogue", out["pellet_analogue"])

R = spf >= Z
idx = [n for n in range(Z | 1, X + 1, 2) if R[n] and R[n + 2] and s_val[n] and s_val[n + 2]]
idx = np.array(idx, dtype=np.int64)
out["rough_pairs"] = dict(z=Z, pairs=len(idx),
    s_with_lambda=float(np.mean(s_val[idx] * lam[idx])),
    s_twin=float(np.mean(s_val[idx] * s_val[idx + 2])),
    lambda_twin=float(np.mean(lam[idx] * lam[idx + 2])))
print("rough pairs", out["rough_pairs"])
json.dump(out, open(f"stage5_buium_{X:.0e}.json", "w"), indent=1)
