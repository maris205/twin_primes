---
type: "source-reading"
source_path: "papers/tpc-347-convolution-mask-defect-interface/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-347"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-347-convolution-mask-defect-interface/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-347|TPC-347]] · [[00_开始阅读|首页]]

# TPC-347 proof and scope package

## Proposition 1: mask factorisation

For every finite interval `I`, shell prime `p`, and exponent `s`, the physical block equals `R_I P_p K_p P_p E_I`.

**Proof.** The `(u,t)` entry of the right-hand side is zero when `u=t` by the definition of `k_p`, and is zero when either endpoint is divisible by `p` because of the two diagonal projections. Otherwise it is exactly the displayed kernel entry. Summing with `e_p` proves the assertion. ∎

## Proposition 2: exact defect identity

With `T_I=R_I K_e E_I` and `D_I=A_I-T_I`,

```text
D_I = sum_p e_p R_I ((P_p-I)K_pP_p + K_p(P_p-I)) E_I.
```

**Proof.** Expand the right side for one prime: `(P-I)KP+K(P-I)=PKP-KP+KP-K=PKP-K`. Apply `R_I` and `E_I`, then sum over the finite shell. ∎

## Proposition 3: Fourier multiplier norm

For the absolutely summable kernel `k_e`, convolution on `ell^2(Z)` has norm `ess sup |khat_e|`.

**Proof.** Fourier transformation is unitary on `ell^2(Z)` and maps an absolutely summable convolution kernel to multiplication by its continuous Fourier series. The norm of a multiplication operator is the essential supremum of the multiplier. ∎

## Proposition 4: compression and finite triangle bound

`||R_I K_e E_I||<=||K_e||` and `||A_I||<=||K_e||+||D_I||_F`.

**Proof.** Restriction and zero extension have norm one. Apply the triangle inequality to `A_I=T_I+D_I`, then use `||D_I||<=||D_I||_F`. ∎

## Proposition 5: finite certificate

The declared two-origin, three-count, four-shell, two-exponent, four-law grid contains `192` rows. The independent replay verifies all stored spectral metrics, `96/96` ideal translation identities, and `192/192` combined-bound checks. The exact six-point anchor verifies the decomposition over the rationals.

The maximum observed defect-to-ideal ratio is `0.467075645603`, and `93` rows are above `1/4`. This is a finite obstruction to dropping the masks on the declared grid, not a uniform asymptotic lower bound.

## Claim ceiling

```text
MASK_FACTORISATION = PROVED_EXACT_FINITE_DECLARED_MODEL
FOURIER_INTERFACE = PROVED_EXACT_CONDITIONAL
YOUNG_ENVELOPE = PROVED_EXACT_FOR_UNMASKED_KERNEL
FINITE_AUDIT = NUMERICALLY_CERTIFIED_FINITE_192_ROWS
MASK_DISCARD_SHORTCUT = REFUTED_SCOPED
SOURCE_UNIFORM_ARITHMETIC_L2 = OPEN
UNIFORM_MASKED_OPERATOR_BOUND = OPEN
ARITHMETIC_ADVANCE = NO
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```
