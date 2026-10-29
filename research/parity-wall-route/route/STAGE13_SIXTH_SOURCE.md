# 第十三阶段：寻找"第六类奇偶来源"（2026-10-28）

**问题：** 第九阶段把已知的破奇偶机制按"奇偶信息从哪里来"分成五类，孪生素数不满足其中任何一类的前提。是否存在第六类？第六类如果存在，就是真正的突破方向。

**一句话答案：** 普查约 20 个已知的破奇偶结果之后，**没有找到无条件的第六类**。

找到了两类边缘机制：
- **⓪ 解析的第二因子**：伪孪生素数、Piatetski-Shapiro 素数。孪生的第二因子是算术的，所以不适用。
- **⑥ 伪装结构（Siegel 零点世界）**：只在 Siegel 零点存在时成立，方向上与普遍预期相反。

此外得到一个统一判据：**所有已知机制最终都把两点相关化为双线性和 $\sum a_mb_n\,c(mn)$，并要求 $c$ 本身有可利用的结构。** 对孪生来说 $c(n)=\Lambda(n+2)$，它的结构正是要证明的东西，所以是循环的。这与第九阶段的四变量方程是同一件事。

**状态标注：** 普查与分类是对文献的分析（AI 辅助），不保证穷尽；"⓪ 不适用于孪生""⑥ 依赖 Siegel 零点"两条依据的是已发表定理的前提。

---

## 1. 普查表

"类别"一栏指奇偶信息的来源，编号沿用第九阶段的五类，新增 ⓪ 和 ⑥。

| 结果 | 问题 | 奇偶信息从哪里来 | 类别 |
|---|---|---|---|
| Vinogradov 1937 | 三素数 | 第三个变量，加上 Type II 双线性和 | ③ |
| Green–Tao–Ziegler | 有限复杂度的线性方程组 | 至少两个自由变量；Gowers 范数控制 | ③ |
| Friedlander–Iwaniec 1998 | $a^2+b^4$ | 范数形式（Gauss 整数）带来的双线性结构 | ② |
| Heath-Brown 2001 | $x^3+2y^3$ | 三次域的范数形式 | ② |
| Heath-Brown–Li、Merikoski 等 | $a^2+p^4$ 等 | 同上，代数结构 | ② |
| Sawin–Shusterman | $\mathbb F_q[T]$ 上的孪生素数 | Frobenius 与导数（$q$ 大） | ② |
| Mikawa、MRT | 对 $h$ 平均的 Hardy–Littlewood | 对移位求平均，加圆法 | ④ |
| GPY、Maynard–Tao、Polymath8b | 有界间隙 | 析取（鸽笼原理） | ⑤ |
| Tao 2016、Tao–Teräväinen | 对数平均的 Chowla（奇数阶） | 小素数处的乘性，加熵递减 | ① |
| Helfgott–Radziwiłł、Pilatte | 对数 Chowla 的定量形式 | 小素数处的乘性，加膨胀图 | ① |
| Matomäki–Radziwiłł 2016 | 乘性函数在几乎所有短区间上的均值 | 小素数处的乘性（Ramaré 恒等式） | ① |
| OpenAI 2026（007、011） | 普通两点 Chowla、$\mu(p-1)=1$ | 小素数取符号（第七阶段已核对） | ① |
| Bourgain–Sarnak–Ziegler、Kátai | Sarnak 猜想的特例 | 两个小素数 $p,q$ 处的乘性 | ① |
| **Piatetski-Shapiro 1953** | $\lfloor n^c\rfloor$ 中的素数 | 第二个集合是**解析的**（光滑相位），化为 $\sum\Lambda(n)e(f(n))$，用 Vaughan 的 Type I/II | **⓪** |
| **Kontorovich（math/0507569）** | "伪孪生素数"：素数 $p=\lfloor\mathrm{iL}(n)\rfloor$ | 同上：$\sum\Lambda(p)e(h\,\mathrm{Li}(p))$ 加 Type I/II | **⓪** |
| **Heath-Brown 1983** | Siegel 零点 ⟹ 孪生素数 | $\lambda$ 伪装成例外实特征 $\chi$，两点相关化为周期函数 | **⑥（条件）** |
| **Tao–Teräväinen 2021、Matomäki–Merikoski 2023** | Siegel 零点 ⟹ Hardy–Littlewood–Chowla 混合形式 | 同上 | **⑥（条件）** |
| 一点 PNT（$\sum_{n\ \text{粗糙}}\lambda(n)=o(\cdot)$） | 粗糙数上的单点奇偶 | Euler 乘积和零点自由区域（全局解析信息） | ⓪ |

## 2. 两类新机制，以及为什么都帮不上孪生

