"""L1 falsification test (route/L1_TEST.md).

Unknowns: relative deviations u(s, r') = m(s, r') / (model I_s I_r') - 1 of the rough-pair mass
with Omega(n) = s, Omega(n+2) = r'.
One-sided Bombieri (GEH), sieve weight on n, sequence a = f_{r'}(n+2):
     (A_r')  u(., r') in span{(-1)^s}      for every r'
Same with roles exchanged:
     (B_s)   u(s, .) in span{(-1)^{r'}}    for every s
Part 1: dimension of the solution space of (A) and (B) on {1..R}^2.
Part 2: synthetic worlds built on a product model:
     W1 one-sided flip       u = e1 (-1)^s
     W2 two independent flips u = (1+e1(-1)^s)(1+e2(-1)^{r'}) - 1
     W3 coupled flip          u = c (-1)^{s+r'}
     W4 "second parameter"    u = c (-1)^{s+r'} + d [s>=2][r'>=2] (-1)^{s+r'}
   For each: residual of (A) and (B) (least-squares distance of each column/row from the allowed span).
Part 3: real data (counts from amplification.json, x = 1e7): fit
     u = a + b(-1)^s + c(-1)^{r'} + d(-1)^{s+r'}, weighted by expected counts, with standard errors,
   and the (A)/(B) residuals relative to Poisson noise.
"""
import json, math
import numpy as np

R = 6
S = np.arange(1, R + 1)
sgn = (-1.0) ** S

# ---- Part 1: solution space of (A) and (B) ----
idx = {(s, r): i for i, (s, r) in enumerate([(s, r) for s in S for r in S])}
rows = []
P_s = np.eye(R) - np.outer(sgn, sgn) / (sgn @ sgn)          # projector onto complement of span{(-1)^s}
for r in S:                                                 # (A_r): P_s u(., r) = 0
    for k in range(R):
        row = np.zeros(R * R)
        for j, s in enumerate(S):
            row[idx[(s, r)]] = P_s[k, j]
        rows.append(row)
for s in S:                                                 # (B_s): P_r u(s, .) = 0
    for k in range(R):
        row = np.zeros(R * R)
        for j, r in enumerate(S):
            row[idx[(s, r)]] = P_s[k, j]
        rows.append(row)
Mc = np.array(rows)
sv = np.linalg.svd(Mc, compute_uv=False)
null_dim = int(np.sum(sv < 1e-10)) + (R * R - len(sv) if len(sv) < R * R else 0)
_, _, Vt = np.linalg.svd(Mc)
v = Vt[-1].reshape(R, R)
v = v / v[0, 0]
out = {"part1": {"grid": f"{R}x{R}", "nullspace_dim": null_dim,
                 "nullspace_vector_(normalised)": np.round(v, 6).tolist(),
                 "is_(-1)^(s+r')": bool(np.allclose(v, np.outer(sgn, sgn) / (sgn[0] * sgn[0])))}}
print(json.dumps(out["part1"]), flush=True)


def residuals(u, w=None):
    """Weighted LS distance of each column (A) / row (B) of u from span{(-1)^.}."""
    if w is None:
        w = np.ones_like(u)
    resA, resB = 0.0, 0.0
    for j in range(u.shape[1]):
        ww, uu, ss = w[:, j], u[:, j], sgn[:u.shape[0]]
        if ww.sum() == 0: continue
        coef = (ww * uu * ss).sum() / (ww * ss * ss).sum()
        resA += (ww * (uu - coef * ss) ** 2).sum()
    for i in range(u.shape[0]):
        ww, uu, ss = w[i, :], u[i, :], sgn[:u.shape[1]]
        if ww.sum() == 0: continue
        coef = (ww * uu * ss).sum() / (ww * ss * ss).sum()
        resB += (ww * (uu - coef * ss) ** 2).sum()
    return resA, resB


# ---- Part 2: synthetic worlds ----
e1, e2, c, d = 0.3, 0.2, 0.25, 0.15
ss, rr = np.meshgrid(sgn, sgn, indexing="ij")
big_s = (S >= 2)[:, None] & (S >= 2)[None, :]
worlds = {
    "W1 one-sided flip": e1 * ss,
    "W2 independent flips": (1 + e1 * ss) * (1 + e2 * rr) - 1,
    "W3 coupled (1D)": c * ss * rr,
    "W4 coupled + second parameter on s,r'>=2": c * ss * rr + d * big_s * ss * rr,
}
out["part2"] = {}
for name, u in worlds.items():
    rA, rB = residuals(u)
    out["part2"][name] = {"res_A": rA, "res_B": rB, "GEH-consistent": bool(rA < 1e-12 and rB < 1e-12)}
    print(name, json.dumps(out["part2"][name]), flush=True)

