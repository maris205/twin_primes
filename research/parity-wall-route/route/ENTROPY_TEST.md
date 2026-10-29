# 熵递减证伪测试：孪生（稀疏粗糙）vs Chowla（稠密）（2026-10-27）

脚本 [entropy_test.py](entropy_test.py)。数据：
- [entropy_test_1e08_H8.json](entropy_test_1e08_H8.json) 与 [entropy_run_1e8.log](entropy_run_1e8.log)；
- 对照：[entropy_test_1e07_H8.json](entropy_test_1e07_H8.json)、[entropy_test_1e07_H6.json](entropy_test_1e07_H6.json)。

对应路线图第三阶段 ①，以及 [AMPLIFICATION.md](AMPLIFICATION.md) §3.3(a) 的启发式反对理由。

## 0. 结论

> **更新（同日，读完 Tao 2016 §3，见 §6）：** 下面第 1 条中"方差敏感版可能可行"的情形在 Tao 的迭代结构里不会出现。原因是每一步的递减量按 $1/\log H$ 衰减，使所需尺度关于"预算 ÷ 门槛"是双指数的。**结论：两种版本都走不通。熵递减按 Tao 的迭代只能处理 $z\le(\log x)^{o(1)}$，而孪生参数需要 $z=x^\eta$。路线图 ① 关闭。**

1. **没有证伪熵递减，但把它的处境量化清楚了。** 结果分成两半：
   - **Tao 原版**（Pinsker 不等式，按上确界范数控制）需要 $J\asymp H\log^3z$ 个"递减单位"。尺度预算是超多项式的，**走不通**。这确认了 AMPLIFICATION §3.3(a) 的启发式，并把那里猜测的指数换成了实测指数 3.08。
   - **方差敏感版**（χ² 或输运型，按信号的实际大小控制）只需要 $J\asymp\log z$。它是否走得通，取决于每一步熵递减消耗多少尺度：
     - 若每步只消耗一个二进素数带，所需范围是 $z^{O(1/\varepsilon^2)}$，属于多项式，对 PND（$\varepsilon$ 可以接近 1）**可能放得下**；
     - 若每步要把尺度乘上一个 $p\ge z$，所需范围是 $\exp(c\log^2z)$，**放不下**。
2. **真正的解耦在数值上是成立的。** 对 $p>z$，$\lvert\mathbb E[\Phi\mid p\mid n]-\mathbb E[\Phi]\rvert/\sigma$ 在两种设定下都落在采样噪声以内。所以障碍在"能否证明"，不在"是否为真"。
3. **结构性发现：$p<z$ 的小素数携带确定性信息。** 在孪生设定下，$I(X_H;n\bmod p)\approx0.3$–$0.8$ bit，因为 $n\bmod p$ 精确决定了窗口里哪些位置是粗糙的。所以熵递减只能使用 $p>z$ 的素数，而且窗口熵的大部分（约 75–80%）是粗糙掩码，不是奇偶符号。

**下一步的关键问题从"熵递减行不行"变成两个更具体的问题：**
- (Q1) 是否存在按方差（χ²）而不是按上确界控制的熵递减不等式；
- (Q2) Tao 迭代中每一步实际消耗多少尺度。

---

## 1. 测的是什么

Tao 在 2016 年证明对数 Chowla 时有一个关键步骤：在膨胀恒等式之后，需要把 $\mathbf 1_{p\mid n}$ 换成 $1/p$，也就是让
$$\mathbb E[\Phi\mid p\mid n]\approx\mathbb E[\Phi]$$
成立。熵递减通过互信息 $I(X_H;n\bmod p)$ 来证明这一点：若互信息大，则窗口熵在更大的尺度上下降；而熵总量有上界，所以只有有限多个尺度能让互信息大。

