---
type: "source-reading"
source_path: "papers/tpc-79-anchor-direct-orphan-quotient/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-079"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-79-anchor-direct-orphan-quotient/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-079|TPC-079]] · [[00_开始阅读|首页]]

# TPC-79: Anchor-direct completion on the orphan quotient

This paper separates three finite-dimensional values that are often conflated:

-   the direct completion gauge;
-   its free quotient on target directions visible to anchor synthesis;
-   the hybrid infimal convolution that charges both anchor and direct coefficients.

The formulas assume that direct synthesis is surjective onto the stated target and that anchor/direct coefficient variables form a verified separable direct sum with additive cost. Coupled native variables need one joint synthesis norm and do not use the polar-intersection formula.

The main exact formulas are

```text
delta_orph(pi k)
  = max { <lambda,k> : lambda in B_D, S_A^* lambda = 0 },

h(k)
  = min_v [alpha(v) + delta(k-v)]
  = max { <lambda,k> : lambda in B_A intersect B_D }.
```

It proves:

-   `delta_orph <= h <= delta`;
-   a fixed-datum equality test using direct norming functionals;
-   an orphan norming functional as a no-improvement certificate;
-   global redundancy of the anchor channel iff `alpha(v) >= delta(v)` on the anchor range;
-   quantitative upper and lower certificate gaps.

The paper requires an actual synthesis map from anchor data into the same target as direct completion. Observation, trace, or four-corner data do not become subtractable target entries merely by sharing labels.

These are exact L0 convex-algebraic results that advance the L1 interface. They do not prove a fixed-shift arithmetic saving, parity breaking, or the twin-prime conjecture.

Build with:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
