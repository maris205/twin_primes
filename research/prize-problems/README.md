# 公开题库路线（prize problems）

孪生素数研究的第三条路线：不再直攻 TPC、RH，而是把前两条路线磨出来的工具用到公开题库里的中等难度问题上。

- **题库：** [TheJustinSunPrize/awards](https://github.com/TheJustinSunPrize/awards)（1,072 题，大部分数论题来自 [erdosproblems.com](https://www.erdosproblems.com)）。
- **上两条路线：**
  - [`../parity-wall-route/`](../parity-wall-route/)：奇偶墙的完整刻画；
  - [`../dynamics-route/`](../dynamics-route/)：动力学语言下墙的分层，以及函数域如何绕开它。
- **可复用的工具：** 筛编码与符号序列、粗糙数、奇偶墙分析（判断一个问题是否挡在墙后）、乘性赝品、大规模数值核验。
- **奖金规则提醒：** 题库只收对原问题的完整解答，并且需要 Lean 证明；部分结果不进入奖金流程，但可以写成论文，或发到 erdosproblems.com 的讨论区。

所有结论都由 AI 辅助得出（Claude，Anthropic），并逐条标明是**定理**、**分析**还是**数值**。

**链接：**
- **在线路线图：** https://claude.ai/artifact/CPzfxMJoTjW1yYuTbNcrrd
  - 本地副本：[`roadmap.html`](roadmap.html)
- **上两条路线的论文：**
  - 论文一 v1.3：[10.5281/zenodo.23736249](https://doi.org/10.5281/zenodo.23736249)
  - 论文二 v1.0：[10.5281/zenodo.23766118](https://doi.org/10.5281/zenodo.23766118)
  - 论文三 v1.0：[10.5281/zenodo.23804621](https://doi.org/10.5281/zenodo.23804621)

## 阶段

| 阶段 | 内容 | 判决 |
|---|---|---|
| 0 | [选题](STAGE0_SELECT.md)：从 676 道开放题中筛出相关题目；首选 Erdős #854（素数阶乘既约剩余系的间隙），次选 #1139（至多两个素因子的整数的大间隙）；#854 的数值计算到 $k=11$ | ◎ |
| 1 | [#854 的严格下界与精确数据](STAGE1_GAPS.md)：覆盖判定（引理 1.1）；无条件下界 $s(k)\ge(e^\gamma/(1+e^\gamma)-o(1))p_k\approx0.640\,p_k$（定理 1.3）；0-1 整数规划精确算到 $k=26$，得到 OEIS A389839 的 14 个新项；缺失全部落在最大间隙下方 8 以内。第二问仍开放 | ◎ 部分结果 |

## 候选题

| 档 | 题库编号 | Erdős 编号 | 问题 |
|---|---|---|---|
| A | JSP-000707 | [#854](https://www.erdosproblems.com/854) | 素数阶乘既约剩余系中出现哪些间隙 |
| A | JSP-000944 | [#1139](https://www.erdosproblems.com/1139) | 至多两个素因子的整数，相邻间隙除以 $\log k$ 的上极限是否为无穷 |
| B | JSP-000742 | [#891](https://www.erdosproblems.com/891) | 长度为素数阶乘的区间中是否必有素因子较多的整数 |
| B | JSP-000804 | [#970](https://www.erdosproblems.com/970) | Jacobsthal 函数 $h(k)\ll k^2$ |
| B | JSP-000200 | [#218](https://www.erdosproblems.com/218) | 相邻素数间隙的增减模式 |
| B | JSP-000949、JSP-000416 | [#1144](https://www.erdosproblems.com/1144)、[#520](https://www.erdosproblems.com/520) | 随机乘性函数部分和的涨落 |
| B | JSP-000552、JSP-000553 | [#680](https://www.erdosproblems.com/680)、[#681](https://www.erdosproblems.com/681) | 大 $n$ 附近最小素因子较大的整数 |
