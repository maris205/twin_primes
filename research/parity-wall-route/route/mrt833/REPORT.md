# MRT 的 8/33：能否只靠改进 Type $d_3$ 指数和一步来降低？（2026-10-28）

**对象：** Matomäki–Radziwiłł–Tao, *Correlations of the von Mangoldt and higher divisor functions **I**. Long shift ranges*，arXiv:1707.01315（Proc. LMS 118 (2019)）。
- 更正：任务描述写的是 "II, Math. Ann."。但 arXiv:1707.01315 是第 I 篇；Math. Ann. 上的第 II 篇（arXiv:1712.08840）处理的是对数长度的 $H$。
- 下文的 §、命题、引理和公式编号都指 arXiv v3。

**一句话答案：**
- **到 3/13：** 目前做不到，属于结论 (b)。本文给出每条自然路线断在哪里。
- **到 7/30：** 有一条干净的条件路线。只要一个与 Robert–Sargos 同型的四元计数猜想（猜想 A，在 $\ell$ 上平均即可）成立，就能把 8/33 降到 **7/30**。
  - 这条路线本身证明不了 7/30 以下的任何指数。
  - 猜想 A 我没能证明。现有的无条件计数（除数界）太弱，代入后只得到 7/24，比 MRT 还差。
- **新颖性：** 没有找到 2019–2026 年间改进 8/33 或改进 $d_3$ 步骤的文献（检索有限，见 §6）。

**状态标签：**
- 【定理】：完整证明，或可由文中步骤直接补全的标准论证。
- 【条件定理】：依赖猜想 A。
- 【分析】：指数核算、启发式、或者"某方法到此为止"式的论证。这类结论 AI 辅助完成，未经专家核对。
- 【数值】：小规模穷举，只作佐证。

**脚本：** `route/mrt833/mrt833_exponents.py`（Python 2.7/3 均可）。
- Part A：全部指数，用 `fractions` 精确有理数计算。
- Part B：整数恒等式检验。
- Part C：小 $M$ 穷举计数。

---

## 0. 记号与目标（沿用第十二阶段）

| 记号 | 含义 |
|---|---|
| $H=X^{\sigma}$ | 平移范围 |
| $T\asymp\lambda X$ | $X^{5/6-2\varepsilon}\ll T\ll X$，见 (108) |
| $M=M_1$ | $M\ll X^{1/3}$，见 (110) |
| $\ell$ | $1\le\ell\ll X^{O(\varepsilon^2)}M/H$ |
| $r$ | $t_1<\dots<t_r$ 的个数，$t_j\in[T,2T]$ 两两相距 $\ge\sqrt T$，故 $r\ll\sqrt T$ |

MRT (105) 在用引理 2.2 去掉 $\beta_1$ 与 $\hat\eta$ 权之后，给出
$$\tilde Y(t)=\frac HM\sum_{1\le\ell\ll M/H}\Big|\sum_{M\le m\le 2M}e\Big(\frac t{2\pi}\log\frac{m+\ell}{m-\ell}\Big)\Big|^*=\frac HM\sum_\ell |S_\ell(t)|^*,\qquad S_\ell(t):=\sum_{m}\Big(\frac{m+\ell}{m-\ell}\Big)^{it}.$$

**目标（命题 7.5）：**
$$\sum_j\tilde Y(t_j)^4\ll X^{-\varepsilon}H^4\sqrt T .$$

**MRT 实际证到的（§8 末）：**
$$\sum_j\tilde Y(t_j)^4\ll X^{4/3}+H^{-3/2}\lambda X^{11/6}.$$
其中第二项在 $\lambda=1$ 时恰好给出 $8/33$（脚本 Part A 复算）。

---

## 1. 精确重写：artanh 加法公式【定理】

