---
type: "source-reading"
source_path: "synthesis/seven-island-monograph/paper-en/main.md"
snapshot_date: "2026-09-12"
owner: "SYNTHESIS-EN"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- MATHJAX_CAUTION -->
> [!warning] 公式显示兼容性
> 此文有 2 处公式未通过服务端MathJax兼容性检查；原始TeX仍完整保留。请对照 [逐项记录](../99_%E7%BB%B4%E6%8A%A4/%E5%85%AC%E5%BC%8F%E6%98%BE%E7%A4%BA%E5%85%BC%E5%AE%B9%E6%80%A7.md#note-202bafedd146e06c) 和原PDF，不将显示错误当作数学结论。


<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/synthesis/seven-island-monograph/paper-en/main.md.txt)；可用外部编辑器核对。


> [!info] 阅读范围
> 2026-09-12 English synthesis; full translation, not a new mathematical result.

[[00_开始阅读|首页]] · [[05_综合与进展/历史总结校注|历史与当前状态的区别]]

# A Seven-Island Framework for Twin-Prime Research

Exact Structures, Analytic Obstructions, and Two Bridging Problems

Complete English synthesis. The [PDF](../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/synthesis/seven-island-monograph/paper-en/main.pdf) is authoritative for equation numbering and layout; citation keys refer to the [bibliography](../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/synthesis/seven-island-monograph/paper-en/references.bib).

## Abstract

We organize a collection of fixed-shift prime-pair investigations into seven modules: arithmetic foundations, analytic cancellation, fixed atoms, actual-occurrence structures, nonautonomous dynamics, the twin-prime endpoint, and auxiliary geometric lifts. The purpose is to distinguish established structures from transfers that still require arithmetic input, while keeping the objects, quantifiers, and normalizations consistent. The analytic core is an arithmetic operator retaining unit masks, a smooth kernel, and diagonal deletion. We restate and prove its exact positive-form decomposition, norm and row-energy bounds, and the restrictions that the actual coefficient norms impose on coefficient-blind methods. At interval scale $x$ and prime-modulus scale $Q=x^{1/3}$, a low-frequency compression yields $(1/4+o(1))Q^2$ negative directions. An exact Kloosterman representation explains why one-sided short support does not automatically supply a two-sided critical-range estimate. For an explicitly constructed smooth partition, the collective boundary contribution is bounded by $xQ^2x^{-11/64+o(1)}$. On the dynamical side, the Chinese remainder theorem and Abel summation give a linear variance bound and Haar-almost-everywhere infinite recurrence for the actual moving sieve events, while leaving the return to the distinguished arithmetic seed $0$ unproved. These results establish neither the required signed interior cancellation nor the twin-prime conjecture. They provide a source-traceable synthesis of structures and obstructions that separates two unresolved bridging problems from the available results.

**Keywords:** twin primes; Möbius correlations; reduced residue classes; Gram operators; Kloosterman sums; distinguished seeds.

# Introduction: a common problem behind local results

The twin-prime problem asks for infinitely many prime pairs at the fixed displacement $2$. Producing an expression that resembles a correlation sum, or a finite matrix with a small norm, is not enough. If a method transfers the original counting problem to another space, its coefficients, support, quantifiers, and normalization must travel with it. Omitting any of these can produce a correct statement that does not apply to the original problem.

The research archive contains successive local investigations numbered TPC1–TPC418, together with prototypes, source-unavailable markers, and later unnumbered work. Its development was problem-driven: an obstruction motivated a different representation, and a source audit sometimes required the actual object to be identified again. A chronological condensation would preserve this history without necessarily preserving the mathematical dependencies. We instead use Figure [1](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-98cc21c714717829) as a shared coordinate system and reconstruct a readable argument, leaving material outside that argument in a traceable companion index.

###### ref-98cc21c714717829

![The user’s English seven-island map, reproduced unchanged. Islands name objects and tasks, not completed steps. Solid and dashed connections depict proposed main and auxiliary routes; broken bridges indicate unproved transfers, not impossibility for every method. Schematic labels and formulae do not certify isomorphisms, positive savings, or twin-prime asymptotics: the hypotheses and qualifications in the text govern all mathematical claims. In particular, rare-event mass does not establish recurrence at the arithmetic seed. Map Bridge A contains both archive Gate A and Gate B; map Bridge B is the distinguished-seed dynamical bridge, not a filename containing “Bridge-B.” Enlarge the image for small labels; an identical full-resolution companion is supplied.](../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/synthesis/seven-island-monograph/paper-en/figures/tpc_route_en.png)

## One framework, two substantive gaps

The analytic route seeks to pass from local correlation structure to signed collective cancellation with the complete coefficients. One target considered here has natural scale $xQ^2$. To be an effective input to the specified endpoint interface, it must exhibit a power saving strictly exceeding $1/400$. Exact identities preserve the object but do not themselves supply that saving. Islands 3 and 4 concern the identification of local atoms and actual occurrences; Island 2 concerns the required estimates.

The dynamical gap is different. Adequate event mass and covariance control in an encoding system do not show that the particular orbit selected by arithmetic belongs to the good set. A statement about almost every initial point need not hold at a prescribed one. Calling that point “typical” cannot remove the quantifier gap. A geometric lift that merely changes the representation cannot supply the missing input either.

## Results retained in this synthesis

The analytic exposition develops four groups of statements that can be checked separately:

1.  An exact decomposition and row-energy bounds for the actual operator, under specified fixed-shift coefficients, unit masks, and kernel conventions, without substituting a model matrix.

2.  A constant-vector norm lower bound, lower bounds for the actual coefficient norms, and a growing-dimensional obstruction to low-rank repairs. These restrict particular bounding methods, not the size of the actual mixed scalar.

3.  An exact full-range Kloosterman representation and the norm of a one-short/one-complete array interface, separating algebraic representation, support compression, and signed reassembly.

4.  An explicit partition with uniform derivative control and a paid collective boundary bound in the original mixed scalar, leaving the signed interior estimate open.

The dynamical section additionally gives the $O(N)$ variance and Haar-almost-everywhere infinite-recurrence proof for the actual moving sieve events, separately from the unproved assertion at seed $0$. These are unified statements and reorganized proofs of archived results; no first-discovery or optimality claim is made. The appendix distinguishes the evidentiary roles of earlier finite certificates and later growing-model results, rather than counting them as savings for the actual arithmetic problem.

## Relation to existing mathematical inputs

