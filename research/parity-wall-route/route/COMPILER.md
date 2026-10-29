# 通路编译器：GEH ⟹ $\sum W\sim8\Pi_2x\log^2x$，以及 GEH + LRC ⟹ 对数平均 HL（草稿 v0.1，2026-10-26）

对应 [ROUTE.md](ROUTE.md) §6 的两个“待写全”。数学正文用英文，说明用中文。数值核对见 [check_compiler.py](check_compiler.py) / [check_compiler.json](check_compiler.json)。

## 0. 结论与更正

| 结果 | 状态 |
|---|---|
| **C1**：EH + GEH ⟹ $M(x)=\sum_{n\le x}\Lambda_2(n)\Lambda_2(n+2)=(8\Pi_2+o(1))x\log^2x$ | 证明完成（§6），条件是 Bombieri–Tao 定理（黑盒，§1）与一个标准上界筛（引理 2） |
| **C2**：同一假设下，单点奇偶项 $D_1,D_2=o(x\log^2x)$ | 证明完成（§7） |
| **C3**：同一假设下，$4T=8\Pi_2x\log^2x+D_3^\flat(x)+o(x\log^2x)$；于是 HL ⟺ $D_3^\flat=o(x\log^2x)$ | 由 C1、C2 与**精确**奇偶恒等式（引理 1）得到 |
| **C4**：同一假设下，$\sum_{n\le X}\frac{\Lambda(n)\Lambda(n+2)}n=2\Pi_2\log X\,(1+\rho(X))+o(\log X)$ | 证明完成（§9） |
| 推论 | **LRC₂**（$\rho\to0$）⟹ 对数平均 HL ⟹ TPC；更弱的 **PND$_{\log}$**（$\limsup\rho>-1$）就已经 ⟹ TPC |

**两处更正（ROUTE.md 已同步修改）：**

1. **ROUTE.md 原 LRC 的归一化是退化的。** 在相对粗糙的定义下，$\sum_n\mathbf 1_R(n)\mathbf 1_R(n+2)/n$ **收敛**，因为其通项约为 $1/(n\log^2n)$。所以原陈述只是关于一个有界量的命题，这也是数值卡在 −0.05 的原因。正确的权重要多乘 $\log^2n$。本文改用等价但更干净的形式 LRC₂（§9），它直接以 $\Lambda_2^\flat\otimes\Lambda_2^\flat$ 加权。
2. **Tao 笔记中 “$\sum\mu\mathbf 1_R(n)\Lambda(n+2)=o(x/\log x)$” 这一形式需要谨慎使用。** 对固定的 $\alpha$，$\sum_{n\le x}\mu(n)\mathbf 1[P^-(n)>x^\alpha]$ 本身就不是 $o(x/\log x)$：当 $\frac13<\alpha<\frac12$ 时，主项为 $(-1+\log\frac{1-\alpha}\alpha)\frac x{\log x}$，数值上见 §11。因此本文不用 $\mu\mathbf 1_R$，而用不含歧义的 $\Lambda_2^\flat$ 精确恒等式。Tao 的原意大概是“与无偏模型比较”或改用另一种筛权，这里不依赖它。

**未完成：**

- Bombieri 原文（Mem. Accad. XL 1976）和 Friedlander–Iwaniec（Ann. SNS Pisa 1978）的扫描件文字层是乱码，未能逐条核对。本文以 Tao 笔记中的 Theorem 1（四条公理全文可读）作为黑盒。
- 引理 2 依赖标准的两线性形式上界筛，定理编号待补。

---

## 1. 黑盒：Bombieri 渐近筛（Tao 2016 笔记 Theorem 1）

**Theorem B.** Let $a_n=a_n(x)$ satisfy:

- (i) $a_n\ge0$;
- (ii) $a_n\ll\tau(n)^{O(1)}\log^{O(1)}n$;
- (iii) $\sum_{n\le x}a_n=(C+o(1))x$ for a constant $C>0$;
- (iv) for every $\varepsilon,A>0$,
$$\sum_{d\le x^{1-\varepsilon}}\Bigl|\sum_{n\le x,\,d\mid n}a_n-Cx\frac{g(d)}d\Bigr|\ll_{\varepsilon,A}\frac x{\log^Ax},$$
with $g$ multiplicative and $g(p^j)=1+O(1/p)$.

