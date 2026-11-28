# Referee guide for `note854.md` (Erdős Problem #854)

Liang Wang, with AI assistance (Claude, Anthropic). Version of 2026-11-28.

This guide accompanies [`note854.md`](note854.md). It says what is claimed, what each proof depends on, and which steps most need an independent check. Nothing here has been refereed. A recheck by the same AI system (`../STAGE10_CHECK.md`) found no mathematical error, but it is not independent.

## 1. What we ask of a referee

The main request is to check **Theorems D, E and F** (§6.1–6.3 of the note, about five pages), the parts that use sieve theory. The rest is either elementary (Theorem A, the lemmas of §6.4), superseded (Theorem B), a reduction to a published black box (Theorem C), or computational (§5).

For each question in §4 below, a short answer is enough: **OK**, **gap** (the step is plausibly true but the argument is incomplete), or **error** (the step is false as stated), with a line on why.

A sieve-theory specialist should need about two to three hours for §6.1–6.3.

## 2. Claims

| | Statement (short form) | Where | Inputs from the literature | Priority |
|---|---|---|---|---|
| A | $s(k)\ge(\frac{e^\gamma}{1+e^\gamma}-o(1))p_k$ | §2 | Mertens | low |
| B | $s(k)\gg p_k\log p_k\log_3p_k/(\log_2p_k)^2$, explicit constant | §3 | Brun–Titchmarsh, Canfield–Erdős–Pomerance | low (superseded by C) |
| C | $s(k)\gg p_k\log p_k\log_3p_k/\log_2p_k$ | §4 | FGKMT Theorem 2 and the deduction in their §3; fundamental lemma | medium |
| D | $(1-\varepsilon)\min(J(\lceil(1-\eta)k\rceil),p_k^{1+\delta_0})\le s(k)$ | §6.1 | fundamental lemma, dimension 2, arbitrary classes | **high** |
| E | $\#\{\text{even gaps}\}\ge c(\varepsilon)\min(J(\lceil(1-\eta)k\rceil),p_k^{2-\varepsilon})$ | §6.2 | linear-sieve lower bound (L), upper-bound sieve (U) | **high** |
| F | D and E with lag $k^{1-\kappa}$; consequences outside a density-zero set of $k$ | §6.3 | as D and E; Iwaniec's $J(k)\ll(k\log k)^2$ | **high** |
| 13.2 | If $J(2k)\le D\,J(k)$ for large $k$ with $D<4$, then $\#\{\text{even gaps}\}\gg J(k)$ for all large $k$ | §6.3, last remark | Theorem F; Iwaniec | medium (short) |

Here $s(k)$ is the smallest even integer that is not a gap between consecutive integers coprime to $P_k=p_1\cdots p_k$, and $J(k)$ is the largest such gap.

**What is not claimed.** The second question of #854 ($\gg J(k)$ distinct gaps for every large $k$) is **not** solved. The note reduces it to the regularity of $J$ (conditions (R1), (R2) in the Summary, or the doubling condition of Theorem 13.2), and observes that the doubling condition would itself improve the exponent in Iwaniec's bound. The asymptotic $s(k)\sim J(k)$ is proved only outside a density-zero set of $k$, and only at those $k$ where $J(k)\le p_k^{1+\delta_0}$; we do not know how many $k$ satisfy that.

## 3. External theorems, in the exact form used

Every sieve statement is applied to an interval of integers with **arbitrary** residue classes removed (one or two per prime), so the remainder terms satisfy $|R_d|\le\omega(d)$. Please check that each cited theorem holds in this generality.

