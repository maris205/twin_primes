# Paper Improvement Log

日期：2026-09-12。对象：统一中文研究母稿；非新编号论文，非投稿认证。

## 审阅方式与范围

写作技能要求的 GPT-5.4 MCP 接口不可用，本次使用实际可用、独立于作者的只读审阅代理完成两轮内容审核，并由另一代理逐页审阅 PDF。没有模拟模型身份、分数或接受率。原始报告全文保留如下，独立文件位于 [reviews](../reviews)。

作者保留整合与编辑责任；来源核查和全文复审不意味着全部420目录的数学认证。两轮内容审阅以相同审阅者保持上下文，视觉审阅为不同审阅者。

## 修订轨迹

| 阶段 | 篇幅 | 实际结论 | 文件 |
|---|---|---|---|
| 初版 | 22页 | 完整可编译初稿，尚未完成后续内容修订 | [round0](main_round0_original.pdf) |
| 第一轮修订 | 23页 | 实施2项主要问题及10项细节修改；补齐岛①和24文件来源矩阵 | [round1](main_round1.pdf) |
| 第二轮 | 23页 | 两项主要及十项细节问题均关闭；没有识别出新的必改内容问题；随后落实视觉建议 | [round2](main_round2.pdf) |

无数值评分。ROUND2报告锁定的是round1 PDF的内容版本；之后只改了图注中的高清原图导航、目录/页眉和书目对齐，没有改变定理、证明或条件接口。最终视觉报告和散列以 FINAL_QA.md 为准。

## 已实施修复

- M1：定义有限物理块集，全部极化/条件/权重求和与边界分类共用同一合法域。
- M2：补齐V58的物理输出、导入恒等式、Gate A假设、误差和399/400参照指数；明确不是S2计数或完整TPC证明链。
- m1–m4：准确的范数上下界；实线性修补的域/值域/秩与范数；完整双线性型和损失量词；包含区间起点的几何级数定义。
- m5–m7：柱集尺度只作充分条件；种子引理独立归属；EPS/ETO/FUM与保留载体/认证非零支持的区别。
- m8–m10：删除附录未兑现的承诺；修复圈号缺字与内部书目元数据；将筛周期的实际误差与误差上界严格区分。
- 视觉：书目局部左对齐使7条underfull警告归零；参考文献加入目录；去掉易混淆的章节页眉；保持原图并提供全分辨率访问入口。

## 第一轮原始全文（含补遗）

<details>
<summary>展开ROUND1原始报告</summary>

TPC_AGENT_RESULT_V1

- review_round: `ROUND 1`
- review_scope: `independent full-manuscript content audit`
- baseline_HEAD: `d37c92b8a66bbd3d9084b1597d346429a9285302`，已核对
- manuscript: `synthesis/seven-island-monograph/paper`，中文母稿 v0.1
- files_changed: `[]`
- score: 未生成
- submission_certification: 未作出

## 总体意见

**建议完成一轮有针对性的内容修订，再进行 ROUND 2。**

本轮未发现足以推翻主要算子、实际系数范数、增长秩或 Haar 方差结论的 CRITICAL 错误。特别核查的五条高风险证明链——物理算子分解、lane 下界、增长负空间、Kloosterman 极化、Haar 协方差——在目前明确的限定范围内基本成立，且主要常数、指数和共轭方向正确。

发现 **2 项 MAJOR 问题**：一项是分块指标集缺失，导致一个实际使用的求和界按当前定义不成立；另一项是解析终端账本缺少被估计对象和条件接口，使关键阈值无法在正文内复核。另有若干 MINOR 定义、量词、来源归属和摘要性措辞问题。

这不是要求补出新的算术消去或 TPC 证明。必要修改均可通过恢复已有来源中的定义、限定条件和短推导完成。

## MAJOR 问题

### M1. 分块指标集未限制为与物理区间相交的块，导致求和界按字面为无穷

**位置：**

- [emitter.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/emitter.tex:3)，3–4、55–72 行。
- [boundary.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/boundary.tex:4)，4–7、14–26 行。
- PDF 第 14–16 页。

