---
type: "source-reading"
source_path: "papers/tpc-384-c1-bandwidth-normalization-phase-diagram/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-384"
generated: true
semantic_review: "not-certified-by-conversion"
---

> [!warning] 原文保留视图
> 此补充材料含未规范定界的TeX或不稳定Markdown标记。自动重排的文字核对未通过，因此下面逐字保留原文（仅统一换行），不猜补符号或修正数学结论。完整论文另有正常阅读层。

[原始Markdown字节附件](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-384-c1-bandwidth-normalization-phase-diagram/DERIVATION_PACKAGE.md.txt) · [[02_论文/TPC-384|论文入口]]

# 原始补充材料

```markdown
# TPC-384 derivation package

Let (I_o={o,ldots,o+511}), partitioned into four consecutive blocks of
length 128. For a shell (S_Q={p:Q<ple 2Q, p {
m prime}}), define the
centered component

\[
B_p(u,t)=p(p/Q)^2\frac{66^2}{66^2+(u-t)^2}
\left(1_{p\mid(u-t)}-\frac1{p-1}\right)
1_{p\nmid u}1_{p\nmid t}1_{u\ne t}.
\]

For a declared law (ell), (M_{o,Q,ell}) is the signed sum of (B_p)
over the shell. The common row geometry is

\[
g_{o,Q}(u)=\sum_{t\in I_o}\sum_{p\in S_Q}B_p(u,t)^2.
\]

For (c\in\{0,1,2,3\}), let
\[
\mathbf 1_c(u,t)=1\{ |b(u)-b(t)|\le c\},
\]
where (b) is the block index. The two declared normalizations are

\[
A^{\rm loc}_{u,t}=M_{u,t}/\sqrt{g(u)g(t)},\qquad
A^{\rm pool}_{u,t}=M_{u,t}/G_Q,
\]

with (G_Q) the mean of all (g_{o,Q}(u)) over the three selected origins.
The reported band matrix is (mathbf 1_c A). Its spectral metric is the
largest absolute eigenvalue; Schur and Frobenius envelopes are recorded as
finite diagnostics.

For each law, Q, c, and normalization, the origin-spread statistic is

\[
\Delta=\frac{\max_o s_o-\min_o s_o}{\frac13\sum_o s_o},
\]

with the one-percent threshold fixed before readout. Every displayed phase
cell is therefore a finite consequence of the declared matrix construction,
not an asymptotic inference.

The q=8 anchor replaces floating-point arithmetic by rational arithmetic on
the 13-point interval. Positivity of (g) and exact symmetry of every law
matrix are checked before the numerical certificate is accepted.

```
