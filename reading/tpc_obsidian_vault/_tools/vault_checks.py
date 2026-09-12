"""Resolve real heading targets and retain unavailable historical links explicitly."""
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote
from build_vault import VAULT, properties, relative_link, wiki

LINK = re.compile(r'\]\(([^\s)]+)\)')

def resolve_deferred_links(builder):
    reports={r['destination']:r for r in builder.adapt_reports}
    for note in sorted(builder.generated):
        if not note.endswith('.md'):continue
        raw=(VAULT/note).read_text()
        if '#pending-' not in raw:continue
        def replace(match):
            target=match[1]
            if '#pending-' not in target:return match[0]
            path,fragment=target.split('#pending-',1)
            fragment=unquote(fragment)
            resolved=(VAULT/Path(note).parent/unquote(path)).resolve()
            if not resolved.is_relative_to(VAULT):
                raise ValueError('Deferred link escapes the vault')
            rel=str(resolved.relative_to(VAULT))
            report=reports.get(rel,{})
            mapping={**report.get('heading_targets',{}),**report.get('label_targets',{})}
            actual=mapping.get(fragment)
            if actual is None and fragment in mapping.values():actual=fragment
            if actual:
                return ']('+relative_link(rel,note,actual)+')'
            origin=builder.source/builder.note_sources.get(note,'TPC_HANDOFF.md')
            alternative=builder.missing(target,origin,note,'Cross-document source anchor unavailable after parsing')
            return ']('+alternative+')'
        result=LINK.sub(replace,raw)
        builder.put(note,result)

def write_issue_note(builder):
    lines=[properties(type='source-link-exceptions',generated=True),'# 待解决的原始来源链接\n',
           '这些问题来自被导入的历史材料。知识库将其转为可追溯的例外条目，不把缺失源、跨范围文件或未知锚点伪装成已经找到的证据。\n',
           '“内部导航无断链”不等于“每个历史来源链接已经解决”。下面保留原目标、出处和原因。\n',
           '条目数：'+str(len(builder.unresolved))+'。\n']
    for ident,item in sorted(builder.unresolved.items()):
        lines += ['## '+ident+'\n', '- 原目标：`'+item['target'].replace('`','\\`')+'`\n',
                  '- 原出处：`'+item['source']+'`\n','- 原因：'+item['reason']+'\n',
                  '- 返回阅读层：'+wiki(item['destination'],Path(item['destination']).stem)+'\n']
    builder.put('99_维护/待解决来源链接.md','\n'.join(lines))
    builder.put('99_维护/source_link_exceptions.json',json.dumps(builder.unresolved,ensure_ascii=False,indent=2)+'\n')
