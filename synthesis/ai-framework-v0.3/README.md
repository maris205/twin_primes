# AI-assisted TPC research framework · v0.3

**A Source-Traceable Framework for AI-Assisted Research on the Twin Prime Conjecture**

Liang Wang<br>
School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430070, P.R. China<br>
wangliang.f@gmail.com

这是已完成英文 v0.3 的 Git 交付副本。论文日期为 12 September 2026，最终稿 30 页。文件原样复制，不重写论文、历史评审或验证记录；这不是新的 TPC 编号或数学研究轮次。

## 阅读与下载

- [最终论文 PDF（30 页）](edition/paper/main.pdf)
- [可独立编译的 LaTeX 源码 ZIP](edition/english_v0.3_source.zip)
- [Markdown 阅读版](edition/paper/main.md)
- [LaTeX 主文件](edition/paper/main.tex)
- [后续研究与评测规划](edition/refine-logs/EXPERIMENT_PLAN.md)及[尚未运行的实验清单](edition/refine-logs/EXPERIMENT_TRACKER.md)
- [论文 QA 报告](edition/QA_REPORT.md)及[完整审读与修改记录](edition/paper/PAPER_IMPROVEMENT_LOG.md)
- [当前仓库可导航的数学来源表](SOURCES.md)
- [保留的 v0.2 基线 PDF](edition/paper/main_round0_original.pdf)、[第一轮稿](edition/paper/main_round1.pdf)及[排版修正前的 31 页稿](edition/paper/visual_candidate_31p.pdf)

PDF SHA-256：916693565d81741756af7fcd6151a9e583b1f96a03cd50d2628149be745e0f41。源码 ZIP SHA-256：a1c73088829d00c7995cfc98e4f172e21e76c56fd988e7409a0225a33392a118。

## 在克隆后的仓库中使用

编译只需进入本目录的 edition/paper，再执行：

    latexmk -pdf -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex

也可以将源码 ZIP 解压到任意新目录，按照其中的 BUILD_SOURCE.md 编译。该 ZIP 不依赖原工作区、Wiki 或旧版本目录。

为保持归档副本不变，推荐在 ZIP 的解压副本中编译。在仓库内覆盖 PDF 会使原有哈希及视觉检查记录失效。

在本目录运行只读归档核验：

    python -B tools/verify_bundle.py
    python -O -B tools/verify_bundle.py

它核对全部交付文件、PDF 与源码包、24 项仓库来源及已有审读记录的哈希关联，不生成或重新认证数学结论。

## 归档边界与旧路径

edition/ 是原工作区交付目录的逐文件字节快照；[文件清单](IMPORT_MANIFEST.json)用于核对。原来的 README、来源导航、日志和验证脚本保留当时的相对路径及绝对临时目录，因此它们不全是克隆后可执行的入口。请优先使用本页、SOURCES.md 和上面的独立编译命令。

首次推送本版本时仅包含 v0.3。随后已补齐 [Obsidian Wiki](../../reading/README.md)、[英文 v0.2](../wiki-informed-english-v0.2/README.md)和[原综合稿](../seven-island-monograph/README.md)，统一说明见[相关新增资料总入口](../../docs/EDITORIAL_MATERIALS.md)。edition/ 内的旧路径仍按原始快照保留；其工作区检查器依赖当时的布局及临时渲染图片，不能直接当作克隆环境的核验入口。

现有数学来源直接链接到本仓库的 papers/ 和 research/ 等原始路径；Wiki 的资源规模与显示限制仍以论文所引用的原报告为准，没有在这次推送中重跑或扩大认证。

框架的 AI 效果尚未实验验证，研究计划中的全部试验仍为 NOT_RUN。编译成功、归档核验或 Git 推送均不意味着孪生素数猜想得到证明。
