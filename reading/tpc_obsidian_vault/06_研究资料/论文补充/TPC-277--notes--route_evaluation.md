---
type: "source-reading"
source_path: "papers/tpc-277-four-packet-gain-floor/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-277"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-277-four-packet-gain-floor/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-277|TPC-277]] · [[00_开始阅读|首页]]

# Route evaluation

```text
ROUTE_A = NOT_APPLICABLE_TO_THIS_SOURCE_GAIN_GEOMETRY_AUDIT
ROUTE_B = YES_SCOPED_SOURCE_GAIN_FLOOR_AND_FINITE_ATTACK
MAXIMUM_CLAIM = PROVED_EXACT_UNIVERSAL_FOUR_PACKET_GAIN_FLOOR_PLUS_NUMERICALLY_CERTIFIED_SOURCE_SCAN
STRONGEST_POSITIVE = SHARP_R>=1/4_AND_CONDITIONAL_R>=1_PLUS_EIGHT_EXACT_SOURCE_ROWS
STRONGEST_OBSTRUCTION = GEOMETRY_ALONE_HAS_NO_POWER_GAIN; R>=101/100_FAILS_FINITE
OPEN_THEOREM = UNIFORM_SOURCE_LEVEL_SIGNED_GAIN_LOWER_BOUND
REUSABLE_STRUCTURE = D,G,E -> kappa -> inverse_gain -> endpoint_budget_input
ROUND2_CLUE = TEST_CROSS_SCALE_SIGNED_GAIN_STABILITY_AND_SHELL_SENSITIVITY
```

The Route-B verdict is scoped. The absent Session-named evaluator files are not replaced by an invented definition; the proof package, exact replay, independent checker, stress audit, and Bridge-B checker are the local fail-closed evidence.
