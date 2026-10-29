# 第十七阶段：把"绝对值 Mellin 障碍"写成严格命题（2026-10-28）

**目标：** 第十六阶段的数值显示，对孪生双线性形式
$$\mathcal B=\sum_{p,q}a_pb_q\overline{c(pq)},\qquad c(r)=\lambda(r+2),$$
任何只用绝对值的 Mellin 论证都停在平凡界的常数倍上。本阶段把这一点证成定理。

**结果：成功（✓，定理）。** 已写入论文 v1.2，作为命题 7.8，并附注 7.9 说明适用范围。

**状态标注：**
- 命题是严格证明。黑箱只有一个：二维 Berry–Esseen 定理（Bentkus 2005）。
- 常数 $\kappa$ 非常小。
- 对抗数值是数值证据。

脚本：`route/stage17_adversary.py`；结果见 `stage17_adversary_k{12,24,48}.json`。

---

## 1. 命题

**设定：**
- $\mathcal P$ 为 $[P,2P]$ 中的素数，$k=|\mathcal P|$；$\mathcal S=\{pq\}$，于是 $|\mathcal S|=k(k+1)/2$。
- $A(t)=\sum a_pp^{-it}$，$B_b(t)=\sum b_qq^{-it}$，$C(t)=\sum_{r\in\mathcal S}c(r)r^{-it}$。
- $\mathbf M$ 表示 Bohr 均值（$T\to\infty$ 的时间平均）。

于是 $\mathcal B=\mathbf M[A B_b\bar C]$，由三角不等式 $|\mathcal B|\le\mathbf M|AB_bC|$。任何在均值号内取绝对值的论证，之后无论怎样估计 $\mathbf M|AB_bC|$（Hölder 拆分、矩、大值分解、$\Lambda(p)$/Sidon、decoupling），最好也只能证到这个界。

**命题 7.8.** 存在绝对常数 $\kappa>0$ 和 $k_0$，使得当 $k\ge k_0$ 时，对所有满足 $|a_p|=|b_q|=|c(r)|=1$ 的 $a,b,c$，都有
$$\mathbf M\big[|A\,B_b\,C|\big]\ \ge\ \kappa k^2=\kappa\cdot\text{平凡界}.$$

因此对 $c=\lambda(\cdot+2)$，绝对值论证证不出 Type II 界 $|\mathcal B|=o(k^2)$，而真实值预期只有 $O(k^{1+\varepsilon})$。

## 2. 证明思路（完整证明见论文）

1. **约化到环面（Kronecker–Weyl）：** $\{\log p\}$ 在 $\mathbb Q$ 上线性无关，所以 $(p^{-it})_p$ 在 $\mathbb T^k$ 上等分布。Bohr 均值因此等于对独立均匀相位 $\theta_p$（Steinhaus 变量）求期望。由唯一分解，不同的 $r$ 对应不同的单项式，所以 $\mathbb E|C|^2=|\mathcal S|$。
2. **矩（唯一分解计数）：**
   - $\mathbb E|A|^{2m}\le m!\,k^m$；
   - $\mathbb E|C|^{2m}\le K_m|\mathcal S|^m$，其中 $K_2\le6$，$K_6\le12!$。
3. **反集中：** 由二维 Berry–Esseen，$\mathbb P(|A|^2\le\delta k)\le\delta+O(k^{-1/2})$，取 $\delta=1/100$。坏事件的概率不超过 $0.04$，而 $|C|^2$ 在坏事件上的质量不超过 $\sqrt6\cdot0.2|\mathcal S|<\frac12|\mathcal S|$。由此 $\mathbb E|F|^2\ge\frac12\delta^2k^2|\mathcal S|$，其中 $F=AB_bC$。
4. **四阶矩上界：** 由 Hölder 和步骤 2 的矩，$\mathbb E|F|^4\ll k^4|\mathcal S|^2$。
5. **反向 Hölder：** $\mathbb E|F|\ge(\mathbb E|F|^2)^{3/2}/(\mathbb E|F|^4)^{1/2}\gg k|\mathcal S|^{1/2}\asymp k^2$。∎

## 3. 对抗数值：能否找到让界变小的 $c$？

在环面模型上取 $a=b=1$，对 $c$ 的相位做梯度下降，目标是最小化 $\mathbb E|A|^2|C|/k^2$。每个 $k$ 做 3 次随机重启，用新样本评估。

| $k$ | $c=1$ | 随机符号 | 对抗最小值 |
|---|---|---|---|
| 12 | 0.994 | 0.637 | **0.531** |
| 24 | 0.973 | 0.622 | **0.577** |
| 48 | 1.006 | 0.621 | **0.619** |

**读法：**
- 对抗搜索压不到 0，最低约 $0.53k^2$。这与命题一致（证明给出的 $\kappa$ 远小于实测值）。
- 随机符号在环面上的值 $0.62$，与第十六阶段对真实 $t$ 求平均得到的 $0.621$–$0.638$ 吻合，这在数值上确认了 Kronecker 约化。

## 4. 适用范围（论文注 7.9）

- **只对 Bohr 均值证明。** 实际论证用的是有限 $T\approx x^{O(1)}$ 和光滑权，那时 Parseval 带误差项，这些变体还没有写出。
- **不覆盖保留相位的论证。** 例如 Parseval 恒等式本身，经由 Kloosterman 和或 Gauss 和的 Type II，以及在整数一侧做的 Cauchy–Schwarz 或分散法。按表 5，所有已知的 Type II 信息都来自这一侧。
- **粗糙支撑的情形：** $a,b$ 支撑在因子个数有界的 $x^\eta$-粗糙数上时，同样的证明应当成立，但反集中一步需要低次 Steinhaus 多项式的不变性原理，细节未核对。

## 5. 对路线图的意义

- 第十二到十六阶段的"相位而非大值"结论，现在有了一条定理作支撑：**在 Bohr 均值意义下，绝对值方法对孪生 Type II 无能为力。**
- 这和定理 A、定理 E 是同一种形式：给出一个方法类，证明它的极限。墙的描述现在是：

> 孪生奇偶 ⟸ 关于 $\sum a_mb_n\lambda(mn+2)$ 的**相位**信息，而且它不能来自任何绝对值估计（命题 7.8）。

- **判决：✓（定理，方法极限）。**

**下一步候选：**
- **(a)** 写出有限 $T$ 版本和粗糙支撑版本，让命题覆盖实际使用的 Harman 筛法式论证。
- **(b)** "相位抽卡"：只考虑能给 $\lambda(mn+2)$ 提供相位信息的结构。
- **(c)** 等 8/33 → 3/13 子课题会话的结果。
