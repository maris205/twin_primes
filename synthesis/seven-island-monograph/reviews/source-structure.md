TPC_AGENT_RESULT_V1

id: `synth-fixed-structure`  
mode: `READ_ONLY source audit`  
scope: islands ① arithmetic baseline, ③ fixed determinant-two atom, ④ pair-native/H1 actual-support and cover interface  
root: `/root/autodl-tmp/math_research3/twin_primes`  
baseline_HEAD: `d37c92b8a66bbd3d9084b1597d346429a9285302` — verified  
TPC_HANDOFF_sha256: `fee6147d2a01b324b723949a19c5a4ddd470237a315974b37acd18bd09e82bc8` — verified  
files_changed: `[]`

The consolidation can reuse six source-backed statement packages below. Their combined conclusion is **an exact arithmetic baseline and precisely defined structural interfaces—not a fixed-atom cancellation theorem or a completed actual-support cover**. Physical-return operators and dynamics are excluded from this audit.

All line ranges below refer to original TeX sources, not generated Markdown reading layers.

## 1. Island ①: exact local sieve factor

**Original definitions.** For distinct shifts \(\mathcal H=\{h_1,\ldots,h_r\}\),
\[
P_y=\prod_{p\le y}p,\qquad
s_y(n)=\mathbf1_{(n,P_y)=1},\qquad
\rho_y=\prod_{p\le y}(1-p^{-1}),
\]
\[
\nu_p(\mathcal H)=\#(\mathcal H\bmod p),\qquad
C_y(\mathcal H)=\frac1{P_y}\sum_{n\bmod P_y}\prod_{h\in\mathcal H}s_y(n+h).
\]

**Reusable theorem and fixed-two corollary.**
\[
C_y(\mathcal H)=\prod_{p\le y}\left(1-\frac{\nu_p(\mathcal H)}p\right),
\qquad
\frac{C_y(\mathcal H)}{\rho_y^r}\longrightarrow\mathfrak S(\mathcal H)
\]
for each fixed admissible \(\mathcal H\). In particular,
\[
\frac{C_y(2)}{\rho_y^2}\longrightarrow2C_2,
\qquad
C_2=\prod_{p>2}\frac{p(p-2)}{(p-1)^2}.
\]

**Anchors:** [TPC1 definitions and local-product theorem](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-1-two-scale-prime-sieve-correlations/main.tex:99), lines 99–168; [fixed-pair corollary](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-1-two-scale-prime-sieve-correlations/main.tex:203), lines 203–233.

**Dependencies and qualifiers:** CRT and convergence of the singular-series product; complete-period averages; fixed shifts in the limiting assertion. TPC1 explicitly labels this local product classical, lines 186–188.

**Not proved:** that a surviving pair is prime, any positive twin-prime lower bound, or a parity-breaking estimate.

**Placement:** opening arithmetic-baseline subsection; approximately one-third page. Present as classical input, not a new contribution.

## 2. Island ①: exact survivor-to-prime decomposition and scale mismatch

Define, after translating \(\min\mathcal H=0\) and setting \(H=\max\mathcal H\),
\[
A_{\mathcal H}^{>y}(X,y)
=\sum_{y<n\le X}\prod_{h\in\mathcal H}s_y(n+h),
\]
\[
T_{\mathcal H}^{>y}(X)
=\sum_{y<n\le X}\prod_{h\in\mathcal H}\mathbf1_{\{n+h\text{ prime}\}},
\qquad
R_{\mathcal H}=A_{\mathcal H}^{>y}-T_{\mathcal H}^{>y}\ge0.
\]

**Reusable propositions.** At \(Y_X=\sqrt{X+H}\), for sufficiently large \(X\),
\[
R_{\mathcal H}(X,Y_X)=0,\qquad
A_{\mathcal H}^{>Y_X}(X,Y_X)=T_{\mathcal H}^{>Y_X}(X).
\]
But the elementary periodic-window estimate
\[
|A_{\mathcal H}(X,y)-XC_y(\mathcal H)|\le P_y+1
\]
only gives the normalized singular-series limit under
\[
P_y=o(X\rho_y^r).
\]
The primality-exact endpoint does not meet that condition:
\[
\log P_{Y_X}=(1+o(1))\sqrt X,\qquad P_{Y_X}/X\to\infty.
\]

