"""Two checks for route/ATTACK_LRC2.md.

(1) Moebius analogue of the Buchstab function: m(u) with (u m(u))' = -m(u-1), u m(u) = -1 on (1,2].
    sum_{n<=x, P^-(n) > x^{1/u}} mu(n) ~ u m(u) x/log x ... in the normalisation
    sum = (x/log x) * M(alpha), M(alpha) = u m(u), alpha = 1/u.
    Rough count uses Buchstab: (u w(u))' = w(u-1), u w(u) = 1 on (1,2].
    HL-model prediction for the rough two-point correlation:
        C_R(alpha) = sum mu1_R(n) mu1_R(n+2) / sum 1_R(n)1_R(n+2)  ->  (M(alpha)/W(alpha))^2,
    W(alpha) = u w(u).  m has no zeros, so the neutral term is a nonzero constant that is negligible for small alpha.
(2) Mertens barrier: for S_y = {n : no prime factor in (y, x^alpha)}, the share of
    sum 1_S(n)1_S(n+2)/n carried by pairs with both n, n+2 free of primes <= y
    (i.e. x^alpha-rough), against prod_{2<p<=y}(1-2/p)/prod-type prediction.
"""
import json, math, sys
import numpy as np

# ---- (1) delay differential equations on a fine grid ----
du = 1e-4
U = np.arange(1.0, 12.0 + du, du)
uw = np.zeros_like(U); um = np.zeros_like(U)
w = np.zeros_like(U); m = np.zeros_like(U)
lag = int(round(1.0 / du))
for i, u in enumerate(U):
    if u <= 2.0:
        uw[i] = 1.0; um[i] = -1.0
    else:
        uw[i] = uw[i - 1] + du * w[i - lag]          # (u w)' = w(u-1)
        um[i] = um[i - 1] - du * m[i - lag]          # (u m)' = -m(u-1)
    w[i] = uw[i] / u; m[i] = um[i] / u
# u m(u) has no zeros: it increases from -1 to 0^- and decays super-exponentially.
zeros = [float(U[i]) for i in range(lag, len(U) - 1) if U[i] > 2 and um[i] * um[i + 1] < 0]
def at(arr, u): return float(arr[int(round((u - 1.0) / du))])
res = {"zeros_of_m_u (none expected)": zeros, "table": []}
for alpha in (0.45, 0.4, 0.35, 0.3, 0.25, 0.2):
    u = 1 / alpha
    res["table"].append({"alpha": alpha, "M=u m(u)": at(um, u), "W=u w(u)": at(uw, u),
                         "pred_C_R=(M/W)^2": (at(um, u) / at(uw, u)) ** 2})
print(json.dumps(res, indent=1))

# ---- numerical rough Chowla at those alpha ----
X = int(float(sys.argv[1])); top = X + 2
spf = np.zeros(top + 1, dtype=np.int32)
for p in range(2, math.isqrt(top) + 1):
    if spf[p] == 0:
        blk = spf[p * p::p]; blk[blk == 0] = p
isp = spf == 0; isp[:2] = False; spf[isp] = np.nonzero(isp)[0]
n = np.arange(top + 1, dtype=np.int64)
mm = n.copy(); Om = np.zeros(top + 1, np.int8); sqf = np.ones(top + 1, bool); prev = np.zeros(top + 1, np.int64)
for _ in range(40):
    act = mm > 1
    if not act.any(): break
    p = spf[np.where(act, mm, 0)].astype(np.int64)
    sqf &= ~(act & (p == prev)); prev = np.where(act, p, prev)
    mm = np.where(act, mm // np.maximum(p, 1), mm); Om += act
mu = np.where(sqf, np.where(Om % 2 == 0, 1, -1), 0).astype(float)
for row in res["table"]:
    alpha = row["alpha"]; z = X ** alpha
    R = (spf > z).astype(float)
    a, b = slice(3, X + 1), slice(5, X + 3)
    pair = R[a] * R[b]
    row["num_C_R"] = float((mu[a] * mu[b] * pair).sum() / pair.sum())
    row["num_mean_mu_rough/(x/log x)"] = float((mu[2:X + 1] * R[2:X + 1]).sum() / (X / math.log(X)))
    print(json.dumps(row), flush=True)

# ---- (2) Mertens barrier ----
alpha = 0.3; zA = X ** alpha
bar = []
del mm, Om, sqf, prev, mu
primes_small = [q for q in range(2, 64) if all(q % r for r in range(2, int(q ** 0.5) + 1))]
rem = n[2:X + 3].copy()          # index i <-> n = i + 2; primes <= y stripped cumulatively
Rr = (spf[2:X + 3] > zA)
wts = 1.0 / n[3:X + 1]
Ra, Rb = Rr[1:X - 1], Rr[3:X + 1]
rr = float(((Ra & Rb) * wts).sum())
pred = 1.0
for y in (1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61):
    for p in [q for q in primes_small if q <= y]:
        for _ in range(64):
            d = rem % p == 0
            if not d.any(): break
            rem[d] //= p
        del d
    if y >= 3 and y in primes_small:
        pred *= (1 - 2 / y)
    S = (rem == 1) | (spf[np.minimum(rem, top)] > zA)
    mass = float(((S[1:X - 1] & S[3:X + 1]) * wts).sum())
    del S
    bar.append({"y": y, "rough_share": rr / mass, "prod_{2<p<=y}(1-2/p)": pred,
                "ratio": rr / mass / pred})
    print(json.dumps(bar[-1]), flush=True)
res["mertens_barrier"] = bar
json.dump(res, open("rough_parity_model.json", "w"), indent=1)