Put $G(1)=\prod_p\frac{1-g(p)/p}{1-1/p}$. Then for every fixed tuple $\vec k\ne(1,\dots,1)$,

$$\sum_{n\le x}\Lambda_{\vec k}(n)a_n=(G(1)+o(1))\frac{\prod k_i!}{(|\vec k|-1)!}\,Cx\log^{|\vec k|-1}x .$$

We only use $\vec k=(2)$, for which the constant is $2\,G(1)\,C\,x\log x$.

> **核对说明：**
> - Tao 笔记对 $a_n=\Lambda(n+2)$ 写的是 “$C=2\Pi_2$”。按 (iii) 应有 $C=1$，此时 $g(p)=\frac p{p-1}$（$p$ 奇）、$g(2^j)=0$，$G(1)=2\Pi_2$。两种写法的乘积 $G(1)C$ 相同，结论不受影响。本文统一采用“$C$ 由 (iii) 决定”的写法。
> - 由 (iv) 中的 “$Cx$” 可知，(iii) 实际上需要误差为 $O(x\log^{-A}x)$。本文所用序列都满足这一点（§5）。

**Hypotheses used.**

- **EH**：对每个 $\varepsilon>0$，$\sum_{q\le x^{1-\varepsilon}}\max_{(a,q)=1}\max_{y\le x}|\psi(y;q,a)-\frac y{\varphi(q)}|\ll x\log^{-A}x$。
- **GEH**（Polymath8b, Claim 2.6 的形式，对每个 $\theta<1$）：设 $\alpha,\beta$ 分别是尺度 $N,M$ 上的系数序列（除数型有界，$\beta$ 满足 Siegel–Walfisz），$N,M\ge x^{\varepsilon}$，$NM\asymp x$。则 $\sum_{q\le x^\theta}\sup_{(a,q)=1}|\Delta(\alpha*\beta;a\bmod q)|\ll x\log^{-A}x$。

---

## 2. Notation

- $L^\flat(m)=\log^2 m\cdot\mathbf 1_{\mathbb P}(m)$；$\Lambda_2^\flat=\mu^2\Lambda_2$，支撑在素数与积 $pq$（$p\ne q$）上，并且 $\Lambda_2^\flat(pq)=2\log p\log q$。
- Fix $0<\eta<\frac1{10}$. 记 $B_\eta(m)=\sum_{pq=m,\ p\ne q,\ p,q\ge m^\eta}\log p\log q$（有序对），$U_\eta^\flat=\Lambda_2^\flat-L^\flat-B_\eta\ge0$（至少一个素因子 $<m^\eta$ 的积 $pq$）。
- $\lambda(m)=(-1)^{\Omega(m)}$。
- 以下各量都对 $n\le x$ 求和：
$$M^\flat=\sum\Lambda_2^\flat(n)\Lambda_2^\flat(n+2),\qquad D_1^\flat=\sum\Lambda_2^\flat(n)\lambda(n)\Lambda_2^\flat(n+2),$$
$$D_2^\flat=\sum\Lambda_2^\flat(n)\Lambda_2^\flat(n+2)\lambda(n+2),\qquad D_3^\flat=\sum\Lambda_2^\flat(n)\lambda(n)\Lambda_2^\flat(n+2)\lambda(n+2),$$
$$T=\sum_{n\le x}\log n\,\mathbf 1_{\mathbb P}(n)\log(n+2)\,\mathbf 1_{\mathbb P}(n+2)\,\log n\log(n+2)$$
（即 $\sum L^\flat(n)L^\flat(n+2)$）。

---

## 3. Lemma 1 (exact parity identity)

For every $m$, $L^\flat(m)=\Lambda_2^\flat(m)\,\dfrac{1-\lambda(m)}2$. Consequently, for every $x$,

