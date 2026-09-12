---
type: "source-reading"
source_path: "papers/tpc-321-cross-shell-profile-stability/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-321"
generated: true
semantic_review: "not-certified-by-conversion"
---

> [!warning] 原文保留视图
> 此补充材料含未规范定界的TeX或不稳定Markdown标记。自动重排的文字核对未通过，因此下面逐字保留原文（仅统一换行），不猜补符号或修正数学结论。完整论文另有正常阅读层。

[原始Markdown字节附件](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-321-cross-shell-profile-stability/PROOF_PACKAGE.md.txt) · [[02_论文/TPC-321|论文入口]]

# 原始补充材料

```markdown
# TPC-321 proof package and claim firewall

## Proposition 1 — exact normalization identity (PROVED)

If (G\succeq0), (operatorname{tr}(G)>0), and (c>0), then the descending
eigenvalue profile (p_j(G)=\lambda_j(G)/\operatorname{tr}(G)) satisfies
(p_j(cG)=p_j(G)) for every (j).  Consequently (D_{
m TV}), (D_{
m L}),
and (D_{
m int}) are unchanged by a common positive rescaling of either
matrix.

**Proof.** Positive rescaling multiplies every eigenvalue by (c) and the
trace by (c); cancellation gives the identity term by term.  Substitution
in the three definitions gives the metric invariance. \(square)

## Proposition 2 — finite profile separation (NUMERICALLY_CERTIFIED)

For the exact panel

\[
 X\in\{640,1280,2560\},\quad Q\in\{24,36,54,80\},\quad s\in\{1,2\},
\]

all 18 adjacent-(Q) comparisons satisfy

\[
 D_{\rm TV}>0.03,\qquad D_{\rm L}>0.02,
\]

with the producer's outward path intervals.  The independent reverse-order
replay reproduces the estimates and labels.  This proposition is a finite
certificate, not an asymptotic theorem.

## Proposition 3 — no common majorization direction on the panel
 (NUMERICAL OBSERVATION / REFUTED_FINITE_PANEL)

The same 18 comparisons contain three (p_Q\succeq p_{Q'}) labels, two
(p_{Q'}\succeq p_Q) labels, and thirteen mixed labels under
(\tau=10^{-8}).  Therefore the panel does not support a single universal
majorization direction.

## Explicit non-claims

The following remain `OPEN` or `NONE`:

* a uniform full-profile law as (X\to\infty) or as shell anchors vary;
* conversion of an unsigned PSD Gram profile into a signed prime sum;
* arithmetic cancellation or any power saving;
* fixed-power credit and full Gate B;
* the twin-prime conjecture.

The repository lacks the Session-named official evaluator files.  The local
Bridge-B checker is intentionally fail-closed and reports only the finite
certificate status above.

```
