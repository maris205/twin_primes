---
type: "source-reading"
source_path: "papers/tpc-409-c1-odd-complete-shell-height-ladder/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-409"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-409-c1-odd-complete-shell-height-ladder/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-409|TPC-409]] · [[00_开始阅读|首页]]

# TPC-409 derivation package

The complete-shell local identity is unchanged when the height changes: only the window `N=4H` and the kernel sums `S_0,S_1` change. Since the fixed `Q=65536` shell is odd, the exact profile has 2854 odd-index and 2855 even-index primes. The Cauchy–Schwarz step uses the actual odd count `P_-^2<=m_-V_-`; the factor cancels against `V_->=m_-a_min^2`. Thus the same finite `4/H` bound applies to every height in the declared ladder.
