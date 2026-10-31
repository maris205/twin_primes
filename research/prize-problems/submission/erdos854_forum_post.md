Draft comment for https://www.erdosproblems.com/forum/thread/854. To be posted by the author; nothing has been posted.

---

**Lower bounds for the smallest missing even gap, and exact values up to k = 26**

Write $s(k)$ for the smallest even number that is not a gap between consecutive totatives of the $k$-th primorial (OEIS A389839). Write $J(k)$ for the largest gap (A048670). We prove three lower bounds for $s(k)$; the full write-up is linked below.

1. $s(k)\ge(e^\gamma/(1+e^\gamma)-o(1))\,p_k\approx0.64\,p_k$. This comes from an averaging construction and is elementary.
2. $s(k)\gg p_k\log p_k\,\log_3p_k/(\log_2p_k)^2$, with the explicit constant $e^\gamma/(8C_f)\approx0.026$. This is an Erdős–Rankin construction in which the two endpoints are kept uncovered. The endpoint weight is controlled on average over shifted primes, using Brun–Titchmarsh.
3. $s(k)\gg p_k\log p_k\,\log_3p_k/\log_2p_k$. This is the order of the Ford–Green–Konyagin–Maynard–Tao lower bound for $J(k)$.
   - The proof uses their "sieving primes" theorem (Theorem 2 of *Long gaps between primes*) as a black box.
   - The two endpoints are taken to be a pair of rough numbers at distance $t$, which the fundamental lemma of sieve theory provides. Insisting on prime endpoints would run into the parity problem.
   - Conflicts with the large-prime classes are avoided by averaging over candidate endpoints.

**Consequence for the first question.** At least $s(k)/2-1$ distinct even numbers occur as gaps. This number is therefore $\gg$ the best known lower bound for $J(k)$.

**The second question remains open.** It asks for $\gg J(k)$ itself, and the true order of $J(k)$ is unknown.

**Data.** We computed $s(k)$ exactly for $k\le26$:

76, 86, 98, 108, 120, 134, 146, 166, 182, 194, 218, 230, 254, 266 (k = 13, …, 26).

- For every even $t\le J(k)$, a gap comes with an explicit witness $n$.
- A non-gap was found infeasible by HiGHS. For $k\le21$, CP-SAT confirmed every non-gap independently. For $k=22,24,25$, CP-SAT timed out after one hour per case, so those three values rest on a single solver.
- For $k\le26$, all missing even numbers lie in $[J(k)-8,\,J(k)-2]$. This suggests that $J(k)-s(k)$ may be small compared with $J(k)$, which would answer the second question positively. This is only a numerical observation.

**Disclosure.** This work was done with substantial AI assistance (Claude, Anthropic). The AI system drafted the proofs and ran the computations; I chose the direction and checked the write-up. The proofs have not been refereed, and I would be grateful for corrections, especially on the black-box transfer in part 3.

- Write-up: https://github.com/maris205/twin_primes/blob/main/research/prize-problems/submission/note854.md
- Witnesses and checker: `a389839_witnesses.json` and `verify_a389839.py` in the same directory's parent folder.
