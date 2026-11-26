# Gaps between totatives of primorials: the smallest missing even gap (Erdős Problem #854)

Liang Wang, with AI assistance (Claude, Anthropic). Draft of 2026-11-22.

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

- **Theorem D (transfer).** There is an absolute constant $\delta_0>0$ such that, for fixed $\varepsilon,\eta\in(0,\frac12)$ and all large $k$, with $j=\lceil(1-\eta)k\rceil$,
$$(1-\varepsilon)\,\min\bigl(J(j),\,p_k^{1+\delta_0}\bigr)\ \le\ s(k)\ \le\ J(k)+2 .$$
  So, as long as $J$ is not larger than $p_k$ by a fixed power, $s(k)$ is as large as the Jacobsthal function at a slightly lower level. Theorem C follows from Theorem D and the lower bound of [FGKMT] for $J$.

- **Theorem E (counting).** For fixed $\varepsilon\in(0,1)$ and $\eta\in(0,\frac12)$ there is $c=c(\varepsilon)>0$ such that, for all large $k$, the number of distinct even gaps is at least
$$c\,\min\bigl(J(\lceil(1-\eta)k\rceil),\,p_k^{2-\varepsilon}\bigr).$$
  In particular it is at least $J(\lceil(1-\eta)k\rceil)^{1-\varepsilon}$ for all large $k$, unconditionally.

- **Theorem F (short lag; almost all $k$).** In Theorems D and E the level $\lceil(1-\eta)k\rceil$ can be replaced by $k-\lceil k^{1-\kappa}\rceil$ for a fixed small $\kappa>0$. Since $J$ grows at most polynomially, it can grow by a constant factor across such short windows only for a sparse set of $k$. Consequently, for every fixed $\varepsilon>0$, outside a set of $k$ of density zero,
$$s(k)\ge(1-\varepsilon)\min\bigl(J(k),p_k^{1+\delta_0}\bigr),\qquad\#\{\text{even gaps}\}\ge c(\varepsilon)\min\bigl(J(k),p_k^{2-\varepsilon}\bigr).$$

**Consequence.** At least $s(k)/2-1$ distinct even integers occur as gaps. So the number of distinct even gaps is at least $(\frac12-\varepsilon)\min\bigl(J(\lceil(1-\eta)k\rceil),p_k^{1+\delta_0}\bigr)$; Theorem E extends the range to $p_k^{2-\varepsilon}$ with a smaller constant.

**What remains open.** The second question of #854 asks for $\gg J(k)$ gaps. By Theorem F it holds at every $k$ outside a set of density zero at which $J(k)\le p_k^{2-\varepsilon}$. For every large $k$ it would follow from

- (R1) $J(k)\ll J\bigl(k-\lceil k^{1-\kappa}\rceil\bigr)$, i.e. $J$ does not grow by a large factor across a window of length $k^{1-\kappa}$, and
- (R2) $J(k)\le p_k^{2-\varepsilon}$ for some fixed $\varepsilon>0$.

(R1) fails for at most $O(K^{1-\kappa}\log K)$ values $k\le K$ (§6.3), but it is not proved for every $k$. The best known upper bound is $J(k)\ll(k\log k)^2\asymp p_k^2$ (Iwaniec), so (R2) asks for any power saving over it. So the second question is reduced to the regularity of the Jacobsthal function, and is not settled for every $k$.

**Numerical data.** We computed $s(k)$ exactly for $k\le26$; the terms for $k=13,\dots,26$ are new. For $k\le26$, every even integer missing below $J(k)$ lies in $[J(k)-8,\,J(k)-2]$.

Notation: $\log_2=\log\log$, $\log_3=\log\log\log$, and $\gamma$ is Euler's constant.

**Logical status.**
- Theorems A and B are self-contained.
- Theorem C uses Theorem 2 of [FGKMT] as a black box, together with the deduction that follows it in their §3.
- Theorem D uses only the fundamental lemma of sieve theory. It gives a second proof of Theorem C that needs only the statement of the [FGKMT] lower bound for $J$.
- Theorem E uses two standard sieve theorems: the Jurkat–Richert lower bound for the linear sieve and a Selberg-type upper bound.
- Theorem F uses the same sieve theorems as Theorems D and E, and Iwaniec's upper bound for $J$.
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
  - For $k\le22$, CP-SAT also found every non-gap infeasible. For $k=22$ this needed a six-hour run (`stage5_cpsat_long.py`, which adds a mirror-symmetry break and a redundant counting constraint, both sound).
  - For $k=24,25$ (the non-gaps $t=230$; $254,256$), CP-SAT reached its time limit both at one hour and at six hours. So $s(24)$ and $s(25)$ currently rest on HiGHS alone.
  - Neither solver produces a machine-checkable certificate of infeasibility.
