---
type: "source-reading"
source_path: "papers/tpc-mvp1-fixed-shift-proof-architecture/paper/main.md"
snapshot_date: "2026-09-12"
owner: "TPC-MVP1"
generated: true
semantic_review: "not-certified-by-conversion"
---

> [!info] 阅读范围
> 原文阅读层；转换状态不等于定理认证。公式与印刷编号以原 PDF/TeX 为准。

论文入口：[[02_论文/TPC-MVP1|TPC-MVP1]] · [[00_开始阅读|首页]]

# **TPC-MVP1: A Falsifiable Proof Architecture** **for Fixed-Shift Prime-Pair Correlations:** Verified Interfaces, Explicit Working Hypotheses, and Stop–Go Tests at the Parity Frontier

> Mechanical reading layer generated from the preserved TeX. Original TeX/PDF and hand-edited package materials remain authoritative. This conversion does not certify a proof or upgrade any finite, conditional, synthetic, or open claim.

-   Source TeX: [main.tex](../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-mvp1-fixed-shift-proof-architecture/main.tex)
-   Preserved PDF: [tpc-mvp1-fixed-shift-proof-architecture.pdf](../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-mvp1-fixed-shift-proof-architecture/tpc-mvp1-fixed-shift-proof-architecture.pdf)
-   Bibliography source: [references.bib](../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-mvp1-fixed-shift-proof-architecture/references.bib)
-   Conversion and audit scope: [CONVERSION\_RECORD.md](../99_%E7%BB%B4%E6%8A%A4/%E8%BD%AC%E6%8D%A2%E8%AE%B0%E5%BD%95/TPC-MVP1.md)
-   Author metadata: Liang Wang; School of Artificial Intelligence and Automation,; Huazhong University of Science and Technology, Wuhan 430074, P.R. China; wangliang.f\@gmail.com
-   Source date: July 2026
-   Source repository commit: `d37c92b8a66bbd3d9084b1597d346429a9285302`
-   Converter: `source-markdown-audit-v2`
-   Included-source hashes, input order, and original-file line/page maps: [dependency ledger](../99_%E7%BB%B4%E6%8A%A4/%E8%BD%AC%E6%8D%A2%E8%AE%B0%E5%BD%95/TPC-MVP1.md)

## Abstract

The first 102 papers of the TPC fixed-shift program contain exact identities, literal carrier dictionaries, finite spectral theorems, selected packet closures, obstruction results, and several dependency audits. They do not contain a fixed-shift prime-pair theorem. This paper deliberately changes scale: it compresses that infrastructure into a single falsifiable proof architecture.

We first record a coarse seven-stage audit and isolate the results that may be imported without conjecture. These include the reduction of a weighted fixed-shift prime correlation to one named hard packet, the determinant and full-block interfaces, lossless low-window affine export, endpoint-scale return of two literal exceptional resonance branches within the present low-window decomposition, an exact multiplicative resonance spectrum, and a width-sensitive three-ledger inequality for the remaining positive resonant carrier.

We then formulate three macro hypotheses—literal completeness, literal packet saving, and physical synthesis—resolved into nine separately auditable gates. One gate, a growing fixed-$h_0$ signed affine Möbius estimate, is explicitly identified as the parity-facing arithmetic hypothesis; it is neither proved nor called technical. Under the nine hypotheses, with all objects in one normalization and a total physical loss strictly below $1/400$, we prove a conditional weighted Hardy–Littlewood asymptotic. For a nonnegative weight this conditionally gives $\gg X/\log^2 X$ prime pairs in a dyadic interval, and only then may one specialize to $h_0=2$.

The contribution is therefore a map rather than an exit from the maze: every conjectural edge has a go certificate, a genuine stop certificate, and a publishable fallback. No new $\mathrm{L2}$ estimate, parity breakthrough, twin-prime conclusion, Riemann-hypothesis consequence, or spectral identification of zeta zeros is asserted.

<!-- SOURCE_BODY_BEGIN -->

**Keywords:** fixed-shift prime pairs; parity barrier; Möbius correlation; determinant dispersion; literal arithmetic carrier; conditional synthesis; falsifiable roadmap.

# Purpose, claim taxonomy, and the fixed-shift target

## Four claim tags and three proof levels

Every major statement in this paper carries one of four logical tags: $$\textcolor{green!45!black}{\textbf{[E]}}\ \text{established},\qquad \textcolor{orange!70!black}{\textbf{[H]}}\ \text{working hypothesis},\qquad \textcolor{blue!65!black}{\textbf{[C]}}\ \text{conditional synthesis},\qquad \textcolor{red!65!black}{\textbf{[N]}}\ \text{not established}.$$ The tags answer a different question from the inherited proof levels: $\mathrm{L0}$ denotes finite algebra, exact model identities, abstract operator theorems, or countermodels; $\mathrm{L1}$ denotes a literal physical-frame interface preserving the actual arithmetic typing; and $\mathrm{L2}$ is reserved for a new growing estimate on the complete coefficient attached to one prescribed nonzero shift $h_0$.

###### ref-0cd721f8a477ea83

> **Definition: Promotion rule** \[def:promotion\] An averaged-shift, almost-all-scale, frozen-family, random-sign, support-only, positive-square, or surrogate-carrier estimate is not an $\mathrm{L2}$ estimate for the physical fixed-$h_0$ coefficient unless an explicit theorem returns it to that coefficient with all losses and exceptional sectors controlled.

This paper is an $\mathrm{L1}$ synthesis. A conditional implication may have an $\mathrm{L2}$ conclusion while none of its unproved hypotheses is promoted to an established $\mathrm{L2}$ theorem.

## The target correlation

###### ref-4d0f04326548e427

