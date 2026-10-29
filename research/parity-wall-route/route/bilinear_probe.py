"""Direction 2 probe: Moebius on shifted primes, full vs rough, and FI-type Type II sums.

P1 (x = XMAX). For a roughness level z (z=1 means no restriction):
    A(z) = mean of mu(p+2)   over primes p <= x with mu^2(p+2)=1 and p+2 z-rough
    B(z) = mean of mu(n+2)   over all n <= x  with mu^2(n+2)=1 and n+2 z-rough
  z=1: A is the Lu-Wang-Wu statement (A -> 0), B -> 0 by the PNT.
  z=x^eta: B is the parity bias of rough numbers (nonzero for fixed eta);
  by Bombieri's one-sided structure A - B measures (minus) the one-sided
  parity parameter delta'-1 of the sequence 1_P(m-2) on rough shifted values.
P2 (x = XTYPE2). FI hypothesis (B)-type sums for N in a range, M = x/N:
    T_f(N) = sum_m | sum_{N<n<=2N} mu(n) f(mn+2) |  /  sum_m sum_n mu^2(n) |f(mn+2)|
  for f = 1_P (twins, the FI input), f = mu (Lu-Wang-Wu type), and a random-sign
  control (mu(n) replaced by independent signs on squarefree n).

usage: python bilinear_probe.py XMAX XTYPE2
"""
import sys, json, time, math
import numpy as np

XMAX = int(float(sys.argv[1])) if __name__ == "__main__" else 0
XT2 = int(float(sys.argv[2])) if len(sys.argv) > 2 else 10 ** 7
ETAS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25]
SEG = 10_000_000
rng = np.random.default_rng(7)


def primes_upto(m):
    s = np.ones(m + 1, bool); s[:2] = False
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def first_mult(a, p):
    return ((a + p - 1) // p) * p - a


def factor_info(a, b, plist):
    """For n in [a,b): Omega(n), squarefree flag, smallest prime factor (capped)."""
    n = b - a
    rem = np.arange(a, b, dtype=np.int64)
    om = np.zeros(n, np.int16)
    sqf = np.ones(n, bool)
    spf = np.full(n, np.iinfo(np.int64).max, np.int64)
    for p in plist:
        p = int(p)
        s = first_mult(a, p)
        if s >= n:
            continue
        v = spf[s::p]; np.minimum(v, p, out=v)
        pk = p; k = 0
        while pk < b:
            s = first_mult(a, pk)
            if s >= n:
                break
            om[s::pk] += 1
            rem[s::pk] //= p
            if k >= 1:
                sqf[s::pk] = False
            k += 1
            if pk > b // p:
                break
            pk *= p
    big = rem > 1
    om += big.astype(np.int16)
    np.minimum(spf, np.where(big, rem, spf), out=spf)
    return om, sqf, spf


def p1():
    t0 = time.time()
    zs = [1 if e == 0 else XMAX ** e for e in ETAS]
    plist = primes_upto(int((XMAX + 4) ** 0.5) + 1)
    acc = {e: dict(Ap=0, Ac=0, Bp=0, Bc=0) for e in ETAS}
    for a in range(1, XMAX + 1, SEG):
        b = min(a + SEG, XMAX + 1)
        om, sqf, spf = factor_info(a, b + 2, plist)
        n = b - a
        isprime = (om[:n] == 1) & (spf[:n] == np.arange(a, b))
        isprime &= np.arange(a, b) > 1
        om2, sqf2, spf2 = om[2:2 + n], sqf[2:2 + n], spf[2:2 + n]
        mu2 = np.where(sqf2, 1 - 2 * (om2 % 2), 0).astype(np.int64)
        for e, z in zip(ETAS, zs):
            sel = (mu2 != 0) & (spf2 >= z)
            selp = sel & isprime
            acc[e]['Ap'] += int(mu2[selp].sum()); acc[e]['Ac'] += int(selp.sum())
            acc[e]['Bp'] += int(mu2[sel].sum()); acc[e]['Bc'] += int(sel.sum())
        print(f"P1 segment to {b}: {time.time()-t0:.0f}s", flush=True)
    rows = []
    for e, z in zip(ETAS, zs):
        A = acc[e]['Ap'] / acc[e]['Ac']; B = acc[e]['Bp'] / acc[e]['Bc']
        rows.append(dict(eta=e, z=z, n_primes=acc[e]['Ac'], A=A, B=B, A_minus_B=A - B,
                         noise_A=1 / math.sqrt(acc[e]['Ac'])))
    return rows


def p2():
    x = XT2
    plist = primes_upto(int((x + 4) ** 0.5) + 1)
    om, sqf, spf = factor_info(1, x + 3, plist)
    vals = np.arange(1, x + 3)
    isprime = (om == 1) & (spf == vals) & (vals > 1)
    mu = np.where(sqf, 1 - 2 * (om % 2), 0).astype(np.int64)
    def at(k):  # arrays indexed by value k (k>=1)
        return k - 1
    rand = np.where(mu != 0, rng.choice([-1, 1], size=mu.size), 0)
    rows = []
    for N in [10, 30, 100, 300, 1000, 3000]:
        M = x // (2 * N)
        ms = np.arange(1, M + 1, dtype=np.int64)
        res = {}
        for name, f in [('twin_1P', isprime.astype(np.int64)), ('mu_shift', mu)]:
            S_mu = np.zeros(M, np.int64); S_rd = np.zeros(M, np.int64); T = np.zeros(M, np.int64)
            for nn in range(N + 1, 2 * N + 1):
                if mu[at(nn)] == 0:
                    continue
                k = ms * nn + 2
                ok = k <= x + 2
                fv = np.zeros(M, np.int64); fv[ok] = f[at(k[ok])]
                S_mu += mu[at(nn)] * fv
                S_rd += rand[at(nn)] * fv
                T += np.abs(fv)
            tot = T.sum()
            res[name] = dict(ratio_mu=float(np.abs(S_mu).sum() / tot),
                             ratio_random=float(np.abs(S_rd).sum() / tot),
                             mean_inner_terms=float(tot / M))
        rows.append(dict(N=N, M=int(M), **res))
        print(f"P2 N={N}: twin mu/rand = {res['twin_1P']['ratio_mu']:.4f}/{res['twin_1P']['ratio_random']:.4f}, "
              f"mu_shift mu/rand = {res['mu_shift']['ratio_mu']:.4f}/{res['mu_shift']['ratio_random']:.4f}", flush=True)
    return rows


if __name__ == '__main__':
    out = dict(x=XMAX, x_type2=XT2)
    out['P1'] = p1()
    for r in out['P1']:
        print(f"eta={r['eta']:.2f} z={r['z']:.1f}: A={r['A']:+.5f} B={r['B']:+.5f} A-B={r['A_minus_B']:+.5f} "
              f"(noise {r['noise_A']:.5f}, primes {r['n_primes']})")
    out['P2'] = p2()
    fn = f"bilinear_probe_{XMAX:.0e}.json".replace('+', '')
    json.dump(out, open(fn, 'w'), indent=1)
    print('wrote', fn)