- When no even $t\le J(k)$ is missing, $s(k)=J(k)+2$, because $J(k)$ is the largest gap.
- The witnesses, and a checker that uses only the Python standard library, are in the repository (§8).

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

## 6. Theorem D and the second question

### 6.1 Theorem D

A *covered interval at level $j$* is a choice of classes $c_p \bmod p$, $p\le p_j$, such that every integer of $[1,L]$ lies in some class. The maximal gap gives one with $L=J(j)-1$, and any sub-interval of a covered interval is covered.

**Theorem D.** There is an absolute constant $\delta_0>0$ with the following property. Fix $\varepsilon,\eta\in(0,\frac12)$. For all large $k$, put $j=\lceil(1-\eta)k\rceil$ and $L=\min\bigl(J(j)-1,\,p_k^{1+\delta_0}\bigr)$. Then every even $t\le(1-\varepsilon)L$ is a gap between consecutive totatives of $P_k$.

*Proof.* Take a covered interval $[1,L]$ at level $j$ with classes $c_p$. Call the primes $p_{j+1},\dots,p_k$ *free*; there are $F=k-j\ge\eta k-1$ of them, all larger than $p_j$. Fix an even $t\le(1-\varepsilon)L$ and put $X=L-t\ge\varepsilon L$. We look for $x\in[1,X]$ and new classes such that $x$ and $x+t$ are uncovered and every integer strictly between them is covered; Lemma 1 with $A=x$ then gives the claim.

- **Parameters.** Let $B=K\,L\log p_k/(\eta p_k)$ with $K$ a large absolute constant. Since $J(j)/p_k\to\infty$ (Theorem B), $L\ge p_k/\varepsilon$ and $B\to\infty$. Since $L\le p_k^{1+\delta_0}$, $B\le p_k^{\delta_0+o(1)}$.
- **Step 1: good starting points.** For $p\le B$ let $\Omega_p=\{c_p,\,c_p-t\}\bmod p$ and $\rho(p)=|\Omega_p|$. Then $\rho(2)=1$ because $t$ is even, and $\rho(p)\le2<p$ for $p\ge3$. Let $\mathcal X$ be the set of $x\in[1,X]$ with $x\bmod p\notin\Omega_p$ for all $p\le B$, and $V=\prod_{p\le B}(1-\rho(p)/p)\gg1/\log^2B$. So $x\in\mathcal X$ means that neither $x$ nor $x+t$ lies in the class of a prime $p\le B$. By the fundamental lemma (dimension 2, arbitrary classes) there is an absolute constant $s_0$ such that:
  - (S1) if $X\ge B^{s_0}$, then $|\mathcal X|\ge\frac12XV$;
  - (S2) for a prime $q>B$ and any $a$, if $X/q\ge B^{s_0}$, then $\#\{x\in\mathcal X: x\equiv a\ (\mathrm{mod}\ q)\}\le2(X/q)V$.

  Take $\delta_0=1/(2s_0)$. Then $B^{s_0}\le p_k^{1/2+o(1)}\le X$, so (S1) applies.
- **Step 2: release the primes that cover the endpoints.** For $x\in\mathcal X$ let $Q(x)$ be the set of primes $q\le p_j$ with $x\in c_q$ or $x+t\in c_q$; all of them exceed $B$. Give each a new class avoiding $x$ and $x+t$. The *exposed* points are the $z\in(x,x+t)$ all of whose covering primes lie in $Q(x)$. They lie in $\bigcup_{q\in Q(x)}c_q$, so their number is at most $\mathrm{cost}(x)=\sum_{q\in Q(x)}(t/q+1)$.
- **Step 3: the average cost is small.** Let $N_q=\#\{x\in\mathcal X:q\in Q(x)\}$, so $\sum_{x\in\mathcal X}\mathrm{cost}(x)=\sum_{B<q\le p_j}(t/q+1)N_q$.
  - For $q\le X/B^{s_0}$, (S2) gives $N_q\le4(X/q)V$. These primes contribute at most $4XV\bigl[2t/(B\log B)+2\log\log p_k\bigr]$.
  - For $X/B^{s_0}<q\le p_j$, trivially $N_q\le4X/q$ (note $q\le p_j\le X$). These primes contribute at most $4X\bigl[2tB^{s_0}/X+1\bigr]\le4X\bigl[2B^{s_0}/\varepsilon+1\bigr]$.

  Dividing by $|\mathcal X|\ge\frac12XV$, the average cost is at most
  $$\frac{16\,t}{B\log B}+16\log\log p_k+\frac{C_1}{\varepsilon}B^{s_0}\log^2B .$$
  The first term is at most $16L/B=16\eta p_k/(K\log p_k)\le F/6$ for large $K$. The other two are $o(F)$, because $B^{s_0}\le p_k^{1/2+o(1)}$ and $F\asymp\eta p_k/\log p_k$. So some $x\in\mathcal X$ has at most $F/2$ exposed points. Fix it.
