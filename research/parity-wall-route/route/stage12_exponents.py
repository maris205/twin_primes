"""Stage 12: exponent bookkeeping for the Type d3 step of Matomaki-Radziwill-Tao
(arXiv:1707.01315, Sections 7-8). Exact rational arithmetic.

Notation (all as powers of X): H = X^s, T = lambda*X with X^{-1/6} <~ lambda <~ 1,
M1 <~ X^{1/3}, L ~ M1/H, r ~ sqrt(T) windows.

MRT (end of Sec. 8):  sum_j Y(t_j)^4 << X^{4/3} + H^{-3/2} lambda X^{11/6}
target (Prop 7.5):    sum_j Y(t_j)^4 << X^{-eps} H^4 sqrt(lambda X)
"""
from fractions import Fraction as F

def thresholds():
    # term H^{-3/2} lam X^{11/6} <= H^4 lam^{1/2} X^{1/2}: worst lam = 1
    s_main = (F(11, 6) - F(1, 2)) / (F(4) + F(3, 2))
    # term X^{4/3} <= H^4 (lam X)^{1/2}: worst lam = X^{-1/6}
    s_low = (F(4, 3) - F(1, 2) * (1 - F(1, 6))) / 4
    return s_main, s_low

def sigma_theta(theta):
    """Interpolate the binding term between MRT (theta=1) and the square-root
    ideal r*M1^2 (theta=0):  sqrt(T) M1^2 (sqrt(T) M1^{1/2} H^{-3/2})^theta <= H^4 sqrt(T),
    at lam = 1, M1 = X^{1/3}."""
    theta = F(theta)
    return (F(2, 3) * (1 + theta)) / (4 + F(3, 2) * theta)

def theta_for(target):
    # solve (2/3)(1+th) = target (4 + 3/2 th)
    target = F(target)
    return (4 * target - F(2, 3)) / (F(2, 3) - F(3, 2) * target)

if __name__ == "__main__":
    s_main, s_low = thresholds()
    print("binding d3 term  ->", s_main, float(s_main))       # 8/33
    print("X^{4/3} d3 term  ->", s_low, float(s_low))         # 11/48
    print("theta=1 (MRT)    ->", sigma_theta(1))
    print("theta=0 (ideal)  ->", sigma_theta(0))
    d4_classical, d4_robert, d5_gate = F(7, 30), F(3, 13), F(1, 5)
    print("d4: classical", d4_classical, float(d4_classical), "| Robert", d4_robert, float(d4_robert))
    th = theta_for(d4_robert)
    print("theta needed for d3 to reach 3/13 ->", th, float(th))
    print("best overall from improving d3 alone ->", max(s_low, d4_robert), float(max(s_low, d4_robert)))
    for t in [1, F(9, 10), F(4, 5), F(1, 2), 0]:
        s = sigma_theta(t)
        print("  theta=%5s: d3 sigma = %8s = %.4f; overall = %.4f" % (t, s, float(s), float(max(s, s_low, d4_robert))))
