---
type: "source-reading"
source_path: "papers/tpc-404-c1-local-normalization-boundary/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-404"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-404-c1-local-normalization-boundary/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-404|TPC-404]] · [[00_开始阅读|首页]]

# Derivation package

Let `a_p=p^3/[Q^2(p-1)]` be the TPC-403 coefficients, with even-index primes positive and odd-index primes negative. The CRT masks give `p|o` for positive primes and `p∤o,o+1` for negative primes. At `o`, each positive row is deleted and each negative row contributes the full off-diagonal energy `S_0`; hence `G(o)=V_minus S_0`, where `V_minus=sum_{odd i}a_{p_i}^2` and `V_plus=sum_{even i}a_{p_i}^2`.

At `o+1`, every selected prime is a unit. Each negative row contributes `S_1`, while a positive row has its `d=1` contribution removed because its row was deleted at `o`, giving `S_1-T_1^2`. Summing squared row amplitudes gives `G(o+1)=V_minus S_1+V_plus(S_1-T_1^2)`.

TPC-403 gives the signed adjacent coefficient `M(o,o+1)=T_1 P_minus`. Division by the two positive local diagonal energies therefore yields the exact normalized square `(T_1P_minus)^2/(G(o)G(o+1))`.

All assertions above are finite identities under the declared CRT masks.
