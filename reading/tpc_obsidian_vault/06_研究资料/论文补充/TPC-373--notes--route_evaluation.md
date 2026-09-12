---
type: "source-reading"
source_path: "papers/tpc-373-eigenmode-block-separation/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-373"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-373-eigenmode-block-separation/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-373|TPC-373]] · [[00_开始阅读|首页]]

# TPC-373 route evaluation

## Strongest positive result

The full matrix admits an auditable, common-normalization decomposition into eight fixed block-distance layers. All 18 rows select the minimum-eigenvalue mode and distance zero is the largest layer. On all six beta=2 parent failure rows every layer term is negative, while distances zero through three carry at least 99.157% of absolute Rayleigh mass.

## Strongest obstruction

The profile is finite and eigenmode-specific. It does not provide an operator-norm estimate for the near-block truncation, and therefore cannot yet show that the first four distances reproduce the parent failures or give a uniform decay law.

## Open theorem

Determine whether the predeclared band `sum_{d=0}^3 L_d` reproduces the six beta=2 full-window failures under the same normalization, before considering any growing-window statement.

## Reusable structure

```text
full-window normalization -> deterministic extremal mode
  -> fixed block-distance masks -> signed/absolute Rayleigh profile
  -> adversarial finite replay -> next layerwise test
```

`ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, and `FULL_GATE_B=OPEN`.

```text
ROUND2_CLUE = TEST_LAYERWISE_CROSS_BLOCK_DECAY
```