- **Step 4: repair with the free primes.** Give each exposed $z$ its own free prime $\ell_z$ with the class $z\bmod\ell_z$, where $\ell_z\nmid(z-x)(x+t-z)$, so that $\ell_z$ covers neither endpoint. Both factors are positive integers below $t\le p_k^{1+\delta_0}<p_j^2$, so each has at most one prime factor above $p_j$, and $z$ excludes at most two free primes. As there are at most $F/2\le F-2$ exposed points, a greedy choice works. The unused free primes get any class avoiding $x$ and $x+t$.
- **Step 5: check.** The primes that covered $x$ or $x+t$ were all re-classed away from them, and the free primes avoid them. Each $z\in(x,x+t)$ was covered originally, because $(x,x+t)\subset[1,L]$: either one of its covering primes is unchanged, or $z$ is exposed and covered by $\ell_z$. ∎

**Corollaries.**
- $(1-\varepsilon)\min\bigl(J(\lceil(1-\eta)k\rceil),p_k^{1+\delta_0}\bigr)\le s(k)\le J(k)+2$. The upper bound holds because $J(k)+2$ exceeds the largest gap.
- Theorem C: insert the lower bound of [FGKMT] for $J(j)$ and use $p_j\asymp p_k$.
- **Second question, conditionally.** If $J(k)\le C\,J(\lceil(1-\eta)k\rceil)$ and $J(k)\le p_k^{1+\delta_0}$, then the number of even gaps is at least $\frac{1-\varepsilon}{2C}J(k)-1$.
- **Second question, at most scales.** Suppose $J(k)\le p_k^{1+\delta_0}$ for all large $k$. Let $\rho=1/(1-\eta)$ and $k_i=\lceil\rho^i\rceil$. Since $J(k_n)\le\rho^{2n}$ for large $n$ and $J$ is non-decreasing, at least half of the $i\le n$ satisfy $J(k_{i+1})\le\rho^4J(k_i)$, and for those $k=k_{i+1}$ the previous item applies.

**Remarks.**
- The lag can be shortened: with $F=\lceil k/\log^Ak\rceil$ free primes and $B$ larger by a factor $\log^Ak$, the same proof works with $j=k-F$. Numerically $s(k)>J(k-1)$ for $6\le k\le26$, which this proof does not reach.
- The cap $p_k^{1+\delta_0}$ comes from Step 1: the sieve must reach $B\approx(L/p_k)\log p_k$ in an interval of length about $L$.

**Numerical run of the construction.** Script `stage7_transfer.py`. The base is a long greedy cover at level $j$ (not maximal). For each even $t$ the script finds $x$, releases $Q(x)$, repairs by a bipartite matching with the free primes, and then checks the final cover directly. Every success is a proof that $t$ is a gap of $P_k$.

| $k$ | $p_k$ | $j$ | free primes | length of base cover | every even $t$ succeeds up to | that value / $p_k$ |
|---|---|---|---|---|---|---|
| 60 | 281 | 30 | 30 | 254 | 254 | 0.9 |
| 60 | 281 | 45 | 15 | 530 | 494 | 1.76 |
| 100 | 541 | 50 | 50 | 566 | 566 | 1.05 |
| 100 | 541 | 75 | 25 | 1088 | 1080 | 2.0 |
| 100 | 541 | 90 | 10 | 1422 | 1320 | 2.44 |
| 200 | 1223 | 100 | 100 | 1644 | 1644 | 1.34 |
| 200 | 1223 | 150 | 50 | 2998 | 2970 | 2.43 |
| 200 | 1223 | 180 | 20 | 3920 | 3872 | 3.17 |
| 300 | 1987 | 150 | 150 | 2998 | 2994 | 1.51 |
| 300 | 1987 | 225 | 75 | 5328 | 5286 | 2.66 |
| 300 | 1987 | 270 | 30 | 6748 | 6686 | 3.36 |
| 400 | 2741 | 300 | 100 | 7852 | 7830 | 2.86 |
| 400 | 2741 | 360 | 40 | 10142 | 10022 | 3.66 |

