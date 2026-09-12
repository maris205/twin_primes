#!/usr/bin/env python3
"""Publish measured QA findings without altering sources or scientific claims."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from prepare_sources import VAULT,CACHE,digest

def main():
    manifest_path=VAULT/'99_维护/generated_manifest.json'
    manifest=json.loads(manifest_path.read_text())
    if manifest.get('build_incomplete'):raise ValueError('Incomplete vault')
    for relative,sha in manifest['files'].items():
        if digest(VAULT/relative)!=sha:raise ValueError('Changed generated file: '+relative)
    def put(relative,content):
        path=VAULT/relative
        data=content.encode() if isinstance(content,str) else content
        sha=hashlib.sha256(data).hexdigest()
        if path.exists() and digest(path)!=sha and manifest['files'].get(relative)!=digest(path):
            raise ValueError('Refusing to overwrite unknown QA artifact: '+relative)
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(data)
        manifest['files'][relative]=sha
    regressions=[]
    for flags in [['-B'],['-O','-B']]:
        run=subprocess.run([sys.executable,*flags,str(VAULT/'_tools/test_reader_extensions.py')],
                           capture_output=True,text=True)
        if run.returncode:raise ValueError('Reader regression failed: '+run.stderr)
        regressions.append(dict(flags=flags,returncode=run.returncode,output=run.stdout+run.stderr))
    put('99_维护/regression_results.json',json.dumps(dict(runs=regressions,scope='Reader/adaptation edge cases, not mathematical proof checks'),ensure_ascii=False,indent=2)+'\n')
    checks=json.loads((VAULT/'99_维护/validation_results.json').read_text())
    maths=json.loads((CACHE/'mathjax_report.json').read_text())
    if maths['input_sha256']!=digest(CACHE/'math_nodes.json'):
        raise ValueError('Stale MathJax report')
    put('99_维护/mathjax_results.json',json.dumps(maths,ensure_ascii=False,indent=2)+'\n')
    audits=[]
    for name,title in [('CARD_SOURCE_AUDIT_RAW.md','知识卡片来源审阅'),
                       ('CONVERSION_AUDIT_ROUND0_RAW.md','转换器首轮审阅'),
                       ('CONVERSION_AUDIT_FOLLOWUP_RAW.md','转换器修复复核'),
                       ('CONVERSION_AUDIT_FINAL_RAW.md','两项剩余问题关闭复核')]:
        path=CACHE/name
        if path.is_file():
            target='99_维护/原始审阅/'+name+'.txt'
            put(target,path.read_bytes())
            audits.append('- ['+title+'](原始审阅/'+name+'.txt)（原始文本，不改写审阅发现）')
    counts=Counter(row['conversion_status'] for row in json.loads((VAULT/'99_维护/论文清单.json').read_text()))
    unmatched=sum(p.read_text().count('> [!warning] 未匹配书目键') for p in (VAULT/'99_维护/参考文献').glob('*.md'))
    text='''# 知识库验收报告

范围：文档组织、来源完整性、导航与公式显示兼容性。**不是数学正确性或孪生素数猜想的证明认证。**

## 覆盖与导航

'''
    text+=f'''- 目录身份：{checks['paper_directories']}；机械全文：{checks['accessible_fulltexts']}；缺源目录：{checks['source_unavailable']}。
- 原有完整MD复用：{counts['REUSED_SOURCE_COMPLETE_MECHANICAL']}；本次从TeX补转：{counts['FULL_TEX_TO_MARKDOWN_MECHANICAL']}。
- 可见Markdown文档：{checks['note_count']}；已导入来源文档：{checks['adapted_notes']}，其中{len(checks.get('literal_source_fallbacks',[]))}份旧补充材料采用逐字原文保留视图，其余为适配阅读层。
- 库内有效链接：{checks['internal_links']}；实际导航错误：{len(checks['live_navigation_errors'])}；从首页无法到达的核心文档：{len(checks['unreachable_core_notes'])}。
- 原始附件散列一致：{checks['source_files_preserved']}份。PDF是原始附件，未重新编译。
- 历史来源链接例外：{checks['historical_source_link_exceptions']}项，均进入[来源链接例外](待解决来源链接.md)，没有伪造目标；“库内链接有效”不等于“原历史链接全部可恢复”。
- 原始书目未匹配键：{unmatched}项，逐项保留并警告；没有联网补造条目。
- 外部链接：{checks['external_links_not_network_checked']}次出现，未做逐条联网可用性检查。

## 公式与文字

- 适配来源正文的数学节点：{checks['math_nodes']}，数学节点序列往返核对通过。
- MathJax {maths['version']}服务端兼容性检查：{maths['totalExpressions']}次公式出现、{maths['uniqueExpressions']}个不同表达式；失败{maths['failedOccurrences']}次、涉及{maths['failedUnique']}个不同表达式。这是带明确限制的交付，不是全部公式原生显示均通过。
- 文字往返待核提示：{len(checks['adapter_text_roundtrip_warnings'])}份；Pandoc警告：{len(checks['adapter_reader_warnings'])}份。详见[机器检查结果](validation_results.json)。

逐项限制见[公式显示兼容性与原文保留视图](公式显示兼容性.md)，相应阅读页也有提示。7份原文保留视图仅涉及旧补充材料，419份论文全文仍保留正常机械阅读层。

这台服务器没有桌面Obsidian实测；MathJax服务端检查不能代替实际桌面的字体、分页、主题或插件兼容性检查。公式印刷编号以PDF为准；原有宏或源文错误不静默改写成新结论。

## 独立审阅与复现

'''
    text+='\n'.join(audits)+'\n\n'
    text+='18项专项回归在普通Python与优化模式下均通过，覆盖真实星号、verbatim边界、引用文字与属性、数学注释换行、引用限定语和嵌套代码块。详见[实测回归输出](regression_results.json)。检查通过不等于所有419份正文已被逐段人工复核。\n\n'
    text+='本次仅在独立知识库目录内生成内容；原仓库与先前中文、英文综合稿未改写，不提交、不推送、不启动新论文或实验。手写空间与已有Obsidian设置受保护。\n\n'
    text+='[完整结构检查结果](validation_results.json) · [MathJax详细结果](mathjax_results.json) · [[99_维护/使用与更新说明|使用与更新]] · [[00_开始阅读|首页]]\n'
    put('99_维护/验收报告.md',text)
    usage='99_维护/使用与更新说明.md'
    body=(VAULT/usage).read_text()
    if '<!-- QA_REBUILD_PIPELINE -->' not in body:
        body+='''

<!-- QA_REBUILD_PIPELINE -->
## 复现显示检查与保留视图

仅阅读不需要构建依赖。本次使用Python 3.12、Pandoc 2.9.2.1，以及独立工具目录中的MathJax-full 3.2.2；没有把这些环境混进原仓库。

在完成前面的准备、构建、原始Markdown附件保留后，可运行下列验收流程。`/path/to/node_modules`必须换成自己安装MathJax-full的真实目录；不要把命令退出成功等同于“全部公式显示通过”，应检查报告中的失败数量。

```sh
python -B _tools/validate_vault.py --report
node _tools/check_mathjax.cjs /path/to/node_modules
python -B _tools/apply_reading_cautions.py
python -B _tools/validate_vault.py --quick --report
node _tools/check_mathjax.cjs /path/to/node_modules
python -B _tools/write_qa_report.py
python -O -B _tools/validate_vault.py --quick
```

原文保留视图仅对出现文字往返差异的旧补充材料启用，保留原始字节附件，不猜修源公式。公式显示告警保留原始TeX并链接PDF和逐项记录，不把兼容性失败当作数学真伪判断。完整结果见[[99_维护/验收报告|验收报告]]。
'''
        put(usage,body)
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(structure=checks['status'],mathjax_failures=maths['failedOccurrences'],unmatched_citations=unmatched),ensure_ascii=False))

if __name__=='__main__':main()