| 量 | 定义 |
|---|---|
| $h$ | Chowla：$\lambda$；孪生：$\lambda\cdot\mathbf 1[z\text{-粗糙}]$ |
| $X_H(n)$ | 窗口 $(h(n+1),\dots,h(n+H))$，$n\in(x/2,x]$ |
| $\Phi(n)$ | 窗口内移位 2 的相关的平均，$\frac1{H-2}\sum_jh(n+j)h(n+j+2)$ |
| $\sigma$ | 信号大小，$\mathbb E\lvert h(n)h(n+2)\rvert$（Chowla 为 1；孪生为粗糙对密度） |
| $H_{\rm sign}$ | $H(X_H)-H(\text{粗糙掩码})$，即奇偶符号的熵预算 |
| $\mathrm{KL}^*$ | 达到相对精度 $\varepsilon$ 所需的 KL 门槛：χ² 版 $\varepsilon^2\sigma^2/(2\operatorname{Var}\Phi)$，Pinsker 版 $\varepsilon^2\sigma^2/2$ |
| $J=H_{\rm sign}/\mathrm{KL}^*$ | 预算要支付的"递减单位"数 |

另外实测了：互信息 $I_p$（Miller–Madow 校正，并给出打乱标签后的偏差底线）、$\mathrm{KL}(P_{X\mid p\mid n}\Vert P_X)$，以及实际的解耦误差 $D_p$（附随机子集噪声底线）。

$\varepsilon=0.1$，$H=8$，$z\in\{5,7,13,23,53,101\}$，素数带 $[P,2P)$ 取 $P\in\{5,30,100,300\}$，每带 8 个素数。

## 2. 结果（$x=10^8$，$H=8$）

| 设定 | $H_{\rm sign}$ (bit) | $H_{\rm mask}$ | $\sigma$ | $J_{\chi^2}$ | 相对 Chowla | $J_{\rm Pinsker}$ | 相对 Chowla |
|---|---:|---:|---:|---:|---:|---:|---:|
| Chowla | 8.000 | 0 | 1 | 267 | 1 | 1,600 | 1 |
| 孪生 $z=5$ | 2.667 | 2.585 | 0.1667 | 533 | 2.0 | 19,200 | 12 |
| $z=7$ | 2.133 | 4.190 | 0.1000 | 711 | 2.7 | 42,667 | 27 |
| $z=13$ | 1.662 | 4.558 | 0.0584 | 948 | 3.6 | 97,343 | 61 |
| $z=23$ | 1.368 | 4.415 | 0.0390 | 1,168 | 4.4 | 179,538 | 112 |
| $z=53$ | 1.110 | 4.096 | 0.0255 | 1,450 | 5.4 | 341,162 | 213 |
| $z=101$ | 0.962 | 3.834 | 0.0191 | 1,675 | 6.3 | 524,857 | 328 |

**拟合：**
- $J_{\chi^2}\propto(\log z)^{1.06}$，斜率约为 $373\ln z$；
- $J_{\rm Pinsker}\propto(\log z)^{3.08}$。

**常数与理论吻合：**
- $\rho_1\log z\approx0.54$，接近 $e^{-\gamma}=0.56$（Mertens）；
- $\sigma\log^2z\approx0.40$，接近 $2\Pi_2e^{-2\gamma}=0.42$；
- $\operatorname{Var}\Phi\approx\sigma/(H-2)$。

由此得到闭式：
$$J_{\chi^2}\approx\frac{2}{\varepsilon^2}\frac{H}{H-2}\cdot\frac{\rho_1}{\sigma}\asymp\frac{\log z}{\varepsilon^2},\qquad J_{\rm Pinsker}\approx\frac{2H}{\varepsilon^2}\cdot\frac{\rho_1}{\sigma^2}\asymp\frac{H\log^3z}{\varepsilon^2}.$$