$$\boxed{\,4\sum_{n\le x}L^\flat(n)L^\flat(n+2)=M^\flat-D_1^\flat-D_2^\flat+D_3^\flat\,}$$

*Proof.* On primes, $\Lambda_2^\flat=\log^2p$ and $\frac{1-\lambda}2=1$. On $pq$, $\frac{1-\lambda}2=0$. Elsewhere both sides vanish. Expand $(1-\lambda(n))(1-\lambda(n+2))$. $\square$

注意：若用 $\Lambda_2$ 而不是 $\Lambda_2^\flat$，恒等式在 $p^aq^b$（如 $12=2^2\cdot3$）上不成立，那里 $\lambda=-1$ 而 $\Lambda=0$。数值上，用 $\Lambda_2$ 时残差为 −14%，用 $\Lambda_2^\flat$ 时残差恰为 0（§11）。

---

## 4. Lemma 2 (unconditional upper bound) and its corollaries

**Lemma 2.** Uniformly for integers $1\le k\le y^{1/5}$,

$$\sum_{b\le y}\Lambda(b)\,\Lambda_2(kb-2)\ll\frac k{\varphi(k)}\,y\log y .$$

*Proof.* Write $\Lambda_2=\Lambda\cdot\log+\Lambda*\Lambda$. Prime powers $b$ contribute $O(y^{1/2+o(1)})$.

- *(a) The $\Lambda\cdot\log$ part.* The two linear forms $b$ and $kb-2$ have discriminant 2. The Selberg upper-bound sieve for two linear forms gives
$$\#\{b\le y:\ b,\ kb-2\ \text{prime}\}\ll\frac k{\varphi(k)}\frac y{\log^2y}.$$
Multiplying by the weights $\le\log^3(ky)$ gives $\ll\frac k{\varphi(k)}y\log y$.
- *(b) The $\Lambda*\Lambda$ part.* Write $kb-2=rs$ with $r\le s$, so $r\le\sqrt{ky}\le y^{3/5}$. Prime powers $r$ or $s$ contribute $O(y^{1-c})$.
  - For a fixed prime $r$: if $r\mid k$ then $r\mid2$. Otherwise $b\equiv2\bar k\pmod r$, so $b=rt+c$ with $t\le y/r$, and then $s=kt+c'$ with $c'=(kc-2)/r$.
  - The two forms $rt+c$ and $kt+c'$ have discriminant $r c'-kc=-2$. The upper-bound sieve gives
  $$\#\{t\le y/r:\ \text{both prime}\}\ll\frac{rk}{\varphi(rk)}\frac{y/r}{\log^2(y/r)}\ll\frac{rk}{\varphi(rk)}\frac y{r\log^2y},$$
  using $\log(y/r)\ge\frac25\log y$.
  - With the weights $\Lambda(b)\Lambda(r)\Lambda(s)\le\log^3(ky)$ and summing over $r\le y^{3/5}$, using $\sum_{r\le Y}\frac{\log r}r\frac r{\varphi(r)}\ll\log Y$, we get $\ll\frac k{\varphi(k)}y\log y$. $\square$

> 待补：两线性形式上界筛对系数一致性的准确出处（Halberstam–Richert, *Sieve Methods* 第 2、5 章中的相应定理）。

**Lemma 3 (what the sieve leaves for free).** Unconditionally, as $x\to\infty$, with an absolute constant $C_0$:

- (a) $\displaystyle\sum_{n\le x}\Lambda_2(n)\,U_\eta^\flat(n+2)\le C_0\,\eta\,x\log^2x+O(x\log x)$;
- (b) $\displaystyle\sum_{n\le x}\Lambda_2(n)\,(\Lambda_2-\Lambda_2^\flat)(n+2)\ll x\log x$;
- (c) the same two bounds with the roles of $n$ and $n+2$ exchanged.

*Proof.*

