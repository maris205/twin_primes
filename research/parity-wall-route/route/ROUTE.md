# TPC 通路 v2：素数 = 零熵筛骨架 × 正熵奇偶位（2026-10-26）

**目标：** 基于早期“素数符号动力学”的想法，搭一条**每一段都有明确身份**的通路。每段要么是已证定理，要么是标准猜想，要么是本文提出的、大概率正确的新猜想。

**不追求马上写论文。** 地图见 [tpc_route_v2.svg](tpc_route_v2.svg)。

---

## 0. 一句话

早期论文的直觉是“素数来自低维混沌”。这个直觉对了一半，但放错了位置：

- **筛骨架**（哪些数没被小素数筛掉）是零熵的确定性系统，也就是 profinite odometer $\hat{\mathbb Z}$。它已经被完全刻画，并且在 Pólya 归一化下精确给出 Hardy–Littlewood 主项。
- **混沌**只属于另一个维度：剩下的“粗糙数”是素数还是两个大素数之积，即**奇偶位** $\lambda(n)=(-1)^{\Omega(n)}$。Logistic 映射在 $u=2$ 时共轭于 Bernoulli 移位，正好是奇偶位的模型。

通路 = 骨架桥（GEH，标准猜想）+ 奇偶桥（一个新猜想），在 **Bombieri 渐近筛**这个枢纽汇合，通到 TPC。Bombieri 的结果告诉我们：在 GEH 下，奇偶桥是**唯一**剩下的缺口，而且它只有**一个**自由度。

---

## 1. 节点总表

| 节点 | 内容 | 状态 |
|---|---|---|
| **A 编码岛** | 早期论文的 $Q_k$（$S_p=RL^{p-1}$ 逐位 AND）就是 odometer 的有限层柱集；移动事件 $Z_n$ 在种子 0 处精确编码孪生对 | **已证**（main.pdf §8.1；Phase I） |
| **B 骨架岛** | Haar 质量、区间方差 $\le\frac56\lvert I\rvert+2$、Haar 几乎处处强大数律；**Pólya 截断 $c=e^{-\gamma}$ 下，Haar 均值 = HL 主项** | **已证**（Lemma 5.4′、Thm 5.2、Prop 5.3）。Prop 5.3 是经典结果（Mertens paradox） |
| **C 奇偶岛** | $\lambda$ 作为混沌位：Chowla 猜想 ⟺ $\lambda$ 是 Bernoulli(½,½) 的通有点 | 立足点均已证：Tao 2016（对数平均两点 Chowla）、Tao–Teräväinen（奇数阶）、Pilatte（两点的幂次节省）、MRT（几乎所有移位 $h$ 的平均 HL） |
| **S 分布桥** | **GEH**：Bombieri–Friedlander–Iwaniec 型广义 Elliott–Halberstam，水平 $1-\varepsilon$ | **标准猜想**，大概率正确。已有：BV（水平 ½）；Zhang、Polymath、Maynard 等对特殊权重超过 ½ |
| **⊕ 枢纽** | Bombieri 渐近筛：在 GEH 下，一切孪生型分布量只剩一个参数 $\delta_x\in[0,2]$；HL ⟺ $\delta_x\to1$；$\liminf\delta_x>0$ ⟹ TPC | **已知定理**（Bombieri 1976；Tao 2016 博客笔记） |
| **P 奇偶桥** | 新猜想族 PND / FCP / RB / LRC₂（§3）；编译器见 COMPILER.md | **新猜想**，数值支持（§4） |
| **D 终点** | 无穷多孪生素数（PND 即够）；HL 渐近（需 FCP） | — |
| 已关闭 | 旧 Bridge A（Gate A 就是终点的换写）；旧 Bridge B 的“种子典型性”（依赖截断选择）；Hénon 几何提升 | Phase I 及新颖性核查 |
| 支线 | Gate B 作为平均移位 HL 问题（对奇偶不敏感） | 可做，但不在主路上 |

---

## 2. 通路定理（编译器）

**Theorem R（Bombieri 型，已知）.** 假设 GEH。则存在 $\delta_x\in[0,2]$ 使得

$$\sum_{n\le x}\Lambda(n)\Lambda(n+2)=(\delta_x+o(1))\,2\Pi_2x,$$