### ⓪ 解析的第二因子（一点信息）
- **机制：** 第二个集合由光滑相位定义，例如 $\lfloor n^c\rfloor$、$\lfloor\mathrm{iL}(n)\rfloor$。展开成 Fourier 级数后，问题化为一个变量的素数指数和 $\sum\Lambda(n)e(f(n))$，其中 $f$ 光滑且非线性。这类和由 $\Lambda=\mu*\log$ 的 Type I/II 分解直接处理，奇偶信息来自 $\zeta$ 的 Euler 乘积，而这本来就是已知的一点信息。
- **为什么不适用于孪生：** 孪生的第二个集合 $\{n:\ n+2\text{ 是素数}\}$ 是算术集合，它的 Fourier 谱集中在**有理频率**上（主弧）。二元圆法在次弧上要求 $L^2$ 控制，而这恰好就是奇偶障碍本身。Kontorovich 本人也说明，这个定理是 Piatetski-Shapiro 方法的翻版，"伪"字的意思正是"第二个因子不是算术的"。
- **对应于本项目：** 粗糙数上的一点奇偶由 Buchstab 加 PNT 可以证明；我们的定理 C 说明，难点完全在两点相关。⓪ 正好落在墙的另一侧。

### ⑥ 伪装结构（Siegel 零点世界）
- **机制：** 如果存在 Siegel 零点 $\beta$（属于实特征 $\chi\bmod q$），那么在 $q^{O(1)}\le n\le q^{O(1)}$ 范围内，$\lambda(n)\approx\chi(n)$（$\lambda$ "伪装"成 $\chi$）。于是 $\lambda(n)\lambda(n+2)\approx\chi(n)\chi(n+2)$ 是周期函数，可以直接计算，结论是孪生素数以 Hardy–Littlewood 的渐近成立（Heath-Brown 1983）。
- **为什么不是突破：**
  1. 它是条件结果，而普遍预期 Siegel 零点不存在。
  2. 它与另一侧（没有 Siegel 零点、$\lambda$ 不伪装）构成一个二分法，而另一侧恰好就是 Chowla 问题。第八阶段的 H13 已经指出：排除 Siegel 零点反而关掉了这条路。
  3. 在本项目的语言里：⑥ 世界中 $\delta$ 被 $\chi$ 强行固定，这是定理 C 的"外部给定类参数"；无条件地，类参数仍然未知。
- **它为什么值得单列：** 它是唯一不依赖小素数、代数、额外变量、平均或析取的机制。它依赖的是 $\lambda$ 的**全局结构**，并且是唯一已知能真正处理固定 $h=2$ 的机制，尽管是在一个（大概）不存在的世界里。

## 3. 统一判据

把每一类机制都还原到最后一步，形式都是双线性和
$$\sum_{m\sim M}\sum_{n\sim N}a_m b_n\,c(mn),\qquad MN\approx x,\ M,N\ge x^{\eta},$$
区别只在于 $c$ 的结构从哪里来：

| 类别 | $c$ 的结构来源 |
|---|---|
| ① | $c$ 是乘性的，并在小素数处可以分解 |
| ② | $c(mn)$ 在代数整数环里分解（范数形式） |
| ③、④ | 对额外变量或移位求平均之后，$c$ 被 Fourier 化为可控的指数和 |
| ⑤ | 不需要 $c$，只需要析取 |
| ⓪ | $c=e(f)$，其中 $f$ 光滑 |
| ⑥ | $c\approx$ 周期函数（Siegel 零点） |

**孪生素数：** $c(n)=\lambda(n+2)$（粗糙版本），所以 $\sum a_mb_n\lambda(mn+2)$ 等价于计数 $p_1p_2+2=q_1q_2$（第九阶段），这正是要证的东西。**这就是"第六类不存在"的结构原因：要在二元固定移位问题上得到奇偶信息，$c$ 必须有结构，而孪生的 $c$ 就是待证对象。**

## 4. 剩下的真正候选（第六类可能的样子）

按上面的判据，一个新的第六类必须给"$\lambda(mn+2)$ 关于 $(m,n)$ 的双线性相关"提供结构信息，而且不能来自上面六种。我能想到的形式只有以下两个，都没有已知的实现：
1. **一个无条件的"部分伪装"定理：** $\lambda$ 在粗糙数上与某个结构对象（例如零点附近的特征或幂零序列）有不可忽略的相关性，强度足以固定 $\delta$。已知的 Matomäki–Radziwiłł–Tao 型结果说明 $\lambda$ 在平均意义下不伪装，方向相反。
2. **"$mn+2$"的代数化：** 找一个环，使得 $mn+2$ 在其中有乘性分解，对应于 ② 的新实例。第六阶段的 H9 已经证明在 $\mathbb Z$ 上走导数路线不行；而 $n(n+2)$ 对应的是分裂代数 $\mathbb Q\times\mathbb Q$，没有非平凡的范数结构。

**判决：◎（定位）。** 奇偶来源从五类补成 5+2 类（⓪、⑥），仍然没有一类适用于孪生。"第六类"的形状被刻画成：**给 $\lambda(mn+2)$ 的双线性形式提供结构**。这既是这个项目目前最准确的墙的描述，也是下一阶段唯一值得抽卡的方向。

## 5. 参考
- Kontorovich, *A pseudo-twin primes theorem*, arXiv:math/0507569.
- Heath-Brown, *Prime twins and Siegel zeros*, Proc. LMS 1983.
- Tao–Teräväinen, *The Hardy–Littlewood–Chowla conjecture in the presence of a Siegel zero*, arXiv:2109.06291.
- Matomäki–Merikoski, *Siegel zeros, twin primes, Goldbach's conjecture, and primes in short intervals*, arXiv:2112.11412.
- 第九阶段的五类表：[STAGE9_DETERMINANT.md](STAGE9_DETERMINANT.md)。
