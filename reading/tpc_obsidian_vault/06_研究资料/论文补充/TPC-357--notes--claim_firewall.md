---
type: "source-reading"
source_path: "papers/tpc-357-operator-norm-scale-ladder/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-357"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-357-operator-norm-scale-ladder/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-357|TPC-357]] · [[00_开始阅读|首页]]

# TPC-357 claim firewall

| Claim                              | Status                                | Boundary                            |
|------------------------------------|---------------------------------------|-------------------------------------|
| Schur and Frobenius inequalities   | `PROVED_EXACT_FINITE`                 | finite real matrices                |
| 288-row operator replay            | `NUMERICALLY_CERTIFIED_FINITE`        | declared origins/counts/shells/laws |
| normalized Schur cap `<0.83`       | `NUMERICALLY_CERTIFIED_FINITE_SCOPED` | panel only                          |
| all-plus spectral cap `<0.64`      | `NUMERICALLY_CERTIFIED_FINITE_SCOPED` | 72 all-plus rows only               |
| monotone normalized spectral decay | `REFUTED_SCOPED_ON_DECLARED_LADDER`   | 15 finite upward transitions        |
| growing operator bound             | `OPEN`                                | no extrapolation                    |
| arithmetic advance                 | `NO`                                  | source absent                       |
| fixed-power credit                 | `0`                                   | unpaid                              |
| full Gate B                        | `OPEN`                                | official evaluator absent           |
| twin-prime result                  | `NONE`                                | unchanged                           |

The finite caps are not uniform estimates and are not used as such.
