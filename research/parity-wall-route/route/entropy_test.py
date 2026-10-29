"""Entropy-decrement falsification test: twin (sparse rough) vs Chowla (dense).

For n in (x/2, x] let X_H(n) = (h(n+1), ..., h(n+H)) with
    Chowla: h = lambda                      (values +-1)
    twin:   h = lambda * 1[n is z-rough]    (values -1, 0, +1)
and Phi(n) = mean_{1<=j<=H-2} h(n+j) h(n+j+2), the window version of the
shift-2 correlation that the dilation step must decouple from 1_{p|n}.

Measured, for each setting:
  H_X        block entropy of X_H (bits) -- the entropy-decrement budget
  sigma      E|h(n)h(n+2)|                -- size of the signal
  var_phi    Var Phi
  per prime p (in bands): I_p = I(X_H; n mod p) (Miller-Madow corrected),
             a shuffled-label bias floor, KL0 = KL(P_{X|p|n} || P_X),
             D_p = |E[Phi | p|n] - E[Phi]| (the actual decoupling error),
             B_inf = 2*sqrt(KL0/2) (Pinsker, |Phi|<=1) and
             B_2 = sqrt(2*KL0*var_phi) (optimistic chi^2 ~ 2KL version).
Derived: KL_needed = eps^2 sigma^2 / (2 var_phi) for relative precision eps,
and the budget ratio H_X / KL_needed (how many 'decrement units' the
entropy budget must pay for).

usage: python entropy_test.py XMAX [H]
"""
import sys, json, math, time
import numpy as np

XMAX = int(float(sys.argv[1]))
H = int(sys.argv[2]) if len(sys.argv) > 2 else 8
ZS = [None, 5, 7, 13, 23, 53, 101]   # None = Chowla; otherwise twin with z-rough
BANDS = [5, 30, 100, 300]       # primes in [P, 2P)
PER_BAND = 8
EPS = 0.1
SEG = 10_000_000
LN2 = math.log(2)
rng = np.random.default_rng(1)


