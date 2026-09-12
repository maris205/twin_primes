---
type: "source-reading"
source_path: "papers/tpc-288-growing-shell-gram-obstruction/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-288"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-288-growing-shell-gram-obstruction/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-288|TPC-288]] · [[00_开始阅读|首页]]

# TPC-288 claim firewall

```text
PROVED_EXACT = finite operator/output/attachment additivity
PROVED_EXACT = Gram PSD and trace/all-ones energy identities
NUMERICALLY_CERTIFIED_FINITE = 34/34 Gram full-rank rows
NUMERICALLY_CERTIFIED_FINITE = 6/6 selected aggregate active matrices full rank
NUMERICALLY_CERTIFIED_FINITE = 13 scalar-energy mismatch rows
NUMERICALLY_CERTIFIED_FINITE = maximum shell cardinality 17
NUMERICAL_OBSERVATION = none needed for the core obstruction; decimals are display only
MODELING_CHOICE = declared growth path and source-control grid
OPEN = uniform growing-shell Gram bound
OPEN = literal source arithmetic L2
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```

The phrase “positive spectrum” means the finite output Gram matrices are positive definite after the exact PSD identity and modular full-rank witness. It does not mean the physical aggregate operator has a favorable condition number, a small norm, or an asymptotic saving. The six operator rank rows are selected witnesses, not a theorem for every shell.

The scalar retention upper bound is an interval-certified upper bound for a finite scalar quotient. Its coexistence with `R_E>1` blocks a specific scalar-to-energy promotion. It does not refute all possible collective prime-shell estimates.
