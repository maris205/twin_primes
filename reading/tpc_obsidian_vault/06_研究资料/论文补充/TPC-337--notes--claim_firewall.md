---
type: "source-reading"
source_path: "papers/tpc-337-control-covariance-masked-response/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-337"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-337-control-covariance-masked-response/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-337|TPC-337]] · [[00_开始阅读|首页]]

# TPC-337 claim firewall

```text
TPC337_MEAN_CENTERED_OUTPUT_IDENTITY = PROVED_EXACT_FINITE_DECLARED_MODEL
TPC337_COVARIANCE_GRAM_PSD = PROVED_EXACT_FINITE_DECLARED_MODEL
TPC337_MASKED_CONTROL_REPLAY = NUMERICALLY_CERTIFIED_FINITE_6_ROWS_5_CONTROLS
TPC337_FULL_CENTERED_COVARIANCE_DOMINANCE = NUMERICALLY_CERTIFIED_FINITE_6_OF_6
TPC337_TWIN_BACKGROUND_COVARIANCE_SIGN = NUMERICALLY_CERTIFIED_FINITE_POSITIVE_6_OF_6
TPC337_ZERO_BACKGROUND_COVARIANCE_SIGN = NUMERICALLY_CERTIFIED_FINITE_NEGATIVE_6_OF_6
TPC337_SOURCE_SHARE_TRANSFER = REFUTED_SCOPED
TPC337_ARITHMETIC_ADVANCE = NO
TPC337_FIXED_POWER_CREDIT = 0
TPC337_SOURCE_UNIFORM_L2 = OPEN
TPC337_UNIFORM_MASKED_OPERATOR_BOUND = OPEN
TPC337_FULL_GATE_B = OPEN
TPC337_TWIN_PRIME_RESULT = NONE
```

`zero_support` denotes the complement of the source cross-support mask. It is not a zero vector, so its nonzero covariance response is expected.