- **(FL) Fundamental lemma, dimension 2.** Used in Theorem D, Step 1, in two forms: (S1) a lower bound $|\mathcal X|\ge\frac12XV$ when $X\ge B^{s_0}$; (S2) an upper bound $\le2(X/q)V$ for the elements in a fixed class mod a prime $q>B$, when $X/q\ge B^{s_0}$. Also used in Theorem C, Step 1 (candidates). Reference: Friedlander–Iwaniec, *Opera de Cribro*, Ch. 6.
- **(L) Linear sieve lower bound** [HR, Theorem 8.4]. One class per prime $p\le z$, interval length $N\ge z^{2+\theta}$: at least $c_0(\theta)N/\log z$ survivors. Used in Theorem E, Step 1, and Theorem F(b).
- **(U) Upper-bound sieve** [HR, Theorem 2.2]. At most two classes per prime ($\omega(2)\le1$), $2\le z\le N$: at most $CN\prod_{p\le z}(1-\omega(p)/p)$ survivors. Used in Theorem E, Steps 2–3, and Theorem F.
- **FGKMT, Theorem 2** (*Long gaps between primes*, JAMS 2018), together with the deduction in their §3 that leaves $\ll x/\log x$ uncovered primes in $(x,y]$. Used only in Theorem C. Theorem D gives a second route to C that needs only the *statement* of the FGKMT lower bound for $J$.
- **Iwaniec**, $J(k)\ll(k\log k)^2$. Used in the corollaries of E and F and in the sparse-jumps lemma, in the weak form $J(2K)\le K^3$.

**Not yet done on our side:** the statements of [HR] Theorems 2.2 and 8.4 were checked against secondary sources, not against the book itself. If the numbering or hypotheses differ, the intended statements are the standard Brun-sieve upper bound and the Jurkat–Richert lower bound.

## 4. Questions, in order of importance

### Theorem D (§6.1)

- **D1. Step 1.** Is (S2) a correct consequence of the fundamental lemma? Writing $x=a+qn$, the variable $n$ runs over an interval of length $X/q$ and must avoid at most two classes modulo each $p\le B$, $p\ne q$.
- **D2. Step 3.** The average cost splits at $q=X/B^{s_0}$. For large $q$ the bound $N_q\le4X/q$ is trivial and needs $q\le X$; this holds because $q\le p_j<p_k\le\varepsilon L\le X$. Is the resulting third term, $(C_1/\varepsilon)B^{s_0}\log^2B=p_k^{1/2+o(1)}$, correctly $o(F)$ with $F\asymp\eta p_k/\log p_k$?
- **D3. Step 4.** Each exposed point $z$ excludes at most two free primes, because $(z-x)$ and $(x+t-z)$ are below $p_j^2$ and every free prime exceeds $p_j$. This needs $t<p_j^2$, which follows from $t\le p_k^{1+\delta_0}$ and $p_j\sim(1-\eta)p_k$. Correct?
- **D4. Step 5.** After the changes, can any endpoint be covered? The three kinds of primes are: those $\le B$ (unchanged; the endpoints avoid them because $x\in\mathcal X$), those in $(B,p_j]$ (either outside $Q(x)$, hence not hitting the endpoints, or re-classed away from them), and the free primes (chosen so that $\ell_z\nmid(z-x)(x+t-z)$).
- **D5. The value of $\delta_0$.** The proof takes $\delta_0=1/(2s_0)$ so that $B^{s_0}\le p_k^{1/2+o(1)}$. Is anything else needed from $\delta_0$?

### Theorem E (§6.2)

- **E1. Parameters.** $L\le p_k^{2-\varepsilon}$ is used only to get $L\ge B^{2+\varepsilon}$ for large $k$, so that (L) applies. Please check the inequality $\log B\le(\frac{1-\varepsilon}{2-\varepsilon}+o(1))\log L$.
- **E2. Step 2 (positive proportion of differences).** Three bounds are combined: $\sum_tr(t)\ge c_0^2L^2/\log^2B$; the upper bound $r(t)\le C_1h(t)L/\log^2B$ from (U); and the mean-square bound $\sum_{t\le T}h(t)^2\le C_2T$. Is the deduction $|\mathcal T|\ge cL$ correct, including the treatment of the $t$ with large $h(t)$?
- **E3. Step 3.** (U) is applied to $n$ (where $x=a+qn$) with sifting range $z=\min(B,M)$, $M=L/(2p_k)$. HR Theorem 2.2 needs $z\le N$; here $N=L/(2q)\ge M\ge z$. The claim $\log z\ge\frac14\log B$ uses $\log B\le3\log M+O(1)$. Correct?
- **E4. Parity.** All elements of $S$ lie in one class mod 2, because $2\le B$. So every $t$ with $r(t)>0$ is even. Correct?

