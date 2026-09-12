---
type: "source-reading"
source_path: "papers/tpc-372-full-window-offblock-decomposition/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-372"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-372-full-window-offblock-decomposition/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-372|TPC-372]] · [[00_开始阅读|首页]]

# TPC-372 route evaluation

## Strongest positive result

The common-normalization identity `T=D+R` is reproduced on all 18 declared rows. For beta=2, every full-window failure row has a positive finite reverse-triangle lower bound for the off-block norm.

## Strongest obstruction

On beta=2, the full matrix has 6 spectral-cap failures, but the block-diagonal and off-block components each have zero spectral-cap failures. The finite excess is therefore a sum/coherence phenomenon for this common normalization, not a single-component cap crossing. This does not establish causality.

## Open theorem

Resolve the eigenmode/block-separation profile of the six full beta=2 failure rows, using the same full-window normalization and a predeclared block-pair partition.

## Reusable structure

```text
local normalized obstruction -> common full normalization -> D+R identity
  -> reverse-triangle necessity -> eigenmode phase audit
```

`ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, and `FULL_GATE_B=OPEN`.

```text
ROUND2_CLUE = TEST_EIGENMODE_BLOCK_SEPARATION
```
