---
type: "source-reading"
source_path: "papers/tpc-403-c1-crt-origin-proxy-obstruction/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-403"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-403-c1-crt-origin-proxy-obstruction/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-403|TPC-403]] · [[00_开始阅读|首页]]

# Route evaluation

The exact CRT construction is a scoped finite analytic obstruction for the TPC proxy. The official Route-A and Route-B evaluator files are absent from the checkout. The raw coefficient obstruction does not pay a normalized operator bound, arithmetic `L2`, fixed-power saving, or Route-B reassembly. The next clue is `TEST_C1_CRT_PROXY_NORMALIZATION_BOUNDARY`.