Our prime-counting input is the classical prime number theorem and its partial-summation consequences [\[\@selberg1949\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-d546b7aa9ddb4d3c). The second-moment estimate for the hybrid coefficient uses the unconditional Mertens product baseline, stated at the beginning of [\[\@lamzouri2015\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-839bc50119180e6c); none of that paper’s conditional conclusions on bias distributions is used. Frequency separation, positive-semidefinite compression, finite Fourier orthogonality, and spectral min–max arguments are standard tools in the structural proofs, not new prime-pair theorems.

The critical-interval bilinear estimate of Blomer–Pascadi [\[\@blomer2026\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-cee6b8e4496327ac) supplies an external benchmark: with the appropriate lengths and coprimality conditions, a Kloosterman bilinear form admits a local power saving. We use only the square-root-length specialization of their Theorem 1.1 and examine whether the actual representation satisfies its input conditions. The existence of that theorem is not an estimate for the complete arithmetic expression.

This article is not an exhaustive literature survey, and the number of internal documents is not a substitute for comparison with external work. It is a mathematical synthesis draft for a delimited research program. Submission would still require contribution positioning, a fuller bibliography, verification of all selected historical dependencies, and independent mathematical scrutiny of the complete argument.

## Reading guide

Section [2](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#The%20arithmetic%20endpoint%2C%20quantifiers%2C%20and%20division%20of%20tasks) fixes the endpoint and the transfer requirements. Section [3](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#Fixed%20atoms%20and%20actual%20occurrences%3A%20Islands%203%20and%204) treats the fixed atom and occurrence interfaces. Sections [4](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#The%20analytic%20core%3A%20the%20actual%20operator%20and%20its%20exact%20structure)–[7](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#A%20paid%20component%3A%20constructive%20partitioning%20and%20the%20boundary%20contribution) develop the analytic core on one common object. Section [8](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#Islands%205%20and%207%3A%20moving%20targets%2C%20a%20distinguished%20seed%2C%20and%20geometric%20attachment) separates metric recurrence, the distinguished seed, and geometric attachment. Section [9](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#The%20two%20bridges%3A%20conditional%20ledgers%20and%20conclusions) assembles the two conditional bridge ledgers. The appendices distinguish model evidence and document provenance. Readers need not read every historical manuscript in sequence to understand the main text; exact sources, material not selected for this synthesis, and the scope of review can be found in the accompanying source matrix and full catalog.

# The arithmetic endpoint, quantifiers, and division of tasks

## The endpoint and auxiliary quantities

Write $\pi_2(y)=\#\{p\le y:p,p+2\text{ are both prime}\}$. The endpoint is $\pi_2(y)\to\infty$, not the discovery of more pairs in a finite interval. A customary weighted auxiliary quantity is $$S_2(y)=\sum_{n\le y}\Lambda(n)\Lambda(n+2),$$ where $\Lambda$ denotes the von Mangoldt function. An asymptotic such as $S_2(y)\sim cy$ with $c>0$ would imply infinitely many twin primes. This is a sufficient condition, not an asymptotic proved here.

To justify the implication, one must remove proper prime powers. There are $O(\sqrt y\log y)$ pairs in which at least one coordinate is $p^k$ with $k\ge2$, and each weight is $O(\log^2y)$. Their total contribution is $o(y)$. Finitely many genuine prime pairs cannot account for a positive linear main term. Even for a standard auxiliary quantity, its connection to the endpoint should therefore be stated rather than inferred from its name.

## Island 1: local sieve factors versus prime-pair counts

For $y\ge2$, put $P_y=\prod_{p\le y}p$, $s_y(n)=\mathbf 1_{(n,P_y)=1}$, and $\rho_y=\prod_{p\le y}(1-1/p)$. Let $\mathcal H=\{h_1,\ldots,h_r\}\subset\mathbb Z$ be a fixed finite nonempty set of distinct shifts, and let $\nu_p(\mathcal H)$ count its distinct residues modulo $p$. The Chinese remainder theorem (CRT) gives $$C_y(\mathcal H):=\frac1{P_y}\sum_{n\bmod P_y}\prod_{h\in\mathcal H}s_y(n+h) =\prod_{p\le y}\left(1-\frac{\nu_p(\mathcal H)}p\right).$$ Indeed, there are $p-\nu_p(\mathcal H)$ allowed classes at each prime, and CRT multiplies these counts. If $\mathcal H$ is admissible, meaning $\nu_p<p$ for every prime, then $\nu_p=r$ for all sufficiently large $p$. The normalized factor is $(1-r/p)(1-1/p)^{-r}=1+O_r(p^{-2})$, so the product converges. In particular, $$\frac{C_y(\{0,2\})}{\rho_y^2}\longrightarrow2C_2,\qquad C_2=\prod_{p>2}\frac{p(p-2)}{(p-1)^2}>0.$$ This is a classical local calculation, not a new prime-pair asymptotic [\[\@archive1\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-c82451d4ba11923a).

Translate $\min\mathcal H$ to zero, set $h_{\max}=\max\mathcal H$, and let $X\to\infty$. If $Y_X=\sqrt{X+h_{\max}}$ and $Y_X<n\le X$, then every $n+h$ exceeds $Y_X$ and is at most $Y_X^2$. These integers survive the sieve through $Y_X$ if and only if they are all prime. This is a pointwise identification, not an estimate for the number of survivors. By contrast, complete-period decomposition on $1\le n\le X$ only gives $$\left|\sum_{1\le n\le X}\prod_{h\in\mathcal H}s_y(n+h)-XC_y(\mathcal H)\right|\le P_y+1.$$ Complete periods contribute exactly; the remaining partial period costs at most $P_y$, with an additional $1$ for a noninteger endpoint. If $P_y=o(X\rho_y^r)$, this bound makes the normalized error vanish. At the primality-exact cutoff, however, the prime number theorem gives $\log P_{Y_X}\sim\sqrt X$, so this error bound provides no useful relative control. This is a mismatch between two elementary arguments, not an impossibility theorem for all sieve methods.

## The seven islands are not a serial proof

| Island | Object or task            | Transfer still requiring identification in this framework                                            |
|:------:|:--------------------------|:-----------------------------------------------------------------------------------------------------|
|    1   | Arithmetic foundations    | Preserve the original counting interpretation when starting from sieves, correlations, or encodings. |
|    2   | Analytic cancellation     | Pass from local structure to a signed saving for the complete actual coefficients.                   |
|    3   | Fixed atoms               | Control the specified shift, phase, and packet pointwise.                                            |
|    4   | Actual occurrences / H1   | Supply complete carriers, source correspondences, multiplicities, and coefficientwise conservation.  |
|    5   | Nonautonomous dynamics    | Pass from a measure statement to recurrence at the specified arithmetic seed.                        |
|    6   | Twin-prime endpoint       | Obtain infinitely many genuine prime pairs, not a model statement or finite certificate.             |
|    7   | Auxiliary geometric lifts | Preserve time and event readout, without assuming arithmetic genericity for free.                    |

: Division of mathematical tasks. The final column does not assert necessary conditions for every possible route.

## What every transfer must retain

To compare expressions from different stages, we record a source specification as $$\begin{split} \mathcal O=(&\text{coefficients},h_0,\text{support and order},\text{parameter range},\\ &\text{quantifiers},\text{normalization},\text{loss budget}). \end{split}$$ This is bookkeeping against misapplication, not a new mathematical object. Similar notation does not imply equal specifications. An arbitrarily large CRT origin is not an origin in the prescribed physical interval; a prefix of a full prime shell is not an arbitrary prime selection; recomputing local row energy is not compressing the original normalized matrix.

We distinguish four evidence types: finite identities verified by expansion; uniform propositions with complete hypotheses and proofs; conditional consequences retaining their unproved premises; and finite numerical diagnostics. Diagnostics do not carry infinite quantifiers, and a successful program check does not make a conditional implication unconditional. The results below should be read in this hierarchy, not by their order of appearance in the archive.

# Fixed atoms and actual occurrences: Islands 3 and 4

This layer identifies the object to which a downstream estimate must apply. A fixed displacement, phase, modulus, and support are four distinct requirements; estimating a convenient substitute does not settle them.

## The order-preserving determinant-two pullback

Let $I$ be an integer interval, $a,s$ positive integers, and $d,u$ integers satisfying $$\begin{gathered} D(z)=d+sz>0,\quad V(z)=u+az>0\quad(z\in I),\quad su-ad=2,\\ (a,s)=1,\quad(as,2)=1,\quad(d,s)=(u,a)=1. \end{gathered}$$ Write $\lambda$ for the Liouville function, distinct from the truncated projector weight below. Let $B,\tau$ be the specified integers and $\chi,W_X$ the functions prescribed by the original block. Its literal coefficient is $$a_{\xi,X}(z)=\mu(D(z))\mu(V(z))\mathbf 1_{(B,V(z))=1}\chi(\tau+Bz)W_X(\tau+Bz).$$

###### ref-451bc17a5c8f4880

\[prop:pullback\] Set $q_{\rm prog}=as$ and $n(z)=su+as z=sV(z)=aD(z)+2$. This is an order-preserving bijection from $I$ onto its image $\mathcal N_I$, and $$\begin{aligned} \mu(D(z))\mu(V(z))&=\lambda(q_{\rm prog})\lambda(n-2)\lambda(n)\mathcal Q_{a,s}(n),\\ \mathcal Q_{a,s}(n)&=\mu^2((n-2)/a)\mu^2(n/s).\end{aligned}$$ For every $\alpha\in\mathbb R$, the original sum is therefore exactly $$\sum_{z\in I}a_{\xi,X}(z)\mathrm e(-\alpha z) =\lambda(q_{\rm prog})\sum_{n\in\mathcal N_I} \lambda(n-2)\lambda(n)\mathcal Q_{a,s}(n)\mathcal W_{\xi,X}(n)\mathrm e(-\alpha z(n)),$$ where $\mathcal W_{\xi,X}(n)=\mathbf 1_{(B,n/s)=1}\chi(\tau+Bz(n))W_X(\tau+Bz(n))$. The same identity holds for every initial prefix.

The positivity of $as$ gives order preservation, and $su-ad=2$ gives the two integer quotients. Since $\mu(m)=\mu^2(m)\lambda(m)$ and $\lambda$ is completely multiplicative, $\lambda(n-2)\lambda(n)=\lambda(a)\lambda(s)\lambda(D(z))\lambda(V(z))$. Multiplying by $\lambda(as)$, whose square is $1$, proves the coefficient identity. Substitute all remaining factors unchanged, without taking absolute values or removing the quotient-squarefree masks. The increasing bijection maps each initial prefix to its corresponding prefix.

This is the core interface of TPC127 [\[\@archive127\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-ba84fa480e1f8780). It also preserves variation along consecutive image points and absolute comparison mass, but does not estimate either quantity. Fixing $h_0=2$ neither fixes one phase across scales nor permits the quotient-squarefree conditions to be discarded.

## Ordered pairs, child reassembly, and occurrence conservation

Squaring a sum produces ordered row pairs, a different carrier from the pair of affine forms above. For example, in the opened-$D$ construction, $N_\alpha(j)=\ell_\alpha d_\alpha j+h_0$, and the off-diagonal coefficient contains $$\mu(d_\alpha)\mu(d_\gamma)(\log\ell_\alpha)(\log\ell_\gamma) r_R(N_\alpha(j))r_R(N_\gamma(j))B_\alpha(j)B_\gamma(j).$$ Here $r_R$ and $B_\alpha$ denote the truncation factor and row-weight aliases in the source expansion. They are not newly defined free functions, and the display does not attach an actual production pair to an affine atom. The complete TPC18 formula is located in the source matrix. Attachment to a retained atom must still preserve the original joint mask, schedule, and normalization.

For a legitimately retained source term, divisor decomposition gives a useful conservation identity. For $G>0$, set $$\lambda_G(v)=\sum_{g\mid v,\ g\le G}\mu(v/g).$$ Then, for positive integers $d,e$, $$\sum_{v\mid(d,e)}\lambda_G(v)=\mathbf 1_{(d,e)\le G}.$$ Interchange $g,v$ and use $\sum_{h\mid m}\mu(h)=\mathbf 1_{m=1}$ to prove the identity. Reconstructing the source requires the weighted sum of all children; one child is not the source coefficient. TPC93’s inverse and signed reconstruction hold on its squarefree primitive support. TPC205’s composition from production pairs remains conditional on a legitimate attachment [\[\@archivestructure\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-a3b2405ec2cee411).

A linear occurrence lift is a separate issue. The source labels $\mathsf{EPS}$, $\mathsf{ETO}$, and $\mathsf{FUM}$ mean eligible-prefix-soft, eligible-tail-open, and frontier-unmapped. The nonsoft domain is $\mathcal C=\mathcal C^{\mathsf{ETO}}\sqcup\mathcal C^{\mathsf{FUM}}$; retaining only the frontier would omit the eligible tail. If the upstream cut satisfies $$\mathbf 1_{\mathsf{EPS}}^TM^{\mathsf{EPS}}+\mathbf 1_{\mathcal C}^TM^{\rm ns}=\mathbf 1_{\mathcal N}^T,$$ and a supplied lift $L:\mathbb C^{\mathcal C}\to\mathbb C^{\mathcal O}$ satisfies $\mathbf 1_{\mathcal O}^TL=\mathbf 1_{\mathcal C}^T$, multiplication gives $$\mathbf 1_{\mathsf{EPS}}^TM^{\mathsf{EPS}}+\mathbf 1_{\mathcal O}^TLM^{\rm ns}=\mathbf 1_{\mathcal N}^T.$$ The sets $\mathcal N,\mathcal C,\mathcal O$ are respectively native terms, nonsoft branches, and retained occurrences with source paths. A retained carrier is not the certified nonzero active support: after inverse aggregation, the literal coefficient must still be certified nonzero. An unevaluated coefficient cannot simply be declared zero. This conditional statement does not construct $L$; row separation, metadata fidelity, and the actual nonzero support must also be supplied. A formal support envelope is not the actual occurrence set.

## A weighted-cover criterion

Suppose the actual coefficient vector $c_{\rm phys}$ and admissible-block synthesis matrix $B$ have been supplied, with the specified positive-definite inner products on both spaces. Let $B^\dagger$ be the corresponding Moore–Penrose inverse and $P=BB^\dagger$.

In finite dimensions, the following are equivalent: $$c_{\rm phys}\in\operatorname{Ran}B,\qquad Pc_{\rm phys}=c_{\rm phys},\qquad \langle y,c_{\rm phys}\rangle=0\quad(y\in\ker B^*).$$ Moreover, $$\|(I-P)c_{\rm phys}\|= \max_{y\in\ker B^*,\ \|y\|\le1}|\langle y,c_{\rm phys}\rangle|.$$

The singular value decomposition identifies $P$ as the orthogonal projection onto $\operatorname{Ran}B$, whose orthogonal complement is $\ker B^*$. Orthogonal decomposition gives the equivalences. Cauchy–Schwarz proves the upper bound in the distance formula. A normalized nonzero residual attains equality; when the residual vanishes, both sides are zero.

This is the linear-algebraic content of the TPC117 criterion [\[\@archivestructure\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-a3b2405ec2cee411). Even if $B^\dagger c_{\rm phys}$ gives an exact cover, block bounds $U_b$ still incur the transport cost $\sum_b|(B^\dagger c_{\rm phys})_b|U_b$. The existence of a cover is not the existence of an inexpensive cover, much less an arithmetic saving for the actual growing family.

# The analytic core: the actual operator and its exact structure

Sections [4](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#The%20analytic%20core%3A%20the%20actual%20operator%20and%20its%20exact%20structure)–[7](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#A%20paid%20component%3A%20constructive%20partitioning%20and%20the%20boundary%20contribution) use one object from the fully recovered scalar specification [\[\@archivev59; \@archivephysical\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-be9fa27bed7ab906); [\[archivephysical\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-7e6f6fbcb85b6e45). Here “physical” means the arithmetic data actually prescribed by the research problem, as opposed to models in which signs, origins, or kernels may be freely selected.

## Parameters, coefficients, and kernel

###### ref-45862620c0893c3b

###### ref-8d415ec04f7ad4aa

Let $x\to\infty$ and set $$I_x=(x/2,x]\cap\mathbb Z,\quad N=\lfloor x\rfloor-\lfloor x/2\rfloor,\quad Q=x^{1/3},\quad H=x^{21/32},\quad U=x^{133/400}.$$ The older source scale is $x=2X$, so $N=X+O(1)$. Let $\mathcal Q=\{q\text{ prime}:Q<q\le2Q\}$. Fix $K>0$, put $z=(\log x)^K$, and define $$\begin{aligned} P(z)&=\prod_{p\le z}p,&W_z&=\prod_{p\le z}\frac p{p-1},& C_z&=\prod_{p>z}\left(1-\frac1{(p-1)^2}\right),\nonumber\\ b_x^{(z)}(u)&=\mathbf 1_{I_x}(u)C_zW_z\mathbf 1_{(u+2,P(z))=1} \prod_{\substack{p\mid u\\p>z}}\frac{p-1}{p-2},\label{eq:hybrid}\\ \beta(t)&=\frac{\Lambda(t)}{\log t}-\sum_{\substack{d\mid t\\d\le U}}\mu(d),\nonumber\\ w(u)&=\Lambda(u+2)-b_x^{(z)}(u).\label{eq:lanes}\end{aligned}$$ Take $x$ sufficiently large that $z\ge2$. The parameter $K$ is fixed before the threshold is chosen; no assertion is made for growing $K$. The small-prime product includes $2$, and its forbidden residue is $-2$. The symbol $\mu$ in $\beta$ is the Möbius function. Both actual coefficient vectors are real, but their signs may vary.

Fix a nonnegative real smooth function $\psi_+$ supported in $[-1,1]$ with integral $1$. Write $\mathrm e(t)=\exp(2\pi\mathrm it)$ and $$\kappa(y)=\int_{\mathbb R}\psi_+(v)\mathrm e(-vy)\,dv,\qquad K_H(h)=\kappa(h/H).$$ The profile need not be even, so $\kappa$ need not be real. Nevertheless, $\kappa(-y)=\overline{\kappa(y)}$ and $\kappa(0)=1$. The kernel is Schwartz, not identically zero for $|h|>H$. Reflection, $\psi_+(v)=\psi(-v)$, reconciles this convention with the older positive-sign Fourier convention.

## The complete scalar and row energy

###### ref-127753b266e4e0f3

Set $a_q=q/(q-1)$ and define, on $\ell^2(I_x;\mathbb C)$, $$A_q(u,t)=a_q\kappa((u-t)/H) \big((q-1)\mathbf 1_{q\mid u-t}-1\big)\mathbf 1_{q\nmid u}\mathbf 1_{q\nmid t}\mathbf 1_{u\ne t}, \qquad A=\sum_{q\in\mathcal Q}A_q.$$ With $\langle f,g\rangle=\sum\overline f g$, the target scalar is $$\mathfrak C_x=\langle w,A\beta\rangle =\sum_{q\in\mathcal Q}q\sum_{\substack{u,t\in I_x\\u\ne t,\ q\nmid ut}} w(u)\beta(t)K_H(u-t)\left(\mathbf 1_{u\equiv t\ (q)}-\frac1{q-1}\right). \label{eq:scalar}$$ The outer factor $q$ is already present in the matrix definition and must not be inserted twice. The matrix is Hermitian, but its mixed scalar between two real vectors can still be complex.

###### ref-a648a0b8f79b008b

The row energy under consideration is $$G(u)=\sum_{q\in\mathcal Q}\sum_{t\in I_x}|A_q(u,t)|^2,\quad D_G=\mathop{\mathrm{diag}}(G(u)),\quad Z=D_G^{-1/2}AD_G^{-1/2}.$$ The square is taken separately at each prime; cross-prime terms are absent. Whenever every $G(u)>0$, $$\mathfrak C_x=\langle D_G^{1/2}w,Z D_G^{1/2}\beta\rangle.\label{eq:readout}$$ A smaller normalized operator norm therefore need not reduce the original scalar: the costs of both weighted vectors must also be counted.

## The reduced-residue correction

###### ref-b76a443db138528b

\[prop:decomp\] Let $r_q(n)=q\mathbf 1_{q\mid n}-1$ and define $$\begin{aligned} T(u,t)&=\kappa((u-t)/H)\sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}\mathrm e(a(u-t)/q),\\ R(u,t)&=\kappa((u-t)/H)\sum_{q\in\mathcal Q}\frac{r_q(u)r_q(t)}{q-1},\\ \Delta(u)&=\sum_{q\in\mathcal Q}a_q(q-2)\mathbf 1_{q\nmid u}.\end{aligned}$$ Then $A=T-R-\mathop{\mathrm{diag}}\Delta$ and, in positive-semidefinite order, $$R\ge0,\qquad0\le A+\mathop{\mathrm{diag}}\Delta\le T.$$

On residues modulo $q$, put $$F_q(r,s)=q\mathbf 1_{r=s}-1,\qquad S_q(r,s)=a_q\big((q-1)\mathbf 1_{r=s}-1\big)\mathbf 1_{r\ne0}\mathbf 1_{s\ne0}.$$ When both residues are nonzero, exactly one is zero, or both are zero, respectively, $F_q-S_q$ equals $1/(q-1)$, $-1$, or $q-1$. Hence $$F_q-S_q=\frac{r_qr_q^*}{q-1}.$$ Also, $F_q/q$ projects orthogonally onto the mean-zero subspace of all residues, while $S_q/q$ projects onto the subspace vanishing at zero and summing to zero over the units. Thus $0\le S_q\le F_q$.

Pullback along $I_x\to\mathbb Z/q\mathbb Z$ preserves this order and does not require equal residue multiplicities. For the diagonal matrix $D_v(n,n)=\mathrm e(-vn/H)$, $$[\kappa((u-t)/H)S_q(u,t)]_{u,t\in I_x} =\int\psi_+(v)D_vS_qD_v^*\,dv.$$ Integration against a nonnegative weight preserves the order. Sum over primes and remove the exact diagonal $S_q(n,n)=a_q(q-2)\mathbf 1_{q\nmid n}$ to conclude.

After diagonal deletion, $A$ need not be positive semidefinite. The negative directions below arise precisely at this stage. Dropping $\Delta$ during reassembly changes the problem.

# Norm scales, actual coefficient costs, and low-rank obstructions

## An upper bound from frequency separation

Fix finite constants $B_\psi,B_\kappa$ such that $$0\le\psi_+(v)\le B_\psi(1+|v|)^{-2},\qquad |\kappa(y)|\le B_\kappa(1+|y|)^{-2}.$$

###### ref-172b0b6c79d78791

\[lem:upper\] For $Q\ge2$, $$\left\|A\right\|_2\le4B_\psi(H+4Q^2)+3Q^2.$$

Distinct reduced fractions $a/q$ are separated on the circle by at least $(4Q^2)^{-1}$, including the gap across zero. The convolution kernel $\kappa(h/H)\sum_{q,a}\mathrm e(ah/q)$ on all integers has Fourier multiplier $$m(\theta)=H\sum_{q,a}\sum_{k\in\mathbb Z}\psi_+\big(H(a/q-\theta-k)\big)\ge0$$ by Poisson summation for the fixed Schwartz kernel. The points on the right are separated on the real line by at least $s=H/(4Q^2)$. Each half-open unit interval contains at most $1+1/s$ points. Splitting the positive and negative half-lines and summing $(1+j)^{-2}$ gives $m(\theta)\le4B_\psi H(1+1/s)$. Compression to $I_x$ cannot increase the norm. Proposition [\[prop:decomp\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-b76a443db138528b) gives $\left\|A+\mathop{\mathrm{diag}}\Delta\right\|_2\le\left\|T\right\|_2$, and $\max\Delta<\sum_{Q<q\le2Q}q\le3Q^2$. The claimed bound follows.

Since $H<Q^2$, the physical scales satisfy $\left\|A\right\|_2\ll_\psi Q^2$. No cancellation in $\beta,w$ is used.

## Energy of every actual row

###### ref-439da380e3fa45e9

\[prop:energy\] For the fixed kernel and every sufficiently large $x$, uniformly in $u\in I_x$, $$G(u)\asymp_\psi\frac{HQ^2}{\log Q}.$$

Continuity and $\kappa(0)=1$ give fixed $0<\rho,b\le1$ with $|\kappa(y)|\ge b$ for $|y|\le\rho$. For $q\nmid u$, put $$S_q(u)=\sum_{\substack{t\in I_x\\t\ne u,\ q\nmid t}}|\kappa((u-t)/H)|^2,\quad C_q(u)=\sum_{\substack{t\in I_x\\t\ne u,\ q\mid u-t}}|\kappa((u-t)/H)|^2.$$ Squaring gives the exact identity $$G(u)=\sum_{\substack{q\in\mathcal Q\\q\nmid u}}a_q^2 \big(S_q(u)+(q-1)(q-3)C_q(u)\big).$$ Integral comparison yields $S_q(u)\le2B_\kappa^2H/3$ and $C_q(u)\le2B_\kappa^2H/(3q)$. Since $1+(q-1)(q-3)/q\le q$, the contribution of each prime is at most $(2B_\kappa^2/3)a_q^2qH$.

If $N-1\ge2\rho H$ and $H\ge2Q/\rho$, at least one side of every row contains $\lfloor\rho H/q\rfloor\ge\rho H/(2q)$ nonzero congruent differences. Their entries are still units, and $(q-2)^2\ge q^2/9$. This prime therefore contributes at least $(\rho b^2/18)a_q^2qH$.

An integer $u\le x=Q^3$ has at most two distinct prime factors greater than $Q$. Removing the primes dividing $u$ from $S_Q=\sum_{q\in\mathcal Q}a_q^2q$ loses at most $9Q$. The prime number theorem and partial summation give $S_Q\sim(3/2)Q^2/\log Q$. Beyond a common threshold $S_Q\ge18Q$, so $$\frac{\rho b^2}{36}HS_Q\le G(u)\le\frac{2B_\kappa^2}{3}HS_Q$$ for all actual rows.

The restriction $u\le Q^3$ is essential to this argument. This is not a theorem for equal-length intervals at arbitrary huge origins or for arbitrary coordinate prefixes.

## A constant-vector witness and the actual coefficients

###### ref-e122b78aee14f006

\[thm:normbarrier\] For the fixed data of Section [4](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#The%20analytic%20core%3A%20the%20actual%20operator%20and%20its%20exact%20structure), $$\left\|A\right\|_2\ge(3/2+o(1))\frac{Q^2}{\log Q},\qquad \left\|w\right\|_2^2\sim\frac x2\log x,\qquad \left\|\beta\right\|_2^2\ge\left(\frac12\log\frac{27}{22}+o(1)\right)\frac x{\log x}.$$ Consequently, $$\liminf_{x\to\infty}\frac{\log Q}{xQ^2}\left\|A\right\|_2\,\left\|\beta\right\|_2\,\left\|w\right\|_2 \ge\frac34\sqrt{\log(27/22)}>0.$$ Any proof using only $B_x\left\|\beta\right\|_2\left\|w\right\|_2$, with $B_x\ge\left\|A\right\|_2$, cannot by itself supply a fixed positive power saving.

Let $f=N^{-1/2}\mathbf 1_{I_x}$. Before diagonal deletion, the positive form is $$\langle f,(A+\mathop{\mathrm{diag}}\Delta)f\rangle=\frac1N\sum_q q\int\psi_+(v)V_q(v/H)\,dv,$$ where $V_q(\alpha)$ is the sum of squared deviations of the unit-residue sums $\sum_{n\equiv r(q),\,n\in I_x}\mathrm e(\alpha n)$ from their mean over the units. It is not further divided by $q-1$. Write $I_x=\{a+1,\ldots,a+N\}$ and $N=mq+s$, $0\le s<q$, and define $$\begin{gathered} G_m(y)=\sum_{k=0}^{m-1}\mathrm e(ky),\\ S_j(\alpha)=\mathrm e(\alpha(a+j))\bigl(G_m(\alpha q)+\mathbf 1_{j\le s}\mathrm e(\alpha mq)\bigr), \quad1\le j\le q. \end{gathered}$$ The sum $S_j$ is exactly the residue sum for $a+j$, comprising $m$ complete periods and at most one terminal term. If $0<|\alpha|q\le1/2$, $$|G_m(\alpha q)|\le(2|\alpha|q)^{-1},\qquad |\mathrm e(\alpha j)-1|\le2\pi|\alpha|q\quad(1\le j\le q).$$ Each sum thus lies within $\pi+1$ of a common center, and within $1$ when $\alpha=0$. Subtracting the mean minimizes the sum of squared distances, giving $V_q(\alpha)\le q(\pi+1)^2$. The fixed frequency support and the eventual inequality $2Q/H<1/2$ place the whole integral in this range. The positive form is therefore $O(Q^3/(N\log Q))=O(1/\log Q)$. On the other hand, the number of unit integers is $N_q=N(1-1/q)+O(1)$, whence $$\langle f,Af\rangle=-\sum_{q\in\mathcal Q}(q-2)+O(1/\log Q).$$ The prime number theorem and partial summation give the operator lower bound.

For $w$, define $c(p)=((p-1)/(p-2))^2-1=O(1/p)$ and extend multiplicatively on squarefree integers. Expand the nonnegative Euler product, discard masks bounded by $1$, and enlarge the interval to obtain $$\left\|b_x^{(z)}\right\|_2^2\le xW_z^2\prod_{p>z}(1+c(p)/p)\ll xW_z^2.$$ The product converges since $c(p)/p=O(p^{-2})$. Mertens’ product theorem gives $W_z\ll\log z\ll_K\log\log x$. The prime number theorem also gives $\sum_{u\in I_x}\Lambda(u+2)^2\sim(x/2)\log x$, with proper prime powers contributing a lower-order term. The two-sided triangle inequality for norms proves the asymptotic for $w$, without assuming orthogonality between $b_x^{(z)}$ and $\Lambda$.

For $\beta$, take primes $x^{2/5}<p\le x^{9/20}$ and $x/(2p)<r\le x/p$. Eventually $p<r$, and both exceed $U$. Thus $n=pr\in I_x$, $\Lambda(n)=0$, and the only divisor of $n$ at most $U$ is $1$, so $\beta(n)=-1$. The smaller prime factor is unique, avoiding repeated counts. The ordinary prime number theorem in doubling intervals is uniform over this range. The number of such products is $$(1+o(1))\frac x2\sum_{x^{2/5}<p\le x^{9/20}}\frac1{p\log(x/p)} =\left(\frac12\log\frac{27}{22}+o(1)\right)\frac x{\log x}.$$ The final equality follows by partial summation and $\int_{2/5}^{9/20}[a(1-a)]^{-1}\,da=\log(27/22)$. Multiplying the three lower bounds proves the last assertion.

###### ref-1bd05cdbef8ba2d8

\[cor:normalized\] For the specified row-energy normalization, $$H^{-1}\ll_\psi\left\|Z\right\|_2\ll_\psi(\log Q)/H.$$ Moreover, $\left\|Z\right\|_2\,\left\|D_G^{1/2}\beta\right\|_2\,\left\|D_G^{1/2}w\right\|_2$ is still at least $c_\psi xQ^2/\log Q$ for some $c_\psi>0$.

Since $A=D_G^{1/2}ZD_G^{1/2}$, $\left\|A\right\|_2/G_{\max}\le\left\|Z\right\|_2\le\left\|A\right\|_2/G_{\min}$. Each weighted vector contributes a factor of at least $\sqrt{G_{\min}}$ relative to its unweighted norm. Thus the norm-product expression is at least $$(G_{\min}/G_{\max})\left\|A\right\|_2\left\|\beta\right\|_2\left\|w\right\|_2.$$ Apply Proposition [\[prop:energy\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-439da380e3fa45e9) and Theorem [\[thm:normbarrier\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-e122b78aee14f006).

This is a lower bound on an upper-bound expression, not a lower bound on $|\mathfrak C_x|$. It does not rule out cancellation between the actual coefficients, other preconditioners, or coefficient-sensitive methods.

## A growing number of negative directions

###### ref-de3b201514ed5f23

\[thm:rank\] Put $\tau_x=Q^2/\log Q$ and $$J_x=\left\lfloor N\left(\frac1{4Q}-\frac1H\right)\right\rfloor,\qquad d_x=2J_x+1,\qquad k_x=d_x-35.$$ For all sufficiently large $x$, there is a complex subspace $W_x$ such that $$\dim_\mathbb CW_x\ge k_x,\qquad \langle f,Af\rangle\le-\frac{\tau_x}{2}\left\|f\right\|_2^2\quad(f\in W_x).$$ Every matrix $E$ of complex rank less than $k_x$, even if non-Hermitian, satisfies $\left\|A-E\right\|_2\ge\tau_x/2$, and $k_x=Q^2/4-x^{11/32}+O(1)$.

Set $U_0=A+\mathop{\mathrm{diag}}\Delta\ge0$ and take $f_j(n)=N^{-1/2}\mathrm e(jn/N)$ for $|j|\le J_x$. These vectors are orthonormal on $N$ consecutive integers, and eventually $d_x<N$. For all $q\le2Q$ and $|v|\le1$, we have $q|j/N+v/H|\le1/2$. The preceding residue-variance bound gives $$\langle f_j,U_0f_j\rangle\le\frac{C_0}{N}\sum_q q^2,\qquad C_0=(\pi+1)^2.$$ Let $F$ have these vectors as columns, $B=F^*U_0F\ge0$, and $M_1=\sum_q q$. Then $$\mathop{\mathrm{tr}}B\le C_0(1+2Q/N)M_1.$$ An actual integer is divisible by at most two shell primes, so $$\Delta(n)\ge D_*:=\sum_q\frac{q(q-2)}{q-1}-4Q\sim\frac32\tau_x.$$ The number of eigenvalues of $B$ exceeding $D_*/2$ is at most $2\mathop{\mathrm{tr}}B/D_*<35$ eventually, and eventually $D_*\ge\tau_x$. Map the $[0,D_*/2]$ spectral subspace of $B$ through $F$ to obtain $W_x$. At most $35$ dimensions are lost; on this space the $U_0$ form is at most $D_*/2$, whereas the removed diagonal is at least $D_*$. This proves negativity. If $\mathop{\mathrm{rank}}E<k_x$, then $W_x\cap\ker E$ is nonzero. A unit vector in the intersection gives $\left\|A-E\right\|_2\ge|\langle f,(A-E)f\rangle|\ge\tau_x/2$. Finally, expand $d_x$ using $N=x/2+O(1)$ to obtain the dimension asymptotic.

The spectral cutoff does not say that the whole low-frequency band is negative, or that repairs above some higher rank must succeed.

Real witnesses require a separate construction; a complex spectral space cannot simply be renamed a real one. In the same symmetric band, form the real orthonormal matrix $V$ from $f_0$, $(f_j+f_{-j})/\sqrt2$, and $(f_j-f_{-j})/(\mathrm i\sqrt2)$. The real symmetric matrix $\operatorname{Re}(V^*U_0V)$ is positive semidefinite and has trace $\mathop{\mathrm{tr}}B$. Repeating the spectral cutoff gives a different real subspace of dimension at least $k_x$. In particular, for a real-linear map $$E:\mathbb R^{I_x}\longrightarrow\mathbb C^{I_x},\qquad\mathop{\mathrm{rank}}_{\mathbb R}E<k_x,$$ a unit vector in its kernel intersected with this real negative subspace gives $\|A-E\|_{\mathbb R^{I_x}\to\mathbb C^{I_x}}\ge\tau_x/2$. The norm uses the Euclidean unit sphere in the real domain, and rank means real image dimension, not complex rank. The identity $f^TAf=f^T\operatorname{Re}(A)f$ applies to a quadratic form at one real vector. It cannot replace the mixed scalar $w^TA\beta$ by $w^T\operatorname{Re}(A)\beta$.

# From exact emission to two-sided short arrays: the costs that remain

## The complete Kloosterman representation

Let $\eta_b$ be the real partition functions constructed in Section [7](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#A%20paid%20component%3A%20constructive%20partitioning%20and%20the%20boundary%20contribution), and define the finite set of physical labels $$\mathcal J_x=\{j\in\mathbb Z:\operatorname{supp}\eta_{j,H}\cap[x/2,x]\ne\varnothing\}, \qquad |\mathcal J_x|=O(x/H+1).$$ All ordered block pairs and their sums in this section are restricted to $(b,c)\in\mathcal J_x^2$. Set $a^{(j)}(t)=\eta_b(t)\beta(t)+\mathrm i^j\eta_c(t)w(t)$ for $j=0,1,2,3$. For fixed $q\in\mathcal Q$ and $v\in\mathbb R$, define the sums on unit residue classes and their centered versions by $$F_r^{(j)}=\sum_{t\in I_x,\ t\equiv r(q)}a^{(j)}(t)\mathrm e(vt/H),\qquad F_r^{(j),0}=F_r^{(j)}-\frac1{q-1}\sum_{s\ne0}F_s^{(j)}.$$ Set the centered vector to zero at the zero residue class. Suppressing the superscript $j$, put $$\alpha_m=\frac1q\sum_{r\ne0}F_r^0\mathrm e(-mr/q),\quad \gamma_n=\frac1q\sum_{r\ne0}\overline{F_r^0}\mathrm e(-n\bar r/q),\quad 1\le m,n<q,$$ where $\bar r$ is the multiplicative inverse of $r$ modulo $q$.

###### ref-f0807f85e445b09f

\[prop:emitter\] For the unnormalized Kloosterman sum $S(m,n;q)=\sum_{r\ne0}\mathrm e((mr+n\bar r)/q)$, $$\mathcal B=\sum_{m,n=1}^{q-1}\alpha_m\gamma_nS(m,n;q) =\sum_{r\ne0}|F_r^0|^2 =q\left\|\alpha\right\|_2\left\|\gamma\right\|_2.$$

Centering makes the zero frequency of both Fourier transforms vanish. Expand $S$ and apply finite Fourier inversion to the two inner sums, recovering $F_r^0$ and $\overline{F_r^0}$. Parseval gives $\left\|\alpha\right\|_2^2=\left\|\gamma\right\|_2^2=q^{-1}\left\|F^0\right\|_2^2$, since inversion permutes the unit residue classes.

This is an exact representation, not a cancellation estimate. The arrays have range $q-1$; centering does not shorten them to length $\sqrt q$. For example, if $F^0=e_1-e_2$, every nonzero frequency of the first array is nonzero. This example tests the interface; it does not identify the actual arithmetic vector with that example.

## Signed recombination before residual estimates

###### ref-c1900feb79a2cc46

Write $$d_j(q)=\frac{q-2}{q-1}\sum_{t\in I_x,\ q\nmid t}|a^{(j)}(t)|^2,\qquad E_{bcq}=\int\psi_+(v)\frac14\sum_{j=0}^3\mathrm i^j[\mathcal B_j-d_j(q)]\,dv.$$ Expanding the four squares and using $\sum_j\mathrm i^j=\sum_j\mathrm i^{2j}=0$ gives $$\mathfrak C_x=\sum_{b,c}\sum_{q\in\mathcal Q}qE_{bcq}.\label{eq:polarreturn}$$ The phase inside the integral is $\mathrm e(v(t-u)/H)$, with the same orientation as the kernel in Section [4](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#The%20analytic%20core%3A%20the%20actual%20operator%20and%20its%20exact%20structure). Subtracting $d_j$ removes the diagonal exactly; the outer factor $q$ must not be counted twice. Each of the four positive packages may saturate even when their signed combination exhibits cancellation. Taking their absolute values separately loses this distinction.

###### ref-2bb345379e6b5258

For arrays supported on integer intervals and vanishing at multiples of $q$, write $$\mathcal B_q(A_1,A_2)=\sum_{m,n}A_1(m)A_2(n)S(m,n;q).$$ The unit multiplier is always $1$ here and does not vary with the decomposition index. When both integer intervals have length at most a constant multiple of $\sqrt q$, the unit multiplier and coprimality hypotheses of the Blomer–Pascadi theorem yield the critical-scale bound $$|\mathcal B_q(A_1,A_2)|\ll_\epsilon q^{31/32+\epsilon} \left\|A_1\right\|_2\left\|A_2\right\|_2.\label{eq:bp}$$ We use the prime-modulus, nonzero-index specialization of their Theorem 1.1[\[\@blomer2026\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-cee6b8e4496327ac), not a direct application to the complete emitted arrays. Cutting each length-$q-1$ array into $k\asymp\sqrt q$ blocks gives $$\sum_{A,B}\left\|\alpha_A\right\|_2\left\|\gamma_B\right\|_2\le k\left\|\alpha\right\|_2\left\|\gamma\right\|_2.$$ Applying [\[eq:bp\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-2bb345379e6b5258) rectangle by rectangle therefore produces only a $q^{47/32+o(1)}$ norm factor, worse than the full scale in Proposition [\[prop:emitter\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-f0807f85e445b09f). This is the cost of that recombination method, not an impossibility theorem for every decomposition.

###### ref-4707aa8056efa21f

\[cond:compression\] Fix a loss exponent $\ell\ge0$ and $A_0>2$ before sending $x\to\infty$; let $\omega_{bc}=(1+|b-c|)^{-A_0}$ for $(b,c)\in\mathcal J_x^2$. For the already signed, diagonal-removed, integrated quantity $E_{bcq}$, there is a decomposition $$E_{bcq}=\sum_\nu\lambda_\nu\mathcal B_q(A_{1,\nu},A_{2,\nu})+R_{bcq},$$ in which every rectangle satisfies all hypotheses of [\[eq:bp\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-2bb345379e6b5258), and $$\begin{aligned} \sum_\nu|\lambda_\nu|\left\|A_{1,\nu}\right\|_2\left\|A_{2,\nu}\right\|_2 &\ll\omega_{bc}(H/q)x^{\ell+o(1)},\\ |R_{bcq}|&\ll\omega_{bc}Hq^{-1/32}x^{\ell+o(1)}.\end{aligned}$$ The constants and small-exponent terms are uniform over all original ordered block pairs and the full prime shell, with no unpaid exceptional set.

If this condition holds, then $$\sum_{b,c\in\mathcal J_x}\omega_{bc} \le |\mathcal J_x|\sum_{h\in\mathbb Z}(1+|h|)^{-A_0}\ll x/H,$$ and [\[eq:bp\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-2bb345379e6b5258), followed by the outer prime sum, gives $$|\mathfrak C_x|\ll (x/H)H\sum_{q\in\mathcal Q}q^{31/32}x^{\ell+o(1)} \ll xQ^2x^{-1/96+\ell+o(1)}.$$ Here $o(1)$ means that an arbitrarily small fixed positive exponent loss can be absorbed at sufficiently large scales: first fix a strict margin, then choose $\epsilon$ in [\[eq:bp\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-2bb345379e6b5258) sufficiently small. Thus $\ell<19/2400$ suffices to pay for $\delta>1/400$. This is a conditional exponent ledger. We do not prove Condition [\[cond:compression\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-4707aa8056efa21f), nor require every successful route to use this decomposition.

# A paid component: constructive partitioning and the boundary contribution

Unlike cancellation of the full scalar, the boundary term can be controlled by support size while preserving the actual objects[\[\@archivephysical\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-7e6f6fbcb85b6e45).

###### ref-7672f9bcf6a9c0f8

\[thm:boundary\] There is a nonnegative smooth partition $\sum_j\eta_{j,H}=1$ with finite overlap, each support of length $H$, and $H^r\|\eta_{j,H}^{(r)}\|_\infty\le C_r$ uniformly in $j,H$. Classify labels only inside the physical set $\mathcal J_x$ of supports meeting $[x/2,x]$: $$\mathcal J_\partial=\{j\in\mathcal J_x:\operatorname{supp}\eta_{j,H}\not\subset(x/2,x)\}.$$ Let $\theta_\partial=\sum_{j\in\mathcal J_\partial}\eta_{j,H}$ be their total weight and set $\theta_{\rm int}=1-\theta_\partial$. Then $$\left|\mathfrak C_x-\langle \theta_{\rm int}w,A(\theta_{\rm int}\beta)\rangle\right| \ll xQ^2x^{-11/64+o(1)}.$$

Take $\chi(s)=\exp[-1/(1-4s^2)]$ for $|s|<1/2$ and zero elsewhere, and set $$D(s)=\sum_{j\in\mathbb Z}\chi(s-j/2),\qquad \eta_{j,H}(t)=\frac{\chi(t/H-j/2)}{D(t/H)}.$$ The function $D$ is positive, smooth and $1/2$-periodic: every point lies within $1/4$ of a half-integer. All derivatives of $D$ and $D^{-1}$ are bounded on one period. The chain rule gives the required derivative estimates. Each closed support is contained in $[(j-1)H/2,(j+1)H/2]$, at most three closed supports overlap, and $|\mathcal J_x|=O(x/H+1)$. Since every classified support meets the physical closed interval, a boundary support must contain at least one endpoint. There are therefore at most six such supports, and $$\operatorname{supp}_{I_x}\theta_\partial \subset [x/2,x/2+H]\cup[x-H,x], \quad |\operatorname{supp}_{I_x}\theta_\partial|=O(H+1).$$ Only pointwise envelopes for the actual coefficients are needed. The divisor bound $\tau(n)\ll_\epsilon n^\epsilon$ gives $|\beta(n)|\le1+\tau(n)$. By [\[eq:hybrid\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-45862620c0893c3b), $0\le b_x^{(z)}(n)\le W_z2^{\omega(n)}\le W_z\tau(n)$, so $|\beta(n)|+|w(n)|\le x^{o(1)}$ uniformly on the actual interval, for fixed $K$. The divisor bound follows prime power by prime power: for $p\ge2^{1/\epsilon}$, $k+1\le2^k\le p^{\epsilon k}$; for each of the finitely many remaining primes, $\sup_k(k+1)p^{-\epsilon k}$ is finite.

Thus each boundary vector has norm $H^{1/2}x^{o(1)}$, while each full vector has norm $x^{1/2+o(1)}$. Expand exactly, counting the double-boundary term only once: $$\mathfrak C_x-\langle w_{\rm int},A\beta_{\rm int}\rangle =\langle w_\partial,A\beta\rangle+\langle w_{\rm int},A\beta_\partial\rangle.$$ Lemma [\[lem:upper\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-172b0b6c79d78791), namely $\left\|A\right\|_2\ll Q^2$, now gives $Q^2\sqrt{xH}x^{o(1)}=xQ^2x^{-11/64+o(1)}$.

The theorem bounds the *collective contribution* of all weighted ordered pairs with a boundary label, not the absolute value of each positive polarization package. It makes an admissible explicit choice of partition; it does not assert derivative bounds for every previously specified partition. The interior cutoff is genuinely smooth, but this does not turn $\Lambda$, the Möbius coefficients, or the hybrid main term into smooth coefficients. If an interior saving $\delta_{\rm int}$ is proved in the future, this recombination certifies a full saving of $\min(\delta_{\rm int},11/64)$. The signed interior estimate remains unresolved here.

# Islands 5 and 7: moving targets, a distinguished seed, and geometric attachment

## Exact arithmetic encoding and a metric hitting theorem

Let $\widehat\mathbb Z$ be the group of profinite integers, let $m_H$ be Haar probability measure, and let $T(\xi)=\xi+1$. We write $m_H$ to avoid confusion with the Möbius function $\mu$. Set $$y_n=\sqrt{n+2},\quad Q_n=\prod_{p\le y_n}p,\quad E_n=\{\xi:p\nmid\xi(\xi+2)\text{ for every }p\le y_n\},\quad Z_n(\xi)=\mathbf 1_{E_n}(T^n\xi).$$ For $n\ge3$, $Z_n(0)=1$ if and only if both $n$ and $n+2$ are prime: both exceed the common sieve threshold, whereas every composite integer at most $n+2$ has a prime factor at most $\sqrt{n+2}$. The Chinese remainder theorem gives $$\alpha_n=m_H(E_n)=\frac12\prod_{2<p\le y_n}(1-2/p)\asymp(\log n)^{-2}.$$ The underlying $T$ is an autonomous adding map, not a mixing transformation. Nonautonomy enters through the targets and sieve scales that change with $n$.

###### ref-7b3e7bce089742fc

\[thm:haar\] Let $S_N=\sum_{3\le n\le N}Z_n$ and $A_N=\sum_{3\le n\le N}\alpha_n$. Then $$\operatorname{Var}_{m_H}(S_N)\ll N,\qquad A_N\asymp N/(\log N)^2.$$ For $m_H$-almost every $\xi$, $S_N(\xi)\to\infty$.

For $m<n$, put $d=n-m$. Separating common sieve primes from newly added primes in the Chinese remainder theorem gives $$\operatorname{Cov}(Z_m,Z_n)=\alpha_m\alpha_n(K_{y_m}(d)-1).$$ For a common prime $p$, the forbidden classes are $0,-2,-d,-d-2$. Counting their coincidences gives $$\begin{aligned} k_2(d)&=2\mathbf 1_{2\mid d},&k_3(d)&=3\mathbf 1_{3\mid d},\\ k_p(d)&=1-\frac4{(p-2)^2}+\frac{2p}{(p-2)^2}\mathbf 1_{p\mid d} +\frac p{(p-2)^2}(\mathbf 1_{p\mid d-2}+\mathbf 1_{p\mid d+2})\quad(p\ge5),\end{aligned}$$ where $K_y=\prod_{p\le y}k_p$. Every factor has mean $1$ over a complete residue system. Expanding into indicators of Chinese-remainder residue classes, the sum of absolute coefficients is at most $$D(y)=6\prod_{5\le p\le y}(1-2/p)^{-2}\ll\log^4(2y).$$ The final bound follows from Mertens’ product theorem and a convergent $O(p^{-2})$ correction. The count of any residue class in an integer interval differs from the interval length divided by its modulus by at most $1$. Hence $$\left|\sum_{d\in J}(K_y(d)-1)\right|\le D(y).$$ For fixed $m$, Abel summation against the nonincreasing weights $\alpha_{m+d}$ yields $$\left|\sum_{d=1}^{N-m}\alpha_{m+d}(K_{y_m}(d)-1)\right| \le\alpha_{m+1}D(y_m).$$ When $y_m\ge3$, $\alpha_m^2D(y_m)=1/6$, so the absolute value of the grouped covariance for each $m$ is at most $1/6$. The finitely many initial $m$ contribute a bounded amount, and the diagonal variance is at most $\sum\alpha_n\le N$. This proves the variance estimate. Mertens’ product theorem and the fixed two-point singular series give the order of $A_N$. Chebyshev’s inequality along $N=j^2$ gives $$m_H\{|S_{j^2}-A_{j^2}|>A_{j^2}/2\}\ll\frac{(\log j)^4}{j^2}.$$ The right-hand side is summable. The first Borel–Cantelli lemma implies that almost every seed eventually satisfies $S_{j^2}\ge A_{j^2}/2\to\infty$. Monotonicity of $S_N$ extends the conclusion to all $N$.

This argument comes from the original moving-target proof[\[\@archivedynamics\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-441a58c68884b6c1). It is a metric theorem for the actual sieve events, not merely a finite-model statement. Its null exceptional set may nevertheless contain $0$, so it does not cross the map’s Bridge B.

## A precise form of the distinguished-seed gap

The following sufficient criterion comes from the existing distinguished-seed reconnaissance report[\[\@archiveseed\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-5359a67dfa077694); we reproduce its short proof. Choose $q_N\mid Q_N$, put $U_N=q_N\widehat\mathbb Z$, and define $$V_N=\|S_N-A_N\|_{L^2(m_H)},\qquad \Omega_N=\sup_{\xi\in U_N}(S_N(\xi)-S_N(0)).$$

###### ref-116dd6b4896cf166

\[prop:seed\] For every $N$, $$S_N(0)\ge A_N-\sqrt{q_N}V_N-\Omega_N.$$ If, along an unbounded sequence $N_j$, some fixed $\eta>0$ satisfies $\Omega_{N_j}+\sqrt{q_{N_j}}V_{N_j}\le(1-\eta)A_{N_j}$, then there are infinitely many twin primes.

We have $m_H(U_N)=1/q_N$. The definition of $\Omega_N$ and Cauchy–Schwarz imply $$S_N(0)\ge q_N\int_{U_N}S_N\,dm_H-\Omega_N \ge A_N-\sqrt{q_N}V_N-\Omega_N.$$ The assumed condition gives $S_{N_j}(0)\ge\eta A_{N_j}\to\infty$; apply the exact arithmetic encoding.

The known bound $V_N\ll\sqrt N$ ensures that $q_N=o(N/\log^4N)$ implies $\sqrt{q_N}V_N=o(A_N)$. This is sufficient, not necessary, and the required bound for $\Omega_N$ is not known in this regime. For the fine cylinder $q_N=Q_N$, $S_N$ is constant on the cylinder and $\Omega_N=0$, but $Q_N=\exp((1+o(1))\sqrt N)$ makes the generic point-evaluation cost too large. The proposition is a sufficient criterion, not an assertion that its hypothesis holds or that it is the only possible return mechanism.

## Stage-preserving sieve evolution and a scoped obstruction to strongly mixing carriers

Let $P_k=\prod_{j\le k}p_j$, equip $V_k=\mathbb C^{\mathbb Z/P_k\mathbb Z}$ with the normalized counting inner product, and put $B_k(r)=\mathbf 1_{(r(r+2),P_k)=1}$, $a_k=\operatorname{mean}B_k$, and $W_k=B_k-a_k$. When a new odd prime $p$ is added, define the replication-and-deletion operator by $$(R_pf)(r+jP_k)=f(r)\mathbf 1_{p\nmid(r+jP_k)(r+jP_k+2)},\quad 0\le j<p.$$ Exactly $p-2$ children survive for every parent residue. Thus, with $\alpha_p=1-2/p$, $$R_p^*R_p=\alpha_p I,\quad \operatorname{mean}(R_pf)=\alpha_p\operatorname{mean}f.$$ Set $g=R_p1-\alpha_p$. Direct averaging gives $\|g\|^2=\alpha_p(1-\alpha_p)$, and every mean-zero $f$ satisfies $\langle R_pf,g\rangle=0$. Consequently, $$W_{k+1}=R_pW_k+a_kg,\qquad \|W_k/a_k\|^2=a_k^{-1}-1\asymp(\log p_k)^2.$$ The forcing term is part of the actual evolution; this is not a homogeneous exponentially contracting system.

More precisely, suppose maps $J_k$ are uniformly bounded and coercive on the entire mean-zero space, $c\|f\|\le\|J_kf\|\le C\|f\|$, and satisfy the exact intertwining relation $J_{k+1}R_{p_{k+1}}=Q_kJ_k$. They cannot also satisfy a uniform arbitrary-product estimate $\|Q_{b-1}\cdots Q_a\|\le C_Q\theta^{b-a}$ with $0<\theta<1$. Indeed, the three assumptions imply $$c\prod_{a<j\le b}(1-2/p_j)^{1/2}\le CC_Q\theta^{b-a}.$$ For fixed $a$, the left side is only of order $1/\log p_b$, and the prime number theorem gives $p_b\asymp b\log b$, contradicting exponential decay on the right. This excludes only the simultaneous validity of those three assumptions. It does not exclude noncoercive quotient maps, observable seminorms, or nonautonomous representations with controlled defects[\[\@archiveintertwiner\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-8050454dadc14b8c).

## The role and limits of Island 7

A useful geometric lift must at least supply a time-preserving semiconjugacy, event pullback, an applicable measure correspondence, and a correspondence for the *distinguished seed*. For example, candidate maps $\rho_k$ and transformations $H_k,F_k$ must satisfy $\rho_{k+1}H_k=F_k\rho_k$, and lifted events must be exactly the inverse images of the original events. These are attachment conditions to be proved. We do not construct a twin-prime-specific Hénon lift here.

Even a stationary mixing system cannot have a nontrivial addition-by-one clock modulo $M$ as a measure-preserving factor: the clock’s mean-zero eigenfunction $\mathrm e(r/M)$ has autocorrelation of constant absolute value $1$, contradicting mixing after pullback. This finite-factor argument does not establish impossibility for all nonautonomous geometric representations. Nor does a two-dimensional phase space imply that all relevant observables have a two-dimensional linear carrier. Island 7 is therefore an auxiliary representation route; a geometric picture cannot replace the distinguished-orbit hitting requirement on Island 5.

# The two bridges: conditional ledgers and conclusions

## The analytic bridge: established structure and unpaid estimates

Bridge A in the map runs from Island 2 to Island 6. The repository’s Gate A and Gate B are both analytic obligations inside this bridge, not the two different red bridges in the map. Table [1](../99_%E7%BB%B4%E6%8A%A4/%E5%BE%85%E8%A7%A3%E5%86%B3%E6%9D%A5%E6%BA%90%E9%93%BE%E6%8E%A5.md#issue-ef7513bf9554b8be) places the quantities used here on a common scale.

<div id="tab:ledger">

| Component              | Content on the common scale                                                                                                               | Status                    |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| Actual operator        | $Q^2/\log Q\ll\left\|A\right\|_2\ll Q^2$; every actual row has energy $\asymp HQ^2/\log Q$                                                | Proved, scoped            |
| Actual coefficients    | A norm-product argument alone cannot pay for a fixed power saving                                                                         | Proved method obstruction |
| Boundary recombination | $xQ^2x^{-11/64+o(1)}$                                                                                                                     | This component paid       |
| Critical-array input   | Factor $q^{31/32+o(1)}$ for admissible two-sided short arrays                                                                             | External theorem          |
| Two-sided attachment   | Condition [\[cond:compression\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-4707aa8056efa21f), including every residual | Unproved                  |
| Full scalar target     | $|\mathfrak C_x|\ll xQ^2x^{-\delta+o(1)}$, $\delta>1/400$                                                                                 | Unproved                  |
| Analytic Gate A        | Original full-shell signed folding with positive margin $\eta_A$                                                                          | Separately unproved       |

: The exponent ledger. A logarithmic gap remains between the operator bounds. Structural identities, method obstructions, and target upper bounds are different kinds of evidence.

</div>

#### Imported conditional interface and reference exponent.

###### ref-3c0390c86ce707c3

To specify what the ledger estimates, write $$S_x^{\rm phys}=\sum_{t\in I_x}\beta(t)w(t),\qquad K_* =\sum_{q\in\mathcal Q}q\frac{q-2}{q-1}=x^{2/3+o(1)}.$$ The scalar $S_x^{\rm phys}$ is not $S_2(x)$ from Section [2](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#The%20arithmetic%20endpoint%2C%20quantifiers%2C%20and%20division%20of%20tasks). The source folding scalar $A_*$ and error scalar $E_*$ in V58 provide the imported interface[\[\@archivev58\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-93ac8690502c1912) $$S_x^{\rm phys}=\frac{A_*-\mathfrak C_x+E_*}{K_*},\qquad |E_*|\ll x^{143/96+o(1)}.$$ Here $A_*$ is a complex scalar, not the matrix $A$. Its source definition is the full-shell fold $\sum_q qP_q$, and $E_*=\sum_q qE_q$; the cited source interface supplies the rowwise construction of $P_q,E_q$ and the error proof. We import these identities and the error bound as premises, without reconstructing the upstream row data. The still-unproved analytic Gate A hypothesis is explicitly $$|A_*|\ll x^{1997/1200-\eta_A+o(1)},\qquad \eta_A>0.$$ Under this hypothesis and the full scalar target $|\mathfrak C_x|\ll x^{5/3-\delta+o(1)}$, division by $K_*$ gives the three output exponents $$\frac{399}{400}-\eta_A,\qquad 1-\delta,\qquad \frac{79}{96}.$$ The conditional output is therefore $|S_x^{\rm phys}|\ll x^{399/400-\eta+o(1)}$, where $$0<\eta<\min\{\eta_A,\delta-1/400,419/2400\}.\label{eq:terminal}$$ The margins in [\[eq:terminal\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-3c0390c86ce707c3) are exactly those relative to $399/400$: $(399/400)-(1-\delta)=\delta-1/400$ and $(399/400)-(79/96)=419/2400$. This is an exponent calculation under the source contract[\[\@archivev58; \@archivev59; \@archivephysical\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-93ac8690502c1912); [\[archivev59\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-be9fa27bed7ab906); [\[archivephysical\]](../99_%E7%BB%B4%E6%8A%A4/%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE/SYNTHESIS-EN.md#cite-7e6f6fbcb85b6e45), not a new independent proof of the entire upstream implication chain to the twin-prime conjecture. In particular, a saving for this paper’s scalar alone does not dispense with Gate A or the historical upstream structural attachments. If the critical-array route succeeds, $\delta=1/96-\ell$, requiring strictly $\ell<19/2400$. For a different interior estimate, boundary recombination limits the full saving certified here to $\min(\delta_{\rm int},11/64)$.

## The dynamical bridge: from a metric theorem to a distinguished point

Bridge B runs from Island 5 to Island 6. Exact sieve-event encoding, mass estimates, and the metric hitting theorem in Theorem [\[thm:haar\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-7b3e7bce089742fc) are already available; the missing step is to establish the conclusion for the distinguished seed $0$. Proposition [\[prop:seed\]](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#ref-116dd6b4896cf166) expresses one sufficient gap in terms of within-cylinder oscillation and point-evaluation cost, but does not supply the required joint bound. Any representation from Island 7 must return to this pointwise requirement or to another equally exact arithmetic readout condition.

## What the synthesis establishes

The seven islands distinguish research objects and transfer tasks; they do not turn a sequence of historical paper numbers into a closed proof chain. Basic arithmetic supplies local consistency. The fixed atom and occurrence layer fix the coefficients, support, and prefixes. The analytic layer supplies actual operator structure, growing-dimensional obstructions, and a boundary contribution that can be paid for. The dynamical layer supplies metric hitting for the actual moving targets and exact sieve geometry. These results have distinct mathematical content: they should neither be merged into a proof of the twin-prime conjecture nor dismissed indiscriminately as toy models.

This manuscript is a research synthesis of existing results, not a final paper with completed novelty assessment and submission positioning. A future version for external readers should further compress historical interfaces, expand the systematic external related-work discussion, and specify authorship and a target journal. The essential mathematical change cannot come from editorial work: the analytic bridge still needs signed estimates sensitive to the actual coefficients, and the dynamical bridge still needs a return to the distinguished arithmetic seed. This paper does not prove the twin-prime conjecture.

# Complete kernels, one-sided short support, and the status of model evidence

The complete Kloosterman matrix $\mathsf K=(S(m,n;q))_{1\le m,n<q}$ satisfies the directly verifiable identity $$\mathsf K\mathsf K^*=q^2I-(q+1)\mathbf J,$$ where $\mathbf J$ is the all-ones matrix. To verify it, expand the two Kloosterman sums. Summation over $n$ gives $q\mathbf 1_{r=s}-1$. The first contribution is $q\sum_{r\ne0}\mathrm e((m-m')r/q)=q(q\mathbf 1_{m=m'}-1)$, and the second is $1$, giving the stated matrix. Every row sums to $1$. Thus any vector $a$ with zero coordinate sum satisfies $\|\mathsf K^*a\|_2=q\|a\|_2$. Choosing $a=e_{m_1}-e_{m_2}$ supported on two distinct indices shows that scale $q$ is still attained when one side has only two coordinates while the other is complete and centered. One-sided short support therefore cannot replace the two-sided critical-array hypotheses.

This extremal example does not assert that the actual emitted coefficients attain that extremum. It shows that a universal bound knowing only support and centering cannot be stronger. Likewise, finite matrix checks test only the chosen scales. A model with a common growing-parameter theorem is stronger than a finite check, but still needs attachment of actual coefficients, a fixed starting point, parameter ranges, and residuals before it can address the original arithmetic problem. We do not reissue historical finite certificates as asymptotic theorems or add synthetic experiments merely to increase the manuscript’s length.

# Sources, deduplication, and the scope of verification

This paper selects core original sources from a standalone repository containing 420 TPC directories and rewrites them by mathematical dependency rather than paper number. Every proposition proved in the body remains subject to its stated hypotheses; classical inputs such as the Chinese remainder theorem, the prime number theorem, and Mertens’ theorem are not new discoveries here. The number of historical manuscripts is not the number of independent contributions.

The accompanying `SOURCE_CATALOG.md/json` enumerates all 420 directories, retaining original names, primary-source hashes, and candidate island labels obtained by text matching. These labels aid retrieval; they do not represent a manual semantic audit of all 420 full texts. The `CORE_SOURCE_MATRIX.md/json` records the core files actually used here, their source line ranges, SHA-256 hashes, and claim boundaries. Source proofs, historical interfaces, current handoff state, and independent reviews are listed separately; status files do not replace proofs.

The early structural interfaces in Section [3](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#Fixed%20atoms%20and%20actual%20occurrences%3A%20Islands%203%20and%204) come from original TeX sources. The main operator results in Sections [4](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#The%20analytic%20core%3A%20the%20actual%20operator%20and%20its%20exact%20structure)–[7](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#A%20paid%20component%3A%20constructive%20partitioning%20and%20the%20boundary%20contribution) come from the unnumbered research cycle of 9 September 2026. The CRT–Abel proof in Section [8](%E4%B8%83%E5%B2%9B%E7%BB%BC%E5%90%88%E7%A8%BF-English.md#Islands%205%20and%207%3A%20moving%20targets%2C%20a%20distinguished%20seed%2C%20and%20geometric%20attachment) comes from the original moving-target proof, and the replication-and-deletion structure comes from the exact physical-intertwining document. Original papers, research manuscripts, handoff files, and maps remain unchanged. The new synthesis is stored separately and adds no TPC paper number.

The verifiable core consists of complete definitions of shared objects, step-by-step proofs, and source hashes. Successful compilation, resolved citations, embedded fonts, and page-by-page visual inspection verify presentation, not theorems. Independent reviews apply only to their explicitly read scope; they certify neither the entire 420-directory collection nor novelty.

This full English translation preserves the Chinese edition’s proofs and claim boundaries and reproduces the supplied English map unchanged. The Chinese sources remain the provenance baseline; no research route is reopened.