**Anchors:** [TPC1 periodic-window theorem](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-1-two-scale-prime-sieve-correlations/main.tex:244), lines 244–269; [decomposition and endpoint propositions](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-1-two-scale-prime-sieve-correlations/main.tex:625), lines 625–684.

**Dependencies and qualifiers:** elementary composite-factor bound, periodicity, and PNT for primorial growth. The mismatch concerns these two sufficient elementary regimes, not every possible sieve method.

**Not proved:** useful asymptotic evaluation of the primality-exact survivor count. Exact identification does not evaluate its size.

**Placement:** immediately after statement 1; approximately one-third page. This gives a concise reason the manuscript needs an analytic core beyond local congruences.

## 3. Island ③: determinant-two pullback with complete coefficient and prefix preservation

**Original object.** On an integer interval \(I\),
\[
D(z)=d+sz>0,\qquad V(z)=u+az>0,\qquad su-ad=2,
\]
with \(a,s\in\mathbb N\) and the physical primitive-branch conditions
\[
(a,s)=1,\qquad(as,2)=1,\qquad(d,s)=(u,a)=1.
\]
The literal block is
\[
A_{\xi,X}(z)=
\mu(D(z))\mu(V(z))
\mathbf1_{(B,V(z))=1}
\chi(\tau+Bz)W_X(\tau+Bz),
\]
\[
S_{\xi,X}(\alpha)=\sum_{z\in I}A_{\xi,X}(z)e^{-2\pi i\alpha z}.
\]

**Reusable theorem package.** Put
\[
q=as,\qquad n_0=su=ad+2,\qquad n(z)=n_0+qz=sV(z)=aD(z)+2.
\]
This is an order-preserving bijection onto the literal progression \(\mathcal N_I\), with congruences \(n\equiv0\pmod s\), \(n\equiv2\pmod a\). Exactly,
\[
\mu(D(z))\mu(V(z))
=\lambda(q)\lambda(n-2)\lambda(n)
\mu^2\!\left(\frac{n-2}{a}\right)
\mu^2\!\left(\frac ns\right).
\]
Consequently,
\[
S_{\xi,X}(\alpha)
=\lambda(q)\sum_{n\in\mathcal N_I}
\mathcal Q_{a,s}(n)\lambda(n-2)\lambda(n)
\mathcal W_{\xi,X}(n)e^{-2\pi i\alpha z(n)},
\]
where
\[
\mathcal Q_{a,s}(n)=\mu^2((n-2)/a)\mu^2(n/s),
\]
\[
\mathcal W_{\xi,X}(n)
=\mathbf1_{(B,n/s)=1}\chi(\tau+Bz(n))W_X(\tau+Bz(n)).
\]

Every initial prefix, absolute comparison mass, and endpoint-anchored variation is preserved, the latter along consecutive progression points. Thus an estimate with the complete displayed data and all required prefixes returns the same exponent to the original block.

**Anchors:** [TPC127 assumptions and original coefficient](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-127-determinant-two-liouville-pullback/main.tex:75), lines 75–120; [pullback theorem](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-127-determinant-two-liouville-pullback/main.tex:124), lines 124–199; [ordered isometry](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-127-determinant-two-liouville-pullback/main.tex:251), lines 251–285; [complete transport and no-loss statement](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-127-determinant-two-liouville-pullback/main.tex:287), lines 287–385.

**Dependencies:** TPC93 supplies primitive affine branches; TPC108 supplies the decorated coefficient; the identity uses \(\mu=\mu^2\lambda\) and complete multiplicativity of \(\lambda\).

**Not proved:** cancellation on this generally growing progression, removal of quotient-squarefree masks, uniform all-prefix decay, or selection of one fixed additive atom across all scales. “Fixed \(h_0=2\)” must not be rewritten as “one fixed phase \(\alpha_\star\) occurs at every scale.”

**Placement:** approximately one page; central island-③ subsection. Use a notation such as \(q_{\mathrm{prog}}=as\) to prevent confusion with a separate Fourier conductor.

## 4. Island ④: conditional source–child reconstruction, not an automatic pair-to-\(\omega\) bridge

