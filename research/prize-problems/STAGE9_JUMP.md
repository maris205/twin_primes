# 第九阶段：攻"跳跃"——短滞后，以及对几乎所有 $k$ 成立

**结论：**
- **定理 9.1（短滞后）：** 定理 7.1 和 8.1 里的层 $\lceil(1-\eta)k\rceil$ 可以换成 $k-\lceil k^{1-\kappa}\rceil$，$\kappa>0$ 是固定的小常数。
- **定理 9.2（几乎所有 $k$）：** 对每个固定的 $\varepsilon>0$，在一个密度为零的例外集之外，
  $$s(k)\ \ge\ (1-\varepsilon)\min\bigl(J(k),\,p_k^{1+\delta_0}\bigr),\qquad |G_k|\ \ge\ c(\varepsilon)\min\bigl(J(k),\,p_k^{2-\varepsilon}\bigr).$$
  例外集在 $[1,K]$ 里至多有 $O(K^{1-\kappa}\log K)$ 个元素。

**这回答了什么：**
- **第一问：** 存在一个密度为零的集合 $\mathcal E'$，使得 $k$ 跑过 $k\notin\mathcal E'$ 且 $J(k)\le p_k^{1+\delta_0}$ 的值时，$s(k)=(1+o(1))\,J(k)$（由下面的定理对 $\varepsilon\to0$ 做对角线论证）。注意例外集只是相对**全体整数**密度为零；满足 $J(k)\le p_k^{1+\delta_0}$ 的 $k$ 有多少，目前不知道。下界 $s(k)$ 和上界 $J(k)+2$ 渐近重合，没有指标平移。
- **第二问：** 对例外集之外的每个 $k$，只要 $J(k)\le p_k^{2-\varepsilon}$，第二问成立。无条件地，对几乎所有 $k$，偶数间隙个数 $\ge J(k)^{1-\varepsilon}$。
- **没有解决的：** 对**每个** $k$ 仍需要
  - (R1′) $J(k)\le C\,J(k-\lceil k^{1-\kappa}\rceil)$，即 $J$ 在长度 $k^{1-\kappa}$ 的窗口内不放大常数倍；
  - (R2′) $J(k)\le p_k^{2-\varepsilon}$。

  两条都没有证明。本阶段证明的是：(R1′) 失败的 $k$ 是稀疏的。

> **第十阶段检查：** [STAGE10_CHECK.md](STAGE10_CHECK.md) 逐步重推了本阶段的证明，没有发现数学错误；收紧了"几乎所有 $k$"的一处表述，补写了 $M$ 的下界说明和 $\kappa(\varepsilon)$。

**状态标注：** 定理 9.1、9.2 是**定理**，证明见 §2、§3，只用第七、八阶段的同一组筛法定理，**未经审稿**。注记 8.5 里的去掉第三项的做法在 §2 被完整写出。本阶段**没有新的数值**。本阶段由 AI 辅助完成（Claude，Anthropic）。

---

## 1. 想法

第七、八阶段的证明里，自由素数个数 $F$ 必须超过平均修补代价，而平均代价大约是 $L/B$，$B$ 是筛法水平。当时取的 $B\approx(L/p_k)\log p_k$ 是**最小**的可行值，所以需要 $F\asymp\eta k$ 个自由素数，滞后是 $\eta k$。

如果把 $B$ 取到下界筛允许的**最大**值（线性筛 $B\approx L^{1/(2+\theta)}$，二维 $B\approx L^{1/s_0}$），平均代价就降到 $L^{1/2+o(1)}$ 或 $L^{1-1/s_0}$。在 $L\le p_k^{2-\varepsilon}$ 或 $L\le p_k^{1+\delta_0}$ 时，这比 $k$ 小一个幂次，于是 $F=k^{1-\kappa}$ 个自由素数就够了。

窗口变短之后，"跳跃"可以计数：$J$ 在 $[K,2K]$ 上至多增长 $K^{3}$ 倍（Iwaniec），所以互不相交的、各自放大 $C$ 倍的短窗口至多有 $O(\log K/\log C)$ 个，它们一共只覆盖 $O(K^{1-\kappa}\log K)$ 个 $k$。

---

## 2. 定理 9.1（短滞后）

**定理 9.1.**
- **(a)** 存在绝对常数 $\delta_0,\kappa_0>0$：对固定的 $\varepsilon\in(0,\tfrac12)$ 和充分大的 $k$，设 $j=k-\lceil k^{1-\kappa_0}\rceil$，$L=\min\bigl(J(j)-1,\,p_k^{1+\delta_0}\bigr)$，则每个偶数 $t\le(1-\varepsilon)L$ 属于 $G_k$。
- **(b)** 对固定的 $\varepsilon\in(0,1)$，存在 $c(\varepsilon)>0$：对充分大的 $k$，设 $j=k-\lceil k^{1-\varepsilon/4}\rceil$，$L=\min\bigl(J(j)-1,\,p_k^{2-\varepsilon}\bigr)$，则至少 $cL$ 个偶数 $t\le L/2$ 属于 $G_k$。

