# 新论文提纲：Why expansion methods for Chowla do not reach twin primes（v0.5，2026-10-27）

> **v1.3（已发布，2026-10-29，DOI 10.5281/zenodo.23736249，https://zenodo.org/records/23736249）：** 50 页。
> - **推论 7.9：** 有限窗口版本的绝对值障碍，要求 $T\ge4\pi(2P)^8$。注 7.10 给出 $T\asymp x$ 时的数值，并说明为什么那里证不出来。
> - **注 7.4：** 猜想 A ⟹ MRT 的指数可从 8/33 降到 7/30（条件结果）。数值支持，M ≤ 1600 时为猜想阶的 0.93–0.985 倍；无条件只能得到 1/4。
> - 参考文献 MRT19 已更正为第 I 篇（Proc. LMS 118 (2019)）。
>
> **v1.2（已发布，2026-10-28，DOI 10.5281/zenodo.23734041，https://zenodo.org/records/23734041）：** 50 页。arXiv 包同步更新，在干净目录中测试编译为 50 页，无错误。
> - **新增命题 7.8（绝对值障碍，定理）：** 对 $[P,2P]$ 中的 $k$ 个素数和任意单位模的 $a,b,c$，有 $\mathbf M|AB_bC|\ge\kappa k^2$。
> - **新增注 7.9：** 说明适用范围，并附对抗数值，最低值为 $0.53k^2$。
> - 摘要、引言、第 9 节和附录 D 相应更新；新增参考文献 Bentkus 2005。
>
> **v1.1（已发布，2026-10-28，DOI 10.5281/zenodo.23733715，https://zenodo.org/records/23733715）：** 48 页。arXiv 包同步更新，在干净目录中测试编译为 48 页，无错误；摘要 1903 字符。
> - **命题 6.19 加强：** 对任意非负权成立，指数改为 $(1-|t|)^2-t^4/2$，天花板从 0.586 提高到 0.676。
> - **新增第 7 节"Locating the barrier"：**
>   - 表 4：墙的四个坐标；
>   - 命题 7.1：GEH ⟹ de Polignac 数的下密度 ≥ 1/6；
>   - 注 7.2：模 3 赝品说明 1/6 在筛法意义下是锐的；
>   - 注 7.3：MRT 的 8/33，以及 3/13 的天花板；
>   - 表 5：奇偶来源分 5+2 类；
>   - 注 7.4：统一的双线性判据；
>   - 注 7.5：Type I 部分容易处理（由 BV 推出）；
>   - 注 7.6：七张卡 H17–H23；
>   - 注 7.7：Mellin 频率与绝对值障碍；
>   - 注 7.8：刚过平方根的大值。
> - **§1.1：** 注明 2026 年 AI 预印本声称证明了普通两点 Chowla，尚未经过评审。
> - **附录 D：** 新增 6 个脚本、账本 H10–H23 和局限说明。
> - **arXiv 包：** 修正了 v1.0 包中 `P{'o}lya` 漏掉反斜杠的问题。包现在由 `make_arxiv.py` 生成。
>
> **v1.0（已发布，2026-10-28，DOI 10.5281/zenodo.23723965，https://zenodo.org/records/23723965）：** 41 页。arXiv 包已更新到 v1.0：干净目录测试编译 41 页无错误，摘要 1901 字符。
> - 新增 §4.4：命题 4.12（移位 2、4、6 各自的成对相干）、注 4.13（三点相干超出 GEH）、命题 4.14（Polymath8b 析取）、定理 4.15（GEH + SC_ν ⟹ TPC）、注 4.16。
> - §6.3 末尾新增命题 6.24（ℤ 上没有"导数线"）和注 6.25（H9 数值）。
> - Polymath8b 的引用已对照 arXiv:1407.4897v4 核对：Thm 1.4(xii)、Thm 3.2(xii)、Lemma 3.4、Table 1、§8、Thm 1.5 / Prop 9.1。
> - 附录 C、D 的各表、H 系列账本（H9）、探索地图（H9 框）、Limitations 都已同步。
> - 备份：main_v09_backup.tex、ai_workflow_v09_backup.tex。
>
> **v0.9（已发布，2026-10-28，DOI 10.5281/zenodo.23722939，https://zenodo.org/records/23722939）：** 38 页，新增四个结果，都已写成严格陈述：
> - §4.3 推论 4.7（任意一个粗糙类都与 δ 等价）；
> - 命题 4.9 和推论 4.10（类 (2,2) 的量化形式，只用 Bombieri 定理，误差为 O(η + ε(x) + 1/log x)）；
> - §6.3 中的 t-族：定义 6.18、命题 6.19（t-天花板 |t| > 2−√2）、命题 6.21（ℓ^p 证书被 ℓ² 支配）；
> - 表 3、附录 C 的命令表、附录 D 的验证表与 H 系列账本（H8）、探索地图都已同步，Limitations 新增两条。
> - 备份：main_v08_backup.tex、ai_workflow_v08_backup.tex。arXiv 包（paper_parity/arxiv/ 和 arxiv_submission.tar.gz）已更新到 v0.9：在干净目录中测试编译为 38 页，没有错误；摘要 1863 字符。
>
> **v0.8（已发布，DOI 10.5281/zenodo.23694711，https://zenodo.org/records/23694711）：** 新增附录 D.5「探索路线图与假设账本」。
> - 图 2：英文探索路线图，按状态标注（定理 / 模型内定理 / 分析 / 数值）；
> - 表 10：H 系列账本（H1–H7）。H3 在模型内被显式见证否定（独立延拓）；H6 在 10⁸ 量级上没有相关性；
> - 代码包新增 parity_lp.py、h6_digits.py 和 make_exploration_map_tex.py。
>
> **v0.7（已发布，DOI 10.5281/zenodo.23692061）：** 新增**定理 E**（熵递减证书的方法限制，严格结果）。
> - 定义 6.12：熵递减证书，包含公理 E0–E3；
> - 引理 6.13：解耦的锐性，偏差 ≥ ⅓√(ln2·σθ)；
> - 命题 6.14：递减不等式本身的锐性，需要双指数的尺度范围；
> - 定理 E：可达粗糙度 $z\le(\log x)^{O(\varepsilon^4)}$。
>
> 天花板表因此有两行是定理。备份：`main_v06_backup.tex`。
>
> **v0.6（已发布）：** 新增 §6.3"已知机制的粗糙度天花板"。
> - 推论 6.11 是严格结果：定理 A 对 $z$ 一致成立，所以膨胀–谱证书的可达粗糙度为 $\exp(O(\sqrt{\log x}))$。
> - 注记 6.12（Tao 熵递减迭代）和注记 6.13（Lü–Wang–Wu 的论证）都标注为"对具体证明的分析"。
> - 表 3 汇总各机制；注记 6.14 给出共同障碍。
>
> **v0.5 重新定位：** 主结果改为方法限制定理（新 Theorem A，即原 Thm C）。原 Thm A（对数编译器）改称 Theorem B，作为 Bombieri–Tao 重述的显式形式；原 Thm B（两边相干）改称 Theorem C。下文第 2 节的编号仍是旧编号。

