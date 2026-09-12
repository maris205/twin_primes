---
type: "source-reading"
source_path: "papers/tpc-302-growing-shell-budget-gap-audit/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-302"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-302-growing-shell-budget-gap-audit/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-302|TPC-302]] · [[00_开始阅读|首页]]

# TPC-302 claim firewall

## PROVED\_EXACT\_FINITE

-   Gram PSD and quadratic-energy identity;
-   global-sign reduction and finite Gray enumeration;
-   tolerance/prefix feasible-set monotonicity;
-   common-prefix normalization cancellation.

## NUMERICALLY\_CERTIFIED\_FINITE

-   34 source-first physical sign minimizers;
-   612 frontier cases (three contexts, three tolerances, two targets);
-   common and full weighted/positive gaps above 10 at every tolerance;
-   common weighted budget above 1e-5 in 102 cases for each of three normalizers.

## NUMERICAL\_OBSERVATION

The gap minima and budget minima are finite summaries of the declared grid.

## MODELING\_CHOICE

TPC-288 growth/control rows, 17 literal cutoffs, equal-sign targets, relative RMS ladder (1/4,1/2,3/4), and the common-prefix protocol.

## OPEN / NONE

No uniform growing-shell budget theorem, arithmetic (L\^2), fixed-power credit, full Gate B, or twin-prime conclusion is claimed.
