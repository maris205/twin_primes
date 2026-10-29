# Questions for a number-theory referee

**Paper.** L. Wang, *Why expansion methods for Chowla do not reach twin primes: a method-limitation theorem and an explicit parity compiler*, version 0.7 (Zenodo, DOI 10.5281/zenodo.23687596; 30 pages). Statement numbers refer to v0.7.

**Context.** The paper was produced with substantial AI assistance (Appendix D). None of the proofs has yet been checked by a specialist. We would be grateful for a check of the four points below, which we consider the most delicate. A short answer of the form "fine", "wrong because …" or "known, see …" is very helpful. We do not ask for a full report.

---

## 1. Theorem 4.1 (one-sided parity structure) and condition (U)

Theorem 4.1 (p. 10) is Bombieri's one-sided parity structure: for a sequence $a$ satisfying the hypotheses of Theorem 2.3, sums of $a_n$ over $n=p_1\cdots p_r$ with weight $g\in\mathcal G_r$ equal $\bigl(1+(-1)^{r+1}(\delta_x(a)-1)\bigr)$ times the model. We attribute it to Bombieri via Friedlander–Iwaniec (Ann. Pisa 1978, Remark I.4) and give a self-contained proof. The proof needs an extra hypothesis:

> **(U)** For fixed $r$ and $\tau$: $\displaystyle\sum_{n\le x^{1-\tau}}a_n\Lambda_r(n)/\log^rn+\sum_{n\le x,\ \mu^2(n)=0}a_n\Lambda_r(n)/\log^rn=o(x/\log x)$.

