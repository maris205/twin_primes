# 攻 LRC₂：Tao 熵递减证明的解剖、断点与替代机制（2026-10-26）

目标：在 [COMPILER.md](COMPILER.md) 的 Thm C4 下，LRC₂（几乎素数对上的对数平均两点 Chowla）⟹ 对数平均 HL ⟹ TPC。本文分四步：

1. 逐行定位 Tao 2016 证明中“小素数乘性”的每一次使用；
2. 分析几乎素数权重在哪一步断开；
3. 设计替代机制；
4. 给出这类机制在定量上的**障碍**，以及仍然开着的方向。

原文均已直接阅读：Tao, arXiv:1509.05422（Forum Math. Pi 2016）；Pilatte, arXiv:2310.19357 v3（2026-08）。

---

## 0. 结论先行

1. **Tao 证明中乘性只用在三处**：
   - **M1**：命题 2.6 的膨胀恒等式 $g(pn)=g(p)g(n)$，取 $p\sim H$ 的中等素数；
   - **M2**：命题 2.4，即 Matomäki–Radziwiłł–Tao 的短区间指数和估计；
   - **M3**：§2 中归约到完全乘性、单位模的技术步骤。

   引理 2.5（对数平均带来的仿射不变性）和 §3（熵递减）**不用乘性**，只用对数平均和取值有限。Pilatte 的论文也写明，完全乘性只用在其命题 3.1 和主定理的归约中。
2. **几乎素数权重 $\Lambda_2^\flat/\log^2$ 在 M1 处直接断开**：$n$ 是几乎素数时，$pn$ 不是，所以 $f(pn)=0\ne\pm f(n)$。此外它是稀疏序列（密度约 $1/\log x$），而 Tao 定理 1.3 的误差是绝对的（$\varepsilon\log\omega$），对稀疏序列没有内容。
3. **替代设计**：改用“膨胀透明”的筛权 $g=\lambda\cdot\mathbf 1_{S_y}\cdot\theta$，其中 $S_y=\{n:\ n\text{ 在 }(y,x^\alpha)\text{ 内无素因子}\}$，$\theta$ 是小素数上的任意单位模扭曲。$g$ 是完全乘性的，并且在 $p\le y$ 的膨胀下封闭。对 $\theta$ 做 Haar 平均可以**精确地**分离出粗糙对的相关（引理 A）。于是 LRC 被归约为对 $S_y$ 支撑乘性函数的“相对精度”估计。
4. **定量障碍（平方根壁垒，仅对小膨胀；大膨胀见 AMPLIFICATION.md）**：设支撑在膨胀集 $D$ 下封闭，$V=\sum_{d\in D}1/d$。
   - 素数在支撑中的相对份额 $\lesssim1/V$，所以孪生信号 $\lesssim V^{-2}$；
   - Helfgott–Radziwiłł/Pilatte 一类谱方法的精度下限约为 $V^{-1/2}$（HR 称其“essentially best possible”）。

   因此**任何“膨胀 + 谱”型方法，无论怎样选择支撑与膨胀集，都看不到孪生奇偶**。数值验证：$S_y$ 中粗糙对的份额 $\approx0.4\prod_{2<p\le y}(1-2/p)\asymp V^{-2}$（§5）。
5. **要越过壁垒，必须有新成分**：信号放大，即在膨胀封闭的支撑上构造奇偶不平衡量 $\gg V^{-1/2}$ 的权重；或者完全不依赖膨胀的奇偶破坏输入（双线性型）。§6 列出可做的子问题。这一结论把“LRC₂ 是新难点”精确化为“需要一种绕过平方根壁垒的机制”。

---

## 1. Tao 2016 证明解剖（页码与公式号按 arXiv 版）

