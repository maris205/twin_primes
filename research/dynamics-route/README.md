# 动力学路线（dynamics route）

孪生素数研究的第二条路线：换到物理和动力学一侧。

- **起点：** 本项目最早的素数与符号动力学工作，即有限筛写成 Logistic 映射的 kneading 序列，以及 Hénon 映射与零点模型。
- **上一条路线：** [`../parity-wall-route/`](../parity-wall-route/) 的 33 个阶段，它给出了墙的完整刻画。
- **目标：** 寻找一座双向精确的桥，把粗糙对上 $\lambda(n)\lambda(n+2)$ 的信息完整地搬到动力学一侧，并且对岸有能区分 Liouville 函数与乘性赝品 $\chi_3,\chi_4$ 的定理。

**链接：**
- **在线路线图：** https://claude.ai/artifact/5UXWduxFAcN7sM3fxXjjQK
  - 本地副本：[`roadmap.html`](roadmap.html)
- **上一条路线图（奇偶墙）：** https://claude.ai/artifact/R4YKS4ABCmSkbRC1ZMFQSJ
- **上一条路线的论文：**
  - 论文一 v1.3：[10.5281/zenodo.23736249](https://doi.org/10.5281/zenodo.23736249)
  - 论文二 v1.0：[10.5281/zenodo.23766118](https://doi.org/10.5281/zenodo.23766118)

所有结论都由 AI 辅助得出（Claude，Anthropic），并逐条标明是**定理**、**分析**还是**数值**。

## 阶段

| 阶段 | 内容 | 判决 |
|---|---|---|
| 0 | [起点、入场检验与候选通道](STAGE0_START.md)：命题 0.1（只读筛编码的动力学模型是奇偶盲的）；7 条候选通道 D1–D7 | ◎ |
| 1 | [D1 加 D3 清场](STAGE1_CLEAR.md)：筛编码三分法（命题 1.1）；Mertens 因子 $e^{2\gamma}/4$（命题 1.2）；谱统计只携带对间隙平均的孪生数据（引理 1.3） | ✗ |
| 2 | [D2 Furstenberg 系统](STAGE2_FURSTENBERG.md)：加法层退化（定理 2.1）；不相交性排除不了成对随机赝品（命题 2.2）；强平稳性只排除非乘性赝品（命题 2.3） | ✗ |
| 3 | [D6 ax+b 不变量](STAGE3_AXB.md)：原始约化（引理 3.1）；二次不变量只有目标本身与伪装数据两种（定理 3.2）；缺的一环是稳健刚性（定理 3.4） | ✗ |

## 入场检验

任何新输入必须同时满足上一条路线得到的六条必要条件，见 [`../parity-wall-route/route/WALL.md`](../parity-wall-route/route/WALL.md)。尤其是：
- **第 5 条：** 钉住单个间隙 2；
- **第 6 条：** 在伪装距离有界时仍能区分 $\lambda$ 与 $\chi_3,\chi_4$。
