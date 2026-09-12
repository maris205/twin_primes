---
type: "source-reading"
source_path: "papers/tpc-407-c1-complete-shell-q-scale-ladder/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-407"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-407-c1-complete-shell-q-scale-ladder/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-407|TPC-407]] · [[00_开始阅读|首页]]

# Derivation package

At fixed `H=66,N=264`, the TPC-406 local identities are independent of the shell scale. For each even complete shell, the alternating CRT residues make the two local energies

```text
G_0=V_-S_0,
G_1=V_-S_1+V_+(S_1-t_1^2),
```

and the adjacent coefficient is `M=t_1P_-`. The chain `G_1>=V_-S_1`, `P_-^2<=mV_-`, `V_->=m a_min^2`, and `S_0,S_1>=H/4` yields `z<=4/(a_min H)<=4/H` at every declared Q.

The Q ladder is a finite exact extension, with no asymptotic inference.
