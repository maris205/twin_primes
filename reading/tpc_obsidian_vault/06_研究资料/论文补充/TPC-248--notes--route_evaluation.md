---
type: "source-reading"
source_path: "papers/tpc-248-shared-lane-gram-ellipsoid-feasible-set/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-248"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-248-shared-lane-gram-ellipsoid-feasible-set/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-248|TPC-248]] · [[00_开始阅读|首页]]

# Route evaluation

Route A remains untouched. On Route B this is a structural `L1` advance: the actual TPC-247 shared-lane joint feasible set is now exact, including its rank defects and group-budget coupling. It is not arithmetic `L2`.

-   strongest positive result: exact shared-lane Gram ellipsoid and sphere/slack law;
-   strongest obstruction: marginal disks can overstate the joint set from a diagonal disk to a bidisk;
-   open theorem: sharp weighted aggregate radius on the literal grouped probes;
-   reusable structure: `V`, `G`, `G^dagger`, minimum preimage, orthogonal slack;
-   `ROUND2_CLUE`: `CONTRACT_WEIGHTED_PROBES_INSIDE_EACH_SHARED_OUTPUT_LANE_BEFORE_SUMMING_ACROSS_OUTPUT_BLOCKS`.
