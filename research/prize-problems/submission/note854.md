# Gaps between totatives of primorials: the smallest missing even gap (Erdős Problem #854)

Liang Wang, with AI assistance (Claude, Anthropic). Draft of 2026-10-31.

## Summary

Let $P_k=p_1p_2\cdots p_k$ be the $k$-th primorial, and let $1=a_1<a_2<\cdots$ be the integers coprime to $P_k$. Two quantities matter here:
- $s(k)$, the smallest even integer that is **not** of the form $a_{i+1}-a_i$ (OEIS [A389839](https://oeis.org/A389839));
- $J(k)=\max_i(a_{i+1}-a_i)$, the Jacobsthal function of $P_k$ (OEIS [A048670](https://oeis.org/A048670)).

Erdős Problem [#854](https://www.erdosproblems.com/854) asks for an estimate of $s(k)$, and whether $\gg J(k)$ even integers occur as gaps. We prove the following.

- **Theorem A.** $s(k)\ge\bigl(\frac{e^\gamma}{1+e^\gamma}-o(1)\bigr)p_k\approx0.6404\,p_k$.
- **Theorem B.** For every $\varepsilon>0$ and all large $k$,
$$s(k)\ge\Bigl(\frac{e^\gamma}{8C_f}-\varepsilon\Bigr)\frac{p_k\log p_k\,\log_3p_k}{(\log_2p_k)^2},\qquad C_f=\prod_q\Bigl(1+\frac{2q-1}{(q-1)^3}\Bigr)=8.4425\ldots$$
  The constant is about $0.026$.
- **Theorem C.** There is an absolute constant $c'>0$ such that, for all large $k$,
$$s(k)\ge c'\,\frac{p_k\log p_k\,\log_3p_k}{\log_2p_k}.$$
  This is the order of the best known lower bound for $J(k)$, due to Ford, Green, Konyagin, Maynard and Tao [FGKMT].

**Consequence.** At least $s(k)/2-1$ distinct even integers occur as gaps. So the number of distinct even gaps is $\gg$ the best known lower bound for $J(k)$.

**What remains open.** The second question of #854 asks for $\gg J(k)$ itself, and the true order of $J(k)$ is unknown. The best known upper bound is $J(k)\ll p_k^2\log^2p_k$ (Iwaniec). Our results do not settle that question.

**Numerical data.** We computed $s(k)$ exactly for $k\le26$; the terms for $k=13,\dots,26$ are new. For $k\le26$, every even integer missing below $J(k)$ lies in $[J(k)-8,\,J(k)-2]$.

Notation: $\log_2=\log\log$, $\log_3=\log\log\log$, and $\gamma$ is Euler's constant.

**Logical status.**
- Theorems A and B are self-contained.
- Theorem C uses Theorem 2 of [FGKMT] as a black box, together with the deduction that follows it in their §3.
- The table in §5 is computational. How each entry was certified is described there.

---

## 1. The covering criterion

**Lemma 1.** Let $t$ be even. Then $t$ is a gap between consecutive totatives of $P_k$ if and only if there are residue classes $c_p \bmod p$, one for each $p\le p_k$, and an integer $A$, such that:
- $A$ and $A+t$ lie in no class $c_p$;
- every integer strictly between $A$ and $A+t$ lies in some class $c_p$.

*Proof.* By the Chinese remainder theorem, choose $N$ with $N+j\equiv0\pmod p$ exactly when $j\equiv c_p\pmod p$. Then $N+A$ and $N+A+t$ are totatives, and every integer strictly between them shares a prime factor with $P_k$. The converse is the same argument read backwards. ∎

When $A=0$ we can remove the prime $2$: the class $c_2=1$ is forced and covers the odd positions. Halving the remaining positions shows that $t=2m$ is a gap if and only if the points $1,\dots,m-1$ can be covered by one class per odd prime $p\le p_k$, each class avoiding $0$ and $m \bmod p$. This is the 0-1 program used in §5.

## 2. Theorem A (an averaging construction)

For even $t$, let $Q_t=\prod_{q<t}q$. Choose $a \bmod Q_t$ uniformly among the classes with $a\not\equiv0,-t\pmod q$ for all $q<t$. Let $R(a)$ be the number of $0<i<t$ with $\gcd(a+i,Q_t)=1$. By the Chinese remainder theorem,
$$E(t):=\mathbb E\,R(a)=\sum_{0<i<t}\prod_{q<t,\ q\nmid i(t-i)}\Bigl(1-\frac1{q-\nu_q}\Bigr),$$
where $\nu_q=1$ if $q\mid t$ and $\nu_q=2$ otherwise.

**Covering by large primes.** Suppose $t<p_k$ and $\pi(p_k)-\pi(t)\ge E(t)$. Take $a$ with $R(a)\le E(t)$. Assign to each of the $R(a)$ exceptional points $u$ its own prime $p\in(t,p_k]$, with the class that covers $u$. Since $0<u<t<p$, this class covers neither endpoint. Give every unused prime $p>t$ any class that avoids both endpoints. Then $t$ is a gap.

**Asymptotics of $E(t)$.**
- Averaged over $i \bmod q$, the local factor at $q$ is exactly $1-1/q$.
- Write the factor at $q$ as $(1-1/q)(1+g_q)$. The product of the factors $1+g_q$ over $q>\tfrac12\log t$ is $1+o(1)$, uniformly in $i$.
- The product over $q\le\tfrac12\log t$ is periodic with period $t^{1/2+o(1)}$ and has mean $1$.
- Hence, by Mertens' theorem, $E(t)\sim e^{-\gamma}t/\log t$.

The condition $\pi(p_k)-\pi(t)\ge E(t)$ becomes $(1+e^{-\gamma}+o(1))\,t/\log t\le p_k/\log p_k$. This gives Theorem A.

## 3. Theorem B (an Erdős–Rankin construction with free endpoints)

**Parameters.** Put $x=p_k$, $L_2=\log_2x$ and $L_3=\log_3x$. Fix $\eta>0$, and let
$$u=(1+\eta)L_2/L_3,\qquad z=x^{1/u},\qquad \lambda=c\,\log x\cdot L_3/L_2^2\ \text{ with }c<e^\gamma/(8C_f(1+\eta)).$$
Let $t\le\lambda x$ be even. We use endpoints $1$ and $t+1$, so the positions $2,\dots,t$ must be covered.

**(A) Medium primes $z<p\le x/2$.**
- Give each such $p$ the class $0$ if $p\nmid t+1$, and otherwise any class that avoids both endpoints.
- At most $2u$ primes are of the second kind. The positions they fail to cover form a set $E$ with $|E|\le 2u(t/z+1)$.
- Every surviving position, apart from $E$, is either $z$-smooth or of the form $mP$ with $m\le2\lambda$ and $P>x/2$ prime.

**(B) Small primes $q\le z$.** Give each one a uniformly random class among those avoiding the endpoints. For a surviving position $i$, the probability that it remains uncovered is at most
$$W(z)\,H(i-1)\,H(t+1-i),\qquad W(z)=\prod_{q\le z}(1-1/q),\qquad H(n)=\prod_{q\mid n,\,q\le z}(1-1/q)^{-1}.$$
Use $H(a)H(b)\le\tfrac12\bigl(H(a)^2+H(b)^2\bigr)$, then truncate $H$ at $(\log x)^2$; this costs only a factor $1+o(1)$. Then expand
$$H^2=\sum_{d\mid n}f(d),\qquad f(q)=\frac{2q-1}{(q-1)^2}.$$
- Brun–Titchmarsh for $d\le x^{1/2}$ gives
$$\sum_{x/2<P\le Y}H(mP-1)^2\le(4C_f+o(1))\frac{Y}{\log x}.$$
- The terms with $d>x^{1/2}$ are negligible by Rankin's trick.
- The smooth positions and $E$ are negligible: Canfield–Erdős–Pomerance gives $\Psi(t,z)\le t(\log x)^{-1-\eta/2}$, and the trivial bound $H\ll L_2$ suffices on them.

So some choice of classes leaves
$$|S_B|\le(1+o(1))\,4C_fe^{-\gamma}\,u\,\frac{\lambda(1+\log 2\lambda)\,x}{(\log x)^2}<(1-o(1))\frac{x}{2\log x}$$
uncovered positions.

**(C) Large primes $x/2<p\le x$.** Match each remaining position $v$ to its own large prime $p\nmid(v-1)(t+1-v)$, with the class of $v$. Each $v$ excludes at most two such primes, because both $v-1$ and $t+1-v$ are less than $(x/2)^2$. So the matching succeeds, and Theorem B follows by letting $\eta\to0$. ∎

The averaging over shifted primes in (B) is what reaches Rankin's order. Bounding $H(i-1)H(t+1-i)$ by its maximum instead loses a factor $(\log_2x)^2$.

Numerically, for $x=10^5,\dots,10^7$, the mean of $H(i-1)H(t+1-i)$ over the surviving positions stays between $4.5$ and $5.5$. Its maximum grows from $56$ to $64$.

## 4. Theorem C (transfer from the FGKMT sieving theorem)

**The FGKMT theorem [FGKMT, §3].** Let
$$y=c\,x\log x\,L_3/L_2,\qquad z=x^{L_3/(4L_2)},$$
$$\mathcal S=\{\log^{20}x<s\le z\},\qquad \mathcal P=\{x/2<p\le x\},\qquad \mathcal Q=\{x<q\le y\},$$
where each set consists of primes. Their Theorem 2 gives classes $\vec a$ on $\mathcal S$ and $\vec b$ on $\mathcal P$ such that $\#(\mathcal Q\cap S(\vec a)\cap S(\vec b))\ll x/\log x$.

Give class $0$ to every other prime $p\le x$. Then the set $T$ of uncovered integers in $(x,y]$ satisfies $\#T\le Kx/\log x$.

**Proof of Theorem C.**
- Let $X=p_k$ and $x=X/C$, where $C\ge K+3$ is a constant. Fix $\vec a$ and $\vec b$, and fix an even $t\le y/2$.

- **Step 1: endpoints.** Call $A\in(x,y-t]$ a *candidate* if:
  - $s\nmid A(A+t)$ for every prime $s\le\log^{20}x$;
  - $A\not\equiv a_s$ and $A+t\not\equiv a_s\pmod s$ for every $s\in\mathcal S$.

  This is a two-dimensional sieve problem with sifting limit $z$, sieving the interval at level $D=y^{1/2}$; note $\log D/\log z\to\infty$. The fundamental lemma applies for arbitrary residue classes, so there are $N_c\gg y/(\log z)^2$ candidates.

  Let $I(A)$ be the number of $p\in\mathcal P$ with $b_p\equiv A$ or $b_p\equiv A+t\pmod p$. Then $\sum_A I(A)\le3y/\log x$. So some candidate has
  $$I(A)\ll\frac{(\log z)^2}{\log x}\le\log x.$$

- **Step 2: classes and repairs.**
  - Keep $\vec a$, $\vec b$ and the zero classes, with two kinds of change.
  - A prime $s\in(z,x/2]$ that divides $A(A+t)$ gets a class avoiding both endpoints. There are at most $3u$ such primes, where $u=4L_2/L_3$.
  - The at most $\log x$ primes $p\in\mathcal P$ whose class $b_p$ hits an endpoint get new classes avoiding both endpoints.
  - Primes $s\le\log^{20}x$ never hit an endpoint, because $A$ is a candidate.

- **Step 3: what is left.** The integers in $(A,A+t)$ still uncovered lie in $T$, or among the multiples of repaired zero-class primes, or among positions previously covered by repaired large primes. The second set has at most $3u(y/z+1)=o(x/\log x)$ elements, and the third $\ll\log^2x$. In total there are at most $(K+o(1))\,x/\log x$ of them.

- **Step 4: final cover.** Cover each remaining position $v$ with its own prime $p\in(x,Cx]$ such that $p\nmid(v-A)(A+t-v)$. Each $v$ excludes at most two such primes, since both factors are less than $x^2$. There are $(C-1+o(1))\,x/\log x$ such primes, which is enough.

By Lemma 1, every even $t\le y/2$ is a gap. Therefore
$$s(k)>\frac y2\sim\frac c{2C}\cdot\frac{p_k\log p_k\,L_3}{L_2}.\qquad ∎$$

**Remarks.**
- **Why the endpoints are rough numbers.** If both endpoints in $(x,y]$ had to be primes, every $t$ would have to be a difference of two primes. That is a twin-prime-type statement, beyond the parity barrier. Requiring only that the endpoints be rough needs nothing but the fundamental lemma.
- **Generality.** The argument uses only the form of FGKMT's Theorem 2. Any future sieving theorem of the same shape transfers to $s(k)$ with the same order.

## 5. Exact values for $k\le26$

**Method.**
- For each $k$ and each even $t\le J(k)$, decide the 0-1 covering program of §1. For $t\le J(k)$ we use the values of $J(k)$ from A048670.
- If $t$ is a gap, record an explicit witness $N$: $\gcd(N,P_k)=\gcd(N+t,P_k)=1$, and $\gcd(N+j,P_k)>1$ for $0<j<t$.
- If $t$ is not a gap, the program was found infeasible by HiGHS (via SciPy). We re-ran every such case with CP-SAT (OR-Tools) under a one-hour limit per case.
  - For $k\le21$, CP-SAT also found every non-gap infeasible.
  - For $k=22,24,25$ (the non-gaps $t=194$; $230$; $254,256$), CP-SAT reached its time limit. So $s(22)$, $s(24)$ and $s(25)$ currently rest on HiGHS alone.
  - Neither solver produces a machine-checkable certificate of infeasibility.
- When no even $t\le J(k)$ is missing, $s(k)=J(k)+2$, because $J(k)$ is the largest gap.
- The witnesses, and a checker that uses only the Python standard library, are in the repository (§7).

**Table.**

| $k$ | $p_k$ | $J(k)$ | $s(k)$ | missing even $t<J(k)$ |
|---|---|---|---|---|
| 13 | 41 | 74 | 76 | — |
| 14 | 43 | 90 | 86 | 86, 88 |
| 15 | 47 | 100 | 98 | 98 |
| 16 | 53 | 106 | 108 | — |
| 17 | 59 | 118 | 120 | — |
| 18 | 61 | 132 | 134 | — |
| 19 | 67 | 152 | 146 | 146 |
| 20 | 71 | 174 | 166 | 166, 170, 172 |
| 21 | 73 | 190 | 182 | 182, 186, 188 |
| 22 | 79 | 200 | 194 | 194 |
| 23 | 83 | 216 | 218 | — |
| 24 | 89 | 234 | 230 | 230 |
| 25 | 97 | 258 | 254 | 254, 256 |
| 26 | 101 | 264 | 266 | — |

For $k\le12$ our values agree with the existing terms of A389839. For $k\le26$ every missing even number lies in $[J(k)-8,\,J(k)-2]$.

On this evidence, $J(k)-s(k)$ might be $o(J(k))$, or even bounded. This is unproved. If true, it would answer the second question of #854 affirmatively.

## 6. AI assistance

This work was produced with substantial assistance from an AI system (Claude, Anthropic), working under the direction of the author. The AI system drafted the proofs, wrote and ran the computations, and searched the literature. The author chose the problem and the direction, and is responsible for the content.

The proofs have not yet been refereed. Independent checking, especially of §4, is welcome.

## 7. References and files

- [FGKMT] K. Ford, B. Green, S. Konyagin, J. Maynard, T. Tao, *Long gaps between primes*, J. Amer. Math. Soc. 31 (2018), 65–105. arXiv:1412.5029.
- E. R. Canfield, P. Erdős, C. Pomerance, *On a problem of Oppenheim concerning "factorisatio numerorum"*, J. Number Theory 17 (1983).
- H. L. Montgomery, R. C. Vaughan, *The large sieve*, Mathematika 20 (1973) (Brun–Titchmarsh).
- J. Friedlander, H. Iwaniec, *Opera de Cribro*, AMS 2010, Ch. 6 (fundamental lemma).
- R. A. Rankin, *The difference between consecutive prime numbers*, J. London Math. Soc. 13 (1938).
- Repository: https://github.com/maris205/twin_primes/tree/main/research/prize-problems
  - Chinese stage reports: `STAGE1_GAPS.md`, `STAGE3_LOGLOSS.md`, `STAGE4_FGKMT.md`.
  - Witnesses: `a389839_witnesses.json`.
  - Checker: `verify_a389839.py`.
