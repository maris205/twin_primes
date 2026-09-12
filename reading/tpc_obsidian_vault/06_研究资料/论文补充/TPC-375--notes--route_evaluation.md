---
type: "source-reading"
source_path: "papers/tpc-375-bandwidth-stability-minimal-cutoff/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-375"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-375-bandwidth-stability-minimal-cutoff/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-375|TPC-375]] · [[00_开始阅读|首页]]

# TPC-375 route evaluation

## Strongest positive result

On the complete nine-row beta=2 panel, the first cutoff whose band has the parent’s six spectral failure keys is `c=1`. Cutoff zero has no failure; cutoffs one, two, and three all have exactly the six high-Q/all-plus keys.

## Strongest obstruction

The minimal-cutoff result is scoped to one fixed count-2048 panel and a finite cutoff list. It does not control the band operator uniformly, and the selected-mode retention is not an operator norm. The beta=2 `Q=512` rows remain below the spectral cap at every cutoff.

## Open theorem

Does the predeclared minimal cutoff `c=1` preserve the same failure support on a fresh origin family or an enlarged window under the same normalization?

## Reusable structure

```text
full normalization -> nested predeclared cutoffs
  -> failure-key first-hit census -> selected-mode tail profile
  -> independent reverse-shell replay -> bandwidth holdout
```

`ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, and `FULL_GATE_B=OPEN`.

```text
ROUND2_CLUE = TEST_BANDWIDTH_HOLDOUT
```
