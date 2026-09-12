---
type: "source-reading"
source_path: "papers/tpc-417-c1-four-shell-finite-operator-bound/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-417"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-417-c1-four-shell-finite-operator-bound/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-417|TPC-417]] · [[00_开始阅读|首页]]

# Derivation package

For `N=4H`, the production divisibility condition gives `M_{0r}=P_minus T_r` and `M_{rs}=-A T_{r-s}` for interior `r,s`, where `A=P_plus-P_minus`. The exact diagonal energies are `D_0=V_minus S_0` and `D_r=V_minus S_r+V_plus(S_r-T_r^2)` for `r>=1`.

Writing the locally normalized matrix as `Z=[[0,q^T],[q,C]]`, `||q||^2<=4/(a_min^2 H)` follows from `S_r>=H/4`, `sum T_r^2<=S_0`, `P_minus^2<=m_minus V_minus`, and `V_minus>=m_minus a_min^2`. The interior row sum is at most `16|A|/V_minus`, because `D_r>=V_minus H/4` and the two-sided kernel sum is at most `4H`. The triangle inequality gives the stated full finite bound.
