---
type: "source-reading"
source_path: "papers/tpc-301-budget-gap-robustness-audit/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-301"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-301-budget-gap-robustness-audit/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-301|TPC-301]] · [[00_开始阅读|首页]]

# TPC-301 claim firewall

## PROVED\_EXACT\_FINITE

-   tolerance nesting of the relative RMS feasible sets;
-   target homogeneity of the relative budget;
-   first-feasible-prefix monotonicity;
-   cancellation of any positive target-independent normalizer at a common prefix.

## NUMERICALLY\_CERTIFIED\_FINITE

-   324 finite frontier cases;
-   common-prefix gap above 10 in 18/18 rows for each of three tolerances;
-   common weighted budget above 3e-5 in 54/54 cases for all three normalizers;
-   36 full-prefix tolerance-monotonicity checks;
-   source-first independent replay and normal/optimized equality.

## NUMERICAL\_OBSERVATION

The displayed gap minima and maxima are finite numerical summaries, not asymptotic bounds.

## MODELING\_CHOICE

-   17 literal cutoffs;
-   inherited 18-row fixture;
-   relative RMS tolerances 1/4, 1/2, 3/4;
-   weighted and all-positive target classes;
-   common weighted-selected prefix;
-   \|\|beta\|\|\^2, tr(M\_k)/k, and first-profile energy.

## OPEN / NONE

No growing profile-budget theorem, arithmetic L2, fixed-power credit, full Gate B, or twin-prime result is claimed.