So, for example, $s(100)\ge1322$, $s(200)\ge3874$, $s(300)\ge6688$ and $s(400)\ge10024$. In every row at least 92% of the length of the base cover is transferred, and at least 98.8% when there are 20 or more free primes.

### 6.2 Theorem E

Theorem D shows that *every* even $t$ in a range is a gap, and needs a lower-bound sieve of dimension 2. The second question only asks for the *number* of gaps. For that a positive proportion of $t$ is enough, and a lower-bound sieve of dimension 1 suffices; its sifting limit is 2, which is why the range extends to $p_k^{2-\varepsilon}$.

**Theorem E.** Fix $\varepsilon\in(0,1)$ and $\eta\in(0,\frac12)$. There is $c=c(\varepsilon)>0$ such that for all large $k$, with $j=\lceil(1-\eta)k\rceil$ and $L=\min\bigl(J(j)-1,\,p_k^{2-\varepsilon}\bigr)$, at least $cL$ even integers $t\le L/2$ are gaps between consecutive totatives of $P_k$.

**Two sieve theorems.** Let $I$ be an interval of $N$ integers, and for each prime $p\le z$ let $\omega(p)$ residue classes be given, with $\omega(2)\le1$ and $\omega(p)\le2$. Both statements use only that the number of integers of $I$ lying in given classes for all $p\mid d$ is $N\omega(d)/d+O(\omega(d))$, so they hold for arbitrary classes.

- **(L)** (Jurkat–Richert; [HR, Theorem 8.4]). If every $\omega(p)=1$ and $N\ge z^{2+\theta}$ with $\theta>0$ fixed and $z$ large, then at least $c_0(\theta)N/\log z$ integers of $I$ avoid all the classes.
- **(U)** ([HR, Theorem 2.2]). If $2\le z\le N$, then at most $C\,N\prod_{p\le z}(1-\omega(p)/p)$ integers of $I$ avoid all the classes.

*Proof of Theorem E.* Take a covered interval $[1,L]$ at level $j$ with classes $c_p$. There are $F=k-j\ge\eta p_k/(2\log p_k)$ free primes. Let $B=K\,L\log p_k/(\eta p_k)$, with $K=K(\varepsilon)$ large, and $M=L/(2p_k)$.

- **Parameters.** By Theorem B, $M\ge(\log p_k)^{1/2}$, so $B\to\infty$ and $\log B\le3\log M+O(1)$. Since $L\le p_k^{2-\varepsilon}$, we have $\log B\le\bigl(\frac{1-\varepsilon}{2-\varepsilon}+o(1)\bigr)\log L$, so $L\ge B^{2+\varepsilon}$ for large $k$. This is the only place where $L\le p_k^{2-\varepsilon}$ is used.
- **Step 1: survivors of the small primes.** Let $S$ be the set of $x\in[1,L]$ lying in no class $c_p$ with $p\le B$. All elements of $S$ have the same parity. By (L) with $\theta=\varepsilon/2$, every sub-interval of $[1,L]$ of length at least $L/2-1$ contains at least $c_0L/\log B$ elements of $S$.
- **Step 2: a positive proportion of differences.** For $1\le t\le L/2$ let $\mathcal X_t=\{x\in S\cap[1,L/2]:x+t\in S\}$ and $r(t)=|\mathcal X_t|$.
  - $\sum_tr(t)=\sum_{x\in S\cap[1,L/2]}|S\cap(x,x+L/2]|\ge c_0^2L^2/\log^2B$.
  - For $x\in\mathcal X_t$, $x$ avoids the classes $c_p$ and $c_p-t$ for all $p\le B$; these are one class if $p\mid t$ and two otherwise. By (U), $r(t)\le C_1h(t)L/\log^2B$ with $h(t)=\prod_{p\mid t,\,p\ge3}\frac{p-1}{p-2}$.
  - $\sum_{t\le T}h(t)^2\le C_2T$, because $h^2$ is multiplicative with $h(p)^2=1+O(1/p)$.

  Let $\mathcal T$ be the set of even $t\le L/2$ with $r(t)\ge c_1L/\log^2B$ and $h(t)\le H$, where $c_1=c_0^2/2$ and $H=2C_1C_2/c_0^2$. The $t$ with $r(t)<c_1L/\log^2B$ contribute at most $c_0^2L^2/(4\log^2B)$ to $\sum_tr(t)$. The $t$ with $h(t)>H$ contribute at most $C_1\frac{L}{\log^2B}\cdot\frac{C_2L}{2H}=c_0^2L^2/(4\log^2B)$. So $\sum_{t\in\mathcal T}r(t)\ge c_0^2L^2/(2\log^2B)$. As $r(t)\le C_1HL/\log^2B$ on $\mathcal T$,
  $$|\mathcal T|\ \ge\ \frac{c_0^2}{2C_1H}L=\frac{c_0^4}{4C_1^2C_2}\,L=:cL .$$
