# 方向 ③：寻找新的对称性——候选筛查（2026-10-27）

脚本与数据：
- [pellet_check.py](pellet_check.py)
- [pellet_check_q3_d7.json](pellet_check_q3_d7.json)
- [pellet_check_q5_d5.json](pellet_check_q5_d5.json)

## 0. 结论

- **筛了 9 类候选机制。只有一个通过判据，而且它只存在于函数域中：** Pellet 公式 $\mu(f)=(-1)^{\deg f}\chi(\operatorname{disc}f)$。这正是 Sawin–Shusterman（Annals 2022）在 $\mathbb F_q[T]$ 上证明孪生素数定理所用的"Möbius 在特殊子空间上像 Dirichlet 特征"的根源。我们在 $\mathbb F_3$（次数 $\le7$）和 $\mathbb F_5$（次数 $\le5$）上对**所有**无平方因子的首一多项式验证了它，包括"粗糙"的多项式（最小不可约因子次数为 3、4、5、6、7）。它对粗糙度完全不敏感，因为它不提取任何小素因子。
- **整数上缺少的东西可以说得很具体。** Pellet 公式把奇偶性拆成两个"有结构"的因子：
  - 一个**整数值、可加的分级** $\deg$，满足 $\deg(fg)=\deg f+\deg g$；
  - 一个**代数不变量上的二次特征** $\chi(\operatorname{disc}f)$。在互素的情形下它是乘性的，而且在不可约元上的取值只依赖于次数：$\chi(\operatorname{disc}P)=(-1)^{\deg P-1}$。
  
  在 $\mathbb Z$ 上，"大小"由 $\log n$ 度量，而 $\log n$ 不是整数值，所以不存在乘性兼容的 $\pm1$ 分级函数 $n\mapsto(-1)^{\deg n}$。于是没有 Pellet 公式的类比。这就是方向 ③ 的**精确靶子**：在 $\mathbb Z$ 上为粗糙数找到"分级 × 代数特征"型的奇偶表示，或者找到能替代它的结构。
- **方向 ③ 的状态：候选筛查完成。** 没有找到可以在整数上执行的新机制。唯一的正面例子在函数域，而它依赖的结构在整数上缺失。这一步在已知数学的范围内到头了，后续属于长期的、开放的研究问题。

---

## 1. 判据

一个候选机制必须同时满足：
- **(C1) 作用于粗糙数。** 在 $x^\eta$-粗糙、至多 $1/\eta$ 个素因子的整数上起作用，**不依赖提取小素因子**（论文 v0.6 §6.3，注记 6.14）。
- **(C2) 奇偶敏感。** 能区分真素数与 Selberg 奇偶赝品，后者与真素数共享全部筛法信息（Type I）。
- **(C3) 不被已知障碍挡住。** 不被已证的方法限制或已知障碍（奇偶原理、$\sqrt x$ 障碍、定理 A）覆盖。

## 2. 候选筛查

