# 第八阶段：计数版转移定理——把上限从 $p_k^{1+\delta_0}$ 推到 $p_k^{2-\varepsilon}$

**结论（定理 8.1）：** 对任意固定的 $\varepsilon\in(0,1)$、$\eta\in(0,\tfrac12)$，存在 $c=c(\varepsilon)>0$，使得对充分大的 $k$，记 $j=\lceil(1-\eta)k\rceil$，有

$$\#\{\text{偶数间隙}\}=|G_k|\ \ge\ c\cdot\min\bigl(J(j),\ p_k^{2-\varepsilon}\bigr).$$

**和第七阶段的区别：**
- 第七阶段证明**每个**偶数 $t$ 都是间隙，所以需要二维筛法的下界，范围只到 $p_k^{1+\delta_0}$。
- 第二问只问间隙的**个数**。本阶段只证明**正比例**的 $t$ 是间隙，于是只需要一维筛法的下界（线性筛，筛分极限为 2）加二维筛法的上界，范围到 $p_k^{2-\varepsilon}$。
- 已知的无条件上界是 $J(k)\ll p_k^2\log^2p_k$（Iwaniec），所以上限和已知上界之间只差 $p_k^{\varepsilon}$。

**这回答了什么：**
- **无条件：** $|G_k|\ge J(\lceil(1-\eta)k\rceil)^{1-\varepsilon}$ 对所有充分大的 $k$ 成立（推论 8.2）。
- **无条件，多数尺度：** 在至少一半的几何尺度 $k$ 上，$|G_k|\ge c'\min\bigl(J(k),p_k^{2-\varepsilon}\bigr)$（推论 8.4）。
- **第二问：** 现在只依赖两条，且第二条比第七阶段弱得多：
  - (R1) $J(k)\le C\,J(\lceil(1-\eta)k\rceil)$；
  - (R2′) $J(k)\le p_k^{2-\varepsilon}$ 对某个固定的 $\varepsilon>0$，即对 Iwaniec 上界的**任何幂次改进**。
- **第二问仍未无条件解决。** (R1) 没有证明；(R2′) 是公开问题。

**状态标注：** 定理 8.1 及推论是**定理**，证明见 §2，只用两条标准筛法定理（Jurkat–Richert 线性筛下界、Selberg 型上界），**未经审稿**。注记 8.5 是**证明梗概**，其中的筛分极限数值凭文献记忆引用，需要对照原文。本阶段**没有新的数值**：新结论只在 $J\ge p_k^{1+\delta_0}$ 的范围内才比第七阶段强，而这个范围在可计算的 $k$ 上不出现。本阶段由 AI 辅助完成（Claude，Anthropic）。

---

## 1. 陈述

记号同第七阶段：$G_k$ 是 $P_k=p_k\#$ 的既约剩余系的间隙集合，$J(k)=\max G_k$。第 $j$ 层的被覆盖区间是一组剩余类 $c_p \bmod p$（$p\le p_j$），使 $[1,L]$ 的每个整数落在某个类里。

**定理 8.1。** 固定 $\varepsilon\in(0,1)$，$\eta\in(0,\tfrac12)$。存在 $c=c(\varepsilon)>0$，对所有充分大的 $k$ 成立：设 $j=\lceil(1-\eta)k\rceil$，$L=\min\bigl(J(j)-1,\ p_k^{2-\varepsilon}\bigr)$，则至少有 $cL$ 个偶数 $t\le L/2$ 属于 $G_k$。

**推论 8.2（无条件）。** 对固定的 $\varepsilon,\eta$ 和充分大的 $k$，$|G_k|\ge J(\lceil(1-\eta)k\rceil)^{1-\varepsilon}$。

*证明.* 由 Iwaniec 的上界，$J(j)\le Cp_j^2\log^2p_j$，所以 $J(j)^{1-\varepsilon}\le p_k^{2-\frac32\varepsilon}$ 对大的 $k$ 成立。于是 $c\min(J(j),p_k^{2-\varepsilon/2})\ge J(j)^{1-\varepsilon}$（对定理 8.1 用 $\varepsilon/2$）。∎

**推论 8.3（第二问，有条件）。** 若 $J(k)\le C\,J(\lceil(1-\eta)k\rceil)$ 且 $J(k)\le p_k^{2-\varepsilon}$，则 $|G_k|\ge (c/C)\,J(k)$。

