# 第三阶段：去掉 #854 下界中的对数损失（2026-10-30）

**问题：** 定理 2.1 给出 $s(k)\gg p_k\log p_k/(\log\log p_k)^4$。注 2.3 指出指数 4 来自两处损失。能否把它们都去掉，达到 Rankin 量级？

**一句话答案：能。**
- **定理 3.1（无条件）：** 对任意固定的 $\varepsilon>0$ 和充分大的 $k$，
$$s(k)\ \ge\ \Bigl(\frac{e^\gamma}{8C_f}-\varepsilon\Bigr)\frac{p_k\log p_k\cdot\log\log\log p_k}{(\log\log p_k)^2},\qquad C_f=\prod_q\Bigl(1+\frac{2q-1}{(q-1)^3}\Bigr)=8.4425\ldots$$
  所以常数约为 $0.0264$。出现的不同偶数间隙也至少有这个量级（差一个因子 2）。
- **这是 Rankin 量级：** 它与 Rankin（1938）对 Jacobsthal 函数的经典下界同阶。
  - 与已知最好的下界 $J(k)\gg p_k\log p_k\cdot\log\log\log p_k/\log\log p_k$（Ford–Green–Konyagin–Maynard–Tao）只差一个 $\log\log p_k$ 因子。
  - 定理 2.1 与它差 $(\log\log p_k)^3\log\log\log p_k$。
- **两处改进：**
  1. **端点权重：** 用 Brun–Titchmarsh 不等式对移位素数平均，权重从最大值 $(\log\log x)^2$ 降到常数 $4C_f$。
  2. **光滑数参数：** 改用 Canfield–Erdős–Pomerance 的光滑数估计，$u$ 从 $3\log\log x$ 降到 $(1+\eta)\log\log x/\log\log\log x$。

**判决：◎（第一问达到 Rankin 量级；第二问仍开放）。**
- 第二问要与 $J(k)$ 本身比较，而 $J(k)$ 的真实大小未知，所以仍然开放。
- 剩下的 $\log\log p_k$ 因子正是 Rankin 构造与 FGKMT 构造的差距。要跨过它，需要让每个大素数覆盖不止一个位置（超图覆盖），见第 4 节。

**状态标注：**
- 定理 3.1 严格。它用到素数定理、Mertens 定理、$n/\varphi(n)$ 的 Rosser–Schoenfeld 上界，以及两个标准结果：
  - **Brun–Titchmarsh 不等式**（Montgomery–Vaughan 1973）：$\pi(Y;d,a)\le 2Y/(\varphi(d)\log(Y/d))$；
  - **光滑数上界**（Canfield–Erdős–Pomerance 1983；也可由 Rankin 技巧直接得到）：$u\to\infty$ 时 $\Psi(X,X^{1/u})\le X u^{-(1+o(1))u}$，在我们的范围内一致成立。
- 表 3 是数值，只说明平均权重确实有界，不是证明的一部分。
- 定理 3.1 仍是渐近结论，有限 $k$ 上的可核验范围见第二阶段表 2。

脚本：`stage3_endpoint_weight.py`。

---

## 1. 记号

沿用第二阶段的坐标（STAGE2_RANKIN.md 第 1 节）：
- 位置 $1,\dots,t+1$；端点 $1$ 和 $t+1$ 不被覆盖，$2,\dots,t$ 全部被覆盖。
- $x=p_k$，$L_2=\log\log x$，$L_3=\log\log\log x$。
- 固定 $\eta>0$，取 $u=(1+\eta)L_2/L_3$，$z=x^{1/u}$。
- 记
$$H(n)=\prod_{q\mid n,\ q\le z}\Bigl(1-\frac1q\Bigr)^{-1},\qquad W(z)=\prod_{q\le z}\Bigl(1-\frac1q\Bigr)=\frac{e^{-\gamma}+o(1)}{\log z}=\frac{(e^{-\gamma}+o(1))\,u}{\log x}.$$

设 $t\le\lambda x$ 为偶数，其中
$$\lambda=c\,\frac{\log x\cdot L_3}{L_2^2},\qquad c<\frac{e^\gamma}{8C_f(1+\eta)}.$$
目标是证明 $t$ 是间隙。

## 2. 定理 3.1 的证明

