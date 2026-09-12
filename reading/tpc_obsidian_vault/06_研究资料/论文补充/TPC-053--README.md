---
type: "source-reading"
source_path: "papers/tpc-53-literal-factor-dictionary/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-053"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-53-literal-factor-dictionary/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-053|TPC-053]] · [[00_开始阅读|首页]]

# TPC-53: Literal factor dictionary

This directory contains the source and final PDF for:

> *A Literal Factor Dictionary for Prime-Squarefree Orbit Packets: Exact Atomic Normalization and Certified Interior Overlap*

## Core result

For one explicitly declared representative four-factor direct left packet, the paper proves the exact coordinate dictionary left conditional in TPC-52:

-   the outer coefficient is the literal source coefficient;
-   the opposite-row logarithmic base weight is the coefficient-free `e=0` weight, while its fixed unary shape remains in both profiles;
-   the static mask remains literal;
-   direct residue amplitudes and all Mellin normalizations are tracked exactly;
-   the norm is the retained-label pre-terminal atomic norm.

A strict reachable-support point yields an explicit positive overlap on a fixed compact source-row-orbit subpacket. The subpacket has positive geometric density and zero positive polynomial endpoint cost, so its canonical Mellin actual direction has bounded condition number.

The paper also proves that positive geometric density need not imply positive actual energy coverage: an arbitrary bounded source factor, or unbalanced cofactor multiplicity, may concentrate all energy outside the compatible cell.

## Claim boundary

This is an L1 physical-interface theorem. It does not prove a coherent prime square, residual-grouping stability, native-Gram identification, a parity breakthrough, or a twin-prime result.

## Build

Run `pdflatex`, `bibtex`, and two further `pdflatex` passes in this directory.