**稳定性：**
- $x=10^7$ 与 $10^8$ 的结果三位有效数字一致。
- $H=6$ 与 $H=8$ 的孪生/Chowla 比值相同：$\chi^2$ 版都是 6.2–6.3，Pinsker 版都是 326–328。
- Pinsker 版的绝对值随 $H$ 线性增长（$8/6$），与闭式一致。

**解耦误差 $D/\sigma$（$p>z$ 的带）：** 所有设定都在噪声底线以内（$10^{-3}$ 量级），没有观察到解耦失败。

**小素数信息（$p<z$）：**

| $z$ | $I_p$（$P=5$ 带） | $I_p$（$P=30$ 带） |
|---|---|---|
| $z\ge7$ | 0.80 / 0.64 / 0.47 / 0.35 / 0.30 bit | — |
| $z\ge53$ | — | 0.034–0.037 bit |

打乱标签后的偏差底线约为 $10^{-6}$。这些信息是确定性的（粗糙掩码），不是噪声。

## 3. 解读：尺度预算

Tao 的论证之所以能对固定的 $\varepsilon$ 成功，是因为在稠密情形下 $J$ 与 $x$ 无关，只消耗常数倍的尺度。在孪生情形下，$J$ 随 $z=x^\eta$ 增长：

| 不等式 | $J$ | 每步消耗一个二进带（$2^J$） | 每步乘以 $p\ge z$（$z^J$） |
|---|---|---|---|
| Pinsker（Tao 原版） | $\asymp H\log^3z$ | $\exp(cH\log^3z)$：超多项式，✗ | ✗ |
| χ²/方差敏感 | $\asymp\log z/\varepsilon^2$ | $z^{2.6/\varepsilon^2}=x^{2.6\eta/\varepsilon^2}$：多项式，取 $\eta$ 很小时**可能可行** | $\exp(c\log^2z/\varepsilon^2)$：✗ |

可用的素数范围是 $[z,x^\kappa]$。对 PND，只需要排除 $\rho=-1$，所以 $\varepsilon$ 可以取到 $1/2$ 左右。在最乐观的那一格里，条件是 $2.6\cdot4\cdot\eta\le\kappa$，即 $\eta\lesssim0.1\kappa$。

## 4. 注意事项

- **这是代理测量，不是 Tao 论证的逐行实现。** $J$ 是"总熵预算 ÷ 每步门槛"的会计，忽略了 Tao 迭代中的对数损失、窗口长度的增长以及 $\varepsilon$ 的选择。指数（1 与 3）比常数更可信。
- **方差敏感版的熵递减是假设的。** 互信息控制的是 KL；把 KL 转成 χ² 精度，需要对 $\Phi$ 的尾部有额外控制，或者需要输运型不等式。是否有这样的不等式能套进熵递减的框架，正是 Q1。
- **实测的 $I_p$（$p>z$）都在偏差底线附近，不能用来直接估计熵递减实际能拿到的递减量。** 能可靠估计的是预算一侧（$H_{\rm sign},\sigma,\operatorname{Var}\Phi$）。

## 5. 对路线的影响与下一步

- ~~路线图 ① 的状态改为"Tao 原版走不通；方差敏感版未排除"~~。Q2 已回答（§6），**方差敏感版在 Tao 的迭代框架内同样走不通**，① 关闭。
- ~~Q2~~：已完成，见 §6。
- ~~Q1~~：Q2 的结果不利，Q1 不再能单独打开缺口（§6.4）。

---

## 6. Q2 的答案：Tao 迭代每一步的尺度代价（读 Tao 2016 §2–3）

原文：Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Forum Math. Pi 4 (2016)，arXiv:1509.05422。读的是命题 2.6、(2.17)–(2.18)、§3 的 (3.8)–(3.12)、引理 3.2、3.3、3.5。

### 6.1 原文的结构

