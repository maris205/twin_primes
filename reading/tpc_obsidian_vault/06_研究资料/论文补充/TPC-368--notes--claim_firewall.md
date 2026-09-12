---
type: "source-reading"
source_path: "papers/tpc-368-predeclared-origin-replication/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-368"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-368-predeclared-origin-replication/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-368|TPC-368]] · [[00_开始阅读|首页]]

# TPC-368 claim firewall

```text
TPC368_ORIGIN_FAMILY_PROTOCOL = PROVED_EXACT_FINITE_PREDECLARED_RESPONSE_BLIND
TPC368_WEIGHTED_GEOMETRY_POSITIVITY = PROVED_EXACT_FINITE
TPC368_FINITE_REPLAY = NUMERICALLY_CERTIFIED_FINITE_144_ROWS
TPC368_SECOND_ORIGIN_FAMILY = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC368_BETA2_LONG_WINDOW_REPLICATION = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC368_BETA2_FAILURE_PATTERN = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC368_ORIGIN_UNIFORMITY = OPEN
TPC368_WINDOW_UNIFORMITY = OPEN
TPC368_BETA2_ASYMPTOTIC_REPAIR = OPEN
TPC368_NORMALIZATION_SOURCE_VALIDITY = MODELING_CHOICE_OPEN
TPC368_GROWING_OPERATOR_BOUND = OPEN
TPC368_SOURCE_UNIFORM_L2 = OPEN
TPC368_ARITHMETIC_ADVANCE = NO
TPC368_FIXED_POWER_CREDIT = 0
TPC368_FULL_GATE_B = OPEN
TPC368_TWIN_PRIME_RESULT = NONE
```

The finite replication status applies only to the declared grid, three origins, two counts, three shell anchors, exponent one, and four laws. `TPC368_BETA2_LONG_WINDOW_REPLICATION` does not mean a uniform or asymptotic beta=2 theorem. The official `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` files are absent in this checkout; local Bridge-B is fail-closed repository evidence only.
