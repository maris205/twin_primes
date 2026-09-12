---
type: "source-reading"
source_path: "papers/tpc-222-four-packet-cross-term-obstruction/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-222"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-222-four-packet-cross-term-obstruction/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-222|TPC-222]] · [[00_开始阅读|首页]]

# TPC-222 proof package

## Theorem 1: packet Gram positivity

For vectors `V_0,...,V_3` in a complex Hilbert space, `G_(j,l)=<V_j,V_l>` is Hermitian positive semidefinite and `||sum_j c_jV_j||^2=c^*Gc`.

## Theorem 2: four-point polarization

For all `x,y`,

```text
<x,y> = 1/4 sum_(r=0)^3 i^(-r)||x+i^r y||^2.
```

This is an exact identity, not an estimate.

## Theorem 3: trace envelope and scoped non-identifiability

`0<=c^*Gc<=tr(G)||c||^2`. The upper endpoint is attained by a rank-one aligned Gram. The two exact fixtures `s^+` and `s^-` have identical diagonal/trace but target energies `16` and `0`; hence diagonal/trace information alone cannot certify signed reassembly.

All arithmetic in the certificate is exact Gaussian-rational arithmetic. No claim about the growing prime shell is made.
