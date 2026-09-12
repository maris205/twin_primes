---
type: "source-reading"
source_path: "papers/tpc-308-adversarial-exclusive-completion-envelope/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-308"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-308-adversarial-exclusive-completion-envelope/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-308|TPC-308]] · [[00_开始阅读|首页]]

# TPC-308 claim firewall

## PROVED\_EXACT\_FINITE

-   Hamming-ball construction and candidate-count formula;
-   exact finite extrema for a fixed prediction;
-   radius monotonicity, radius-zero recovery, and global-sign invariance;
-   conditional soundness of the positive ratio interval classification.

## NUMERICALLY\_REPRODUCED\_FINITE / NUMERICAL\_OBSERVATION

-   18 locked shell-transition cells, three radii, 54 envelope observations;
-   candidate totals `36`, `186`, `480`;
-   agreement counts `13/3/2`, `11/2/5`, `10/1/7`;
-   discordance counts `3`, `2`, `1`, all localized to `70->90`, exponent 1.

The producer uses a vectorized float64 physical replay, decimalized entries, and high-precision frontier solves with padded enclosures. The independent checker uses a separate NumPy replay and slack. This is not directed rounding.

## MODELING\_CHOICE / INHERITED\_LEAKAGE

The radii, binary completion family, frozen coefficients, and fixed profile prefixes are finite protocol choices. Labels inherit TPC-302’s physical-Gram-dependent construction, so this paper does not identify an independent target law.

## OPEN / NONE

Completion invariance beyond the tested finite radii, causal identification, uniform growing-budget asymptotics, arithmetic `L2`, fixed-power credit, full Route-B Gate B, and a twin-prime conclusion remain open or none.