并且对每个 $k\ge2$ 都有 $\sum_{n\le x}\Lambda_k(n)\Lambda(n+2)=(2\Pi_2+o(1))kx\log^{k-1}x$，即与 $\delta$ 无关。特别地，

$$\frac{\sum_{n\le x}\Lambda(n)\log n\,\Lambda(n+2)}{\sum_{n\le x}\Lambda_2(n)\Lambda(n+2)}=\frac{\delta_x}2+o(1).$$

因此：$\liminf\delta_x>0$ ⟹ TPC；$\delta_x\to1$ ⟺ HL。

> 来源：Tao, *Notes on the Bombieri asymptotic sieve*（2016）。投稿前须核对 Bombieri 原文的精确条件。

**读法：** 在 GEH 下，奇偶桥**不可能**比 TPC 更弱（这是奇偶原理）。但它可以被换成结构上更自然、并能连到 Chowla/Sarnak 生态的命题。这正是第 3 节新猜想的作用。

**一个容易漏掉的事实**（Tao 笔记）：即使同时假设 GRH、GUE、abc、Chowla，目前也只知道 $0\le\delta\le2$。所以奇偶桥需要**新的**假设，现有大猜想都不够。原因是 Chowla 型方法依赖小素数处的乘性，而“粗糙数”的限制恰好把它破坏了。

---

## 3. 奇偶桥上的新猜想（由弱到强）

记 $\Lambda_2=\mu*\log^2$。它支撑在至多两个不同素因子的数上：在素数上 $\lambda=-1$，在两大素数之积上 $\lambda=+1$。这就是“奇偶位”。

### PND（奇偶不退化，最弱，足以推出 TPC）

$$\liminf_{x\to\infty}\delta_x>0 .$$

含义：在 $n+2$ 为素数、$n$ 为 $P_{\le2}$ 的配对中，“$n$ 是素数”所占的 $\Lambda_2$ 加权份额不趋于 0。换句话说，奇偶位不会退化成常数 $+1$。

动力学说法：奇偶余循环沿孪生加权轨道不是渐近上边界。

### FCP（四花样公平硬币，⟺ HL，在 GEH 下）

令 $W_{\varepsilon_1\varepsilon_2}(x)=\sum_{n\le x}\Lambda_2(n)\Lambda_2(n+2)\mathbf 1[\lambda(n)=\varepsilon_1,\lambda(n+2)=\varepsilon_2]$。则

$$\frac{W_{\varepsilon_1\varepsilon_2}(x)}{\sum W}\longrightarrow\frac14\qquad(\varepsilon_i=\pm1).$$

由于在 $\Lambda_2$ 的支撑上（除素数幂外）$\log m\,\Lambda(m)=\Lambda_2(m)\frac{1-\lambda(m)}2$，有

$$\sum_{n\le x}\log n\,\Lambda(n)\log(n+2)\Lambda(n+2)=W_{--}(x)+O(x^{1/2+o(1)}).$$

FCP 加上 $\sum W\sim8\Pi_2x\log^2x$ 即给出 HL。后者已在 [COMPILER.md](COMPILER.md) 的 Thm C1 中证明（EH + GEH），并且 C2 表明单点奇偶项自动为 $o$，所以 FCP 实际上只需要两点项 $D_3$（C3）。注意恒等式须用无平方因子部分 $\Lambda_2^\flat=\mu^2\Lambda_2$。

### RB（相对 Bernoulli，机制猜想，最强）

在 $\Lambda_2\otimes\Lambda_2$ 加权的配对上，奇偶对 $(\lambda(n),\lambda(n+2))$ 与骨架信息渐近独立，并且是公平硬币对。骨架信息包括任意固定模 $W$ 下的剩余类，以及素因子尺度剖面 $(\log p_i/\log n)$。对任意可容许的 $k$ 元组，同样的陈述应当成立。

动力学说法：沿种子 0 的 $\Lambda_2$ 加权轨道，奇偶过程在 odometer 因子上**相对 Bernoulli**。

它是“Chowla 在骨架之上的相对版本”。它推出 FCP，并在 GEH 下推出所有 HL $k$ 元组。

### LRC₂（几乎素数对上的对数平均两点 Chowla，最有希望的攻击点）

