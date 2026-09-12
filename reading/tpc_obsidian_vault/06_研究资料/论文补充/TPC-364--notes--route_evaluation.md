---
type: "source-reading"
source_path: "papers/tpc-364-shell-tilt-phase-diagram/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-364"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-364-shell-tilt-phase-diagram/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-364|TPC-364]] · [[00_开始阅读|首页]]

# TPC-364 route evaluation and proof boundary

## Positive finite result

The complete five-beta, four-law replay is numerically certified on the frozen TPC-361 panel. The beta=2 weighted congruence has no spectral-cap violation in 192 rows, while the inherited beta=0 normalization has 30. The weighted geometry remains spread over a substantial fraction of the literal shell (`effective fraction >= 0.669383...` on the recorded panel).

## Obstruction and open gates

The beta=2 result is selected from a finite menu on the same panel and is not an independent holdout. It does not establish that the normalization is source-valid, that the cap holds for growing Q or new origins, or that any arithmetic reassembly is possible. Source-uniform L2, a growing operator bound, fixed-power saving, official Route-A/Route-B evaluation, and the twin-prime endpoint remain open.

## Route decision

`TPC364_STATUS = NUMERICALLY_CERTIFIED_FINITE_SHELL_TILT_PHASE_DIAGRAM`. The next minimal test is a response-blind disjoint fresh-origin holdout for the predeclared beta=2 rule. A transfer failure should be recorded as an obstruction rather than repaired by refitting beta.
