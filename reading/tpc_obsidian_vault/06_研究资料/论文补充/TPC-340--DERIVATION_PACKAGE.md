---
type: "source-reading"
source_path: "papers/tpc-340-schur-frobenius-hybrid-envelope/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-340"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-340-schur-frobenius-hybrid-envelope/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-340|TPC-340]] · [[00_开始阅读|首页]]

# TPC-340 derivation package

For a finite vector `x` supported on `S`, TPC-339 gives

```text
||A x||^2 <= F(S)^2 ||x||^2,
F(S)^2 = ||A[:,S]||_F^2.                                  (1)
```

For a symmetric finite matrix define

```text
R = max_i sum_j |A(i,j)|.
```

Because `||A||_1=||A||_infty=R`, the standard induced-norm inequality gives

```text
||A||_2 <= sqrt(||A||_1 ||A||_infty) = R,
||A x||^2 <= R^2 ||x||^2.                                  (2)
```

Taking the smaller of the two valid right-hand sides yields the sign-free hybrid envelope

```text
||A x||^2 <= min(F(supp(x))^2,R^2) ||x||^2.                 (3)
```

The active branch is a diagnostic: it does not change the proof of (3). For nonzero `x`, the hybrid occupancy is the response gain divided by the hybrid gain and is at most one.

The exact anchor uses the symmetric matrix with every entry in absolute value one, `A=[[1,-1],[-1,1]]`, and `x=(1,1)`. Its response energy is zero, source norm is two, and `R^2=4`, explicitly satisfying (2).
