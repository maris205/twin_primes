---
type: "source-reading"
source_path: "papers/tpc-272-correlation-margin-budget-compiler/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-272"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-272-correlation-margin-budget-compiler/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-272|TPC-272]] · [[00_开始阅读|首页]]

# TPC-272 claim firewall

```text
CONDITIONAL_BUDGET_COMPILER = PROVED_CONDITIONAL
MARGIN_IDENTITY = PROVED_EXACT_FINITE
SIGN_ONLY_CONVERSE = PROVED_EXACT
FINITE_MARGIN_AUDIT = NUMERICALLY_CERTIFIED
SOURCE_LEVEL_MARGIN = OPEN_ASYMPTOTIC
SOURCE_LEVEL_SIGNED_SCALAR = OPEN_ASYMPTOTIC
FIXED_POWER_CREDIT = 0
ARITHMETIC_ADVANCE = NO
L2 = NONE
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```

The word \``margin'' denotes the finite correlation coordinate`\|C\_perp\|/R\`; it is not a probability of independence. The conditional compiler is not active until both source-level hypotheses are proved on the same clock. The finite phase sign is not promoted to a uniform sector or a lower correlation bound.
