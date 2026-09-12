---
type: "source-reading"
source_path: "papers/tpc-410-c1-odd-complete-shell-height-replication/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-410"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-410-c1-odd-complete-shell-height-replication/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-410|TPC-410]] · [[00_开始阅读|首页]]

# TPC-410 route evaluation

This release extends the odd complete-shell proxy across four window heights. It does not identify synthetic signs with arithmetic source signs, transfer the proxy to the physical operator, establish a growing estimate, pay arithmetic `L2` or the `1/400` budget, or close Route A/B. Strongest status: `PROVED_EXACT_FINITE_ODD_COMPLETE_SHELL_HEIGHT_REPLICATION`.
