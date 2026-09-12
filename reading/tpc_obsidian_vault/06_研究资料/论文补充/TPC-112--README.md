---
type: "source-reading"
source_path: "papers/tpc-112-determinant-zero-compatibility-audit/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-112"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-112-determinant-zero-compatibility-audit/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-112|TPC-112]] · [[00_开始阅读|首页]]

# TPC-112: Determinant-Zero Compatibility Audit

This paper closes the bookkeeping part of the TPC-109–112 batch.

At the critical scales,

$$ \frac{|Z_X|^2}{D_X} \le X^{1/400-(2\eta_Z-\lambda_D)+o(1)}. $$

Therefore:

-   the determinant/zero-mode certificate passes when `lambda_D <= 2 eta_Z`;
-   equality passes with zero determinant reserve;
-   the independent physical condition is `Lambda_phys < 1/400`;
-   equality in the physical ledger is a stop;
-   determinant reserve cannot be spent as physical slack without a new literal intertwining theorem.

Current honest verdict: TPC-109–111 certify no exponent pair because they establish exact structural criteria but no growing lower bound for `D_X` and no growing upper bound for `Z_X`. The route remains open, not passed and not globally disproved.

## Reproduction

```powershell
python experiments/tpc112_audit.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Stable archival PDF:

`tpc-112-determinant-zero-compatibility-audit.pdf`

SHA-256:

`2162B79321CD0CDECA6848F3077CC575A721DA3A05A77163D7852AC54AC61EAD`

Release QA: 5 A4 pages, all fonts embedded, no Type 3 fonts, and all pages rendered and visually inspected.