**问题：**

第 7 节实际构造了由全部 \(j\in\mathbb Z\) 索引、在整个实轴上满足
\[
\sum_{j\in\mathbb Z}\eta_{j,H}=1
\]
的分割。但第 6 节没有定义有限的物理块标签集，随后直接使用
\[
\sum_{b,c}\omega_{bc}\ll x/H,\qquad
\omega_{bc}=(1+|b-c|)^{-A_0}.
\]
如果 \(b,c\in\mathbb Z\)，左边由于所有对角项 \(\omega_{bb}=1\) 而发散。

同一遗漏使第 7 节“将不完全包含在 \((x/2,x)\) 内的支持标为边界块”包含了无限多个完全位于区间外的块，因此“边界支持必须包含至少一个端点，所以至多六个”并不按当前定义成立。

区间外的块不改变原算术标量，但这不能使上述无权块数或 \(\omega\)-求和自动变为有限。

**可执行修复：**

在首次使用分块时明确定义
\[
\mathcal J_x=
\{j\in\mathbb Z:
\operatorname{supp}\eta_{j,H}\cap[x/2,x]\ne\varnothing\},
\qquad
|\mathcal J_x|=O(x/H+1).
\]
此后所有 \(b,c\) 求和及条件 6.2 的统一性都限定于 \(\mathcal J_x^2\)。再定义
\[
\mathcal J_{\partial}
=\{j\in\mathcal J_x:
\operatorname{supp}\eta_{j,H}\not\subset(x/2,x)\}.
\]
这样才有 \(|\mathcal J_\partial|\le6\)，并可写出
\[
\sum_{b,c\in\mathcal J_x}(1+|b-c|)^{-A_0}
\le |\mathcal J_x|\sum_{h\in\mathbb Z}(1+|h|)^{-A_0}
\ll x/H.
\]

原始 [CONSTRUCTIVE_PARTITION_PROOF.md，S1–S2](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/research-rounds/2026-09-09-physical-return-loop/CONSTRUCTIVE_PARTITION_PROOF.md:1) 已包含这一限制。恢复即可，不涉及新研究。

**影响范围：**修复前，条件 6.2 到全标量指数界的书面证明不完整；不否定极化恒等式或边界估计的预期结论。

### M2. 解析终端账本缺失输出对象和 Gate A 的实际假设，关键阈值无法自足复核

**位置：**

- [bridges.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/bridges.tex:15)，15–28 行。
- [introduction.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/introduction.tex:13)，13–14、35–36 行。
- PDF 第 19–20 页。

**问题性质：MAJOR 自足性/接口缺口，不是发现源公式错误。**

正文列出“除以 \(x^{2/3+o(1)}\)”“误差指数 \(79/96\)”以及
\[
0<\eta<
\min\{\eta_A,\delta-1/400,419/2400\},
\]
却没有说明 \(\eta\) 是哪个量相对于哪个基准指数的节省，也没有给出 Gate A 的具体上界。

因此读者无法从正文判断：

- 为什么目标要求严格超过 \(1/400\)，而不只是 \(\delta>0\)；
- \(419/2400\) 的参照指数是什么；
- 这里的终端对象是否等于第 2 节的 \(S_2(y)\)。

“这是源契约记录，不重新证明完整上游链”的声明是正确的，但不能替代所记录契约自身的定义。

**可执行修复：**

增加一个明确标为“导入的条件接口”的短段落，恢复 V58 的：
\[
S_x^{\rm phys}:=\sum_{t\in I_x}\beta(t)w(t),
\qquad
S_x^{\rm phys}
=\frac{A_*-\mathfrak C_x+E_*}{K_*},
\]
\[
K_*=\sum_{q\in\mathcal Q}q\frac{q-2}{q-1}
=x^{2/3+o(1)},
\]
以及分别标注为假设/已导入误差的
\[
|A_*|\ll x^{1997/1200-\eta_A+o(1)},\qquad
|E_*|\ll x^{143/96+o(1)}.
\]
于是正文能直接核算三个输出指数
\[
399/400-\eta_A,\qquad 1-\delta,\qquad79/96,
\]
并说明输出为
\[
|S_x^{\rm phys}|\ll x^{399/400-\eta+o(1)}.
\]

