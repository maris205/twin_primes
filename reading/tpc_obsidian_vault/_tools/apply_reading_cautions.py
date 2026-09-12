#!/usr/bin/env python3
"""Make measured reading limitations visible; never guess source-math repairs."""
from collections import Counter,defaultdict
import hashlib
import json
from pathlib import Path
import re
from prepare_sources import VAULT,CACHE,digest
from build_vault import relative_link

def fence(raw,language='text'):
    mark='`'*max(3,1+max((len(m[0]) for m in re.finditer(r'`+',raw)),default=0))
    return mark+language+'\n'+raw+'\n'+mark+'\n'

def main():
    path=VAULT/'99_维护/generated_manifest.json'
    manifest=json.loads(path.read_text())
    for rel,sha in manifest['files'].items():
        if digest(VAULT/rel)!=sha:raise ValueError('Changed generated file: '+rel)
    def put(relative,data):
        if isinstance(data,str):data=data.encode()
        target=VAULT/relative;sha=hashlib.sha256(data).hexdigest()
        if target.exists() and digest(target)!=sha and manifest['files'].get(relative)!=digest(target):
            raise ValueError('Refusing to overwrite unknown file: '+relative)
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        manifest['files'][relative]=sha
    report_path='99_维护/adaptation_report.json'
    reports=json.loads((VAULT/report_path).read_text())
    math_report=json.loads((CACHE/'mathjax_report.json').read_text())
    if math_report['input_sha256']!=digest(CACHE/'math_nodes.json'):
        raise ValueError('Stale MathJax report')
    # Preserve pre-fallback machine findings, not a rewritten success story.
    for name in ['adaptation_report.json','validation_results.json']:
        origin=VAULT/'99_维护'/name
        target='99_维护/首轮检查/'+name
        if not (VAULT/target).exists():put(target,origin.read_bytes())
    target='99_维护/首轮检查/mathjax_results.json'
    if not (VAULT/target).exists():put(target,(CACHE/'mathjax_report.json').read_bytes())
    fallbacks=[]
    for row in reports:
        if row.get('literal_source_fallback') or row['text_roundtrip']:continue
        note=row['destination']
        if not note.startswith('06_研究资料/'):
            raise ValueError('A core/full-paper prose mismatch requires separate review: '+note)
        source_relative=Path(row['origin']).relative_to(Path(json.loads((CACHE/'source_baseline.json').read_text())['source']))
        original='90_附件/原始资料/'+str(source_relative)+'.txt'
        original_bytes=(VAULT/original).read_bytes()
        baseline=json.loads((CACHE/'source_baseline.json').read_text())
        if hashlib.sha256(original_bytes).hexdigest()!=baseline['files'][str(source_relative)]:
            raise ValueError('Original Markdown attachment hash mismatch')
        raw=original_bytes.decode().replace('\r\n','\n').replace('\r','\n')
        body=(VAULT/note).read_text();end=body.index('\n---\n',4)+5
        new=body[:end]+'\n> [!warning] 原文保留视图\n> 此补充材料含未规范定界的TeX或不稳定Markdown标记。自动重排的文字核对未通过，因此下面逐字保留原文（仅统一换行），不猜补符号或修正数学结论。完整论文另有正常阅读层。\n\n'
        new+='[原始Markdown字节附件]('+relative_link(original,note)+') · [[02_论文/'+row['owner']+'|论文入口]]\n\n'
        new+='# 原始补充材料\n\n'+fence(raw,'markdown')
        put(note,new)
        row.update(original_adapter_math_nodes=row['math_nodes'],math_nodes=0,
                   math_roundtrip=None,text_roundtrip=None,literal_source_fallback=True,
                   fallback_original_attachment=original,fallback_original_sha256=hashlib.sha256(original_bytes).hexdigest())
        fallbacks.append(note)
    put(report_path,json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
    all_fallbacks={r['destination'] for r in reports if r.get('literal_source_fallback')}
    nodes=json.loads((CACHE/'math_nodes.json').read_text())
    filtered=[r for r in nodes if r['note'] not in all_fallbacks]
    if len(filtered)!=len(nodes):
        old=CACHE/'math_nodes_before_literal_fallback.json'
        if not old.exists():old.write_bytes((CACHE/'math_nodes.json').read_bytes())
        (CACHE/'math_nodes.json').write_text(json.dumps(filtered,ensure_ascii=False,indent=2)+'\n')
    failures=[v for v in math_report['failures'] if v['note'] not in all_fallbacks]
    by_note=defaultdict(list)
    for item in failures:by_note[item['note']].append(item)
    lines=['# 公式显示兼容性与原文保留视图\n',
           '此处记录服务端MathJax检测的显示限制，不据报错判断数学真伪，也不静默改变原始公式。原TeX可能有效但不被MathJax支持，个别旧源也可能有自身格式错误；原PDF与原始TeX附件用于核对。\n',
           '## 旧补充材料的原文保留视图\n']
    for note in sorted(all_fallbacks):lines.append('- [['+note.removesuffix('.md')+'|'+Path(note).stem+']]：原文逐字保留，未自动重排。\n')
    lines+=['\n## 数学显示检查\n',f'仍渲染为公式的内容中，{len(failures)}次出现涉及{len(by_note)}份文档的兼容性警告。以下“序号”是该来源阅读层中的数学节点索引，不是论文印刷公式号。\n']
    for note,items in sorted(by_note.items()):
        heading='note-'+hashlib.sha256(note.encode()).hexdigest()[:16]
        lines+=['## '+heading+'\n','[['+note.removesuffix('.md')+'|'+Path(note).stem+']]\n']
        for item in items:
            lines+=['- 数学节点 '+str(item['index'])+'：`'+item['error']+'`\n',fence(item['tex'],'latex')]
        body=(VAULT/note).read_text()
        if '<!-- MATHJAX_CAUTION -->' not in body:
            end=body.index('\n---\n',4)+5 if body.startswith('---\n') else 0
            alert='\n<!-- MATHJAX_CAUTION -->\n> [!warning] 公式显示兼容性\n> 此文有 '+str(len(items))+' 处公式未通过服务端MathJax兼容性检查；原始TeX仍完整保留。请对照 [逐项记录]('+relative_link('99_维护/公式显示兼容性.md',note,heading)+') 和原PDF，不将显示错误当作数学结论。\n\n'
            put(note,body[:end]+alert+body[end:])
    put('99_维护/公式显示兼容性.md','\n'.join(lines))
    put('99_维护/reading_cautions.json',json.dumps(dict(literal_source_fallbacks=sorted(all_fallbacks),
        mathjax_failed_occurrences=len(failures),mathjax_affected_notes=len(by_note),
        error_counts=dict(Counter(v['error'] for v in failures)),scope='Reading fidelity and display warnings; no mathematical corrections'),ensure_ascii=False,indent=2)+'\n')
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(literal_source_fallbacks=len(all_fallbacks),mathjax_failed_occurrences=len(failures),
                         mathjax_affected_notes=len(by_note),remaining_math_nodes=len(filtered)),ensure_ascii=False))

if __name__=='__main__':main()
