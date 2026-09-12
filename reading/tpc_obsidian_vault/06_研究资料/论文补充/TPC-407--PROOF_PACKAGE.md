---
type: "source-reading"
source_path: "papers/tpc-407-c1-complete-shell-q-scale-ladder/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-407"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-407-c1-complete-shell-q-scale-ladder/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-407|TPC-407]] · [[00_开始阅读|首页]]

# Proof package

## Theorem (finite complete-shell Q-scale ladder)

Fix `H=66` and `N=264`. Let `Q>N` and assume the complete shell `(Q,2Q]` has even cardinality `2m`, with primes `p_0<...<p_{2m-1}`. Under the CRT residues `o=0 (mod p_i)` for even `i` and `o=-N (mod p_i)` for odd `i`, define `t_d=H^2/(H^2+d^2)`, `S_0=sum_{d=1}^{N-1}t_d^2`, and `S_1=sum_{d=1}^{N-2}t_d^2+t_1^2`. With `a_i=p_i^3/[Q^2(p_i-1)]`, let `P_-`, `V_-`, and `V_+` be the odd/even amplitude sums. The local proxy has

```text
G_0=V_-S_0,  G_1=V_-S_1+V_+(S_1-t_1^2),  M=t_1P_-.
```

For `z=M/sqrt(G_0G_1)` and `a_min=min_i a_i`,

```text
0 <= z <= t_1/(a_min sqrt(S_0S_1)) <= 4/(a_min H) <= 4/H.
```

## Proof

The complete-shell mask profile gives the displayed local energies because `p_i>N`: even primes hit offset zero, odd primes first hit offset `N`, and no prime hits offset one. Thus the TPC-404 local identity applies at every scale. As in TPC-406, `G_1>=V_-S_1`, Cauchy–Schwarz gives `P_-^2<=mV_-`, and the odd terms give `V_->=m a_min^2`. Therefore `z^2<=t_1^2/(a_min^2S_0S_1)`. The terms `d=1,...,H` occur in both sums and have `t_d>=1/2`, so `S_0,S_1>=H/4`; shell membership gives `a_i>1`. Taking square roots proves the claim.

The certificate instantiates the theorem at the four complete shells `Q=4096,8192,16384,32768`, whose exact prime counts are `464,872,1612,3030`. It is a finite Q-scale audit, not a growing or source-valid theorem.
