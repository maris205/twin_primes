# arXiv 投稿包与填表信息（v1.3，2026-10-29）

## 1. 上传文件

**上传 [arxiv_submission.tar.gz](arxiv_submission.tar.gz)。** 包内共 5 个文件：

| 文件 | 说明 |
|---|---|
| `main.tex` | 主文件。人名中的重音字母已转成 LaTeX 写法（如 `P{\'o}lya`），全文为纯 ASCII；日期行去掉了 "Draft" |
| `main.bbl` | 预先生成的参考文献。arXiv **不运行** BibTeX，所以必须附上 |
| `roadmap.tex` | 图 1（路线图），TikZ，由 `\input{roadmap}` 引入 |
| `ai_workflow.tex` | 附录 D（AI 辅助的工作流程），由 `\input{ai_workflow}` 引入 |
| `exploration_map.tex` | 图 2（探索路线图与 H 系列账本配套的英文图），TikZ，由附录 D.5 中的 `\input{exploration_map}` 引入 |

**本地已在干净目录中模拟 arXiv 编译：**
- 只用这 5 个文件，pdflatex 编译 3 遍，不运行 BibTeX；
- 结果为 50 页，没有错误，没有未定义的引用或文献；
- 重音字母（Lü、Matomäki、Pólya、Teräväinen、Radziwiłł）都正确显示。v1.0 包中 `P{'o}lya` 漏掉了反斜杠，v1.1 已修正；包现在由 `make_arxiv.py` 生成。

只用到标准宏包：amsart、amsmath、amssymb、amsthm、booktabs、float、tikz、geometry、hyperref。

**有 21 处 overfull hbox。** 这是排版上的小问题，不影响编译，arXiv 也会接受。如果要求更整洁，可以在终稿时处理。

## 2. 填表信息（直接复制）

- **Title：** Why expansion methods for Chowla do not reach twin primes: a method-limitation theorem and an explicit parity compiler
- **Authors：** Liang Wang
- **Primary category：** math.NT（Number Theory）
- **MSC classes：** 11N35 (Primary); 11N05, 11N36, 11N37 (Secondary)
- **Comments：** `50 pages, 2 figures. Earlier versions on Zenodo, DOI 10.5281/zenodo.23687596. Prepared with substantial AI assistance; see Appendix D.`
- **License：** 建议选 CC BY 4.0，与 Zenodo 一致。
- **Abstract：** 复制 [arxiv_abstract.txt](arxiv_abstract.txt)。纯文本，1916 字符，上限是 1920。v1.2 把绝对值障碍那句改为"we prove"（命题 7.8）。v1.1 把 t-天花板改为 0.676，并新增两句，概括第 7 节（移位密度 1/6，以及双线性/绝对值障碍）。

## 3. 提交前需要你决定或注意的事

1. **背书（endorsement）。** 如果这是你第一次向 math.NT 投稿，arXiv 可能要求一位 math.NT 作者为你背书。可以请第 4 节的审读人顺带帮忙。
2. **AI 使用的披露。** arXiv 的政策是 AI 不能列为作者，但应当披露使用情况。附录 D 和 Comments 字段已经做到这一点。
3. **作者信息。** 论文中的单位和邮箱是 HUST 自动化学院与 wangliang.f@gmail.com。请确认这是你希望公开的。
4. **时机。** 建议先请专家看过 [REFEREE_QUESTIONS.md](REFEREE_QUESTIONS.md) 中的问题，至少看过定理 4.1 与定理 E 的部分，再挂 arXiv。arXiv 的版本可以更新，但第一印象很难改。
5. **由你自己提交。** 提交、接受协议条款都需要登录你的 arXiv 账户。这一步我不代办。

## 4. 给审读人的材料

- [REFEREE_QUESTIONS.md](REFEREE_QUESTIONS.md)：一页纸的具体问题清单，英文，按定理编号组织；
- 论文 PDF：Zenodo v0.7，或本地的 `main.pdf`。