def primes_upto(m):
    s = np.ones(m + 1, bool); s[:2] = False
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def first_mult(a, p):
    return ((a + p - 1) // p) * p - a


def omega_and_rough(a, b, plist, zs):
    """Omega(n) for n in [a, b), and n's smallest prime factor capped at max z."""
    n = b - a
    rem = np.arange(a, b, dtype=np.int64)
    om = np.zeros(n, np.int8)
    zmax = max(z for z in zs if z)
    spf_small = np.full(n, 10 ** 9, np.int32)   # smallest prime factor if < zmax
    for p in plist:
        p = int(p)
        s = first_mult(a, p)
        if s >= n:
            continue
        if p < zmax:
            v = spf_small[s::p]
            np.minimum(v, p, out=v)
        pk = p
        while pk < b:
            s = first_mult(a, pk)
            if s >= n:
                break
            om[s::pk] += 1
            rem[s::pk] //= p
            if pk > b // p:
                break
            pk *= p
    om += (rem > 1).astype(np.int8)
    return om, spf_small


def main():
    t0 = time.time()
    lo, hi = XMAX // 2 + 1, XMAX + 1           # n in [lo, hi)
    plist = primes_upto(int((hi + H + 2) ** 0.5) + 1)
    bands = {}
    allp = primes_upto(2 * max(BANDS))
    for P in BANDS:
        ps = [int(p) for p in allp if P <= p < 2 * P][:PER_BAND]
        bands[P] = ps
    ps_all = sorted({p for v in bands.values() for p in v})
    shuf_ps = [bands[P][0] for P in BANDS]

    st = {}
    for z in ZS:
        base = 2 if z is None else 3
        K = base ** H
        st[z] = dict(base=base, K=K, cx=np.zeros(K, np.int64),
                     cmask=np.zeros(2 ** H, np.int64), dnoise=[],
                     joint={p: np.zeros(K * p, np.int64) for p in ps_all},
                     shuf={p: np.zeros(K * p, np.int64) for p in shuf_ps},
                     phi_sum=0.0, phi_sq=0.0, sig_sum=0.0, N=0,
                     phi0={p: [0.0, 0] for p in ps_all})

    for a in range(lo, hi, SEG):
        b = min(a + SEG, hi)
        om, spf = omega_and_rough(a, b + H + 2, plist, ZS)
        lam = (1 - 2 * (om & 1)).astype(np.int8)
        nseg = b - a
        nn = np.arange(a, b, dtype=np.int64)
        for z in ZS:
            S = st[z]
            h = lam if z is None else (lam * (spf >= z)).astype(np.int8)
            sym = (h + 1) // 2 if z is None else (h + 1)   # 0..base-1
            code = np.zeros(nseg, np.int64)
            for j in range(H):
                code = code * S['base'] + sym[1 + j:1 + j + nseg]
            prod = np.zeros(nseg, np.float64)
            for j in range(1, H - 1):
                prod += h[j:j + nseg].astype(np.float64) * h[j + 2:j + 2 + nseg]
            phi = prod / (H - 2)
            S['cx'] += np.bincount(code, minlength=S['K'])
            mcode = np.zeros(nseg, np.int64)
            for j in range(H):
                mcode = mcode * 2 + (h[1 + j:1 + j + nseg] != 0)
            S['cmask'] += np.bincount(mcode, minlength=2 ** H)
            # noise floor for D: Phi averaged over random subsets of size nseg/p
            for P in BANDS:
                k = max(nseg // P, 1)
                idx = rng.integers(0, nseg, k)
                S['dnoise'].append((P, float(phi[idx].mean()), k))
            S['phi_sum'] += phi.sum(); S['phi_sq'] += (phi * phi).sum()
            S['sig_sum'] += np.abs(h[:nseg].astype(np.int64) * h[2:2 + nseg]).sum()
            S['N'] += nseg
            for p in ps_all:
                r = nn % p
                S['joint'][p] += np.bincount(code * p + r, minlength=S['K'] * p)
                m0 = r == 0
                S['phi0'][p][0] += phi[m0].sum(); S['phi0'][p][1] += int(m0.sum())
            for p in shuf_ps:
                r = rng.integers(0, p, nseg)
                S['shuf'][p] += np.bincount(code * p + r, minlength=S['K'] * p)
        print(f"segment {a}-{b} done, {time.time()-t0:.0f}s", flush=True)

    def H_bits(c):
        c = c[c > 0].astype(np.float64); q = c / c.sum()
        return float(-(q * np.log2(q)).sum())

    def mi_mm(joint, K, p):
        J = joint.reshape(K, p).astype(np.float64); N = J.sum()
        px, py = J.sum(1), J.sum(0)
        nz = J > 0
        mi = float((J[nz] / N * np.log2(J[nz] * N / np.outer(px, py)[nz])).sum())
        kxy, kx, ky = nz.sum(), (px > 0).sum(), (py > 0).sum()
        return mi, mi - (kxy - kx - ky + 1) / (2 * N * LN2)

    out = dict(x=XMAX, H=H, eps=EPS, settings=[])
    for z in ZS:
        S = st[z]; N = S['N']; K = S['K']
        HX = H_bits(S['cx'])
        Hmask = H_bits(S['cmask'])
        mean_phi = S['phi_sum'] / N
        var_phi = S['phi_sq'] / N - mean_phi ** 2
        sigma = S['sig_sum'] / N
        kl_need = EPS ** 2 * sigma ** 2 / (2 * var_phi) if var_phi > 0 else float('nan')
        rec = dict(setting='chowla' if z is None else f'twin z={z}', z=z,
                   N=N, H_X_bits=HX, H_X_per_site=HX / H, H_mask_bits=Hmask,
                   H_sign_bits=HX - Hmask, sigma=sigma,
                   mean_phi=mean_phi, var_phi=var_phi, KL_needed=kl_need,
                   KL_needed_pinsker=EPS ** 2 * sigma ** 2 / 2,
                   budget_ratio=HX / kl_need,
                   sign_budget_ratio=(HX - Hmask) / kl_need,
                   sign_budget_ratio_pinsker=(HX - Hmask) / (EPS ** 2 * sigma ** 2 / 2),
                   bands=[])
        px = S['cx'] / N
        for P in BANDS:
            rows = []
            for p in bands[P]:
                J = S['joint'][p].reshape(K, p)
                mi, mi_c = mi_mm(S['joint'][p], K, p)
                c0 = J[:, 0].astype(np.float64); n0 = c0.sum()
                q0 = c0 / n0; nz = q0 > 0
                kl0 = float((q0[nz] * np.log2(q0[nz] / px[nz])).sum())
                kl0_c = kl0 - (nz.sum() - 1) / (2 * n0 * LN2)
                kl0_nats = max(kl0_c, 0.0) * LN2
                phi0 = S['phi0'][p][0] / S['phi0'][p][1]
                D = abs(phi0 - mean_phi)
                rows.append(dict(p=p, I_plugin=mi, I_mm=mi_c, KL0_bits=kl0_c,
                                 D=D, D_over_sigma=D / sigma,
                                 B_inf=2 * math.sqrt(kl0_nats / 2),
                                 B_2=math.sqrt(2 * kl0_nats * var_phi)))
            sh = None
            p0 = bands[P][0]
            if p0 in S['shuf']:
                sh = mi_mm(S['shuf'][p0], K, p0)[1]
            dn = [abs(m - mean_phi) for (PP, m, k) in S['dnoise'] if PP == P]
            rec['bands'].append(dict(P=P, primes=bands[P], rows=rows,
                                     shuffled_I_mm=sh,
                                     D_noise_over_sigma=float(np.mean(dn)) / sigma,
                                     sum_I_over_p=sum(r['I_mm'] / r['p'] for r in rows),
                                     mean_I=float(np.mean([r['I_mm'] for r in rows])),
                                     mean_D_over_sigma=float(np.mean([r['D_over_sigma'] for r in rows])),
                                     mean_Binf_over_sigma=float(np.mean([r['B_inf'] for r in rows])) / sigma,
                                     mean_B2_over_sigma=float(np.mean([r['B_2'] for r in rows])) / sigma))
        out['settings'].append(rec)
    out['seconds'] = time.time() - t0
    fn = f"entropy_test_{XMAX:.0e}_H{H}.json".replace('+', '')
    with open(fn, 'w') as f:
        json.dump(out, f, indent=1)
    for rec in out['settings']:
        print(f"\n== {rec['setting']}: H_X={rec['H_X_bits']:.3f} bits, H_mask={rec['H_mask_bits']:.3f}, "
              f"H_sign={rec['H_sign_bits']:.3f}, sigma={rec['sigma']:.4f}, var_phi={rec['var_phi']:.3e}, "
              f"J_chi2={rec['sign_budget_ratio']:.3e}, J_pinsker={rec['sign_budget_ratio_pinsker']:.3e}")
        for bd in rec['bands']:
            print(f"  P={bd['P']:4d}: mean I={bd['mean_I']:.2e} (shuffled {bd['shuffled_I_mm']:.1e}), "
                  f"sum I/p={bd['sum_I_over_p']:.2e}, D/sigma={bd['mean_D_over_sigma']:.2e} "
                  f"(noise {bd['D_noise_over_sigma']:.1e}), "
                  f"Binf/sigma={bd['mean_Binf_over_sigma']:.2e}, B2/sigma={bd['mean_B2_over_sigma']:.2e}")
    print(f"\nwrote {fn} in {out['seconds']:.0f}s")


if __name__ == '__main__':
    main()