特别注明 \(A_*\) 是标量，不是第 4 节矩阵 \(A\)；\(S_x^{\rm phys}\) 也不是 \(S_2(x)\)。完整 TPC 回接仍是另行导入、未经本稿全链审核的接口。

原始证据为 [V58 终端恒等式](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_terminal_scalar_root_and_q_transverse_split.md:63)，63–104 行，及 [条件定理 5.1](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/bridge_b_terminal_scalar_root_and_q_transverse_split.md:293)，293–330 行。

## MINOR 问题与修订建议

### m1. 范数表使用了严格意义不成立的 \(\asymp\) 记号

**位置：**[bridges.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/bridges.tex:10)，10、19 行。

“\(\|A\|\asymp Q^2\) 在对数因子内”及图注中的文字解释不应修改标准 \(\asymp\) 的含义。改为
\[
Q^2/\log Q\ll_\psi\|A\|\ll_\psi Q^2.
\]
这样准确且更短。

### m2. 实修补结论需要写出映射类型及范数定义

**位置：**[barriers.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/barriers.tex:199)，199–207 行。

实负空间构造正确，但“实线性修补保留上述障碍”没有明示修补的定义域、值域及算子范数。建议直接恢复来源中的形式：
\[
E:\mathbb R^{I_x}\to\mathbb C^{I_x},\qquad
\rank_{\mathbb R}E<k_x
\Longrightarrow
\|A-E\|_{\mathbb R^N\to\mathbb C^N}\ge\tau_x/2.
\]
否则读者可能将此误读为一般实线性映射在 \(\mathbb C^N\) 上的结论，或混用复秩。

### m3. 条件 6.2 的损失参数与双线性型缺少显式定义

**位置：**[emitter.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/emitter.tex:43)，43–74 行。

建议补充：

- “固定损失指数 \(\ell\ge0\)”及其选择顺序；
- \(\mathcal B_q(A_1,A_2)\) 的明确求和定义；
- 若允许单位乘子，注明它是否随 \(\nu\) 改变；
- 使用 \(q^{o(1)}\) 表述临界定理，或说明先固定严格余量，再选择充分小的 \(\epsilon\)。

目前指数计算是对的，但接口定义不宜依赖读者猜测。

### m4. 常向量证明中的 \(G_m\) 未定义，区间起点的处理略去得过多

**位置：**[barriers.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/barriers.tex:90)，90–100 行。

建议增加来源已有的两行：
\[
I_x=\{a+1,\ldots,a+N\},\qquad
G_m(y)=\sum_{k=0}^{m-1}e(ky),
\]
\[
S_j(\alpha)
=e(\alpha(a+j))
\bigl(G_m(\alpha q)+\mathbf1_{j\le s}e(\alpha mq)\bigr).
\]
这会明确“共同中心”的来源，并防止误认为物理区间从零开始或余类数目相同。

### m5. 指定柱集条件的“只在”措辞过强

**位置：**[dynamics.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/dynamics.tex:85)，85 行。

当前“已知方差界只在 \(q_N=o(N/\log^4N)\) 时自动支付方差项”容易被理解为必要性结论。

建议改为：
> 已知 \(V_N\ll\sqrt N\) 保证：若 \(q_N=o(N/\log^4N)\)，则 \(\sqrt{q_N}V_N=o(A_N)\)。

这只是现有上界的一条充分推论。若仅要求占据一个小的固定比例，适当常数下的 \(q_N\asymp N/\log^4N\) 也不能被这句话排除。

### m6. 柱集回接命题需要单独归属其实际来源

**位置：**

- [dynamics.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/dynamics.tex:63)，63–88 行。
- [provenance.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/provenance.tex:11)，11–13 行。

