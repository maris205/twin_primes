---
type: "source-reading"
source_path: "papers/tpc-218-prime-shell-packet-lift/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-218"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-218-prime-shell-packet-lift/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-218|TPC-218]] · [[00_开始阅读|首页]]

# TPC-218 Proof Package

## Maximum claim

PROVED\_STRUCTURAL\_L1: the literal V46 common-source finite-window kernel admits a prime-label- and packet-label-preserving Hilbert lift with normalized split envelope x\^(1/96)(log x)\^5; scalar shell recovery costs P\<=2Q and returns x\^(11/32)(log x)\^5.

TPC218\_ARITHMETIC\_ADVANCE = NO; TPC218\_FIXED\_ATOM\_CREDIT = 0; TPC218\_L2 = NONE; TPC218\_FULL\_GATE\_B = OPEN.

## Theorem

Let I\_x=(x/2,x\] and N=\|I\_x\|. For fixed J and M=max\_j \|\|psi\_j\|\|\_infty, define the rows and kernels in research/tpc-big-road/bridge\_b\_prime\_shell\_packet\_lift.md. Then

```text
sum_(n in I_x)||K_vec(n)||_2^2
  << J M^2 (N+U^2)(Q^2/H)(log x)^5,

N^(-1)sum_(n in I_x)||K_vec(n)||_2^2
  << J M^2 x^(1/96)(log x)^5.
```

Moreover, with K\_j=sum\_q K\_(j,q),

```text
N^(-1)sum_(n in I_x)sum_j|K_j(n)|^2
  << J M^2 x^(11/32)(log x)^5.
```

## Proof dependencies

1.  4Q\<H gives fixed-q cutoff injectivity.
2.  Active rows satisfy h\>=H/(2Q), giving the unsigned harmonic cluster bound.
3.  Reduced fractions with denominator at most U have spacing at least U\^(-2).
4.  The scalar additive large sieve is applied coordinatewise in q and j.
5.  Pointwise Cauchy over q gives the scalar corollary.

No PNT, Möbius cancellation, prime cancellation, or source theorem for the signed Gate-B scalar is used.

## Exact finite validation

The producer and independent checker recompute a rational-coefficient dilation fixture, three finite intervals, the P=4 q-alignment, and the packet projection alignment. The rational fixture uses mu(d)/d only to avoid floating logarithms; it is explicitly not an asymptotic substitute for the literal coefficient.

## Invalid promotion rules

The following promotions are forbidden:

```text
split x^(1/96) -> arithmetic saving                 FORBIDDEN
finite q ratio 4 -> asymptotic prime lower bound     FORBIDDEN
packet trace bound -> signed four-packet cancellation FORBIDDEN
checker PASS -> full Gate-B or twin-prime theorem    FORBIDDEN
```

## Open edge

The next theorem must act on the literal signed prime shell and beat the exact P collapse while retaining the four-packet, zero/nonunit, fixed-atom, and normalization interfaces. This is recorded as ROUND2\_CLUE = PROVE\_A\_SIGNED\_PRIME\_SHELL\_REASSEMBLY\_BEYOND\_THE\_EXACT\_P\_COLLAPSE.