| 步 | 内容 | 是否用乘性 |
|---|---|---|
| §2.1–2.2 | 归约：$g_1,g_2$ 完全乘性、取值在单位圆上（命题 2.1、2.2，概率模型加上对 $h$ 的卷积） | **M3**（技术性） |
| (2.3) | 非伪装条件：$\sum_{p\le x}(1-\mathrm{Re}\,g_1(p)\bar\chi(p)p^{-it})/p\ge A$ | 条件本身 |
| 命题 2.4 | 对几乎所有 $n$，$\sup_\alpha\lvert\sum_{j\le H}g_1(n+j)e(\alpha j)\rvert=o(H)$，来自 MRT 的短区间结果 | **M2**（深度使用乘性） |
| 引理 2.5 | 对数平均下的近似仿射不变性：$\mathbb E[X(n)\mathbf 1_{n\equiv r(q)}]=\frac1q\mathbb E[X(qn+r)]+o(1)$，要求 $q\le H_+\ll A$ | **否**，只用对数权重 |
| **命题 2.6** | 由 $g(pn)=g(p)g(n)$ 得 $\mathbb E[g_1(n)g_2(n+h)]=c_p\,p\,\mathbb E[\mathbf 1_{p\mid n}g_1(n)g_2(n+ph)]$，再平移、对 $p\in\mathcal P_H$ 求和，得到 (2.11)：$\bigl\lvert\mathbb E\sum_{p\in\mathcal P_H}\sum_jc_p\mathbf 1_{p\mid n+j}g_1(n+j)g_2(n+j+ph)\bigr\rvert\gg\varepsilon H/\log H$ | **M1**（核心） |
| (2.17)–(2.18) | 写成 $\lvert\mathbb EF(X_H,Y_H)\rvert$，$X_H$ 为长 $H$ 的块，$Y_H=n\bmod P_H$ | 否 |
| §3 引理 3.2 | 熵递减：存在 $H\in[H_-,H_+]$ 使 $I(X_H;Y_H)\ll H/(\log H\log\log\log H)$ | **否**，只用平移不变性与有限取值 |
| §4 | Hoeffding 集中、圆法，再用命题 2.4 控制 $\sum_p\frac1p\sum_jg(n+j)g(n+j+ph)$ | 通过 M2 |

**精度**：按 Tao 文中脚注，最优化后的衰减约为 $(\log\log\log x/\log\log x)^{c}$；而 $A$ 对 $1/\varepsilon$ 的依赖约为三重指数。

**后续改进**（均属同一“膨胀 + 谱”机制）：
- Helfgott–Radziwiłł 2021：$\ll\log x/(\log\log x)^{1/2}$，把命题 2.6 之后的部分换成矩阵 $A$ 的特征值界 $(\sum_p1/p)^{1/2}$；
- Pilatte：$(\log x)^{1-c}$，膨胀改用 $J\approx\log\log H$ 个素数之积 $d$（素数在 $(H_0,H)$ 内，$H_0=\exp((\log H)^{1-\varepsilon_1})$），特征值界为 $(\sum_{d\in D}1/d)^{1/2+o(1)}$。

Pilatte 自述：“一个典型整数只有 $O(\log x)$ 个因子”，这限制了节省只能是 $\log$ 的小幂次。

---

## 2. 几乎素数权重在哪里断开

记 $f=\lambda\cdot\nu$，其中 $\nu=\Lambda_2^\flat/(\log n\log(n+2))$ 型权重，支撑在 $P_{\le2}$ 上。

| 断点 | 原因 | 能否修补 |
|---|---|---|
| **B1（M1）** | $n\in P_{\le2}$ 时 $pn\notin P_{\le2}$，所以 $f(pn)=0$，命题 2.6 的恒等式失效 | 不能就地修补，需要换权重（§3） |
| **B2（稀疏）** | 支撑密度约 $1/\log x$。块长 $H$ 有界时块几乎全为 0；定理 1.3 的界 $\varepsilon\log\omega$ 远大于几乎素数对的总质量（约 $\log\omega/\log^2x$），所以是空命题 | 需要“相对”版本，块长 $H\gtrsim\log x$ |
| **B3（M2）** | 需要稀疏序列在短区间上的 MR 型估计（带指数扭曲），且误差要相对于密度。对素数/几乎素数而言，这本身带有奇偶内容 | 只有部分已知（Matomäki–Teräväinen 关于几乎素数在几乎所有短区间中的结果） |
| B4 | $\Lambda_2^\flat$ 的剖面权重 $\log p\log q/\log^2n$ 不是乘性的 | 可修：对剖面做 Mellin 展开，写成乘性函数 $g_\tau(p)=-p^{i\tau}$ 的叠加；非伪装条件由小素数处取 0 自动满足 |

