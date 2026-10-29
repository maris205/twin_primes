"""Channel 2: twin parity in F_q[T] for small prime q.

All monic f of degree n are encoded by k = sum_{i<n} c_i q^i.  A sieve over monic irreducibles
P of degree <= n/2 and their powers gives Omega(f), squarefreeness and the least degree of an
irreducible factor.  For each constant shift a in F_q^* we measure:

  twins     #{f : f, f+a irreducible} against the Hardy-Littlewood prediction S_q pi(n)^2 / q^n
  chowla    mean of lambda(f) lambda(f+a), and of mu(f) mu(f+a)
  rough     on pairs with both f, f+a 'rough' (every factor of degree >= r0): mean m of lambda,
            correlation c, two-point deviation D = c - m1 m2       (the parity parameter's carrier)
  lines     Sawin-Shusterman lines: classes of f with the same coefficients off the exponents
            divisible by p (so the same derivative f').  f+a stays in the class of f.  We record
            the normalised line sums S/sqrt(L) of mu(f)mu(f+a) (L = class size).  Independent
            signs give an RMS close to sqrt(density of mu(f)mu(f+a) != 0).

usage: python fq_parity.py q nmax
"""
import sys, json, math, time
import numpy as np

q = int(sys.argv[1]); NMAX = int(sys.argv[2])
p = q                                   # prime fields only
t0 = time.time()


def digits(M, length):
    """Coefficient matrix (M x length) of the indices 0..M-1 in base q."""
    k = np.arange(M, dtype=np.int64)
    D = np.empty((M, length), np.int64)
    for i in range(length):
        D[:, i] = k % q; k //= q
    return D


def polymul(a, b):
    out = np.zeros(len(a) + len(b) - 1, np.int64)
    for i, x in enumerate(a):
        out[i:i + len(b)] += x * b
    return out % q


def sieve(n, irr):
    """Omega, squarefree flag, least factor degree for all monic f of degree n."""
    N = q ** n
    om = np.zeros(N, np.int8); sdeg = np.zeros(N, np.int16)
    sqf = np.ones(N, bool); mind = np.full(N, n, np.int8)
    pw = q ** np.arange(n, dtype=np.int64)
    for d in range(1, n // 2 + 1):
        for P in irr.get(d, []):
            Pk = np.array(P, np.int64); k = 1
            while k * d <= n:
                e = k * d
                m = n - e
                G = np.concatenate([digits(q ** m, m), np.ones((q ** m, 1), np.int64)], axis=1)
                prod = np.zeros((q ** m, n + 1), np.int64)
                for j, c in enumerate(Pk):
                    if c:
                        prod[:, j:j + m + 1] += c * G
                prod %= q
                idx = prod[:, :n] @ pw
                om[idx] += 1; sdeg[idx] += d
                if k == 1:
                    np.minimum.at(mind, idx, d) if False else None
                    mind[idx] = np.minimum(mind[idx], d)
                else:
                    sqf[idx] = False
                Pk = polymul(Pk, np.array(P, np.int64)); k += 1
    om = om + (sdeg < n)
    return om, sqf, mind


def irreducibles(dmax):
    irr = {}
    for d in range(1, dmax + 1):
        om, _, _ = sieve(d, irr)
        ks = np.nonzero(om == 1)[0]
        D = digits(q ** d, d)[ks]
        irr[d] = [list(row) + [1] for row in D]
    return irr


def pi_q(d):
    s = 0
    for e in range(1, d + 1):
        if d % e == 0:
            mu = 1; m = e; f = 2
            while f * f <= m:
                if m % f == 0:
                    m //= f
                    if m % f == 0:
                        mu = 0; break
                    mu = -mu
                f += 1
            if mu and m > 1:
                mu = -mu
            s += mu * q ** (d // e)
    return s // d


S_q = 1.0
for d in range(1, 60):
    x = q ** (-d)
    S_q *= ((1 - 2 * x) / (1 - x) ** 2) ** pi_q(d)

irr = irreducibles(NMAX // 2)
print(f"q={q}: irreducibles up to degree {NMAX//2} ready ({time.time()-t0:.0f}s); S_q={S_q:.5f}", flush=True)
rows = []
for n in range(4, NMAX + 1):
    N = q ** n
    om, sqf, mind = sieve(n, irr)
    lam = 1 - 2 * (om.astype(np.int64) % 2)
    mu = lam * sqf
    isirr = om == 1
    D0 = (np.arange(N, dtype=np.int64) % q)
    # class key: zero out the coefficients at exponents divisible by p
    kk = np.arange(N, dtype=np.int64)
    key = kk.copy()
    for i in range(0, n, p):
        key -= ((kk // q ** i) % q) * q ** i
    del kk
    _, cls = np.unique(key, return_inverse=True)
    ncls = cls.max() + 1
    L = N // ncls
    row = dict(q=q, n=n, N=N, pi=int(isirr.sum()), pi_exact=pi_q(n), S_q=S_q, line_len=int(L), shifts=[])
    for a in range(1, q):
        part = np.arange(N, dtype=np.int64) - D0 + (D0 + a) % q
        tw = int((isirr & isirr[part]).sum())
        hl = S_q * row['pi'] ** 2 / N
        ch = float((lam * lam[part]).mean()); chm = float((mu * mu[part]).mean())
        rough = {}
        for name, r0 in [('n/4', math.ceil(n / 4)), ('n/3', math.ceil(n / 3))]:
            R = mind >= r0
            both = R & R[part]
            if both.sum() == 0:
                continue
            m1 = float(lam[both].mean()); m2 = float(lam[part][both].mean())
            c = float((lam * lam[part])[both].mean())
            rough[name] = dict(r0=r0, pairs=int(both.sum()), m1=m1, m2=m2, c=c, D=c - m1 * m2,
                               noise=1 / math.sqrt(both.sum()))
        prodmu = mu * mu[part]
        Sline = np.bincount(cls, weights=prodmu.astype(float), minlength=ncls)
        nz = np.bincount(cls, weights=(prodmu != 0).astype(float), minlength=ncls)
        z = Sline / np.sqrt(L)
        row['shifts'].append(dict(a=a, twins=tw, HL=hl, ratio=tw / hl, chowla_lambda=ch, chowla_mu=chm,
                                  rough=rough, line_rms=float(np.sqrt((z ** 2).mean())),
                                  line_rms_random=float(np.sqrt((nz / L).mean())),
                                  line_max=float(np.abs(z).max())))
    rows.append(row)
    s = row['shifts']
    avg = lambda f: sum(f(x) for x in s) / len(s)
    rq = avg(lambda x: x['rough'].get('n/4', {}).get('D', float('nan')))
    print(f"n={n:2d} N={N:9d}  twins/HL={avg(lambda x: x['ratio']):.4f}  chowla(lam)={avg(lambda x: x['chowla_lambda']):+.5f}"
          f"  q^(-n/2)={q**(-n/2):.5f}  rough D(n/4)={rq:+.4f}  line L={L} rms={avg(lambda x: x['line_rms']):.3f}"
          f" (random {avg(lambda x: x['line_rms_random']):.3f})  ({time.time()-t0:.0f}s)", flush=True)

json.dump(rows, open(f'fq_parity_q{q}.json', 'w'), indent=1)
print('wrote', f'fq_parity_q{q}.json')
