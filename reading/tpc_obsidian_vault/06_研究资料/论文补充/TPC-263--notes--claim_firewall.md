---
type: "source-reading"
source_path: "papers/tpc-263-rank-three-physical-cross-gram/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-263"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-263-rank-three-physical-cross-gram/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-263|TPC-263]] · [[00_开始阅读|首页]]

# TPC-263 claim firewall

```text
PROVED = exact rank-three orthogonal projection and exact residual split
PROVED_SOURCE_BACKED = three `w` frame moments have arbitrary fixed-log
                       control; three `A_x beta` frame coefficients have
                       the frozen TPC-257 asymptotics; their product channel
                       is O(x^(5/3)/(log x)^(M+3))
NUMERICALLY_CERTIFIED = rational/Gaussian-rational projection audit and
                         exponent certificate
HEURISTIC = none required for the stated channel bound
CONJECTURE = none promoted
OPEN = orthogonal-complement cross-Gram C_perp; any fixed-power credit;
       arithmetic L2; full Gate B; twin-prime theorem
REFUTED_SCOPED = rank-three channel cannot be silently identified with the
                 full coupling
```

The `w` estimate is source-backed for each fixed `M,K`; constants are not claimed uniform as the hybrid cutoff or the requested logarithmic strength varies. The result gives zero fixed-power credit and leaves the strict `1/400` threshold unpaid.
