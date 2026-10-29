"""H8: l^p and weighted-l^2 certificates for the t-family on the twin divisibility graph.

Vertices W = (0.9X, X].  Dilators: primes p in [5, y), y = X^eps (all y-smooth, so
g_t(p) = t).  Operator (Helfgott-Radziwill type, twin shift 2p, centred):
    A_{n, n+2p} = A_{n+2p, n} = 1[p | n] - 1/p.
Signal capacity: cap_t = 2 sum_p sum_{p | n} |g_t(n) g_t(n+2p)|  (divisibility edges).

(a) Unweighted l^p, conjugate pair (p, p'):  bound_p = ||A||_{p->p} ||g||_p ||g||_{p'}.
    ||A||_{p->p} is estimated from below by Boyd's power iteration.
(b) Weighted l^2 with u = |g_t|^beta:  <g, A g> = <g/u, (U A U) g/u>, so
    bound_beta = ||U A U||_2 * sum |g|^{2-2 beta}.
Resolution = bound / cap_t.  The l^2 ceiling (Prop. T) says res_2 grows like
(log z)^{(1-|t|)^2 - t^2/2}.

With centring 'adapt' the comparison coefficient is -t^2/p instead of -1/p: |g_t| is damped
by t^2 on multiples of p, and with -1/p the test vector Phi|g| alone forces res >= t^-2 - 1
for every diagonal weighting Phi (a centring artifact, not an obstruction).

usage: python h8_lp_norms.py X eps [fast] [adapt]
  fast: skip Boyd (l^p) and use a smaller (t, beta) grid, for the scaling runs.
"""
import sys, json, math, time
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
sys.path.insert(0, '.')
from bilinear_probe import factor_info, primes_upto

X = int(float(sys.argv[1])); EPS = float(sys.argv[2])
FAST = 'fast' in sys.argv[3:]
ADAPT = 'adapt' in sys.argv[3:]
TS = [0.25, 0.5, 0.75] if FAST else [0.1, 0.25, 0.5, 0.75, 1.0]
BETAS = [0.0, 0.25, 0.5, 0.75] if FAST else [0.0, 0.25, 0.5, 0.75, 1.0]
Y = X ** EPS
a, b = X - X // 10 + 1, X + 1          # window (0.9X, X]
N = b - a
t0 = time.time()
plist = primes_upto(int((X + 4) ** 0.5) + 1)
small = [int(p) for p in plist if p < Y]
P = [p for p in small if p >= 5]
om, _, _ = factor_info(a, b, plist)
oms = np.zeros(N, np.int16)
for p in small:
    pk = p
    while pk < b:
        oms[(-a) % pk::pk] += 1
        if pk > b // p:
            break
        pk *= p
lam_r = 1.0 - 2.0 * ((om - oms) % 2)
n = np.arange(a, b, dtype=np.int64)
div = {p: (n % p == 0).astype(np.float64) for p in P}
print(f"setup {time.time()-t0:.0f}s  N={N} y={Y:.1f} |P|={len(P)} Q={sum(1/p for p in P):.3f}", flush=True)


KAPPA = 1.0


def Amul(f):
    out = np.zeros_like(f)
    for p in P:
        s = 2 * p
        c = div[p][:-s] - KAPPA / p          # coefficient on edge (n, n+2p)
        out[:-s] += c * f[s:]
        out[s:] += c * f[:-s]
    return out


def l2norm(op_diag=None):
    if op_diag is None:
        mv = Amul
    else:
        u = op_diag
        mv = lambda v: u * Amul(u * v)
    L = LinearOperator((N, N), matvec=lambda v: mv(np.asarray(v, float).ravel()), dtype=float)
    val = eigsh(L, k=1, which='LM', tol=1e-2 if FAST else 1e-3, maxiter=400, return_eigenvectors=False)
    return float(abs(val[0]))


def boyd(p, iters=40, seed=0):
    """Lower bound for ||A||_{p->p} (A symmetric) by Boyd's power iteration."""
    q = p / (p - 1)
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(N)
    x /= np.linalg.norm(x, p)
    best = 0.0
    for _ in range(iters):
        y = Amul(x)
        val = np.linalg.norm(y, p)
        best = max(best, val)
        z = Amul(np.sign(y) * np.abs(y) ** (p - 1))        # A^T psi_p(Ax)
        x = np.sign(z) * np.abs(z) ** (q - 1)               # psi_{p'}(z)
        x /= np.linalg.norm(x, p)
    return best


def cap(g):
    c = 0.0
    for p in P:
        s = 2 * p
        c += 2 * float((div[p][:-s] * np.abs(g[:-s] * g[s:])).sum())
    return c


out = dict(X=X, eps=EPS, y=Y, logz=math.log(Y), N=N, Q=sum(1 / p for p in P), lp=[], weighted=[])
A2 = l2norm()
out['A2'] = A2
print(f"||A||_2 = {A2:.4f}  ({time.time()-t0:.0f}s)", flush=True)
Ap = {2.0: A2}
for p in ([] if FAST else [1.25, 1.5, 3.0, 5.0]):
    Ap[p] = boyd(p if p < 2 else p / (p - 1))                 # ||A||_p = ||A||_{p'} for symmetric A
    print(f"||A||_{p} >= {Ap[p]:.4f}  ({time.time()-t0:.0f}s)", flush=True)

for t in TS:
    g = np.power(t, oms.astype(float)) * lam_r
    C = cap(g)
    if ADAPT:
        KAPPA = t * t
        A2 = l2norm()
    for p in sorted(Ap):
        q = p / (p - 1)
        cost = np.linalg.norm(g, p) * np.linalg.norm(g, q)
        out['lp'].append(dict(t=t, p=p, normA=Ap[p], cost=cost, cap=C, res=Ap[p] * cost / C))
    for beta in BETAS:
        u = np.abs(g) ** beta
        nm = A2 if beta == 0 else l2norm(u)
        cost = float((np.abs(g) ** (2 - 2 * beta) * (g != 0)).sum())
        out['weighted'].append(dict(t=t, beta=beta, normM=nm, cost=cost, cap=C, res=nm * cost / C))
        print(f"t={t:.2f} beta={beta:.2f}  ||UAU||={nm:.4f}  cost={cost:.4g}  cap={C:.4g}  res={nm*cost/C:.4f}  ({time.time()-t0:.0f}s)", flush=True)

json.dump(out, open(f'h8_lp_{X:.0e}_eps{EPS}{"_fast" if FAST else ""}{"_adapt" if ADAPT else ""}.json'.replace('+', ''), 'w'), indent=1)
print("\nl^p (conjugate pair) resolutions:")
for r in out['lp']:
    print(f"t={r['t']:.2f} p={r['p']:.2f}  ||A||_p>={r['normA']:.3f}  res>={r['res']:.4f}")