**A. 中等素数 $z<p\le x/2$：** 与定理 2.1 相同。
- 若 $p\nmid t+1$ 取类 $0$，否则任取一个容许类。被放弃的位置记为 $E$，$|E|\le 2u(t/z+1)$。
- 因为 $t<(x/2)^2$，剩余集合满足 $S_A\subset S_{\rm sm}\cup S_{\rm pr}\cup E$，其中
  - $S_{\rm sm}$ 是不超过 $t$ 的 $z$-光滑数；
  - $S_{\rm pr}=\{mP:\ m\le 2\lambda,\ x/2<P\le t/m,\ P\text{ 为素数}\}$。

**B. 小素数 $q\le z$ 随机取容许类。** 与定理 2.1 一样，期望剩余个数为
$$\mathbb E|S_B|\ \le\ W(z)\sum_{i\in S_A}H(i-1)\,H(t+1-i)\ \le\ W(z)\Bigl[M\bigl(|S_{\rm sm}|+|E|\bigr)+\sum_{i\in S_{\rm pr}}\frac{h(i-1)+h(t+1-i)}2\Bigr],$$
其中：
- $h=H^2$；
- 第二个不等式对 $S_{\rm pr}$ 用了 $ab\le(a^2+b^2)/2$；
- $M=\max_{n\le t}H(n)^2\le(e^\gamma L_2+3)^2$（Rosser–Schoenfeld）。

**B1. 光滑部分可以忽略。**
- $u\log u=(1+\eta)L_2(1-o(1))$，所以 $\Psi(t,z)\le t\,(\log x)^{-1-\eta/2}$。
- 于是 $M(|S_{\rm sm}|+|E|)=o\bigl(t/\log x\bigr)$，比下面的主项小一个 $L_2$ 因子以上。

**B2. 移位素数上的平均（关键一步）。** 取 $w_0=(\log x)^2$。

- **截断：** 当 $q\ge2$ 时 $(1-1/q)^{-1}\le e^{2/q}$。对 $n\le t$，有 $\omega(n)\le 2\log x/\log2$，所以
$$H(n)\le H_1(n)\exp\Bigl(\frac{2\omega(n)}{w_0}\Bigr)=(1+o(1))H_1(n),\qquad H_1(n)=\prod_{q\mid n,\ q\le w_0}\Bigl(1-\frac1q\Bigr)^{-1}.$$
- **展开：** $H_1(n)^2=\sum_{d\mid n,\ d\mid P(w_0)}f(d)$，其中 $f$ 是平方自由数上的乘性函数，满足
$$f(q)=\Bigl(1-\frac1q\Bigr)^{-2}-1=\frac{2q-1}{(q-1)^2}\le\frac6q .$$
- **计数：** 固定 $m\le2\lambda$，记 $Y_m=t/m\ge x/2$。条件 $d\mid mP-1$ 要求 $(m,d)=1$，此时它等价于 $P$ 落在模 $d$ 的一个剩余类中。取 $D=x^{1/2}$。
  - **$d\le D$：** 由 Brun–Titchmarsh，这样的 $P\le Y_m$ 至多 $2Y_m/(\varphi(d)\log(Y_m/d))\le(4+o(1))\,Y_m/(\varphi(d)\log x)$ 个。对 $d$ 求和，贡献至多
  $$(4+o(1))\frac{Y_m}{\log x}\sum_{d}\frac{f(d)}{\varphi(d)}\le(4+o(1))\,C_f\frac{Y_m}{\log x}.$$
  - **$d>D$：** 用平凡计数 $Y_m/d+1$。
    - "$+1$" 部分至多 $\sum_{d\le t}6^{\omega(d)}/d\ll(\log x)^6$。
    - 主体部分用 Rankin 技巧，取 $\varepsilon=1/\log w_0$：
  $$\sum_{\substack{d\mid P(w_0)\\ d>D}}\frac{f(d)}d\le D^{-\varepsilon}\prod_{q\le w_0}\Bigl(1+\frac{e\,f(q)}q\Bigr)\ll\exp\Bigl(-\frac{\log x}{4L_2}\Bigr).$$
    两部分都可以忽略。
- **另一个端点：** $h(t+1-mP)$ 的处理完全相同，只是剩余类变成 $P\equiv(t+1)\bar m\pmod d$。
- **对 $m$ 求和：** 由 $\sum_{m\le2\lambda}Y_m\le t(1+\log2\lambda)$，得
$$\sum_{i\in S_{\rm pr}}\frac{h(i-1)+h(t+1-i)}2\le(4C_f+o(1))\frac{t\,(1+\log2\lambda)}{\log x}.$$

