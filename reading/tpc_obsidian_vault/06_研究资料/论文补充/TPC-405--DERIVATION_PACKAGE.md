---
type: "source-reading"
source_path: "papers/tpc-405-c1-local-normalization-scale-ladder/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-405"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-405-c1-local-normalization-scale-ladder/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-405|TPC-405]] · [[00_开始阅读|首页]]

# Derivation package

Use the TPC-404 identities G\_0=V\_-S\_0, G\_1=V\_-S\_1+V\_+(S\_1-t\_1\^2), and M=t\_1P\_-. Because S\_1-t\_1^2=sum\_{d=1}^{N-2}t\_d\^2\>=0, G\_1\>=V\_-S\_1. Cauchy–Schwarz gives P\_-\^2\<=mV\_-; since each selected amplitude is at least a\_min, V\_-\>=m a\_min\^2. Therefore

```text
z^2 = t_1^2 P_-^2/(G_0 G_1)
   <= t_1^2 m V_-/(V_-S_0 V_-S_1)
   <= t_1^2/(a_min^2 S_0 S_1).
```

For integer H\>=1, N\>=H+2, the terms d=1,…,H occur in both S\_0 and S\_1. Since t\_d=H^2/(H^2+d\^2)\>=1/2, both sums are at least H/4. Finally, for Q\<p, a\_p=(p/Q)\^2 p/(p-1)\>1. Taking square roots yields the bound.

This is an exact theorem for the declared selected-prime CRT proxy. The heights in the certificate are a finite audit of the theorem, not its proof.
