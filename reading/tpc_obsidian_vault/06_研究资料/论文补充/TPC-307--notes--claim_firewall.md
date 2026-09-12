---
type: "source-reading"
source_path: "papers/tpc-307-common-ambient-union-shell-holdout/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-307"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-307-common-ambient-union-shell-holdout/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-307|TPC-307]] · [[00_开始阅读|首页]]

# TPC-307 claim firewall

## PROVED\_EXACT\_FINITE

-   the common union-shell ambient row set and the `O,E_L,E_R` partition;
-   the directional overlap-only constrained frontier definition;
-   holdout separation, global-sign invariance, and nested-prefix feasibility;
-   the finite algebraic interval-classification implication, conditional on a valid enclosure.

## NUMERICALLY\_REPRODUCED\_FINITE / NUMERICAL\_OBSERVATION

-   18 cases, 36 directional fits, and 54 normalizer rows;
-   13 concordant, 3 discordant, and 2 unresolved budget/holdout classes;
-   all three discordances at `Q=70 -> 90`, exponent 1, across `tau=.25,.5,.75`.

The producer builds a vectorized double-precision literal matrix and solves a high-precision frontier on its decimalized entries. Relative padding is `1e-5`; the independent NumPy replay checks containment with a separate slack. This is not a formal directed-rounding certificate.

## MODELING\_CHOICE / INHERITED\_LEAKAGE

The native exclusive completion, fixed profile cutoff order, source window, and three normalizers are finite protocol choices. The target labels are inherited from TPC-302’s physical-Gram-dependent source-first construction. Thus this paper does not claim causal independence of target and operator.

## OPEN / NONE

Formal enclosure certification, completion-invariant preference, causal identification, uniform growing-budget asymptotics, arithmetic `L2`, fixed power credit, full Route-B Gate B, and a twin-prime conclusion remain open or none.
