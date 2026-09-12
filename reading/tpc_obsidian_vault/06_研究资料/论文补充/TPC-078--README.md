---
type: "source-reading"
source_path: "papers/tpc-78-exact-forest-completion-reduction/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-078"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-78-exact-forest-completion-reduction/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-078|TPC-078]] · [[00_开始阅读|首页]]

# TPC-78: Exact forest completion reduction

This paper specializes the sparse component program of TPC-77 to complex-scalar incidence matrices whose actual nonzero bipartite support is a forest.

Its exact results are:

-   variable leaves admit cost-preserving erasure;
-   forest support fixes matrix rank through maximum matching;
-   the pruned-core defect is `1 + sum_j (deg(j)-2)`;
-   one-complex-defect components have a closed primal-dual formula;
-   degree-two variable trees admit explicit phase transport;
-   column-dominant pivots admit exact Schur-type elimination;
-   higher-defect components reduce to a defect-dimensional complex SOCP;
-   balanced Hall motifs give additive and fractional dual-packing lower certificates.

The paper also records sharp stop rules: row leaves are not free, complex stars are geometric-median problems rather than coordinatewise median problems, cycle support does not determine rank, and general real-linear blocks require additional surjectivity/conformality hypotheses.

These are exact L0 algebraic results that advance the L1 interface/certificate layer. They do not establish a fixed-shift arithmetic saving, a parity-breaking estimate, or a twin-prime theorem.

Build with:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
