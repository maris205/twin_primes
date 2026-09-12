---
type: "source-reading"
source_path: "papers/tpc-374-near-block-band-truncation/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-374"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-374-near-block-band-truncation/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-374|TPC-374]] · [[00_开始阅读|首页]]

# TPC-374 route evaluation

## Strongest positive result

The predeclared `B3` near-block band reproduces all six beta=2 full-window spectral-cap failures on the complete 18-row panel. On those rows it retains at least `0.99157117644491055` of the selected full-mode absolute Rayleigh mass, while the omitted distances four through seven contribute at most `0.0084288235550895561`.

## Strongest obstruction

This is a fixed finite panel and a truncation selected from a finite block partition. The band is not shown to be uniformly bounded as the window grows, and reproducing a data-dependent Rayleigh quotient does not establish operator causality. At `Q=512`, the beta=2 band spectral value is slightly larger than the full value on all three origins, so “truncation” is not a monotone repair principle.

## Open theorem

Prove or refute a bandwidth-stability statement for predeclared cutoffs on an independently enlarged panel, beginning with cutoffs below 3 and retaining the same normalization and cap definitions.

## Reusable structure

```text
full-window geometry -> fixed block mask -> band/complement identity
  -> full-mode Rayleigh retention -> independent reverse-shell replay
  -> adversarial certificate stress -> bandwidth-stability test
```

`ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, and `FULL_GATE_B=OPEN`.

```text
ROUND2_CLUE = TEST_BANDWIDTH_STABILITY
```