---

## 3. 替代设计：膨胀透明权重与 θ-傅里叶分离

令 $\alpha>0$ 固定，$y<x^\alpha$，$S_y=\{n:\ n\text{ 在 }(y,x^\alpha)\text{ 内无素因子}\}$。每个 $n\in S_y$ 唯一分解为 $n=s\cdot m$，其中 $s$ 是 $y$-光滑部分，$m$ 是 $x^\alpha$-粗糙部分。

对 $\theta\in\mathbb T^{\pi(y)}$（每个素数 $p\le y$ 上一个单位复数），定义完全乘性函数：

$$g_\theta(p)=\begin{cases}-\theta_p,&p\le y,\\0,&y<p<x^\alpha,\\-1,&p\ge x^\alpha.\end{cases}$$

于是 $g_\theta(n)=\theta(s)\,\lambda(n)\,\mathbf 1_{S_y}(n)$。

**性质：**

- (a) **膨胀透明**：对 $p\le y$，$S_y$ 在乘以 $p$ 下封闭，且 $g_\theta(pn)=-\theta_pg_\theta(n)$。因此命题 2.6 的恒等式成立。
- (b) **非伪装**：对 Haar 意义下几乎所有的 $\theta$ 成立（几乎每个 $\theta$ 都离任何 $\chi(p)p^{it}$ 很远），伪装的 $\theta$ 只占指数小的测度。

**Lemma A（精确分离）.** For independent Haar-random $\theta,\theta'$,

$$\mathbb E_{\theta,\theta'}\sum_{n\le X}\frac{g_\theta(n)\,\overline{g_{\theta'}(n+2)}}n=\sum_{n\le X}\frac{\lambda\mathbf 1_R(n)\,\lambda\mathbf 1_R(n+2)}n,\qquad R=\{x^\alpha\text{-rough}\}.$$

*Proof.* $\mathbb E_\theta\theta(s)=\mathbf 1_{s=1}$. $\square$

**归约**：若对几乎所有 $\theta,\theta'$，相对于 $S_y$ 的对数质量 $\mathcal M_y$ 有