> **更正：** 本节原先的 LRC 以 $\sum\mathbf 1_R(n)\mathbf 1_R(n+2)/n$ 归一化。在相对粗糙的定义下这个和**收敛**，陈述是退化的。另外，$\mu\mathbf 1_R$ 型的写法即使在没有奇偶问题时也不趋于 0。现改用下面不含歧义的形式，详见 [COMPILER.md](COMPILER.md) §0。

令 $\Lambda_2^\flat=\mu^2\Lambda_2$，$w(n)=1/(n\log n\log(n+2))$，

$$\rho(X)=\frac{1}{8\Pi_2\log X}\sum_{n\le X}\Lambda_2^\flat(n)\Lambda_2^\flat(n+2)\,\lambda(n)\lambda(n+2)\,w(n).$$

**LRC₂：** $\rho(X)\to0$。

- **已证的编译器**（COMPILER.md Thm C4，EH + GEH 下）：$\sum_{n\le X}\frac{\Lambda(n)\Lambda(n+2)}n=2\Pi_2\log X\,(1+\rho(X))+o(\log X)$。
  - 因此 LRC₂ ⟹ 对数平均 HL ⟹ TPC。
  - 更弱的 **PND$_{\log}$**：$\limsup\rho(X)>-1$，就已经 ⟹ TPC。也就是说，只要几乎素数对的奇偶不是近乎完全反相关即可。
- **为什么有希望：** 把权重 $\Lambda_2^\flat(n)\Lambda_2^\flat(n+2)/(\log n\log(n+2))$ 换成 1，它就是 Tao 2016 已证的 $\sum\lambda(n)\lambda(n+2)/n=o(\log X)$。
- **真正的新难点：** Tao 的熵递减用到小素数 $p$ 处的乘性 $\lambda(pn)=-\lambda(n)$，而几乎素数权重让小素数不再出现。需要找替代机制，候选包括中等素数的膨胀、骨架上的平均。**这就是整条路最值得投入的地方。**

**强弱关系：** RB ⟹ FCP ⟹ PND。在 EH + GEH 下：FCP ⟺ HL；LRC₂ ⟹ 对数平均 HL；PND 或 PND$_{\log}$ ⟹ TPC。

---

## 4. 数值证据

### FCP 四花样份额（[parity_patterns.json](parity_patterns.json)）

| $x$ | $\delta_x$ | 奇份额 $s_x$（→½） | (素,素) | (素,半) | (半,素) | (半,半) | (素素−半半)$\cdot\log x$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| $10^4$ | 1.0076 | 0.522 | 0.346 | 0.241 | 0.253 | 0.160 | 1.71 |
| $10^5$ | 0.9961 | 0.519 | 0.325 | 0.251 | 0.246 | 0.178 | 1.69 |
| $10^6$ | 0.9943 | 0.513 | 0.311 | 0.248 | 0.249 | 0.192 | 1.65 |
| $10^7$ | 1.0052 | 0.516 | 0.303 | 0.248 | 0.248 | 0.200 | 1.66 |

读法：

- 两个混合花样已经稳定在 0.248。
- (素,素) 与 (半,半) 的差约等于 $1.66/\log x$，是一个**二阶项**，趋于 0。这与 FCP 一致，并给出了一个可检验的二阶常数（约 1.66）。
- $\delta_x$ 在 1 附近 ±0.6% 内波动。

### 粗糙 Chowla（[rough_chowla.json](rough_chowla.json)，$\varepsilon=0.2$）

