# 第十二阶段：Guth–Maynard 能否改进 MRT 的 d₃ 步骤（8/33）？（2026-10-28）

**问题：** Matomäki–Radziwiłł–Tao（arXiv:1707.01315，下称 MRT）证明了：只要 $H\ge X^{8/33+\varepsilon}$，几乎所有 $h\le H$ 都满足平均 Hardy–Littlewood。第十一阶段已确认 $8/33$ 卡在 Type $d_3$ 步骤上，与零点无关。现在要问的是，Guth–Maynard 2024 的大值估计（arXiv:2405.20552）能否推动这一步。

**一句话答案：不能。** $d_3$ 步骤分两半：
- Dirichlet 多项式一半（Jutila）已经最优，到 $X^\varepsilon$ 为止；
- 指数和一半（命题 7.5）的损失出在一个"间距"步骤上，所处的区间是 $V\approx N^{1/2+\delta}$（刚过平方根），而 Guth–Maynard 只在 $N^{7/10}<V<N^{8/10}$ 才有改进。

另外，即使把 $d_3$ 做到完美，整体指数也只能降到 $3/13\approx0.2308$，因为下一道关卡是 $d_4$。

**状态标注：** 第 1 节是对原文的核对（附精确有理数计算）；第 2、3 节中，"Jutila 一半已最优"是简单的 Hölder 下界，属于严格论证；其余是分析，AI 辅助，未经专家核对。

脚本：`route/stage12_exponents.py`（Python 2.7，使用 `fractions`）。

---

## 1. 8/33 精确来自哪一项（核对 MRT §7–8）

记号：$H=X^\sigma$，$T=\lambda X$，其中 $X^{-1/6}\lesssim\lambda\lesssim1$；$M_1\lesssim X^{1/3}$ 是 $d_3$ 和中最短因子的长度；$L\approx M_1/H$。

- **Hölder 分解**（§7）：
  $$Z_1\le\lambda H\sum_J\tilde Y(t_J)\,m_J,\qquad m_J:=\int_J|D[g](\tfrac12+it)|^2dt,$$
  其中 $J$ 是长 $\sqrt{\lambda X}$ 的区间，$g=\alpha*\beta_2*\beta_3$ 的长度约 $X^{2/3}$。然后用 Hölder 指数 $(3/2,3)$，需要两件事：
  - **命题 7.4（Jutila 一半）：** $\sum_J m_J^3\ll X^{O(\varepsilon^2)}(\lambda X)^2$；
  - **命题 7.5（指数和一半）：** $\sum_j\tilde Y(t_j)^4\ll X^{-\varepsilon}H^4\sqrt{\lambda X}$。

  这里 $\tilde Y(t)$ 是最短因子 $D[\beta_1]$ 在长 $\approx H$ 的窗口上均方的非对角部分，写成 $\sum_m e\big(\tfrac{t}{2\pi}\log\tfrac{m+\ell}{m-\ell}\big)$ 的和。

- **MRT 实际证到的**（§8 末尾）：
  $$\sum_j\tilde Y(t_j)^4\ll X^{4/3}+H^{-3/2}\lambda X^{11/6}.$$
  - 第二项在最坏情形 $\lambda=1$ 下，要求 $H^{11/2}\ge X^{4/3}$，即 $\sigma\ge 8/33$。**这就是 8/33。** 脚本复算结果一致。
  - 第一项在最坏情形 $\lambda=X^{-1/6}$ 下给出 $\sigma\ge11/48\approx0.229$，不是瓶颈。
- **$d_4$ 和**（引理 7.2）：用指数对 $(1/14,2/7)$ 得到 $7/30$；按注 7.3 换用 Robert 的指数对得到 $3/13\approx0.2308$。$\sigma<1/5$ 时还会出现 $d_5$ 和。

## 2. Jutila 一半已经最优（严格的小结论）

