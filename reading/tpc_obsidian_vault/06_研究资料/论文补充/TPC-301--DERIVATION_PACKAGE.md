---
type: "source-reading"
source_path: "papers/tpc-301-budget-gap-robustness-audit/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-301"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-301-budget-gap-robustness-audit/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-301|TPC-301]] · [[00_开始阅读|首页]]

# TPC-301 derivation package

Let S be one frozen shell, let A be the physical source-to-shell matrix, and let U\_k be the first k literal Mobius cutoff profiles. Write $$         V_k=A^T U_k,\qquad M_k=U_k^T U_k . $$ The finite source cost at relative RMS tolerance tau is $$  B_{k,\tau}(b)=  \min\{c^T M_kc:\|V_kc-b\|_2\leq \tau\|b\|_2\}.                 \tag{1} $$ Every target in this audit has entries in {-1,1}, so its target norm is also the square root of the shell cardinality.

## Theorem 1: tolerance nesting

For fixed k and 0 \< tau\_1 \<= tau\_2, the feasible set in (1) for tau\_1 is contained in the feasible set for tau\_2. Therefore $$  B_{k,\tau_1}(b)\geq B_{k,\tau_2}(b),                           \tag{2} $$ whenever both values are feasible.

## Theorem 2: target homogeneity

For alpha != 0, the substitution c mapsto alpha c gives $$  B_{k,\tau}(\alpha b)=\alpha^2 B_{k,\tau}(b).                    \tag{3} $$ The relative radius is essential: both the target and the allowed residual are multiplied by \|alpha\|.

## Theorem 3: threshold prefix nesting

Define r\_k(b)=min\_c \|\|V\_kc-b\|\|*2/\|\|b\|\|*2, and let k\_tau(b) be the first k with r\_k(b) \<= tau. Since range(V\_k) is contained in range(V*{k+1}), the sequence r\_k(b) is nonincreasing. Hence k*{tau\_2}(b) \<= k\_{tau\_1}(b) for tau\_1 \<= tau\_2.

## Theorem 4: common-prefix normalization invariance

Let N\_k \> 0 depend on the row and prefix but not on the target class. At a common prefix k, $$  \frac{B_{k,\tau}(b_w)/N_k}{B_{k,\tau}(b_+)/N_k}  =\frac{B_{k,\tau}(b_w)}{B_{k,\tau}(b_+)}.                     \tag{4} $$ Thus a weighted/positive gap measured in the same source space cannot be created or removed by changing the common source normalization.

The three audited choices are $$  N_\beta=\|\beta\|_2^2,\qquad  N_{\rm mean}=\frac{\operatorname{tr}(M_k)}{k},\qquad  N_{\rm first}=M_k[1,1]. $$

## Numerical protocol

For each row and tolerance, the first weighted-feasible prefix is selected. Both targets are then evaluated in that common prefix, in their own first feasible prefixes, and in the full available prefix. The finite audit uses 60-digit mpmath ridge solves and 180 bisection steps; the independent replay repeats the matrix construction and all frontier evaluations.
