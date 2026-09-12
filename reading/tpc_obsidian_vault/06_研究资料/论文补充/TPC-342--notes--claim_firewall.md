---
type: "source-reading"
source_path: "papers/tpc-342-independent-fresh-holdout-reproduction/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-342"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-342-independent-fresh-holdout-reproduction/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-342|TPC-342]] · [[00_开始阅读|首页]]

# TPC-342 claim firewall

```text
TPC342_PROJECTION_IDENTITY = PROVED_EXACT_FINITE_DECLARED_MODEL
TPC342_INDEPENDENT_FRESH_REPLAY = NUMERICALLY_CERTIFIED_FINITE_108_RAW_RECORDS
TPC342_IN_SAMPLE_PROJECTION = NUMERICALLY_CERTIFIED_FINITE_3_ROWS
TPC342_HOLDOUT_OBSTRUCTION = NUMERICALLY_CERTIFIED_FINITE_27_RECORDS
TPC342_IN_SAMPLE_RETENTION = NUMERICAL_OBSERVATION_0.270_TO_0.296
TPC342_HOLDOUT_RETENTION = NUMERICAL_OBSERVATION_0.589_TO_0.943
TPC342_CONTROL_STABILITY = REFUTED_SCOPED
TPC342_ARITHMETIC_ADVANCE = NO
TPC342_FIXED_POWER_CREDIT = 0
TPC342_SOURCE_UNIFORM_L2 = OPEN
TPC342_UNIFORM_MASKED_OPERATOR_BOUND = OPEN
TPC342_FULL_GATE_B = OPEN
TPC342_TWIN_PRIME_RESULT = NONE
```

The projection is a finite modeling operation. It does not label nuisance directions as arithmetic noise and does not convert a holdout diagnostic into independence.
