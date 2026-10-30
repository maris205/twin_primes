"""Constructive certificates for gaps t > p_k (Erdos #854, stage 2).

Positions 1 .. t+1 stand for n+1 .. n+t+1, and "p takes class c" means
p | n+i  <=>  i = c (mod p). The gap t occurs if positions 1 and t+1 are
uncovered and every position 2..t is covered (Lemma 1.1, original form).

The construction follows the proof of Theorem 2.1 (STAGE2_RANKIN.md):
  A. primes p in (z, w] take class 0, unless p | t+1 (then a class avoiding 1, t+1);
  B. primes q <= z take, one after another, the admissible class (not 1, not t+1 mod q)
     that covers the most remaining positions (greedy instead of random);
  C. primes p in (w, x] are matched to the remaining positions u, one prime per
     position, with p not dividing u-1 or t+1-u.
Several (z, w) are tried. Every success is checked by `verify`.
"""
import json
import sys

import numpy as np

from stage1_gap_solver import primes_upto

PR = primes_upto(200000)


def verify(k, t, cls):
    primes = PR[:k]
    cov = np.zeros(t + 2, dtype=bool)
    for p in primes:
        c = cls[p] % p
        if c == 1 % p or c == (t + 1) % p:
            return False
        start = c if c > 0 else p
        cov[start::p] = True
    return bool(cov[2:t + 1].all()) and not cov[1] and not cov[t + 1]


def attempt(k, t, z, w):
    primes = PR[:k]
    x = primes[-1]
    cls = {}
    unc = np.zeros(t + 2, dtype=bool)
    unc[2:t + 1] = True
    pos = np.arange(t + 2)

    def admissible(p, c):
        return c % p != 1 % p and c % p != (t + 1) % p

    # A: class 0 for medium primes
    for p in primes:
        if z < p <= w:
            if admissible(p, 0):
                cls[p] = 0
                unc[0::p] = False
                unc[1] = False
                unc[t + 1] = False
    # B: greedy classes for small primes, largest coverage first by increasing q
    for q in primes:
        if q > z:
            break
        idx = pos[unc]
        counts = np.bincount(idx % q, minlength=q)
        counts[1 % q] = -1
        counts[(t + 1) % q] = -1
        c = int(np.argmax(counts))
        cls[q] = c
        unc[(pos % q == c)] = False
    # medium primes that could not take class 0: greedy too
    for p in primes:
        if z < p <= w and p not in cls:
            idx = pos[unc]
            counts = np.bincount(idx % p, minlength=p)
            counts[1 % p] = -1
            counts[(t + 1) % p] = -1
            c = int(np.argmax(counts))
            cls[p] = c
            unc[(pos % p == c)] = False
    # C: match large primes to remaining positions (greedy, largest-degree-last)
    rest = [int(u) for u in pos[unc]]
    large = [p for p in primes if p > w]
    free = set(large)
    for u in rest:
        if unc[u] == False:
            continue
        cand = [p for p in free if (u - 1) % p and (t + 1 - u) % p]
        if not cand:
            return None
        p = max(cand)
        free.discard(p)
        cls[p] = u % p
        unc[(pos % p == u % p)] = False
        unc[1] = False if (1 - u) % p else unc[1]
    if unc[2:t + 1].any():
        return None
    for p in free:
        c = next(c for c in range(p) if admissible(p, c))
        cls[p] = c
    return cls


def certify(k, t):
    x = PR[k - 1]
    for wf in (0.5, 0.4, 0.6, 0.33, 0.7):
        w = wf * x
        for z in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101, 113, 127, 151, 181, 211):
            if z >= w:
                break
            cls = attempt(k, t, z, w)
            if cls is not None and verify(k, t, cls):
                return (round(wf, 2), z)
    return None


def certified_T(k, start=2):
    T = 0
    t = start
    while True:
        r = certify(k, t)
        if r is None:
            return T, t
        T = t
        t += 2


if __name__ == "__main__":
    out = []
    try:
        out = json.load(open("stage2_rankin_certify.json"))
    except Exception:
        pass
    for k in [int(a) for a in sys.argv[1:]]:
        pk = PR[k - 1]
        T, fail = certified_T(k)
        r = {"k": k, "p_k": pk, "certified_T": T, "first_uncertified": fail, "T_over_pk": round(T / pk, 3)}
        out = [o for o in out if o["k"] != k] + [r]
        print(r, flush=True)
        json.dump(sorted(out, key=lambda o: o["k"]), open("stage2_rankin_certify.json", "w"), indent=1)
