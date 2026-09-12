---
type: "source-reading"
source_path: "papers/tpc-350-fresh-growth-signed-incidence/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-350"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-350-fresh-growth-signed-incidence/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-350|TPC-350]] · [[00_开始阅读|首页]]

# TPC-350 derivation package

Let `I={o,...,o+M-1}` and let `D_I=A_I-T_I` be the literal physical-minus-ideal mask defect. For the ordered shell `p_0<...<p_(r-1)`, put `m=floor(r/2)` and

```text
beta_j = +1 (j<m), 0 (m<=j<r-m), -1 (j>=r-m).
```

For `h_(p,I)(t)=1_(p divides t)`, define `b_I=sum_j beta_j h_(p_j,I)`. The first and last blocks have the same size, so `sum beta_j=0`; the middle block has at most one entry.

Linearity gives

```text
D_I b_I = sum_j beta_j D_I h_(p_j,I).
```

Taking the Euclidean square and expanding the finite sum gives the exact prime-incidence Gram identity

```text
||D_I b_I||_2^2
 = sum_(j,k) beta_j beta_k
   <D_I h_(p_j,I), D_I h_(p_k,I)>.
```

When `b_I != 0`, `x_I=b_I/||b_I||_2` is a unit vector. Therefore

```text
||D_I||_(2->2) >= ||D_I x_I||_2
                   = ||D_I b_I||_2 / ||b_I||_2.
```

TPC-350 adds only a finite growth-series diagnostic. For each fixed `(o,Q,s,law)`, the four stored ratios are ordered by `M=256,512,1024,2048`; the endpoint log-two slope is

```text
[log_2(rho_2048)-log_2(rho_256)]/3.
```

This is a descriptive finite statistic. It is not a limit, a monotonicity theorem, or an arithmetic estimate.
