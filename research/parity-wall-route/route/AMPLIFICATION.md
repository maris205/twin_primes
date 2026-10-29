# 信号放大：小膨胀稀释、大膨胀相干，以及新的瓶颈（2026-10-26）

接续 [ATTACK_LRC2.md](ATTACK_LRC2.md) §6.3。数值脚本见 [amplification.py](amplification.py) / [amplification.json](amplification.json)。

## 0. 结论

1. **更正命题 B(i)。** “孪生信号只落在无膨胀因子的元素上”只对**小膨胀**（素因子 $\le y$）成立。
   - 小膨胀产生的合数 $s\cdot m$ 带有小素因子，它们的奇偶参数 $\delta_s$ 与孪生的 $\delta$ 在先验上无关，所以信号被稀释到 $\asymp1/\log^2y$。
   - **大膨胀**（素因子 $\ge x^\eta$）产生的合数仍在粗糙世界里。在 GEH 下 Bombieri 的一维奇偶结构（$r$ 为奇数时贡献 $\delta$，为偶数时贡献 $2-\delta$）对所有 $r$ 同时成立。因此对任何 $\lambda$-符号权重，奇偶系数 $K_w$ 等于**全部 $|w|$ 质量**：信号是**相干**的、常数阶的。
   - 换言之，**信号放大在粗糙世界中是自动的**，不需要再寻找特殊权重。