| # | 候选 | (C1) 粗糙数 | (C2) 奇偶敏感 | (C3) 已知障碍 | 结论 |
|---|---|---|---|---|---|
| 1 | **大素数膨胀**：$\lambda(pm)=-\lambda(m)$，$p\ge x^\eta$（粗糙数在其下封闭） | ✓ | ✓ | **定理 A（严格）**：粗糙膨胀子的分辨率 $\gg\eta^2\kappa^{-1}\log x$；L4 数值显示诱导图平均度 $\to0$ | ✗ |
| 2 | **在移位变量上提取少数大素数**（LWW 的 $K\le1/\eta$ 版本） | ✓ | ✓ | 被提取的乘积 $a\ge x^{K\eta}$ 成为模数，问题变成模 $x^{1-\eta}$ 量级、任意系数的级数分布，即 **$\sqrt x$ 障碍**；LWW 的矩方法需要 $K$ 很大 | ✗ |
| 3 | **高阶 Fourier / Gowers 范数**（Green–Tao；Green–Sawhney 的 Type II） | ✓ | 部分 | 孪生 $(n,n+2)$ 是**无穷复杂度**的模式（单变量的两个线性型）；Green–Sawhney 需要二维格结构 | ✗ |
| 4 | **自守 / 谱方法**（Kuznetsov，移位卷积和） | ✓ | ✗ | 这类方法能处理 $\sum\lambda_f(n)\lambda_f(n+2)$，因为 $\lambda_f$ 是自守系数；而 $\lambda$ 不是自守的，按"Möbius 随机性"它与一切自守对象正交，无法转移 | ✗ |
| 5 | **数域 spin 符号**（Friedlander–Iwaniec 的 $X^2+Y^4$，Heath-Brown 的 $x^3+2y^3$） | ✓ | ✓ | 孪生对应分裂代数 $\mathbb Q\times\mathbb Q$（$k(k+2)=(k+1)^2-1$），没有非平凡的 spin / Jacobi–Kubota 符号 | ✗ |
| 6 | **假装论 / 例外特征**（Heath-Brown：Siegel 零点 ⟹ 孪生；Tao–Teräväinen） | ✓（例外特征在所有尺度上与 $\lambda$ 相关） | ✓ | **条件性**：只在 Siegel 零点存在时成立。无条件的二分法需要在"没有 Siegel 零点"的一侧约束 $\delta$，而 Tao 指出，即使假设 GRH、GUE、abc 和 Chowla，也没有已知的界 | 条件性 ✓，无条件 ✗ |
| 7 | **遍历论 / Furstenberg 系统**（Frantzikinakis–Host；对数 Sarnak） | ✗ | ✓ | 粗糙度 $z=x^\eta$ 随尺度变化，没有固定的极限系统；已知的结构定理同样依赖小素数处的乘性 | ✗ |
| 8 | **Ramanujan 和 / Fourier 展开、筛法换位（Chen switching）** | ✓ | ✗ | 只携带 Type I 信息，被 **Selberg 奇偶原理** 挡住；Chen 换位只给出 $P_2$ 的上下界 | ✗ |
| 9 | **函数域的 Pellet 公式**：$\mu(f)=(-1)^{\deg f}\chi(\operatorname{disc}f)$（Sawin–Shusterman，Carmon–Rudnick） | **✓**（实测：与最小因子次数无关） | **✓**（精确等式） | 在 $\mathbb F_q[T]$ 上**不被挡住**：Sawin–Shusterman 由此在 $q$ 很大时证明了孪生素数定理。**但在 $\mathbb Z$ 上没有类比** | **函数域 ✓；整数上缺失** |

## 3. 候选 9 的验证（[pellet_check.py](pellet_check.py)）

对每个无平方因子的首一多项式 $f$，按最小不可约因子的次数（"粗糙度"）分组，检验 $\mu(f)=(-1)^{\deg f}\bigl(\tfrac{\operatorname{disc}f}{q}\bigr)$。

| $q$ | 次数 | 最小因子次数 | 成立 / 总数 |
|---|---|---|---|
| 3 | 6 | 1 / 2 / 3 / 6 | 287/287，55/55，28/28，116/116 |
| 3 | 7 | 1 / 2 / 3 / 7 | 834/834，168/168，144/144，312/312 |
| 5 | 5 | 1 / 2 / 5 | 1476/1476，400/400，624/624 |

**全部成立。** 公式对"粗糙"多项式（例如次数 7、只有一个次数 7 的不可约因子）和"光滑"多项式一视同仁。它表达奇偶性**不需要任何小因子**。

## 4. 为什么 $\mathbb Z$ 上没有类比：缺少的是"可加的整数分级"