Fix throughout a nonzero even integer $h_0$, and let $W\in C_c^\infty((0,\infty))$ be fixed. Write $$\mathcal C_{h_0,W}(X) = \sum_{n\ge1}\Lambda(n)\Lambda(n+h_0)W(n/X).$$ If $\nu_{h_0}(p)$ is the number of residue classes occupied by $\{0,-h_0\}\pmod p$, define the usual singular series $$\mathfrak S(h_0) = \prod_p \frac{1-\nu_{h_0}(p)/p}{(1-1/p)^2}.$$ It is positive for every fixed admissible even $h_0$. The centered defect is the classical prime-pair target [`\cite{HardyLittlewood1923,FriedlanderIwaniec2010}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-f4ffa381ee727373); [\[FriedlanderIwaniec2010\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-c8acfd6f8b1ff9cf): $$\Delta_{h_0,W}(X) = \mathcal C_{h_0,W}(X) -\mathfrak S(h_0)X\int_0^\infty W(t)\,dt. \label{eq:defect}$$

###### ref-f3666ac1d899727a

###### ref-f9999b0333290eda

> **Proposition: **\[E\]** Established hard-packet anchor** \[prop:anchor\] The TPC fixed-shift local-model reduction gives, for a suitable fixed $0<\delta<1/2$, $$\Delta_{h_0,W}(X) = B_{h_0,\delta}(X) +O_{A,h_0,W,\delta}\!\left(X(\log X)^{-A}\right) \label{eq:hard-packet-anchor}$$ for every fixed $A>0$, where $B_{h_0,\delta}$ is an explicitly defined bilinear hard packet. Consequently the weighted Hardy–Littlewood asymptotic is equivalent, within that reduction, to $$B_{h_0,\delta}(X)=o(X).$$

This is the entrance to the architecture, not an estimate of the hard packet. The purpose of the later TPC layers is to expose its literal geometry without replacing it by an easier random or averaged object [`\cite{WangTPC15,WangTPC18}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-b0805195de3a7444); [\[WangTPC18\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-4abf939102bd1649).

## Six invariants that no route may drop

Every hypothesis and every future promotion is audited against:

1.  the literal physical coefficients, including their signs and reconstruction multipliers;

2.  one prescribed nonzero $h_0$, not an averaged or subsequently chosen shift;

3.  physical atomic normalization and exactly one global normalization;

4.  canonical or losslessly invertible native keys, without null-pair inflation;

5.  the actual active support, masks, prefixes, polarizations, short fibers, and boundary sectors; and

6.  a nonduplicated endpoint ledger whose total physical loss is strictly below $1/400$.

Failure of any item prevents a claim of final proof progress. In particular, equality at the physical endpoint is a stop.

# What 102 papers actually established

The papers TPC-1 through TPC-102 are consecutive, but they are not 102 monotone steps toward a proof. They include exact identities, finite spectral calculations, literal dictionaries, conditional interfaces, selected packet theorems, sharp countermodels, and route audits. A useful compression is the following seven-stage ledger.

@ \>p0.9cm \>p1.55cm Y \>p2.0cm@ Stage & Papers & Established content at coarse resolution & Honest status\
A & TPC-1–9 & Two-scale sieve correlations, singular-series calibration, prime-target defect identities, and the exact appearance of the large-divisor fixed-shift tail. Ordinary spectral flatness is shown not to control rare prime-pair events. & $\mathrm{L0}/\mathrm{L1}$ entrance and no-go\
B & TPC-10–18 & Factor-scale and fixed-shift Type-II normal forms, the named hard packet, two $TT^*$ quadraticizations, determinant variables, exact endpoint collapses, and a conditional full-block closure template. & $\mathrm{L1}$ reduction; determinant dispersion open\
C & TPC-19–36 & Primitive determinants, conductor and fiber decompositions, dynamic cutoffs, one-sided Poisson passages, joint-before-centering rules, selected calibrated squares, and the distinguished zero-frequency gate. & Several selected $\mathrm{L1}$ blocks; full tail open\
D & TPC-37–55 & CRT and alias tomography, native Gram expansions, four-Möbius isolation, partial sign freezing, all-band tiling, atomic distortion, literal cell survival, and canonical-frame obstructions. & Physical interfaces plus sharp no-go theorems\
E & TPC-56–72 & Shorted-Gram reassembly, exact quantifier-safe closure alternatives, native affine provenance, residual grouping, primitive cofactor planes, trace/operator nonteleportation, and a ten-paper route audit. & $\mathrm{L0}/\mathrm{L1}$ carrier architecture\
F & TPC-73–92 & Primitive support and completion certificates, actual-support incidence, scalar holonomy, determinant-energy transfer, zero-mode barriers, Tauberian defects, local squarefree support, and exact full-block cover criteria. & Five separately required gates; no $\mathrm{L2}$ theorem\
G & TPC-93–102 & Lossless literal low-window affine export, exact conductor and progression ledgers, anchored translation formulas, safe zero-mode projection, two exceptional branch returns, exact multiplicative resonance spectrum, opened-atom linearization, and the three-ledger master inequality. & Latest $\mathrm{L1}$ resonance route\

Representative anchors for the seven stages are TPC-1 and TPC-15 for A, TPC-18 for B, TPC-28 and TPC-32 for C, TPC-50 and TPC-51 for D, TPC-70 for E, TPC-82 and TPC-92 for F, and TPC-102 for G [`\cite{WangTPC1,WangTPC15,WangTPC18,WangTPC28,WangTPC32,WangTPC50, WangTPC51,WangTPC70,WangTPC82,WangTPC92,WangTPC102}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-74fc6e16e37efeee); [\[WangTPC15\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-b0805195de3a7444); [\[WangTPC18\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-4abf939102bd1649); [\[WangTPC28\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-1f714b6620a45b76); [\[WangTPC32\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-49ad82103eb75eb7); [\[WangTPC50\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-0d8078e2652e9912); [\[WangTPC51\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-09a584963bbbf4f9); [\[WangTPC70\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-9d0361df6408698e); [\[WangTPC82\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-cfeb22890911c08a); [\[WangTPC92\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-8444c63105c2920e); [\[WangTPC102\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-7967ea1ba73edadd).

## What moved forward

The principal progress is not a numerical count of manuscripts. Four qualitative changes are durable.

1.  The target was reduced from an informal parity narrative to the named scalar defect $B_{h_0,\delta}(X)$ in [\[eq:hard-packet-anchor\]](TPC-MVP1.md#ref-f9999b0333290eda).

2.  Many changes of variables are now losslessly typed: source, content, conductor, determinant, affine slope, mask, polarization, and global normalization can be traced in important low-window and residual sectors [`\cite{WangTPC18,WangTPC70,WangTPC93}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-4abf939102bd1649); [\[WangTPC70\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-9d0361df6408698e); [\[WangTPC93\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-2d5bd9665d7257b5).

3.  Several seductive but invalid shortcuts have exact countermodels: support or unsigned energy does not determine the zero mode; continuous signed Mellin representations do not possess a uniform finite lower frame; logarithmic cancellation does not automatically translate to ordinary cancellation; and a singleton cell does not provide cross-cell dispersion [`\cite{WangTPC51,WangTPC81,WangTPC90,WangTPC100}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-09a584963bbbf4f9); [\[WangTPC81\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-ff65f956e7cf0d6d); [\[WangTPC90\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-4f3149d531dce18d); [\[WangTPC100\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-3a25dec8d6d49e3b).

4.  The latest resonance carrier is no longer a vague spectral object. Its constant and $q_X\mid u$ exceptional branches are separately returned within the present low-window decomposition and native normalization, and its remaining positive part is governed by three explicit weighted ledgers [`\cite{WangTPC98,WangTPC101,WangTPC102}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-b430ed4aad3480af); [\[WangTPC101\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-9e9161a8530e65b2); [\[WangTPC102\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-7967ea1ba73edadd).

## What did not move

No paper through TPC-102 proves a growing estimate for the complete literal coefficient attached to one prescribed $h_0$. In particular:

-   no fixed-shift Möbius or Liouville cancellation theorem is available on the full generic affine carrier;

-   no determinant-energy lower bound and distinguished zero-mode estimate have been proved simultaneously on the actual support;

-   no all-block physical return with strict endpoint slack is complete; and

-   no parity breakthrough, prime-pair lower bound, or twin-prime theorem has been obtained.

The dependency graph has become narrower and more falsifiable; no quantitative distance to a proof is asserted.

# The established ledger

This section collects only facts that the MVP architecture imports as proved. Their conjunction still falls short of an $\mathrm{L2}$ estimate.

> **Proposition: **\[E\]** E1: exact target anchoring** The target defect is anchored by [\[eq:hard-packet-anchor\]](TPC-MVP1.md#ref-f9999b0333290eda). Thus a proof of $B_{h_0,\delta}(X)=o(X)$, with the actual fixed-$h_0$ coefficient, is sufficient and necessary within the imported local-model reduction.

> **Proposition: **\[E\]** E2: determinant and full-block interfaces** The Möbius tail admits exact $TT^*$, lcm-return, content, determinant, and primitive/nonprimitive decompositions. A generic primitive determinant-dispersion input together with an all-block cover would conditionally close the tail. Neither that dispersion input nor the all-block cover is asserted as proved [`\cite{WangTPC18,WangTPC91}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-4abf939102bd1649); [\[WangTPC91\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-8f1d4a8c9b42f76d).

> **Proposition: **\[E\]** E3: literal carrier typing** On the sectors for which a literal dictionary has been certified, the physical coefficient can be transported while retaining $h_0$, source keys, content/projector children, both polarizations, masks, prefixes, Möbius signs, actual support, and one global normalization. TPC-93 gives a lossless low-window affine export and restores the reduced determinant to the physical value $h_0$ [`\cite{WangTPC93}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-2d5bd9665d7257b5).

> **Proposition: **\[E\]** E4: route exclusions** The following implications are false without additional literal input:
>
> 1.  ordinary Haar spectral behavior implies rare prime-pair correlation [`\cite{WangTPC1}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-74fc6e16e37efeee);
>
> 2.  support, completion, or unsigned energy implies zero-mode cancellation [`\cite{WangTPC81,WangTPC82}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-ff65f956e7cf0d6d); [\[WangTPC82\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-cfeb22890911c08a);
>
> 3.  arbitrary continuous signed Mellin synthesis has a uniform finite lower frame [`\cite{WangTPC51}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-09a584963bbbf4f9);
>
> 4.  anchor-free logarithmic cancellation implies translated ordinary cancellation [`\cite{WangTPC87,WangTPC96}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-c10bb69652986ef9); [\[WangTPC96\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-b1a041931cf4c7cf);
>
> 5.  squarefree local density implies Möbius-sign cancellation [`\cite{WangTPC90}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-4f3149d531dce18d); and
>
> 6.  conductor $q_X$, singleton fine cells, or bounded overlap by itself implies physical resonance dispersion or full-block cover [`\cite{WangTPC91,WangTPC99,WangTPC100}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-8f1d4a8c9b42f76d); [\[WangTPC99\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-d0d31470086cb360); [\[WangTPC100\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-3a25dec8d6d49e3b).

###### ref-b6b4f3295a2ce8dc

> **Proposition: **\[E\]** E5: two literal exceptional returns** \[prop:exceptional-returns\] Within the present literal low-window decomposition, the conductor-one constant-phase branch and the nonconstant $q_X\mid u$ opened branch are each returned at the recorded endpoint scale $$X^{o(1)}Q_X^2.$$ These are $\mathrm{L1}$ branch closures. They are not estimates of the complete signed low-window coefficient [`\cite{WangTPC98,WangTPC100}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-b430ed4aad3480af); [\[WangTPC100\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-3a25dec8d6d49e3b).

###### ref-bbfd4fcb3bbc17cb

###### ref-9f7632b90811001e

> **Theorem: **\[E\]** E6: three-ledger resonance inequality** \[thm:three-ledger\] For the remaining positive invertible resonant carrier, define $$\mathfrak P_X =\sum_{H\in\mathcal H_X}\frac{2H}{q_X-1}M_H^{\mathrm{inv}}, \qquad \mathfrak X_X =\sum_{H\in\mathcal H_X}g_{q_X}(H) \sqrt{|\mathfrak X_H^\circ|},$$ where $$g_q(H) = \sqrt{\frac{2H(q-1-2H)}{q-1}},$$ and let $W_X$ be the maximum normalized opened-atom weight. The imported literal results give $$\mathcal C_{\mathrm{exc},X}^{\mathrm{abs}} \ll X^{o(1)}Q_X^2 +B_X\left[ \mathfrak P_X+ \sqrt{W_X|\mathcal H_X|(q_X-1)\mathfrak P_X} +\mathfrak X_X \right]. \label{eq:three-ledger}$$ The first term includes the exceptional returns in [\[prop:exceptional-returns\]](TPC-MVP1.md#ref-b6b4f3295a2ce8dc); the three quantities in brackets are not bounded at the required growing scale by the established theory [`\cite{WangTPC101,WangTPC102}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-9e9161a8530e65b2); [\[WangTPC102\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-7967ea1ba73edadd).

###### ref-fe27ab20c0328fa5

###### ref-1f79b8eda88708f5

###### ref-35527426b18efe95

> **Proposition: **\[E\]** E7: two independent exponent ledgers** \[prop:two-ledgers\] If the determinant energy and distinguished zero mode are written as $$D_X\ge X^{-\lambda_D+o(1)}Q_X^3J_X^2, \qquad |Z_X|\le X^{-\eta_Z+o(1)}Q_X^2,$$ then the recorded sufficient compatibility condition is $$\lambda_D\le 2\eta_Z. \label{eq:det-compatibility}$$ This is independent of the physical synthesis requirement $$\Lambda_{\mathrm{phys}}<\frac1{400}. \label{eq:physical-endpoint}$$ Equality is compatible in [\[eq:det-compatibility\]](TPC-MVP1.md#ref-1f79b8eda88708f5) but leaves no determinant reserve; equality in [\[eq:physical-endpoint\]](TPC-MVP1.md#ref-35527426b18efe95) is a stop. The same loss may not be charged to both ledgers [`\cite{WangTPC81,WangTPC82,WangTPC92}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-ff65f956e7cf0d6d); [\[WangTPC82\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-cfeb22890911c08a); [\[WangTPC92\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-8444c63105c2920e).

> **Proposition: **\[E\]** E8: cover and arithmetic dispersion are independent** An exact or controlled-remainder full-block cover does not imply primitive determinant cancellation, and a determinant estimate on a selected block does not imply literal full-block reassembly. Both must be supplied in one carrier and one quantifier scope [`\cite{WangTPC91,WangTPC92}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-8f1d4a8c9b42f76d); [\[WangTPC92\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-8444c63105c2920e).

> **Remark: The first genuinely new $\mathrm{L2}$ event** A future theorem would count as the first $\mathrm{L2}$ advance only if it reduces a fixed polynomial exponent for the actual growing fixed-$h_0$ coefficient, uniformly returns every sector required by its statement, and survives the physical normalization. A new exact spectrum or finite certificate, however useful, remains $\mathrm{L0}/\mathrm{L1}$.

# The minimum viable hypothesis stack

Set $$\sigma_*=\frac1{400}.$$ The architecture has three macro hypotheses: $$\begin{gathered} \boxed{\mathbf L\ \text{literal completeness}} \quad+\quad \boxed{\mathbf P\ \text{literal packet saving}} \quad+\quad \boxed{\mathbf S\ \text{physical synthesis}}\\ \Longrightarrow\quad B_{h_0,\delta}(X)=o(X). \end{gathered}$$ They are resolved below into nine gates. The resolution is intentionally redundant enough to be falsifiable: a failed gate names the object and the route that failed.

## Macro hypothesis $\mathbf L$: literal completeness

###### ref-62ba4a5b2dbfc831

\[hyp:canonical-synthesis\] There is a provenance-preserving canonical packet family $\{\mathcal P_b\}_{b\in\mathcal B_X}$, with $|\mathcal B_X|=X^{o(1)}$, defined from the actual fixed-$h_0$ coefficient. On the actual support, this family is an exhaustive disjoint classification into exceptional resonant, remaining resonant, generic, and returned-complement packets; no physical block lies outside these classes. Its keys retain every invariant in [1.3](../99_%E7%BB%B4%E6%8A%A4/%E6%BA%90%E5%AE%9A%E4%BD%8D/TPC-MVP1.md#src-f80339956e1f4145). The synthesis map is the inherited physical map, not an arbitrary signed representation, and its cost is entered once in $\Lambda_{\mathrm{phys}}$.

###### ref-fae9666638a15d00

\[hyp:high\] The high-frequency reconstruction tail, ultra-long residual complement, short and bounded fibers, slope collisions, both polarizations, endpoint bands, and outer keys are either assigned to a soft remainder whose *complete outer sum* is $o(X)$ in the original normalization, or retained as packet terms that satisfy the same raw saving $X^{1-\sigma_*+o(1)}$ used below. Write $\mathcal B_X^{\mathrm{ns}}\subseteq\mathcal B_X$ for the indices of these retained nonsoft packets. No favorable sector is silently promoted to the full coefficient.

###### ref-9ca7babc220bb159

\[hyp:full-block\] The TPC-18 block family covers the literal physical tail in one carrier and one quantifier scope. Either an exact certificate $Bc=w$ holds, or the uncovered physical remainder is estimated separately by $o(X)$. Overlap, missing blocks, and normalization are included in the synthesis operator.

###### ref-e326e6186ebae5e4

\[hyp:localization\] Every frozen, aliased, frequency-averaged, or auxiliary-parameter estimate used by the route returns, with subcritical recorded cost, to the same prescribed nonzero $h_0$. An almost-all or averaged-shift statement does not satisfy this hypothesis.

###### ref-c0f71b8382f40c80

\[hyp:reconnection\] After all packet estimates and reassembly, the output intertwines exactly with the original hard packet $B_{h_0,\delta}(X)$ in [\[eq:hard-packet-anchor\]](TPC-MVP1.md#ref-f9999b0333290eda). There is no second global normalization, omitted branch, duplicated atom, or substitution of a surrogate Gram matrix for the native physical Gram matrix.

Together, H1, H4, H6, H7, and H8 constitute macro hypothesis $\mathbf L$. They are structural and analytic, but they are not declared easy.

## Macro hypothesis $\mathbf P$: packet saving

###### ref-b7d2012885f47d36

###### ref-b705ddfbaff6f285

\[hyp:resonance\] On the actual growing TPC-102 invertible carrier, $$B_X\le X^{o(1)},\qquad W_X\le X^{o(1)},\qquad \mathfrak P_X\le X^{o(1)}Q_X^2,\qquad \mathfrak X_X\le X^{o(1)}Q_X^2. \label{eq:resonance-hypothesis}$$ These bounds use the opened atomic weights and active widths, not an ambient branch census. The exact inherited normalization transports [\[eq:three-ledger\]](TPC-MVP1.md#ref-9f7632b90811001e), including its leading exceptional term and the two E5 returns, to the raw packet target $$|\mathcal P_{b,\mathrm{res}}| \le X^{1-\sigma_*+o(1)}.$$

The last sentence is part of the hypothesis because [\[eq:three-ledger\]](TPC-MVP1.md#ref-9f7632b90811001e) is a native $TT^*$-scale statement. A normalization crosswalk must be proved rather than inferred by dimension counting.

###### ref-c48244d98c7eee53

###### ref-fe74ddc4eb74002f

###### ref-d627f5c0595de4db

\[hyp:generic\] For every actual long generic affine block, retain in the same sum the literal Möbius weights, the $r$-dependent phase, the affine character, the reconstruction multiplier, all prefixes, and the fixed $h_0$. Its normalized signed $TT^*$ correlation satisfies the working target $$\mathcal G_{b,\mathrm{gen}}^{\mathrm{signed}} \ll XQ_b\,X^{-1/200+o(1)}, \label{eq:generic-ttstar}$$ and, jointly, its exact physical $TT^*$ normalization supplies the packet target $$|\mathcal P_{b,\mathrm{gen}}| \ll X^{1-\sigma_*+o(1)}. \label{eq:generic-packet}$$ The estimate is required only for the literal coefficient family generated by the TPC dictionary, not for arbitrary slopes, arbitrary weights, or a uniform Chowla family.

No derivation of [\[eq:generic-packet\]](TPC-MVP1.md#ref-d627f5c0595de4db) from [\[eq:generic-ttstar\]](TPC-MVP1.md#ref-fe74ddc4eb74002f) is asserted in this paper. The two displays are joint parts of H3. A future proof must exhibit the exact normalizing prefactor that turns the $1/200$ quadratic saving into a $1/400$ packet saving.

Hypothesis H3 is the parity-facing arithmetic gate. It is the boldest assumption in the paper and may contain most of the difficulty of the original problem. Calling it “spectral” does not make it a proved cancellation theorem.

###### ref-7f62e726490205a3

\[hyp:det-zero\] On the actual post-bin coefficient, there exist exponents $\lambda_D,\eta_Z\ge0$ such that $$D_X\ge X^{-\lambda_D+o(1)}Q_X^3J_X^2, \qquad |Z_X|\le X^{-\eta_Z+o(1)}Q_X^2,$$ and $$\lambda_D\le2\eta_Z.$$ The corresponding literal transfer inequality is assumed to introduce no further fixed-power loss beyond the exponents already charged in this determinant ledger and in $\Lambda_{\mathrm{phys}}$. Ambient, random-model, pre-bin, or support-only energy is not a substitute for $D_X$, and a nonzero-frequency spectral gap is not a substitute for the estimate of $Z_X$.

H2, H3, and H5 constitute macro hypothesis $\mathbf P$. H2 is a sufficient positive route for the resonance sector. If it fails, a signed filter-before-majorant replacement may be inserted, but the replacement must still deliver the packet bound at the same normalization.

## Macro hypothesis $\mathbf S$: strict physical endpoint

###### ref-77da2eef56d57e72

\[hyp:endpoint\] After every frame, grouping, missing-high, localization, cover, boundary, and native-Gram cost has been charged exactly once, the physical synthesis operator obeys $$\left| \mathscr S_X\bigl(\{\mathcal P_b\}_{b\in\mathcal B_X^{\mathrm{ns}}}\bigr) \right| \le X^{\Lambda_{\mathrm{phys}}+o(1)} \max_{b\in\mathcal B_X^{\mathrm{ns}}}|\mathcal P_b|,$$ with $$\Lambda_{\mathrm{phys}}<\sigma_*=\frac1{400}.$$

Subpower block multiplicity is absorbed in the $o(1)$. Equality $\Lambda_{\mathrm{phys}}=1/400$ does not close the route. The compatibility $\lambda_D=2\eta_Z$ in H5 is not reusable as physical endpoint slack.

## Strength and nonminimality

> **Remark: The stack may be stronger than the target** The conjunction H1–H9 is designed to imply a scalar Hardy–Littlewood asymptotic, but the converse is neither claimed nor expected. A scalar asymptotic need not imply a positive bound on every fiber, a uniform cross-map majorant, or a canonical frame estimate. Thus “minimum viable” means a compact program exposing the interfaces currently identified in this series; it does not mean a logically minimal or independently easier reformulation of the twin-prime problem.

> **Remark: The three resonance ledgers are not all remaining obstacles** The quantities $W_X,\mathfrak P_X,\mathfrak X_X$ are the remaining ledgers in one positive resonant subcarrier. Generic signed arithmetic, full-block return, fixed-$h_0$ localization, determinant/zero-mode compatibility, high-frequency return, and the strict endpoint remain independent.

# Conditional synthesis

The following implication is the only global theorem of TPC-MVP1. Its proof is short because the difficulty has been made explicit in the hypotheses.

###### ref-74ec56cc6b878d98

###### ref-39461e8c85cf669a

> **Theorem: **\[C\]** Conditional fixed-shift Hardy–Littlewood synthesis** \[thm:conditional-hl\] Fix an admissible nonzero even integer $h_0$ and $W\in C_c^\infty((0,\infty))$. Assume H1–H9 for the literal TPC carrier, with every estimate taken in the same physical normalization and quantifier scope. Then $$\sum_{n\ge1}\Lambda(n)\Lambda(n+h_0)W(n/X) = \mathfrak S(h_0)X\int_0^\infty W(t)\,dt+o(X). \label{eq:conditional-hl}$$

> **Proof** Hypotheses H1, H4, and H6 produce an exhaustive subpower-size classification of physical blocks. Every term assigned to the soft remainder contributes $o(X)$ after the complete outer summation. The two established exceptional returns together with H2 handle the resonant blocks; H3 handles the generic signed blocks; and H4 returns every remaining short, high, ultra, boundary, and outer block. Thus every nonsoft raw block entering synthesis satisfies $$\max_{b\in\mathcal B_X^{\mathrm{ns}}}|\mathcal P_b| \le X^{1-\sigma_*+o(1)}.$$ Hypothesis H5 certifies that the determinant/zero-mode transfer used in that statement has no unrecorded incompatibility. H7 returns all auxiliary parameters to the prescribed $h_0$, and H9 gives $$\left| \mathscr S_X\bigl(\{\mathcal P_b\}_{b\in\mathcal B_X^{\mathrm{ns}}}\bigr) \right| \le X^{1-\sigma_*+\Lambda_{\mathrm{phys}}+o(1)} =o(X),$$ because $\Lambda_{\mathrm{phys}}<\sigma_*$. H8 identifies this synthesis output with $B_{h_0,\delta}(X)$, up to the already recorded $o(X)$ remainder. Therefore $$B_{h_0,\delta}(X)=o(X).$$ Insert this in the established identity [\[eq:hard-packet-anchor\]](TPC-MVP1.md#ref-f9999b0333290eda).

> **Remark: What the theorem does and does not prove** [\[thm:conditional-hl\]](TPC-MVP1.md#ref-74ec56cc6b878d98) proves an implication from explicit unproved hypotheses to the target correlation. It does not prove H1–H9. In particular H3 contains the unresolved growing fixed-$h_0$ arithmetic cancellation, and the conjunction of the hypotheses may be stronger than [\[eq:conditional-hl\]](TPC-MVP1.md#ref-39461e8c85cf669a).

## The conditional prime-pair consequence

###### ref-f726065b80ab924c

> **Corollary: **\[C\]** Conditional fixed-gap prime pairs** \[cor:conditional-pairs\] Assume H1–H9 for a fixed admissible even $h_0$ and for one fixed nonnegative, nonzero $W\in C_c^\infty((1,2))$. Then $$\#\{p\in[X,2X+O_{h_0}(1)]:       p\ \text{and}\ p+h_0\ \text{are prime}\} \gg_{h_0,W}\frac{X}{(\log X)^2}$$ for all sufficiently large $X$.

> **Proof** Since $\mathfrak S(h_0)>0$ and $\int W>0$, [\[thm:conditional-hl\]](TPC-MVP1.md#ref-74ec56cc6b878d98) gives $$\mathcal C_{h_0,W}(X)\gg_{h_0,W}X.$$ The terms for which $n$ or $n+h_0$ is a prime power of exponent at least two contribute at most $$O_{h_0,W}\!\left(X^{1/2}(\log X)^2\right)=o(X).$$ The remaining mass comes from prime-prime pairs, and each term is at most $O_W((\log X)^2)$. Division gives the stated lower bound.

###### ref-2ac8bdccf69614dc

> **Corollary: **\[C\]** Conditional $h_0=2$ specialization** \[cor:conditional-twins\] If H1–H9 are eventually proved for the prescribed shift $h_0=2$, then [\[cor:conditional-pairs\]](TPC-MVP1.md#ref-f726065b80ab924c) implies infinitely many twin primes.

> **Remark: No sharp unsmoothing is needed for infinitude** A single fixed nonnegative smooth weight already yields the conditional lower bound in [\[cor:conditional-pairs\]](TPC-MVP1.md#ref-f726065b80ab924c). Smooth majorants and minorants may recover sharper interval formulations, but positivity and removal of higher prime powers are not the new parity-facing input. That input is H3, or an equally strong signed replacement for a failed positive route.

## A proof skeleton in nine moves

The conditional theorem may be read as the following end-to-end program:

1.  calibrate the singular-series main term and isolate $B_{h_0,\delta}$;

2.  export the literal coefficient into canonical native packets;

3.  return the two established exceptional resonance branches;

4.  prove or replace the $W_X,\mathfrak P_X,\mathfrak X_X$ positive resonance gates;

5.  prove signed generic affine Möbius cancellation on the actual carrier;

6.  return every short, high, ultra, boundary, and outer sector;

7.  verify determinant energy and the distinguished zero mode;

8.  reassemble and localize to the prescribed $h_0$ with strict endpoint slack; and

9.  reconnect to the original hard packet and use positivity only after the weighted asymptotic is obtained.

No move may be deleted by renaming its output.

# Dependency graph and the role of dynamics

## The full logical graph

The route is intentionally drawn with conjectural nodes visible.

The graph has two important forks.

1.  H2 is a *positive* sufficient route. If a literal principal or cross-map ledger is too large, the route may switch to a signed filter before taking absolute values. Failure of H2 does not disprove the scalar correlation.

2.  H3 may be approached through direct native-$h_0$ determinant dispersion, a coherent prime-square theorem, or a signed affine large sieve. A result on an averaged shift or random coefficient is a different branch, not a proof of H3.

## Where the parity difficulty lives

The program has already classified the local squarefree support in the primitive affine sector. After that classification the remaining sign is an actual growing Liouville/Möbius parity correlation [`\cite{WangTPC90}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-4f3149d531dce18d). Accordingly, the architecture does not claim that the parity barrier has been partly broken. It claims something more modest and testable:

> the literal carrier and normalization at which parity-sensitive cancellation must occur have been isolated more sharply.

H3 is the node where an actual arithmetic advance must enter. A support theorem, positive density, spectral decomposition, or finite certificate cannot substitute for it.

## What the dynamical language contributes

The dynamical and spectral language used throughout the broader program contributes:

-   canonical symbolic, orbit, conductor, and affine coordinates;

-   transfer-like decompositions and exact finite resonance modes;

-   Gram, projection, energy, holonomy, and width-sensitive norm identities;

-   branch classification, provenance, and loss ledgers; and

-   sharp countermodels that identify where a proposed transfer loses the physical zero mode.

These are genuine structural uses. In particular, the multiplicative character spectrum behind [\[eq:three-ledger\]](TPC-MVP1.md#ref-9f7632b90811001e) replaces a crude worst-eigenvalue estimate by the exact filter factor $g_q(H)$ [`\cite{WangTPC99,WangTPC101}`](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-d0d31470086cb360); [\[WangTPC101\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/TPC-MVP1.md#cite-9e9161a8530e65b2).

## What it does not contribute automatically

No dynamical or finite spectral identity in this program automatically supplies:

-   independence of primes;

-   Möbius randomness on the actual fixed-$h_0$ carrier;

-   a fixed-shift arithmetic cancellation theorem;

-   a breach of sieve parity; or

-   an identification of Riemann zeros with eigenvalues of the TPC operators.

The safe summary is:

> *Dynamics organizes the arithmetic carrier and exposes where cancellation must occur; it does not itself supply that cancellation.*

No statement in TPC-MVP1 concerns the Riemann hypothesis, Hilbert–Pólya, or a zeta-spectrum realization.

## Two exponent geometries

The current packet scales $$Q_X=X^{267/400+o(1)}, \qquad J_X=X^{133/400+o(1)}$$ satisfy $Q_XJ_X=X^{1+o(1)}$. On a resolved long fiber $N\ge J_X$, the established width-sensitive resonance norm replaces the crude exponent $267/800$ by $67/400$, a gain $$\frac{267}{800}-\frac{67}{400} =\frac{133}{800}.$$ This is a real native spectral improvement on those fibers. It is not a global packet estimate because short fibers, principal mass, cross-map excess, and physical synthesis still have to be returned.

Independently, the physical synthesis has only the strict allowance $$\Lambda_{\mathrm{phys}}<\frac1{400}.$$ The large local numerical gain above may not be spent twice or transferred to unrelated blocks without a theorem.

# Stop–go criteria and route switching

A route does not stop because a proof attempt is difficult. A genuine stop certificate is an actual-coefficient lower bound, counterexample, kernel, nonidentifiability theorem, or exponent obstruction in the claimed quantifier scope.

@ \>p1.8cmY Y Y@ Gate & Go certificate & Genuine stop certificate & Response\
Opened-atom cap & $W_X\le X^{o(1)}$ for actual normalized atoms & An actual family forces $W_X\ge X^\omega$ on active mass, with no compensating small total weight & Peel heavy atoms; refine conductor/length; analyze them with signs\
Principal mass & $\mathfrak P_X\le X^{o(1)}Q_X^2$ in the literal inverse-length census & $\mathfrak P_X/Q_X^2\ge X^\pi$ on actual packets & Stop the positive termwise bound; center or keep principal/nonprincipal cancellation\
Map quotient & Identical affine maps aggregate with exact weight and recoverable provenance & Literal provenance forces polynomial unresolved multiplicity after canonical quotient & Publish collision classification; change the carrier\
Cross-map excess & $\mathfrak X_X\le X^{o(1)}Q_X^2$ after identical maps are removed & Distinct actual maps force a fixed-power excess & Use signed filter before majorant, retaining phases and Möbius weights\
Generic affine & [\[eq:generic-ttstar\]](TPC-MVP1.md#ref-fe74ddc4eb74002f) on the complete literal family & A coherent actual subfamily violates the required exponent, or the gate is proved equivalent to an unresolved stronger input & Change cutoff geometry, subtract a new main term, or publish the no-reduction theorem\

@ \>p1.8cmY Y Y@ Gate & Go certificate & Genuine stop certificate & Response\
Determinant / zero & $\lambda_D\le2\eta_Z$ on the actual post-bin coefficient & An actual family forces $\lambda_D>2\eta_Z$ & Improve the zero mode, use a direct physical expansion, or publish the compatibility no-go\
Canonical frame & Subpower condition cost on the inherited packet family & A genuine canonical condition number spends a fixed power at or beyond the budget & Switch to direct native-$h_0$ determinant dispersion\
Localization & Auxiliary estimates return to the prescribed $h_0$ at recorded subcritical cost & Only averaged, density-one, or frozen-family control is possible & Publish the restricted theorem with its qualifier; do not promote it\
Full return & Exact cover or separately controlled physical remainder & Actual-support remainder or native-Gram mismatch has fixed-power size & Repair the partition or publish the reassembly obstruction\
Endpoint & $\Lambda_{\mathrm{phys}}<1/400$, with every loss charged once & $\Lambda_{\mathrm{phys}}\ge1/400$, including equality & Reoptimize parameters or publish endpoint infeasibility\

## The positive-to-signed switch

The positive resonance strategy takes absolute values before the outer signed reconstruction. If its principal or cross-map ledger has a literal polynomial obstruction, the correct fallback is $$\text{signed filter}\quad\longrightarrow\quad \text{arithmetic estimate}\quad\longrightarrow\quad \text{majorization},$$ not another paper on positive cross-cell dispersion. The signed object must retain:

-   the reconstruction multiplier and its sign;

-   the $r$-dependent unit phase;

-   the affine character and actual moving row;

-   the Möbius factors inside each resolved fiber; and

-   coherent outer reassembly across frequency-free branches.

An estimate for independent $r$ and branch variables does not control this product.

## The three principal route families

1.  **Positive resonance route.** Test $W_X$, then $\mathfrak P_X$, then the identical-map quotient, and only then $\mathfrak X_X$. This is the cheapest falsifiable route.

2.  **Signed native route.** Attack H3 directly in the physical affine/determinant coordinates, bypassing a failed positive majorant or continuous Mellin lower frame.

3.  **Coherent prime-square route.** Prove a coefficient-specific Bessel or dispersion estimate inside one residual coordinate, preserving the three nonsmooth coefficient slots and the physical prime weights.

The second and third routes may share exact dictionaries, but gains may be combined only when they act on disjoint costs or a theorem places them in one common carrier.

# TPC-103 through TPC-120: a verification queue

The next sequence is a decision schedule, not a claim that eighteen papers remain before a proof. Each item may produce a positive theorem, a route-switching obstruction, or a sharper formulation of the next gate.

<div id="tab:queue">

| Paper | Working title                                    | Decisive deliverable                                                                                              |
|:------|:-------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| 103   | Normalized opened-atom cap                       | Prove or refute $W_X\le X^{o(1)}$ from the literal factor list.                                                   |
| 104   | Resolved principal-mass disintegration           | Open $\mathfrak P_X$ before width grouping; return $N=1,2$ exactly.                                               |
| 105   | Provenance-preserving affine-map quotient        | Aggregate identical maps without losing source recovery or weight.                                                |
| 106   | Width-weighted distinct-map incidence            | Test the positive $\mathfrak X_X$ target on genuine distinct maps.                                                |
| 107   | Signed filter before positive majorization       | Construct the exact signed replacement if TPC-104 or 106 stops.                                                   |
| 108   | Literal generic-affine Möbius dispersion         | Attempt the restricted $X^{-1/200}$ $TT^*$ gain in H3.                                                            |
| 109   | Coherent prime-square block test                 | Seek a coefficient-specific saving or a saturation theorem on one actual residual block.                          |
| 110   | Post-bin determinant energy on actual support    | Prove a natural-scale lower bound or an actual energy obstruction.                                                |
| 111   | Distinguished zero-mode cancellation             | Estimate $Z_X$ independently of the energy census.                                                                |
| 112   | Determinant–zero compatibility audit             | Test $\lambda_D\le2\eta_Z$ with no double charging.                                                               |
| 113   | Canonical physical frame and reassembly          | Measure the inherited synthesis cost or prove a condition-number lower bound.                                     |
| 114   | Residual grouping and native-Gram identification | Control $s=d(m)r$ and prove the exact Gram intertwining.                                                          |
| 115   | Fixed-$h_0$ de-aliasing and localization         | Return frozen and frequency-averaged estimates to one prescribed shift.                                           |
| 116   | High-frequency and ultra-tail closure            | Return the complete complement at the original normalization.                                                     |
| 117   | TPC-18 full-block physical remainder             | Prove exact cover or estimate the physical remainder.                                                             |
| 118   | Strict endpoint optimization                     | Assemble a nonduplicated loss ledger and require $<1/400$.                                                        |
| 119   | Original hard-packet reconnection                | Audit H8 against the TPC-15 scalar packet.                                                                        |
|       |                                                  |                                                                                                                   |
| MVP2  | Global route decision                            | Insert proved gates, declare failed routes, and decide whether a conditional closure implementation is justified. |

: A falsifiable verification queue after TPC-MVP1.

</div>

## Why the inexpensive gates come first

TPC-103–106 concern positive or exact literal quantities. They can often be settled by factor bookkeeping, exact disintegration, or a counterexample before a deep arithmetic theorem is attempted. TPC-108 is deliberately delayed: proving a sophisticated affine Möbius estimate is wasteful if the positive normalization or the final synthesis already has a polynomial obstruction.

## Promotion checkpoints

The queue has four formal checkpoints.

1.  After TPC-106, choose positive or signed resonance.

2.  After TPC-112, decide whether determinant transfer remains viable.

3.  After TPC-117, decide whether the literal full-block carrier exists with a controlled remainder.

4.  At TPC-118, stop unless the physical loss is strictly below $1/400$. Only then may TPC-119 reconnect to the original scalar packet.

TPC-MVP2 is not scheduled as a proof announcement. It is a new audit that may conclude “go”, “reroute”, or “current endpoint infeasible”.

# Publication-worthy negative outcomes

The architecture is useful even if a main route fails, provided the failure is mathematical rather than autobiographical. The following would be legitimate standalone outcomes when proved on actual coefficients:

1.  a polynomial opened-atom concentration theorem;

2.  a sharp principal-mass obstruction to the positive majorant;

3.  a literal example showing that positive majorization destroys a signed cancellation present before the filter;

4.  a canonical frame condition-number lower bound;

5.  an equivalence or no-reduction theorem between the generic affine gate and a prescribed-shift Chowla-type input;

6.  determinant energy and zero-mode incompatibility on an actual family;

7.  an average-to-fixed-$h_0$ localization obstruction;

8.  an actual-support remainder obstruction to full-block cover;

9.  a proof that the present parameter geometry forces $\Lambda_{\mathrm{phys}}\ge1/400$; or

10. nonidentifiability of the required physical Gram from the available surrogate Gram.

> **Remark: Failure to prove is not a theorem** Computational saturation, a stalled argument, or the absence of a known estimate is not a stop certificate. A negative paper requires an exact family, lower bound, kernel, counterexample, or logical nonimplication with the physical typing visible.

## Weaker positive outputs

If a fixed-$h_0$ gate remains open, the same methods may yield valuable but strictly qualified results:

-   averaged-shift or density-one-shift cancellation;

-   a fixed-power gain on a literal selected block;

-   a density-one cofactor range;

-   a theorem after smoothing or freezing one coefficient slot;

-   a complete classification of saturating resonance families; or

-   a parameter range in which the endpoint is feasible.

These results may be publishable. They remain $\mathrm{L0}/\mathrm{L1}$ or a restricted arithmetic theorem unless a fixed-$h_0$ return is proved.

## A portfolio rather than a single bet

The MVP program therefore has three kinds of success:

1.  a gate closes and the dependency graph advances;

2.  a gate fails by a sharp theorem and an entire false route is retired; or

3.  the literal audit reveals a better carrier on which a new route can be formulated.

What it does not permit is indefinitely renaming the same unresolved arithmetic cancellation.

# Finite route audit

The standard-library script `experiments/tpc_mvp1_route_audit.py` encodes the dependency graph used in this paper. It audits 98 recorded items:

-   19 nodes are typed as established, hypothetical, or conditional;

-   all 18 declared dependency edges have valid endpoints and the graph is acyclic;

-   all nine hypotheses are ancestors of the conditional Hardy–Littlewood node;

-   no established node is labeled $\mathrm{L2}$;

-   all ten route gates contain nonempty go, stop, and fallback records;

-   the TPC-103–120 queue is consecutive and has 18 entries; and

-   five rational identities in the scale and endpoint ledgers are exact.

The committed output is `experiments/tpc_mvp1_route_audit.json`.

In particular the audit checks $$\frac{267}{400}+\frac{133}{400}=1, \qquad \frac{267}{800}-\frac{67}{400}=\frac{133}{800},$$ $$\frac1{200}=2\cdot\frac1{400}, \qquad \frac1{400}-\frac1{500}=\frac1{2000}>0.$$ The sample $1/500$ is only a consistency witness for strict endpoint slack, not a proved physical loss.

> **Remark: Certificate scope** The route audit verifies graph syntax, claim typing, and rational bookkeeping. It does not test H1–H9, asymptotic Möbius cancellation, prime-pair data, or the plausibility of a parity breakthrough. A passing finite audit is $\mathrm{L0}$ evidence only.

# Claim boundary and final verdict

## **\[E\]** Established in the imported series

-   The fixed-shift target has an exact hard-packet anchor.

-   Important sectors possess literal native dictionaries and exact determinant/resonance decompositions.

-   Two exceptional literal resonance branches are returned at their recorded endpoint scale within the present low-window decomposition and native normalization.

-   The remaining positive resonant carrier satisfies the three-ledger inequality [\[eq:three-ledger\]](TPC-MVP1.md#ref-9f7632b90811001e).

-   Several false transfers and coefficient-blind shortcuts have rigorous countermodels.

-   Full-block return, generic arithmetic dispersion, determinant/zero-mode compatibility, and the physical endpoint are separately required gates.

## **\[H\]** Explicitly assumed here

H1–H9 are working hypotheses. In particular, no established result currently supplies the growing fixed-$h_0$ signed affine Möbius estimate H3, the complete physical return H6, or the full strict endpoint statement H9.

## **\[C\]** Proved conditionally

If H1–H9 all hold in one literal normalization, then the hard packet is $o(X)$, the weighted Hardy–Littlewood asymptotic follows, and a nonnegative weight gives a fixed-gap prime-pair lower bound. The specialization $h_0=2$ is a conditional corollary only.

## **\[N\]** Not established

TPC-MVP1 does not establish:

-   any new $\mathrm{L2}$ growing fixed-$h_0$ arithmetic estimate;

-   H1–H9, individually or jointly;

-   that the hypothesis stack is weaker than, or independently easier than, the original hard packet;

-   a sieve-parity breakthrough, Hardy–Littlewood asymptotic, prime-pair lower bound, or twin-prime theorem;

-   a Riemann-hypothesis consequence or a zeta-zero spectral realization; or

-   a numerical measure of how close the program is to a proof.

## Current honest verdict

After 102 technical papers, the program has enough verified structure to state an end-to-end candidate conditional route with all currently identified edges shown. That is a meaningful change: the maze now has named doors, dependency arrows, kill criteria, and fallback corridors. It is not the same as having opened the parity-facing door.

The immediate rational strategy is therefore: $$\begin{gathered} \text{cheap literal kill tests}\\[-0.2em] \Longrightarrow\ \text{positive or signed resonance decision}\\[-0.2em] \Longrightarrow\ \text{first genuine fixed-\(h_0\) arithmetic attack}\\[-0.2em] \Longrightarrow\ \text{physical return and endpoint audit}. \end{gathered}$$ If any actual-coefficient obstruction closes a corridor, that negative theorem is part of the program’s success. If the corridor remains open, the next paper must prove a quantitative statement at its own declared level; it may not substitute another representation for the same unresolved cancellation.

# References (preserved BibTeX)

Bibliography source: references.bib

```bibtex
@article{HardyLittlewood1923,
  author  = {Hardy, G. H. and Littlewood, J. E.},
  title   = {{Some Problems of Partitio Numerorum. III. On the
             Expression of a Number as a Sum of Primes}},
  journal = {Acta Mathematica},
  volume  = {44},
  pages   = {1--70},
  year    = {1923}
}

@book{FriedlanderIwaniec2010,
  author    = {Friedlander, John and Iwaniec, Henryk},
  title     = {{Opera de Cribro}},
  publisher = {American Mathematical Society},
  address   = {Providence, RI},
  year      = {2010}
}

@misc{WangTPC1,
  author = {Wang, Liang},
  title  = {{Two-Scale Correlations in Finite Prime-Sieve Dynamics:
            Singular Series, Repair Stability, and a Local-Information
            Boundary}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-1-two-scale-prime-sieve-correlations}
}

@misc{WangTPC15,
  author = {Wang, Liang},
  title  = {{Fixed-Shift Local Models within the Square-Root
            Distribution Range: Quarter-Scale Row Masks, Ramanujan
            Spectral Calibration, and a Vaughan Type-II Reduction}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-15-fixed-shift-local-models}
}

@misc{WangTPC18,
  author = {Wang, Liang},
  title  = {{Two Quadraticizations of a M{\"o}bius Tail: LCM Cutoff
            Return, Generic Row Determinants, and Nonprimitive
            Endpoint Collapse}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-18-mobius-tail-determinant-dispersion}
}

@misc{WangTPC28,
  author = {Wang, Liang},
  title  = {{Joint Before Centering at a Poisson-Long Base:
            Full-Rectangle Exact Conductors and High-Beta Initial-Value
            Closure}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-28-joint-before-centering}
}

@misc{WangTPC32,
  author = {Wang, Liang},
  title  = {{Matched Prime--M{\"o}bius Cutoff Shells: Rank--Two
            Factorization, Determinant--Frequency Dispersion, and the
            Distinguished Zero--Frequency Gate}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-32-matched-cutoff-frequency-gate}
}

@misc{WangTPC50,
  author = {Wang, Liang},
  title  = {{Fixed-Complexity Cell Survival and Sharp Concentration
            Obstructions for the TPC Static Mask}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-50-fixed-complexity-cell-survival}
}

@misc{WangTPC51,
  author = {Wang, Liang},
  title  = {{Canonical Mellin Quotient Frames: Finite-Sampling
            Kernels, Interior Stability, and the Boundary of Signed
            TPC Reassembly}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-51-canonical-mellin-quotient-frames}
}

@misc{WangTPC70,
  author = {Wang, Liang},
  title  = {{Primitive Cofactor Coordinates for Two-Key Erasure
            Rectangles: Divisor Compression, Frozen Prime Rays, and
            the Residual M{\"o}bius Plane}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-70-primitive-cofactor-plane}
}

@misc{WangTPC81,
  author = {Wang, Liang},
  title  = {{A Fixed-Shift Arithmetic Transfer Gap: From Literal
            Completion Certificates to Zero-Frequency Flatness}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-81-fixed-shift-arithmetic-transfer-gap}
}

@misc{WangTPC82,
  author = {Wang, Liang},
  title  = {{A Ten-Paper Fixed-Shift Completion-to-Flatness Audit:
            Exact Certificate Closures, the Determinant-Energy Gate,
            and a Zero-Slack Endpoint Ledger}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-82-ten-paper-completion-to-flatness-audit}
}

@misc{WangTPC87,
  author = {Wang, Liang},
  title  = {{The Sharp Logarithmic Tauberian Gap: Signed Ces\`aro
            Defects, Dyadic Countermodels, and the Literal Fixed-Shift
            Affine Gate}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-87-sharp-logarithmic-tauberian-gap}
}

@misc{WangTPC90,
  author = {Wang, Liang},
  title  = {{Primitive Affine Local-Obstruction Splitting at a Fixed
            Determinant: Squarefree Support, Exact Root Counts, and
            the Remaining Liouville Parity Correlation}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-90-primitive-affine-local-obstruction-split}
}

@misc{WangTPC91,
  author = {Wang, Liang},
  title  = {{Overlap-Corrected Full-Block Cover Certificates:
            Incidence Geometry, Dual Obstructions, and the TPC-18
            Interface}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-91-overlap-corrected-full-block-cover}
}

@misc{WangTPC92,
  author = {Wang, Liang},
  title  = {{A Ten-Paper Mass--Cancellation--Cover Audit: Exact
            Closures, Independent Arithmetic Gates, and a Stop/Go
            Roadmap}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-92-ten-paper-mass-cancellation-cover-audit}
}

@misc{WangTPC93,
  author = {Wang, Liang},
  title  = {{Literal Low-Window Affine Export: Content-Factor
            Extraction, Resonance Sectors, and Fixed-Determinant
            Preservation}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-93-literal-low-window-affine-export}
}

@misc{WangTPC96,
  author = {Wang, Liang},
  title  = {{Anchored Logarithmic Primitives on Translated Fibers:
            Exact Tauberian Defects, Uniformity Regimes, and the Literal
            Reassembly Gate}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-96-anchored-tauberian-translation-defect}
}

@misc{WangTPC98,
  author = {Wang, Liang},
  title  = {{The Literal Constant-Phase Sector at the Strong No-Wrap
            Prime: Orbit Sparsity and an Endpoint-Scale Literal
            Bound}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-98-long-constant-phase-orbit-sparsity}
}

@misc{WangTPC99,
  author = {Wang, Liang},
  title  = {{Multiplicative Resonance Incidence at the No-Wrap Prime:
            Exact Character Spectrum, Parity Nullspace, and the
            Native Dispersion Gate}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-99-multiplicative-resonance-incidence}
}

@misc{WangTPC100,
  author = {Wang, Liang},
  title  = {{Invertible Ultra-Divisor Linearization on the
            Nonconstant Branch: Exact Orbit Preimages, Diagonal Cell
            Energy, and the Cross-Cell Gate}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-100-invertible-ultra-multiplier-linearization}
}

@misc{WangTPC101,
  author = {Wang, Liang},
  title  = {{Wiener-to-Hilbert--Schmidt Transfer for Multiplicative
            Resonance: Width-Sensitive Dispersion and the
            Long-Fiber Gate}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-101-wiener-hilbert-schmidt-resonance}
}

@misc{WangTPC102,
  author = {Wang, Liang},
  title  = {{Literal Resonance after TPC-101: Verified Branch
            Closures, the Three-Ledger Master Inequality, and a
            Stop--Go Roadmap}},
  year   = {2026},
  note   = {Preprint},
  url    = {https://github.com/maris205/prime_dynamics_theory/tree/main/papers/tpc-102-literal-resonance-stage-audit}
}
```
<!-- SOURCE_BODY_END -->
