---
type: "source-reading"
source_path: "papers/tpc-368-predeclared-origin-replication/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-368"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-368-predeclared-origin-replication/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-368|TPC-368]] · [[00_开始阅读|首页]]

# TPC-368 route evaluation

## Strongest positive result

The localized beta=2 failure pattern from TPC-367 is reproduced on all three origins of a second predeclared grid. Beta=2 has no spectral failure at count 512, and no Schur failure on any of its 72 rows. The reverse-shell implementation independently reproduces all 144 rows.

## Strongest obstruction

The count-1024 beta=2 spectral cap still fails at `Q=2048` and `Q=8192` under the all-plus law at every declared origin. There are six failures; the maximum is `0.674101905927736` against cap `0.64`. The replication rules out the narrow explanation that TPC-367’s pattern was unique to its first origin family, but it does not establish origin uniformity.

## Route decision

`TPC368_STATUS = NUMERICALLY_CERTIFIED_FINITE_PREDECLARED_ORIGIN_REPLICATION`.

`TPC368_BETA2_LONG_WINDOW_REPLICATION = NUMERICALLY_CERTIFIED_FINITE_SCOPED`, `ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, and `FULL_GATE_B=OPEN`. The next natural finite attack is a third predeclared origin family or a count-2048 window. If the pattern breaks, residue-phase localization is the minimal follow-up.

No official Route-A/Route-B evaluator is available in this checkout; local Bridge-B is fail-closed finite evidence only.

```text
ROUND2_CLUE = TEST_BETA2_THIRD_ORIGIN_FAMILY_OR_COUNT_2048
```