**定位：** 这是一篇创新型论文，主线是孪生素数问题的“条件归约 + 新猜想 + 方法限制”。它与 III-A（七岛路线的审计）分开写；七岛审计降为附录或单独的技术报告。

LaTeX 骨架见 [main.tex](main.tex)，参考文献见 [refs.bib](refs.bib)。各结果的来源文档列在第 2 节。

---

## 1. 一句话贡献

在 GEH 下，孪生素数猜想等价于一个**奇偶比特**的性质。本文做四件事：

1. 把这一比特写成一个精确、可数值检验的量 $\rho(X)$，并证明 $\limsup\rho>-1$ 就已足以推出孪生素数猜想；
2. 证明两边的奇偶结构只有一个**相干**的自由度；
3. 证明目前唯一成功处理对数 Chowla 的“膨胀 + 谱”方法，在**结构上无法分辨**这一比特；
4. 给出支持新猜想的数值证据。

---

## 2. 结果清单（新 / 已知，以及来源文档）

| 编号 | 结果 | 新否 | 来源 |
|---|---|---|---|
| Thm 2.1 | Bombieri 渐近筛（Tao 笔记 Theorem 1） | 已知，引用 | Bombieri 1976；Friedlander–Iwaniec 1978；Tao 2016 博客 |
| Lem 3.1 | 精确奇偶恒等式：$L^\flat=\Lambda_2^\flat\frac{1-\lambda}2$，由此 $4T=M^\flat-D_1^\flat-D_2^\flat+D_3^\flat$ | 新（初等） | route/COMPILER.md §3 |
| Lem 3.2 | 无条件上界 $\sum_b\Lambda(b)\Lambda_2(kb-2)\ll\frac k{\varphi(k)}y\log y$ | 标准 | COMPILER §4 |
| Lem 3.3 | 喂给 Bombieri 的序列满足公理（EH/GEH） | 新（技术性） | COMPILER §5 |
| **Thm A**（3.4–3.7） | GEH ⟹ $\sum\Lambda_2\Lambda_2\sim8\Pi_2x\log^2x$；单点奇偶项为 $o$；**对数平均编译器** $\sum\Lambda\Lambda/n=2\Pi_2\log X(1+\rho)+o$ | **新**（形式与证明） | COMPILER §6–9 |
| Cor 3.8 | GEH + PND$_{\log}$（$\limsup\rho>-1$）⟹ TPC | 新形式；本质是 Bombieri 的 “$\delta>0$” | COMPILER §9 |
| **Thm B**（4.1） | 两边奇偶相干：$u(s,r')=c(-1)^{s+r'}$ | **新**（由单边 Bombieri 推出） | route/L1_TEST.md |
| Prop 5.1 | Pólya 截断归一化（Mertens 悖论） | 经典 | paper_IIIA/NOVELTY_CHECK.md |
| **Prop 5.2** | **无参数耦合律**：odometer 中孪生柱集的 Haar 质量 = $2\Pi_2$（中国剩余定理）× $(e^{-\gamma}/c)^2$（Mertens）× $(\ln n)^{-2}$。由此取消了 [Wan26] 中拟合的 $k\approx12.73$：$c=\frac12$ 时恰好高估 $4e^{-2\gamma}$ 倍，Pólya 截断时恰好给出 HL | 新的识别方式（截断现象本身是经典的）；**直接回应前作审稿意见** | main.tex §5.2；route/cutoff_ratio.json |
| Conj 5.2–5.4 | RB ⟹ LRC₂ ⟹ PND$_{\log}$ | **新猜想** | route/ROUTE.md §3 |
| **Thm C**（6.3） | 方法限制：粗糙或光滑膨胀下，$\mathrm{res}_R\gtrsim\log x$ | **新** | paper_IIIA/BARRIER.md |
| §7 | 数值证据：四花样、$\rho(X)$、$(r,r')$ 因子分解、Mertens 壁垒、L4 Lanczos | 新 | route/*.json |

---

## 3. 章节结构（目标约 25–30 页）

1. **Introduction**：问题、Bombieri 的一维奇偶、本文的三个定理与新猜想；与 Chowla、Tao、HR、Pilatte 的关系。
2. **Setup**：记号，GEH，Bombieri 定理（Thm 2.1，作为黑盒，写明公理）。
3. **The compiler**：Lem 3.1–3.3，Thm 3.4–3.7（Thm A），Cor 3.8。
4. **Two-sided coherence**：Thm 4.1（Thm B）及证明；“第二参数”世界被排除。
5. **The symbolic-dynamics picture**：odometer 骨架、Pólya 截断、奇偶比特；Conj 5.2–5.4；与 Chowla/Sarnak 的关系。
6. **Limits of dilation–spectral methods**：Def 6.1，Lem 6.2，Thm 6.3（Thm C）；为何 Chowla 可以而孪生不行；熵递减的情形（启发式）。
7. **Numerical evidence**。
8. **Discussion and open problems**：熵递减的严格限制；双线性结构；$k$ 元组推广。
9. 附录：A 上界筛的细节；B GEH 的盒分解；C 数值协议与代码。

---

## 4. 写作顺序（步步为营）

1. ✅ 骨架：定理全文与证明要点已写进 main.tex（本轮）。
2. BARRIER 收尾：补筛法引理的出处与显式常数（BARRIER §6）。
3. ✅ 补全 §3 的长证明（从 COMPILER.md 搬入），以及附录 A、B（v0.2，15 页）。搬入时的修正：
   - $D_j=(1-\delta^{(j)})M^\flat$，不是 $o$。原 C2 有符号错误，所以 $\rho$ 现在包含单点项；
   - $\Lambda_2(p^aq^b)\ne0$，非无平方部分的界改为在附录 A 中按小因子分类证明；
   - Thm B 曾以 Hypothesis 4.1（H1）为条件。**v0.3 已去掉这一条件**：新增 Thm 4.1，对一般序列 $a$ 证明 Bombieri 的单边奇偶结构（Tao 笔记 (7)–(8) 只对 $\Lambda(n+2)$ 陈述，且未给证明），需要的额外条件 (U) 已对本文序列验证。现在 Thm B 只依赖 GEH，结论为 $u(s,r')=(\delta_x-1)(-1)^{s+r'}+o(1)$，模型归一化取 $2\Pi_2\nu_s\nu_{r'}x/\log^2x$；
   - Thm C 新增 (c) 并集情形。**v0.4 已重写**：
     - Def 6.1 推广为双线性形式、一般可除性系数 $c_d(n)\ge c_0$、乘性的 $F,G$，以及限制集 $X$；
     - 与 HR21、Pil23 逐条对照（表 6.1），两者都满足定义，$c_0=\tfrac12$；
     - Thm C 统一处理光滑、粗糙与混合膨胀 $d=st$：$\mathrm{res}_R\ge c_0c/(4C)\cdot\log z/(1+C'\kappa/\eta)$，与 $D$ 的光滑部分无关；
     - 新增注记：若函数携带配对条件，比较项本身就是孪生型相关，方法变成循环论证。
4. 写 §5 与 §7 的正文和表格。
5. 引言与摘要。
6. **查重**：L1/Thm B、Thm C、对数编译器 C4 在文献中是否已有。
7. 内部审读后挂 arXiv（math.NT）。