- **Step 3: the average cost is small.** Fix $t\in\mathcal T$. For $x\in\mathcal X_t$ define $Q(x)$, the exposed points and $\mathrm{cost}(x)$ as in the proof of Theorem D; all primes of $Q(x)$ exceed $B$. Let $N_q=\#\{x\in\mathcal X_t:q\in Q(x)\}$. Here $x\equiv c_q$ or $c_q-t\pmod q$. Write $x=a+qn$, where $n$ runs over an interval of length $L/(2q)\ge M$, and apply (U) to $n$ with $z=\min(B,M)$. Since $\log z\ge\frac14\log B$,
  $$N_q\le C_3H\frac{L}{q\log^2B}\qquad(B<q\le p_j).$$
  Hence
  $$\sum_{x\in\mathcal X_t}\mathrm{cost}(x)=\sum_{B<q\le p_j}\Bigl(\frac tq+1\Bigr)N_q\le\frac{C_3HL}{\log^2B}\Bigl[\frac{2t}{B\log B}+2\log\log p_k\Bigr].$$
  Dividing by $|\mathcal X_t|\ge c_1L/\log^2B$, the average cost is at most $C_4[t/(B\log B)+\log\log p_k]$ with $C_4=2C_3H/c_1$. Now $t/(B\log B)\le L/(2B)=\eta p_k/(2K\log p_k)\le F/K$. With $K=4C_4$ the first term is at most $F/4$, and the second is at most $F/4$ for large $k$. So some $x\in\mathcal X_t$ has at most $F/2$ exposed points.
- **Steps 4 and 5** are those of Theorem D. They only need $t<p_j^2$, which holds because $t\le p_k^{2-\varepsilon}$. ∎

**Corollaries.**
- **Unconditional.** For fixed $\varepsilon,\eta$ and large $k$, the number of even gaps is at least $J(\lceil(1-\eta)k\rceil)^{1-\varepsilon}$. This follows from Theorem E with $\varepsilon/2$ and $J(j)\ll p_j^2$.
- **Second question, conditionally.** If $J(k)\le C\,J(\lceil(1-\eta)k\rceil)$ and $J(k)\le p_k^{2-\varepsilon}$, then the number of even gaps is at least $(c/C)J(k)$.
- **Unconditional, at most scales.** Let $\rho=1/(1-\eta)$ and $k_i=\lceil\rho^i\rceil$. For large $n$, at least half of the $i\le n$ satisfy $J(k_{i+1})\le\rho^5J(k_i)$, because $J$ is non-decreasing and $J(k_n)\le\rho^{(2+o(1))n}$. For those $i$ and $k=k_{i+1}$, the number of even gaps is at least $c\rho^{-5}\min\bigl(J(k),p_k^{2-\varepsilon}\bigr)$.

So the second question can fail at $k$ only if $J$ jumps by a large factor on $[(1-\eta)k,k]$, or $J(k)>p_k^{2-\varepsilon}$.

**Remarks.**
- The exponent $2-\varepsilon$ comes from two requirements: the repair budget needs $B\gtrsim L/p_k$, and (L) needs $L\ge B^{2+\theta}$. Iwaniec's bound $J(k)\ll p_k^2$ rests on the same sifting limit.
- The argument of Step 3 also applies to Theorem D and removes the third term in its Step 3. The only remaining constraint is the lower-bound sieve of dimension 2, so Theorem D holds for every $\delta_0<1/(\beta_2-1)$, where $\beta_2$ is the sifting limit of that sieve. (Sketch only. For the Diamond–Halberstam–Richert sieve $\beta_2=4.266\ldots$ [DH; see Table 1 of Franze], which gives $\delta_0<0.306$.)
- There is no numerical run for Theorem E: it improves on Theorem D only when $J\ge p_k^{1+\delta_0}$, which does not occur for computable $k$.

### 6.3 Theorem F: short lag and almost all $k$

In the proofs of Theorems D and E the sieve level $B$ was taken as small as possible, which forces $\asymp\eta k$ free primes. Taking $B$ as large as the lower-bound sieve allows lowers the average repair cost to a power of $L$ below $p_k$, so far fewer free primes are needed.

