"""L4 experiment (route/L4_TEST.md): spectral bound for the divisibility operator restricted to
rough numbers, versus the dense Helfgott-Radziwill setting.

Rough setting (shift h = 2, both endpoints rough):
  X = {n in (x/2, x] : no prime factor < z}, z = x^eta;   P = primes in (z, P2]
  (A f)(n) = sum_{p in P} [1_{p|n} - 1/p] (f(n+2p) + f(n-2p)),  restricted to n, n +- 2p in X
  (for n, n+2p in X:  p | n  <=>  p | n+2p, so A is symmetric).
  A = S - T:  S = divisibility edges (weight 1, sparse), T f = 1_X (K * 1_X f), K(+-2p) = 1/p (FFT).
Dense setting (Helfgott-Radziwill, shift h = 1, all integers):  X' = (x'/2, x'], same P,
  (A' f)(n) = sum_p [1_{p|n} - 1/p] (f(n+p) + f(n-p)).
Reported: |X|, rho, L = sum 1/p, divisibility edges, average S-degree, component sizes,
  top / bottom eigenvalues of A (Lanczos), and ratios against sqrt(L), L and the per-vertex signal scale.

Usage: python l4_experiment.py X_ROUGH X_DENSE
"""
import json, math, sys, time
import numpy as np
from scipy import fft as sfft
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import LinearOperator, eigsh

XR = int(float(sys.argv[1])); XD = int(float(sys.argv[2]))


def primes_upto(m):
    s = np.ones(m + 1, dtype=bool); s[:2] = False
    for p in range(2, math.isqrt(m) + 1):
        if s[p]: s[p * p::p] = False
    return np.nonzero(s)[0]


PR = primes_upto(200000)


def build(x, z, P2, h, rough):
    lo = x // 2 + 1; N = x - lo + 1
    if rough:
        mask = np.ones(N, dtype=bool)
        for p in PR[PR < z]:
            mask[(-lo) % p::p] = False
    else:
        mask = np.ones(N, dtype=bool)
    P = PR[(PR > z) & (PR <= P2)] if rough else PR[(PR >= 2) & (PR <= P2)]
    idx = -np.ones(N, dtype=np.int64)
    Xpos = np.nonzero(mask)[0]
    idx[Xpos] = np.arange(len(Xpos))
    rows, cols = [], []
    for p in P:
        p = int(p); s = p * h
        first = (-lo) % p
        n = np.arange(first, N - s, p)              # p | n, n + s inside window
        ok = mask[n] & mask[n + s]
        rows.append(idx[n[ok]]); cols.append(idx[n[ok] + s])
    r = np.concatenate(rows) if rows else np.zeros(0, np.int64)
    c = np.concatenate(cols) if cols else np.zeros(0, np.int64)
    M = len(Xpos)
    S = coo_matrix((np.ones(2 * len(r)), (np.concatenate([r, c]), np.concatenate([c, r]))), shape=(M, M)).tocsr()
    # convolution kernel for T on the full window
    L = float(np.sum(1.0 / P))
    span = int(h * P.max()) if len(P) else 0
    nfft = sfft.next_fast_len(N + span + 1)
    ker = np.zeros(nfft, dtype=np.float32)
    for p in P:
        ker[int(h * p)] += 1.0 / p
        ker[nfft - int(h * p)] += 1.0 / p
    Fk = sfft.rfft(ker)
    full = np.zeros(nfft, dtype=np.float32)

    def T(v):
        full[:] = 0.0
        full[Xpos] = v
        conv = sfft.irfft(sfft.rfft(full) * Fk, n=nfft, workers=-1)
        return conv[Xpos].astype(np.float64)

    def A(v):
        return S @ v - T(v)
    # Schur row-sum bound for T restricted to X
    Tones = T(np.ones(M))
    return dict(M=M, N=N, P=P, L=L, S=S, A=A, T=T, Tmax=float(Tones.max()), Tmean=float(Tones.mean()), E=len(r))


def analyse(tag, x, z, P2, h, rough):
    t0 = time.time()
    G = build(x, z, P2, h, rough)
    M, S = G["M"], G["S"]
    deg = np.asarray(S.sum(axis=1)).ravel()
    ncomp, lab = connected_components(S, directed=False)
    sizes = np.bincount(lab)
    vert_in_edges = int((deg > 0).sum())
    op = LinearOperator((M, M), matvec=G["A"], dtype=np.float64)
    top = eigsh(op, k=2, which="LA", tol=1e-3, maxiter=300, return_eigenvectors=False)
    bot = eigsh(op, k=2, which="SA", tol=1e-3, maxiter=300, return_eigenvectors=False)
    lam = float(max(abs(top.max()), abs(bot.min())))
    Sl = float(eigsh(S.astype(np.float64), k=1, which="LA", tol=1e-4, return_eigenvectors=False)[0])
    avgdeg = float(deg.mean())
    row = {"setting": tag, "x": x, "z": z, "P2": P2, "h": h, "|X|": M, "rho=|X|/N": M / G["N"],
           "|P|": int(len(G["P"])), "L=sum 1/p": G["L"], "div_edges": G["E"],
           "avg S-degree": avgdeg, "max S-degree": int(deg.max()),
           "frac vertices with an edge": vert_in_edges / M,
           "largest component": int(sizes.max()),
           "frac edge-vertices in comps of size<=2": float(((sizes[lab] <= 2) & (deg > 0)).sum() / max(vert_in_edges, 1)),
           "T row-sum mean/max": [G["Tmean"], G["Tmax"]],
           "lam_max(S)": Sl, "lam_max|A| (Lanczos)": lam,
           "lam/sqrt(L)": lam / math.sqrt(G["L"]), "lam/avgdeg": lam / max(avgdeg, 1e-12),
           "seconds": round(time.time() - t0, 1)}
    print(json.dumps(row), flush=True)
    return row


out = {"rough": [], "dense": []}
for eta in (0.15, 0.2):
    z = XR ** eta
    for P2 in (100, 1000, 10000, 100000):
        out["rough"].append(analyse("rough", XR, z, P2, 2, True))
for P2 in (100, 1000, 10000, 100000):
    out["dense"].append(analyse("dense", XD, 1, P2, 1, False))
json.dump(out, open("l4_experiment.json", "w"), indent=1)