$$\Bigl\lvert\sum\frac{g_\theta(n)\overline{g_{\theta'}(n+2)}}n-\text{(模型主项)}\Bigr\rvert\le\varepsilon\,\mathcal M_y,$$

则粗糙对的相关被确定到 $\varepsilon\,\mathcal M_y$ 的精度。另一方面，粗糙对的质量是 $\mathcal M_R\approx c(y)\,\mathcal M_y$，其中 $c(y)\approx0.4\prod_{2<p\le y}(1-2/p)\asymp1/\log^2y$（§5 数值）。所以**需要相对精度 $\varepsilon=o(c(y))=o(1/\log^2y)$**，并且只能使用 $\le y$ 的膨胀。

---

## 4. 平方根壁垒（方法层面的不可行性）

> **2026-10-26 更正：** 本节 (i) 的“信号只在无 $D$ 因子的元素上”只对**小膨胀**成立。对素因子 $\ge x^\eta$ 的大膨胀，在 GEH 的一维奇偶结构下信号是相干的（$K_w$ 等于全部质量），障碍转移到仿射代价与稀疏独立性步骤。详见 [AMPLIFICATION.md](AMPLIFICATION.md)。

**命题 B（启发式，待写成方法限制定理）.** Let $\mathcal S$ be a support closed under multiplication by every $d$ in a dilation set $D$, and let $V=\sum_{d\in D}1/d$.

- (i) **信号上界。** 在对数权重下，$\mathcal S$ 中“素数”（或任何没有 $D$ 中因子的元素）的相对份额 $\lesssim1/V$，因为每个 $m\in\mathcal S$ 都产生 $\{dm\}$ 这一族合数，其对数质量为 $V$ 倍。所以孪生对信号 $\lesssim V^{-2}$。
- (ii) **精度下界。** Tao/HR/Pilatte 的谱方法给出的界是 $(\sum_{d\in D}1/d)^{-1/2}=V^{-1/2}$。HR 证明了对应矩阵的最大特征值约为 $V^{1/2+o(1)}$，并称之为本质最优。
- (iii) 因此 $\text{信号}/\text{精度}\lesssim V^{-3/2}<1$：**膨胀 + 谱的方法无法分辨孪生奇偶**。

两种极端情形：

- 小膨胀：$D$ 为 $y$-光滑数，$V\approx e^\gamma\log y$。精度约 $(\log y)^{-1/2}$，信号约 $(\log y)^{-2}$。
- 大膨胀：$D$ 的素因子 $\ge x^\alpha$。仿射不变性要付出 $O(\log d/\log x)$，最优约为 $\alpha^{1/3}$；而粗糙数中素数对的份额约为 $\alpha^2$。

两种情形下信号都比精度低至少一个幂次。

> 这与 Tao 文中“these methods do not appear to have any bearing on twin prime-type sums”的说法一致，并把它定量化了。它不是关于孪生素数的定理，而是关于一类证明方法的限制。

---

## 5. 数值（$x\le10^7$，[rough_parity_model.py](rough_parity_model.py)）

**(a) Mertens 壁垒。** $\alpha=0.3$。$S_y$ 加权的对数质量中，粗糙对所占份额：

| $y$ | 3 | 5 | 7 | 13 | 19 | 29 | 37 | 47 | 61 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 粗糙对份额 | 0.145 | 0.077 | 0.054 | 0.038 | 0.031 | 0.027 | 0.024 | 0.022 | 0.020 |
| 份额 $/\prod_{2<p\le y}(1-2/p)$ | 0.43 | 0.39 | 0.38 | 0.39 | 0.40 | 0.41 | 0.41 | 0.42 | 0.43 |

比值稳定在 0.38–0.43，与 $c(y)\asymp\prod(1-2/p)\asymp V^{-2}$ 一致。

**(b) 粗糙 Chowla 的中性主项（Möbius 版 Buchstab 函数）。** $(um(u))'=-m(u-1)$，$um(u)=-1$（$1<u\le2$）。

- 该函数**没有零点**：$um(u)$ 从 −1 单调升向 0，并超指数衰减（$u=5$ 时为 $-0.005$）。
- 所以 $\sum_{n\le x}\mu\mathbf 1_R(n)\sim M(\alpha)\,x/\log x$，其中 $M(\alpha)=um(u)\ne0$。
- 数值上，粗糙两点相关 $C_R\approx(\text{μ 在粗糙数上的均值}/\text{粗糙密度})^2$：

| $\alpha$ | $C_R$（数值） | （μ 均值/粗糙密度）² | 渐近 $(M/W)^2$ |
|---|---:|---:|---:|
| 0.45 | 0.687 | 0.645 | 0.443 |
| 0.40 | 0.337 | 0.300 | 0.179 |
| 0.35 | 0.139 | — | 0.055 |
| 0.25 | 0.0070 | 0.0034 | 0.0005 |

读法：

- $\lambda\mathbf 1_R(n)$ 与 $\lambda\mathbf 1_R(n+2)$ 表现为“均值非零的独立变量”，这与公平硬币（RB）图景一致。
- 有限 $x$ 的均值与渐近值仍有明显差距（$1/\log x$ 型二阶项）。
- 这也说明 Tao 笔记中“$\sum\mu\mathbf 1_R\mu\mathbf 1_R=o(x/\log^2x)$”应理解为：减去中性主项 $(M/W)^2$ 之后，或者在 $\alpha$ 很小时（中性项超指数小）。

---

## 6. 仍然开着的方向（按可行性排序）

1. **把命题 B 写成严格的“方法限制”定理。**
   - 内容：对任意膨胀封闭的支撑，构造使 HR/Pilatte 型矩阵达到 $V^{1/2}$ 量级特征值的检验向量，并给出 (i) 的精确信号上界。
   - 价值：一个干净的负结果，可并入 III-A 论文的“方法障碍”章节。
   - 难度：中。
2. **粗糙版编译器。** 仿照 C1–C4，用 $\mathbf 1_R$（或光滑筛权）代替 $\Lambda_2^\flat$，在 GEH 下写出：
$$\text{粗糙相关}=N(\alpha)+(1-\bar\delta)K(\alpha),$$
   并算出 $K(\alpha)$。这能精确告诉我们信号系数 $K$ 随 $\alpha$ 或 $y$ 的衰减，从而把命题 B(i) 的“$\lesssim$”变成等式。难度：中（与 C1–C4 同类）。
3. **信号放大（真正的新想法所在）。** 寻找三元组 $(\mathcal S,D,w)$，满足：
   - $\mathcal S$ 在 $D$ 下封闭；
   - $V$ 大；
   - 权重 $w$ 的奇偶不平衡（在 GEH 下与 $\delta$ 成比例的系数）$K_w\gg V^{-1/2}$。

   命题 B 的论证依赖“信号只在无 $D$ 因子的元素上”。若 GEH 的一维性使 $\delta$ 也出现在 $r$ 个因子的奇偶模式上（Bombieri：$r$ 为奇数时贡献 $\delta$，为偶数时贡献 $2-\delta$），那么信号可能分布在整个 $\mathcal S$ 上，而不只在素数上。此时关键量是 $\sum_r(-1)^rw_r$ 型的不平衡。对 $\lambda$ 本身，它就是 Möbius 版 Buchstab 量，超指数地小。**能否设计出加权使该不平衡为常数阶、同时保持膨胀封闭**，是一个明确、可数值探索的问题，也是本路线现在唯一的突破口。
4. **不经膨胀的奇偶破坏。** Friedlander–Iwaniec（$a^2+b^4$）与 Heath-Brown（$x^3+2y^3$）依赖目标序列自身的双线性结构。$\{n(n+2)\}$ 没有这样的结构是公认难点。可以检索是否存在“混合”方案，例如 $p+2=$ 范型或二元型的值。低优先级。
5. **例外特征二分（备注）。** Heath-Brown 1983：若存在 Siegel 零点，则孪生素数无穷多。这不构成通路，但说明“λ 伪装成实特征”的世界已经被排除在障碍之外。

---

## 7. 对整体通路的影响

- 通路的形状不变：GEH + 奇偶桥 ⟹ TPC。但奇偶桥的攻法要更新：**直接改造 Tao/HR/Pilatte 的“膨胀 + 谱”方法被平方根壁垒挡住**。LRC₂ 仍然是正确的目标陈述，数值上 $\rho\to0$ 也在支持它，只是证明需要“信号放大”一类的新机制（§6.3）。
- 早期符号动力学想法在这里有一个对应：膨胀封闭的支撑，就是 odometer 上在“乘以小素数”这一半群作用下不变的集合。命题 B 说明，**乘法半群作用的不变性与素数（作用的“不可约元”）的稀有性是互相制约的**。这是素数版的“生成元稀疏性”，可能是理解奇偶障碍的一个动力学视角。

## 8. 未完成

- 命题 B 目前是启发式论证，需要写成严格的方法限制定理（§6.1）。
- 粗糙版编译器尚未写出（§6.2）。
- Helfgott–Radziwiłł 原文未直接阅读，其“本质最优”的说法引自 Pilatte 的介绍。
- §5(b) 中 $\alpha=0.35$ 行缺少数值均值（脚本未输出），待补。
