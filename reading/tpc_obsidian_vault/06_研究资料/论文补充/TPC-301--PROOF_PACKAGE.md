---
type: "source-reading"
source_path: "papers/tpc-301-budget-gap-robustness-audit/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-301"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-301-budget-gap-robustness-audit/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-301|TPC-301]] · [[00_开始阅读|首页]]

# TPC-301 proof package

## Finite theorem

Assume M\_k is positive definite and define $$  {\cal F}_{k,\tau}(b)=  \{c:\|V_kc-b\|_2\leq\tau\|b\|_2\},\qquad  B_{k,\tau}(b)=\min_{c\in{\cal F}_{k,\tau}(b)}c^TM_kc . $$

### Proposition 1 (tolerance monotonicity)

If 0 \< tau\_1 \<= tau\_2, then F\_{k,tau\_1}(b) is contained in F\_{k,tau\_2}(b). Taking the minimum of the same positive quadratic form over nested sets gives B\_{k,tau\_1}(b) \>= B\_{k,tau\_2}(b).

### Proposition 2 (relative homogeneity)

For alpha != 0, c is in F\_{k,tau}(b) if and only if alpha c is in F\_{k,tau}(alpha b), because $$  \|V_k(\alpha c)-\alpha b\|_2  =|\alpha|\|V_kc-b\|_2  \leq\tau|\alpha|\|b\|_2. $$ The objective scales by alpha\^2; applying the equivalence in both directions proves B\_{k,tau}(alpha b)=alpha\^2 B\_{k,tau}(b).

### Proposition 3 (first feasible prefix)

The least-squares residual is the distance from b to range(V\_k). Prefix inclusion gives range(V\_k) contained in range(V\_l) for k \<= l, so r\_k(b) is nonincreasing. The set of indices satisfying r\_k(b) \<= tau therefore has a first element, and increasing tau can only move that first element to the left.

### Proposition 4 (normalization)

At a common prefix k, N\_k is a positive scalar independent of the target class. It cancels from the quotient of the two normalized budgets, which proves (4). The statement does not assert invariance when the two targets are assigned different prefixes.

## Numerical status

The proof package does not promote finite floating-point values to exact theorems. It labels the 324 frontier values, 54 common-prefix gap triples, and all aggregate floors as NUMERICALLY\_CERTIFIED\_FINITE because a separate source-first checker reconstructs them from the frozen parent engine and checks the published intervals. No asymptotic conclusion is attached.