- (a) $U^\flat_\eta(n+2)\ne0$ forces $n+2=pb$ with $p<(n+2)^\eta\le x^\eta$. So the sum is at most
$$2\sum_{p\le x^\eta}\log p\sum_{b\le(x+2)/p}\log b\cdot\Lambda_2(pb-2).$$
Lemma 2 with $k=p$ and $y=x/p\ge x^{1-\eta}$ bounds this by $\ll\sum_{p\le x^\eta}\frac{\log p}p\,x\log x\le C_0\eta x\log^2x$.
- (b) $\Lambda_2-\Lambda_2^\flat$ is supported on $m=p^jr^i$ with $j\ge2$ (or on prime powers). For $p^j\le x^{1/5}$, Lemma 2 with $k=p^j$ gives $\ll x\log x\sum_{p,j\ge2}\frac{\log p}{p^j}\ll x\log x$. For $p^j>x^{1/5}$, the cofactor is $<x^{4/5}$; exchanging the roles of the two factors and counting the prime powers $p^j$ trivially gives a smaller contribution.
- (c) Write $m=n+2$ and use $b$ for the other factor; the argument is the same. $\square$

---

## 5. Lemma 4 (axioms of Theorem B for the sequences we feed in)

Assume EH and GEH. Each of the following sequences satisfies (i)–(iv) of Theorem B, with $g(p^j)=\frac p{p-1}$ for odd $p$, $g(2^j)=0$, and hence $G(1)=2\Pi_2$:

| 序列 $a_n$ | $C$ | 所需假设 |
|---|---|---|
| $\alpha_n=\mathbf 1_{\mathbb P}(n+2)\log(n+2)$ | $1$ | EH |
| $\beta_n=B_\eta(n+2)/\log(n+2)$ | $1-2\eta$ | GEH |

The same holds for the reflected sequences $\mathbf 1_{\mathbb P}(m-2)\log(m-2)$ and $B_\eta(m-2)/\log(m-2)$ in the variable $m$.

*Proof.*

- **(i), (ii)** are clear.
- **(iii) with error $O(x\log^{-A}x)$.**
  - For $\alpha$ this is the PNT with de la Vallée Poussin error.
  - For $\beta$, apply the PNT to both prime variables. The main term is
  $$\iint_{uv\le x,\ u,v\ge(uv)^\eta}\frac{du\,dv}{\log(uv)}=\int_2^x\frac{(1-2\eta)\log w}{\log w}\,dw=(1-2\eta)x+O(1),$$
  obtained by the substitution $w=uv$ (for fixed $w$, $\int du/u$ over $[w^\eta,w^{1-\eta}]$ equals $(1-2\eta)\log w$). The error is $O(x\log^{-A}x)$.
- **(iv), even $d$.** $d\mid n$ forces $m=n+2$ to be even. Then $\alpha$ only sees $m=2$, and $\beta$ vanishes once $m^\eta>2$. Hence $\sum_{d}|\cdot|\ll x^{o(1)}$, consistent with $g(2^j)=0$.
- **(iv), odd $d$.** $d\mid n$ means $m\equiv2\pmod d$, and then automatically $(m,d)=1$. Write
$$\sum_{m\equiv2\,(d)}a'_m=\frac1{\varphi(d)}\sum_{(m,d)=1}a'_m+\Delta_d .$$
  - *Difference between the coprime total and the full total.* For $\alpha$, $m$ prime and $(m,d)>1$ force $m\mid d$, giving $\le\omega(d)\log x$. For $\beta$, $m=pq$ with $p\mid d$ and $p\ge m^\eta$: terms with $m\le x^{1/2}$ contribute $\le x^{1/2+o(1)}$ in total; terms with $m>x^{1/2}$ have $p\ge x^{\eta/2}$ and contribute $\le\frac x p\log x\le x^{1-\eta/2}\log x$ per $p$. After weighting by $1/\varphi(d)$ and summing over $d$, the total is $\ll x^{1-\eta/2+o(1)}$.
  - *$\sum_{d\le x^{1-\varepsilon}}|\Delta_d|$.*
    - For $\alpha$, this is exactly EH.
    - For $\beta$, split $m\le x$ into $m\le x^{1-\varepsilon/2}$ and $m>x^{1-\varepsilon/2}$.
      - The first part is bounded trivially by $\sum_d(y/d+1)\log^2x\ll x^{1-\varepsilon/2}\log^3x$.
      - In the second part, $d\le x^{1-\varepsilon}\le m^{1-\varepsilon/2}$, so the level is below 1. Decompose $(p,q)$ into $(1+\log^{-B}x)$-adic boxes. Boxes that cross the boundaries $pq\le x$ or $p,q\ge(pq)^\eta$ are bounded trivially by $O(x\log^{-B+O(1)}x)$. Every remaining box is a convolution of two prime-supported sequences with Siegel–Walfisz (each factor $\ge x^{\eta/2}$), to which GEH applies directly.
      - The weight $1/\log m$ is removed by partial summation. The result is $\ll x\log^{-A}x$. $\square$

