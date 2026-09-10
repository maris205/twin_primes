# 迁移与复现说明

## 迁移边界

来源是原仓库已提交版本 `02d51d372e9c95ffc2ed36727829363a32cec030`。
`provenance/MIGRATION_SOURCE.json` 列出全部选定主线文件的路径、Git blob、SHA-256、大小和模式。
论文目录、科学代码、实验数据与原始评审逐字节保留 Git 中的规范内容；原工作区仅有 CRLF/LF
表示差异的文件另有记录。没有拷贝未跟踪缓存、环境、密钥、RH 项目目录或 RH 代理配置。

新 README、AGENTS、TPC 专属索引及其维护代码是显式的迁移适配；
`provenance/MIGRATION_ADAPTATIONS.json` 单独列出变更及原/新摘要。
旧交接里的日期、旧仓库提交和旧的 823 项统计作为历史记录保留；当前清单只有 420 个 TPC 目录。
早期四分支快照及各文件哈希见 `provenance/EARLY_BRANCHES.json`。

## 原始 Git 来源的保留

一些原检查器与 Markdown 转换记录直接引用旧提交 ID，不能随意重写这些哈希。
`provenance/git-objects/pack/` 因而保存真实原 Git 对象，并用清单校验。
选取范围包括检查代码/转换记录引用的已有提交、迁移基准和早期分支：保留 commit、
根/中间 tree，以及 TPC 子树、文件和必要共享根文档。共享历史 README/AGENTS 中可能含
原混合项目文字；这些是冻结的来源上下文，不是新仓库的工作入口。

这不是旧仓库完整历史：未导入无关项目文件、全部父提交或全部 refs。
需要遍历旧仓库完整提交图、全项目树和全对象数量的历史审计（例如 TPC206 的旧整库扫描）
仍需原仓库，不能把本迁移的局部对象档案当作其完全复现。各早期快照内相对链接按当时布局保留。

读取历史源时使用：

```sh
python -B tools/with_legacy_sources.py -- git show 02d51d372e9c95ffc2ed36727829363a32cec030:papers/tpc-418-c1-shell-parity-envelope/paper/main.tex
```

工具先检查对象包的大小与 SHA-256，再仅给子进程设置 `GIT_ALTERNATE_OBJECT_DIRECTORIES`。
使用真实 Git，不模拟返回值，也不永久修改 Git 配置。原本缺失的源不会被伪造补全。

## 环境与只读检查

迁移时使用 Python 3.12.3。数值工具依赖的本机版本列在 `requirements-core.txt`；
这不是所有历史论文环境均已重建的声明。建议使用独立虚拟环境。
源 Markdown 核验还需要系统命令 `pandoc`、`pdftotext`、`pdfinfo`。
归档完整性核验不需要这些转换工具或科学计算包。

```sh
python -B tools/verify_migration.py
python -B research/tpc-big-road/tpc_bridge_b_tpc418_c1_shell_parity_envelope_checker.py --check
python -O -B research/tpc-big-road/tpc_bridge_b_tpc418_c1_shell_parity_envelope_checker.py --check
python -B tools/with_legacy_sources.py -- python -B research/tpc-big-road/refresh_source_markdown_inventory.py --check
python -B tools/with_legacy_sources.py -- python -B research/tpc-big-road/check_source_markdown_batch.py --first 140 --last 418 --paper-dir tpc-207-critical-moving-hole-bdh-defect
PYTHONPATH=research/tpc-big-road python -B tools/with_legacy_sources.py -- python -B -m unittest discover -s research/tpc-big-road -p 'test_source_markdown_*.py'
```

转换检查的 PASS 只说明其明确检查到的源锁、机械转换与链接，不代表数学证明正确、
PDF 与 TeX 已全面同步或跨文档锚点全部有效。TPC418 的有限样例/证书检查不证明增长尺度估计。
请勿为了“全部重跑”直接执行历史 producer；有些默认写入结果。迁移未重写科学 expected artifacts。

## 归档策略

原版本已经跟踪的 PDF 副本、编译日志、辅助文件按原样保留，因为部分检查器与索引依赖它们。
新的缓存/环境由 `.gitignore` 排除。不要用忽略规则删掉已经归档的源文件。
本次新仓库为独立主分支；不会把混合仓库的整段 RH 历史带进新分支提交图。