由 $\log\frac{m+\ell}{m-\ell}=2\,\mathrm{artanh}(\ell/m)$ 和 $\mathrm{artanh}\,x+\mathrm{artanh}\,y=\mathrm{artanh}\frac{x+y}{1+xy}$，
$$\frac{(m_1+\ell)(m_2+\ell)}{(m_1-\ell)(m_2-\ell)}=\frac{1+\ell u}{1-\ell u},\qquad u=u_\ell(m_1,m_2)=\frac{m_1+m_2}{m_1m_2+\ell^2}.$$
所以 $S_\ell(t)^2=\sum_{m_1,m_2}\big(\tfrac{1+\ell u}{1-\ell u}\big)^{it}$：两项相加之后，相位只依赖于一个**分母 $\asymp M^2$、分子 $\asymp M$ 的有理数** $u$。

四次矩里出现的量是：
$$P=(m_1+\ell)(m_2+\ell)(m_3-\ell)(m_4-\ell),\qquad Q=P|_{\ell\to-\ell}.$$
它们满足精确恒等式
$$P-Q=2\ell\,D_\ell(\mathbf m),\qquad D_\ell(\mathbf m):=(m_1+m_2)(m_3m_4+\ell^2)-(m_3+m_4)(m_1m_2+\ell^2)=\det\big(v(m_1,m_2),v(m_3,m_4)\big),$$
其中 $v(a,b)=(a+b,\ ab+\ell^2)\in\mathbb Z^2$。

令 $s=m_1+m_2$，$s'=m_3+m_4$，$w=m_1-m_2$，$z=m_3-m_4$，$d=s-s'$。则还有
$$4D_\ell=s'w^2-sz^2-ss'd+4d\ell^2 .$$

脚本 Part B 在 2000 个随机整数组上逐一验证了以上恒等式。

**推论（光滑化后的四次矩 = 计数）。** 取光滑 $w\ge0$，在 $[1/2,3]$ 上 $w\ge1$，且 $\hat w$ 快速衰减。由 $|\log(P/Q)|\asymp|P-Q|/M^4$，
$$\int w(t/T)|S_\ell(t)|^4dt\ \ll\ T\sum_{k\ge0}2^{-10k}N_\ell(2^k\eta_\ell),\qquad \eta_\ell:=\frac{M^4}{T\ell},$$
$$N_\ell(\eta):=\#\{\mathbf m\in[M,2M]^4:\ |D_\ell(\mathbf m)|\le\eta\}.$$

几点说明：
- 极大和 $|\cdot|^*$（对子区间取上确界）的处理是标准的：插入 $\int_0^1|\sum_m e(m\theta)\cdots|\min(M,\|\theta\|^{-1})d\theta$，付出 $\log^4$ 的代价。扭曲因子 $e(\theta(m_1+m_2-m_3-m_4))$ 的模为 1，所以同一个计数上界仍然成立。
- 与 MRT §8 的 Taylor 展开不同，这里**没有余项** $R_{j,\ell}$，因为恒等式是精确的。

**取值规模：** 在最坏点 $T=X$、$M=X^{1/3}$、$\ell\asymp M/H$ 处，$\eta_\ell\asymp H$。

---

## 2. 去掉"盒子"之后能走多远：条件改进到 7/30

### 2.1 MRT 的损失在哪里【分析，核对原文】

MRT 先把 $\Sigma_j$ 换成对 $\alpha=t\ell/M$ 的积分（局部常数尺度为 $M/\ell\le H$），再用引理 2.3(i) 缩短到 $\alpha\ll S$，然后把 $L$ 条直线 $\beta=\ell^2\alpha/M^2$（$\ell\sim L$）的 1-邻域并起来，**整体换成矩形盒子** $\{\alpha\asymp A,\ \beta\ll L^2A/M^2\}$。$W_3$ 一项就是在这个盒子上的积分。

- **在盒子上 $W_3\ll L^2A^2$ 已经是对角最优的**（第十二阶段已核对）。
- **真正的损失**是"直线并 → 盒子"这一步。当 $A\gg M^2/L$ 时，这些直线在 $\beta$ 方向的间距 $LA/M^2\gg1$，盒子面积是直线并的 $LA/M^2$ 倍。
- **$S$ 的选取已最优【定理，初等】：** (118) 的右边 $\frac{HTL^2M^2}{S}+\frac{HTL^3S}{M^2}$ 由 AM-GM 在 $S=M^2L^{-1/2}$ 处取到最小，而在最坏点 $TL^{3/2}\ge M^3$，约束 $S\le TL/M$ 并不起作用。所以"按 $(L,A)$ 换一个 $S$"在盒子框架内**不可能**有任何改进。

