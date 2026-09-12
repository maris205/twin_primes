#!/usr/bin/env python3
"""Archive exact source Markdown bytes alongside adapted reading notes."""
import argparse
import hashlib
import json
from pathlib import Path
from prepare_sources import VAULT,CACHE,DEFAULT_SOURCE,digest,source_snapshot
from build_vault import relative_link

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,default=DEFAULT_SOURCE)
    args=parser.parse_args();source=args.source.resolve()
    baseline=json.loads((CACHE/'source_baseline.json').read_text())
    if source_snapshot(source)!=baseline['files']:raise ValueError('Source baseline changed')
    path=VAULT/'99_维护/generated_manifest.json'
    manifest=json.loads(path.read_text())
    if manifest.get('build_incomplete'):raise ValueError('Incomplete build')
    for rel,sha in manifest['files'].items():
        if digest(VAULT/rel)!=sha:raise ValueError('Changed generated file: '+rel)
    def put(relative,data):
        if isinstance(data,str):data=data.encode()
        target=VAULT/relative;sha=hashlib.sha256(data).hexdigest()
        if target.exists() and digest(target)!=sha and manifest['files'].get(relative)!=digest(target):
            raise ValueError('Refusing to overwrite unknown file: '+relative)
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        manifest['files'][relative]=sha
    source_path='99_维护/source_manifest.json'
    sources=json.loads((VAULT/source_path).read_text())
    count=0
    for row in json.loads((VAULT/'99_维护/adaptation_report.json').read_text()):
        origin=Path(row['origin'])
        if not origin.is_relative_to(source):raise ValueError('Foreign source origin')
        if not origin.is_file():continue  # Fresh mechanical main.md has no original MD file.
        relative=str(origin.relative_to(source))
        sha=digest(origin)
        if baseline['files'].get(relative)!=sha:raise ValueError('Unpreserved reading source: '+relative)
        attachment='90_附件/原始资料/'+relative+'.txt'
        put(attachment,origin.read_bytes())
        sources['source_files'][relative]=dict(vault_path=attachment,sha256=sha,original_path=relative)
        note=row['destination'];raw=(VAULT/note).read_text()
        if '<!-- ORIGINAL_BYTES_LINK -->' not in raw:
            marker='<!-- ORIGINAL_BYTES_LINK -->\n[原始Markdown文件（逐字节保留）]('+relative_link(attachment,note)+')；可用外部编辑器核对。\n\n'
            end=raw.index('\n---\n',4)+5 if raw.startswith('---\n') else 0
            raw=raw[:end]+'\n'+marker+raw[end:]
            put(note,raw)
        count+=1
    put(source_path,json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    if source_snapshot(source)!=baseline['files']:raise ValueError('Source preservation failed')
    print(json.dumps(dict(exact_markdown_sources=count,all_preserved_attachments=len(sources['source_files'])),ensure_ascii=False))

if __name__=='__main__':main()
