---
type: "source-reading"
source_path: "papers/tpc-306-two-way-operator-target-interaction/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-306"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-306-two-way-operator-target-interaction/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-306|TPC-306]] · [[00_开始阅读|首页]]

# TPC-306 claim firewall

## PROVED\_EXACT\_FINITE

-   the four-cell log decomposition;
-   `m^2-i^2=d_Ld_R` and the strict dominance criterion;
-   invariance under independent positive scaling of the two operator rows.

## NUMERICALLY\_CERTIFIED\_FINITE

-   18 cases and 54 normalizer-level decomposition rows;
-   target-main dominance in 12/18 cases and interaction dominance in 6/18, with zero unresolved cases;
-   middle `Q=60->70`: target-main 5/6 and interaction 1/6;
-   all 3/3 inherited same-prefix cases are target-main dominant;
-   every target-main ratio `|i|/|m|` is below `0.88`, every interaction-dominant ratio is above `1.2`, and the middle same-prefix maximum is below `0.64`.

## MODELING\_CHOICE

The TPC-305 shell spine, shell-specific native off-overlap completion, log scale, positive normalizers, and the definition of target-main versus interaction.

## OPEN / NONE

The four cells do not identify a causal effect because the two rows use different physical operators and shell-specific target completions. A common ambient union-shell holdout is still open, as are uniform asymptotics, arithmetic `L2`, fixed-power credit, full Gate B, and a twin-prime conclusion.
