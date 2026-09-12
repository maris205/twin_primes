---
type: "source-reading"
source_path: "papers/tpc-372-full-window-offblock-decomposition/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-372"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-372-full-window-offblock-decomposition/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-372|TPC-372]] · [[00_开始阅读|首页]]

# TPC-372 claim firewall

```text
TPC372_FULL_WINDOW_PROTOCOL = PROVED_EXACT_FINITE_INHERITED_RESPONSE_BLIND
TPC372_COMMON_NORMALIZATION = PROVED_EXACT_FINITE
TPC372_DECOMPOSITION_IDENTITY = NUMERICALLY_CERTIFIED_FINITE
TPC372_FULL_REPLAY = NUMERICALLY_CERTIFIED_FINITE_18_ROWS
TPC372_BETA2_FULL_FAILURE = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC372_BLOCK_DIAGONAL_PHASE = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC372_OFF_BLOCK_NECESSITY = NUMERICALLY_CERTIFIED_FINITE_SCOPED
TPC372_CROSS_BLOCK_CAUSALITY = OPEN
TPC372_ORIGIN_UNIFORMITY = OPEN
TPC372_WINDOW_UNIFORMITY = OPEN
TPC372_NORMALIZATION_SOURCE_VALIDITY = MODELING_CHOICE_OPEN
TPC372_GROWING_OPERATOR_BOUND = OPEN
TPC372_SOURCE_UNIFORM_L2 = OPEN
TPC372_ARITHMETIC_ADVANCE = NO
TPC372_FIXED_POWER_CREDIT = 0
TPC372_FULL_GATE_B = OPEN
TPC372_TWIN_PRIME_RESULT = NONE
```

`TPC372_OFF_BLOCK_NECESSITY` is the finite reverse-triangle statement: on each full beta=2 failure row, the off-block norm is at least the recorded positive lower bound needed to bridge the gap between the full and diagonal norms. It is not a causal or asymptotic attribution. Both components can remain below the cap while their sum exceeds it.

The official Session Route-A/Route-B evaluator files are absent. The local Bridge-B is fail-closed repository evidence only.
