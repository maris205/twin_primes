---
type: "source-reading"
source_path: "papers/tpc-412-c1-pooled-complete-shell-extension/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-412"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-412-c1-pooled-complete-shell-extension/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-412|TPC-412]] · [[00_开始阅读|首页]]

# TPC-412 proof package

Pool the complete shells `65536<p<=131072` and `131072<p<=262144`, retaining `16458` primes. For each prime use `a_i=p_i^3/[Q_i^2(p_i-1)]`, where `Q_i` is its source shell, and impose alternating CRT residues in the pooled order. For each `H` in `{16,32,66,128}`, set `N=4H`. The pooled even cardinality gives `m_minus=m_plus=8229`; the exact local identities are

```text
G0=V_minus S0,  G1=V_minus S1+V_plus(S1-t1^2),  M=t1 P_minus.
```

Cauchy–Schwarz gives `P_minus^2<=m_minus V_minus`, while `V_minus>=m_minus a_min^2` and `G1>=V_minus S1`. Since `S0,S1>=H/4` and `a_i>1`,

```text
0 <= z <= t1/(a_min sqrt(S0 S1)) <= 4/(a_min H) <= 4/H.
```

The certificate and independent literal replay establish only this finite four-height synthetic proxy extension, not a full operator or arithmetic theorem.
