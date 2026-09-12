---
type: "source-reading"
source_path: "papers/tpc-391-c1-recursive-horizon-localization/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-391"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-391-c1-recursive-horizon-localization/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-391|TPC-391]] · [[00_开始阅读|首页]]

# TPC-391 derivation package

## Finite kernel

For p in (Q,2Q\], H=66, and distinct admissible integers u,v, define

```text
K_p(u,v) = p (p/Q)^2 H^2/(H^2+(u-v)^2)
           (1_{p | u-v} - 1/(p-1)).
```

Terms with p \| u or p \| v are removed. The row geometry is G(u) = sum\_p sum\_v K\_p(u,v)\^2. A sign law ell gives M\_ell(u,v) = sum\_p s\_ell(p) K\_p(u,v).

## Readouts

The local-diagonal matrix is M\_ell(u,v)/(G(u)G(v))\^(1/2). The pooled scalar matrix divides by the calibration-origin mean geometry at the same calibration length; its terminal scalar is extrapolated from the 1024 to 1280 geometry slope. This scalar is a modeling choice and carries no source-valid theorem.

The fixed band retains block distance at most three. The full-relative band retains all block pairs. Spectral and Schur diagnostics are computed after masking.

## Trajectory algebra

For a cell let S\_N be the relevant origin mean. The frozen parent slope is alpha\_P, while

```text
alpha_L = log(S_1280/S_1024)/log(1280/1024).
```

For N in {1152,1280,1408,1536},

```text
P_N = S_1024 (N/1024)^alpha_P,
L_N = S_1024 (N/1024)^alpha_L.
```

For N \>= 1280, the staged parent expression is

```text
R_N = [S_1024 (1280/1024)^alpha_P] (N/1280)^alpha_P.
```

Since powers with the same exponent compose, R\_N = P\_N in exact real arithmetic. The implementation records the floating-point residual as a diagnostic and does not treat it as a theorem.

## Selection and disjointness

All five origins and all roles are fixed before response computation. The producer checks interval disjointness against the prior TPC releases through TPC-390. The rational anchor \[3400001,3400014) at Q=8 checks positive geometry and exact symmetry for all sign laws.

The finite output has 448 rows: (3 calibration origins x 4 lengths + 2 holdout origins x 1 length) x 2 bands x 2 Q x 4 laws x 2 normalizations.