命题 8.2 的证明正确，也确实已有来源：它出现在 [recon-distinguished-seed.md](/root/autodl-tmp/math_research3/twin_primes/research/tpc-big-road/research-rounds/2026-09-09-multi-agent-recon/agent-reports/recon-distinguished-seed.md:78)，78–102 行。

它不是 README 中 Haar 方差定理本身，也不是复制删除文件的结论。请将这条归属交给父会话的来源矩阵，并在正文或书目增加定位。这样避免把既有未编号结果呈现成母稿中新提出的路线。

### m7. H1 的缩略标签和支持类型仍不足以独立阅读

**位置：**[structure.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/structure.tex:63)，63–75 行；[arithmetic.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/arithmetic.tex:22)，22 行。

建议：

- 定义 \(\mathsf{EPS}\) 的含义；
- 明示非软域包含 eligible-tail 与 frontier 两类；
- 区分“保留的出现项载体”和“系数已认证非零的 active support”；
- 将表中“恰好一次覆盖”改为“保留重数的精确带权重组”。

后一修改尤其重要：H1 允许一列分裂成多条带符号/复权边，并不是每个对象只出现一次。

### m8. 附录内容与导论承诺不一致

**位置：**[introduction.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/introduction.tex:26)，26 行；[models.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/models.tex:1)，全节。

导论称早期有限证书和后续模型增长结果“保留在附录的对象对照中”，但附录实际只有完整 Kloosterman 矩阵恒等式和一般范围说明，没有这样的对照。

不必新增大量历史材料。可将承诺改成“保留在配套索引中；附录说明其证据边界”，并准确说明模型增长定理未在本文展开。

### m9. PDF 文本中的圈号缺字属于呈现问题，不是数学问题

读取的 `main.txt` 中，目录及部分节标题把岛号提取为 `�`。已观察到父会话正在修改相关字体声明，因此不将其作为内容阻断项；交由父会话在最终 PDF 文本/视觉检查中确认即可。

另外，书目标题应保护 `{Kloosterman}`、`{Liouville}`、`{CRT}`、`{TPC127}` 等大小写。内部文献缺年份产生的“`, .`”可一并清理。

## 重点证明核查结果

### 1. 物理算子分解：未发现实质错误

[operator.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/operator.tex:29)，29–93 行。

逐项核对得到：

- 外层 \(q\) 已正确包含在矩阵系数中；
- 两侧单位掩码及非对角删除均保留；
- \[
  F_q-S_q=r_qr_q^*/(q-1)
  \]
  的三种余类情形正确；
- 非负 Fourier 轮廓与酉共轭积分确实保持正半定序；
- 删除对角量为 \(a_q(q-2)\mathbf1_{q\nmid n}\)。

允许非偶轮廓、允许复 Hermitian 核，以及“不把混合标量改为实部”的限定均正确。

### 2. lane 范数及范数方法障碍：未发现实质错误

[barriers.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/barriers.tex:68)，68–153 行。

- 混合主项二阶矩的非负 Euler 展开合法，不依赖与 \(\Lambda\) 的未证正交性。
- 半素数 \(n=pr\) 的两个素因子均大于 \(U\)，且 \(p<r\)，故 \(\beta(n)=-1\) 且不重复计数。
- 使用普通二倍区间 PNT，未偷换成短区间或移动算术级数 PNT。
- \[
  \int_{2/5}^{9/20}\frac{da}{a(1-a)}=\log(27/22)
  \]
  及最终常数 \(\frac34\sqrt{\log(27/22)}\) 正确。
- 对归一化范数乘积的下界，是“上界表达式的下界”，正文没有误称为 \(|\mathfrak C_x|\) 的下界。

### 3. 增长秩：复证明成立，实版本仅需补齐表述

[barriers.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/barriers.tex:155)，155–207 行。

检查了频带宽度、正压缩迹界和逐点对角下界。关键数值
\[
2(\pi+1)^2<35
\]
确实允许最终丢弃至多 35 维。维数展开
\[
k_x=Q^2/4-x^{11/32}+O(1)
\]
正确。非 Hermitian 低秩修补通过核交集处理也成立。

