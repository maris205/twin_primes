---
type: "source-reading"
source_path: "papers/tpc-322-signed-projector-reassembly/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-322"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-322-signed-projector-reassembly/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-322|TPC-322]] · [[00_开始阅读|首页]]

# TPC-322 proof package

## Proposition 1 — direct-sum identity

For every (v), $$  \|A_\oplus v\|^2=\sum_p\|B_pv\|^2. $$

**Proof.** The summands are coordinates in an orthogonal direct sum. Expand the Hilbert norm. $square$

## Proposition 2 — signed projector identity

For every sign vector (e), (E\_e\^*E\_e=I), (P\_e=E\_eE\_e\^*) is an orthogonal projection, and $$  \|P_eA_\oplus\|_{\rm HS}^2=m^{-1}\|\sum_pe_pB_p\|_F^2. $$

**Proof.** The factors (m\^{-1/2}) and (e\_p\^2=1) give (E\_e\^\*E\_e=m\^{-1}\sum\_pI=I). Thus (P\_e) is an orthogonal projection. For each source basis vector (u\_t), $$ P_eA_\oplus u_t=E_e(m^{-1/2}C_eu_t). $$ The isometry (E\_e) preserves norms. Summing the squared column norms gives the identity. $square$

## Proposition 3 — cross-block Gram and contraction

Let (H\_{pq}=\langle B\_p,B\_q\rangle\_F). Then (H\succeq0), (D=\operatorname{tr}H\>0), and $$  \rho_e=e^THe/D,\qquad 0\leq\phi_e=\rho_e/m\leq1. $$

**Proof.** (H) is a Gram matrix in the Frobenius inner-product space, so it is PSD. The expansion of (C\_e) gives (\|C\_e\|\_F^2=e^THe). Finally, orthogonal projection contraction gives $\|P_eA_\oplus\|_{\rm HS}\leq\|A_\oplus\|_{\rm HS}$, proving the last inequality. $square$

## Proposition 4 — global sign gauge

For every (e), ( ho\_{-e}= ho\_e). Therefore fixing the first sign to +1 does not remove any distinct ratio.

**Proof.** (C\_{-e}=-C\_e), and the Frobenius norm is unchanged. $square$

## Proposition 5 — finite signed atlas

On the 24 declared literal rows, the dual accumulation paths and exhaustive search certify a sign with ( ho\_e\<1) and a sign with ( ho\_e\>1) in every row. The all-plus ratios are below one in 3 rows and above one in 21 rows; the index-alternating ratios are below one in 21 rows and above one in 3 rows.

These are finite numerical statements under the declared binary64 error guard. They do not assert a canonical sign law or a growing estimate. $square$

## Claim ceiling

```text
PROVED_EXACT_FINITE = projector, cross-block Gram, contraction, and gauge identities
NUMERICALLY_CERTIFIED_FINITE = 24 literal rows; dual paths; exhaustive signs
NUMERICAL_OBSERVATION = canonical-law counts and finite ratio ranges
REFUTED_FINITE_PANEL = all-plus and alternating universal laws
OPEN = growing signed reassembly, source-native arithmetic L2, fixed-power credit,
       full Gate B, and twin-prime endpoint
```
