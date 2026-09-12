---
type: "source-reading"
source_path: "papers/tpc-314-canonical-weight-law-audit/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-314"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-314-canonical-weight-law-audit/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-314|TPC-314]] · [[00_开始阅读|首页]]

# TPC-314 claim firewall

```text
PROVED_EXACT_FINITE = weighted Gram identity; positive normalizer; scale
                      invariance; atanh remainder bound; directed interval
                      arithmetic
NUMERICALLY_CERTIFIED_FINITE = 48 interval cases, 8 row-level order audits,
                               and independent exact replay
NUMERICAL_OBSERVATION = displayed decimal centers and table formatting
MODELING_CHOICE = three-law menu, source interval, shell anchors, trace-like
                  weighted normalizer, inherited Gram-minimum target
FRESHNESS_LIMIT = same locked TPC-268/TPC-312 engine and same physical panel
EXTERNAL_INDEPENDENCE = NONE
TARGET_LEAKAGE = the minimum label is selected from the Gram being weighted;
                 the all-positive vector is a control, not observed data
REFUTED_FINITE = any claim that the three laws have a common amplitude order
                 on this declared panel
OPEN = canonical law selection; genuinely fresh physical holdout; uniform
       growing weighted theorem; arithmetic L2; fixed-power credit; Gate B;
       twin-prime endpoint
```

The word “externally motivated” describes how the finite menu was chosen. It does not supply external independence or a causal interpretation.
