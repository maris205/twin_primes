---
type: "source-reading"
source_path: "papers/tpc-293-signed-shell-maxcut-atlas/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-293"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-293-signed-shell-maxcut-atlas/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-293|TPC-293]] · [[00_开始阅读|首页]]

# TPC-293 claim firewall

```text
TPC293_ALL_POSITIVE_MAXCUT = PROVED_EXACT_CONDITIONAL
TPC293_SIGNED_OBJECTIVE = PROVED_EXACT_FINITE
TPC293_SWITCHING_INVARIANCE = PROVED_EXACT_FINITE
TPC293_SIGNED_MAXCUT_ATLAS = NUMERICALLY_CERTIFIED_FINITE_18_ROWS
TPC293_EDGE_CENSUS = NUMERICALLY_CERTIFIED_FINITE_1380_EDGES
TPC293_EXCEPTIONAL_GAIN = NUMERICALLY_CERTIFIED_FINITE_PLUS_3_EDGES_ONE_ROW
TPC293_GROWING_SIGNED_GRAPH = OPEN
TPC293_MAGNITUDE_WEIGHTED_RAYLEIGH = OPEN
TPC293_SOURCE_NATIVE_L2 = OPEN_LITERAL_SOURCE
TPC293_FIXED_POWER_CREDIT = 0
TPC293_FULL_GATE_B = OPEN
TPC293_TWIN_PRIME_RESULT = NONE
TPC293_STATUS = PROVED_EXACT_ALL_POSITIVE_MAXCUT_PLUS_NUMERICALLY_CERTIFIED_FINITE_SIGNED_SHELL_FRUSTRATION_ATLAS
```

The signed max-cut value is an unweighted sign diagnostic. It must not be read as a bound for `||sum_i c_i g_i||` when the Gram magnitudes differ, and the finite exceptional row must not be promoted to a growing-shell claim. The Session-named Route-A/Route-B evaluator files are absent from this checkout; no official evaluator pass is claimed.