> 这里用相对截断 $p,q\ge m^\eta$（而不是 $x^\eta$），使序列不依赖 $x$。Theorem B 在每个尺度上都能使用，从而支撑后面的分部求和。

---

## 6. Theorem C1

**Theorem C1.** Assume EH and GEH. Then

$$M(x)=\sum_{n\le x}\Lambda_2(n)\Lambda_2(n+2)=(8\Pi_2+o(1))\,x\log^2x,$$

and the same holds for $M^\flat$.

*Proof.* Fix $\eta$. Since $\Lambda_2^\flat=L^\flat+B_\eta+U^\flat_\eta$,

$$\sum_{n\le x}\Lambda_2(n)\Lambda_2^\flat(n+2)=\underbrace{\sum\Lambda_2(n)\,(\alpha_n+\beta_n)\log(n+2)}_{(\star)}+\underbrace{\sum\Lambda_2(n)\,U^\flat_\eta(n+2)}_{\le C_0\eta x\log^2x+O(x\log x)}.$$

Apply Theorem B with $\vec k=(2)$ to $\alpha+\beta$, for which $C=2-2\eta$ and $G(1)=2\Pi_2$:

$$\sum_{n\le t}\Lambda_2(n)(\alpha_n+\beta_n)=(2\cdot2\Pi_2\cdot(2-2\eta)+o(1))\,t\log t ,$$

valid for every $t\to\infty$. Partial summation against $\log(n+2)$ gives

$$(\star)=(8\Pi_2(1-\eta)+o(1))\,x\log^2x .$$

Hence

$$8\Pi_2(1-\eta)\le\liminf\frac{\sum\Lambda_2(n)\Lambda_2^\flat(n+2)}{x\log^2x}\le\limsup\le8\Pi_2(1-\eta)+C_0\eta .$$

Let $\eta\to0$. Lemma 3(b) and (c) replace $\Lambda_2^\flat$ by $\Lambda_2$ on either side at cost $O(x\log x)$, which gives both $M$ and $M^\flat$. $\square$

---

## 7. Theorem C2

**Theorem C2.** Assume EH and GEH. Then $D_1^\flat(x),\ D_2^\flat(x)=o(x\log^2x)$.

*Proof.* We have $\Lambda_2^\flat(m)\lambda(m)=-L^\flat(m)+B_\eta(m)+U^\flat_\eta(m)$, because $\lambda=+1$ on $pq$. So

$$D_2^\flat=-\sum\Lambda_2(n)\alpha_n\log(n+2)+\sum\Lambda_2(n)\beta_n\log(n+2)+O\bigl(C_0\eta x\log^2x+x\log x\bigr).$$

The last term uses Lemma 3, together with replacing $\Lambda_2^\flat(n)$ by $\Lambda_2(n)$.

- Theorem B with $C=1$ gives the first sum $=(4\Pi_2+o(1))x\log^2x$.
- Theorem B with $C=1-2\eta$ gives the second sum $=(4\Pi_2(1-2\eta)+o(1))x\log^2x$.

Therefore $|D_2^\flat|\le(8\Pi_2+C_0)\eta\,x\log^2x+o(x\log^2x)$. Let $\eta\to0$.

$D_1^\flat$ is the same computation in the variable $m=n+2$, applying Theorem B to the reflected sequences of Lemma 4 with the weight $\Lambda_2(m)$. $\square$

