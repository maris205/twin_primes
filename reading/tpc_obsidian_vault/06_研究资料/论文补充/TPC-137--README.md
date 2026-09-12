---
type: "source-reading"
source_path: "papers/tpc-137-prime-square-fixed-two-log-closure/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-137"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-137-prime-square-fixed-two-log-closure/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-137|TPC-137]] · [[00_开始阅读|首页]]

# TPC-137: Prime-square fixed-two logarithmic closure

Paper title:

> *Prime-Square Closure of the Frozen Determinant-Two Logarithmic Shadow*

For fixed primitive positive affine forms

$$ D(z)=d+sz,\qquad V(z)=u+az,\qquad su-ad=2, $$

and a fixed bounded periodic coefficient $\rho$, the paper proves

$$ \sum_{x/\omega(x)<z\le x} \frac{\mu(D(z))\mu(V(z))\rho(z)}{z} =o(\log\omega(x)). $$

The proof uses Tao’s proved fixed-affine logarithmic two-point theorem and the prime-square cutoff

$$ \mathsf S_P(m)=\prod_{p\le P}(1-\mathbf 1_{p^2\mid m}). $$

For fixed $P$, this is a finite signed CRT expansion. Its elementary tail has relative logarithmic mass $O(P^{-1})+o(1)$, so one first lets $x\to\infty$ with $P$ fixed and then lets $P\to\infty$. When a period $M$ is included, a retained pair $(k,\ell)$ uses a combined modulus dividing

$$ M\,\operatorname{lcm}(k,\ell)^2 \le M(P^\#)^2. $$

On each retained residue $z=r+Lt$, extracting the two fixed contents leaves the exact reduced determinant

$$ \frac{L(su-ad)}{c_Dc_V} =\frac{2L}{c_Dc_V}\ne0. $$

Thus neither the CRT split nor content extraction destroys the nonparallelity required by Tao’s theorem.

Status:

-   prime-square identity, CRT support, and tail: **L0**;
-   full-Möbius fixed-data logarithmic theorem: **frozen L1 arithmetic shadow**;
-   growing coefficients, physical weight/phase, ordinary all-prefix power saving, and positive L2: **not proved**.

Reproduce:

```powershell
python experiments/tpc137_prime_square_log_audit.py
python experiments/tpc137_prime_square_log_audit.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Archival PDF:

`tpc-137-prime-square-fixed-two-log-closure.pdf`
