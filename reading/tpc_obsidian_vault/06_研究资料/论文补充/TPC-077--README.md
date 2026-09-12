---
type: "source-reading"
source_path: "papers/tpc-77-sparse-incidence-completion-certificates/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-077"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-77-sparse-incidence-completion-certificates/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-077|TPC-077]] · [[00_开始阅读|首页]]

# TPC-77: sparse incidence completion certificates

TPC-77 decomposes the finite provenance-completion program of TPC-76 using the exact nonzero incidence of

$$ b=A_DF^0,\qquad C=A_DB_{\boldsymbol L}. $$

## Main results

-   Zero columns, immutable rows, and exactly solvable zero-cost blocks have distinct, rigorous deletion rules.
-   The bipartite graph of the exact nonzero entries of $C$ gives the component factorization $$ \Gamma(b,C) = \|b_{\rm fix}\|_1+ \sum_s\min_{\theta_s}\|b_s+C_s\theta_s\|_1 . $$
-   The dual factors over the same components: $$ \gamma_s = \max_{\|z_s\|_\infty\le1,\ C_s^*z_s=0} \operatorname{Re}\langle z_s,b_s\rangle . $$
-   A matched fill/charge pair gives certified componentwise lower and upper bounds whose gaps add exactly.
-   The ambient filter–site–analysis tripartite graph is a safe coarse decomposition; exact cancellations in $C=A_DB_{\boldsymbol L}$ may split it further.
-   A finite carrier census is specified by a reproducible manifest and certificate schema. No literal TPC-74 coefficient table is fabricated where the previous papers did not archive one.

These are L0 results with an L1 specialization to the complete fixed-$h_0$ carrier. They are not an asymptotic saving, a Perron decay theorem, or a parity/twin-prime result.

The archival PDF is `sparse-incidence-completion-certificates.pdf`.

## Build

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
