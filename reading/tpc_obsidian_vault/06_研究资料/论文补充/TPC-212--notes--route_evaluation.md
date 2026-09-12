---
type: "source-reading"
source_path: "papers/tpc-212-truncated-boundary-emitter/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-212"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-212-truncated-boundary-emitter/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-212|TPC-212]] · [[00_开始阅读|首页]]

# Route Evaluation

## Route A

```text
A0 = NOT_APPLICABLE
A1 = NOT_APPLICABLE
A2 = NOT_APPLICABLE
A3 = NOT_APPLICABLE
A4 = NOT_APPLICABLE
```

This project remains in the analytic prime/twin-prime family, not the dynamical spectral Route-A family.

## Route B

```text
STRUCTURAL_THRESHOLD_A = PASS
CUT_ENDPOINT_LEAKAGE = PROVED_EXACT
BOUNDARY_DECOMPOSITION = PROVED_EXACT
RECIPROCAL_COLLISION = PROVED_EXACT_FINITE
EMITTER_GRAM = PROVED_EXACT_BLOCK_DIAGONAL
EMITTER_ONLY_UNIVERSAL_SAVING = REFUTED_SCOPED
LITERAL_PHYSICAL_BOUNDARY_BOUND = OPEN
PHYSICAL_CROSS_DIVISOR_GRAM_BOUND = OPEN
FULL_GATE_B = OPEN
STRICT_1_OVER_400 = UNPAID
ARITHMETIC_ADVANCE = NO
L2 = NONE
FIXED_ATOM_CREDIT = 0
```

## Strongest positive result

The cut is an exact Boolean-incidence operator, and the reciprocal occupancy norm is an exact determinant-free collision count. These identities expose the precise operator that must be estimated.

## Strongest obstruction

In the natural direct-sum residual space, the emitter Gram is block diagonal and full rank. Unit-weight residuals can align every nonzero block, so the reciprocal map alone cannot create a cross-divisor saving.

## Open theorem

Prove a Gram or cancellation estimate for the *literal coupled* residuals after the boundary and smooth `A_d(r)` emitter are kept together.

## Reusable structure

```text
divisor band
  -> signed Boolean endpoint incidence
  -> complete-minus-missing boundary operator
  -> reciprocal occupancy collision Gram
  -> direct-sum sharp alignment obstruction
  -> literal physical coupling theorem required
```

## ROUND2\_CLUE

Build a nontrivial coupling map from the actual V46 Euler profile at divisor `d` to the emitter block at divisor `e`; only a theorem on that map can improve the block-diagonal direct-sum obstruction.
