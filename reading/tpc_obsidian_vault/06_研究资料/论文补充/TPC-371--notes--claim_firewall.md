---
type: "source-reading"
source_path: "papers/tpc-371-block-phase-localization/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-371"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-371-block-phase-localization/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-371|TPC-371]] · [[00_开始阅读|首页]]

# TPC-371 claim firewall

```text
TPC371_ORIGIN_FAMILY_PROTOCOL = PROVED_EXACT_FINITE_INHERITED_RESPONSE_BLIND
TPC371_BLOCK_PARTITION = PROVED_EXACT_FINITE_PREDECLARED
TPC371_WEIGHTED_GEOMETRY_POSITIVITY = PROVED_EXACT_FINITE
TPC371_BLOCK_LOCAL_REPLAY = NUMERICALLY_CERTIFIED_FINITE_576_ROWS
TPC371_BETA2_BLOCK_PHASE_AUDIT = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC371_BETA2_LOCAL_FAILURE = REFUTED_SCOPED
TPC371_CROSS_BLOCK_COHERENCE = OPEN
TPC371_ORIGIN_UNIFORMITY = OPEN
TPC371_WINDOW_UNIFORMITY = OPEN
TPC371_NORMALIZATION_SOURCE_VALIDITY = MODELING_CHOICE_OPEN
TPC371_GROWING_OPERATOR_BOUND = OPEN
TPC371_SOURCE_UNIFORM_L2 = OPEN
TPC371_ARITHMETIC_ADVANCE = NO
TPC371_FIXED_POWER_CREDIT = 0
TPC371_FULL_GATE_B = OPEN
TPC371_TWIN_PRIME_RESULT = NONE
```

`TPC371_BETA2_LOCAL_FAILURE = REFUTED_SCOPED` means that no declared independently normalized 256-point block crosses the working cap. It does not mean that a causal cross-block theorem has been proved. The block-local normalization differs from the full-window normalization, so the next paper must audit the latter explicitly.

The Session-named official Route-A/Route-B evaluator files are absent from this checkout. The repository Bridge-B is therefore fail-closed evidence, not an official route verdict.
