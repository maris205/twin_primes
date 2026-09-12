---
type: "source-reading"
source_path: "papers/tpc-280-leakage-aware-endpoint-compiler/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-280"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-280-leakage-aware-endpoint-compiler/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-280|TPC-280]] · [[00_开始阅读|首页]]

# TPC-280 derivation package

Let `X >= 1`, `D > 0`, and suppose

`D >= d X^a`, `d > 0`,

and

`G <= B X^(-gamma) D + ell X^(a-delta)`,

with nonnegative coefficients and exponents. Division by the source floor gives

`q=G/D <= B X^(-gamma) + (ell/d) X^(-delta)`.

Writing `kappa=min(gamma,delta)` and `C=B+ell/d`, monotonicity for `X>=1` gives `q <= C X^(-kappa)`. Reciprocal division gives the two-term and collapsed gain bounds whenever `G>0`; if the right side is zero, the hypotheses force `G=0`.

The preceding four-packet identity `m^2=(D/G)m_D^2` therefore yields

`m^2 >= m_D^2/[B X^(-gamma)+(ell/d)X^(-delta)]`.

If `m_D >= c X^(-eta_D-epsilon)`, the collapsed form has effective loss `eta_eff=max(0,eta_D-kappa/2)`. Under the inherited endpoint model, the strict target remains `sigma-eta_eff>1/400`.

Sharpness is formal but exact: choose `D=dX^a` and `G=B X^(-gamma)D+ell X^(a-delta)`. Then every inequality in the normalized two-term compiler is an equality. If `delta<gamma` and `ell>0`, the leakage term controls the asymptotic exponent.