正文正确避免了“整个低频带都负”和“复谱空间自动是实空间”这两种过强结论。

### 4. Kloosterman 发射与极化：共轭和方向正确

[emitter.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/emitter.tex:5)，5–41 行。

按 \(\langle f,g\rangle=\sum\overline f g\) 展开，使用
\[
a^{(j)}=f+i^jg,\qquad \frac14\sum_j i^jQ(a^{(j)})
\]
选出的是 \(\langle g,Tf\rangle\)。这里 \(f=\eta_b\beta\)、\(g=\eta_cw\)，正好给出所需的 \(w\)-左、\(\beta\)-右顺序。

有限 Fourier 反演、Parseval、\(d_j(q)\) 的对角系数以及完整矩阵
\[
\mathsf K\mathsf K^*=q^2I-(q+1)\mathbf J
\]
均一致。

另核对了公开原始定理：Blomer–Pascadi 定理 1.1 接受指定整数区间上的任意复数组，在临界长度给出 \(q^{31/32+o(1)}\) 范数因子；正文没有将它直接用于长度 \(q-1\) 的完整数组。此引用范围正确。[原始定理 1.1](https://arxiv.org/html/2607.24311v1#Thmtheorem1)

### 5. Haar 协方差及 \(O(N)\) 方差：未发现实质错误

[dynamics.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/dynamics.tex:17)，17–61 行。

逐一核对了 \(p=2,3\) 的特殊局部因子及 \(p\ge5\) 的碰撞公式。展开系数和、CRT 区间计数误差、Abel 求和顺序均正确。尤其
\[
\alpha_m^2D(y_m)=1/6\qquad(y_m\ge3)
\]
准确地消除了粗糙的对数损失。

这里控制的是每个 \(m\) 的**带符号分组协方差和**，不是逐对协方差绝对值总和；正文未作这一非法替换。平方子序列 Borel–Cantelli 及单调延伸也成立。指定种子 \(0\) 的缺口保留正确。

## ROUND 2 建议复核清单

1. 有限物理块集是否同时进入极化、条件 6.2、边界分类和块权求和。
2. 终端输出是否明确为 \(S_x^{\rm phys}\)，并给出参照指数 \(399/400\)。
3. 实线性修补是否写清映射空间与范数。
4. 条件附接的 \(\ell\)、数组区间、单位乘子和统一性是否完整。
5. 柱集命题来源是否与 Haar 方差来源分开记录。
6. 表格及总结是否仍严格区分实际系数恒等式、条件接口、方法障碍和未证算术节省。

## 已审阅范围与限制

已完整读取：

- `PAPER_PLAN.md`；
- `paper/main.tex`、`math_commands.tex`、`references.bib`；
- 全部 12 个包含文件：`abstract`、`introduction`、`arithmetic`、`structure`、`operator`、`barriers`、`emitter`、`boundary`、`dynamics`、`bridges`、`models`、`provenance`；
- `paper/main.txt` 全文，对应所给 22 页母稿；
- 核心原始算子、lane、增长秩、实见证、发射、单侧支撑、边界、Haar 方差、交织及终端接口来源；结构部分结合上一轮已读的原始 TeX 复核；
- Blomer–Pascadi 原始定理陈述，未重新审核该外部论文完整证明。

本轮没有执行生成器、编译、实验、git 修改或网络上传；没有改动任何文件。父会话并行进行的来源矩阵和 PDF 布局工作不计入本人的完成范围。结论仅针对实际读取的 v0.1 内容，不认证未来修订版、全部历史文献或 TPC 证明。

`files_changed=[]`

TPC_AGENT_RESULT_V1 — ROUND 1 内容审核补遗

reviewed_scope: 最新 `arithmetic.tex` 全文、`abstract.tex`、`introduction.tex`、`bridges.tex` 的相关修改，以及 `main.tex` 的字体/目录设置；对照 TPC1 原始证明与新增 `archive1` 书目项。  
baseline_HEAD: `d37c92b8a66bbd3d9084b1597d346429a9285302`，仍一致。  
files_changed: `[]`

**本轮内容审核已完成。新增岛①内容数学上成立，没有新增 CRITICAL 或 MAJOR 问题；有一处应修正的 MINOR 逻辑措辞。** 本补遗与先前完整 ROUND 1 报告共同构成本轮意见，不替代原报告。

### 新增岛①内容：核查通过，保留一个措辞修正

[arithmetic.tex 第 11–40 行](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/arithmetic.tex:11) 正确重述了：

- 完整周期 CRT 乘积；
- 固定可容许移位集的归一化 Euler 乘积收敛；
- 固定移位二的局部因子 \(2C_2\)；
- \(Y_X=\sqrt{X+h_{\max}}\)、\(Y_X<n\le X\) 上的逐点素性识别；
- 周期截断误差上界 \(P_y+1\)，以及该上界在素性识别尺度失效。

这些内容与 TPC1 原文的 140–168、203–227、244–266、652–684 行一致。正文明确区分了“逐点识别”和“计数估计”，没有将局部奇异级数变成素数对渐近式，也没有宣称所有筛方法不可能。

**新增 MINOR m10：不要把误差上界失效写成实际误差的下界。**

位置：[arithmetic.tex 第 38–39 行](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/arithmetic.tex:38)。

当前文字：
> 在精确识别尺度上这个误差远大于主项。

证明得到的是**所给误差上界**远大于比较尺度，未证明实际误差如此大。建议将这两行改为：

> 当 \(P_y=o(X\rho_y^r)\) 时，上述周期截断界保证归一化误差趋于零；而在精确识别尺度 \(y=Y_X\) 上，素数定理给出 \(\log P_{Y_X}\sim\sqrt X\)，故这一误差上界不能提供所需的相对误差控制。

同时建议第 12–13 行显式写明 \(y\ge2\)、\(\mathcal H\subset\mathbb Z\) 为固定有限非空移位集，并在端点段注明 \(X\to\infty\)。这些是定义完整性补充，不改变结论。

### 已核实关闭或部分关闭的原报告事项

| 原编号 | 最新状态 |
|---|---|
| **m1：算子范数表的 \(\asymp\) 误用** | **已关闭。** 最新表格明确写为 \(Q^2/\log Q\ll\|A\|\ll Q^2\)，图注也正确保留对数差距。 |
| **m7：“恰好一次覆盖”措辞** | **该子项已关闭。** 最新表格改为“逐系数守恒”，与带权、多路径重组相容。EPS 等定义及支持类型区分的其余建议仍保留。 |
| **m8：附录对象对照承诺不实** | **已关闭。** 最新导论改为证据类型区分，与现有附录相符。 |
| **m9：圈号字体** | 已确认 TeX 加入 `xeCJK` 字符类设置；最终 PDF 是否正确由父会话编译和检查确认，本次不作渲染认证。 |

### 最新摘要与导论：没有新增过度主张

[abstract.tex](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/abstract.tex:1) 现在定义了 \(Q=x^{1/3}\)，并准确写出 Haar 线性方差与几乎处处无限命中的正面结果，同时保留指定种子 \(0\) 的未证条件。

[introduction.tex 第 26 行](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/sections/introduction.tex:26) 的对应补充也准确。这两项改动使综整稿不再只强调动力学缺口而遗漏已证的度量结果，且没有把它提升为指定算术轨道结论。

### ROUND 1 最终状态

原完整报告的两项 MAJOR 意见仍然保留：

1. **M1：**明确有限物理块标签集，使边界块计数和 \(\sum_{b,c}\omega_{bc}\ll x/H\) 有合法求和域。
2. **M2：**补齐导入的终端输出对象、Gate A 假设及参照指数，使 \(1/400\) 和 \(419/2400\) 可在正文复核。

其余未被本补遗明确关闭的意见仍按原报告处理。主要五条高风险证明链的正面核查结论不变。

这是 **ROUND 1 的 TeX 内容审核完成记录**，不是 ROUND 2、最终 PDF 验收或投稿认证。无文件修改、无生成器执行、无 git 修改或网络上传。

`files_changed=[]`

</details>

## 第二轮原始全文

<details>
<summary>展开ROUND2原始报告</summary>

## ROUND 2 独立内容复审报告

结论：ROUND 1 的两项 MAJOR 与十项 minor 均已在本轮修订中解决。在本轮读取范围内，未发现新的 CRITICAL、MAJOR 或需要强制修订的数学内容问题。这个结论仅针对当前母稿的内容与声明边界，不是投稿认证、全部历史来源认证或 TPC 证明认证。

### 1. 审阅范围

复审了最新完整 TeX 正文、附录、摘要、引言、参考文献及 24 文件核心来源矩阵，并通读最新 23 页编译稿的全文提取文本；针对新增终端接口，重新比对了 V58 的原始恒等式、误差指数与条件定理。

本轮结合 ROUND 1 的原始来源核查，检查修订及全文之间是否出现矛盾；**没有将此表述为重新完整审计了全部 24 个源文件，更没有审计全部 420 个历史目录。**

基线保持为 `d37c92b8a66bbd3d9084b1597d346429a9285302`。审阅对象为 [main.pdf](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper/main.pdf)；读取时的 SHA-256：

```text
main.pdf
95da921f425ebb831499459f14ed99aa16ff16bb85c3214a13ed46d5094a34e8

main.txt
0db5a8637bcf28e97ed25a980c25738df1bd5921526c2e459335c8dd038ecf37
```

未编译、运行生成器或生成页面渲染；逐页视觉 QA 留给主会话。

### 2. 两项 MAJOR：均已解决

**M1 — 有限分块求和域与边界标签：已解决。**

第 6.1 节在首次使用时定义
\[
\mathcal J_x=\{j:\operatorname{supp}\eta_{j,H}\cap[x/2,x]\ne\varnothing\},
\qquad |\mathcal J_x|=O(x/H+1),
\]
并将所有有序块对限制在 \(\mathcal J_x^2\)。条件 6.2 后的求和现在合法：
\[
\sum_{b,c\in\mathcal J_x}(1+|b-c|)^{-A_0}
\le |\mathcal J_x|\sum_{h\in\mathbb Z}(1+|h|)^{-A_0}
\ll x/H.
\]

第 7 节也在同一有限集合内定义边界标签。边界支持必须包含物理区间至少一个端点，结合闭支持重叠数得到至多六个边界块；实际边界支持大小为 \(O(H+1)\)。因此，原先无限标签导致的求和问题已消除，边界估计的支持论证成立。

**M2 — 终端输出、归一化及 Gate A 未明确：已解决。**

第 9.1 节现在明确区分：

- 物理标量 \(S_x^{\rm phys}=\sum_{t\in I_x}\beta(t)w(t)\) 与素数对辅助量 \(S_2(x)\)；
- 源折叠复标量 \(A_*\) 与矩阵 \(A\)；
- 导入的 V58 接口与本稿自行证明的结果。

重新比对 V58 后，以下接口及误差一致：
\[
S_x^{\rm phys}=\frac{A_*-\mathfrak C_x+E_*}{K_*},
\quad K_*=x^{2/3+o(1)},
\quad |E_*|\ll x^{143/96+o(1)}.
\]
加入明确的 Gate A 假设后，三个输出指数确为
\[
399/400-\eta_A,\qquad 1-\delta,\qquad 79/96,
\]
对应严格余量
\[
0<\eta<\min\{\eta_A,\delta-1/400,419/2400\}.
\]

正文明确将上游接口作为导入前提，没有把这段指数推导冒充完整的上游至 TPC 独立证明链。

### 3. Minor 修订逐项结论

| 编号 | 复审结论 |
|---|---|
| m1 范数账本 | 已解决。正文与表格均保留 \(Q^2/\log Q\ll\|A\|_2\ll Q^2\) 的对数差距，没有误写成同阶渐近。 |
| m2 实秩约定 | 已解决。明确 \(E:\mathbb R^{I_x}\to\mathbb C^{I_x}\)、实像空间维数及实定义域范数；没有混用复秩。 |
| m3 双线性型及损失量词 | 已解决。明确非归一化 \(B_q\)、固定单位乘子 \(1\)、模数倍数处取零、先固定 \(\ell\ge0\)，以及严格余量与 \(\varepsilon\) 的选择顺序。 |
| m4 剩余类和定义 | 已解决。\(G_m\)、区间起点 \(a\) 及 \(S_j(\alpha)\) 的末项均已写明，共同中心估计可直接核查。 |
| m5 柱集尺度条件 | 已解决。\(q_N=o(N/\log^4N)\) 被准确表述为控制通用点值代价的充分条件，不是必要条件。 |
| m6 指定种子引理出处 | 已解决。增加独立 SEED 引文及来源矩阵条目，并保留本文的短证明。 |
| m7 EPS／ETO／FUM 与载体 | 已解决。缩写、完整非软域 \(C^{\rm ETO}\sqcup C^{\rm FUM}\)、保留出现项与认证非零的 active support 均已区分。 |
| m8 附录承诺 | 已解决。引言改为附录实际提供的证据类型区分，不再承诺不存在的对象对照。 |
| m9 字形与内部文献元数据 | 就内容及文本核查而言已解决。内部标题与未定日期的处理不再暗示未经证实的出版信息；字形及布局的最终视觉确认仍属主会话 QA。 |
| m10 周期误差与算术假设 | 已解决。加入 \(y\ge2\)、固定有限非空整数移位集及渐近条件；正确说明周期截断的“误差上界不能提供控制”，没有将其误称为实际误差下界。 |

### 4. 全文一致性复核

修订未破坏以下关键关系：

- 算子分解保留单位掩码、核的 Fourier 方向和对角删除；行能量仍是逐素数平方后求和，而非全算子的行平方。
- 负方向与系数范数结果限制的是指定范数方法，没有被转述为实际混合标量的下界。
- 完整 Kloosterman 发射仍是长度 \(q-1\) 的精确表达；四包极化、对角扣除与外层 \(q\) 的归一化相容。
- 双侧短数组条件仍明确未证。其条件性账本给出 \(\delta=1/96-\ell\)，故 \(\ell<19/2400\) 的门槛正确。
- 构造性边界估计支付的是加权边界对的集体贡献，不是内部消去，也不是任意既有分割的统一结论。
- Haar 线性方差与几乎处处无限命中保留为实际移动筛事件的正面定理；没有降格为有限模型，也没有升级为指定种子 \(0\) 的结论。

七岛／两桥坐标也保持一致：图像 Bridge A 内的 Gate A 与实际有符号全标量估计仍未完成；图像 Bridge B 的指定种子回接仍未完成。几何表示没有被用于替代这一点值义务。

### 5. 剩余事项与动作

本轮没有需要因内容缺陷而强制修改的项目，也没有发现必须重新开启 ROUND 1 问题的理由。

主会话仍需完成已安排的独立页面渲染 QA；这不影响上述内容结论，但本报告不替代视觉验收。正文列出的内部消去、Gate A、双侧附接和指定种子条件是明确披露的研究缺口，不应被当作本轮文字修订尚未完成的缺陷。

```text
round: 2
resolved: M1, M2, m1–m10
remaining_critical: none identified
remaining_major: none identified
remaining_required_content_actions: none identified
visual_QA: outside this review; parent-owned
files_changed: []
publication_or_TPC_certification: not provided
```

</details>

## 未完成的数学输入不是本次文字缺陷

实际内部有符号节省、Gate A、双侧短数组附接、指定算术种子回接及部分生产级结构接口仍未证明。本文如实保留这些条件。全文外部查新、作者/期刊确认和完整历史依赖审计不在本次完成声明内。

