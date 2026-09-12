---
type: "source-reading"
source_path: "papers/tpc-282-literal-source-attachment-audit/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-282"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-282-literal-source-attachment-audit/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-282|TPC-282]] · [[00_开始阅读|首页]]

# TPC-282 derivation package

Let `P_3` be the declared three-contrast block-Haar projection, let `A` be the literal finite prime-shell matrix, and let `beta` be the locked source profile. Put

```text
S=(I-P_3)A beta,
w_perp=(I-P_3)w,
C=<w_perp,S>,
W=||w_perp||^2,
Y=||S||^2,
rho^2=C^2/(WY).
```

The implementation evaluates `C` and `W` by the same block-energy identity as the upstream source audit, preserving outward intervals. `Y` is evaluated from the exact rational matrix. If `C` is sign-separated and `W,Y>0`, then the row has a certified nonzero attachment. Cauchy–Schwarz gives `0<rho^2<=1`; the certificate checks the stronger strict upper separation for every registered row.

The calculation is a source identification audit, not an asymptotic theorem: the row set is finite and the interval constants depend on the declared cutoff, shell, height, and kernel exponent.
