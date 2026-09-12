---
type: "source-reading"
source_path: "papers/tpc-337-control-covariance-masked-response/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-337"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-337-control-covariance-masked-response/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-337|TPC-337]] · [[00_开始阅读|首页]]

# TPC-337 derivation package

Let `P_1,...,P_m` be the five declared coordinate bijections and let `y_(C,j)=A P_j beta_C`, where `A` is the fixed all-plus matrix. Define

```text
ybar_C = (1/m) sum_j y_(C,j),
z_(C,j) = y_(C,j)-ybar_C.
```

Then `sum_j z_(C,j)=0`. Expanding a finite square gives

```text
(1/m) sum_j ||y_(C,j)||^2
  = ||ybar_C||^2 + (1/m) sum_j ||z_(C,j)||^2.                 (1)
```

For two classes `C,D`, the same bilinear expansion gives

```text
(1/m) sum_j <y_(C,j),y_(D,j)>
  = <ybar_C,ybar_D>
    + (1/m) sum_j <z_(C,j),z_(D,j)>.                         (2)
```

Summing (1) over classes and applying it to `y_j=sum_C y_(C,j)` yields

```text
mean_j ||y_j||^2 = ||sum_C ybar_C||^2
                 + mean_j ||sum_C z_(C,j)||^2.               (3)
```

The matrix `K=(K_CD)` in (2) is a Gram matrix: for arbitrary real numbers `a_C`,

```text
a^T K a = mean_j ||sum_C a_C z_(C,j)||^2 >= 0.              (4)
```

Thus positive semidefiniteness is a theorem of the finite declared model, not a numerical conjecture. The observed negative off-diagonal entries are compatible with (4); they describe anti-alignment between different centered class orbits.

The exact rational anchor in the certificate uses two controls and two class orbits. Its average cross term is `0`, its coherent cross term is `1/2`, and its centered cross term is `-1/2`, verifying (2) exactly.