> **更正（2026-10-27 晚）：把缺失的东西说成"分级"不够准确。** 在粗糙整数上，素因子个数 $r$ 本来就由因子大小剖面 $(t_1,\dots,t_r)$ 决定，"分级"本身并不缺。真正缺的是下面这一点：在函数域中，取定次数 $d$ 后，$\mu$ 在整个次数-$d$ 族上**等于系数的一个多项式（判别式）的二次特征** $\chi(\operatorname{disc}f)$。正因为如此，Weil/Deligne 的特征和估计可以直接作用于 $\mu$；Sawin–Shusterman 的优势来自 $q$ 很大时这些估计足够强。整数没有"系数"，也没有这样的代数几何，所以 $\lambda$ 在 $[x,2x]$ 上不是任何"坐标的多项式的特征"。下文关于"分级"的说法应按这个意思理解。

Pellet 公式可以拆成两个有结构的因子：
$$\lambda(f)=\underbrace{(-1)^{\deg f}}_{\text{整数值、可加的分级}}\cdot\underbrace{\chi(\operatorname{disc}f)}_{\text{代数不变量上的二次特征}} .$$

- 由 $\operatorname{disc}(fg)=\operatorname{disc}f\cdot\operatorname{disc}g\cdot\operatorname{Res}(f,g)^2$，第二个因子在互素时是乘性的；在不可约元 $P$ 上，$\chi(\operatorname{disc}P)=(-1)^{\deg P-1}$，只依赖次数。它的来源是 Frobenius 作用在根上的置换的符号：置换的符号等于 $(-1)^{\deg f-r}$，而这个符号由 $\sqrt{\operatorname{disc}f}$ 是否被 Frobenius 固定来检测。
- **在 $\mathbb Z$ 上**，"大小"由 $\log n$ 度量，它不是整数值，所以没有乘性兼容的 $\pm1$ 分级函数。整数也没有"根"，因此没有 Frobenius 置换，也没有判别式。
- **方向 ③ 的靶子由此变得具体。** 要在整数上得到 Pellet 型的奇偶表示，至少要有下面两样之一：
  - **(T1)** 为整数（至少为粗糙整数）构造一个起"Frobenius 置换符号"作用的代数对象；
  - **(T2)** 证明某种"近似分级"已经足够。例如对至多 $1/\eta$ 个、都 $\ge x^\eta$ 的素因子，$\log p_i/\log x\in[\eta,1]$ 是有界的连续参数；Bombieri 的一维奇偶结构（定理 4.1）正是在这些参数的单纯形上说话。
  
  （以下是推测，不是结论。）(T2) 也许是值得写成具体问题的方向：在单纯形 $\Delta_r$ 上，有没有一个"连续版本的 Pellet 分解"，把 $(-1)^r$ 写成可由筛法与某个额外的代数输入共同确定的形式？目前我们没有具体的候选。

## 5. 状态与建议

- **方向 ③：候选筛查完成。** 已知数学中唯一的"不提取小素数的奇偶机制"是函数域的 Pellet / Frobenius 结构；整数上缺少对应的分级与代数对象。
- **整个第三阶段的结论**（①②③合起来）：
  - 已知的奇偶突破机制，都依赖"许多小素数处的乘性"，或者依赖整数所没有的代数结构（数域 spin、函数域 Frobenius）；
  - 孪生的奇偶参数恰好落在这两类资源都缺失的地方：$x^\eta$-粗糙的整数，而且是一维的线性型。
- **建议：**
  1. 把 §2 的表和 §4 的观察作为论文讨论部分的一段，把方向说清楚；
  2. 研究上暂停在这里，或者转向可以产出严格结果的子问题，例如把注记 6.12 升级为熵递减的严格限制定理；
  3. (T1)/(T2) 留作长期的开放问题。

**参考：**
- Sawin–Shusterman, *On the Chowla and twin primes conjectures over $\mathbb F_q[T]$*, Ann. Math. 196 (2022)，arXiv:1808.04001；
- Kowalski, Bourbaki Exp. 1193；
- Heath-Brown, *Prime twins and Siegel zeros* (1983)；
- Tao, *Notes on the Bombieri asymptotic sieve* (2016)。
