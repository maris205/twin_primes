"""Stage 15: heuristic model for the #681 exceptions n = p - 1.

For n = p - 1 of size x, a witness is an odd k with k^4 < n + k such that
n + k has no prime factor <= k^2 and is composite.  Model:
  * the residues of n mod each prime q are independent and uniform among
    the q - 1 classes != -1 (because n + 1 = p is prime);
  * given that n + k has no prime factor <= y = k^2, it is prime with
    probability pi_k = 1 / (u * omega(u)), u = log x / log y, where omega is
    Buchstab's function (the y-rough integers near x have density
    omega(u)/log y and the primes 1/log x), independently over k.
Then P(no witness) = E[ prod_{k uncovered} pi_k ].

(1) Monte Carlo of this expectation for x = 10^4 ... 10^12, compared with
    the observed exception fractions from stage15_681.json;
(2) the independent-position (Poisson-type) approximation
        log P ~ sum_k log(1 - P(k uncovered) (1 - pi_k)),
    computed up to x = 10^30, and the expected number of exceptions per
    decade, to estimate where the last exception should lie.
This is a heuristic, not a proof.  Writes stage15_model.json.
"""
import json
import math
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")


def primes_upto(n):
    s = np.ones(n + 1, bool)
    s[:2] = False
    for q in range(2, int(n**0.5) + 1):
        if s[q]:
            s[q * q::q] = False
    return np.nonzero(s)[0]


# Buchstab omega on a grid (u >= 1), by the delay equation (u omega(u))' = omega(u-1)
H = 1e-4
UG = np.arange(1.0, 40.0 + H, H)
OM = np.empty_like(UG)
m1 = UG <= 2.0
OM[m1] = 1.0 / UG[m1]
i2 = int(round(1.0 / H))
F = UG * OM
for i in range(np.argmax(UG > 2.0), len(UG)):
    F[i] = F[i - 1] + H * 0.5 * (OM[i - i2] + OM[i - 1 - i2])
    OM[i] = F[i] / UG[i]


def omega(u):
    return float(np.interp(u, UG, OM))


def pi_k(k, x):
    u = math.log(x) / math.log(k * k)
    return min(1.0, 1.0 / (u * omega(u)))


def mc(x, T, rng):
    K = int((x) ** 0.25)
    ks = np.arange(K + 1)
    qs = [int(q) for q in primes_upto(K * K)]
    cov = np.zeros((T, K + 1), bool)
    cov[:, :2] = True                      # k = 0, 1 are not candidates
    cov[:, 0::2] = True                    # even k: n + k even (q = 2)
    for q in qs[1:]:
        r = rng.integers(0, q - 1, T)      # n mod q, never -1
        k0 = (-r) % q                      # n + k = 0 (mod q)  <=>  k = k0 (mod q)
        kmin = math.isqrt(q - 1) + 1       # need q <= k^2
        j = 0
        while True:
            kk = k0 + j * q
            ok = kk <= K
            if not ok.any():
                break
            ok &= kk >= kmin
            cov[np.nonzero(ok)[0], kk[ok]] = True
            j += 1
    logpi = np.array([0.0, 0.0] + [math.log(pi_k(k, x)) for k in range(2, K + 1)])
    lp = (~cov) @ logpi
    return float(np.exp(lp).mean()), K


Y0 = 10**7
QS = primes_upto(Y0)[1:]                   # odd primes up to Y0
CUM = np.concatenate(([0.0], np.cumsum(np.log1p(-1.0 / (QS - 1.0)))))
KCAP = 10**7
GCORR = np.ones(KCAP + 1)                  # prod_{q | m, q odd} (1 - 1/(q-1))^(-1)
for q in QS[QS <= KCAP]:
    GCORR[q::q] /= 1.0 - 1.0 / (q - 1.0)


def log_prod_odd(y):
    """sum_{3 <= q <= y} log(1 - 1/(q-1)); Mertens beyond Y0."""
    y = np.asarray(y, float)
    n = np.searchsorted(QS, np.minimum(y, Y0), side="right")
    out = CUM[n]
    big = y > Y0
    out[big] += np.log(math.log(Y0) / np.log(y[big]))
    return out


def poisson_logP(x):
    """log P(no witness) assuming independent positions."""
    K = min(int(x ** 0.25), KCAP)
    k = np.arange(3, K + 1, 2, dtype=float)
    # P(odd k uncovered) = prod_{3 <= q <= k^2, q not | k-1} (1 - 1/(q-1))
    pu = np.exp(log_prod_odd(k * k)) * GCORR[(k - 1).astype(np.int64)]
    u = math.log(x) / np.log(k * k)
    pik = np.minimum(1.0, 1.0 / (u * np.interp(u, UG, OM)))
    return float(np.log1p(-pu * (1.0 - pik)).sum())


QUICK = len(sys.argv) > 1 and sys.argv[1] == "quick"
rng = np.random.default_rng(681)
obs = {}
try:
    with open(__file__.replace("stage15_model.py", "stage15_681.json"), encoding="utf-8") as fh:
        for row in json.load(fh)["per_decade"]:
            obs[row["decade"]] = row["fraction_p"]
except FileNotFoundError:
    pass

rows_mc = []
for d in (range(4, 6) if QUICK else range(4, 13)):
    for frac in (0.0, 0.5):
        x = 10 ** (d + frac)
        T = 20000 if d <= 9 else 4000
        p, K = mc(x, T, rng)
        rows_mc.append({"x": "1e%.1f" % (d + frac), "K=x^(1/4)": K, "model_P_exception": p,
                        "poisson_P": math.exp(poisson_logP(x)),
                        "observed_fraction_in_decade": obs.get("[1e%d,1e%d)" % (d, d + 1))})
        print(rows_mc[-1], flush=True)

rows_ext = []
cum_expected = 0.0
for d in (range(9, 11) if QUICK else range(9, 28)):
    # expected exceptions in [10^d, 10^(d+1)): integrate pi(x) density * P(x)
    e = 0.0
    for j in range(8):
        a, b = 10 ** (d + j / 8), 10 ** (d + (j + 1) / 8)
        xm = math.sqrt(a * b)
        e += (b - a) / math.log(xm) * math.exp(poisson_logP(xm))
    rows_ext.append({"decade": "[1e%d,1e%d)" % (d, d + 1), "expected_exceptions_poisson": e})
    print(rows_ext[-1], flush=True)

if not QUICK:
  with open(__file__.replace(".py", ".json"), "w", encoding="utf-8") as fh:
    json.dump({"monte_carlo": rows_mc, "poisson_extrapolation": rows_ext}, fh, indent=1)