### 2.2 逐条直线的四次矩

**猜想 A（在 $\ell$ 上平均的四元间距计数）。** 对 $1\le L\le M/2$ 和一切 $\eta\ge0$，
$$\sum_{\ell\sim L}N_\ell(\eta)\ \ll_\varepsilon\ M^{\varepsilon}\,L\,(M^2+M\eta).$$

关于猜想 A：
- 它与 MRT 引理 2.3(ii)（Robert–Sargos 对单项式 $m^\theta$ 的 $N(\delta)\ll N^{2+\varepsilon}+\delta N^{4+\varepsilon}$）同型。
  - 第一项是对角项：$\{m_1,m_2\}=\{m_3,m_4\}$。
  - 第二项是"$D$ 的取值在长 $M^3$ 的范围内均匀分布"给出的期望值 $M^4\cdot\eta/M^3$。
- 当 $\eta\ge M^3$ 时它是平凡的。
- **注意：** 相位 $\mathrm{artanh}(\ell/m)$ 不是单项式，Robert–Sargos 的齐次性论证不能直接搬过来。

**条件定理 2.1。** 若猜想 A 成立，则对一切 $\sigma>7/30$，命题 7.5 都成立。因此（Type $d_4$ 用经典指数对，引理 7.2 恰好也是 $7/30$）MRT 的 Theorem 1.3 对 $\sigma=7/30=0.2333\ldots$ 成立。

*证明。*
1. **Hölder（与 MRT 相同）：** $\tilde Y(t)^4\ll X^{O(\varepsilon^2)}\frac HM\sum_\ell|S_\ell(t)|^{*4}$。
2. **局部常数性：** $t\mapsto S_\ell(t)$ 的频率 $\log\frac{m+\ell}{m-\ell}$ 落在长 $\asymp\ell/M$ 的区间里。因此 $|S_\ell|^{*4}$ 在尺度 $M/\ell$ 上被其局部平均控制，与 (112) 的论证相同。由于 $M/\ell\le M\le\sqrt T$，以各个 $t_j$ 为中心、长 $M/\ell$ 的窗口两两不交，于是
   $$\sum_j|S_\ell(t_j)|^{*4}\ll X^{O(\varepsilon^2)}\frac{\ell}{M}\int w(t/T)|S_\ell(t)|^{*4}dt .$$
3. **代入 §1 的推论与猜想 A**（对 $\ell$ 作二进分块）：
   $$\sum_j\tilde Y(t_j)^4\ll X^{O(\varepsilon)}\frac HM\sum_{L}\frac LM\,T\,L\Big(M^2+\frac{M^5}{TL}\Big)\ll X^{O(\varepsilon)}\Big(\frac{TM^2}{H}+M^4\Big),$$
   这里用了 $L\ll X^{O(\varepsilon^2)}M/H$。
4. **核对两项：**
   - $TM^2/H\le X^{-\varepsilon}H^4\sqrt T$ 等价于 $H^5\ge X^{\varepsilon}\sqrt T M^2$。在 $T=X$、$M=X^{1/3}$ 时最紧，给出 $\sigma>7/30$。
   - $M^4\le X^{-\varepsilon}H^4\sqrt T$ 在 $T=X^{5/6}$ 时最紧，给出 $\sigma>11/48$；而 $11/48<7/30$。∎

**换算：**
- 用第十二阶段的插值参数表示，$7/30$ 对应 $\theta=16/19$，脚本 Part A 复算。
- 用"每个 $\ell$ 的有效计数"表示（$T=X$，$M=X^{1/3}$，$\eta=H=M^{3\sigma}$，单位为 $M$ 的幂），各方法给出的 $N$ 如下：