2. **数值与相干模型一致。**
   - 粗糙对 $(n,n+2)$ 的 $(\Omega,\Omega')$ 联合分布在 $\eta=0.25$ 时与乘积形式的偏差 $\le2\%$。
   - 奇偶耦合 $\mathbb E[\lambda\lambda]-\mathbb E[\lambda]^2$ 在噪声以内，即约 $\pm0.003$。
   - 在相干模型下，这相当于 $\lvert\delta-1\rvert\lesssim0.3\%$，与直接测得的 $\delta_x\approx1.005$ 相符。
3. **瓶颈转移。** 改用大膨胀 $p\sim x^{\eta}$ 后，Tao 链条的各个环节变为：

   | 环节 | 代价 |
   |---|---|
   | 仿射不变性 | $O(\eta)$，有常数代价 |
   | 主弧输入 | 需要素数在几乎所有长 $x^{\eta}$ 的区间中的渐近计数，Huxley 型结果给出 $\eta>1/6$ |
   | 独立性步骤（关键） | 熵递减在稀疏支撑上的尺度预算**失败**：需要约 $\exp((\log x)^3)$ 的尺度范围，而可用的只有 $x^{\eta}$。只剩 HR/Pilatte 的谱方法这条路未定 |

4. **候选方案 LDPT（大膨胀奇偶转移）** 的账本见 §4。
   - 若各环节都成立，会得到 $\lvert\bar\delta-1\rvert\le C(\eta+L^{-1/2})$。只要右边 $<1$，就有 $\bar\delta>0$，于是在 GEH 下推出 TPC。
   - **这会是“GEH ⟹ TPC”级别的结论，可信度应当打折：** 最可能的漏洞在独立性步骤（§3.3），以及两边一维模型的推导（§1）。
   - 本文把方案写成一个可逐项证伪的账本，而不是一个结论。

---

## 1. 一维奇偶模型与奇偶系数

**Hypothesis 1D**（Tao 2016 笔记中“on GEH the parity obstruction is one-dimensional”的两边形式，**待推导**）.
Among $x^\eta$-rough pairs $(n,n+2)$ with $\Omega(n)=r$, $\Omega(n+2)=r'$ (with smooth profile weights), the mass is

$$m(r,r')=I_rI_{r'}\bigl(1+(\delta-1)(-1)^{r+r'}\bigr),$$

where the $I_r$ are the model (HL) masses.

当 $r'=1$（即 $n+2$ 为素数）时，这正是 Bombieri 的单边结果：奇数 $r$ 得到 $\delta$，偶数 $r$ 得到 $2-\delta$。一般的 $r'$ 是其对称延伸。

**推论（相干性）.** For $\lambda$-signed weights $w=\lambda\cdot|w|$ and $w'=\lambda\cdot|w'|$,

$$\sum w(n)w'(n+2)=\Bigl(\sum_r(-1)^rW_r\Bigr)\Bigl(\sum_{r'}(-1)^{r'}W'_{r'}\Bigr)+(\delta-1)\,\lVert w\rVert\,\lVert w'\rVert ,$$

where $\lVert w\rVert=\sum_r|W_r|$ is the full mass.

- 第一项是中性项，即 Möbius 版 Buchstab 量的平方。$\eta$ 小时它超指数地小。
- 第二项的系数 $K_w=\lVert w\rVert\lVert w'\rVert$ **是全部质量**。

**小膨胀 vs 大膨胀：**

| 膨胀集 $D$ | 合数 $d\cdot m$ 落在哪里 | 奇偶参数 | $K_w/\text{质量}$ |
|---|---|---|---|
| $y$-光滑数（小） | 带小因子 $s$ 的“新图样” | $\delta_s$，与 $\delta$ 无先验关系（除非假设“奇偶刚性”） | 粗糙对份额 $\approx0.4\prod_{2<p\le y}(1-2/p)\to0$（ATTACK §5 实测） |
| 素因子 $\ge x^\eta$（大） | 仍在粗糙世界 | 同一个 $\delta$（1D） | **1**（相干） |

---

## 2. 数值（$x=10^7$，$n\in(x/2,x]$ 的粗糙对）

| $\eta$ | $x^\eta$ | 粗糙对数 | 检验格子数 | 最大偏差 $\lvert m/(\text{row}\cdot\text{col}/\text{tot})-1\rvert$ | $\mathbb E[\lambda\lambda]$ | $\mathbb E[\lambda]^2$ | 噪声 $1/\sqrt{\#}$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0.12 | 6.9 | 499,999 | 30 | 0.54 | −0.0003 | 0.000002 | 0.0014 |
| 0.15 | 11.2 | 292,207 | 22 | 0.39 | +0.0012 | 0.00001 | 0.0018 |
| 0.20 | 25.1 | 178,213 | 15 | 0.21 | +0.0013 | 0.00015 | 0.0024 |
| 0.25 | 56.2 | 122,701 | 9 | **0.02** | +0.0033 | 0.0016 | 0.0029 |

读法：

- $\eta$ 小时偏离乘积形式，来源于刚好大于 $x^\eta$ 的素数造成的局部相关（例如 7 不能同时整除 $n$ 与 $n+2$）。这类偏差是**奇偶中性**的：它改变的是 $I_{r,r'}$，而不是 $(-1)^{r+r'}$ 的耦合。
- 真正的奇偶检验是 $\mathbb E[\lambda\lambda]\approx\mathbb E[\lambda]^2$。四行都在噪声之内。

**移位平均**（$h=2p$，$p$ 为 $(x^\eta,\min(x^{2\eta},199)]$ 内的素数）：

| $\eta$ | $C(2)$ | $\mathrm{mean}_pC(2p)$ | $\mathrm{sd}_p$ | 素数个数 |
|---|---:|---:|---:|---:|
| 0.15 | +0.0012 | −0.0006 | 0.0015 | 25 |
| 0.20 | +0.0013 | −0.0002 | 0.0023 | 37 |
| 0.25 | +0.0033 | +0.0016 | 0.0031 | 30 |

$C(2)$ 与移位平均在噪声内一致，这正是 Tao 型“移位 2 ⟷ 平均移位 $2p$”转移所需要的。

---

## 3. 用大膨胀重跑 Tao 链条：逐环节代价

设 $g=\lambda\mathbf 1_{R_\eta}$。它在粗糙数上完全乘性，因此对每个 $x^\eta$-粗糙素数 $p$ 都有 $g(pn)=-g(n)$。取膨胀素数 $p\in[x^{\eta_1},x^{\eta_2}]$，$\eta\le\eta_1$，$L=\sum1/p=\log(\eta_2/\eta_1)$。

### 3.1 膨胀恒等式（Tao 命题 2.6 的类比）——精确

若 $n=pm$，则 $g(n)g(n+2p)=g(m)g(m+2)$。所以 $p\cdot\mathbb E_X[\mathbf 1_{p\mid n}g(n)g(n+2p)]=\mathbb E_{X/p}[g(m)g(m+2)]$。这是恒等式，不需要任何假设。

### 3.2 仿射不变性（Tao 引理 2.5）——代价 $O(\eta_2)$

在 $[1,X]$ 上做对数平均时，$X/p$ 与 $X$ 两个窗口错开的对数比例为 $\log p/\log X\le\eta_2$，错开部分上的相关量绝对值 $\le1$（相对于粗糙对质量）。所以由此确定的 $\bar\delta$ 误差约为 $c_1\eta_2$，其中 $c_1\approx1$–$2$，待精确计算。

### 3.3 独立性步骤（Tao §3–4 / HR / Pilatte）——**关键，目前未通**

需要证明 $\mathbb E[p\mathbf 1_{p\mid n}g(n)g(n+2p)]\approx\mathbb E[g(n)g(n+2p)]$ 在对 $p$ 平均时成立。

**(a) 熵递减走不通（尺度预算计算）.**

- 稀疏支撑的密度 $\rho\asymp1/(\eta\log x)$，块熵率 $\le\rho\log(1/\rho)$。
- 信号大小约为 $\varepsilon\rho^2H/\log H$。即使用 Bernstein 型集中，所需互信息门槛也只有约 $\varepsilon^2\rho^3H/\log H$，所以每一步熵递减 $\gtrsim\varepsilon^2\rho^3/\log H$。
- 熵递减的不等式里还有一项 $H(Y_H)/(kH)\approx1/k$，它必须小于每步的递减量，于是 $k\gtrsim\log H/(\varepsilon^2\rho^3)\approx(\log x)^4$。
- 所需步数 $J\approx\rho\log(1/\rho)\log H/(\varepsilon^2\rho^3)\approx(\log x)^3$。
- 总的尺度增长为 $k^J\approx\exp\bigl((\log x)^3\log\log x\bigr)\gg x$，但可用的只有 $x^{\eta_2-\eta_1}$。**预算失败。**

  （稠密情形 $\rho\asymp1$ 时，所需增长只是常数的塔，这正是 Tao 能成功的原因。）

**(b) 谱方法（HR/Pilatte）是否可行：未定。** 它不需要熵递减，而是界定可除性图在稠密子集上的特征值。这里需要在**稀疏的粗糙数诱导子图**上做 high-trace 计数：

- 粗糙数在可除性边下是闭的（$n=pm$ 与 $n+p=p(m+1)$），度数约为 $L$；
- 闭途径的计数归结为沿途径的粗糙相关，这是筛法可计算的；
- 期望的特征值界为 $L^{1/2}$，对应精度 $L^{-1/2}$。

**这是整个方案唯一真正开放的数学问题。**

### 3.4 主弧输入（Tao 命题 2.4 / Pilatte 命题 3.1）——$\eta_2>1/6$ 时可用

圆法中，素数指数和 $\sum_{p\sim P}e(2p\alpha)/p$ 在次弧上有 $(\log)^{-A}$ 的节省（Vinogradov），这已足以压过稀疏密度 $\rho$。主弧上需要 $g$ 在几乎所有长度约 $x^{\eta_2}$ 的区间内、在小模算术级数上的均值。

- $r\ge2$ 的部分属于 Type II，可以处理；
- $r=1$ 的部分需要素数在几乎所有短区间中的**渐近**计数，Huxley 型零点密度给出 $\eta_2>1/6+\varepsilon$。

结果是：对 $p$ 平均的移位 $2p$ 相关等于中性值加上 $o(1)$。这是一个三元型、可用圆法处理的输入，本身**不依赖**奇偶。

### 3.5 汇总

若 3.3(b) 成立，则在 GEH 与 1D 模型下：

$$\lvert\bar\delta-1\rvert\le c_1\eta_2+c_2L^{-1/2}+o(1),\qquad \eta_2=\tfrac16+\varepsilon,\quad L\to\infty\ \text{（取 }\eta_1=\eta_2e^{-L}\text{）}.$$

右边 $\approx c_1/6$。若 $c_1<6$，则 $\bar\delta\ge1-c_1/6>0$，即 **PND$_{\log}$ 成立，在 GEH 下推出 TPC**。

---

## 4. LDPT 账本（逐项可证伪）

| # | 环节 | 状态 | 最可能的失败方式 |
|---|---|---|---|
| L1 | Hypothesis 1D（两边一维奇偶模型） | **条件引理**（GEH + Bombieri/Tao 定理），见 [L1_TEST.md](L1_TEST.md)；证伪失败，数值相容 | 已排除“第二参数”世界（W4） |
| L2 | 膨胀恒等式 | **已证**（精确） | — |
| L3 | 仿射代价 $c_1\eta_2$ | 易证，待算常数 | $c_1$ 偏大 |
| L4 | 稀疏诱导子图上的谱界 $L^{1/2}$ | **失败**（[L4_TEST.md](L4_TEST.md)）：两边粗糙的诱导图平均度 $ar dpprox2\kappa Lho	o0$，$\lambda/ar d$ 在 $x=10^8$ 时为 3.9–23.7，并随 $x$ 增大 | — |
| L5 | 主弧短区间输入（$\eta_2>1/6$） | 基本已知（Huxley；Type II） | 带指数扭曲、对几乎所有区间的版本需要核对文献 |
| L6 | 次弧 | 已知（Vinogradov） | — |
| L7 | 常数检查 $c_1\eta_2+c_2L^{-1/2}<1$ | 待算 | — |

**可信度提示（2026-10-27 更新：L1 成立；L4 已证伪，所以 LDPT 失败，“过强结论”的漏洞就在 L4）：** 若 L1–L7 全部成立，就得到 GEH ⟹ TPC。目前公认的状态是：即使在 GEH 加上 Chowla 等假设下，也只知道 $0\le\delta\le2$。所以这个方案很可能在 L1 或 L4 处失败；若失败，失败方式本身就是对奇偶障碍的一个新刻画。**下一步最有价值的是对 L1 和 L4 做最小反例搜索**，而不是先写证明。

---

## 5. 下一步

1. **L1 证伪测试。** 构造满足 GEH 型一切筛信息、但两边奇偶耦合不是“单参数相干”的人工序列（Selberg 型权重在两边独立翻转），检查它是否与 Bombieri 单边结果相容。若相容，1D 模型就不成立，相干性需要额外假设。
2. **L4 数值。** 在 $x\le10^8$ 上构造粗糙数诱导的可除性图（边：$n\sim n\pm p$，$p\mid n$，$p\in[x^{\eta_1},x^{\eta_2}]$），用 Lanczos 方法估计限制在粗糙支撑上的中心化算子的最大特征值，看它是否约为 $L^{1/2}$。这是可执行的实验。
3. **L3 / L7 常数。** 精确计算对数平均的端窗贡献。

## 6. 对路线文档的修订

- ATTACK_LRC2.md 的命题 B 改为“对小膨胀成立”，大膨胀的障碍以本文 §3 为准。
- 地图上奇偶桥的标签改为“LRC₂ → 大膨胀转移（待验 L1/L4）”。
