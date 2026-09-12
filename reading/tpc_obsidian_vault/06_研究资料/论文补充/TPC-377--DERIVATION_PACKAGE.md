---
type: "source-reading"
source_path: "papers/tpc-377-c1-window-scale-holdout/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-377"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-377-c1-window-scale-holdout/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-377|TPC-377]] · [[00_开始阅读|首页]]

# TPC-377 derivation package

## 1. Finite scale family

For an origin a, count N in (1024,1536,2048), and a shell anchor Q, use the finite kernel

K\_p(u,t) = p (p/Q)\^2 66^2/(66^2+(u-t)\^2) (1\_{p\|(u-t)} - 1/(p-1)) 1\_{u!=t}1\_{p not\|u}1\_{p not\|t}.

The all-plus matrix is A=sum\_p K\_p, and its geometry is G(u)=sum\_t sum\_p K\_p(u,t)\^2. Normalize by T(u,t)=A(u,t)/sqrt(G(u)G(t)).

## 2. Exact finite identities

The geometry is a finite sum of nonnegative rational squares. For the fixed block length 256, let b\_N(u)=floor((u-a)/256). The mask \|b\_N(u)-b\_N(t)\|\<=1 defines B\_1, and R\_1=T-B\_1 entrywise. Thus for any selected unit eigenvector v of T, v\^T B\_1 v + v\^T R\_1 v = v\^T T v.

For a fixed origin the three count windows are nested prefixes with the same left endpoint. This is an exact protocol relation, not a claim that the corresponding matrices are restrictions of one normalized operator.

## 3. Finite outcome

The completed certificate records the count-by-Q failure table, the row-level spectra and Schur values, and the selected-mode band/tail Rayleigh fractions. The certified finite comparison is \[\[0,3,3\],\[0,3,3\],\[0,3,3\]\], with rows ordered by N=(1024,1536,2048) and columns by Q=(512,2048,8192).

## 4. Claim ceiling

Even a complete match is only finite scoped evidence for this declared scale ladder. It does not prove origin uniformity, window-scale uniformity, cross-block causality, a growing operator bound, source-uniform arithmetic L2, a power saving, Route-B reassembly, or a twin-prime theorem.
