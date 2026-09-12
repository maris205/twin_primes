---
type: "source-reading"
source_path: "papers/tpc-358-fresh-origin-spectral-holdout/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-358"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-358-fresh-origin-spectral-holdout/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-358|TPC-358]] · [[00_开始阅读|首页]]

# TPC-358 claim firewall

| Claim                               | Status                                | Boundary                           |
|-------------------------------------|---------------------------------------|------------------------------------|
| finite Schur/Frobenius inequalities | `PROVED_EXACT_FINITE`                 | finite matrices                    |
| fresh operator replay               | `NUMERICALLY_CERTIFIED_FINITE`        | 288 declared rows                  |
| parent-cap transfer                 | `NUMERICALLY_CERTIFIED_FINITE_SCOPED` | 3 fresh origins, tolerance `0.001` |
| normalized spectral cap             | `NUMERICALLY_CERTIFIED_FINITE_SCOPED` | all-plus rows only                 |
| monotone spectral decay             | `REFUTED_SCOPED_ON_DECLARED_LADDER`   | 13 finite increases                |
| growing operator bound              | `OPEN`                                | no extrapolation                   |
| arithmetic advance                  | `NO`                                  | source not used                    |
| fixed-power credit                  | `0`                                   | unpaid                             |
| full Gate B                         | `OPEN`                                | official evaluator absent          |
| twin-prime result                   | `NONE`                                | unchanged                          |
