# Twin Primes · 孪生素数研究档案

本仓库独立整理孪生素数（TPC）研究的论文、代码、实验结果、推导、评审和研究交接。
从原混合仓库已提交版本 `02d51d372e9c95ffc2ed36727829363a32cec030`
迁移，保留相关原始文件与历史源哈希，不包含 RH 项目的工作目录或代理配置。

**这是一份持续研究档案，不是孪生素数猜想的证明。** 正式编号止于 TPC418；
后续未编号研究、成立范围、未解决的算术估计和停止条件以交接文档为准。

## 从哪里开始

- [本轮新增 Wiki、中文／英文综合稿及历次修订](docs/EDITORIAL_MATERIALS.md)
- [Obsidian Wiki 阅读首页](reading/tpc_obsidian_vault/00_开始阅读.md)
- [AI 辅助 TPC 研究框架 v0.3：论文、源码与后续规划](synthesis/ai-framework-v0.3/README.md)
- [当前研究状态与下一步条件](TPC_HANDOFF.md)
- [最新 physical-return 研究及评审汇总](research/tpc-big-road/research-rounds/2026-09-09-physical-return-loop/README.md)
- [全部论文资料索引：MD / TeX / PDF](research/tpc-big-road/PAPER_MATERIALS_LINKS.md)
- [完整性与阅读状态清单](research/tpc-big-road/PAPER_MATERIALS_INDEX.md)
- [路线图与桥接概念说明](research/tpc-big-road/TPC_ISLAND_MAP_GUIDE.md)
- [研究历史总结](research/tpc-big-road/TPC_HISTORY_SUMMARY.md)
- [全文转换范围与已知限制](research/tpc-big-road/TPC_CONVERSION_BATCH_2026-09-07.md)
- [逐目录未完成事项](research/tpc-big-road/PAPER_MATERIALS_REMAINING.md)
- [迁移范围、历史源与复现说明](docs/REPRODUCIBILITY.md)
- [本次迁移验证记录](docs/MIGRATION_VALIDATION.md)

## 内容组织

| 路径 | 内容 |
|---|---|
| `papers/tpc-*` | 420 个原有目录：编号 TPC1–418、额外的 TPC207 缺源目录，以及 MVP 原型。保留原路径、TeX、PDF、代码、数据、推导、评审和必要构建记录。 |
| `research/tpc-big-road/` | 研究路线、桥接检查、文献记录、转换工具、索引、未编号研究与评审。 |
| `legacy/branches/` | 四个早期分支的 TPC 专属文件快照，包含重命名前的早期项目。仅作历史材料，不能替代当前主线。 |
| `provenance/` | 原文件 SHA-256 清单、早期分支来源，以及可验证的原始 Git 对象包。 |
| `tools/` | 迁移核验和历史源读取工具；不生成新的数学结论。 |

当前 420 个目录中：279 个有完整的机械源文 Markdown 阅读层，140 个仍为局部材料或笔记，
1 个原稿不可访问；独立全文语义审核等级 `reliable-full-md` 为 0。
这些是资料维护指标，不是定理成立比例。目录内历史错误和范围限定原样保留。

`AUTO_REVIEW.md`、`PROOF_PACKAGE.md`、`DERIVATION_PACKAGE.md` 等根目录文件保留原研究上下文。
`TPC_COMPASS.md` 和 `codex_prompt.md` 是历史路线/工作记录，使用时应先读最新交接，
不能把旧批次指令当作当前继续研究的授权。

## 获取与核验

```sh
git clone git@github.com:maris205/twin_primes.git
cd twin_primes
python -B tools/verify_migration.py
```

基础归档核验只需 Python 标准库和 Git；数值检查另需科学计算依赖，全文转换核验另需
Pandoc 与 Poppler。详细命令、环境和历史检查器的边界见[复现说明](docs/REPRODUCIBILITY.md)。
历史对象包随普通 Git 克隆取得，不依赖本机原仓库或 Git LFS。
