---
type: "source-reading"
source_path: "papers/tpc-246-weighted-covariance-disk-reassembly/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-246"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-246-weighted-covariance-disk-reassembly/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-246|TPC-246]] · [[00_开始阅读|首页]]

# TPC-246 route evaluation

## Strongest positive result

Independent exact local covariance disks reassemble into one exact weighted disk with center `sum lambda_h c_h` and radius `sum |lambda_h|r_h`. The TPC-243 leakage then yields the explicit robust margin `|C_0|-R_0-epsilon||W||||B||`.

## Strongest obstruction

If `|C_0|<=R_0`, the abstract product model realizes exact cancellation, so local moments and transverse energies alone cannot force a positive aggregate covariance. In the arithmetic source, block independence and the literal two-lane attachment are not yet available.

## Open theorem

Construct source-native coefficient lanes and block projections, prove the required local disks or a smaller actual feasible set, and establish a payable strict margin exceeding both transverse radius and hard-window leakage.

## Reusable structure

`local disks -> weighted exact disk -> zero/margin dichotomy -> window-inflated disk`.

## ROUND2\_CLUE

`SOURCE_NATIVE_WEIGHTED_LONGITUDINAL_DOMINANCE_BEYOND_TRANSVERSE_RADIUS_AND_WINDOW_LEAKAGE`.
