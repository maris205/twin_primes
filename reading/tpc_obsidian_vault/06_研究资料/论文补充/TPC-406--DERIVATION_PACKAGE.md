---
type: "source-reading"
source_path: "papers/tpc-406-c1-local-normalization-complete-shell-entry-boundary/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-406"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-406-c1-local-normalization-complete-shell-entry-boundary/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-406|TPC-406]] · [[00_开始阅读|首页]]

# Derivation package

TPC-405 already supplies the local masked-energy calculation. Selecting all 872 primes in the shell changes only the profile cardinality: `m=436`.

`G_0=V_-S_0`, `G_1=V_-S_1+V_+(S_1-t_1^2)`, and `M=t_1P_-`. Since `G_1>=V_-S_1`, `P_-^2<=mV_-`, and `V_->=m a_min^2`,

```text
z^2 <= t_1^2/(a_min^2 S_0 S_1).
```

The kernel terms `d=1,...,H` occur in both sums and satisfy `t_d>=1/2`, so `S_0,S_1>=H/4`. Shell membership gives `a_i>1`. Thus the complete-shell profile obeys `z<=4/(a_min H)<=4/H` exactly. The certificate checks five heights; it is evidence for the finite instantiation, not an asymptotic claim.
