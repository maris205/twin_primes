# 通道 ③ 4a：量化的推论 C′（2026-10-28）

**问题：** 量化定理 C 的误差项，写出量化的推论 C′。要推出"无穷多对孪生"，粗糙 $P_2$ 孪生需要多大的密度？

**状态标注：**
- 命题 Q 是严格的推导，**以 Bombieri 渐近筛的一个量化误差 $\varepsilon_B$ 为前提**；
- 关于 $\varepsilon_B$ 大小的讨论（§3）是分析；
- §4 是数值。

---

## 1. 定理 C 在哪里丢掉了量化

定理 C 的证明（论文 §4）中有三处 $o(1)$：
1. **Bombieri 定理本身**：误差 $\varepsilon_B(x)$，没有给出速率；
2. **Weierstrass 逼近**：要用多项式权逼近粗糙示性函数 $\mathbf 1[t_1\ge\eta]$（一个阶跃函数）。多项式的次数 $D$ 越高，组合系数越大，误差越多地被放大。按 Jackson 型速率，大约只能得到 $(\log\log x)^{-1/2}$；
3. **$\tau$ 截断与条件 (U)**。

第 2 处代价最大。**下面绕开它：** 不用粗糙示性函数，改用 Bombieri 自然带有的权
$$L=\Lambda\cdot\log\ (\text{素数，权 }\log^2p),\qquad K=\Lambda*\Lambda\ (\text{无平方因子的 }P_2=pq,\ \text{权 }2\log p\log q),$$
它们满足 $\Lambda_2=L+K$（再加上素数幂和非无平方因子项，这些项的量级是 $O(x\log x)$，见引理 3.2(b)）。这样就**只用 Bombieri 定理（$\vec k=(2)$）**，不用定理 4.1、Weierstrass 逼近或条件 (U)。

## 2. 命题 Q（严格，以 $\varepsilon_B$ 为前提）

**记号：** 在二进窗口 $n\in(x/2,x]$ 上记
$$S_{AB}=\sum_nA(n)B(n+2),\qquad A,B\in\{L,K\}.$$
对序列 $a\in\{L(\cdot+2),\ L(\cdot-2),\ K(\cdot+2)\}$，Bombieri 的主项为 $T_a=2\,G_a(1)\,C_a\,x\log x$（其中 $C_a$ 是质量，$G_a$ 是局部因子）。记 $T_0=T_{L(\cdot+2)}=T_{L(\cdot-2)}$，$T_0'=T_{K(\cdot+2)}$。

**假设 $\mathrm B(\varepsilon_B)$：** 对这三个序列，
$$\sum_na_n\Lambda_2(n)=T_a\bigl(1+O(\varepsilon_B(x))\bigr).$$
在 EH + GEH 下，这三个序列满足 Bombieri 定理的公理（$L$ 由 EH，$K$ 由 EH + GEH，论证同引理 3.3；$K$ 含小素因子的部分由 EH 处理）。所以 $\mathrm B(\varepsilon_B)$ 成立，并且 $\varepsilon_B=o(1)$。

