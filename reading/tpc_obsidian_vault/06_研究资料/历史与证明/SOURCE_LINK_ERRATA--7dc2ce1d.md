---
type: "source-reading"
source_path: "research/tpc-big-road/research-rounds/2026-09-09-physical-return-loop/SOURCE_LINK_ERRATA.md"
snapshot_date: "2026-09-12"
owner: "DOC-7dc2ce1dce8c8253"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/research/tpc-big-road/research-rounds/2026-09-09-physical-return-loop/SOURCE_LINK_ERRATA.md.txt)；可用外部编辑器核对。


[[00_开始阅读|首页]] · [[05_综合与进展/历史总结校注|历史与当前状态的区别]]

# Source-link erratum for the immutable raw archive

The complete reviewer responses are preserved verbatim. A local-link audit found one path typo in [the finite-attachment raw report](physical-loop-finite-attachment-audit--91a04d41.md). Its link to the prior attachment report omitted the directory prefix `research/tpc-big-road/`.

The correct target is [the prior physical-attachment report, line 97](../../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/DOC-7dc2ce1dce8c8253.md#src-c2833ef99c44825f). The mathematical corrections are already in [FINITE\_ATTACHMENT\_ERRATUM.md](FINITE_ATTACHMENT_ERRATUM--bc496b28.md); this additional erratum corrects navigation only.

A first naive Markdown-link regex also misclassified TeX function notation `[f](v)` as links and did not trim whitespace around one valid absolute target. The corrected document check excludes fenced code and TeX display/ inline regions, trims link-target whitespace, and reports this one preserved raw-link exception separately. It does not alter a source or proof to make a mathematical checker pass.
