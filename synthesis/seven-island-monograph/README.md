# 孪生素数研究的七岛框架

**精确结构、解析障碍与两类桥接问题** — 中文统一研究母稿，2026-09-12。

交付版：23页，九章与两个附录；两轮内容复核及最终23页独立视觉检查已完成。

主文将分散材料按同一条问题线索组织为一篇文章，而非按原编号缩写420篇摘要。原地图作为共同坐标，原论文和研究记录作为证据。稿件没有新增 TPC 编号，也没有改动原始档案。

## 阅读入口

- [完整论文 PDF](paper/main.pdf)：正式排版、公式编号与书目。
- [完整英文版 PDF](paper-en/main.pdf)：另行排版，使用用户提供的英文原地图；[英文版说明与源文件](paper-en/README.md)。中文版保持不变。
- [七岛路线图：全分辨率原图](../../research/tpc-big-road/figures/tpc_route_cn.png)：可单独放大查看图内的小字、图例和公式；与正文复用的图片相同。
- [Markdown 阅读版](paper/main.md)：便于批注和搜索；引文键见配套书目，公式编号以 PDF 为准。
- [LaTeX 主文件](paper/main.tex)：正文按章节模块化，便于继续编辑。
- [核心来源矩阵](CORE_SOURCE_MATRIX.md)：24个核心文件的行区间、声明边界与 SHA-256；与冻结提交逐字节核对。
- [420目录检索表](SOURCE_CATALOG.md)：全目录可追溯索引。候选岛号来自字面匹配，不是420篇全文的人工数学认证。
- [写作计划](PAPER_PLAN.md)：主张—证据关系与整合范围。
- [两轮审阅与修改记录](paper/PAPER_IMPROVEMENT_LOG.md)：保留原始完整意见，不生成模拟评分。
- [外部输入核验](EXTERNAL_SOURCES.md)：经典基线与实际使用的临界双线性估计范围。
- [最终交付核查](FINAL_QA.md)：编译、字体、来源散列、逐页视觉检查及剩余限制。

## 一篇文章的主线

1. **共同问题。** 固定移位2的终点是什么；局部筛因子为什么不能直接给出素数对计数。
2. **对象与结构。** 岛③的行列式二拉回与岛④的实际出现项、守恒和带权覆盖，必须保留完整系数、掩码、顺序和归一化。
3. **解析核心。** 在同一个实际算子上，集中给出精确分解、行能量、实际系数范数与增长维数的低秩障碍。
4. **精确表示与已支付部分。** Kloosterman 完整发射不自动产生双侧短数组；一个显式分割确实支付了边界贡献，内部有符号和仍未估计。
5. **动力学与几何。** 实际移动筛事件已有 Haar 方差与几乎处处命中结论；指定种子0仍需回接。Hénon/几何提升只作为需要精确附接的辅助路线。
6. **两桥账本。** 图像 Bridge A 包含解析 Gate A、Gate B；图像 Bridge B 是指定种子动力学桥。两者都未因这次写作而闭合。

正文共九章，另有两个短附录。重写的主要证明来自选定原稿和未编号证明包，不主张首次发现或最优性。

## 稿件定位

这是可继续发展为外部论文的**研究综合母稿**，不是孪生素数猜想的证明，也不是已完成查新、作者确认和期刊定位的投稿终稿。

当前数学边界：全标量的实际系数敏感固定幂次节省、独立的解析 Gate A、指定种子0的无限命中，以及相关生产级结构附接仍未完成。范数方法障碍不是实际标量下界，也不排除所有其他方法。

目录标签与源散列只承担检索及来源保真；有限检查、编译 PASS 或审稿意见均不认证全部历史数学。

## 重建与检查

依赖：Python 3、XeLaTeX、ctex/Fandol 字体、latexmk、BibTeX、Poppler（pdfinfo/pdftotext/pdffonts）及 Pandoc。此稿采用数学长文版式，不使用写作技能的默认 ICLR 九页限制。

从仓库根目录运行：

```sh
python -B synthesis/seven-island-monograph/tools/build_catalog.py
python -B synthesis/seven-island-monograph/tools/build_source_matrix.py
python -B synthesis/seven-island-monograph/tools/build_paper.py
python -B synthesis/seven-island-monograph/tools/check_paper.py
```

构建在独立临时目录中进行，保留本目录的编译日志与 PDF，不清理或覆盖旧论文。PDF 日期元数据随编译改变，所以跨机器复编不要求 PDF 二进制散列不变。来源文件散列必须匹配。

`paper/main_round0_original.pdf`、`paper/main_round1.pdf`、`paper/main_round2.pdf` 保存审稿修订快照；审阅意见与落实记录另列于配套改进日志。内部源资料的未确认日期写作 `n.d.`，不据编号猜测出版年份。

所有更改仅保存在此新目录；未提交、未推送。