**命题 Q.** 在 $\mathrm B(\varepsilon_B)$ 下，令 $\delta=S_{LL}/T_0$（加权的孪生参数），则
$$S_{KL}=(2-\delta)T_0+R_1,\qquad S_{LK}=(2-\delta)T_0+R_2,$$
$$S_{KK}=\delta\,T_0-2\,(T_0-T_0')+R_3,$$
其中 $|R_i|\ll(\varepsilon_B(x)+1/\log x)\,T_0$，并且 $T_0-T_0'$ 是**可显式计算**的主项差，大小为 $O(T_0/\log x)$。

**证明：**
- 由 $\Lambda_2=L+K+(\text{素数幂和非无平方因子项})$，引理 3.2(b) 给出 $\sum a_n\Lambda_2(n)=S_{L\cdot}+S_{K\cdot}+O(T_0/\log x)$。
- 对 $a=L(n+2)$ 用 Bombieri 定理：$S_{LL}+S_{KL}=2T_0(1+O(\varepsilon_B))$。
- 对反射序列 $a=L(n-2)$：$S_{LL}+S_{LK}=2T_0(1+O(\varepsilon_B))$。
- 对 $a=K(n+2)$：$S_{LK}+S_{KK}=2T_0'(1+O(\varepsilon_B))$。
- 解这个线性方程组即可。∎

（这其实是 Bombieri 渐近筛的奇偶结构，实质上很可能早已为人所知，参见 FI78 和 *Opera de Cribro* 第 16 章。这里的贡献是给出量化的记账，包括显式的主项修正 $T_0-T_0'$。）

**推论 Q′（量化的 C′）。** 若对某个 $x_j\to\infty$ 有
$$S_{KK}(x_j)\ >\ C\,\bigl(\varepsilon_B(x_j)+1/\log x_j\bigr)\,T_0(x_j)+2\,(T_0'-T_0)_+ ,$$
则 $S_{LL}(x_j)>0$，即 $(x_j/2,x_j]$ 中有一对孪生，从而孪生素数有无穷多对。

**换成计数：**
- 设 $N_\eta(2,2)$ 是窗口中 $m$ 与 $m+2$ 都是"两个 $\ge x^\eta$ 的素数之积"的个数。
- 每一对的 $KK$ 权至少是 $(2\eta(1-\eta))^2\log^4x$，而 $T_0\asymp2\Pi_2\,x\log^2x$。
- 所以只需
$$N_\eta(2,2)\ \ge\ C_\eta\,\bigl(\varepsilon_B(x)+1/\log x\bigr)\,\frac{x}{\log^2x}\qquad\text{对无穷多个 }x .$$

## 3. 需要多大的密度：答案取决于 $\varepsilon_B$（分析）

| 对 Bombieri 误差的假设 | 推论 Q′ 要求的粗糙 $P_2$ 孪生个数 | 与正比例（$\asymp x/\log^2x$）相比 |
|---|---|---|
| GEH 原样（每个固定 $\theta<1$），$\varepsilon_B=o(1)$ 没有速率 | $\ge c\cdot x/\log^2x$，$c>0$ 任意固定 | **没有改进**：仍然是正比例 |
| 量化 GEH：水平 $x^{1-\epsilon}$，误差 $\ll x\log^{-A}x$，并且对 $\epsilon$ 一致（预期 $\varepsilon_B\approx\epsilon$，待核对） | $\gg\epsilon(x)\cdot x/\log^2x$ | 改进一个因子 $\epsilon(x)$ |
| 最强的自然假设：水平 $x/(\log x)^B$，$\varepsilon_B\approx\log\log x/\log x$ | $\gg x\log\log x/\log^3x$ | 改进约 $\log x/\log\log x$ |
| **下限（结构性的）** | $\gg x/\log^3x$ | 不可能更好 |

**为什么有下限 $1/\log x$：** 在赝品世界 $\delta=0$ 中，$S_{LL}=0$。命题 Q 和 $S_{KK}\ge0$ 推出 $R_3\ge2(T_0-T_0')\asymp T_0/\log x$。所以任何满足筛法公理的论证，误差都不可能小于这个量级。也就是说，推论 Q′ 的门槛**不可能低于** $x/\log^3x$。这个门槛对这种方法是锐的：低于门槛的偶类下界与 $\delta=0$ 相容。

**关于 $\varepsilon_B$ 与水平的关系：** 上表第二、三行假定 Bombieri 渐近筛在水平 $x^\theta$ 下的相对误差是 $O(1-\theta)$ 加上 $\log^{-A}$。这是我们的预期，**尚未逐行核对** Bombieri 或 Friedlander–Iwaniec 的证明。核对它是把第二、三行变成定理的下一步。

## 4. 数值（[kk_identities.py](kk_identities.py)，窗口 $(X/2,X]$）

| $X$ | $S_{LL}/T_0$ | $S_{KL}/T_0$ | $S_{LK}/T_0$ | $S_{KK}/T_0$ | 不含奇偶的恒等式 $(S_{LL}+S_{KL})/(S_{LL}+S_{LK})$ |
|---|---|---|---|---|---|
| $10^6$ | 1.077 | 0.923 | 0.906 | 0.749 | 1.0086 |
| $10^7$ | 1.074 | 0.927 | 0.926 | 0.786 | 1.0003 |
| $10^8$ | 1.061 | 0.939 | 0.940 | 0.816 | 0.9995 |

（这里 $T_0:=(S_{LL}+S_{KL})/2$。）

**主项差 $T_0'/T_0$**（[kk_localfactors.json](kk_localfactors.json)；局部因子 $g(p)$ 由数据对 $p\le200$ 求得）：

| $X$ | $C_K/C_L$ | $G_K/G_L$ | 预测的 $T_0'/T_0$ | 实测 | $S_{LL}-S_{KK}$ | $2(1-T_0'/T_0)$ | 残差 $R/T_0$ |
|---|---|---|---|---|---|---|---|
| $10^6$ | 0.805 | 1.042 | 0.839 | 0.827 | 0.329 | 0.321 | 0.007 |
| $10^7$ | 0.833 | 1.040 | 0.866 | 0.856 | 0.288 | 0.268 | 0.019 |
| $10^8$ | 0.853 | 1.036 | 0.883 | 0.878 | 0.246 | 0.233 | 0.012 |

**解读：**
- 不含奇偶的恒等式（反射对称）在 $10^8$ 上精确到 0.05%。
- $S_{KK}$ 与 $S_{LL}$ 之差几乎完全由可计算的主项差 $2(T_0-T_0')$ 解释（$K$ 的质量更小，并且 $K$ 在小素数处的局部因子不同）。剩下的 $R/T_0\approx1\%$–$2\%$，就是这些高度上实际的 Bombieri 误差，量级约为 $0.2/\log x$。
- 真实世界中 $\delta\approx1$（$S_{LL}/T_0=1.06$，并且随 $x$ 增大趋向 1）。

## 5. 结论

1. **命题 Q 和推论 Q′（严格，以 Bombieri 的量化误差 $\varepsilon_B$ 为前提）：**
   $$S_{LL}=S_{KK}+2(T_0-T_0')+O\bigl((\varepsilon_B+1/\log x)T_0\bigr).$$
   只用 Bombieri 定理，避开了 Weierstrass 逼近。门槛就是 $\varepsilon_B$。
2. **需要多大的密度：**
   - 在 GEH 原样下，仍然要正比例（没有改进）；
   - 在量化 GEH 下，门槛降到 $\varepsilon_B\cdot x/\log^2x$；
   - 最好的情况，结构上不可能更低，是 $\asymp x/\log^3x$ 个粗糙 $P_2$ 孪生，比正比例弱 $\log x$ 倍。
3. **对通道的意义：** 门槛可以降低，但永远在 $\delta=0$ 世界允许的量级之上。所以任何能越过门槛的偶类下界都必须**打破奇偶性**。量化只是把目标缩小了 $\log x$ 倍，并没有绕开奇偶障碍。
4. **下一步（可选）：**
   - 核对 Bombieri / FI 的证明中误差对水平 $\theta$ 的依赖，把 §3 表中的第二、三行变成定理；
   - 把命题 Q 和推论 Q′ 并入论文（v0.9），作为定理 B 的量化补充。