**Theorem F.**
- **(a)** There are absolute constants $\delta_0,\kappa_0>0$ such that for fixed $\varepsilon\in(0,\frac12)$ and all large $k$, with $j=k-\lceil k^{1-\kappa_0}\rceil$ and $L=\min\bigl(J(j)-1,p_k^{1+\delta_0}\bigr)$, every even $t\le(1-\varepsilon)L$ is in $G_k$.
- **(b)** For fixed $\varepsilon\in(0,1)$ there is $c(\varepsilon)>0$ such that for all large $k$, with $j=k-\lceil k^{1-\varepsilon/4}\rceil$ and $L=\min\bigl(J(j)-1,p_k^{2-\varepsilon}\bigr)$, at least $cL$ even $t\le L/2$ are in $G_k$.

*Proof.* Follow the proofs of Theorems D and E with $F=k-j$, $X=L-t$ and $M=\varepsilon L/(2p_k)$; by Theorem B and $J(j)\ge s(j)-2$, $M\ge(\log p_k)^{1/2}$ for large $k$. There are two changes.
- **Largest sieve level.** In (a) take $B=X^{1/s_0}$, so that (S1) applies. In (b) take $B=(L/4)^{1/(2+\theta)}$ with $\theta=\varepsilon/4$, so that (L) applies on every sub-interval of length at least $L/2-1$; Steps 1 and 2 of Theorem E are unchanged.
- **Upper-bound sieve for every $q\in(B,p_j]$.** For $x\equiv a\pmod q$ write $x=a+qn$; then $n$ runs over an interval of length at least $M$, and sifting $n$ by the primes $p\le z:=\min(B,M)$ with at most two classes each, (U) gives $N_q\le C\frac Xq V(\log B/\log z)^2$ in (a) and $N_q\le CH\frac L{q\log^2z}$ in (b). In both cases the average cost is at most
  $$C'\Bigl(\frac{\log B}{\log z}\Bigr)^2\Bigl[\frac t{B\log B}+\log\log p_k\Bigr]\le C''\log^2p_k\cdot\frac LB .$$
- **Exponents.** In (a), $L/B\ll_\varepsilon L^{1-1/s_0}\le p_k^{(1+\delta_0)(1-1/s_0)}\le p_k^{1-1/(2s_0)}$ with $\delta_0=1/(2s_0)$; take $\kappa_0=1/(4s_0)$. In (b), $L/B\ll L^{(1+\theta)/(2+\theta)}\le p_k^{(2-\varepsilon)(4+\varepsilon)/(8+\varepsilon)}\le p_k^{1-\varepsilon/3}$. In both cases the average cost is at most $F/2$ for large $k$.
- Steps 4 and 5 are unchanged; they use only that there are at most $F/2$ exposed points and that $t<p_j^2$. ∎

**Lemma (jumps are sparse).** Let $C>1$, $F(k)=\lceil k^{1-\kappa}\rceil$ and $\mathfrak B_C=\{k: J(k)>C\,J(k-F(k))\}$. For large $K$,
$$\#(\mathfrak B_C\cap[K,2K])\le\Bigl(1+\frac{3\log K}{\log C}\Bigr)\bigl(F(2K)+1\bigr).$$

*Proof.* Let $k_1$ be the largest element of $\mathfrak B_C\cap[K,2K]$, and $k_{i+1}$ the largest element of $\mathfrak B_C\cap[K,k_i-F(k_i))$, for $i<m$. Every element of $\mathfrak B_C\cap[K,2K]$ lies in some $[k_i-F(k_i),k_i]$. Since $J$ is non-decreasing, $J(k_i)>C\,J(k_i-F(k_i))\ge C\,J(k_{i+1})$, so $J(2K)>C^{m-1}J(K)$. Iwaniec's bound gives $J(2K)\le K^3$ for large $K$, so $m\le1+3\log K/\log C$. ∎

**Corollaries.** Fix $\varepsilon$ and put $\kappa=\min(\kappa_0,\varepsilon/8)$. Outside a set $\mathcal E$ with $\#(\mathcal E\cap[1,K])\ll_\varepsilon K^{1-\kappa}\log K$:
- $s(k)\ge(1-\varepsilon)\min\bigl(J(k),p_k^{1+\delta_0}\bigr)$ (Theorem F(a) and the lemma with $C=1+\varepsilon/2$). Letting $\varepsilon\to0$ slowly gives a set $\mathcal E'$ of density zero such that $s(k)=(1+o(1))J(k)$ as $k\to\infty$ through the $k\notin\mathcal E'$ with $J(k)\le p_k^{1+\delta_0}$. The density is relative to all integers: we do not know how many $k$ satisfy $J(k)\le p_k^{1+\delta_0}$.
- The number of even gaps is at least $\frac c2\min\bigl(J(k),p_k^{2-\varepsilon}\bigr)$ (Theorem F(b) and $C=2$), and at least $J(k)^{1-\varepsilon}$.

