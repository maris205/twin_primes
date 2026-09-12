---
type: "source-reading"
source_path: "papers/tpc-369-third-origin-family-audit/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-369"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-369-third-origin-family-audit/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-369|TPC-369]] · [[00_开始阅读|首页]]

# TPC-369 claim firewall

```text
TPC369_ORIGIN_FAMILY_PROTOCOL = PROVED_EXACT_FINITE_PREDECLARED_RESPONSE_BLIND
TPC369_WEIGHTED_GEOMETRY_POSITIVITY = PROVED_EXACT_FINITE
TPC369_FINITE_REPLAY = NUMERICALLY_CERTIFIED_FINITE_144_ROWS
TPC369_THIRD_ORIGIN_FAMILY = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC369_BETA2_PHASE_AUDIT = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC369_BETA2_FAILURE_PATTERN = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC369_INITIAL_ANCHOR_POSITIVITY = REFUTED_SCOPED
TPC369_REPAIRED_ANCHOR_RULE = PROVED_EXACT_FINITE
TPC369_ORIGIN_UNIFORMITY = OPEN
TPC369_WINDOW_UNIFORMITY = OPEN
TPC369_BETA2_ASYMPTOTIC_REPAIR = OPEN
TPC369_NORMALIZATION_SOURCE_VALIDITY = MODELING_CHOICE_OPEN
TPC369_GROWING_OPERATOR_BOUND = OPEN
TPC369_SOURCE_UNIFORM_L2 = OPEN
TPC369_ARITHMETIC_ADVANCE = NO
TPC369_FIXED_POWER_CREDIT = 0
TPC369_FULL_GATE_B = OPEN
TPC369_TWIN_PRIME_RESULT = NONE
```

`REFUTED_SCOPED` applies only to the initial 13-point proof-anchor positivity statement. The replacement anchor is selected by a deterministic unsigned exact-geometry rule before main-panel response computation. No finite status here implies origin/window uniformity or asymptotic behavior. The official evaluator files named by the Session are absent; local Bridge-B is fail-closed evidence only.
