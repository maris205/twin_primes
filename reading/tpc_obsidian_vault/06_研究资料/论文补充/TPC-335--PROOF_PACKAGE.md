---
type: "source-reading"
source_path: "papers/tpc-335-twin-isolated-source-norm/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-335"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-335-twin-isolated-source-norm/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-335|TPC-335]] · [[00_开始阅读|首页]]

# TPC-335 proof and scope package

## Proposition 1 — finite masked norm identity

For a disjoint exhaustive finite partition `I=disjoint_union_C I_C` and `beta_C=beta 1_{I_C}`,

```text
||beta||_2^2 = sum_C ||beta_C||_2^2.
```

**Proof.** Expand both sides as finite sums. Each coordinate occurs exactly once and all cross terms between distinct coordinate supports are zero. `QED`.

## Proposition 2 — source support partition

The four TPC-334 labels form such a partition for the declared source array: the first three separate nonzero cross support, and `zero_support` contains the complement. `QED` follows from the prime-power support implication in TPC-334.

## Proposition 3 — finite certificate

The six rows satisfy the exact masked norm identity to the recorded replay guard. Twin norm fractions lie in `(0.09,0.13)` and background fractions in `(0.65,0.72)` for all six rows. This is `NUMERICALLY_CERTIFIED_FINITE` and does not imply a source-uniform bound.
