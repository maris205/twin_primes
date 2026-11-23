"""Stage 11: how does J(k) = A048670(k) grow across short windows?

Reads only the hard-coded table below; writes stage11_jumps.json.

Source of the table: OEIS A048670 b-file, terms 1..71 (terms 1..57 from
R. Gerbicz's table, 58..64 from A. Bozek, 65..71 from A. Weeks, Oct 2026).
OEIS data are CC BY-SA 4.0.

Quantities (w = window length, F = number of "free" primes in Theorem F):
  ratio(k, w)  = J(k) / J(k - w)
  alpha(k, w)  = log ratio(k, w) / log(k / (k - w))     local growth exponent
  Delta(k)     = J(k) - J(k-1)                           one-step increment
  Delta(k)/p_k                                           increment per new prime
The jump set of Lemma 9.5 is B_C(w) = {k : ratio(k, w) > C}.
"""
import json
import math

J = [2, 4, 6, 10, 14, 22, 26, 34, 40, 46, 58, 66, 74, 90, 100, 106, 118, 132, 152, 174,
     190, 200, 216, 234, 258, 264, 282, 300, 312, 330, 354, 378, 388, 414, 432, 450, 476,
     492, 510, 538, 550, 574, 600, 616, 642, 660, 686, 718, 742, 762, 798, 810, 834, 858,
     876, 908, 926, 954, 978, 1002, 1030, 1058, 1098, 1110, 1134, 1160, 1192, 1216, 1248,
     1274, 1298]
N = len(J)


def primes(n):
    out, c = [], 2
    while len(out) < n:
        if all(c % p for p in out if p * p <= c):
            out.append(c)
        c += 1
    return out


P = primes(N)
Jk = lambda k: J[k - 1]
pk = lambda k: P[k - 1]

res = {"source": "OEIS A048670 b-file, n=1..71", "N": N}

# 1. one-step increments
inc = []
for k in range(2, N + 1):
    d = Jk(k) - Jk(k - 1)
    inc.append({"k": k, "p_k": pk(k), "J": Jk(k), "Delta": d,
                "ratio": round(Jk(k) / Jk(k - 1), 4), "Delta_over_p": round(d / pk(k), 4)})
res["increments"] = inc
tail = [r for r in inc if r["k"] >= 20]
res["one_step_summary_k_ge_20"] = {
    "max_ratio": max(r["ratio"] for r in tail),
    "argmax_ratio": max(tail, key=lambda r: r["ratio"])["k"],
    "max_Delta_over_p": max(r["Delta_over_p"] for r in tail),
    "min_Delta": min(r["Delta"] for r in tail),
    "max_Delta": max(r["Delta"] for r in tail),
    "mean_Delta_over_p": round(sum(r["Delta_over_p"] for r in tail) / len(tail), 4),
}

# 2. windowed ratios and local exponents
windows = {"1": lambda k: 1, "sqrt": lambda k: math.ceil(k ** 0.5),
           "k^0.8": lambda k: math.ceil(k ** 0.8), "k/2": lambda k: math.ceil(k / 2)}
win = {}
for name, wf in windows.items():
    rows = []
    for k in range(10, N + 1):
        w = wf(k)
        if k - w < 1:
            continue
        r = Jk(k) / Jk(k - w)
        a = math.log(r) / math.log(k / (k - w))
        rows.append({"k": k, "w": w, "ratio": round(r, 4), "alpha": round(a, 3)})
    big = [x for x in rows if x["k"] >= 30]
    win[name] = {
        "rows": rows,
        "k_ge_30": {
            "max_ratio": max(x["ratio"] for x in big),
            "argmax": max(big, key=lambda x: x["ratio"])["k"],
            "max_alpha": max(x["alpha"] for x in big),
            "min_alpha": min(x["alpha"] for x in big),
            "count_ratio_gt_1.5": sum(x["ratio"] > 1.5 for x in big),
            "count_ratio_gt_2": sum(x["ratio"] > 2 for x in big),
            "n": len(big),
        },
    }
res["windows"] = win

# 3. comparison with smooth models: J / (p_k log p_k), J / (k log^2 k), J / p_k
res["normalized"] = [{"k": k, "J/p": round(Jk(k) / pk(k), 3),
                      "J/(p log p)": round(Jk(k) / (pk(k) * math.log(pk(k))), 4),
                      "J/(k log^2 k)": round(Jk(k) / (k * math.log(k) ** 2), 4)}
                     for k in range(10, N + 1, 5)] + \
                    [{"k": N, "J/p": round(Jk(N) / pk(N), 3),
                      "J/(p log p)": round(Jk(N) / (pk(N) * math.log(pk(N))), 4),
                      "J/(k log^2 k)": round(Jk(N) / (N * math.log(N) ** 2), 4)}]

# 4. global growth exponent between k and k/2 (what Lemma 9.5 actually uses)
res["dyadic_exponent"] = [{"k": k, "log2(J(k)/J(k/2))": round(math.log2(Jk(k) / Jk(k // 2)), 3)}
                          for k in range(20, N + 1, 10)]

# 5. what Lemma 9.5 would need: the window w where a factor-C jump becomes
#    impossible given the observed maximal local exponent alpha_max:
#    (1 + w/k)^alpha_max <= C  <=>  w <= k (C^(1/alpha_max) - 1).
amax = win["sqrt"]["k_ge_30"]["max_alpha"]
res["implied_jump_free_window_C2_at_k71"] = round(N * (2 ** (1 / amax) - 1), 1)

# 6. smooth model J_s(k) = k log^2 k: spread of J/J_s and of Delta/J_s'
Js = lambda k: k * math.log(k) ** 2
dJs = lambda k: math.log(k) ** 2 + 2 * math.log(k)
ks = range(30, N + 1)
q = [Jk(k) / Js(k) for k in ks]
dq = [(Jk(k) - Jk(k - 1)) / dJs(k) for k in ks]
dq3 = [(Jk(k) - Jk(k - 3)) / (Js(k) - Js(k - 3)) for k in ks]
res["smooth_model_k_ge_30"] = {
    "J/(k log^2 k) min": round(min(q), 4), "J/(k log^2 k) max": round(max(q), 4),
    "Delta/J_s' min": round(min(dq), 3), "Delta/J_s' max": round(max(dq), 3),
    "3-step increment / model min": round(min(dq3), 3),
    "3-step increment / model max": round(max(dq3), 3),
}

# 7. one-step log-elasticity l(k) = k log(J(k) / J(k-1)).
#    Lemma 11.1: if l(k) <= k^(kappa/2) for all large k, then
#    J(k) / J(k - k^(1-kappa)) -> 1, i.e. (R1') holds for every C > 1.
#    Unconditionally the mean of l over (K, 2K] is <= 2 log(J(2K)/J(K)).
el = [k * math.log(Jk(k) / Jk(k - 1)) for k in ks]
res["elasticity_k_ge_30"] = {"min": round(min(el), 3), "max": round(max(el), 3),
                             "mean": round(sum(el) / len(el), 3),
                             "model_k_log2k_at_71": round(1 + 2 / math.log(N), 3)}
res["mean_elasticity_bound_K35"] = round(2 * math.log(Jk(70) / Jk(35)), 3)

out = __file__.replace(".py", ".json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(res, f, indent=1)

print("one-step (k>=20):", res["one_step_summary_k_ge_20"])
for name in windows:
    print(name, win[name]["k_ge_30"])
print("normalized:", res["normalized"][-3:])
print("dyadic exponent:", res["dyadic_exponent"])
print("jump-free window for C=2 at k=71 (using max local exponent):",
      res["implied_jump_free_window_C2_at_k71"])
