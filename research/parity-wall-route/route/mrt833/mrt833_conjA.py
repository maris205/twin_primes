"""route/mrt833: Conjecture A (REPORT2.md).  Python 3.

Part A (exact): exponent of the kappa-family and the slack of the weakest form.
Part B (exact): integer identities used in REPORT2.md section 2.
Part C (numerical): exhaustive l-averaged counts
    C(M, L, eta) = sum_{L <= l < 2L} #{(m1..m4) in [M,2M)^4 : |D_l(m)| <= eta},
    D_l = (m1+m2)(m3 m4 + l^2) - (m3+m4)(m1 m2 + l^2),
at the worst-point scaling L ~ M^{3/10}, eta ~ M/L, compared with
    conj   = L (2 M^2 + M eta)      (Conjecture A, ordered diagonal = 2M^2)
    MRT    = L^{3/2} M^2            (what MRT's box argument is equivalent to)
"""
from fractions import Fraction as F
import random
import sys
import time

# ---------------------------------------------------------------- Part A
def sigma_kappa(kappa):
    """sum_l N_l << M^{2+e} L^{1+kappa} (+ L M eta)  =>  sigma = (7+2k)/(6(5+k))."""
    k = F(kappa)
    return (7 + 2 * k) / (6 * (5 + k))

def slack(mu, tau, s=F(7, 30)):
    """Exponent of X: requirement minus Conjecture-A size, at M = X^mu, T = X^tau,
    L = M/H (worst L), H = X^s.  Requirement (from Prop 7.5):
        sum_l N_l <= H^3 M^2 / (L sqrt T)  =  H^4 M / sqrt T   (L = M/H).
    Conjecture A size: L M^2 + L M eta = L M^2 + M^5/T."""
    req = 4 * s + mu - tau / 2
    conj = max(mu - s + 2 * mu, 5 * mu - tau)
    div = mu - s + 2 * mu + max(0, 4 * mu - tau - (mu - s))  # L M^2 (1+eta)
    return req - conj, req - div

def part_a():
    for k in [0, F(1, 4), F(1, 2), 1]:
        print("  kappa=%-4s -> sigma = %s = %.5f" % (k, sigma_kappa(k), float(sigma_kappa(k))))
    worst = None
    for i in range(0, 41):
        mu = F(1, 6) + F(i, 240)          # mu in [1/6, 1/3]
        for j in range(0, 21):
            tau = F(5, 6) + F(j, 120)      # tau in [5/6, 1]
            sl, sd = slack(mu, tau)
            if worst is None or sl < worst[0]:
                worst = (sl, mu, tau)
    print("  min slack of Conjecture A over grid: %s at mu=%s tau=%s" % worst)
    # divisor bound N_l << M^{2+e}(1+eta) suffices iff M^5 <= H^4 sqrt(T)
    s = F(7, 30)
    mu_div = (4 * s + F(1, 2)) / 5
    print("  divisor bound suffices for 7/30 when M <= X^%s = X^%.4f" % (mu_div, float(mu_div)))
    # RS transfer (section 3.1): kappa = 1  ->  sigma
    print("  RS-transfer (kappa=1) -> sigma =", sigma_kappa(1))

# ---------------------------------------------------------------- Part B
def D(m1, m2, m3, m4, l):
    return (m1 + m2) * (m3 * m4 + l * l) - (m3 + m4) * (m1 * m2 + l * l)

