Draft comment for https://www.erdosproblems.com/forum/thread/854. To be posted by the author; nothing has been posted.

---

**Lower bounds for the smallest missing even gap, and exact values up to k = 26**

Write $s(k)$ for the smallest even number that is not a gap between consecutive totatives of the $k$-th primorial (OEIS A389839). Write $J(k)$ for the largest gap (A048670). We prove three lower bounds for $s(k)$, a transfer theorem, a counting theorem and an almost-all version of both; the full write-up is linked below.

1. $s(k)\ge(e^\gamma/(1+e^\gamma)-o(1))\,p_k\approx0.64\,p_k$. This comes from an averaging construction and is elementary.
2. $s(k)\gg p_k\log p_k\,\log_3p_k/(\log_2p_k)^2$, with the explicit constant $e^\gamma/(8C_f)\approx0.026$. This is an Erdős–Rankin construction in which the two endpoints are kept uncovered. The endpoint weight is controlled on average over shifted primes, using Brun–Titchmarsh.
3. $s(k)\gg p_k\log p_k\,\log_3p_k/\log_2p_k$. This is the order of the Ford–Green–Konyagin–Maynard–Tao lower bound for $J(k)$.
   - The proof uses their "sieving primes" theorem (Theorem 2 of *Long gaps between primes*) as a black box.
   - The two endpoints are taken to be a pair of rough numbers at distance $t$, which the fundamental lemma of sieve theory provides. Insisting on prime endpoints would run into the parity problem.
   - Conflicts with the large-prime classes are avoided by averaging over candidate endpoints.

4. **Transfer.** There is an absolute $\delta_0>0$ such that, for fixed $\varepsilon,\eta>0$ and all large $k$, with $j=\lceil(1-\eta)k\rceil$,
   $$(1-\varepsilon)\min\bigl(J(j),\,p_k^{1+\delta_0}\bigr)\le s(k)\le J(k)+2.$$
   - The proof starts from any covered interval at level $j$, picks two endpoints that are covered only by large primes (fundamental lemma), releases those primes, and repairs the few exposed points with the unused primes $p_{j+1},\dots,p_k$.
   - Item 3 follows from this and the FGKMT lower bound for $J$, without using the structure of their proof.

5. **Counting.** For fixed $\varepsilon\in(0,1)$, $\eta\in(0,\frac12)$ and all large $k$, the number of distinct even gaps is at least
   $$c(\varepsilon)\,\min\bigl(J(\lceil(1-\eta)k\rceil),\,p_k^{2-\varepsilon}\bigr).$$
   - The proof is that of item 4, but only for a positive proportion of $t$. This needs the linear sieve (sifting limit 2) in place of a lower-bound sieve of dimension 2, plus an upper-bound sieve and a Cauchy–Schwarz count of the differences.
   - Unconditionally, the number of even gaps is therefore at least $J(\lceil(1-\eta)k\rceil)^{1-\varepsilon}$ for large $k$.

6. **Short lag; almost all $k$.** In items 4 and 5 the level $\lceil(1-\eta)k\rceil$ can be replaced by $k-\lceil k^{1-\kappa}\rceil$ for a small $\kappa>0$, by taking the sieve level as large as the lower-bound sieve allows. Since $J$ grows at most polynomially, it can grow by a constant factor across such short windows for only $O(K^{1-\kappa}\log K)$ values $k\le K$. Hence, outside a set of $k$ of density zero, $s(k)\ge(1-\varepsilon)\min(J(k),p_k^{1+\delta_0})$ and the number of even gaps is at least $c(\varepsilon)\min(J(k),p_k^{2-\varepsilon})$.

**The second question is not settled for every $k$.** By item 6 it holds at every $k$ outside a set of density zero at which $J(k)\le p_k^{2-\varepsilon}$. For every large $k$ it would follow from $J(k)\ll J(k-\lceil k^{1-\kappa}\rceil)$ and $J(k)\le p_k^{2-\varepsilon}$ for some fixed $\varepsilon>0$. Both are expected, neither is proved; the second asks for a power saving over Iwaniec's bound $J(k)\ll p_k^2$. Both would follow from $J(2k)\le D\,J(k)$ with $D<4$ (the known values give $D\le3.09$ for $40\le k\le71$), but that would itself improve the exponent in Iwaniec's bound.

**Data.** We computed $s(k)$ exactly for $k\le26$:

76, 86, 98, 108, 120, 134, 146, 166, 182, 194, 218, 230, 254, 266 (k = 13, …, 26).

- For every even $t\le J(k)$, a gap comes with an explicit witness $n$.
- A non-gap was found infeasible by HiGHS. For $k\le22$, CP-SAT confirmed every non-gap independently. For $k=24,25$, CP-SAT timed out even after six hours per case, so those two values rest on a single solver.
- For $k\le26$, all missing even numbers lie in $[J(k)-8,\,J(k)-2]$. This suggests that $J(k)-s(k)$ may be small compared with $J(k)$, which would answer the second question positively. This is only a numerical observation.

**Disclosure.** This work was done with substantial AI assistance (Claude, Anthropic). The AI system drafted the proofs and ran the computations; I chose the direction and checked the write-up. The proofs have not been refereed, and I would be grateful for corrections, especially on parts 4–6 and on the black-box transfer in part 3.

- Write-up: https://github.com/maris205/twin_primes/blob/main/research/prize-problems/submission/note854.md
- Guide for checking the proofs: `REVIEW_GUIDE.md` in the same directory.
- Witnesses and checker: `a389839_witnesses.json` and `verify_a389839.py` in the same directory's parent folder.
