---
type: "source-reading"
source_path: "papers/tpc-385-c1-bandwidth-origin-holdout/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-385"
generated: true
semantic_review: "not-certified-by-conversion"
---

> [!warning] 原文保留视图
> 此补充材料含未规范定界的TeX或不稳定Markdown标记。自动重排的文字核对未通过，因此下面逐字保留原文（仅统一换行），不猜补符号或修正数学结论。完整论文另有正常阅读层。

[原始Markdown字节附件](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-385-c1-bandwidth-origin-holdout/DERIVATION_PACKAGE.md.txt) · [[02_论文/TPC-385|论文入口]]

# 原始补充材料

```markdown
# TPC-385 derivation package

Let (I_o={o,ldots,o+511}), divided into four blocks of length 128. For
(Q<pleq2Q), define

\[
B_p(u,t)=p(p/Q)^2\frac{66^2}{66^2+(u-t)^2}
\left(1_{p\mid(u-t)}-\frac1{p-1}\right)
1_{p\nmid u}1_{p\nmid t}1_{u\ne t}.
\]

For each declared law (ell), let (M_{o,Q,ell}) be its signed shell sum
and let

\[
g_{o,Q}(u)=\sum_{t\in I_o}\sum_{Q<p\leq2Q}B_p(u,t)^2.
\]

The origin roles are fixed as (C=(2000001,2004011,2008021)) and
(H=(2012031,2016041)). For each (Q), the training-only pooled scalar is

\[
G_Q^{\rm train}=\frac1{3\cdot512}\sum_{o\in C}\sum_{u\in I_o}g_{o,Q}(u).
\]

For (c\in\{2,3\}), with block-distance mask (mathbf 1_c), the two
matrices reported at every calibration and holdout origin are

\[
A^{\rm loc}_{u,t}=M_{u,t}/\sqrt{g(u)g(t)},\qquad
A^{\rm train}_{u,t}=M_{u,t}/G_Q^{\rm train},\qquad
\mathbf 1_cA.
\]

For a role subset (R), the finite origin spread is

\[
\Delta_R=\frac{\max_{o\in R}s_o-\min_{o\in R}s_o}
{\lvert R\rvert^{-1}\sum_{o\in R}s_o}.
\]

For the four all-plus (Q=8192) cells, the locked TPC-384 phase value
(f_{c,\nu}) is compared to the holdout mean (h_{c,\nu}) by

\[
e_{c,\nu}=(h_{c,\nu}-f_{c,\nu})/f_{c,\nu}.
\]

The one-percent spread and forecast-error caps are declared before all
TPC-385 values are constructed. These are finite diagnostics, not a limiting
or source-attached operator estimate.

```
