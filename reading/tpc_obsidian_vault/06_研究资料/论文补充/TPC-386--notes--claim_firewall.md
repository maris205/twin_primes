---
type: "source-reading"
source_path: "papers/tpc-386-c1-count-holdout-bandwidth/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-386"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-386-c1-count-holdout-bandwidth/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-386|TPC-386]] · [[00_开始阅读|首页]]

# TPC-386 claim firewall

| label                                         | status                                |
|-----------------------------------------------|---------------------------------------|
| selection/count split/coordinate disjointness | `PROVED_EXACT_FINITE`                 |
| 160-row count holdout                         | `NUMERICALLY_CERTIFIED_FINITE`        |
| all-plus count transfer                       | `NUMERICALLY_CERTIFIED_FINITE_SCOPED` |
| inherited 0.64 cap transfer                   | `REFUTED_FINITE_SCOPED`               |
| count-uniformity and growing operator bound   | `OPEN`                                |
| source normalization validity                 | `MODELING_CHOICE_OPEN`                |
| arithmetic advance                            | `NO`                                  |
| fixed-power credit                            | `0`                                   |
| full Route-B gate                             | `OPEN`                                |
| twin-prime result                             | `NONE`                                |

The local Bridge-B checker is repository evidence only. The official evaluator files named by the Session are not present in this checkout.
