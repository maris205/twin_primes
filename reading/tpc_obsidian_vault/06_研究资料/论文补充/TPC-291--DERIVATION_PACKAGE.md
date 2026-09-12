---
type: "source-reading"
source_path: "papers/tpc-291-signed-schur-cancellation-atlas/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-291"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-291-signed-schur-cancellation-atlas/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-291|TPC-291]] · [[00_开始阅读|首页]]

# TPC-291 derivation package

## 1. Pair Gram normal form

For two nonzero physical component vectors `g_i,g_j`, write `d_i=||g_i||^2`, `d_j=||g_j||^2`, and `G=<g_i,g_j>`. Set `Gamma=G^2/(d_i d_j)`.

## 2. Projection calculation

For a real coefficient `rho`,

```text
||g_i-rho g_j||^2 = d_i - 2 rho G + rho^2 d_j.
```

Completing the square gives the unique minimizer `rho*=G/d_j` and

```text
min_rho ||g_i-rho g_j||^2 = d_i-G^2/d_j = d_i(1-Gamma).
```

Thus the normalized Schur residual is exactly `1-Gamma`. The scale-normalized coefficient cost satisfies `|rho*| sqrt(d_j/d_i)=sqrt(Gamma)`.

## 3. Sign cost

If `G>0`, then `rho*>0` and the minimizing expression `g_i-rho*g_j` uses opposite signs. If `G<0`, then `rho*<0`, so the same expression uses same-sign coefficients. The latter is precisely why an exceptional negative Gram pair can be accessed by nonnegative sparse support after a change of orientation, while a positive coherent block requires a signed subtraction.

## 4. Two-vector Rayleigh form

After normalizing by `sqrt(d_i),sqrt(d_j)`, the two-vector Gram matrix is `[[1,c],[c,1]]`, where `c=G/sqrt(d_i d_j)`. Its eigenvalues are `1+-|c|=1+-sqrt(Gamma)`. Consequently the best signed two-coordinate normalized energy is `1-sqrt(Gamma)`; this is a geometric diagnostic, not a full-shell estimate.

## 5. Route consequence

TPC-290 showed that diffuse positive weighting cannot cross an all-positive coherence wall. TPC-291 shows the complementary fact: high coherence creates low-residual signed pair directions, but the sign of that direction is a physical constraint. The remaining problem is to determine whether such pair directions can be assembled with the actual prime-shell signs and source arithmetic without losing the required normalization.
