---
type: "source-reading"
source_path: "papers/tpc-365-beta2-fresh-holdout/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-365"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-365-beta2-fresh-holdout/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-365|TPC-365]] · [[00_开始阅读|首页]]

# TPC-365 claim firewall

```text
TPC365_GEOMETRY_SELECTION = PROVED_EXACT_FINITE_RESPONSE_BLIND
TPC365_WEIGHTED_GEOMETRY_POSITIVITY = PROVED_EXACT_FINITE
TPC365_FINITE_REPLAY = NUMERICALLY_CERTIFIED_FINITE_384_ROWS
TPC365_BETA2_HOLDOUT = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC365_BETA2_CAP_TRANSFER = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC365_BETA2_ASYMPTOTIC_REPAIR = OPEN
TPC365_NORMALIZATION_SOURCE_VALIDITY = MODELING_CHOICE_OPEN
TPC365_GROWING_OPERATOR_BOUND = OPEN
TPC365_SOURCE_UNIFORM_L2 = OPEN
TPC365_ARITHMETIC_ADVANCE = NO
TPC365_FIXED_POWER_CREDIT = 0
TPC365_FULL_GATE_B = OPEN
TPC365_TWIN_PRIME_RESULT = NONE
```

The selection is response-blind but geometry-selected. It is not presented as an independent random holdout or as a uniform theorem. The official Session-named Route-A and Route-B evaluator files are absent from this checkout. The local Bridge-B checker is fail-closed finite reproducibility evidence only and is not an official evaluator pass.