$J$ 的个数约为 $\sqrt{\lambda X}$；$D[g]$ 在临界线上的均方约为 1（相差 $\log$ 因子），所以 $\sum_J m_J\approx\lambda X$。由 Hölder 不等式，
$$\sum_J m_J^3\ \ge\ \frac{(\sum_J m_J)^3}{(\#J)^2}\ \approx\ \frac{(\lambda X)^3}{\lambda X}=(\lambda X)^2 .$$
命题 7.4 的上界恰好是 $(\lambda X)^2$，所以它在相差 $X^{O(\varepsilon^2)}$ 的意义下已经是最优的。**任何大值估计（包括 Guth–Maynard）都不可能改进这一半。**

## 3. 指数和一半：损失在哪里，Guth–Maynard 为什么用不上

- **理想值：** 如果 $\tilde Y$ 有平方根抵消，那么 $\tilde Y\approx\sqrt{M_1}$，于是 $\sum_j\tilde Y^4\approx\sqrt T\,M_1^2$，由此得到 $\sigma\ge1/6$，恰好与方法的零点密度下限重合。
- **MRT 损失的比例：** MRT 的界与理想值之比为
  $$\frac{\sqrt T\,M_1^{1/2}}{H^{3/2}}\approx X^{0.3}\qquad(\sigma\approx0.24).$$
- **损失的来源：** 不在四次矩。
  - MRT 的 $W_3\ll L^2A^2$ 恰好等于对角项下界（面积 $A\cdot L^2A/M_1^2$ 乘以 $M_1^2$），四次矩本身已经最优。
  - 损失在把离散点 $(t_j\ell/M_1,\ t_j\ell^3/M_1^3)$ 换成整块区域 $\alpha\ll S$ 上的积分的那一步（引理 2.3(i) 及其后的重数 $\mu(\alpha,\beta)$ 计数）。这一步扔掉了"$t_j$ 之间相隔 $\sqrt{\lambda X}$"这个结构。
  - 所以它本质上是一个**间距问题**：平面上点集 $\{(t\ell/M_1,\ t\ell^3/M_1^3)\}$ 的能量，属于 Robert–Sargos 或双大筛法一类的问题。
- **Guth–Maynard 适用的区间不对：**
  - 它的定理 1.1 给出 $R\le T^{o(1)}(N^2V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4})$，并且只在 $N^{7/10}<V<N^{8/10}$ 时比"均值定理加 Huxley"好（原文语）。
  - 这里需要控制的是 $D[\beta_1]$（长 $N=M_1\approx T^{1/3}$，系数光滑）在窗口内**略高于平方根**的值，即 $V\approx N^{1/2+\delta}$。把它升幂成 $D^3$（长度约 $T$）后，仍然处在平方根区间。
  - 而且 Guth–Maynard 针对的是任意系数，不利用系数的光滑性。光滑系数的正确工具是指数对、Robert–Sargos 和 decoupling。

## 4. 天花板：只改进 $d_3$ 最多能到哪里

设 MRT 的损失只恢复一部分：把约束写成
$$\sqrt T M_1^2\big(\sqrt T M_1^{1/2}H^{-3/2}\big)^\theta\le H^4\sqrt T ,$$
其中 $\theta=1$ 对应 MRT，$\theta=0$ 对应理想值。于是 $\sigma_{d_3}(\theta)=\tfrac{(2/3)(1+\theta)}{4+1.5\theta}$。

| $\theta$ | $d_3$ 给出的 $\sigma$ | 整体指数（$d_4$ 用 Robert 的 $3/13$） |
|---|---|---|
| 1（MRT） | 8/33 = 0.2424 | 0.2424 |
| 0.9 | 76/321 = 0.2368 | 0.2368 |
| **0.8** | **3/13 = 0.2308** | **0.2308** |
| 0.5 | 4/19 = 0.2105 | 0.2308（被 $d_4$ 卡住） |
| 0（理想） | 1/6 | 0.2308（被 $d_4$ 卡住） |

**结论：**
- 间距步骤只要恢复 20% 的损失指数（$\theta=0.8$），就能把 $8/33$ 推到 $3/13$。这是一个具体、可能可做的指数和问题。
- 再往下要同时处理 $d_4$：需要短区间六次矩，目前未知；Guth–Maynard 同样处在错误的区间，帮不上。$\sigma<1/5$ 时还要处理 $d_5$。

## 5. 对路线图的意义

- **移位坐标的分析一侧已经完全定位：**
  - 零点（准 RH、Guth–Maynard）都不是瓶颈；
  - Jutila 一半已经最优；
  - 唯一的松动在一个光滑指数和的间距步骤上，而且最多推到 $3/13$。
- 这与孪生素数相距更远：$3/13$ 仍然是"几乎所有 $h\le X^{0.23}$"，而孪生要求固定的 $h=2$。**从奇偶的角度看，这条线是死的**；它作为纯分析课题有价值（"把 8/33 推到 3/13"），但不是 TPC 的通道。
- **判决：✗（对 TPC）；作为独立分析问题记为 ◐。**
