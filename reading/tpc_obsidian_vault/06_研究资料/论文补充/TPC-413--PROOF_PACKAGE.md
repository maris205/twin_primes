---
type: "source-reading"
source_path: "papers/tpc-413-c1-pooled-origin-replication/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-413"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-413-c1-pooled-origin-replication/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-413|TPC-413]] · [[00_开始阅读|首页]]

# TPC-413 proof package

Use the pooled complete shells `65536<p<=131072` and `131072<p<=262144`, with shell-local `a_i=p_i^3/[Q_i^2(p_i-1)]`, alternating CRT residues, and `H=16,32,66,128`, `N=4H`. For each CRT period `L`, use the three distinct representatives `o_s=r+sL`, `s=1,2,3`. Every representative has identical residues modulo every prime. Thus the exact local identities and the pooled counts `m_minus=m_plus=8229` are unchanged at all 12 rows:

```text
G0=V_minus S0,  G1=V_minus S1+V_plus(S1-t1^2),  M=t1 P_minus.
```

Cauchy–Schwarz, `V_minus>=m_minus a_min^2`, `G1>=V_minus S1`, and `S0,S1>=H/4` give `0<=z<=t1/(a_min sqrt(S0 S1))<=4/H`. The result is a finite origin-replication audit of one synthetic proxy entry, not a physical, arithmetic, full-operator, or twin-prime theorem.
