---
type: "source-reading"
source_path: "papers/tpc-243-hard-window-near-isometry-bilinear-transfer/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-243"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-243-hard-window-near-isometry-bilinear-transfer/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-243|TPC-243]] · [[00_开始阅读|首页]]

# Route evaluation

## Route A

`N/A` for this paper. TPC-243 is a Bridge-B structural analysis and makes no Route-A claim.

## Route B

`STRUCTURAL_L1_ONLY`.

The paper strengthens the finite-window analytic bridge: the rectangular synthesis operator is close to the coefficient-space identity in operator norm, so complex signed bilinear information survives with an explicit error. The result does not create arithmetic cancellation and does not close any physical gate by itself.

## Strongest positive result

For every finite separated frequency set, a single explicit operator estimate gives both a two-sided hard-window near-isometry and signed bilinear transfer. At the V59 primitive-rational scale the error is

```text
(133/100+o(1)) x^(-67/200) log x.
```

## Strongest obstruction

The transfer error is multiplied by `||z||_2 ||w||_2`. The repository does not yet provide a literal physical attachment of both V59 polarized lanes to these coefficient vectors or a coefficient norm estimate that pays the remaining arithmetic losses.

## Open theorem

Identify the two literal polarized V59 coefficient lanes in one common primitive-rational synthesis map and determine whether their physical `C_h` multipliers are common, conjugate, or asymmetric. Then prove the norm or covariance estimate needed to convert structural transfer into arithmetic credit.

## Reusable structure

```text
geometric hard-window entry bound
  -> two-sided harmonic circular packing
  -> Hermitian Gram perturbation
  -> quadratic near-isometry + signed bilinear transfer
```

The structure is translation invariant in the integer interval and separates analytic transport from arithmetic coefficient control.

## ROUND2\_CLUE

`COMMON_MULTIPLIER_SIGN_AUDIT_FOR_LITERAL_C_H_IN_THE_TWO_POLARIZED_LANES`

This clue is narrow: audit whether a common physical multiplier contributes `|C_h|^2` to the selected cross term, which would erase the literal sign of `C_h`, before seeking cancellation from that sign.

## Recommendation

`CONTINUE_STRUCTURAL_ROUTE_B_WITHOUT_GATE_PROMOTION`.