| $x$ | 粗糙对数 | $C_R$（Cesàro） | 噪声尺度 $1/\sqrt{\#}$ | $C_R$（对数平均，相对粗糙） |
|---|---:|---:|---:|---:|
| $10^5$ | 7,143 | −0.0118 | 0.0118 | −0.0597 |
| $10^6$ | 49,447 | −0.0015 | 0.0045 | −0.0555 |
| $10^7$ | 356,443 | +0.0027 | 0.0017 | −0.0527 |

读法：Cesàro 版在噪声水平内，与 0 一致。**最后一列已作废**：它的归一化是退化的（见 §3 的更正）。

### LRC₂ 的 $\rho(X)$（[check_compiler.json](check_compiler.json)）

| $X$ | $10^4$ | $10^5$ | $10^6$ | $10^7$ |
|---|---:|---:|---:|---:|
| $\rho(X)$ | −0.0199 | −0.0148 | −0.0100 | **−0.0065** |

$\rho(X)$ 单调趋向 0，支持 LRC₂。

---

## 5. 与早期论文的对应（哪些想法在新路里活下来了）

| 早期想法 | 在新路中的位置 |
|---|---|
| 论文 1：$Q_k$ = 周期序列 $RL^{p-1}$ 的 AND | 原样保留，即编码岛（odometer 柱集） |
| 论文 1：$\mu_{LRL}$ 柱集质量，以及手调常数 $k=2C_2/\mu_{LRL}\approx12.73$ | 柱集质量 = Haar 质量 $\alpha_n$。手调常数由 **Pólya 截断** $n^{e^{-\gamma}}$ 精确取代：Haar 均值自动等于 HL 主项，无需定标（$N=10^9$ 时比值为 1.0005） |
| 论文 2：(2,2) 禁止花样（模 3） | 由骨架的局部可容许性自动处理 |
| 论文 1、2：Logistic 混沌“生成”素数 | **角色更换**：混沌只描述奇偶位（$u=2$ 时 Logistic ≅ Bernoulli）。骨架是零熵的，两者不能混为一个映射。原论文的定标问题正源于把两层混在一起 |
| 论文 3：序列 Birkhoff 定理 | 正确的版本活在 odometer 上：Thm 5.2 的强大数律（已证） |
| 论文 4、5：零点谱 | 不在本路线上 |

---

## 6. 下一步（按“能把路修实”的优先级）

1. ~~写全两个“待写全”~~：**已完成**，见 [COMPILER.md](COMPILER.md)（Thm C1–C4）。剩余缺口有三处：Bombieri 原文的条件尚未核对（目前以 Tao 笔记 Theorem 1 为黑盒），两线性形式上界筛的出处待补，GEH 盒分解需写成完整引理。
2. **加强数值。**
   - 把 FCP 份额推到 $10^9$（需分段筛），拟合二阶常数 1.66 并给出理论解释（来自 $\sum\Lambda*\Lambda$ 与 $\sum\Lambda\log$ 的二阶项差）；
   - 检验 RB：按 $n\bmod W$、按素因子尺度剖面分组后，四花样是否仍是 ¼；
   - 把 LRC₂ 的 ρ(X) 推到更大的 X，并对其 1/log 型漂移建模。
3. **攻 LRC₂**：见 [ATTACK_LRC2.md](ATTACK_LRC2.md) 与 [AMPLIFICATION.md](AMPLIFICATION.md)。小膨胀（Tao/HR/Pilatte 原样照搬）会被平方根壁垒挡住。改用大膨胀（素因子 $\ge x^\eta$）后，信号在一维奇偶模型下是相干的，瓶颈转移为一份可逐项证伪的账本 LDPT（L1–L7）：其中 L1（两边一维模型）已在 [L1_TEST.md](L1_TEST.md) 中由 GEH 推出，成为条件引理；L4 已在 [L4_TEST.md](L4_TEST.md) 中被证伪：两边粗糙的膨胀图平均度趋于 0（**稀疏度数壁垒**），所以 LDPT 失败；熵递减也已被尺度预算排除。结论：膨胀–谱方法的两条路（小膨胀导致信号稀释，大膨胀导致图稀疏）都被奇偶障碍堵住。若全部成立，则在 GEH 下 $ar\delta>0$ ⟹ TPC。这一结论过强，奇偶桥仍需一种不依赖膨胀图扩张的新输入。
4. **支线（可并行）：** Gate B 的平均移位问题，对照 MRT。

---

## 7. 诚实声明

- 在 GEH 下，奇偶桥必然与 TPC 同等强度（Bombieri；奇偶原理）。任何路线都绕不开这一点，本路线也不例外。
- 本路线的价值在于：
  - 把唯一的缺口压缩成**一个**自由度；
  - 给它一个动力学上自然的形式（相对 Bernoulli）；
  - 连到已有真实进展的 Chowla 生态（对数平均两点已证）；
  - 指出具体的新难点（粗糙数上没有小素数乘性）。
- PND、FCP、RB、LRC₂ 都是**猜想**，数值支持不等于证明。Theorem R 引自二手笔记，须核对原文。
