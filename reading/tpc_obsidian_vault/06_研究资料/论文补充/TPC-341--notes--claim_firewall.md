---
type: "source-reading"
source_path: "papers/tpc-341-fresh-holdout-nuisance-orthogonalization/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-341"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-341-fresh-holdout-nuisance-orthogonalization/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-341|TPC-341]] · [[00_开始阅读|首页]]

# TPC-341 claim firewall

```text
TPC341_PROJECTION_IDENTITY = PROVED_EXACT_FINITE_DECLARED_MODEL
TPC341_FRESH_HOLDOUT_REPLAY = NUMERICALLY_CERTIFIED_FINITE_108_RAW_RECORDS
TPC341_IN_SAMPLE_PROJECTION = NUMERICALLY_CERTIFIED_FINITE_3_ROWS
TPC341_HOLDOUT_OBSTRUCTION = NUMERICALLY_CERTIFIED_FINITE_27_RECORDS
TPC341_IN_SAMPLE_RETENTION = NUMERICAL_OBSERVATION_0.201_TO_0.256
TPC341_HOLDOUT_RETENTION = NUMERICAL_OBSERVATION_0.444_TO_0.890
TPC341_CONTROL_STABILITY = REFUTED_SCOPED
TPC341_ARITHMETIC_ADVANCE = NO
TPC341_FIXED_POWER_CREDIT = 0
TPC341_SOURCE_UNIFORM_L2 = OPEN
TPC341_UNIFORM_MASKED_OPERATOR_BOUND = OPEN
TPC341_FULL_GATE_B = OPEN
TPC341_TWIN_PRIME_RESULT = NONE
```

The all-control projection and leave-one-control-out test are finite geometric diagnostics. They neither identify a canonical twin-prime component nor provide cancellation credit.
