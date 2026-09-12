---
type: "source-reading"
source_path: "papers/tpc-269-growing-cutoff-profile-transfer/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-269"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-269-growing-cutoff-profile-transfer/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-269|TPC-269]] · [[00_开始阅读|首页]]

# TPC-269 derivation package

Author: Liang Wang, School of Mathematics and Statistics, Huazhong University of Science and Technology (HUST)

Let the finite operator and residual vectors be those of TPC-268, with the comparison cutoff replaced by

```text
z_N=floor(log N)
```

on the registered finite scales. Let A\_1 and A\_2 denote the same operator with the two normalized kernels K\_(H,1) and K\_(H,2). For a rational theta in \[0,1\],

```text
A_theta=(1-theta)A_1+theta A_2
g_theta=A_theta beta
             =(1-theta)g_1+theta g_2.
```

This is an exact finite affine identity because the shell, masks, centered residue factor and deleted diagonal are unchanged. It is the relevant bridge from a convex profile mixture to the projected residual scalar.

With P\_3 the three orthogonal block contrasts, define

```text
C_theta=<w,g_theta>
C_perp,theta=< (I-P_3)w, (I-P_3)g_theta >
R_theta^2=||(I-P_3)w||^2 ||(I-P_3)g_theta||^2
rho_theta^2=|C_perp,theta|^2/R_theta^2.
```

The numerator is affine before taking the absolute square, while the denominator is quadratic in theta. Therefore no monotonicity of rho\_theta is assumed. This explains why two nearby rational profile weights can be used as a hostile matched pair.

All beta values and kernel entries are rational on a finite row. The only transcendental inputs are the shifted prime logarithms and the Euler-product constant, enclosed by the TPC-268 outward interval protocol.
