# 第四阶段：去掉最后一个 $\log\log$，达到 FGKMT 量级（2026-10-31）

**问题：** 定理 3.1 给出 $s(k)\gg p_k\log p_k\cdot L_3/L_2^2$（Rankin 量级），与 Jacobsthal 函数已知最好的下界只差一个 $L_2=\log\log p_k$。能否去掉它？

**一句话答案：能。** 而且不必重写 Ford–Green–Konyagin–Maynard–Tao（下称 FGKMT）的整套论证：他们的"筛素数"定理可以当作黑箱使用，端点条件只需在外层处理。

- **定理 4.1（无条件）：** 存在绝对常数 $c'>0$，使得对充分大的 $k$，
$$s(k)\ \ge\ c'\,\frac{p_k\log p_k\cdot\log\log\log p_k}{\log\log p_k}.$$
- **与 $J(k)$ 已知最好的下界同阶：** FGKMT（J. Amer. Math. Soc. 31 (2018)）证明的正是 $J(k)\gg p_k\log p_k\cdot\log\log\log p_k/\log\log p_k$。由于 $s(k)\le J(k)+2$，定理 4.1 同时蕴含这个下界。
- **推论 4.2：** 出现的不同偶数间隙至少有 $\frac{c'}2\,p_k\log p_k\,L_3/L_2$ 个，与 $J(k)$ 已知最好的下界同阶。

**判决：◎（第一问的下界追平 $J(k)$ 已知最好的下界；第二问仍开放）。**
- 第二问问的是出现的间隙个数是否 $\gg J(k)$。我们只能与 $J(k)$ 的**下界**比较；$J(k)$ 的真实大小未知（上界是 Iwaniec 的 $p_k^2\log^2p_k$），所以第二问仍然开放。
- **更一般的意义（注 4.3）：** 下面的论证只用到 FGKMT 定理 2 的形式。今后任何同一形式的"筛素数"结果（用 $p\le x$ 的剩余类覆盖 $(x,y]$ 中几乎所有素数）都会自动转化为 $s(k)$ 的同阶下界。在这个意义上，用这类方法证明的 $J(k)$ 下界和 $s(k)$ 下界是等价的。

**状态标注：**
- 定理 4.1 严格，前提是 FGKMT 的定理 2 及其推导（已发表、经过审稿）。我们引用的原文见第 1 节。
- 另外只用到素数定理、筛法基本引理（Friedlander–Iwaniec《Opera de Cribro》第 6 章；Halberstam–Richert《Sieve Methods》定理 2.5）和初等计数。
- 外层的归约论证是本阶段的新内容，由 AI 辅助得出，没有经过审稿。
- 常数 $c'$ 没有算出，因为 FGKMT 的常数 $c$ 本身不显式。定理 3.1 的常数是显式的（约 $0.026$），在有限的 $k$ 上它仍然有用。

---

## 1. FGKMT 的筛素数定理（引用）

记 $L_2=\log\log x$，$L_3=\log\log\log x$。FGKMT 第 3 节取
$$y=c\,\frac{x\log x\,L_3}{L_2}\ (c\text{ 是固定的小常数}),\qquad z=x^{L_3/(4L_2)},$$
$$\mathcal S=\{s\text{ 素数}:\log^{20}x<s\le z\},\quad \mathcal P=\{p\text{ 素数}:x/2<p\le x\},\quad \mathcal Q=\{q\text{ 素数}:x<q\le y\}.$$
记 $S(\vec a)=\{n:n\not\equiv a_s\ (\mathrm{mod}\ s)\ \forall s\in\mathcal S\}$，$S(\vec b)$ 类似。

- **FGKMT 定理 2：** $x$ 充分大时，存在 $\vec a=(a_s)_{s\in\mathcal S}$ 和 $\vec b=(b_p)_{p\in\mathcal P}$，使得
$$\#\bigl(\mathcal Q\cap S(\vec a)\cap S(\vec b)\bigr)\ll\frac{x}{\log x}.$$
- **他们的推导：** 对 $p\le x$ 且 $p\notin\mathcal S\cup\mathcal P$ 令 $a_p=0$，对 $p\in\mathcal P$ 令 $a_p=b_p$，并记
$$T=\{n\in(x,y]:\ n\not\equiv a_p\ \forall p\le x\}.$$
  - $T$ 中的元素要么是 $\mathcal Q\cap S(\vec a)\cap S(\vec b)$ 中的素数，要么是 $z$-光滑数。后者至多 $y/\log^{4+o(1)}x$ 个。
  - 所以 $\#T\le K\,x/\log x$，$K$ 是绝对常数。
  - 最后，他们给 $T$ 的每个元素分配 $(x,Cx]$ 中一个不同的素数，用它覆盖该元素，从而盖住整个 $(x,y]$。

## 2. 定理 4.1 的证明

**坐标：**
- 记 $X=p_k$，取绝对常数 $C\ge K+3$，令 $x=X/C$。我们可用的素数恰是 $p\le Cx$。
- 偶数 $t$ 是间隙，当且仅当可以给每个 $p\le Cx$ 选一个剩余类 $c_p$，使某一对端点 $A$、$A+t$ 不被任何类覆盖，而两者之间的每个整数都被覆盖。这是引理 1.1 换一个原点的形式，由中国剩余定理得到。

固定偶数 $t\le y/2$，并固定 FGKMT 定理 2 给出的 $\vec a,\vec b$。

**第 1 步：选端点。** 称 $A\in(x,y-t]$ 为**候选**，如果
- 对每个素数 $s\le\log^{20}x$，有 $s\nmid A(A+t)$；
- 对每个 $s\in\mathcal S$，有 $A\not\equiv a_s$ 且 $A+t\not\equiv a_s\pmod s$。

这是一个筛问题：对每个 $s\le z$ 去掉 $\nu(s)\le2$ 个剩余类，其中 $\nu(2)=1$（因为 $t$ 是偶数）。
- **候选个数：** 区间长度 $\ge y/2-x\ge y/3$。取水平 $D=y^{1/2}$，则 $\log D/\log z\to\infty$。由二维筛的基本引理，候选个数
$$N_c\ \ge\ (1-o(1))\frac y3\prod_{s\le z}\Bigl(1-\frac{\nu(s)}s\Bigr)-O\bigl(y^{0.6}\bigr)\ \gg\ \frac{y}{(\log z)^2}.$$
  注意基本引理对**任意**剩余类都成立，所以黑箱给出的 $a_s$ 无论是什么都不影响这一步。
- **与大素数类的冲突：** 记 $I(A)=\#\{p\in\mathcal P:\ b_p\equiv A\text{ 或 }b_p\equiv A+t\pmod p\}$。则
$$\sum_{A\in(x,y]}I(A)\le\sum_{p\in\mathcal P}2\Bigl(\frac yp+1\Bigr)\le\frac{3y}{\log x}.$$
  所以存在候选 $A$ 使
$$I(A)\le\frac{3y}{N_c\log x}\ll\frac{(\log z)^2}{\log x}=\frac{\log x}{u^2}\le\log x,\qquad u=\frac{\log x}{\log z}=\frac{4L_2}{L_3}.$$

取这样的 $A$。

**第 2 步：赋值并修补。**
- **零类：** 对 $s\le\log^{20}x$ 以及 $z<s\le x/2$，令 $c_s=0$。
  - 例外：若 $z<s\le x/2$ 且 $s\mid A(A+t)$，则任取一个不覆盖 $A$、$A+t$ 的类（$s\ge3$，所以这样的类存在）。这样的例外至多 $2\log y/\log z\le3u$ 个。
  - 当 $s\le\log^{20}x$ 时，$s\nmid A(A+t)$ 由候选条件保证，所以零类不覆盖端点。
- **中等素数：** 对 $s\in\mathcal S$，令 $c_s=a_s$。由候选条件，它们不覆盖端点。
- **大素数：** 对 $p\in\mathcal P$，令 $c_p=b_p$。
  - 例外：若 $b_p$ 覆盖 $A$ 或 $A+t$，则改用一个不覆盖端点的类。这样的修补共 $I(A)\le\log x$ 个。

**第 3 步：数一数剩下多少。** 区间 $(A,A+t)\subset(x,y]$ 中还没被覆盖的位置，只可能来自三处：
1. FGKMT 推导中的集合 $T$：至多 $Kx/\log x$ 个；
2. 例外零类原本覆盖的 $s$ 的倍数：至多 $3u(y/z+1)$ 个。由于 $\log(x^{L_3/(4L_2)})=\log x\,L_3/(4L_2)\gg L_2$，这是 $o(x/\log x)$；
3. 被修补的大素数原本覆盖的位置：至多 $I(A)(2y/x+1)\ll\log^2x$ 个。

所以剩余集合 $L$ 满足 $|L|\le(K+o(1))\,x/\log x$。

**第 4 步：用 $(x,Cx]$ 中的素数逐点补位。**
- 依次对每个 $v\in L$，取一个尚未使用、且不整除 $(v-A)(A+t-v)$ 的素数 $p\in(x,Cx]$，令 $c_p\equiv v\pmod p$。
- 因为 $0<v-A,\ A+t-v<y<x^2$，这两个数各自至多有一个大于 $x$ 的素因子，所以每个 $v$ 至多排除 2 个素数。
- 可用素数有 $\pi(Cx)-\pi(x)=(C-1+o(1))\,x/\log x\ge|L|+3$ 个，所以分配一定能完成。
- 没用到的素数取不覆盖端点的类。

现在 $(A,A+t)$ 中每个整数都被覆盖，而 $A$、$A+t$ 不被任何类覆盖，所以 $t$ 是间隙。

**结论：** 所有偶数 $t\le y/2$ 都是间隙，于是
$$s(k)>\frac y2=\frac c2\cdot\frac{X}{C}\log\frac XC\cdot\frac{L_3}{L_2}\sim\frac{c}{2C}\cdot\frac{p_k\log p_k\,\log\log\log p_k}{\log\log p_k}.$$
∎

## 3. 为什么这一步之前看起来很难（注 4.4）

- **直接改写的障碍：** FGKMT 给 $\le\log^{20}x$ 的所有小素数取零类，使 $(x,y]$ 中幸存下来的几乎只有素数。如果像第二、三阶段那样把端点放在 $1$ 和 $t+1$，零类会覆盖 $t+1$ 的小素因子，修补它们的代价正是那个 $\log\log$。
- **反过来要求端点是素数也不行：** 把端点也放进 $(x,y]$，但要求两个端点都是素数，就需要每个 $t$ 都是两个素数之差，这是孪生素数型问题，挡在奇偶墙后面。
- **本阶段的关键观察：** 端点不必是素数，只需是**粗糙数**，即没有 $\le\log^{20}x$ 的素因子。
  - 端点的中等素因子落在 $\mathcal S$ 或 $(z,x/2]$ 中：前者由候选条件处理，后者的修补代价可以忽略。
  - 粗糙数对 $(A,A+t)$ 由筛法基本引理大量提供。这里只需要筛法的**上下界同阶**，不需要分辨素数，所以不受奇偶墙限制。
  - 剩下与黑箱大素数类的冲突，靠在候选中平均来避开。

## 4. 与前几个阶段的关系

| 阶段 | 下界 | 性质 |
|---|---|---|
| 1 | $(0.640-o(1))\,p_k$ | 自包含，常数显式 |
| 2 | $p_k\log p_k/L_2^4$ | 自包含 |
| 3 | $(0.026-\varepsilon)\,p_k\log p_k\,L_3/L_2^2$ | 自包含，常数显式（Rankin 量级） |
| 4 | $c'\,p_k\log p_k\,L_3/L_2$ | 以 FGKMT 定理 2 为黑箱，常数不显式 |

在 $s(k)$ 的下界上，第四阶段取代了前几阶段，但第一、三阶段的论证自包含、常数显式，仍有独立价值。