**推论 8.4（无条件，多数尺度）。** 设 $\rho=1/(1-\eta)$，$k_i=\lceil\rho^i\rceil$。对充分大的 $n$，至少一半的 $i\le n$ 满足

$$|G_{k_{i+1}}|\ \ge\ c\,\rho^{-5}\min\bigl(J(k_{i+1}),\ p_{k_{i+1}}^{2-\varepsilon}\bigr).$$

*证明.* $J$ 单调不减，且 $J(k_n)\le k_n^{2+o(1)}\le\rho^{(2+o(1))n}$。如果有超过 $n/2$ 个 $i<n$ 满足 $J(k_{i+1})>\rho^5J(k_i)$，则 $J(k_n)>\rho^{5n/2}$，矛盾。对其余的 $i$：$\lceil(1-\eta)k_{i+1}\rceil\ge k_i$，所以定理 8.1 给出 $|G_{k_{i+1}}|\ge c\min(J(k_i),p^{2-\varepsilon})\ge c\rho^{-5}\min(J(k_{i+1}),p^{2-\varepsilon})$。∎

所以第二问只可能在两种情形下失败：$J$ 在 $[(1-\eta)k,k]$ 上跳了一个大因子，或者 $J(k)>p_k^{2-\varepsilon}$。

---

## 2. 定理 8.1 的证明

### 2.0 用到的两条筛法定理

设 $I$ 是长度为 $N$ 的整数区间，对每个素数 $p\le z$ 给定 $\omega(p)$ 个剩余类，$\omega(2)\le1$，$\omega(p)\le2$。筛剩集合是 $I$ 中不落在任何给定类里的整数。两条定理都只用到"落在 $d$ 的所有给定类里的整数个数 $=N\omega(d)/d+O(\omega(d))$"，所以对任意剩余类成立。

- **(L) 线性筛下界**（Jurkat–Richert；Halberstam–Richert《Sieve Methods》定理 8.4）。若每个 $\omega(p)=1$，且 $N\ge z^{2+\theta}$（$\theta>0$ 固定，$z$ 充分大），则筛剩个数 $\ge c_0(\theta)\,N/\log z$。
- **(U) 上界**（Halberstam–Richert 定理 2.2）。若 $2\le z\le N$，则筛剩个数 $\le C\,N\prod_{p\le z}(1-\omega(p)/p)$，$C$ 是绝对常数。

### 2.1 参数

取第 $j$ 层的被覆盖区间 $[1,L]$，剩余类为 $c_p$。**自由素数**是 $p_{j+1},\dots,p_k$，共 $F=k-j\ge\eta k-1\ge\eta p_k/(2\log p_k)$ 个。

令 $B=K\,L\log p_k/(\eta p_k)$，$K=K(\varepsilon)$ 是待定的大常数。

- $M:=L/(2p_k)\to\infty$，并且 $M\ge(\log p_k)^{1/2}$（定理 B）。所以 $B\to\infty$，且 $\log B\le 3\log M+O(1)$。
- $L\le p_k^{2-\varepsilon}$ 给出 $\log p_k\ge\log L/(2-\varepsilon)$，于是 $\log B\le\log L-\log p_k+O(\log\log p_k)\le\bigl(\tfrac{1-\varepsilon}{2-\varepsilon}+o(1)\bigr)\log L$。所以 $L\ge B^{2+\varepsilon}$ 对大的 $k$ 成立。**这是唯一用到 $L\le p_k^{2-\varepsilon}$ 的地方。**

### 2.2 第一步：小素数的幸存点

令 $S=\{x\in[1,L]:\ x\notin c_p\ \forall p\le B\}$。$S$ 的元素奇偶性相同（都不在 $c_2$ 里）。由 (L)，取 $\theta=\varepsilon/2$：$[1,L]$ 的任何长度 $\ge L/2-1$ 的子区间里至少有 $c_0L/\log B$ 个 $S$ 的点，$c_0=c_0(\varepsilon)>0$。

### 2.3 第二步：正比例的差

对 $1\le t\le L/2$，令 $\mathcal X_t=\{x\in S\cap[1,L/2]:\ x+t\in S\}$，$r(t)=|\mathcal X_t|$。$t$ 为奇数时 $r(t)=0$。

