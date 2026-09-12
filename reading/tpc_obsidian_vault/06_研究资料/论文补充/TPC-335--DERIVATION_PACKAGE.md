---
type: "source-reading"
source_path: "papers/tpc-335-twin-isolated-source-norm/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-335"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-335-twin-isolated-source-norm/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-335|TPC-335]] · [[00_开始阅读|首页]]

# TPC-335 derivation package

## 1. Mask construction

Let `C` range over the four TPC-334 classes and define `beta_C(t)=beta(t) 1_C(t)`. The classes are disjoint and exhaustive, so each coordinate belongs to one mask.

## 2. Exact norm identity

Because the supports are disjoint,

```text
||beta||_2^2 = sum_C sum_t beta_C(t)^2
             = sum_C ||beta_C||_2^2.
```

The same argument applies to any finite coordinate-weighted diagonal form, but this paper only claims the source Euclidean norm.

## 3. Amplification diagnostic

Let `f_T^norm` be the twin fraction of residual norm and `f_T^cross` the twin fraction of `<Lambda,b>`. The recorded ratio `A_T=f_T^norm/f_T^cross` measures whether the residual subtraction changes the relative visibility of the twin coordinates. It is descriptive and has no prescribed asymptotic meaning.