def part_b(trials=3000):
    rnd = random.Random(7)
    for _ in range(trials):
        l = rnd.randint(0, 60)
        m1, m2, m3, m4 = [rnd.randint(l + 1, 500) for _ in range(4)]
        s, sp = m1 + m2, m3 + m4
        q = m1 * m2 + l * l
        d = s - sp
        Dv = D(m1, m2, m3, m4, l)
        E = m3 * m4 * s - m1 * m2 * sp
        # (1) D = E + d l^2 ,  E = m1 m2 m3 m4 * (1/m1 + 1/m2 - 1/m3 - 1/m4)
        assert Dv == E + d * l * l
        assert F(E) == m1 * m2 * m3 * m4 * (F(1, m1) + F(1, m2) - F(1, m3) - F(1, m4))
        # (2) factorisation: (s m3 - q)(s m4 - q) = (m1^2 - l^2)(m2^2 - l^2) + s D
        assert (s * m3 - q) * (s * m4 - q) == (m1 * m1 - l * l) * (m2 * m2 - l * l) + s * Dv
        # (3) 4D = s t - d (w - 2l)(w + 2l),  t = w^2 - z^2 - d s + d^2
        w, z = m1 - m2, m3 - m4
        t = w * w - z * z - d * s + d * d
        assert 4 * Dv == s * t - d * (w - 2 * l) * (w + 2 * l)
        # (4) D linear in m1: D = m1 c1 + c0, c1 = (m2-m3)(m2-m4) - m2^2 + l^2,
        #     c0/c1 = B + (m3+m4)(m2-m3)(m2-m4)/c1,  B = m2 - m3 - m4
        c1 = (m2 - m3) * (m2 - m4) - m2 * m2 + l * l
        c0 = Dv - m1 * c1
        assert c0 == m2 * m3 * m4 + l * l * (m2 - m3 - m4)
        if c1 != 0:
            assert F(c0, c1) == (m2 - m3 - m4) + F((m3 + m4) * (m2 - m3) * (m2 - m4), c1)
    print("  identities (1)-(4) verified on %d random cases" % trials)

# ---------------------------------------------------------------- Part C
def count_l(M, l, eta):
    """#{ordered (m1..m4) in [M,2M)^4 : |D_l| <= eta}; D_l = det(v, v'),
    v = (a+b, ab+l^2).  Sort by slope, scan an exact window."""
    mult = {}
    for a in range(M, 2 * M):
        for b in range(a, 2 * M):
            key = (a + b, a * b + l * l)
            mult[key] = mult.get(key, 0) + (1 if a == b else 2)
    keys = sorted(mult, key=lambda k: k[0] / k[1])
    sl = [k[0] / k[1] for k in keys]
    qmin = min(k[1] for k in keys)
    n = len(keys)
    tot = 0
    for i in range(n):
        s, q = keys[i]
        c = mult[keys[i]]
        win = (eta + 1.0) / (q * qmin)
        lo = sl[i] - win
        hi = sl[i] + win
        j = i
        while j >= 0 and sl[j] >= lo:
            j -= 1
        j += 1
        while j < n and sl[j] <= hi:
            s2, q2 = keys[j]
            if abs(s * q2 - s2 * q) <= eta:
                tot += c * mult[keys[j]]
            j += 1
    return tot

def part_c(Ms):
    print("  %-5s %-3s %-5s %-12s %-12s %-6s %-12s %-6s %s"
          % ("M", "L", "eta", "C", "conj", "C/conj", "MRT", "C/MRT", "sec"))
    for M in Ms:
        L = max(1, int(round(M ** 0.3)))
        eta = max(1, M // L)
        t0 = time.time()
        C = sum(count_l(M, l, eta) for l in range(L, 2 * L))
        conj = L * (2 * M * M + M * eta)
        mrt = L ** 1.5 * M * M
        print("  %-5d %-3d %-5d %-12d %-12d %-6.3f %-12d %-6.3f %.0f"
              % (M, L, eta, C, conj, C / conj, int(mrt), C / mrt, time.time() - t0))
        sys.stdout.flush()

if __name__ == "__main__":
    print("Part A (exact):")
    part_a()
    print("Part B (exact):")
    part_b()
    Ms = [int(x) for x in sys.argv[1:]] or [50, 100, 200, 400]
    print("Part C (numerical):")
    part_c(Ms)
