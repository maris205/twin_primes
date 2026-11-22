# 第十阶段：逐步重推定理 D、E、F

**结论：** 定理 D（第七阶段）、E（第八阶段）、F 与引理 9.5（第九阶段）的证明逐步重推之后，**没有发现数学错误**，每一步的不等式和指数都能独立核对出来。查出的问题都在表述和引用上，共四处，已全部改正：

1. **"几乎所有 $k$"的一处说法不准（实质性表述问题）。** 原文写"对几乎所有满足 $J(k)\le p_k^{1+\delta_0}$ 的 $k$，$s(k)=(1+o(1))J(k)$"。定理 9.2 的例外集只是相对**全体整数**密度为零；满足 $J(k)\le p_k^{1+\delta_0}$ 的 $k$ 本身的密度未知，原则上可能整个落在例外集里。正确的说法是："存在密度为零的集合 $\mathcal E'$，使得 $k$ 跑过 $k\notin\mathcal E'$ 且 $J(k)\le p_k^{1+\delta_0}$ 的值时，$s(k)=(1+o(1))J(k)$。"另外，从固定 $\varepsilon$ 到 $(1+o(1))$ 要做一次对角线论证，原文没有提到。
2. **Iwaniec 上界写弱了。** Iwaniec（1978）的结果是 $j(n)\ll(\omega(n)\log\omega(n))^2$，对 $n=P_k$ 就是 $J(k)\ll(k\log k)^2\asymp p_k^2$，没有额外的 $\log^2p_k$。原文写的 $J\ll p_k^2\log^2p_k$ 是对的，但比已知结果弱。证明里只用到 $J(2K)\le K^3$ 和 $J(k)\le p_k^{2+o(1)}$，不受影响；改正后，"上限 $p_k^{2-\varepsilon}$ 与已知上界只差 $p_k^\varepsilon$"这句话更准确。
3. **常数上的小疏漏。** 定理 9.1 的证明里写"由定理 B，$J(j)/p_k\ge(\log p_k)^{1/2}$，所以 $\log M\ge\tfrac12\log\log p_k$"。$M=\varepsilon L/(2p_k)$ 带一个因子 $\varepsilon/2$，严格说推不出来。实际上定理 B 加上 $J(j)\ge s(j)-2$ 给出 $J(j)/p_k\gg\log p_k\log_3p_k/(\log_2p_k)^2$，这比 $(\log p_k)^{1/2}$ 大一个趋于无穷的因子，所以结论成立。已改写。
4. **$\kappa(\varepsilon)$ 没写出来。** 定理 9.2 的 $\kappa$ 应取 $\min(\kappa_0,\varepsilon/8)$：(i) 用 9.1(a) 的 $\kappa_0$，(ii) 用 9.1(b) 的 $\varepsilon/4$，(iii) 对 (ii) 取 $\varepsilon/2$，所以是 $\varepsilon/8$。已补上。

**引用核对：**
- **注记 8.5 的筛分极限：** Diamond–Halberstam–Richert 筛在维数 2 的筛分极限是 $\beta_2=4.266$（Franze, arXiv:1012.3809, 表 1；数值出自 Diamond–Halberstam 的专著）。于是 $\delta_0<1/(\beta_2-1)\approx0.306$ 的数值对了。原先凭记忆写的 beta 筛数值 $4.83$ 没有找到出处，已删去。注记 8.5 本身仍是梗概。
- **[HR] 定理编号：** 二手文献的引用与我们的用法一致：HR 定理 2.2 是 Brun 筛的上界，条件含 $z\le X$；定理 8.4 是线性筛（Jurkat–Richert）的下界，下界函数在 $2\le s\le4$ 上是 $f(s)=2e^\gamma\log(s-1)/s$。**原书的逐字陈述没有看到**，提交前最好对照原书。

**状态标注：** 这是**同一个 AI 系统**对自己证明的复查，不等于独立审稿。它能抓出推理跳步和表述错误，但可能和原证明有同样的盲点。本阶段没有新定理，也没有新数值。本阶段由 AI 辅助完成（Claude，Anthropic）。

---

## 1. 逐步核对表

记号同第七至九阶段。"✓"表示该步重推成立，"改"表示已修正表述。

### 定理 D（第七阶段 §2）

