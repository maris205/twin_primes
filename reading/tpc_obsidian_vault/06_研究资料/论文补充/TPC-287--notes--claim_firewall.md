---
type: "source-reading"
source_path: "papers/tpc-287-prime-shell-cancellation-depth/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-287"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-287-prime-shell-cancellation-depth/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-287|TPC-287]] · [[00_开始阅读|首页]]

# TPC-287 claim firewall

The universal result is finite shell additivity and a conditional interval retention envelope. The 84-row shell-cardinality ladder is a declared finite experiment tied to the frozen TPC-268 source engine; it is not an asymptotic prime average.

```text
TPC287_SHELL_ADDITIVITY = PROVED_EXACT_FINITE_LINEARITY
TPC287_SHELL_LADDER = MODELING_CHOICE_CARDINALITIES_1_THROUGH_7
TPC287_ROWS = NUMERICALLY_CERTIFIED_FINITE_84
TPC287_COMPONENTS = NUMERICALLY_CERTIFIED_FINITE_336
TPC287_COMPONENT_SIGN_SEPARATION = NUMERICALLY_CERTIFIED_FINITE_336_OF_336
TPC287_MIXED_SIGN_ROWS = NUMERICALLY_CERTIFIED_FINITE_57_OF_84
TPC287_RETENTION_UPPER_LT_HALF = NUMERICALLY_CERTIFIED_FINITE_31_OF_84
TPC287_RETENTION_UPPER_LT_QUARTER = NUMERICALLY_CERTIFIED_FINITE_22_OF_84
TPC287_RETENTION_UPPER_LT_TENTH = NUMERICALLY_CERTIFIED_FINITE_8_OF_84
TPC287_LEAVE_ONE_OUT_FLIP_EVENTS = NUMERICALLY_CERTIFIED_FINITE_48
TPC287_LEAVE_ONE_OUT_ZERO_EVENTS = NUMERICALLY_CERTIFIED_FINITE_12
TPC287_GROWING_CANCELLATION_STABILITY = OPEN
TPC287_ARITHMETIC_L2 = OPEN_LITERAL_SOURCE
TPC287_FIXED_POWER_CREDIT = 0
TPC287_FULL_GATE_B = OPEN
TPC287_TWIN_PRIME_RESULT = NONE
```

The finite ladder closes the old atlas’s cardinality blind spot but does not claim that any observed retention threshold persists as $Q$ or $X$ grows.