*证明.* (a) 沿用定理 7.1 的证明，(b) 沿用定理 8.1 的证明，只改两处。记 $F=k-j$，$X=L-t$（(a) 中 $X\ge\varepsilon L$），$M=\varepsilon L/(2p_k)$。由定理 B 和 $J(j)\ge s(j)-2$，$J(j)/p_k\gg\log p_k\,\log_3p_k/(\log_2p_k)^2$，所以对大的 $k$ 有 $M\ge(\log p_k)^{1/2}$，即 $\log M\ge\tfrac12\log\log p_k$。

- **改动一：筛法水平取到最大。**
  - (a) 取 $B=X^{1/s_0}$，$s_0$ 是基本引理 (S1) 的常数，于是 (S1) 适用：$|\mathcal X|\ge\tfrac12XV$。
  - (b) 取 $B=(L/4)^{1/(2+\theta)}$，$\theta=\varepsilon/4$，于是线性筛 (L) 在每个长度 $\ge L/2-1$ 的子区间上适用；第八阶段 §2.2、§2.3 不变，给出 $|\mathcal T|\ge cL$ 和 $r(t)\ge c_1L/\log^2B$（$t\in\mathcal T$）。

- **改动二：第三步对所有 $B<q\le p_j$ 都用上界筛 (U)。** 固定 $q$ 和满足 $q\in Q(x)$ 的两个同余类之一 $x\equiv a\pmod q$，写 $x=a+qn$。$n$ 跑过长度 $\ge X/q\ge M$ 的区间（(b) 中长度 $L/(2q)\ge M$），条件"$x$、$x+t$ 都避开 $p\le B$ 的类"对 $p\le z:=\min(B,M)$ 给出 $n$ 模 $p$ 的至多两个禁类。由 (U)：
  - (a) $N_q\le C\,\dfrac Xq\,V\Bigl(\dfrac{\log B}{\log z}\Bigr)^2$；
  - (b) $N_q\le C\,H\,\dfrac{L}{q\log^2z}$。

  在两种情形下，除以 $|\mathcal X|$（或 $|\mathcal X_t|$）后，
  $$\text{平均代价}\ \le\ C'\Bigl(\frac{\log B}{\log z}\Bigr)^2\Bigl[\frac{t}{B\log B}+\log\log p_k\Bigr]\ \le\ C''\log^2p_k\cdot\frac LB ,$$
  因为 $\log z\ge\tfrac12\log\log p_k$，$\log B\le\log p_k^2$。

- **数值核对。**
  - (a) $L/B\ll_\varepsilon L^{1-1/s_0}\le p_k^{(1+\delta_0)(1-1/s_0)}\le p_k^{1-1/(2s_0)}$，取 $\delta_0=1/(2s_0)$。取 $\kappa_0=1/(4s_0)$，则平均代价 $\le p_k^{1-1/(2s_0)+o(1)}\le F/2$。
  - (b) $L/B\ll L^{(1+\theta)/(2+\theta)}\le p_k^{(2-\varepsilon)(4+\varepsilon)/(8+\varepsilon)}\le p_k^{1-\varepsilon/3}$。所以平均代价 $\le p_k^{1-\varepsilon/3+o(1)}\le F/2$，$F=\lceil k^{1-\varepsilon/4}\rceil$。
  - 两种情形都有 $B<p_j$。

- **第四、五步不变。** 它们只用到"暴露点 $\le F/2$"和 $t<p_j^2$。∎

**注记 9.3.** 原来的定理 7.1、8.1 是定理 9.1 的特例（$\lceil k^{1-\kappa}\rceil\le\eta k$）。注记 8.5 的去掉第三项的做法就是这里的改动二。

**注记 9.4（滞后可以随 $L$ 变短）.** 所需的自由素数只是 $\log^2p_k\cdot L/B$。在猜想 $J(k)=p_k^{1+o(1)}$ 下，(b) 中只需 $F=k^{1/2+o(1)}$。滞后不可能用这个方法缩到 $O(1)$，因为平均代价至少是 $L/B\ge L^{1/2}$。数值上 $s(k)>J(k-1)$（$6\le k\le26$），这个方法达不到。

---

## 3. 定理 9.2（几乎所有 $k$）