| 步骤 | 要核对的内容 | 结果 |
|---|---|---|
| 覆盖判定 | 剩余类 $c_p$ 的未覆盖集是既约剩余系的平移（中国剩余定理） | ✓ |
| 参数 | $L\ge p_k/\varepsilon$ 由 $J(j)/p_k\to\infty$；$B\le p_k^{\delta_0+o(1)}<p_j$ | ✓ |
| (S1)(S2) | 二维基本引理：$\rho(2)=1$，$\rho(p)\le2<p$，余项 $\lvert r_d\rvert\le\rho(d)$，对任意剩余类成立；水平 $D=B^{s}$，$X\ge B^{s+1}$ 时余项被吸收，取 $s_0=s+1$ | ✓ |
| $\delta_0=1/(2s_0)$ | $B^{s_0}\le p_k^{1/2+o(1)}\le p_k\le X$ | ✓ |
| 第二步 | $Q(x)\subset(B,p_j]$；$q\ge5$，至少还剩 $q-2$ 个可选的类；暴露点 $\le\sum_{q\in Q(x)}(t/q+1)$ | ✓ |
| 第三步，小 $q$ | $N_q\le2\cdot2(X/q)V$；$\sum_{q>B}q^{-2}\le2/(B\log B)$；$\sum_{B<q\le p_j}q^{-1}\le2\log\log p_k$ | ✓ |
| 第三步，大 $q$ | $N_q\le2(X/q+1)\le4X/q$（$q\le p_j\le X$）；$Y=X/B^{s_0}\ge p_k^{1/2-o(1)}$，所以 $\sum_{Y<q\le p_j}q^{-1}\le\log2+o(1)\le1$；$t/X\le1/\varepsilon$ | ✓ |
| 平均代价 | 三项分别 $\le F/6$、$o(F)$、$p_k^{1/2+o(1)}=o(F)$ | ✓ |
| 第四步 | $z-x$、$x+t-z<t\le p_k^{1+\delta_0}<p_j^2$，各至多一个 $>p_j$ 的素因子；$F/2\le F-2$ | ✓ |
| 第五步 | 端点：原覆盖素数全在 $Q(x)$ 中（$\le B$ 的素数不覆盖它们）；内部点：原来被覆盖，或保留了一个没动过的覆盖素数，或被 $\ell_z$ 修补 | ✓ |
| 推论 7.5 | $J$ 单调不减（多一个素数只会多覆盖）；$J(k_n)\le p_{k_n}^{1+\delta_0}\le\rho^{2n}$；$\lceil(1-\eta)\lceil\rho^{i+1}\rceil\rceil\ge\lceil\rho^i\rceil$ | ✓ |

### 定理 E（第八阶段 §2）

| 步骤 | 要核对的内容 | 结果 |
|---|---|---|
| (L) | HR 定理 8.4：$(\Omega_1)$、$(\Omega_2(1,L))$、$\lvert R_d\rvert\le\omega(d)$；$N\ge z^{2+\theta}$ 时 $f(2+\theta)>0$，误差项 $\to0$；$c_0(\theta)\asymp\theta$ | ✓（原书逐字未见） |
| (U) | HR 定理 2.2：Brun 筛上界，$z\le N$，维数 $\kappa=2$；$\omega(2)=1$，$\omega(3)\le2$ 满足 $(\Omega_1)$ | ✓（原书逐字未见） |
| $L\ge B^{2+\varepsilon}$ | $(2+\varepsilon)(1-\varepsilon)/(2-\varepsilon)=1-\varepsilon^2/(2-\varepsilon)<1$ | ✓ |
| $\log z\ge\frac14\log B$ | $\log B=\log M+\log\log p_k+O(1)\le3\log M+O(1)$ | ✓ |
| $\sum_tr(t)$ | $(x,x+L/2]\subset[1,L]$，两个区间长度都 $\ge L/2-1$ | ✓ |
| $r(t)$ 上界 | $W=\tfrac12\prod_{3\le p\le B}(1-2/p)\prod_{p\mid t,\,3\le p\le B}\frac{p-1}{p-2}\ll h(t)/\log^2B$ | ✓ |
| $\sum h^2\le C_2T$ | $h^2$ 只依赖根基，$h^2=1*g$，$g(p)=O(1/p)$，$g(p^a)=0$（$a\ge2$）| ✓ |
| $\lvert\mathcal T\rvert\ge cL$ | 两类坏 $t$ 各贡献 $\le c_0^2L^2/(4\log^2B)$；常数逐个算对 | ✓ |
| 第三步 | 写 $x=a+qn$；$q>B$ 与 $p\le B$ 互素，禁类个数不变；只筛 $p\le z$ 给上界 | ✓ |
| $K$ 的选取 | $K=4C_4$；$C_4$ 只依赖 $\varepsilon$，不依赖 $B$，没有循环 | ✓ |
| 推论 8.2、8.4 | 见上；8.2 用 $J(j)\ll p_j^2$ 即可 | ✓（改：上界写法） |

### 定理 F（第九阶段 §2）

