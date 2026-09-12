---
type: "source-reading"
source_path: "papers/tpc-304-overlapping-shell-label-transport/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-304"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-304-overlapping-shell-label-transport/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-304|TPC-304]] · [[00_开始阅读|首页]]

# TPC-304 proof package

## Proposition 1: gauge-invariant transport identity

For any nonempty finite overlap `O` and binary labels `a,b`,

```text
rho = max_epsilon <a,epsilon b>/|O| = |<a,b>|/|O|
d   = min_epsilon mismatch(a,epsilon b)/|O| = (1-rho)/2.
```

**Proof.** The two possible inner products are `u` and `-u`, hence the maximal one is `|u|`. If `m` coordinates agree before alignment, the number of mismatches is `|O|-m`; after the better global sign it is the smaller of these two counts. For binary labels `u=(|O|-2d_min)`, which gives the stated identity. A global sign flip changes `u` only by a sign, leaving `|u|` and the minimized mismatch count unchanged. ∎

## Proposition 2: finite crosswalk statement

On the declared fixed-source spine, the exact finite crosswalk has mean aligned correlations `1/2,1/11,1/2` for `50->60`, `60->70`, and `70->90`. The middle transition is the unique minimum. The independently replayed TPC-303 census has budget descent counts `3,15,3` and same-prefix descent counts `0,9,0`, so the middle transition is also the unique maximum and supports every same-prefix descent.

This proposition is a finite certificate statement: it inherits the parent certificates and makes no asymptotic or causal inference.