- **总数的下界。** $\sum_t r(t)=\sum_{x\in S\cap[1,L/2]}|S\cap(x,x+L/2]|\ \ge\ c_0^2L^2/\log^2B$。
- **单个 $t$ 的上界。** $x\in\mathcal X_t$ 意味着 $x$ 对每个 $p\le B$ 避开 $\{c_p,\,c_p-t\}$；这是 $\omega(p)=1$（当 $p\mid t$）或 $2$（当 $p\nmid t$）个类。由 (U)，
  $$r(t)\ \le\ C_1\,h(t)\,\frac{L}{\log^2B},\qquad h(t)=\prod_{p\mid t,\ p\ge3}\frac{p-1}{p-2}.$$
- **$h$ 的均方。** $h^2$ 是乘性函数，在素数上取值 $1+O(1/p)$，所以 $\sum_{t\le T}h(t)^2\le C_2T$。

**好的 $t$：** 令 $\mathcal T$ 为满足 $r(t)\ge c_1L/\log^2B$ 且 $h(t)\le H$ 的偶数 $t\le L/2$ 的集合，其中 $c_1=c_0^2/2$，$H=2C_1C_2/c_0^2$。

- $r(t)<c_1L/\log^2B$ 的 $t$ 对 $\sum r$ 的贡献 $\le\tfrac L2\cdot c_1L/\log^2B=c_0^2L^2/(4\log^2B)$。
- $h(t)>H$ 的 $t$ 的贡献 $\le C_1\frac{L}{\log^2B}\sum_{h(t)>H}h(t)\le C_1\frac{L}{\log^2B}\cdot\frac{C_2L}{2H}=c_0^2L^2/(4\log^2B)$。
- 所以 $\sum_{t\in\mathcal T}r(t)\ge c_0^2L^2/(2\log^2B)$。而每个 $t\in\mathcal T$ 有 $r(t)\le C_1HL/\log^2B$。于是
  $$|\mathcal T|\ \ge\ \frac{c_0^2}{2C_1H}\,L=\frac{c_0^4}{4C_1^2C_2}\,L=:c\,L .$$

下面证明每个 $t\in\mathcal T$ 都属于 $G_k$。

### 2.4 第三步：放开端点的素数，平均代价小

固定 $t\in\mathcal T$。对 $x\in\mathcal X_t$，$x$ 和 $x+t$ 都不被 $\le B$ 的素数盖住。令 $Q(x)$ 为盖住 $x$ 或 $x+t$ 的素数 $q\le p_j$ 的集合，它们都 $>B$。把这些素数的类改成避开 $x$ 和 $x+t$。**暴露点**是 $(x,x+t)$ 里所有覆盖素数都在 $Q(x)$ 中的点，个数 $\le\mathrm{cost}(x)=\sum_{q\in Q(x)}(t/q+1)$。

令 $N_q=\#\{x\in\mathcal X_t:\ q\in Q(x)\}$。$q\in Q(x)$ 意味着 $x\equiv c_q$ 或 $c_q-t\pmod q$。对每个这样的同余类写 $x=a+qn$，$n$ 取遍长度 $L/(2q)\ge M$ 的区间；条件"$x$、$x+t$ 避开 $p\le B$ 的类"变成 $n$ 对每个 $p\le B$（$p\ne q$）避开同样个数的类。对 $z=\min(B,M)$ 用 (U)。因为 $\log z\ge\tfrac14\log B$（§2.1），

$$N_q\ \le\ C_3\,H\,\frac{L}{q\log^2B}\qquad(B<q\le p_j).$$

于是

$$\sum_{x\in\mathcal X_t}\mathrm{cost}(x)=\sum_{B<q\le p_j}\Bigl(\frac tq+1\Bigr)N_q\ \le\ \frac{C_3HL}{\log^2B}\Bigl[\frac{2t}{B\log B}+2\log\log p_k\Bigr].$$

除以 $|\mathcal X_t|\ge c_1L/\log^2B$：平均代价 $\le C_4\bigl[t/(B\log B)+\log\log p_k\bigr]$，$C_4=2C_3H/c_1$ 只依赖 $\varepsilon$。

- $t/(B\log B)\le L/(2B)=\eta p_k/(2K\log p_k)\le F/K$。取 $K=4C_4$，第一项 $\le F/4$。
- 第二项 $C_4\log\log p_k\le F/4$ 对大的 $k$ 成立。

所以存在 $x\in\mathcal X_t$，暴露点不超过 $F/2$ 个。固定它。

