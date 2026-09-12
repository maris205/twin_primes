---
type: "source-reading"
source_path: "papers/tpc-388-c1-cross-family-slope-transfer/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-388"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-388-c1-cross-family-slope-transfer/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-388|TPC-388]] · [[00_开始阅读|首页]]

# TPC-388 derivation package

Let `B_N` be the same finite masked c=1 matrix used in TPC-387, with local diagonal or current-family calibration-pooled normalization. For each fixed cell `(mode, normalization, law, Q)`, write `S_N` for the mean band spectral diagnostic over the three calibration origins or the two endpoint holdouts.

TPC-387 supplies a locked parent slope `alpha_parent` for the corresponding cell. TPC-388 computes two finite forecasts from the current family’s `S_768`:

$$  \widehat S_{1024}^{\rm parent}=S_{768}(4/3)^{\alpha_{\rm parent}},  \qquad  \widehat S_{1024}^{\rm local}=S_{768}(4/3)^{\alpha_{\rm local}}, $$

where

$$  \alpha_{\rm local}=\frac{\log(S_{768}/S_{512})}{\log(768/512)}. $$

The primary transfer ratio is `S_1024 / \widehat S_1024^parent`; the local ratio is a predeclared control. Neither ratio is used to select a row or fit the parent slope. The pooled geometry scalar is extrapolated from current- family calibration geometry only, so the experiment does not silently assume that absolute normalization transfers between origin families.

At `Q=8`, rational arithmetic checks the positive square-energy geometry and symmetry on the 13-point anchor. All larger matrices and transfer ratios are finite floating-point observations.
