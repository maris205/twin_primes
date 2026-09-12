---
type: "source-reading"
source_path: "papers/tpc-338-growing-control-covariance-spectrum/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-338"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-338-growing-control-covariance-spectrum/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-338|TPC-338]] · [[00_开始阅读|首页]]

# TPC-338 proof and scope package

## Proposition 1 — nested finite covariance identity

Equation (1) holds separately for the five-control and nine-control sets.

**Proof.** Expand `y_(C,j)=ybar_(C,J)+z_(C,j,J)` and use `sum_(j in J) z_(C,j,J)=0`. `QED`.

## Proposition 2 — covariance spectrum is nonnegative

Every covariance Gram matrix `K_J` is positive semidefinite.

**Proof.** This is equation (2), a finite average of squared norms. `QED`.

## Finite certificate

On all six parent-locked windows, five-control centered fractions are `0.7850--0.8553` and nine-control centered fractions are `0.8772--0.8973`. The normalized covariance spectrum changes by `0.0264--0.0441` in `L1`, and the covariance matrix changes by `0.2179--0.2379` in relative Frobenius norm. The twin–zero covariance changes from negative in `6/6` five-control rows to positive in `6/6` nine-control rows. Twin/background stays positive and background/zero stays negative in both ensembles.

## Scope boundary

The result is a nested finite comparison. It does not prove convergence as the number of controls grows, a canonical sign law, a source-uniform `L2` bound, arithmetic cancellation, fixed-power credit, or a twin-prime result.