> 这一步说明：在 GEH 下，**单点**奇偶项不携带任何信息，只有两点项 $D_3$ 携带孪生内容。这与 Bombieri 的“一维奇偶自由度”一致。

---

## 8. Corollary C3 (Cesàro compiler)

Assume EH and GEH. Then

$$4\sum_{n\le x}L^\flat(n)L^\flat(n+2)=8\Pi_2\,x\log^2x+D_3^\flat(x)+o(x\log^2x).$$

Since $\sum_{n\le x}L^\flat(n)L^\flat(n+2)=\sum_{p\le x,\ p+2\ \text{prime}}\log^2p\log^2(p+2)$, it follows that

$$\text{HL}\iff D_3^\flat(x)=o(x\log^2x).$$

The proof is Lemma 1 combined with C1 and C2.

---

## 9. Theorem C4 (log-averaged compiler)

Put $w(n)=\dfrac1{n\log n\log(n+2)}$ and

$$\mathcal L_3(X)=\sum_{n\le X}\Lambda_2^\flat(n)\Lambda_2^\flat(n+2)\lambda(n)\lambda(n+2)\,w(n),\qquad \rho(X)=\frac{\mathcal L_3(X)}{8\Pi_2\log X}\in[-1,1]+o(1).$$

**Theorem C4.** Assume EH and GEH. Then

$$\boxed{\ \sum_{n\le X}\frac{\Lambda(n)\Lambda(n+2)}n=2\Pi_2\log X\,\bigl(1+\rho(X)\bigr)+o(\log X).\ }$$

*Proof.* Let $F(n)=L^\flat(n)L^\flat(n+2)$, so that $\frac{\Lambda(n)\Lambda(n+2)}n=F(n)w(n)$ on twin primes; proper prime powers contribute $O(1)$.

By C3, $A(t)=\sum_{n\le t}F(n)=2\Pi_2t\log^2t+\frac14D_3^\flat(t)+o(t\log^2t)$ for every $t\to\infty$.

Partial summation with $-w'(t)=\frac1{t^2\log^2t}(1+O(\frac1{\log t}))$ gives