- **素数与窗口绑定。** 在窗口长度 $H$ 处使用的素数集是 $\mathcal P_H$，即区间 $[\varepsilon^2H/2,\varepsilon^2H]$ 内的素数；$Y_H=n\bmod\prod_{p\in\mathcal P_H}p$。素数的大小 $p\asymp\varepsilon^2H$ **随窗口一起变**，不是固定的一个二进带。
- **单步不等式 (3.12)：**
$$\frac{H(X_{kH})}{kH}\le\frac{H(X_H)}{H}-\frac{I(X_H,Y_H)}{H}+O\Bigl(\frac1k\Bigr).$$
- **门槛（引理 3.2）：** 要证明存在某个 $H$，使得 $I(X_H,Y_H)\le H/(\log H\log\log\log H)$，这大约就是 $|\mathcal P_H|$。理由是：随后的 Hoeffding 步（引理 3.5）把 $F=\sum_{p\in\mathcal P_H}F_p$ 当作 $|\mathcal P_H|\asymp\varepsilon^2H/\log H$ 个独立项之和，失败集大小为 $\exp(-\varepsilon^7H/\log H)$；引理 3.3 则要求互信息低于这个指数。
- **迭代：** $H_{j+1}=H_j\lfloor C_0\log H_j\log\log\log H_j\rfloor$。

**所以每一步的尺度代价是"乘以 $k\asymp\log H$"，既不是"一个二进带"，也不是"乘以 $p$"。** 更关键的是，**每一步可用的递减量是 $1/\log H_j$，随步数衰减**。Tao 因此只能依赖调和型级数 $\sum_j1/(j\log j\cdots)$ 的缓慢发散，步数 $J$ 是关于 $\varepsilon$ 的塔函数。但在 Chowla 情形，$J$ 与 $x$ 无关，所以论证成立。

### 6.2 孪生版本：门槛中出现 $\sigma$

孪生版本中，$F_p$ 的典型大小是 $\sigma/\varepsilon^2$，而不是 $1/\varepsilon^2$。信号 (2.11) 变为 $\varepsilon\sigma H/\log H$，所以 Hoeffding 步需要的偏差门槛是 $t\asymp\varepsilon\sigma H/\log H$：

| 集中不等式 | 失败集指数 | 所需门槛 $I(X_H,Y_H)/H\lesssim$ |
|---|---|---|
| Hoeffding（Tao 原版，按值域） | $\varepsilon^4\sigma^2H/\log H$ | $\varepsilon^4\sigma^2/\log H$ |
| Bernstein（方差敏感） | $\varepsilon^4\sigma H/\log H$ | $\varepsilon^4\sigma/\log H$ |

这与 §2 的数值吻合：Pinsker 版 $\propto\sigma^{-2}$，χ² 版 $\propto\sigma^{-1}$。

### 6.3 预算推导

把门槛写成 $\delta_H=c\varepsilon^4\sigma^a/\log H$，其中 $a=2$ 对应 Hoeffding，$a=1$ 对应 Bernstein。

- **熵预算。** 预算是符号熵率 $\rho_1$。粗糙掩码由 $n\bmod p$（$p<z$）决定，而 $p<z$ 的素数不在 $\mathcal P_H$ 中（$p\asymp\varepsilon^2H$），所以掩码熵率是一个不会被递减的底，见 §2 的 $H_{\rm mask}$。
- **每步的倍数。** 要让递减量压过 $O(1/k)$，需要 $k\asymp\log H/(\varepsilon^4\sigma^a)$。
- **步数。** 伸缩求和：$\sum_jc\varepsilon^4\sigma^a/\log H_j\le\rho_1$，其中 $\log H_j\approx j\log k$。左边约为 $c\varepsilon^4\sigma^a\log J/\log k$，要超过 $\rho_1$ 就需要
$$\log J\gtrsim\frac{\rho_1}{c\varepsilon^4\sigma^a}\log k ,\qquad\text{因此}\qquad\log H_J\approx J\log k\ge\exp\Bigl(\frac{\rho_1\log k}{c\varepsilon^4\sigma^a}\Bigr).$$
- **代入实测常数**（$\rho_1\approx0.56/\log z$，$\sigma\approx0.42/\log^2z$）：