# ---- Part 3: real data ----
amp = json.load(open("amplification.json"))
out["part3"] = []
for rec in amp["A"]:
    tab = rec["table_rows"]
    rmax = max(max(int(k) for k in tab), max(len(v) for v in tab.values()) - 1)
    T = np.zeros((rmax + 1, rmax + 1))
    for k, row in tab.items():
        T[int(k), :len(row)] = row
    T = T[1:, 1:]                                   # s, r' >= 1
    tot = T.sum(); E = np.outer(T.sum(1), T.sum(0)) / tot
    keep = E > 50
    Rr = T.shape[0]
    sg = (-1.0) ** np.arange(1, Rr + 1)
    Ss, Rs = np.meshgrid(sg, sg, indexing="ij")
    u = np.where(keep, T / np.where(E > 0, E, 1) - 1, 0.0)
    wgt = np.where(keep, E, 0.0)                    # Poisson: var(u) ~ 1/E
    X = np.stack([np.ones_like(u), Ss, Rs, Ss * Rs], -1)[keep]
    y = u[keep]; W = wgt[keep]
    XtW = X.T * W
    beta = np.linalg.solve(XtW @ X, XtW @ y)
    cov = np.linalg.inv(XtW @ X)
    se = np.sqrt(np.diag(cov))
    # residual of (A),(B) beyond Poisson: chi^2-like with weights E (var u = 1/E)
    rA, rB = 0.0, 0.0
    for j in range(Rr):
        m = keep[:, j]
        if m.sum() < 2: continue
        ww, uu, s_ = wgt[m, j], u[m, j], sg[m]
        coef = (ww * uu * s_).sum() / (ww * s_ * s_).sum(); rA += (ww * (uu - coef * s_) ** 2).sum()
    for i in range(Rr):
        m = keep[i, :]
        if m.sum() < 2: continue
        ww, uu, s_ = wgt[i, m], u[i, m], sg[m]
        coef = (ww * uu * s_).sum() / (ww * s_ * s_).sum(); rB += (ww * (uu - coef * s_) ** 2).sum()
    dofA = int(sum(max(keep[:, j].sum() - 1, 0) for j in range(Rr)))
    dofB = int(sum(max(keep[i, :].sum() - 1, 0) for i in range(Rr)))
    row = {"eta": rec["eta"], "cells": int(keep.sum()),
           "fit": {k: [float(b), float(e)] for k, b, e in zip(["a const", "b (-1)^s", "c (-1)^r'", "d (-1)^(s+r')"], beta, se)},
           "chi2_A/dof": [rA, dofA], "chi2_B/dof": [rB, dofB]}
    out["part3"].append(row)
    print(json.dumps(row), flush=True)
json.dump(out, open("l1_test.json", "w"), indent=1)


# ---- Part 4: is the small-eta violation parity or neutral? ----
# Add parity-neutral regressors (size-size correlation) and recompute; neutral effects should be
# absorbed by them while the parity coefficient d stays at 0.
out["part4"] = []
for rec in amp["A"]:
    tab = rec["table_rows"]
    rmax = max(max(int(k) for k in tab), max(len(v) for v in tab.values()) - 1)
    T = np.zeros((rmax + 1, rmax + 1))
    for k, row in tab.items():
        T[int(k), :len(row)] = row
    T = T[1:, 1:]
    tot = T.sum(); E = np.outer(T.sum(1), T.sum(0)) / tot
    keep = E > 50
    Rr = T.shape[0]
    sv_ = np.arange(1, Rr + 1, dtype=float)
    Sg, Rg = np.meshgrid(sv_, sv_, indexing="ij")
    ms = (T.sum(1) @ sv_) / tot
    sg = (-1.0) ** np.arange(1, Rr + 1)
    Ss, Rs = np.meshgrid(sg, sg, indexing="ij")
    u = np.where(keep, T / np.where(E > 0, E, 1) - 1, 0.0)
    wgt = np.where(keep, E, 0.0)
    cols = {"const": np.ones_like(u), "(-1)^s": Ss, "(-1)^r'": Rs, "(-1)^(s+r')": Ss * Rs,
            "(s-m)(r'-m)": (Sg - ms) * (Rg - ms), "(s-m)^2(r'-m)^2": ((Sg - ms) * (Rg - ms)) ** 2}
    X = np.stack(list(cols.values()), -1)[keep]; y = u[keep]; W = wgt[keep]
    XtW = X.T * W
    beta = np.linalg.lstsq(XtW @ X, XtW @ y, rcond=None)[0]
    cov = np.linalg.pinv(XtW @ X)
    resid = y - X @ beta
    chi2 = float((W * resid ** 2).sum()); dof = int(keep.sum() - X.shape[1])
    row = {"eta": rec["eta"], "chi2/dof (with neutral size terms)": [chi2, dof],
           "d (-1)^(s+r')": [float(beta[3]), float(np.sqrt(cov[3, 3]))],
           "size-size coef": [float(beta[4]), float(np.sqrt(cov[4, 4]))]}
    out["part4"].append(row)
    print(json.dumps(row), flush=True)
json.dump(out, open("l1_test.json", "w"), indent=1)
