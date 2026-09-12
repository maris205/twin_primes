---
type: "source-reading"
source_path: "papers/tpc-290-adaptive-shell-weighting-obstruction/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-290"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-290-adaptive-shell-weighting-obstruction/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-290|TPC-290]] · [[00_开始阅读|首页]]

# TPC-290 claim firewall

```text
TPC290_WEIGHTED_IDENTITY = PROVED_EXACT_FINITE
TPC290_NONNEGATIVE_NO_DECAY = PROVED_EXACT_CONDITIONAL
TPC290_DIFFUSE_ACCUMULATION_BOUND = PROVED_EXACT_CONDITIONAL
TPC290_FULL_SUPPORT_POLICY_SCAN = NUMERICALLY_CERTIFIED_FINITE_54_OF_54_AMPLIFIED
TPC290_SPARSE_SIGN_FLIP_ESCAPE = NUMERICALLY_CERTIFIED_FINITE_3_PAIRS_ONE_ROW
TPC290_DROP_ONE_SCAN = NUMERICALLY_CERTIFIED_FINITE_18_OF_18_AMPLIFIED
TPC290_UNIFORM_NONNEGATIVE_NO_DECAY = REFUTED_FINITE_BY_SPARSE_SIGN_FLIP
TPC290_GROWING_WEIGHTED_THEOREM = OPEN
TPC290_SOURCE_NATIVE_L2 = OPEN_LITERAL_SOURCE
TPC290_FIXED_POWER_CREDIT = 0
TPC290_FULL_GATE_B = OPEN
TPC290_TWIN_PRIME_RESULT = NONE
TPC290_STATUS = PROVED_EXACT_NONNEGATIVE_WEIGHTED_GRAM_NO_DECAY_BOUND_PLUS_NUMERICALLY_CERTIFIED_FINITE_ADAPTIVE_WEIGHTING_OBSTRUCTION
```

`REFUTED_FINITE` refers only to the unrestricted statement over every nonnegative support on the declared finite grid. The positive-block theorem and the full-support policy scan remain valid within their stated scopes.