所以存在一种选择，使
$$|S_B|\le(1+o(1))\,4C_fe^{-\gamma}\,u\,\frac{\lambda(1+\log2\lambda)\,x}{(\log x)^2}.$$

**C. 大素数 $x/2<p\le x$：** 与定理 2.1 相同。只要 $|S_B|\le N-3$（$N=(1+o(1))\,x/(2\log x)$），就能逐点补位完成覆盖。

**代入：** $1+\log2\lambda=(1+o(1))L_2$，$u=(1+\eta)L_2/L_3$，所以
$$|S_B|\le(1+o(1))\,4C_fe^{-\gamma}(1+\eta)\,c\,\frac{x}{\log x}<(1-o(1))\frac{x}{2\log x},$$
只要 $c<e^\gamma/(8C_f(1+\eta))$。最后令 $\eta\to0$。∎

**推论 3.2：** 出现的不同偶数间隙至少有 $(\frac{e^\gamma}{16C_f}-\varepsilon)\,p_k\log p_k\,L_3/L_2^2$ 个。

## 3. 数值：平均权重确实有界（表 3）

`stage3_endpoint_weight.py` 对几组 $(x,\lambda,u)$ 精确执行 A 步，然后计算：
- B 步剩余个数的精确期望；
- 端点权重 $H(i-1)H(t+1-i)$ 在 $S_A$ 和 $S_{\rm pr}$ 上的平均；
- 定理 2.1 使用的最大权重 $(e^\gamma\log\log t+3)^2$。

| $x$ | $\lambda$ | $u$ | $\lvert S_A\rvert$ | 精确期望 $\mathbb E\lvert S_B\rvert$ | 平均权重（$S_A$） | 平均权重（$S_{\rm pr}$） | 定理 2.1 用的最大权重 |
|---|---|---|---|---|---|---|---|
| $10^5$ | 2 | 3 | 32,407 | 4,861 | 4.45 | 5.36 | 55.6 |
| $10^5$ | 4 | 3 | 76,452 | 14,496 | 4.71 | 5.30 | 57.1 |
| $10^6$ | 2 | 3 | 265,376 | 34,327 | 4.53 | 5.39 | 60.3 |
| $10^6$ | 4 | 3 | 648,688 | 107,842 | 4.82 | 5.46 | 61.6 |
| $10^6$ | 4 | 4 | 527,065 | 128,113 | 5.19 | 5.42 | 61.6 |
| $10^7$ | 2 | 3 | 2,377,094 | 261,241 | 4.50 | 5.27 | 64.4 |

**读法：**
- **平均权重稳定在 4.5–5.5：** 它不随 $x$ 增长，而定理 2.1 用的最大值从 56 涨到 64，大了一个数量级。这正是定理 3.1 去掉的 $(\log\log x)^2$。
- **证明中的常数偏保守：** 平均权重远小于 $4C_f\approx33.8$，因为 Brun–Titchmarsh 的因子 2 与 $ab\le(a^2+b^2)/2$ 都有富余。
- **只看量级：** 在这些 $x$ 上，精确期望仍大于可用的大素数个数（例如 $x=10^6$ 时约 3.7 万个）。定理 3.1 的增长因子只有在 $x$ 极大时才起作用，所以本表只检验权重的量级。

## 4. 还差什么（注 3.3，分析）

- **剩下的损失：** 现在唯一的对数级损失来自 $S_{\rm pr}$ 的大小 $\sim t\log\lambda/\log x$。这些"小倍数乘大素数"的位置，每个都要单独占用一个大素数。
- **这就是 Rankin 屏障：** 在 Jacobsthal 问题中，跨过它的是 Maier–Pomerance（1990）、Pintz（1997）和 FGKMT（2018）的方法。他们让大素数的剩余类随机或半随机地选取，使一个大素数平均覆盖多个剩余位置，再用超图覆盖定理收尾。
- **对 #854 的意义：** 把这些方法改写成"两端保持不被覆盖"的版本，预期会得到 $s(k)\gg p_k\log p_k\cdot L_3/L_2$，与 $J(k)$ 已知最好的下界同阶。
  - 端点条件只让每个素数少两个可选类。本阶段说明这在平均意义下只付出常数代价，所以改写看起来可行，但工作量大，没有在本阶段完成。
- **第二问：** 即使做到这一步，第一问的下界也只与 $J(k)$ 的**下界**同阶，第二问（出现的间隙个数是否 $\gg J(k)$）仍然依赖 $J(k)$ 的真实大小。
