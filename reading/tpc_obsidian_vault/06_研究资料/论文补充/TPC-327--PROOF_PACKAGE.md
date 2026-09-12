---
type: "source-reading"
source_path: "papers/tpc-327-three-origin-scale-triangulation/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-327"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-327-three-origin-scale-triangulation/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-327|TPC-327]] · [[00_开始阅读|首页]]

# TPC-327 proof and scope package

## Exact finite statements

1.  The displayed blocks define finite matrices, so `G_0` and `G_e` are PSD; positive trace gives a descending probability profile.
2.  The four intervals at origin `20001` are strictly nested and disjoint from the two earlier ladders and the older source panels.
3.  The exact rational anchor is computed from the same literal formula and its numerator/denominator digest is recorded in the certificate.

## Certified finite readout

The producer and independent checker recompute all 32 rows. The new all-plus profile majorizes the direct profile on `32/32` rows. The alternating, mod-4, and half-split counts are respectively `21/11`, `26/6`, and `23/9` for `(majorizes/mixed)`, matching both parent certificates. The three-origin maximum ranges are

```text
TV     = 0.0007970083067065925 < 0.001
energy = 0.004551841150018276  < 0.005
```

These are `NUMERICALLY_CERTIFIED_FINITE` statements tied to canonical rows and independent replay. They are not asymptotic error terms.

## First missing theorem

No source-native Möbius/von-Mangoldt signed `L2` estimate is proved. Thus no fixed-power credit is paid, the full Gate-B condition remains open, and the twin-prime endpoint is not claimed. The three-origin triangulation is a finite robustness result only.
