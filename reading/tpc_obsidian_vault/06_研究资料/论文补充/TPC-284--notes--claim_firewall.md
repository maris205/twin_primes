---
type: "source-reading"
source_path: "papers/tpc-284-admissible-source-control-atlas/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-284"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-284-admissible-source-control-atlas/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-284|TPC-284]] · [[00_开始阅读|首页]]

# TPC-284 claim firewall

`NUMERICALLY_CERTIFIED_FINITE` refers to the exact finite row set and the hash-locked implementation named in the certificate. It does not mean that the six controls exhaust all literal source perturbations, nor that the row set is an initial segment of an asymptotic schedule.

The eight sign flips are a scoped obstruction to a finite sign-stability heuristic. They are not a counterexample to the twin-prime conjecture and do not negate the fact that all 72 tested rows remain nonzero.

```text
TPC284_CONTROL_ATLAS = NUMERICALLY_CERTIFIED_FINITE_72_ROWS
TPC284_SIGN_FLIP_OBSTRUCTION = NUMERICALLY_CERTIFIED_FINITE_8_FLIPS
TPC284_FULL_ADMISSIBLE_CLASS = OPEN
TPC284_ASYMPTOTIC_STABILITY = OPEN
TPC284_ARITHMETIC_L2 = OPEN_LITERAL_SOURCE
TPC284_FIXED_POWER_CREDIT = 0
TPC284_FULL_GATE_B = OPEN
TPC284_TWIN_PRIME_RESULT = NONE
```
