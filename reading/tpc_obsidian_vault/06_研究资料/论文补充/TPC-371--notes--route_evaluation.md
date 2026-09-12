---
type: "source-reading"
source_path: "papers/tpc-371-block-phase-localization/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-371"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-371-block-phase-localization/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-371|TPC-371]] · [[00_开始阅读|首页]]

# TPC-371 route evaluation

## Strongest positive result

The complete predeclared block panel is finite, positive, independently replayed, and reproducible. Every beta=2 block-local row stays below both working envelopes, with maximum normalized spectral value `0.5536333251967529`.

## Strongest obstruction

The TPC-370 parent has six full-window beta=2 high-Q/all-plus spectral failures, but none of the 24 declared 256-point blocks has a beta=2 local failure. Thus the hypothesis that the parent failure is already contained in one independently normalized short block is refuted on this panel. This is not yet a cross-block causality theorem because the normalization changes.

## Open theorem

For the same full-window normalization, decompose the operator into its fixed block-diagonal and off-block parts and determine which component carries the finite high-Q signal. Any uniform or asymptotic version remains open.

## Reusable structure

```text
full-window failure -> fixed contiguous partition -> exhaustive local replay
  -> local-vs-global normalization warning -> off-block decomposition
```

`ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, and `FULL_GATE_B=OPEN`. The local Bridge-B is repository evidence only; official evaluator files are not present.

```text
ROUND2_CLUE = TEST_OFF_BLOCK_COHERENCE_DECOMPOSITION
```
