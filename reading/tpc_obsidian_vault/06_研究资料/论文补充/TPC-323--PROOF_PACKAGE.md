---
type: "source-reading"
source_path: "papers/tpc-323-signed-profile-majorization/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-323"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-323-signed-profile-majorization/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-323|TPC-323]] · [[00_开始阅读|首页]]

# TPC-323 proof package

## Proposition 1 — direct/coherent trace decomposition

For every finite block family,

$$  \operatorname{tr}(G_{\rm direct})=\sum_p\|B_p\|_F^2,  \qquad  \operatorname{tr}(G_e)=\left\|\sum_p e_pB_p\right\|_F^2. $$

**Proof.** Expand the Frobenius norm of the coherent sum and use the definition of the direct-sum Gram. `square`

## Proposition 2 — amplitude/shape factorisation

If both traces are positive, then

$$  \rho_e=\frac{\operatorname{tr}(G_e)}{\operatorname{tr}(G_{\rm direct})}  \quad\text{and}\quad  \pi_e=\frac{\lambda(G_e)}{\operatorname{tr}(G_e)} $$

are well-defined separately. The matrix `G_e` is recovered spectrally from the pair `(rho_e, pi_e)` together with its eigenbasis, and `pi(cG)=pi(G)` for every `c>0`.

**Proof.** The first assertion is the trace decomposition. The spectral theorem gives `G_e=V diag(lambda(G_e)) V^T`; divide the eigenvalues by their positive sum to obtain the stated shape. Multiplication by `c` multiplies both numerator and denominator of each profile coordinate by `c`. `square`

## Proposition 3 — finite profile labels

For the declared binary64 computation, a profile pair is labelled by the signs of its interior cumulative differences. The producer uses a tolerance `10^(-10)` and an outward metric guard `10^(-12)`. The independent checker rebuilds the reverse/einsum path and verifies the stored metric values, interval containment, and labels.

This proposition is a statement about the finite certificate protocol. It is not a floating-point proof for unlisted rows.

## Claim ceiling

```text
PROVED_EXACT_FINITE = trace decomposition and positive-scalar profile invariance
NUMERICALLY_CERTIFIED_FINITE = 24-row law/profile census and all-plus 24/24 label
NUMERICAL_OBSERVATION = all-plus is unique among four named laws on this panel
REFUTED_FINITE_PANEL = no universal profile conclusion for the three alternatives
OPEN = fresh holdout, source-native arithmetic L2, growing reassembly, Gate B, twin primes
```