$$\sum_{n\le X}F(n)w(n)=A(X)w(X)+\int_2^XA(t)(-w'(t))\,dt .$$

- The boundary term $A(X)w(X)$ is $O(1)$.
- The main part of the integral is $2\Pi_2\log X+O(\log\log X)$.
- The $o(t\log^2t)$ error integrates to $o(\log X)$.
- The $D_3$ part equals $\frac14\int D_3^\flat(t)(-w'(t))\,dt$. By the same partial summation, this is $\frac14\mathcal L_3(X)+O(1)$. Here we used $|D_3^\flat(t)|\le M^\flat(t)\ll t\log^2t$ and the $O(1/\log t)$ difference between $w$ and $1/(t\log^2t)$, which contributes $O(\log\log X)$.

Finally, by C1 and the same partial summation, $\sum_{n\le X}\Lambda_2^\flat(n)\Lambda_2^\flat(n+2)w(n)=(8\Pi_2+o(1))\log X$, so $\rho\in[-1,1]+o(1)$. $\square$

**Corollaries** (all assuming EH and GEH):

- **LRC₂**：若 $\rho(X)\to0$（$\Lambda_2^\flat\otimes\Lambda_2^\flat$ 加权的对数平均两点 Chowla），则 $\sum_{n\le X}\Lambda(n)\Lambda(n+2)/n\sim2\Pi_2\log X$。此时孪生素数无穷多，并满足对数平均意义下的 HL。
- **PND$_{\log}$**：若 $\limsup_{X\to\infty}\rho(X)>-1$，则孪生素数无穷多。理由是：若孪生素数只有有限多个，左边有界，于是 $1+\rho(X)=o(1)$。
- **含义**：只要几乎素数对 $(n,n+2)$ 的奇偶在对数平均下**不是近乎完全反相关**，孪生素数猜想就成立（在 GEH 下）。所谓完全反相关，就是 $\Lambda_2^\flat$ 权重几乎全部落在（素，半素）与（半素，素）这类配对上，也就是 Chen 型的世界。这是奇偶桥最弱的一种写法。

**与 Tao 2016 定理的距离：** Tao 证明了 $\sum_{n\le X}\lambda(n)\lambda(n+2)/n=o(\log X)$。LRC₂ 是同一个量，只是换成了 $\Lambda_2^\flat(n)\Lambda_2^\flat(n+2)/(\log n\log(n+2))$ 的权重，即“几乎素数对”上的版本。困难在于这个权重破坏了小素数处的乘性 $\lambda(pn)=-\lambda(n)$，而 Tao 的熵递减正依赖于它。这正是 ROUTE.md 所说的真正新难点，现在有了精确的陈述。

---

## 10. 量词与参数顺序（与仓库约定的关系）

- 本编译器不使用仓库的 $z=(\log x)^K$ 或 $K=K(B)$。它们属于旧 Bridge A 的 Type II 设定，与这里无关。
- 唯一的辅助参数是 $\eta$，顺序为：先固定 $\eta$，再令 $x\to\infty$，最后令 $\eta\to0$。所有 $o(1)$ 都可以依赖 $\eta$。
- GEH 只用于 $\beta$，即两个都 $\ge x^{\eta/2}$ 的素数变量的卷积，并且只用于水平 $<1$ 的情形。EH 用于素数序列 $\alpha$。
- 引理 2、3 是无条件的。

---

## 11. 数值核对（$x\le10^7$，[check_compiler.json](check_compiler.json)）

| $x$ | $M/(8\Pi_2x\log^2x)$ | $D_1/M$ | $D_2/M$ | $D_3/M$ | 恒等式残差（$\Lambda_2$） | 恒等式残差（$\Lambda_2^\flat$） | $(M-M^\flat)/M$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| $10^4$ | 0.710 | −0.174 | −0.197 | +0.012 | −0.239 | **0** | 0.157 |
| $10^5$ | 0.766 | −0.151 | −0.142 | +0.007 | −0.204 | **0** | 0.121 |
| $10^6$ | 0.803 | −0.119 | −0.121 | +0.005 | −0.172 | **0** | 0.098 |
| $10^7$ | 0.831 | −0.104 | −0.103 | +0.008 | −0.145 | **0** | 0.083 |

| $X$ | $\rho(X)$（LRC₂） | $\sum\Lambda\Lambda/n\,/\,(2\Pi_2\log X)$ |
|---|---:|---:|
| $10^4$ | −0.0199 | 0.936 |
| $10^5$ | −0.0148 | 0.946 |
| $10^6$ | −0.0100 | 0.954 |
| $10^7$ | **−0.0065** | 0.962 |

读法：

- $M$ 缓慢趋向 1（二阶项为 $1/\log x$ 量级）。
- $D_1/M$ 与 $D_2/M$ 约为 $-1.67/\log x\to0$，与 C2 一致。
- $D_3/M$ 已经很小。
- $\rho(X)$ 单调趋向 0，支持 LRC₂。
- 二阶项的理论解释尚未给出。

$\mu$ 在粗糙数上的和（更正 2 的依据）：

| $x$ | $\alpha$ | $\sum\mu\mathbf 1_R/(x/\log x)$ | 预测 $-1+\log\frac{1-\alpha}\alpha$ |
|---|---|---:|---:|
| $10^7$ | 0.36 | −0.593 | −0.425 |
| $10^7$ | 0.40 | −0.770 | −0.595 |
| $10^7$ | 0.45 | −0.964 | −0.799 |

数值正以 $1/\log x$ 的速度向预测值靠拢，明显不趋于 0。

---

## 12. 剩余的诚实缺口

1. Theorem B 引自 Tao 笔记，Bombieri 与 Friedlander–Iwaniec 原文未能核对。
2. 引理 2 所需上界筛的准确出处待补。
3. GEH 的盒分解（§5）按标准方式书写，边界盒用了 $(1+\log^{-B}x)$-adic 细分；投稿前应写成完整引理。
4. C4 中有若干 $O(\log\log X)$ 量级的误差项，需要逐项核实。它们都是 $o(\log X)$，不影响结论。
