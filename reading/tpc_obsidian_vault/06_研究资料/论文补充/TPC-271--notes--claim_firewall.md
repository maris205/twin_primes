---
type: "source-reading"
source_path: "papers/tpc-271-phase-radius-decoupling/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-271"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-271-phase-radius-decoupling/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-271|TPC-271]] · [[00_开始阅读|首页]]

# TPC-271 claim firewall

```text
LANE_FACTORIZATION = PROVED_EXACT_FINITE
PHASE_SIGN_CENSUS = NUMERICALLY_CERTIFIED_FINITE
PHASE_RADIUS_DECOUPLING = NUMERICALLY_CERTIFIED_FINITE
OUTPUT_LANE_SPIKE = NUMERICALLY_CERTIFIED_FINITE
SOURCE_LEVEL_SIGNED_PHASE = OPEN_ASYMPTOTIC
SOURCE_LEVEL_RADIUS = OPEN_ASYMPTOTIC
FIXED_POWER_CREDIT = 0
ARITHMETIC_ADVANCE = NO
L2 = NONE
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```

The word `decoupling` is a finite attribution statement: a constant signed phase label coexists with strongly varying normalized radius, and the largest dyadic spike is certified by the output norm lane. It is not a probabilistic independence assertion and it is not an asymptotic counterexample.
