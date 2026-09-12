---
type: "source-reading"
source_path: "papers/tpc-395-c1-origin-cross-family-holdout/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-395"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-395-c1-origin-cross-family-holdout/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-395|TPC-395]] · [[00_开始阅读|首页]]

# TPC-395 derivation package

The finite kernel is the TPC-394 kernel with `Q=8192`, `H=66`, exponent one, and beta two:

`K_p(u,v)=p(p/Q)^2 H^2/(H^2+(u-v)^2)  (1_{p|u-v}-1/(p-1))1_{u!=v}1_{p not|u}1_{p not|v}`.

For each new origin, form `G(u)=sum_{p,v}K_p(u,v)^2` and signed matrices `M_l=sum_p s_l(p)K_p`. The eight 128-point blocks use the fixed `c=3` band. Four normalizations are applied exactly as in TPC-394: local diagonal, mean calibration scalar, current-origin scalar, and first-calibration frozen scalar.

Let `S(o)` be the masked spectral diagnostic. The new-family spread is `(max S-min S)/mean S`. Let `P` be the TPC-394 all-origin mean for the same law/normalization cell. The cross-family errors are `mean_calibration(S)/P-1` and `mean_holdout(S)/P-1`. The within-family transfer error is `mean_holdout(S)/mean_calibration(S)-1`.

Parent code and certificate hashes are checked before `P` is read. The baseline is therefore a frozen interface, not a current-response fit.

The exact anchor uses shell `{11,13}` at `Q=8` on `[5600001,5600014)` and checks the rational geometry and signed-matrix symmetry. All conclusions remain finite proxy statements; no source measure or arithmetic identity is introduced.
