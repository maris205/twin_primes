---
type: "source-reading"
source_path: "papers/tpc-408-c1-complete-shell-q-scale-extension/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-408"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-408-c1-complete-shell-q-scale-extension/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-408|TPC-408]] · [[00_开始阅读|首页]]

# TPC-408 derivation package

The TPC-407 local diagonal identity does not use even shell cardinality in its energy calculation; evenness was only needed for the earlier notation `2m`. For a full shell with `r` primes, retain every prime and define `m_-=floor(r/2)` and `m_+=ceil(r/2)`. The CRT residues are still zero on even indices and `-N` on odd indices. Because every shell prime exceeds `N`, the masks in the window are exactly the same two classes as before.

The only changed proof line is the Cauchy–Schwarz parameter: `P_-^2 <= m_- V_-` and `V_- >= m_- a_min^2`; cancellation of `m_-` gives the same sharp bound. Thus odd complete shells are a genuine extension of the finite proxy domain, while the full operator and arithmetic gates remain untouched.