| $\sigma$ | 允许的 $N\le H^5/\sqrt T$ | MRT 等效 $M^{5/2}\eta^{-1/2}$ | 猜想 A：$M^2+M\eta$ | 除数界 $M^{2}\eta$ |
|---|---|---|---|---|
| 8/33 | $M^{47/22}$ | $M^{47/22}$（恰好相等） | $M^{2}$ | $M^{30/11}$ |
| 7/30 | $M^{2}$ | $M^{43/20}$ | $M^{2}$（恰好相等） | $M^{27/10}$ |
| 3/13 | $M^{51/26}<M^2$ | $M^{28/13}$ | $M^{2}$（不够） | $M^{35/13}$ |

"MRT 等效"一列是把 MRT 的最终界反解成对 $\ell$ 平均的计数，属于【分析】。可以看到，**MRT 的盒子论证在对 $\ell$ 平均的意义下，其实已经胜过逐个 $\ell$ 用除数界**。

### 2.3 无条件能做到什么【分析/定理混合】

**除数界【定理】：**
- 换元 $h=m_3-m_1$，$h'=m_2-m_4$，$X=2m_2-h'$，$Y=2m_1+h$，条件化为
  $$|hX^2-h'Y^2-(h-h')(4\ell^2-hh')|\le4\eta .$$
- 对每个 $(h,h')$ 和每个目标整数值，二元二次型的表示数 $\ll M^\varepsilon$。$hh'$ 为平方数、目标为 0 的退化情形，以及 $h=h'$ 的情形另外计数，都不超过同一量级。
- 由此得到 $N_\ell(\eta)\ll M^{2+\varepsilon}(1+\eta)$。
- 这个界**太弱**：代入后多出一项 $M^5$，只给出 $\sigma\ge7/24$，比 MRT 差。

**$\eta<1$ 的情形【定理】：** 只剩精确解，上面的论证给出 $N_\ell\ll M^{2+\varepsilon}$。但 $\eta_\ell<1$ 等价于 $M^4<T\ell$，在 $M$ 接近 $X^{1/3}$ 的最坏情形从不发生，所以不改变最终指数。

**真正缺的东西：** 证明在长 $\eta\approx M^{0.7}$ 的窗口里，$D_\ell$ 的"近零值"只有期望数 $M\eta$ 个。
- 对 $(w,z)$ 两个变量作 Poisson 求和之后，对偶和的平凡估计只给出 $M^4L/\eta$。
- 需要对偶 $(a,b)$-和再有平方根抵消。这在本质上就是原来的四次矩问题本身，绕了一圈回到原点【分析】。

**数值【数值】：** 脚本 Part C 对 $M\in\{24,48,96\}$、$\eta\in\{0,M/8,M/2,M\}$ 作了穷举。
- $N_\ell(\eta)/(M^2+M\eta)$ 落在 $1.2$–$2.1$ 之间；比值约为 2 来自对角项的两种配对。
- 除数界 $M^2(1+\eta)$ 高估了一到两个数量级。
- 这支持猜想 A，但规模太小，不构成证据。

---

## 3. 7/30 是"连续矩"路线的硬上限【定理 + 分析】

**命题 3.1【定理】。** 在 $T\asymp X$、$M\asymp X^{1/3}$、$\ell\asymp M/H$ 时，
$$\int_T^{2T}|S_\ell(t)|^4dt\ \ge\ (1-o(1))\,TM^2 .$$

*证明。*
- 相邻频率的间距 $\asymp\ell/M^2$。由 Montgomery–Vaughan 均值定理，$\int_T^{2T}|S_\ell|^2=TM+O(M^3/\ell)$。
- 而 $T\ell/M^2\asymp T/(MH)\ge X^{1/2-\sigma}\to\infty$，所以误差项可以忽略。
- 再由 Cauchy–Schwarz 即得。∎

**推论【分析，严格到方法层面】。** 任何先把离散和 $\sum_j|S_\ell(t_j)|^4$ 控制为 (窗口)$^{-1}\times$(整段 $[T,2T]$ 上的连续矩)，再估计连续矩的论证，都会得到
$$\sum_j\tilde Y^4\gg TM^2/H .$$
这个量不小于 $X^{-\varepsilon}H^4\sqrt T$ 当且仅当 $\sigma\le7/30$。所以：
- **盒子换直线**（猜想 A）至多把 $8/33$ 推到 $7/30$。
- 要到 $3/13$，还需要额外节省 $X^{1/78}$（Part A 精确算出），而且这部分节省**只能来自 $t_j$ 的 $\sqrt T$ 间隔**。
- 这一结论也解释了为什么"把离散点直接换成整段积分"（第十二阶段指出的损失）与"盒子"是两层不同的损失：
  - 盒子一层价值 $L^{1/2}$；
  - 整段积分一层价值 $\sqrt T/H$，仅凭四次矩信息无法回收。

---

## 4. 利用 $\sqrt T$ 间隔：三条自然路线断在哪里【分析】

逐个 $\ell$ 看，需要的是一个大值估计。记 $R(V)=\#\{j:|S_\ell(t_j)|\sim V\}$，则需要
$$V^4R(V)\le X^{-\varepsilon}H^4\sqrt T .$$
- 因为 $R\le r\ll\sqrt T$，$V\le H$ 的部分自动成立。
- 所以要控制的是 $V\in[H,M]=[X^{3/13},X^{1/3}]$ 的大值，而且在整个区间上都需要比四次矩多节省 $X^{1/78}$。

### (i) Halász–Montgomery

由对偶，
$$R^2V^2\le M\,(RM+R^2K),\qquad K=\max_{j\ne k}\Big|\sum_m e\big((t_j-t_k)F_\ell(m)\big)\Big| .$$
只要 $V^2\ge2MK$，就得到 $R\le2M^2/V^2$，从而 $V^4R\le2M^4\le H^4\sqrt T$，问题解决。但是：
- 由均值定理，$K\gtrsim\sqrt M$。因此即使假设 Lindelöf 型的 $K\ll M^{1/2+\varepsilon}$，也只能处理 $V\ge M^{3/4}=X^{1/4}$。
- **断点：** $V\in[X^{3/13},X^{1/4}]$ 这一段，Halász 在任何假设下都无能为力。
- 无条件地，用指数对 $(1/6,2/3)$ 估计 $K$，只能覆盖 $V\gtrsim X^{0.314}$。
- 分块版本（Huxley 式，块长 $MH$，使 $K$ 很小）也不行：每块只含 $X^{1/3+\sigma-1/2}\approx X^{0.06}$ 个点，而 Halász 给出的每块界 $M^2/V^2\ge X^{0.2}$ 比平凡界还差。

### (ii) 更高阶矩

如果六次矩是对角的（$\int|S_\ell|^6\ll TM^3$），由
$$\sum_J\sup_J|S|^4\le(\#J)^{1/3}\Big(H^{-1}\int|S|^6\Big)^{2/3}$$
可以得到 $3/14<3/13$，即足以走到 $3/13$。

**但这个前提是假的【定理】。** 六项和 $\sum\pm F_\ell(m_i)$ 只分布在长 $\asymp\ell/M$ 的区间里。对区间分箱后用 Cauchy–Schwarz，得到
$$\int_T^{2T}|S_\ell|^6\gg M^7/\ell\approx H\cdot TM^3 .$$
用真实的量级代入，这条路线只给出 $\sigma\ge1/4$，比 MRT 还差（Part A）。更高阶的矩更糟。

### (iii) 双大筛 / 间距计数

- 作 B-过程之后（$u=\sqrt t$），
  $$S_\ell(t)\approx c\sum_{k\sim K}e\big(u\,\omega_k+\dots\big),\qquad \omega_k\approx2\sqrt{\ell k/\pi},\quad K\asymp T\ell/M^2,\quad |c|\approx X^{-0.05}.$$
  点 $u_j=\sqrt{t_j}$ 两两相距 $\ge1/2$。
- 于是问题变成：对相距 $1/2$ 的点 $u_j$ 和频率 $\nu=\omega_{k_1}+\omega_{k_2}$（范围 $\asymp\sqrt T/H\gg1$），估计 $\sum_j|\sum_\nu a_\nu e(u_j\nu)|^2$。
- Gallagher、Bombieri–Iwaniec 双大筛和对偶核方法都给出因子 $\max(1,\text{频率范围})=\sqrt T/H$，与 §3 的损失完全相同。
- 原因是：**仅知道间隔、不知道点集的其它结构时**，$u_j$ 可以取为公差 $1/2$ 的等差数列。这时核 $\sum_je(u_j(\nu-\nu'))$ 在 $\nu-\nu'\in2\mathbb Z$ 处混叠，$\sqrt T/H$ 层频率可以相干叠加。
- 要排除这种相干叠加，必须用到 $S_\ell$ 本身（或者 $t_j$ 作为 $\tilde Y$ 极大点）的算术结构。这已经超出"间距引理"的范围。

**Guth–Maynard：** 第十二阶段已说明，它的对象（任意系数的 Dirichlet 多项式）和区间都不对。这里补一句：$V\approx M^{0.69}$–$M^{0.75}$ 恰好落在它的"有效区间"附近，但它要求的是 $D[\beta_1]$ 在 $t\approx M^3$ 处的大值点，而本问题的点是 $\sqrt T$-间隔的窗口极大点，无法对接【分析，未深究】。

---

## 5. 结论

1. **到 3/13（$\theta=4/5$）：做不到，结论 (b)。**
   - 只改进间距/盒子这一步，最多回收 $L^{1/2}$，即 $\theta=16/19$，对应 $7/30$。这已是任何"连续矩"论证的硬上限（命题 3.1）。
   - 剩下的 $X^{1/78}$ 必须来自对 $V\in[X^{3/13},X^{1/4}]$ 的大值估计。Halász 在这一段不起作用（即使假设 Lindelöf）；六次矩的真实量级是非对角的；双大筛被等差数列混叠卡住。
   - 第十二阶段"只需恢复 20% 损失"的说法在数字上没错，但这 20% 落在了**结构上最难**的那一层。
2. **到 7/30：有条件定理（定理 2.1，依赖猜想 A）。**
   - 猜想 A 是 artanh 相位的 Robert–Sargos 型四元计数，只需在 $\ell$ 上平均即可。
   - 小规模数值支持猜想 A。
   - 无条件的除数界不够；MRT 的盒子论证在 $\ell$-平均意义下等效于计数 $M^{5/2}\eta^{-1/2}$，比除数界好，但仍不如猜想 A。
3. **严格的新东西：** §1 的精确恒等式（artanh 加法 → 行列式 $\det(v,v')$）。它去掉了 MRT §8 的 Taylor 余项，把问题化为一个干净的整数计数问题。
   - 本报告**不声称**对 8/33 有任何无条件改进。

**下一步最有希望的方向：** 证明猜想 A，哪怕只在 $\ell$ 平均下、只对 $\eta\asymp H$ 成立。
- 可以尝试的结构：$D$ 关于 $\ell^2$ 是线性的，对 $\ell$ 平均是一个关于 $\ell$ 的二次 Weyl 和。
- 可以借鉴的工具：Robert–Sargos 对单项式的论证；整点靠近曲线的计数（Huxley、Swinnerton-Dyer、Bombieri–Pila）。
- 如果能证明，就能无条件得到 $7/30$。由于引理 7.2 恰好也是 $7/30$，不需要 Robert 的指数对。

---

## 6. 文献核对（检索有限）

- 2026-10 的网页检索只找到 MRT 原文；那条检索摘要还称 8/33 是"目前最好的结果"，但这句话的出处没有独立核实。
- 没有找到改进 8/33、或改进 Type $d_3$ 指数和步骤的论文。
- 相近但不相干的工作：
  - Lichtman–Teräväinen（arXiv:2111.08912）：$H$ 为 $\log$ 幂、Chowla 型；
  - MRT II（arXiv:1712.08840）：divisor 相关，短范围。
- 检索只覆盖了网页搜索的两次查询，没有逐篇查 MathSciNet 或 zbMATH。**新颖性判断应当视为初步的。**

参考链接：
- https://arxiv.org/abs/1712.08840
- https://www.math.mcgill.ca/radziwill/correlations.pdf
- https://arxiv.org/abs/2111.08912
- https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/plms.12181
