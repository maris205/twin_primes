# 本轮新增 TPC 资料总入口

本次补齐 Wiki、原始中文／英文综合稿和 Wiki 驱动的英文 v0.2；已经提交的 AI 框架 v0.3 同时保留。目录名表示资料版本，不是新的 TPC 论文编号。

| 资料 | 当前仓库入口 | 内容 |
|---|---|---|
| Obsidian Wiki | [阅读说明](../reading/README.md)、[Wiki 首页](../reading/tpc_obsidian_vault/00_开始阅读.md) | 419 份机械全文、420 个目录入口、14 张知识卡片、全文附件、来源定位、转换工具及验收记录。 |
| 原始综合稿 | [总入口](../synthesis/seven-island-monograph/README.md)、[中文 PDF](../synthesis/seven-island-monograph/paper/main.pdf)、[早期英文 PDF](../synthesis/seven-island-monograph/paper-en/main.pdf) | 原先尚未跟踪的综合稿、来源目录、证明叙述、原始审阅、TeX 与 PDF 版本。 |
| Wiki-informed English v0.2 | [版本入口](../synthesis/wiki-informed-english-v0.2/README.md)、[25 页 PDF](../synthesis/wiki-informed-english-v0.2/edition/paper/main.pdf)、[源码 ZIP](../synthesis/wiki-informed-english-v0.2/edition/english_v0.2_source.zip) | 基于 Wiki 改进的英文版本及完整审读、保留和排版记录。 |
| AI framework v0.3 | [版本入口](../synthesis/ai-framework-v0.3/README.md)、[30 页 PDF](../synthesis/ai-framework-v0.3/edition/paper/main.pdf)、[后续规划](../synthesis/ai-framework-v0.3/edition/refine-logs/EXPERIMENT_PLAN.md) | 作者署名、AI 框架定位、研究规划、源码及两轮审读；之前已推送。 |

## 保存方式

原工作区内容不移动、不改写。Wiki 和 v0.2 复制进仓库；原综合稿保持原路径后纳入 Git。所有正式资料按逐文件 SHA-256 核验，清单见 [EDITORIAL_MATERIALS_MANIFEST.json](EDITORIAL_MATERIALS_MANIFEST.json)。

仅排除可再生成的 .build、Python/Jupyter 等本机缓存，没有删除本地副本。Wiki 的四份原始审读报告已逐字保留在 99_维护/原始审阅；原综合稿的两个 Jupyter PDF 检查点与各自正式 PDF 字节相同，对应关系写入清单。没有上传环境、依赖安装目录、会话存档或无关 RH 项目。

已经生成的源清单、验收报告、原始评审、日志和图像哈希记录保持原样。它们记录的是当时的工作区及验证范围；其中的绝对临时路径和旧目录相对路径不承诺在克隆后仍然存在。本页和各版本包装入口提供当前仓库中的导航。

## 如何使用

1. 克隆仓库后，在 Obsidian 中打开 reading/tpc_obsidian_vault 文件夹。全文与附件均在其中，无需社区插件或重新转换。
2. 编译 v0.2 或 v0.3 时，优先在对应源码 ZIP 的独立解压目录中执行 BUILD_SOURCE.md 的命令，避免覆盖归档 PDF。
3. 若要重新生成 Wiki，先复制到源仓库之外，显式指定 --source，并审查新的源基线。原生成器会拒绝在源仓库内部生成，旧的默认路径不适用于内嵌布局。
4. 历史工作区验证脚本需要它们声明的旧基线和临时文件；克隆后的资料核验使用下面的新入口。

在仓库根目录运行：

    python -B tools/verify_editorial_materials.py
    python -O -B tools/verify_editorial_materials.py

如已安装 Pandoc，可重新解析全部 Wiki 内部链接：

    python -B tools/verify_editorial_materials.py --wiki-links

链接检查的缓存只写入新临时目录，不改写仓库里的 Wiki 或历史验收记录。导入核验结果保存在 [EDITORIAL_MATERIALS_VALIDATION.json](EDITORIAL_MATERIALS_VALIDATION.json)。

## 声明边界

419 份机械全文不等于 419 份完整人工证明审查。原 Wiki 验收报告记录 590 次公式显示兼容性失败，涉及 188 个表达式，并明确未做桌面 Obsidian 实测；原文、回退视图和限制说明保留。

本次只补齐 Git 归档及导航，不重跑研究实验、不增加数学结论、不更改开放问题或停止条件。AI 框架的评测仍是未来计划。