- **Q1a.** Is (U) the right extra hypothesis, or is it implied by (i)–(iv) of Theorem 2.3? The proof uses (U) to replace $\log^Dn$ by $\log^Dx$ and to discard non-squarefree $n$ in the identity $F_P=A+\beta_PL_D$.
- **Q1b.** Lemma 4.4 (p. 12) verifies (U) for $a_m=\log x\cdot\mathbf 1[m+2\in R_{r'}]$. Its key pointwise bound is $\Lambda_r(m)/\log^rm\ll_r\prod_{p^e\|k}\log p^e/\log x$, where $k$ is the $z_0$-smooth part of $m$, combined with a two-linear-form upper-bound sieve. Is that bound correct as stated, uniformly in the structure of $k$?
- **Q1c.** Theorem 2.3 is used exactly as stated in Tao's 2016 blog notes, Theorem 1, with $C=C_x$ allowed to depend on $x$ (Lemma 4.4). Is that use legitimate?
- **Q1d.** Is the general-sequence form of Theorem 4.1 stated explicitly anywhere in the literature, for example in Bombieri 1976 or in *Opera de Cribro*, Ch. 16? If so, please give the reference, so that we can cite it rather than reprove it.

## 2. Lemma B.1 (GEH box decomposition)

Lemma B.1 (p. 25) deduces, from GEH (Polymath8b, Claim 2.6), level of distribution $x^{1-\varepsilon}$ for weighted products of $r$ primes, each at least $x^\eta$, with sharp cutoffs.

- **Q2a.** Interior boxes have the form $I_1\times\dots\times I_r$ with $I_j=[N_j,N_j(1+\Delta_0))$ and $\Delta_0=\log^{-B}x$. We apply GEH at scale $X'=N_1\cdots N_r\in[x^{1-\varepsilon/2},x]$ with $\theta=1-\varepsilon/2$, and with $\alpha,\beta$ supported on sub-intervals of $[N,2N]$ and $[M,2M]$. Does Claim 2.6 apply verbatim to such short supports?
- **Q2b.** We claim that $\beta=(\log\mathbf 1_{\mathbb P\cap I_2})*\cdots*(\log\mathbf 1_{\mathbb P\cap I_r})$ satisfies the Siegel–Walfisz condition: the last factor does by Siegel–Walfisz, and convolving with sequences supported on $x^\eta$-rough integers preserves it for moduli $q\le\log^Ax$. Is that argument sound?
- **Q2c.** Boundary boxes are bounded by the trivial estimate $\sum_{d\le x}|\Delta(G;b\bmod d)|\ll(\mu(G)x)^{1/2}\log^{O(1)}x+\mu(G)\log x$, obtained from Cauchy–Schwarz and $\sum\tau(|m-b|)^2\ll x\log^3x$. Is the bookkeeping, with the number of boxes $\ll\log^{r(B+1)}x$, correct?

## 3. Theorem A: the class of dilation–spectral certificates (Definition 6.1)

Theorem A (Theorem 6.6, p. 18) and its uniform form, Corollary 6.11 (p. 19), are only as good as the class in Definition 6.1 (p. 16). Its conditions (A1)–(A4) are designed to contain the Helfgott–Radziwiłł and Pilatte certificates adapted to the shift 2. The comparison is in Table 2 and Remark 6.2.

- **Q3a. Multiplicativity, (A3).** We require the test functions to be multiplicative, $f=F\mathbf 1_X$ and $g=G\mathbf 1_X$. We argue that otherwise the comparison term becomes a parity-sensitive twin correlation, so the method would be circular. Is this restriction a fair description of what these methods can do? Is there a natural non-multiplicative adaptation that the theorem misses?
- **Q3b. Restriction set, (A4).** We require $|X\cap\mathcal K|\ge\frac12|\mathcal K|$. We verify this for the main part of the exceptional sets (integers with too many prime factors in $P$). We *assume* it for Helfgott–Radziwiłł's $N/\sqrt{H_0}$ part and for Pilatte's technical set (Pilatte, Def. 7.4). Is that assumption plausible, or could these sets concentrate on $\mathcal K$?
- **Q3c. Resolution.** Is $\mathrm{res}_R=\|A\|\,\|f\|\,\|g\|/\mathrm{cap}_R$ the right measure? In particular, could a certificate exploit cancellation between the $R$-part and the non-$R$ part of $\langle f,Ag\rangle$ in a way the definition does not capture?
- **Q3d. Uniformity in $z$.** Corollary 6.11 uses Lemma 6.5(ii) uniformly for $z\ge z_0$, via Buchstab's asymptotic with error $O(Y/\log^2z)$ uniform in $u\ge1$. Is that uniformity correct?

## 4. Theorem E: the class of entropy-decrement certificates (Definition 6.12)

Theorem E (Theorem 6.15, p. 21) proves reach $z\le(\log x)^{O(\varepsilon^4)}$ for the class in Definition 6.12, conditions (E0)–(E3). Its two ingredients are Lemma 6.13 (decoupling cannot beat $\sqrt{\sigma\theta}$) and Proposition 6.14 (the decrement inequality alone needs a double-exponential range).

- **Q4a. (E3).** We claim that Tao's decoupling step (Tao 2016, Lemmas 3.3 and 3.5) uses only the mutual-information bound, the independence of the residues, and boundedness of the per-prime terms. Our class also allows sparsity, i.e. Bernstein-type decoupling. Is that an accurate account of Tao's argument?
- **Q4b. (E0).** We force the primes used to be at least $z$, because the dilation identity $h(pn)=-h(n)$ fails for $p<z$ when $h=\lambda\mathbf 1_{z\text{-rough}}$. Could an entropy argument use primes below $z$ through a modified identity, and so escape the class?
- **Q4c. The search for a good scale.** Proposition 6.14 exhibits numbers satisfying (E1)–(E2) for which no good scale exists. Is it legitimate to conclude a limitation for "any argument that finds a good scale from (E1)–(E2) alone"? Does Tao's Lemma 3.2 indeed use nothing beyond (E1)–(E2)?
- **Q4d. The entropy budget.** We assume $h_0\ge c_1/\log z$, which holds for the trivial counting bound. Is it reasonable to regard a smaller provable budget as out of reach, since it would itself be a non-randomness statement about $\lambda$ on rough integers?

## 5. Novelty (optional)

- **Q5.** Are you aware of earlier statements of any of the following?
  - Theorem A or Theorem E, as limitation theorems for these method classes;
  - the explicit identity in Theorem B with $\Lambda_2^\flat=\mu^2\Lambda_2$, including the one-sided terms $D_j^\flat=(1-\delta^{(j)})M^\flat$;
  - the two-sided coherence $u(s,r')=(\delta_x-1)(-1)^{s+r'}$ (Theorem C).

  Our own literature check is summarised in Section 1.6.

---

*Contact:* wangliang.f@gmail.com. Any comments are appreciated; we will acknowledge all help in the paper.
