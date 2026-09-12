---
type: "source-reading"
source_path: "papers/tpc-278-cross-scale-gain-stability/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-278"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-278-cross-scale-gain-stability/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-278|TPC-278]] · [[00_开始阅读|首页]]

# TPC-278 claim firewall

```text
TPC278_LITERAL_SOURCE_REPLAY = NUMERICALLY_CERTIFIED_FINITE_ALL_12_ROWS
TPC278_NATURAL_CONTROLS = NUMERICALLY_CERTIFIED_FINITE_3_ROWS
TPC278_SHELL_CLOCK_FLIPS = NUMERICALLY_CERTIFIED_FINITE_4_FLIPS
TPC278_SIGNED_GAIN_STABILITY = REFUTED_SCOPED_FINITE
TPC278_SOURCE_LEVEL_UNIFORMITY = OPEN_ASYMPTOTIC
TPC278_FIXED_POWER_CREDIT = 0
TPC278_ARITHMETIC_ADVANCE = NO
TPC278_L2 = NONE
TPC278_FULL_GATE_B = OPEN
TPC278_FULL_GATE_B_STRICT_1_OVER_400 = UNPAID_GLOBAL
TPC278_TWIN_PRIME_RESULT = NONE
TPC278_STATUS = NUMERICALLY_CERTIFIED_FINITE_CROSS_SCALE_GAIN_STABILITY_OBSTRUCTION
TPC278_ROUND2_CLUE = FORMULATE_MINIMAL_SOURCE_LEVEL_COHERENCE_TO_GAIN_THEOREM
```

The words “flip” and “instability” refer only to the declared finite Q/H interface. They do not assert an asymptotic counterexample.