**Remarks.**
- Theorems D and E are special cases of Theorem F.
- The number of free primes needed is about $\log^2p_k\cdot L/B$. If $J(k)=p_k^{1+o(1)}$, as conjectured, a lag of $k^{1/2+o(1)}$ suffices in (b). The method cannot reach a lag $O(1)$, since $L/B\ge L^{1/2}$; numerically $s(k)>J(k-1)$ for $6\le k\le26$.
- At an exceptional $k$, $J$ must grow by a constant factor within $k^{1-\kappa}$ steps. Whether this ever happens is the remaining question for the second part.
- (R1) reduces to a single-step condition. Put $\ell(k)=k\log\bigl(J(k)/J(k-1)\bigr)$. Since $\log\frac{J(k)}{J(k-F)}=\sum_{k-F<i\le k}\ell(i)/i$, the bound $\ell(k)\le k^{\kappa/2}$ for all large $k$ gives $J(k)/J(k-\lceil k^{1-\kappa}\rceil)\le\exp(2k^{-\kappa/2})\to1$, so (R1) holds with every $C>1$. Unconditionally, the mean of $\ell$ over $(K,2K]$ is at most $2\log(J(2K)/J(K))\le(2+o(1))\log K$; the lemma above is the same fact. What is missing is a bound for the maximum of $\ell$.
- Numerically there is no sign of jumps. For all known values ($k\le71$, OEIS A048670) and $30\le k\le71$: $0.95\le J(k)/(k\log^2k)\le1.02$, $J(k)/J(k-1)\le1.073$, $J(k)/J(k-\lceil\sqrt k\,\rceil)\le1.44$, and $0.70\le\ell(k)\le2.35$ (script `stage11_jumps.py`). This range is far too small to test the asymptotic question.
- For the second question the single-step condition is not needed. Suppose $J(2k)\le D\,J(k)$ for all large $k$ with a constant $D<4$. Then (R1) holds for every large $k$ with $C=D$, because $k-\lceil k^{1-\kappa}\rceil\ge k/2$. Iterating also gives $J(k)\ll k^{\log_2D}$ with $\log_2D<2$, so $J(k)\le p_k^{2-\varepsilon}$ for a suitable $\varepsilon>0$. Hence $|G_k|\gg J(k)$ for all large $k$. The hypothesis is at least as strong as improving the exponent in Iwaniec's bound $J(k)\ll p_k^2$, so this reduction does not avoid the main difficulty; it only concentrates it in one statement. For $40\le k\le71$ the known values give $J(k)/J(\lceil k/2\rceil)\le3.09$. (Stage 13, `STAGE13_ONESTEP.md`.)

### 6.4 Producing gaps from a single cover

The rest of this section records an approach that stays at one level: produce many shorter gaps directly from one cover of a long gap. It does **not** settle the second question either, and Theorems D–F make it unnecessary for the reduction above; we keep it for the lemmas and the numerical observations.

Use the halved model of §1: a gap $t=2m$ is a choice of classes $c_p$ for the odd primes $p\le p_k$ such that every point of $1,\dots,m-1$ lies in some class, and $0$ and $m$ lie in none. Write $C(i)$ for the set of primes whose class contains $i$, so $C(0)=C(m)=\varnothing$. Let $G_k$ be the set of gaps.

**Lemma 6.1 (monotonicity).** $G_{k-1}\subseteq G_k$ for $k\ge3$.

*Proof.* Keep a cover from level $k-1$ and give $p_k$ a class that avoids both endpoints. ∎

**Lemma 6.2 (deletion).** Let $0\le x<y\le m$. If no $z$ with $x<z<y$ has $C(z)\subseteq C(x)\cup C(y)$, then $2(y-x)\in G_k$.

*Proof.* Give every prime of $Q=C(x)\cup C(y)$ a new class that avoids $x$ and $y$; an odd prime has at least three classes. Then $x$ and $y$ are uncovered. Every $z$ strictly between them has a covering prime outside $Q$, whose class is unchanged. ∎

