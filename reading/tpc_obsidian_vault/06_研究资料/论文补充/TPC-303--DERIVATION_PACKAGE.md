---
type: "source-reading"
source_path: "papers/tpc-303-cardinality-monotonicity-obstruction/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-303"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-303-cardinality-monotonicity-obstruction/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-303|TPC-303]] · [[00_开始阅读|首页]]

# TPC-303 derivation package

For a positive budget sequence represented by outward intervals (B\_j\in[L_j,U_j]),

$$  U_{j+1}<L_j \Longrightarrow B_{j+1}<B_j,  \qquad L_{j+1}>U_j \Longrightarrow B_{j+1}>B_j. $$

These implications are exact order statements and require no probabilistic or asymptotic assumption. A single first implication refutes a claim that the budget is nondecreasing on the finite path. It does not refute a lower bound of the form (B\_j\geq C m\_j\^\alpha) at sufficiently large (m\_j).

TPC-302 supplies, for each row and tolerance, a common-prefix budget interval for each of

$$  N_\beta=\|\beta\|_2^2,\qquad  N_{\rm mean}=\operatorname{tr}(M_k)/k,\qquad  N_{\rm first}=M_k[1,1]. $$

On the fixed-source spine, compare adjacent (Q)-values. The shell cardinalities are (10,13,15,17), but the shells themselves move; hence the statement being tested is cardinality-only monotonicity, not monotonicity under set inclusion. A transition with equal (k) is labeled same-prefix and isolates the shell/target change from a change in profile dimension.
