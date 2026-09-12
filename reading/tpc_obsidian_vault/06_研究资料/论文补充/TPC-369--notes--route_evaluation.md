---
type: "source-reading"
source_path: "papers/tpc-369-third-origin-family-audit/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-369"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-369-third-origin-family-audit/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-369|TPC-369]] · [[00_开始阅读|首页]]

# TPC-369 route evaluation

## Strongest positive result

The TPC-367/TPC-368 beta=2 six-key long-window pattern is reproduced on all three origins of a third predeclared family. Beta=2 has no spectral failure at count 512 and no Schur failure in any of its 72 rows. An independently written reverse-shell implementation reproduces all 144 rows and the exact anchor metadata.

## Strongest obstruction

The count-1024 beta=2 spectral cap still fails at `Q=2048` and `Q=8192` under the all-plus law at every declared origin. There are six failures, with maximum `0.67410489800609708` against cap `0.64`. In addition, the first candidate exact anchor had zero geometry and had to be rejected by an exact, response-blind proof-anchor rule.

## Route decision

`TPC369_STATUS = NUMERICALLY_CERTIFIED_FINITE_THIRD_ORIGIN_FAMILY_AUDIT`.

`TPC369_BETA2_FAILURE_PATTERN = NUMERICALLY_CERTIFIED_FINITE_SCOPED`, `TPC369_INITIAL_ANCHOR_POSITIVITY = REFUTED_SCOPED`, `TPC369_REPAIRED_ANCHOR_RULE = PROVED_EXACT_FINITE`, `ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, and `FULL_GATE_B=OPEN`. The next minimal finite question is a count-2048 window; residue-phase localization remains the fallback if the pattern changes.

No official Route-A/Route-B evaluator is available in this checkout; local Bridge-B is fail-closed finite evidence only.

```text
ROUND2_CLUE = TEST_COUNT_2048_ORIGIN_PHASE_OR_RESIDUE_PHASE
```
