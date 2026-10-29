"""route/mrt833: exponent bookkeeping and small checks for the Type d3 step of
Matomaki-Radziwill-Tao (arXiv:1707.01315, Sec. 7-8).  Runs under Python 2.7 and 3.

Notation (powers of X): T = lambda*X in [X^{5/6}, X], M = M1 <= X^{1/3},
H = X^s, L <= M/H, S_l(t) = sum_{m~M} ((m+l)/(m-l))^{it},
eta = M^4/(T*l)  (counting precision, see REPORT.md section 2).

Part A: exact rational arithmetic for all exponents quoted in REPORT.md.
Part B: exact-integer checks of the artanh identity and the bilinear form D.
Part C: (numerical, small M) brute-force counts N_l(eta) versus M^2 + M*eta.
"""
from __future__ import print_function
from fractions import Fraction as F
import random

# ---------------------------------------------------------------- Part A
def solve_sigma(coef_H, const):
    """Smallest s with  coef_H*s >= const  (all exponents of X)."""
    return F(const) / F(coef_H)

def part_a():
    third = F(1, 3)
    out = []
    # MRT: H^{-3/2} lam X^{11/6} <= H^4 sqrt(lam X), worst lam = 1
    out.append(("MRT binding term", solve_sigma(F(11, 2), F(11, 6) - F(1, 2))))
    # conditional per-l fourth moment: T M^2 / H <= H^4 sqrt(T); T = X, M = X^{1/3}
    out.append(("Conj A: T M^2/H term", solve_sigma(5, 1 + 2 * third - F(1, 2))))
    # M^4 <= H^4 sqrt(T), worst T = X^{5/6}
    out.append(("Conj A: M^4 term (T=X^{5/6})", solve_sigma(4, 4 * third - F(5, 12))))
    # unconditional divisor count N << M^{2+e}(1+eta): extra term M^5 <= H^4 sqrt(X)
    out.append(("divisor count: M^5 term", solve_sigma(4, 5 * third - F(1, 2))))
    # sixth moment route (k=3), even with the true size int|S|^6 ~ M^7/l:
    #   T^{1/6} M^4 <= H^4 sqrt(T), T = X
    out.append(("sixth-moment route", solve_sigma(4, 4 * third + F(1, 6) - F(1, 2))))
    # hypothetical diagonal sixth moment int|S|^6 << T M^3 (FALSE, see report):
    #   sqrt(T) M^2 (sqrt(T)/H)^{2/3} <= H^4 sqrt(T)  ->  H^{14/3} >= M^2 T^{1/3}
    out.append(("(false) diagonal 6th moment", solve_sigma(F(14, 3), 2 * third + third)))
    for name, s in out:
        print("  %-32s sigma >= %-6s = %.5f" % (name, s, float(s)))
    # interpolation parameter theta of stage 12 for 7/30
    s = F(7, 30)
    theta = (4 * s - F(2, 3)) / (F(2, 3) - F(3, 2) * s)
    print("  stage-12 theta giving 7/30:", theta)
    # saving needed beyond Conj A to reach 3/13 at T=X, M=X^{1/3}
    s = F(3, 13)
    need = (1 + 2 * third - s) - (4 * s + F(1, 2))
    print("  extra saving needed at 3/13 beyond Conj A: X^%s" % need)
    # effective per-l count implied by MRT: N_MRT = M^{5/2} eta^{-1/2} (T=X, eta=H)
    for s in [F(8, 33), F(7, 30), F(3, 13)]:
        eta = 3 * s                      # eta = H = M^{3s} in units of M
        allowed = (5 * s - F(1, 2)) * 3  # N <= H^5/sqrt(T) in units of M
        print("  s=%-5s eta=M^%-6s allowed N<=M^%-7s MRT N=M^%-7s conj N=M^%-5s divisor N=M^%s"
              % (s, eta, allowed, F(5, 2) - eta / 2, max(F(2), 1 + eta), 2 + eta))
    # Halasz-Montgomery window: needs V^2 >= M*K, K >= sqrt(M): V >= M^{3/4} = X^{1/4}
    print("  large values to control: V in [H, M] = [X^%s, X^%s]; Halasz needs V >= X^%s"
          % (F(3, 13), third, F(1, 4)))

