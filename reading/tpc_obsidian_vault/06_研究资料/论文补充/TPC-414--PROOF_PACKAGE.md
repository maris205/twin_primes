---
type: "source-reading"
source_path: "papers/tpc-414-c1-three-shell-pooled-extension/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-414"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-414-c1-three-shell-pooled-extension/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-414|TPC-414]] · [[00_开始阅读|首页]]

# TPC-414 proof package

Pool the complete shells with `Q=65536,131072,262144`, retaining `5709+10749+20390=36848` primes. For each prime use `a_i=p_i^3/[Q_i^2(p_i-1)]`, order the pool increasingly, and impose alternating CRT residues. At `H=66,N=264`, the even pooled cardinality gives `m_minus=m_plus=18424`. Since every prime exceeds `N`,

```text
G0=V_minus S0,  G1=V_minus S1+V_plus(S1-t1^2),  M=t1 P_minus.
```

Cauchy–Schwarz, `V_minus>=m_minus a_min^2`, `G1>=V_minus S1`, and `S0,S1>=H/4` imply `0<=z<=t1/(a_min sqrt(S0 S1))<=4/H`. This is one finite three-shell synthetic proxy entry, not a full operator or arithmetic theorem.
