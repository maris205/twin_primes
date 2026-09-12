---
type: "source-reading"
source_path: "papers/tpc-413-c1-pooled-origin-replication/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-413"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-413-c1-pooled-origin-replication/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-413|TPC-413]] · [[00_开始阅读|首页]]

# TPC-413 derivation package

If `o_s=r+sL` with `s=1,2,3`, then `o_s mod p_i=r mod p_i` for every pooled prime. The masks, energies, signs, and normalized values therefore agree exactly across representatives. Combining this CRT invariance with the TPC-412 height argument gives the same sharp and coarse bounds in all 12 rows.
