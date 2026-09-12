---
type: "source-reading"
source_path: "papers/tpc-312-new-source-shell-separation-atlas/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-312"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-312-new-source-shell-separation-atlas/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-312|TPC-312]] · [[00_开始阅读|首页]]

# TPC-312 claim firewall

```text
PROVED_EXACT_FINITE = Gram identity; PSD; global-sign quotient; Gray coverage;
                      exact comparisons among the declared finite fractions
NUMERICALLY_CERTIFIED_FINITE = modular full rank on 8/8 rows
NUMERICAL_OBSERVATION = decimal table readability only
MODELING_CHOICE = source interval, H=66, Q anchors, exponent pair, first-sign
                  gauge, trace normalization
FRESHNESS_LIMIT = new rows in the same physical engine, not external data
LEAKAGE = minimum signs are generated from the physical Gram itself
OPEN = profile-budget outward rounding; external weight law; growing theorem;
       arithmetic L2; fixed-power credit; full Gate B; twin-prime endpoint
REFUTED = none in this release
```

The word “separation” describes the finite sign-energy normalization only. It does not mean that primes have been separated into twin pairs or that a prime gap estimate has been proved.
