---
type: "source-reading"
source_path: "papers/tpc-387-c1-count-ladder-renormalization/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-387"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-387-c1-count-ladder-renormalization/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-387|TPC-387]] · [[00_开始阅读|首页]]

# TPC-387 derivation package

For the finite kernel `K_p` and square-energy geometry `G` used in TPC-386, form the local or pooled normalized masked matrix `B_{N}` at each declared count. The pooled training scalar at `N=512` and `N=768` is the mean of `G` over the three calibration origins at that count. Its `N=1024` denominator is the log-count extrapolation of those two geometry scalars.

For each fixed tuple `(band mode, normalization, law, Q)`, let `S_512` and `S_768` be the means of the spectral diagnostic over calibration origins. The finite calibration slope is

$$  \alpha = \frac{\log(S_{768}/S_{512})}{\log(768/512)},  \qquad  \widehat S_{1024}=S_{768}(1024/768)^\alpha . $$

The holdout statistic is `S_1024 / \widehat S_1024`; its deviation from one is recorded before any interpretation. This is a two-point interpolation/ extrapolation device, not an asymptotic derivation. The exact `Q=8`, 13-point anchor proves only positive geometry and symmetry by rational arithmetic; all larger values are finite floating-point observations.
