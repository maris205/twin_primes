---
type: "source-reading"
source_path: "papers/tpc-310-cross-holdout-aggregation-order/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-310"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-310-cross-holdout-aggregation-order/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-310|TPC-310]] · [[00_开始阅读|首页]]

# TPC-310 claim firewall

```text
PROVED_EXACT_FINITE = selector enumeration; pooled independent-extrema rule;
                      positive arithmetic/geometric interval maps;
                      ratio-of-sums weighted-mean identity
NUMERICALLY_REPRODUCED_FINITE = 49 selectors; 147 aggregate observations;
                                 class census and full-selector reversal
NUMERICAL_OBSERVATION = pooled and geometric maps classify the full selector
                        RIGHT while equal-case arithmetic map classifies LEFT
REFUTED = universal aggregation-independent finite preference claim
MODELING_CHOICE = pooled MSE, equal-case arithmetic ratio, geometric ratio;
                  strict-majority budget anchor; nonempty subset family
INHERITED_LEAKAGE = TPC-302 physical-Gram-dependent target labels
OPEN = directed rounding; canonical weights; causal identification; profile-
       independent preference law; uniform asymptotic budget; arithmetic L2;
       fixed-power credit; full Gate B; twin-prime conclusion
```

The word `REFUTED` applies only to the declared universal finite claim that all three aggregation maps must have one common strict class on this atlas. It does not refute a future, separately justified weighting theorem.
