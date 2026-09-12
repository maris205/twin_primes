---
type: "source-reading"
source_path: "papers/tpc-333-source-polarization-cross-term/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-333"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-333-source-polarization-cross-term/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-333|TPC-333]] · [[00_开始阅读|首页]]

# TPC-333 proof and scope package

## Proposition 1 — finite polarization identity

For any finite real vectors `a,b`,

```text
||a-b||_2^2 = ||a||_2^2 + ||b||_2^2 - 2<a,b>.
```

**Proof.** Expand the inner product and use symmetry of the real inner product. `QED`.

## Proposition 2 — dimensionless complement

If `S=||a||^2+||b||^2>0`, then `rho=||a-b||^2/S=1-kappa`, where `kappa=2<a,b>/S`.

**Proof.** Divide Proposition 1 by `S`. `QED`.

## Proposition 3 — finite certificate

The TPC-333 certificate has six unique source windows and four adjacent nested-scale pairs. Every row has finite positive component norms, an identity replay error below the recorded guard, and a cancellation coefficient strictly between `0.35` and `0.37`.

**Evidence.** The producer reconstructs the parent-locked source model; the independent checker uses a separate trial sieve, reverse factorization, and reverse product order. The stress suite rejects five mutations. This is `NUMERICALLY_CERTIFIED_FINITE`, not a growing theorem.

## Scope obstruction

The finite data refute only the scoped alternatives “the two components are nearly orthogonal” and “the residual is nearly canceled” for these six windows. They do not bound the coefficient for arbitrary origins or scales, do not identify twin-prime support, and do not pay any route gate.