# ---------------------------------------------------------------- Part B
def D(m1, m2, m3, m4, l):
    return (m1 + m2) * (m3 * m4 + l * l) - (m3 + m4) * (m1 * m2 + l * l)

def part_b(trials=2000):
    rnd = random.Random(1)
    for _ in range(trials):
        l = rnd.randint(1, 50)
        m = [rnd.randint(l + 1, 400) for _ in range(4)]
        m1, m2, m3, m4 = m
        # artanh addition: (m1+l)(m2+l)/((m1-l)(m2-l)) = (1+l u)/(1-l u)
        u = F(m1 + m2, m1 * m2 + l * l)
        assert F((m1 + l) * (m2 + l), (m1 - l) * (m2 - l)) == (1 + l * u) / (1 - l * u)
        # P - Q = 2 l D, P = (m1+l)(m2+l)(m3-l)(m4-l), Q = P(-l)
        P = (m1 + l) * (m2 + l) * (m3 - l) * (m4 - l)
        Q = (m1 - l) * (m2 - l) * (m3 + l) * (m4 + l)
        assert P - Q == 2 * l * D(m1, m2, m3, m4, l)
        # (s,w,z,d) form: 4D... check 4E = s' w^2 - s z^2 - s s' d, E = D - l^2 d
        s, sp = m1 + m2, m3 + m4
        w, z, d = m1 - m2, m3 - m4, s - sp
        E = m3 * m4 * s - m1 * m2 * sp
        assert 4 * E == sp * w * w - s * z * z - s * sp * d
        assert D(m1, m2, m3, m4, l) == E + d * l * l
    print("  identities verified on %d random cases" % trials)

# ---------------------------------------------------------------- Part C
def count_N(M, l, eta):
    """#{(m1,m2,m3,m4) in [M,2M)^4 : |D| <= eta}, via pairs v=(s, p+l^2)."""
    vs = {}
    for a in range(M, 2 * M):
        for b in range(M, 2 * M):
            key = (a + b, a * b + l * l)
            vs[key] = vs.get(key, 0) + 1
    items = sorted(vs.items(), key=lambda kv: F(kv[0][0], kv[0][1]))
    # sort by slope s/q; |s q' - s' q| <= eta  <=>  |s/q - s'/q'| <= eta/(q q')
    n = len(items)
    slopes = [float(k[0]) / k[1] for k, _ in items]
    qmin = min(k[1] for k, _ in items)
    tot = 0
    j0 = 0
    for i in range(n):
        (s, q), c = items[i]
        win = (eta + 0.5) / (q * qmin)
        while slopes[j0] < slopes[i] - win:
            j0 += 1
        j = j0
        while j < n and slopes[j] <= slopes[i] + win:
            (s2, q2), c2 = items[j]
            if abs(s * q2 - s2 * q) <= eta:
                tot += c * c2
            j += 1
    return tot

def part_c():
    print("  M   l   eta    N_l(eta)   M^2+M*eta   ratio   M^2*(1+eta)")
    for M in [24, 48, 96]:
        for l in [2, M // 8]:
            for eta in [0, M // 8, M // 2, M]:
                N = count_N(M, l, eta)
                ref = M * M + M * eta
                print("  %-3d %-3d %-5d %-10d %-11d %-7.2f %d" % (M, l, eta, N, ref, float(N) / ref, M * M * (1 + eta)))

if __name__ == "__main__":
    print("Part A (exact):")
    part_a()
    print("Part B (exact):")
    part_b()
    print("Part C (numerical):")
    part_c()