### 2.5 第四、五步：修补与核对

和定理 7.1 的第四、五步完全相同：
- 每个暴露点 $z$ 分配一个自己的自由素数 $\ell_z$，类取 $z \bmod \ell_z$，要求 $\ell_z\nmid(z-x)(x+t-z)$。两个因子都是小于 $t\le p_k^{2-\varepsilon}<p_j^2$ 的正整数，各自至多有一个大于 $p_j$ 的素因子，所以每个 $z$ 至多排除两个自由素数。暴露点不超过 $F/2$ 个，贪心可行。
- 没用上的自由素数取任何避开 $x$ 和 $x+t$ 的类。
- 核对：$x$ 和 $x+t$ 不被任何素数盖住；$(x,x+t)\subset[1,L]$ 里的每个点原来被盖住，它或者还有一个没动过的覆盖素数，或者是暴露点并被 $\ell_z$ 盖住。由引理 1，$t\in G_k$。∎

---

## 3. 注记

**注记 8.5（定理 7.1 的 $\delta_0$ 可以写成显式，证明梗概）。**
- §2.4 的做法也适用于定理 7.1：对所有 $B<q\le p_j$ 用 (U) 直接得到 $N_q\ll(X/q)V$，原证明第三步的第三项 $\tfrac{C_1}{\varepsilon}B^{s_0}\log^2B$ 就不出现了。
- 剩下的唯一约束是二维筛法下界 (S1)：$X\ge B^{\beta_2+\theta}$，$\beta_2$ 是二维下界筛的筛分极限。这等价于 $L\le p_k^{1+1/(\beta_2-1)-\theta'}$。
- 所以定理 7.1 对任意 $\delta_0<1/(\beta_2-1)$ 成立。按文献数值：beta 筛 $\beta_2\approx4.83$，得 $\delta_0<0.26$；Diamond–Halberstam–Richert 筛 $\beta_2\approx4.27$，得 $\delta_0<0.306$。**这两个数值凭记忆引用，写进提交材料前需要对照原文。**

**注记 8.6（为什么停在 $2-\varepsilon$）。** 修补预算要求 $B\gtrsim L/p_k$；线性筛要求 $L\ge B^{2+\theta}$。两者合起来就是 $L\le p_k^{2-\varepsilon}$。Iwaniec 的上界 $J\ll p_k^2\log^2p_k$ 用的是同一个筛分极限，所以这两个界在同一处相遇不是巧合。让 $\varepsilon\to0$ 时 $c(\varepsilon)\to0$（$c_0(\theta)\asymp\theta$），在端点会损失对数因子。

**注记 8.7（滞后）。** 和注记 7.6 一样，$j$ 可以取 $k-\lceil k/\log^Ak\rceil$，证明不变（$B$ 多一个 $\log^Ak$ 因子）。

---

## 4. 更新后的地图

| | 第七阶段之后 | 第八阶段之后 |
|---|---|---|
| 每个偶数 $t\le(1-\varepsilon)L$ 是间隙 | $L\le p_k^{1+\delta_0}$，$\delta_0$ 未指明 | $\delta_0<0.306$（注记 8.5，梗概） |
| 间隙个数 $\gg L$ | 同上 | $L\le p_k^{2-\varepsilon}$（定理 8.1） |
| 第二问还需要 | (R1) 与 $J\le p_k^{1+\delta_0}$ | (R1) 与 $J\le p_k^{2-\varepsilon}$ |
| 无条件的个数下界 | FGKMT 量级 | $J(\lceil(1-\eta)k\rceil)^{1-\varepsilon}$ |

## 5. 判决

- **定理 8.1 把第二问的两个障碍之一几乎消掉了：** 对 $J$ 上界的要求从"指数 $1+\delta_0$"降到"指数小于 2"，而已知的是指数 $2+o(1)$。
- **剩下的障碍：**
  - (R1)，即 $J$ 在相邻尺度间不跳。无条件地只知道它在多数尺度成立。
  - 端点 $p_k^{2-\varepsilon}\le J\le Cp_k^2\log^2p_k$。这里需要的是 Jacobsthal 函数上界的幂次改进，这是筛法里的公开问题。
- **需要外部检查的地方：** §2.3 的 Cauchy–Schwarz 型计数，§2.4 中对同余类内部用 (U)，以及 (L)、(U) 对任意剩余类的适用性。
