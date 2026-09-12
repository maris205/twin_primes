---
type: "source-reading"
source_path: "papers/tpc-157-literal-weight-periodic-approximation/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-157"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-157-literal-weight-periodic-approximation/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-157|TPC-157]] · [[00_开始阅读|首页]]

# TPC-157: Literal-weight periodic approximation

Paper title:

> *Periodic Approximation of Literal Multipliers on Determinant-Two Mobius Fibers*

TPC-149 controls every bounded periodic multiplier on the literal determinant-two two-Mobius core. This paper gives the exact interface for a nonperiodic literal multiplier `w`.

For

```text
q = a*s,
t(z) = a*d+q*z,
c(z) = mu(d+s*z) mu(u+a*z),
I_N = {z : N < t(z) <= 2N},
```

define

```text
A_R,N(w) =
  inf over period-R rho of
  [ ||rho||_infinity (log X)^(-kappa_0)
    + (q/N) sum over I_N |w-rho| ].
```

Outside the same TPC-149 exceptional set, and whenever `q*R <= (log X)^eta_0`,

```text
(q/N) |sum c(z) w(z)| << A_R,N(w).
```

There is no additional exceptional-set union: the TPC-149 theorem is already simultaneous in the values of the periodic function `rho`. The unpenalized approximation-error term separates exactly over residue fibers. The infinity-norm penalty in the full cost couples the fibers through their maximum. For the quadratic error certificate, the best period-R approximation is the mean on each fiber.

This is an `L1_ACTUAL_CORE_WEIGHT_INTERFACE` theorem. It becomes a literal physical-weight result only after an actual occurrence registry supplies `w` and proves a decaying approximation cost. That production input is currently `NOT_TESTABLE`. No generic phase, all-prefix result, fixed-X power saving, `1/400`, prime-pair lower bound, or twin-prime theorem is claimed.

Reproduce with:

```powershell
python experiments/tpc157_periodic_approximation_audit.py
python experiments/tpc157_periodic_approximation_audit.py --check
```