**引理 9.5（跳跃是稀疏的）.** 设 $C>1$，$F(k)=\lceil k^{1-\kappa}\rceil$，$\mathfrak B_C=\{k:\ J(k)>C\,J(k-F(k))\}$。则对充分大的 $K$，
$$\#\bigl(\mathfrak B_C\cap[K,2K]\bigr)\ \le\ \Bigl(1+\frac{3\log K}{\log C}\Bigr)\bigl(F(2K)+1\bigr).$$

*证明.*
- 贪心地往下取：$k_1$ 是 $\mathfrak B_C\cap[K,2K]$ 的最大元；$k_{i+1}$ 是 $\mathfrak B_C\cap[K,\,k_i-F(k_i))$ 的最大元，直到为空。设一共取了 $m$ 个。
- 由取法，$\mathfrak B_C\cap[K,2K]\subseteq\bigcup_i[k_i-F(k_i),\,k_i]$，所以个数 $\le m\,(F(2K)+1)$。
- $J$ 单调不减，且 $k_{i+1}<k_i-F(k_i)$，所以 $J(k_i)>C\,J(k_i-F(k_i))\ge C\,J(k_{i+1})$。于是 $J(2K)\ge J(k_1)>C^{m-1}J(k_m)\ge C^{m-1}J(K)$。
- 由 Iwaniec 的上界 $J(2K)\ll p_{2K}^2\le K^{3}$，且 $J(K)\ge2$，得 $m-1\le3\log K/\log C$。∎

**定理 9.2.** 固定 $\varepsilon$，取 $\kappa=\min(\kappa_0,\varepsilon/8)$。在一个满足 $\#(\mathcal E\cap[1,K])\ll_\varepsilon K^{1-\kappa}\log K$ 的集合 $\mathcal E$ 之外，
- (i) $s(k)\ge(1-\varepsilon)\min\bigl(J(k),\,p_k^{1+\delta_0}\bigr)$；
- (ii) $|G_k|\ge\tfrac12c(\varepsilon)\min\bigl(J(k),\,p_k^{2-\varepsilon}\bigr)$；
- (iii) $|G_k|\ge J(k)^{1-\varepsilon}$。

*证明.*
- (i) 对 $k\notin\mathfrak B_{1+\varepsilon/2}$ 用定理 9.1(a)（以 $\varepsilon/2$ 代 $\varepsilon$）：$s(k)\ge(1-\tfrac\varepsilon2)\min(J(k-F),p_k^{1+\delta_0})\ge\frac{1-\varepsilon/2}{1+\varepsilon/2}\min(J(k),p_k^{1+\delta_0})$。
- (ii) 对 $k\notin\mathfrak B_2$ 用定理 9.1(b)：$|G_k|\ge c\min(J(k-F),p_k^{2-\varepsilon})\ge\tfrac c2\min(J(k),p_k^{2-\varepsilon})$。
- (iii) 对 (ii) 用 $\varepsilon/2$，再用 $J(k)\le p_k^{2+o(1)}$：$J(k)^{1-\varepsilon}\le p_k^{2-2\varepsilon+o(1)}$。
- 例外集由引理 9.5 控制，对 $[K,2K]$ 按二进分块求和。∎

---

## 4. 更新后的地图

| | 第八阶段之后 | 第九阶段之后 |
|---|---|---|
| 层的滞后 | $\eta k$ | $k^{1-\kappa}$ |
| $s(k)$ 与 $J(k)$ | $(1-\varepsilon)\min(J((1-\eta)k),p_k^{1+\delta_0})\le s(k)$ | 几乎所有 $k$：$s(k)\ge(1-\varepsilon)\min(J(k),p_k^{1+\delta_0})$ |
| 第二问成立的 $k$ | 至少一半的几何尺度（需 $J\le p_k^{2-\varepsilon}$） | 几乎所有 $k$（需 $J\le p_k^{2-\varepsilon}$） |
| 第二问对每个 $k$ 还需要 | $J(k)\ll J((1-\eta)k)$ 与 $J\le p_k^{2-\varepsilon}$ | $J(k)\ll J(k-k^{1-\kappa})$ 与 $J\le p_k^{2-\varepsilon}$ |

## 5. 判决

- **跳跃问题对几乎所有 $k$ 被绕过了**：不需要证明 $J$ 正则，只用到 $J$ 至多多项式增长。
- **对每个 $k$，跳跃问题没有解决。** 剩下的问题是：$J$ 能不能在 $k^{1-\kappa}$ 步之内放大常数倍。引理 9.5 说这至多在稀疏的 $k$ 上发生；排除它需要关于最大覆盖结构的新信息。
- **端点障碍 $J\le p_k^{2-\varepsilon}$ 不变**，它等价于对 Iwaniec 上界的幂次改进。
- **需要外部检查的地方：** §2 改动二中 $z=\min(B,M)$ 的取法与 $(\log B/\log z)^2$ 的损失，以及 (b) 的指数核对。
