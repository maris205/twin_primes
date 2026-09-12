---
type: "source-reading"
source_path: "papers/tpc-311-stratified-tau-holdout-replication/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-311"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-311-stratified-tau-holdout-replication/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-311|TPC-311]] · [[00_开始阅读|首页]]

# TPC-311 claim firewall

```text
PROVED_EXACT_FINITE = balanced factorial census; independent profile extrema;
                      positive ratio enclosure; equal-stratum interval map;
                      tau partition and fail-closed protocol
NUMERICALLY_REPRODUCED_FINITE = 54 strata; 6 primary/control blocks;
                                 22 sensitivity blocks; native reversal
NUMERICAL_OBSERVATION = calibration tau slice is LEFT and confirmation tau
                        slice is RIGHT at native radius; all-radius confirmation
                        is unresolved
REFUTED = strict replication of the declared class on the finite native split
MODELING_CHOICE = equal design-stratum weights; profile pooling within a cell;
                  native radius as primary; tau=.75 as confirmation slice
REGISTRATION_LIMIT = child protocol is declared but not externally timestamped
HOLDOUT_LIMIT = confirmation is a parameter slice in the same locked parent,
                not a fresh physical data source
INHERITED_LEAKAGE = TPC-302 physical-Gram-dependent target labels
OPEN = directed rounding; externally justified weights; fresh physical holdout;
       causal identification; profile-independent growing preference; uniform
       asymptotic budget; arithmetic L2; fixed-power credit; full Gate B;
       twin-prime conclusion
```

The finite `REFUTED` label does not say that the underlying twin-prime problem is false. It says only that this declared finite decision protocol does not replicate its strict orientation across the selected tau slices.
