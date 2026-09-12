#!/usr/bin/env python3
"""Read-only integrity and navigation checks; no mathematical correctness claim."""
import argparse
from collections import Counter,defaultdict,deque
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote
from prepare_sources import VAULT,CACHE,digest
from markdown_adapter import pandoc,walk,plain_inlines,OUTPUT_READER

def require(test,message):
    if not test:raise ValueError(message)

def without_code(text):
    text=re.sub(r'(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$', '',text)
    return re.sub(r'`[^`\n]*`','',text)

def inspect_links(note,raw):
    # Pandoc excludes link-looking examples inside code and resolves reference
    # links, unlike a standalone URL regex. Wikilinks are separately indexed.
    parsed=json.loads(pandoc(raw,OUTPUT_READER)[0])
    links=[node['c'][-1][0] for node in walk(parsed['blocks'],'Link')]
    links += [node['c'][-1][0] for node in walk(parsed['blocks'],'Image')]
    wiki_text=without_code(raw)
    for hit in re.finditer(r'!?\[\[([^\]\n]+)\]\]',wiki_text):
        target=hit[1].split('|',1)[0]
        links.append('WIKI:'+target)
    headings={plain_inlines(n['c'][2]).strip() for n in walk(parsed['blocks'],'Header')}
    return links,headings

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--report',action='store_true',help='write only generated QA artifacts inside the vault')
    parser.add_argument('--quick',action='store_true',help='skip repeated AST link parsing if unchanged cache exists')
    args=parser.parse_args()
    manifest=json.loads((VAULT/'99_维护/generated_manifest.json').read_text())
    require(not manifest.get('build_incomplete'),'Build is incomplete')
    for relative,expected in manifest['files'].items():
        path=VAULT/relative
        require(path.is_file() and digest(path)==expected,'Generated file changed/missing: '+relative)
    inventory=json.loads((VAULT/'99_维护/论文清单.json').read_text())
    require(len(inventory)==len({r['id'] for r in inventory})==420,'Inventory identity coverage mismatch')
    require(len(list((VAULT/'02_论文').glob('*.md')))==420,'Paper entry count mismatch')
    require(len(list((VAULT/'03_全文').glob('*.md')))==419,'Fulltext count mismatch')
    require(sum(r['conversion_status']=='SOURCE_UNAVAILABLE' for r in inventory)==1,'Missing-source classification mismatch')
    source_manifest=json.loads((VAULT/'99_维护/source_manifest.json').read_text())
    for source,item in source_manifest['source_files'].items():
        require(digest(VAULT/item['vault_path'])==item['sha256'],'Source-copy bytes changed: '+source)
    notes={str(p.relative_to(VAULT)):p for p in VAULT.rglob('*.md')
           if not any(part.startswith('.') for part in p.relative_to(VAULT).parts)
           and not str(p.relative_to(VAULT)).startswith(('90_附件/','_tools/'))}
    cache_path=CACHE/'link_check_cache.json'
    previous=json.loads(cache_path.read_text()) if cache_path.exists() else {}
    parsed={}
    def inspect_entry(entry):
        relative,path=entry
        sha=digest(path)
        if args.quick and previous.get(relative,{}).get('sha256')==sha:
            result=previous[relative]
        else:
            links,headings=inspect_links(relative,path.read_text())
            result=dict(sha256=sha,links=links,headings=sorted(headings))
        return relative,result
    with ThreadPoolExecutor(max_workers=8) as pool:
        for i,(relative,result) in enumerate(pool.map(inspect_entry,sorted(notes.items())),1):
            parsed[relative]=result
            if i%150==0: print('Checked note syntax',i,'/',len(notes),flush=True)
    graph=defaultdict(set); errors=[]; internal=0; external=0
    for source,item in parsed.items():
        for target in item['links']:
            if target.startswith(('http://','https://','mailto:','doi:')):
                external+=1;continue
            is_wiki=target.startswith('WIKI:')
            target=target[5:] if is_wiki else unquote(target)
            path,_,fragment=target.partition('#')
            if is_wiki:
                if not Path(path).suffix:path+='.md'
                resolved=(VAULT/path).resolve()
            else:
                resolved=(VAULT/Path(source).parent/path).resolve() if path else VAULT/source
            if not resolved.is_relative_to(VAULT):
                errors.append([source,target,'ESCAPES_VAULT']);continue
            if not resolved.is_file():
                errors.append([source,target,'MISSING_FILE']);continue
            internal+=1
            relative=str(resolved.relative_to(VAULT))
            if relative in notes:
                graph[source].add(relative)
                if fragment and fragment not in parsed[relative]['headings'] and not fragment.startswith('^'):
                    errors.append([source,target,'MISSING_HEADING'])
    reached=set();todo=deque(['00_开始阅读.md'])
    while todo:
        node=todo.popleft()
        if node in reached:continue
        reached.add(node);todo.extend(graph[node]-reached)
    mandatory={p for p in notes if p.startswith(('01_导航/','02_论文/','03_全文/','04_知识卡片/','05_综合与进展/'))}
    unreachable=sorted(mandatory-reached)
    adaptations=json.loads((VAULT/'99_维护/adaptation_report.json').read_text())
    for row in adaptations:
        if row.get('literal_source_fallback'):
            attachment=VAULT/row['fallback_original_attachment']
            require(digest(attachment)==row['fallback_original_sha256'],'Fallback source bytes changed')
            original=attachment.read_bytes().decode().replace('\r\n','\n').replace('\r','\n')
            ast=json.loads(pandoc((VAULT/row['destination']).read_text(),OUTPUT_READER)[0])
            blocks=[v['c'][1] for v in walk(ast['blocks'],'CodeBlock')]
            require(blocks==[original],'Literal fallback does not exactly preserve source text')
        else:require(row['math_roundtrip'],'Math roundtrip failure')
    result=dict(scope='Document and source integrity, not semantic proof or theorem validation',
                paper_directories=420,accessible_fulltexts=419,source_unavailable=1,
                note_count=len(notes),internal_links=internal,external_links_not_network_checked=external,
                live_navigation_errors=errors,unreachable_core_notes=unreachable,
                source_files_preserved=len(source_manifest['source_files']),
                historical_source_link_exceptions=len(json.loads((VAULT/'99_维护/source_link_exceptions.json').read_text())),
                adapted_notes=len(adaptations),math_nodes=sum(r['math_nodes'] for r in adaptations),
                literal_source_fallbacks=[r['destination'] for r in adaptations if r.get('literal_source_fallback')],
                adapter_text_roundtrip_warnings=[r['destination'] for r in adaptations if not r['text_roundtrip'] and not r.get('literal_source_fallback')],
                adapter_reader_warnings=[dict(note=r['destination'],warnings=r['warnings']) for r in adaptations if r['warnings']],
                status='PASS' if not errors and not unreachable else 'FAIL')
    cache_path.write_text(json.dumps(parsed,ensure_ascii=False)+'\n')
    if args.report:
        relative='99_维护/validation_results.json'
        report_path=VAULT/relative
        data=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
        if report_path.exists() and report_path.read_text()!=data and manifest['files'].get(relative)!=digest(report_path):
            raise ValueError('Refusing to overwrite unrecognized QA artifact')
        report_path.write_text(data)
        manifest['files'][relative]=digest(report_path)
        (VAULT/'99_维护/generated_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('live_navigation_errors','adapter_reader_warnings')},ensure_ascii=False,indent=2))
    if errors: print(json.dumps(errors[:30],ensure_ascii=False,indent=2))
    require(not errors and not unreachable,'Vault link/navigation checks failed')

if __name__=='__main__':main()
