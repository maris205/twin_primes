---
type: "source-reading"
source_path: "papers/tpc-416-c1-four-shell-odd-pooled-extension/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-416"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-416-c1-four-shell-odd-pooled-extension/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-416|TPC-416]] · [[00_开始阅读|首页]]

# TPC-416 proof package

Pool the complete shells `Q=65536,131072,262144,524288`, retaining `5709+10749+20390+38635=75483` primes. Use shell-local `a_i=p_i^3/[Q_i^2(p_i-1)]`, alternating CRT residues, `H=66`, and `N=264`. The odd pooled cardinality gives `m_minus=37741` and `m_plus=37742`. Every prime exceeds `N`, so

```text
G0=V_minus S0,  G1=V_minus S1+V_plus(S1-t1^2),  M=t1 P_minus.
```

Cauchy–Schwarz, `V_minus>=m_minus a_min^2`, `G1>=V_minus S1`, and `S0,S1>=H/4` imply `0<=z<=t1/(a_min sqrt(S0 S1))<=4/H`. This is one finite four-shell synthetic proxy entry with explicit odd parity, not a full operator or arithmetic theorem.
