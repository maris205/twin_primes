---
type: "source-reading"
source_path: "papers/tpc-244-common-multiplier-sign-localization/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-244"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-244-common-multiplier-sign-localization/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-244|TPC-244]] · [[00_开始阅读|首页]]

# TPC-244 route evaluation

## Strongest positive result

The aggregate outer sign or unit phase of a common block multiplier is exactly invisible in the orthogonal coefficient covariance. Any nonorthogonal sign sensitivity is completely represented by a graph-cut polynomial, and after TPC-243 the variation between two common sign patterns is at most `2 epsilon ||W||||B||`.

## Strongest obstruction

The same-block main covariance necessarily carries `|C_h|^2`. Outer `C_h` sign cannot drive its cancellation. Only internal cancellation in `|C_h|`, cross-block leakage, or lane asymmetry can retain sign information.

## Open theorem

Prove the literal V59 phasewise primitive two-lane coefficient attachment, including common versus asymmetric multiplier placement, one synthesis map, and a payable coefficient-norm bound.

## Reusable structure

`common diagonal multiplier -> |C_h|^2 local covariance -> sign-cut edge polynomial -> hard-window leakage`.

## ROUND2\_CLUE

Analyze the within-block covariance `<w_h,b_h>` by a longitudinal/transverse decomposition before seeking any outer-sign cancellation.