### Theorem F (§6.3)

- **F1. The maximal sieve level.** In (a), $B=X^{1/s_0}$; in (b), $B=(L/4)^{1/(2+\theta)}$ with $\theta=\varepsilon/4$. Then $M$ may be much smaller than $B$, and the factor $(\log B/\log z)^2$ with $z=\min(B,M)$ can be as large as $(\log p_k/\log_2p_k)^2$. The proof absorbs it into $C''\log^2p_k\cdot L/B$. Is that bound correct uniformly in the range $M\ge(\log p_k)^{1/2}$?
- **F2. Exponents.** In (b), $L/B\ll L^{(1+\theta)/(2+\theta)}\le p_k^{(2-\varepsilon)(4+\varepsilon)/(8+\varepsilon)}\le p_k^{1-\varepsilon/3}$; with $F=\lceil k^{1-\varepsilon/4}\rceil$ this gives average cost $\le F/2$. In (a), $\kappa_0=1/(4s_0)$. Please check both.
- **F3. Sparse-jumps lemma.** The greedy chain $k_1>k_2>\cdots$ and the bound $m\le1+3\log K/\log C$. Correct?
- **F4. Corollaries.** The exceptional set depends on $\varepsilon$ through $\kappa=\min(\kappa_0,\varepsilon/8)$. Is the passage to a single density-zero set $\mathcal E'$ (letting $\varepsilon\to0$ slowly) correct as stated?

### Theorem 13.2 (last remark of §6.3)

- **G1.** From $J(2k)\le D\,J(k)$ for all large $k$: monotonicity of $J$ and $k-\lceil k^{1-\kappa}\rceil\ge\lceil k/2\rceil$ give (R1) with $C=D$; iteration gives $J(k)\ll k^{\log_2D}$, hence $J(k)\le p_k^{2-\varepsilon}$ when $D<4$. Is this correct, and is it fair to say that the hypothesis is at least as strong as an improvement of the exponent in Iwaniec's bound?

### Theorem C (§4)

- **C1.** Is the use of FGKMT Theorem 2 legitimate as stated: classes $\vec a$ on $\mathcal S$ and $\vec b$ on $\mathcal P$, every other prime $p\le x$ in class $0$, leaving $\le Kx/\log x$ uncovered integers in $(x,y]$?
- **C2.** Step 1 counts candidate endpoints with the fundamental lemma in dimension 2, at level $D=y^{1/2}$ with sifting range $z=x^{L_3/(4L_2)}$. Since $\log D/\log z\to\infty$, is $N_c\gg y/(\log z)^2$ justified for arbitrary classes $a_s$?

## 5. Points we already know are weak

- **The remark after Theorem E** that Theorem D holds for every $\delta_0<1/(\beta_2-1)\approx0.306$ is a sketch, not a proof. It plays no role in the main statements.
- **Constants.** $c(\varepsilon)$, $\delta_0$ and $\kappa_0$ are not made explicit.
- **The numerical sections** (§5 table; the runs of the Theorem D construction in §6.1; §6.4) are evidence, not proof, except where a witness is given.

## 6. The computational part

- Every gap in the §5 table has an explicit witness $N$ in `../a389839_witnesses.json`. The checker `../verify_a389839.py` uses only the Python standard library:
  ```
  python verify_a389839.py
  ```
  It reprints $s(k)$ for $k\le26$ (last re-run 2026-11-28).
- Every non-gap was found infeasible by HiGHS; for $k\le22$ also by CP-SAT. For $k=24$ and $25$ (non-gaps 230; 254, 256) only HiGHS finished, so $s(24)$ and $s(25)$ rest on one solver. Neither solver gives a machine-checkable certificate of infeasibility.

## 7. AI assistance

The proofs were drafted, and the computations written and run, by an AI system (Claude, Anthropic) under the direction of the author, who chose the problem and is responsible for the content. Please judge the arguments on their own terms; errors of the kind such systems make (a hypothesis silently dropped, an inequality in the wrong direction, a constant that depends on a parameter it should not) are exactly what we hope a referee will catch.