**Lemma 6.3 (essential points).** In a cover of the maximal gap, $m=J(k)/2$, every odd prime $q\le p_k$ with $q\nmid m$ has a point $z$ with $C(z)=\{q\}$.

*Proof.* Otherwise move $q$ to the class of $m$. Every point of $1,\dots,m-1$ is still covered, $m$ is now covered, and $0$ is still uncovered because $q\nmid m$. The gap would be longer than $J(k)$. ∎

**Self-repair.** Lemma 6.2 has an obvious extension: $2(y-x)\in G_k$ as soon as the primes of $Q$ can be given new classes that avoid $x$ and $y$ and together cover the points $z\in(x,y)$ with $C(z)\subseteq Q$.

**Numerical observations.** Scripts `stage6_deletion.py`, `stage6_repair.py`, `stage6_scale.py`.
- For $13\le k\le26$, starting from a single cover of the maximal gap $J(k)$:
  - Lemma 6.2 alone produces between 59% and 68% of the even numbers up to $J(k)$ as gaps;
  - with self-repair, between 81% and 87% of all gaps are produced.
- For $k$ up to $300$ we used one long greedy cover per $k$ (not maximal; its length is between $1.7\,p_k$ and $4\,p_k$). With self-repair, between 78% and 89% of the even numbers below the length of the cover are produced as gaps. These are lower bounds, because only 400 positions $x$ were tried for each difference.
- For $6\le k\le26$, $s(k)>J(k-1)$.

**What is missing.** Let $S$ be the set of points of a maximal cover that lie in no class of a prime $p\le p_k/2$. By Lemma 6.3, $|S|\ge\pi(p_k)-\pi(p_k/2)-\omega(m)$. A positive answer to the second question would follow from two statements that we cannot prove:
1. the difference set of $S$ has $\gg J(k)$ elements;
2. for a positive proportion of those differences, self-repair succeeds.

For $15\le k\le26$ the difference set of $S$ contains between 63% and 79% of the integers up to $J(k)/2$. Sieve methods give no lower bound here, because the sifting level $p_k/2$ is close to the length of the interval.

A second, independent reduction: if $s(k)>J(k-1)$ for all large $k$ and $J(k)\ll J(k-1)$, then the number of gaps is $\gg J(k)$.

## 7. AI assistance

This work was produced with substantial assistance from an AI system (Claude, Anthropic), working under the direction of the author. The AI system drafted the proofs, wrote and ran the computations, and searched the literature. The author chose the problem and the direction, and is responsible for the content.

The proofs have not yet been refereed. Independent checking, especially of §4 and §6.1–6.3, is welcome. A line-by-line recheck of §6.1–6.3 by the same AI system (`STAGE10_CHECK.md`) found no mathematical error; it is not a substitute for an independent referee.

## 8. References and files

- [FGKMT] K. Ford, B. Green, S. Konyagin, J. Maynard, T. Tao, *Long gaps between primes*, J. Amer. Math. Soc. 31 (2018), 65–105. arXiv:1412.5029.
- E. R. Canfield, P. Erdős, C. Pomerance, *On a problem of Oppenheim concerning "factorisatio numerorum"*, J. Number Theory 17 (1983).
- H. L. Montgomery, R. C. Vaughan, *The large sieve*, Mathematika 20 (1973) (Brun–Titchmarsh).
- J. Friedlander, H. Iwaniec, *Opera de Cribro*, AMS 2010, Ch. 6 (fundamental lemma).
- [HR] H. Halberstam, H.-E. Richert, *Sieve Methods*, Academic Press 1974 (Theorems 2.2 and 8.4).
- [DH] H. G. Diamond, H. Halberstam, *A Higher-Dimensional Sieve Method*, Cambridge Univ. Press 2008.
- C. S. Franze, *Sifting limits for the $\Lambda^2\Lambda^-$ sieve*, arXiv:1012.3809 (Table 1).
- H. Iwaniec, *On the problem of Jacobsthal*, Demonstratio Math. 11 (1978).
- R. A. Rankin, *The difference between consecutive prime numbers*, J. London Math. Soc. 13 (1938).
- Repository: https://github.com/maris205/twin_primes/tree/main/research/prize-problems
  - Chinese stage reports: `STAGE1_GAPS.md`, `STAGE3_LOGLOSS.md`, `STAGE4_FGKMT.md`, `STAGE6_MAP.md`, `STAGE7_TRANSFER.md`, `STAGE8_COUNT.md`, `STAGE9_JUMP.md`, `STAGE10_CHECK.md`.
  - Witnesses: `a389839_witnesses.json`.
  - Checker: `verify_a389839.py`.
