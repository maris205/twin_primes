# 奇偶墙路线（parity-wall route）

这个目录收录孪生素数奇偶墙的阶段式探索：从条件通路"GEH + PND_log ⟹ TPC"出发，一阶段一阶段地试探通往孪生素数猜想（TPC）的路，记录哪些路不通、为什么不通、墙到底在哪里。共 33 个阶段。

- **在线路线图（无需登录）：** https://claude.ai/artifact/R4YKS4ABCmSkbRC1ZMFQSJ
  - 本地副本：[`route/roadmap.html`](route/roadmap.html)，可直接用浏览器打开。
- **一页纸总结（第 20–33 阶段）：** [`route/WALL.md`](route/WALL.md)
- **假设账本（H 系列与各阶段判决）：** [`route/BOLD_HYPOTHESES.md`](route/BOLD_HYPOTHESES.md)

所有结论都由 AI 辅助得出（Claude，Anthropic），并逐条标明是**定理**、**分析**还是**数值**。这里没有证明或否证孪生素数猜想。

## 目录结构

| 路径 | 内容 |
|---|---|
| `route/` | 各阶段报告 `STAGE*.md`、脚本 `stage*.py`、数值结果 `*.json` / `*.jsonl`、路线图 `roadmap.html` |
| `route/mrt833/` | 第十二阶段子课题：MRT 8/33 指数与猜想 A |
| `paper_parity_v1.3/` | 论文 *Parity and the twin prime conjecture* v1.3（第一到十九阶段的成果），DOI [10.5281/zenodo.23736249](https://doi.org/10.5281/zenodo.23736249)，概念 DOI [10.5281/zenodo.23687596](https://doi.org/10.5281/zenodo.23687596) |
| `paper_wall/` | 第二篇论文：第二十到三十三阶段（墙的完整刻画） |

## 主要结论（第 20–33 阶段）

**墙的位置：**
- 孪生只卡在一个点上：间隙固定为 2、两端都是 $x^\eta$-粗糙数、问 $\lambda(n)\lambda(n+2)$ 的符号。
- 在这个点上，极端赝品（所有粗糙对上 $\lambda\lambda=-1$，可取为完全乘性的 $\chi_3$ 或 $\chi_4$）满足全部筛法公理，并且与 $\lambda$ 的伪装距离有界。
- 放宽任何一个条件，问题都是已知定理：
  - 间隙改为析取：Pintz 2010；
  - 间隙改为平均：MRT 2019；
  - 粗糙度改为固定 $z$：由 Tao 2016 推出。

**最弱的目标** $\mathrm E(\eta)$：只要存在一对偶类粗糙孪生。它被赝品挡住（第 27、28 阶段）。

**严格结果：**

| 编号 | 内容 |
|---|---|
| 定理 27.1 | 渐近精确刚性 ⟹ $\mathrm E(\eta)$ |
| 定理 27.2（族引理） | 多项式族给出的关系向量之和恒为零 |
| 命题 28.1 | 固定 $z$ 时 $\mathrm E$ 成立 |
| 定理 31.1 | 粗糙伸缩恒等式（精确） |
| 命题 31.2 | 赝品分解：扩张机制中奇偶只从均值项进来 |
| 引理 33.1 | 抽样迹恒等式 |
| 定理 33.2、命题 33.3 | 迹方法的对数损失，且这个损失是真实的 |
| 定理 33.4 | 剪枝模板（基于 Le–Levina–Vershynin） |
| 命题 33.5 | 粗糙图中的孪生矩形 |

**扩张机制的终点：**
- 粗糙度轴 $\rho=\log\log z/\log\log x$ 上，上限为 $\rho<1/2$（论文 v1.3 的定理 A）。
- 数值上，谱范数按稀疏尺度 $\sqrt{d_R}$ 增长，说明这个上限很可能是锐的（第 32 阶段）。
- 孪生需要 $\rho=1$。

## 复现

- 脚本用 Python 3.10 加 numpy，在 `route/` 目录下运行（它们会 `from bilinear_probe import ...`）。
- 用法写在每个脚本开头的 docstring 里，例如：

```bash
cd route
python3 stage32_sparse_spectrum.py 1e6 11 10000 rough -3
```
