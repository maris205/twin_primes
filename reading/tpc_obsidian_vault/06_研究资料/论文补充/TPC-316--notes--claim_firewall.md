---
type: "source-reading"
source_path: "papers/tpc-316-literal-arithmetic-l2-fresh-panel/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-316"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-316-literal-arithmetic-l2-fresh-panel/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-316|TPC-316]] · [[00_开始阅读|首页]]

# TPC-316 claim firewall

```text
PROVED_EXACT_FINITE = rational matrix definition;
                       signed-difference/residue HS identity;
                       finite Frobenius interface;
                       coordinate-column lower inequality
NUMERICALLY_CERTIFIED_FINITE = 16 rows and 80 probe columns;
                               8/8 normalized-HS rises;
                               16/16 exact upper/lower gap records
NUMERICAL_OBSERVATION = the two-scale rise is interpreted as a finite trend
REFUTED_SCOPED = normalized HS envelope is a decaying proxy on the declared
                 X=640 and X=1280 panels
HEURISTIC = none used in the certificate
CONJECTURE = none asserted
MODELING_CHOICE = H=66, Q anchors, exponents, two panels, five probes
OPEN = true operator-norm decay, growing arithmetic L2, canonical scaling,
       fixed-power credit, full Gate B, twin-prime endpoint
ARITHMETIC_ADVANCE = NO
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```

The finite rise is not a claim that the operator norm itself grows. The Frobenius bound is an upper envelope, and the coordinate probes are lower witnesses; the large gap is retained as evidence that the envelope is not sharp enough for route promotion.
