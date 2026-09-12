---
type: "source-reading"
source_path: "papers/tpc-282-literal-source-attachment-audit/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-282"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-282-literal-source-attachment-audit/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-282|TPC-282]] · [[00_开始阅读|首页]]

# TPC-282 proof package

## Projection identity

For each declared block contrast `a` with denominator `d`, the projection coefficient is the block sum divided by `d`. Orthogonality of the three contrasts gives

```text
<P_3 w, P_3 g> = sum_a <a,w> <a,g>/d_a.
```

Consequently the recorded scalar is the exact decomposition

```text
C = <w,g> - <P_3 w,P_3 g> = <(I-P_3)w,(I-P_3)g>.
```

Here `g=A beta` and `S=(I-P_3)g`. The code uses interval arithmetic for the source weights and exact rational arithmetic for `g` and `S`.

## Finite source-lock proposition

For each of the six scales and two kernel exponents in the registered schedule, the certificate verifies `C<0` or `C>0`, `W>0`, `Y>0`, and `0<C^2/(WY)<1`. Therefore every registered row has a nonzero actual source attachment. This is a finite proposition about the frozen operator family.

## Scope firewall

No implication from twelve finite rows to a bound of the form `|C_X| >= c X^{-theta}` is made. In particular, the sign change and the small minimum of `rho^2` are evidence against silently treating finite attachment as a uniform positive margin.