**Original pair carrier.** For one opened-\(D\) packet, TPC18 defines \(J=K/D\), \(Q=LD\), \(QJ\asymp_WX\), and obtains
\[
|\mathcal T_D|^2\ll_WJ(\mathcal E_D+\mathcal C_D^{\mathrm{off}}).
\]
The off-diagonal sum is over **ordered** distinct rows and has coefficient
\[
\mu(d_\alpha)\mu(d_\gamma)
(\log\ell_\alpha)(\log\ell_\gamma)
r_R(N_\alpha(j))r_R(N_\gamma(j))
B_\alpha(j)B_\gamma(j),
\]
with \(N_\alpha(j)=\ell_\alpha d_\alpha j+h_0\). The second row comes from square expansion.

**Reusable conditional statement.** Given an already retained source atom
\[
\omega=(L/R,\alpha,\gamma,j,u)
\]
on the physical squarefree and target-primitive support, the TPC93 construction gives one child per \(v\mid(d_\alpha,d_\gamma)\), an explicit inverse, and
\[
\sum_{v\mid d,e}\lambda_G(v)=\mathbf1_{(d,e)\le G},
\qquad
\lambda_G(v)=\sum_{\substack{g\mid v\\g\le G}}\mu(v/g).
\]
The sign reassembly is literally
\[
\mu(d)(-\mu(u)\log u)\mathbf1_{(d,e)\le G}
=
\sum_{v\mid d,e}
[-\mu(v)\lambda_G(v)]\mu(d/v)\mu(u)\log u\,
\mathbf1_{(v,(d/v)u)=1}.
\]

TPC205 permits composition **only if** a source-backed theorem supplies the ordered pair, joint mask, packet schedule, \(T,U_0\), polarization, normalization stages, and identification with that retained \(\omega\).

**Anchors:** [TPC18 opened-\(D\) definitions and pair expansion](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-18-mobius-tail-determinant-dispersion/sections/opened-d-dispersion.tex:4), lines 4–57; [TPC93 source/child definitions](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-93-literal-low-window-affine-export/sections/decorated-affine-export.tex:155), lines 155–208; [inverse and coefficient reconstruction](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-93-literal-low-window-affine-export/sections/decorated-affine-export.tex:210), lines 210–282; [TPC205 conditional composition theorem](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-205-pair-native-post-ttstar-registry-interface/main.tex:119), lines 119–155.

**Not proved:** construction of a production \(\omega\) from the TPC18 formula alone. One child is not the whole source coefficient; the projector-weighted sum is essential. The displayed \(B\)-aliases must not silently become products of archived single-row coefficient expressions.

**Placement:** approximately half a page, connecting the fixed affine atom to the structural coverage problem.

## 5. Island ④: conservative H1 occurrence lift

**Original definitions.**
\[
\mathcal C_X^{\rm ns}
=\mathcal C_X^{\mathsf{ETO}}\sqcup\mathcal C_X^{\mathsf{FUM}},
\qquad
L_X:\mathbb C^{\mathcal C_X^{\rm ns}}\to\mathbb C^{\mathcal O_X}.
\]
TPC143 distinguishes formal support envelope, canonical parent carrier obtained through inverse aggregation, and actual active support with certified nonzero literal coefficients.

An occurrence lift is row-separated, metadata-faithful, and conservative if
\[
\mathbf1_{\mathcal O_X}^{T}L_X
=\mathbf1_{\mathcal C_X^{\rm ns}}^{T}.
\]

**Reusable conditional proposition.** For the conservative upstream cut matrix,
\[
\mathbf1_{\mathsf{EPS}}^TM_X^{\mathsf{EPS}}
+\mathbf1_{\mathcal O_X}^TL_XM_X^{\rm ns}
=\mathbf1_{\mathcal N_X}^{T}.
\]
This reconnects every native coefficient exactly **if the occurrence lift is supplied**.

**Anchors:** [TPC143 domain and support distinctions](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-143-frontier-occurrence-lift-contract/main.tex:83), lines 83–123; [typed lift and reconnection proposition](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-143-frontier-occurrence-lift-contract/main.tex:127), lines 127–202.

**Dependencies and qualifiers:** conservation of the TPC136 cut matrix and the stated conservation of \(L_X\). Entries may be signed or complex; splitting paths is allowed. Eligible-tail paths cannot be omitted merely because a finite sample contains only frontier paths.

**Not proved:** existence of this downstream production lift, identification of physical occurrences, nonzero support, or an estimate of the nonsoft scalar. A TT-star bilinear pair is not this linear coefficientwise-conservative map.

