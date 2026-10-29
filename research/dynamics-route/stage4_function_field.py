"""Dynamics route, stage 4: the Pellet mechanism over F_p[T] and its absence over Z.

(1) Over F_p[T] (p odd, small): for every monic squarefree f of degree n,
        mu(f) = (-1)^n chi(disc f)                        (Pellet / Stickelberger)
    and, for c in F_p (a constant, so (f+c)' = f'), disc(f+c) = +- Res(f+c, f') with lead(f')
    fixed, hence  mu(f) mu(f+c) = chi(Res(f, f') Res(f+c, f')):  the twin-type correlation along the
    subspace f + F_p is a quadratic character of resultants against the SAME modulus f'.  We verify the
    first identity exhaustively and the second on all pairs (f, f+1).
(2) Over Z there is no such structure: on windows of H consecutive odd integers near X we compare the best
    agreement of lambda with a real character (Kronecker symbol (d/.) for fundamental discriminants
    |d| <= Q, up to a global sign) against the same statistic for random sign sequences.

usage: python stage4_function_field.py p nmax X H Q windows
"""
import sys, json, itertools, math
import numpy as np

p = int(sys.argv[1]); NMAX = int(sys.argv[2]); X = int(float(sys.argv[3])); H = int(sys.argv[4])
Q = int(sys.argv[5]); WIN = int(sys.argv[6])
chi = lambda a: 0 if a % p == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)

# ---- polynomial arithmetic over F_p, coefficient lists low -> high
def trim(a):
    while a and a[-1] % p == 0: a = a[:-1]
    return a
def pmod(a, b):
    a = [x % p for x in a]; b = trim(b); inv = pow(b[-1], p - 2, p)
    while len(trim(a)) >= len(b):
        a = trim(a); s = len(a) - len(b); c = a[-1] * inv % p
        for i in range(len(b)): a[s + i] = (a[s + i] - c * b[i]) % p
    return trim(a)
def deriv(a): return trim([(i * a[i]) % p for i in range(1, len(a))])
def resultant(a, b):
    a, b = trim(a), trim(b); res = 1
    while True:
        da, db = len(a) - 1, len(b) - 1
        if db < 0: return 0
        if db == 0: return res * pow(b[0], da, p) % p
        r = pmod(a, b); dr = len(r) - 1
        if dr < 0: return 0
        res = res * pow(-1, da * db, p) * pow(b[-1], da - dr, p) % p
        a, b = b, r
def mobius(f):
    """mu of monic f over F_p by trial division with monic polynomials of degree <= deg/2."""
    f = trim(f); n = len(f) - 1; k = 0; g = f
    for d in range(1, n // 2 + 1):
        for tail in itertools.product(range(p), repeat=d):
            q = list(tail) + [1]
            while len(g) - 1 >= d and not pmod(g, q):
                # divide g by q
                quo = [0] * (len(g) - len(q) + 1); r = g[:]
                for s in range(len(quo) - 1, -1, -1):
                    c = r[s + len(q) - 1] % p; quo[s] = c
                    for i in range(len(q)): r[s + i] = (r[s + i] - c * q[i]) % p
                g = trim(quo); k += 1
                if not pmod(g, q): return 0
    if len(g) > 1: k += 1
    return (-1) ** k

out = dict(p=p, nmax=NMAX, pellet={}, twin_subspace={})
for n in range(2, NMAX + 1):
    ok = tot = 0; ok2 = tot2 = 0
    for tail in itertools.product(range(p), repeat=n):
        f = list(tail) + [1]
        m = mobius(f)
        if m == 0: continue
        disc_sign = chi(resultant(f, deriv(f)) * pow(-1, n * (n - 1) // 2, p))
        ok += (m == (-1) ** n * disc_sign); tot += 1
        g = f[:]; g[0] = (g[0] + 1) % p
        m2 = mobius(g)
        if m2 == 0: continue
        fp = deriv(f)
        pred = chi(resultant(f, fp) * resultant(g, fp))
        ok2 += (m * m2 == pred); tot2 += 1
    out["pellet"][n] = dict(squarefree=tot, identity_holds=ok)
    out["twin_subspace"][n] = dict(pairs=tot2, identity_holds=ok2)
    print(n, out["pellet"][n], out["twin_subspace"][n], flush=True)

# ---- (2) lambda versus real characters on short windows of odd integers
def kron(d, m):
    # Kronecker symbol (d/m) for odd positive m via Jacobi
    a, n, t = d % m, m, 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0
def is_fund(d):
    if d % 4 == 1: return all(d % (q * q) for q in range(3, int(abs(d) ** 0.5) + 1, 2))
    if d % 4 == 0:
        e = d // 4
        return e % 4 in (2, 3) and all(e % (q * q) for q in range(3, int(abs(e) ** 0.5) + 1, 2))
    return False
discs = [d for d in range(-Q, Q + 1) if d not in (0, 1) and is_fund(d)]
L = X + 2 * H * WIN + 10
sieve_om = np.zeros(L + 1, np.int64); rem = np.arange(L + 1)
for q in range(2, int(L ** 0.5) + 1):
    if all(q % r for r in range(2, int(q ** 0.5) + 1)):
        qq = q
        while qq <= L:
            idx = np.arange(qq, L + 1, qq); sieve_om[idx] += 1; rem[idx] //= q; qq *= q
sieve_om[rem > 1] += 1
lam = 1 - 2 * (sieve_om % 2)
rng = np.random.default_rng(4)
best_l, best_r = [], []
for w in range(WIN):
    ns = [X + 2 * H * w + 2 * i + 1 for i in range(H)]
    sl = np.array([lam[x] for x in ns])
    sr = rng.choice([-1, 1], size=H)
    bl = br = 0
    for d in discs:
        cv = np.array([kron(d, x) for x in ns])
        nz = cv != 0
        if nz.sum() < H // 2: continue
        bl = max(bl, abs(int(np.sum(sl[nz] * cv[nz]))) / nz.sum())
        br = max(br, abs(int(np.sum(sr[nz] * cv[nz]))) / nz.sum())
    best_l.append(bl); best_r.append(br)
out["characters"] = dict(X=X, H=H, Q=Q, windows=WIN, discriminants=len(discs),
                         lambda_best_mean=float(np.mean(best_l)), lambda_best_max=float(np.max(best_l)),
                         random_best_mean=float(np.mean(best_r)), random_best_max=float(np.max(best_r)))
print(out["characters"])
json.dump(out, open(f"stage4_ff_p{p}.json", "w"), indent=1)