| 步骤 | 要核对的内容 | 结果 |
|---|---|---|
| (a) $B=X^{1/s_0}$ | (S1) 恰好可用；$B\le p_k^{(1+\delta_0)/s_0}<p_j$ | ✓ |
| (b) $B=(L/4)^{1/(2+\theta)}$ | $B^{2+\theta}=L/4\le L/2-1$，(L) 可用；$B\le L^{1/2}<p_j$ | ✓ |
| 改动二 | $n$ 区间长度 $\ge X/q\ge2M$（(a)）或 $L/(2q)\ge M/\varepsilon$（(b)）；$V(z)/V(B)\ll(\log B/\log z)^2$ | ✓ |
| $(\log B/\log z)^2$ 损失 | $\log z\ge\frac12\log\log p_k$，$\log B\le2\log p_k$，损失 $\le16\log^2p_k$；$\log\log p_k\le L/B$ | ✓（改：$M$ 的下界说明） |
| (a) 指数 | $(1+\tfrac1{2s_0})(1-\tfrac1{s_0})=1-\tfrac1{2s_0}-\tfrac1{2s_0^2}$；$F\ge p_k^{1-1/(4s_0)-o(1)}$ | ✓ |
| (b) 指数 | $(2-\varepsilon)(4+\varepsilon)\le(1-\varepsilon/3)(8+\varepsilon)\iff-\varepsilon/3-2\varepsilon^2/3\le0$；$F\ge p_k^{1-\varepsilon/4-o(1)}$ | ✓ |
| 注记 9.3 | $k-\lceil k^{1-\kappa}\rceil\ge\lceil(1-\eta)k\rceil$，$J$ 单调，所以 D、E 是 F 的特例 | ✓ |

### 引理 9.5 与定理 9.2（第九阶段 §3）

| 步骤 | 要核对的内容 | 结果 |
|---|---|---|
| 贪心覆盖 | 每个 $b\in\mathfrak B_C\cap[K,2K]$ 落在某个 $[k_i-F(k_i),k_i]$ 里；$F$ 单调 | ✓ |
| 放大链 | $J(k_i)>C\,J(k_i-F(k_i))\ge C\,J(k_{i+1})$ | ✓ |
| 次数上界 | $J(2K)\ll(2K\log2K)^2\le K^3$；$J(K)\ge2$ | ✓ |
| (i)(ii)(iii) | $\frac{1-\varepsilon/2}{1+\varepsilon/2}\ge1-\varepsilon$；$\min(J(k)/C,P)\ge\min(J(k),P)/C$；二进分块求和 $\ll K^{1-\kappa}\log K$ | ✓（改：写出 $\kappa$） |
| "$(1+o(1))$"推论 | 需要对 $\varepsilon\to0$ 做对角线论证；例外集只相对全体整数密度为零 | 改 |

## 2. 改动清单

- `STAGE8_COUNT.md`：Iwaniec 上界改为 $J\ll p_k^2$（三处）；注记 8.5 写入核对过的 $\beta_2=4.266$，删去 beta 筛数值。
- `STAGE9_JUMP.md`：第一、二问的"几乎所有"表述；$M$ 的下界说明；Iwaniec 上界；$\kappa(\varepsilon)=\min(\kappa_0,\varepsilon/8)$。
- `STAGE2_RANKIN.md`、`STAGE4_FGKMT.md`：Iwaniec 上界的写法。
- `submission/note854.md`：上面的对应改动（英文）；参考文献加 Diamond–Halberstam 与 Franze；§7 注明这次复查不能代替独立审稿。
- `submission/erdos854_forum_post.md`：Iwaniec 上界的写法。
- `submission/README.md`：去掉"$\beta_2$ 未核对"一条，改为"HR 两条定理的原书陈述未逐字核对"。

## 3. 还没做到的

- **独立审稿。** 这次复查和原证明出自同一个系统。真正的检查需要懂筛法的人，最值得看的仍是 §6.3 的改动二（$z=\min(B,M)$ 与对数损失）和 §6.2 的 Cauchy–Schwarz 型计数。
- **HR 原书。** 定理 2.2、8.4 的条件是按二手文献和标准表述核对的，没有看到原书的逐字陈述。
- **注记 8.5** 仍是梗概：把二维下界筛换成 DHR 筛之后的完整证明没有写。

## 4. 判决

- **定理 D、E、F 和引理 9.5 的证明，在这次逐步重推下成立。** 状态仍是"定理（未审稿）"。
- **一处结论的表述收紧了：** "$s(k)\sim J(k)$"只对例外集之外、且满足 $J(k)\le p_k^{1+\delta_0}$ 的 $k$ 成立；后一个条件的 $k$ 有多少，目前不知道。
- 第二问的状况不变：对每个 $k$ 仍需要 (R1′) $J(k)\ll J(k-\lceil k^{1-\kappa}\rceil)$ 和 (R2′) $J(k)\le p_k^{2-\varepsilon}$。

**来源：** C. S. Franze, *Sifting limits for the $\Lambda^2\Lambda^-$ sieve*, arXiv:1012.3809（表 1）；H. G. Diamond, H. Halberstam, *A Higher-Dimensional Sieve Method*, Cambridge Univ. Press 2008；H. Iwaniec, *On the problem of Jacobsthal*, Demonstratio Math. 11 (1978)。