**Placement:** approximately half a page, adjacent to statement 4.

## 6. Island ④: literal weighted cover criterion

**Original definitions.** On the complete active atom set, let \(w\) be the literal coefficient vector and \(B\) the synthesis matrix of actual admissible blocks, including weights, masks, signs, polarizations, and normalization. All adjoints use the declared physical and coefficient-space inner products. Set
\[
P=BB^\dagger,\qquad c^*=B^\dagger w,\qquad r^*=(I-P)w.
\]

**Reusable theorem.**
\[
w\in\operatorname{Ran}B
\iff Pw=w
\iff r^*=0
\iff \langle y,w\rangle=0\quad\forall y\in\ker B^*.
\]
When these conditions hold, \(c^*\) is the least-norm exact cover. Moreover,
\[
\operatorname{dist}(w,\operatorname{Ran}B)
=\|r^*\|
=\max_{\substack{y\in\ker B^*\\\|y\|\le1}}|\langle y,w\rangle|.
\]

**Anchors:** [TPC117 literal carrier and three meanings of cover](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-117-full-block-physical-cover/main.tex:98), lines 98–149; [cover alternatives and dual certificate](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-117-full-block-physical-cover/main.tex:150), lines 150–205; [coefficient transport costs](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-117-full-block-physical-cover/main.tex:263), lines 263–303.

**Dependencies and qualifiers:** finite-dimensional linear algebra **after** the literal carrier and synthesis are supplied. Set-theoretic coverage is insufficient. Even exact cover retains coefficient transport costs such as \(\sum_b|c_b^*|U_b\).

**Not proved:** that the required growing production matrix satisfies the range condition. This is a criterion, not a constructed global cover or arithmetic saving.

**Placement:** approximately half a page, closing island ④ and handing off to the analytic-core section.

## Issues and manuscript safeguards

1. **Do not promote old map status labels.** The long route map calls island ④ `DONE_L0`; this is not proof of production coverage. The stable guide expressly forbids such an inference.

2. **Keep the selected-lineage obstruction scoped.** TPC206 establishes thirteen of forty-two fields for one selected graph, with opened uppercase \(D\) missing—not a global maximality theorem. It still lacks the production pair, full coefficient, crosswalk, and normalization return. See [selected closure](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-206-selected-lineage-pair-registry-projection/main.tex:177), lines 177 onward; [scope and remaining gaps](/root/autodl-tmp/math_research3/twin_primes/papers/tpc-206-selected-lineage-pair-registry-projection/main.tex:229), lines 229–268. The handoff retains this boundary at [lines 16617–16621](/root/autodl-tmp/math_research3/twin_primes/TPC_HANDOFF.md:16617).

3. **Separate affine determinant from ordered-row determinant.** The local atom satisfies \(su-ad=2\); the TPC18 ordered rows have determinant \(h_0(m_\alpha-m_\gamma)\). They are not interchangeable.

4. **Separate fixed displacement from fixed atom/schedule.** Per-packet determinant-two formulas do not produce one cross-scale named additive atom. The handoff explicitly distinguishes complete per-packet data from missing named-atom and scheduling data at [lines 23539–23595](/root/autodl-tmp/math_research3/twin_primes/TPC_HANDOFF.md:23539).

5. **Avoid notation collisions.** Distinguish progression modulus \(as\), Fourier conductor, opened scale \(D\), affine form \(D(z)\), row variable \(d\), Liouville \(\lambda\), and projector \(\lambda_G\). A normalization label is not a defined numerical scalar.

## Recommended 3–4 page narrative

Use thematic exposition rather than a chronology of paper numbers:

- **About 0.7 page — island ①:** classical local product, \(2C_2\), and the exact survivor/primality scale mismatch.
- **About 1 page — island ③:** literal coefficient, determinant-two identity, complete masked progression pullback, and prefix-preserving no-loss qualification.
- **About 1 page — island ④:** ordered TT-star carrier, conditional source–child reconstruction, and the distinct linear H1 lift.
- **About 0.6 page — cover boundary:** weighted range criterion, remaining production-data obligations, and transition to the analytic saving problem.

The closing message should be: **these results identify which coefficients, supports, prefixes, and normalization must be preserved; they do not establish the cancellation required to cross image Bridge A.**

No generators, staging, synchronization, network uploads, or file writes were performed.