| | $\rho_1/\sigma^a$ | $\log H_J\gtrsim$ |
|---|---|---|
| $a=2$（Tao 原版） | $\approx3.2\log^3z$ | $\exp(c\log^3z\cdot\log k/\varepsilon^4)$ |
| $a=1$（方差敏感） | $\approx1.35\log z$ | $z^{c\log k/\varepsilon^4}$，而且 $k\ge\log H\ge\log z$ |

- **可用尺度。** 需要 $z/\varepsilon^2\lesssim H_-\le H_J\le H_+\le x^{\kappa}$，即 $\log H_J\le\kappa\log x=(\kappa/\eta)\log z$。
- **结论。** 即使在 $a=1$ 时，左边也至少是 $z^{c\log\log z/\varepsilon^4}$，远大于 $(\kappa/\eta)\log z$。所以对固定的 $\eta$，**两种版本都走不通**。反过来解出熵递减（按 Tao 的迭代）能处理的最大粗糙度：
$$\log z\lesssim\varepsilon^4\,\frac{\log\log x}{\log\log\log x},\qquad\text{即}\qquad z\le(\log x)^{O(\varepsilon^4/\log\log\log x)} .$$
它比 $\log x$ 的任何正幂都小，而孪生参数需要 $z=x^\eta$。

### 6.4 结论

1. **Q2 的答案：** 每一步把窗口乘以 $k\asymp\log H/(\varepsilon^4\sigma^a)$，所用素数的大小与窗口成正比，而且每步的递减量按 $1/\log H$ 衰减。由于这种衰减，"预算 ÷ 门槛"的比值进入的是**指数**而不是线性项：所需尺度关于这个比值是双指数的。§0–§5 中"$J=$ 预算/门槛"的线性会计低估了困难；那里提出的"每步一个二进带、$z^{O(1/\varepsilon^2)}$ 可能放得下"的情形在 Tao 的框架里不会出现。
2. **方差敏感化（Q1）救不了。** 它把 $\rho_1/\sigma^2\sim\log^3z$ 降到 $\rho_1/\sigma\sim\log z$，但这个量仍在指数里，所以仍然是 $\exp(z^{c})$ 级别的尺度需求。
3. **能救的只有改变迭代结构：** 让每步的递减量不随 $\log H$ 衰减。这需要所用素数的个数不再与 $H/\log H$ 绑定，或者需要一个不按素数逐个集中的集中步骤。这已经不是 Tao 意义下的熵递减。
4. **对照：已知方法能处理的粗糙度。**
   - 对固定的 $z$，$\lambda\mathbf 1_{z\text{-粗糙}}$ 是有界的乘性函数，Tao 的 Elliott 型定理直接给出 $o(1)$；
   - 熵递减（本节）能处理到 $z\le(\log x)^{o(1)}$；
   - 谱方法（Pilatte 的 $(\log x)^{-c}$ 节省，对比信号 $\sigma\asymp1/\log^2z$）预期能处理到 $z\le\exp((\log x)^{c/2})$。这是启发式，尚未验证；
   - 定理 A 证明谱方法到不了 $z=x^\eta$；
   - Bombieri 的奇偶参数需要 $z=x^\eta$。

   **两个已知机制与目标之间都隔着从 $(\log x)^{o(1)}$ 或 $\exp((\log x)^c)$ 到 $x^\eta$ 的鸿沟。**

**状态：** 路线图 ① 关闭。可以考虑把 6.3 写成定理 A 的姊妹命题："Tao 的熵递减迭代对孪生型奇偶的分辨能力上限为 $z\le(\log x)^{o(1)}$"。这个命题针对的是一个具体的证明，而不是一个方法类，所以只能作为 remark 或 proposition，严格性弱于定理 A。
