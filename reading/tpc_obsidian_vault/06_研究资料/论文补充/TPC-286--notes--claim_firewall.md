---
type: "source-reading"
source_path: "papers/tpc-286-diagonal-deletion-attachment-ledger/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-286"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-286-diagonal-deletion-attachment-ledger/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-286|TPC-286]] · [[00_开始阅读|首页]]

# TPC-286 claim firewall

The exact diagonal split is a finite algebraic identity. The 72-row ledger is a replayable finite certificate tied to the TPC-284 controls and the frozen TPC-268 source model. Neither is an asymptotic result.

```text
TPC286_ATTACHMENT_SPLIT = PROVED_EXACT_LINEARITY
TPC286_COMPONENT_SIGN_LEDGER = NUMERICALLY_CERTIFIED_FINITE_72_ROWS
TPC286_FULL_VS_PHYSICAL_FLIPS = NUMERICALLY_CERTIFIED_FINITE_15_ROWS
TPC286_DIAGONAL_OPPOSITION = NUMERICALLY_CERTIFIED_FINITE_30_ROWS
TPC286_DIAGONAL_DOMINANCE = NUMERICALLY_CERTIFIED_FINITE_21_ROWS
TPC286_ASYMPTOTIC_DIAGONAL_DOMINANCE = OPEN
TPC286_SIGNED_FULL_SHELL_CANCELLATION = OPEN
TPC286_ARITHMETIC_L2 = OPEN_LITERAL_SOURCE
TPC286_FIXED_POWER_CREDIT = 0
TPC286_FULL_GATE_B = OPEN
TPC286_TWIN_PRIME_RESULT = NONE
```

In particular, finite diagonal dominance is not promoted to a uniform dominance theorem, and a sign flip is not called a counterexample to a different asymptotic statement.
