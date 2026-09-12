#!/usr/bin/env python3
"""Read preserved TPC sources; cache derived content only inside this vault.

The archive converter is imported as a read-only library. No patch is emitted
to the source repository, no TeX is executed and no experiment is run.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

VAULT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = VAULT.parent / 'twin_primes'
CACHE = VAULT / '.build'
PREPARER_VERSION = 'vault-preparation-v3'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def cache_integrity(value):
    payload={k:v for k,v in value.items() if k!='content_integrity'}
    return hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def require_cache_payload(value):
    status=value.get('conversion_status')
    if status not in {'SOURCE_UNAVAILABLE','CONVERSION_BLOCKED','FULL_TEX_TO_MARKDOWN_MECHANICAL','REUSED_SOURCE_COMPLETE_MECHANICAL'}:
        raise ValueError('Unknown cache conversion state')
    if status in {'SOURCE_UNAVAILABLE','CONVERSION_BLOCKED'}:
        if value.get('markdown') or value.get('record'):raise ValueError('Unavailable/blocked cache has unexpected content')
    elif not value.get('markdown','').strip() or not value.get('record','').strip():
        raise ValueError('Successful cache lacks source content')
    if status=='FULL_TEX_TO_MARKDOWN_MECHANICAL' and value.get('report',{}).get('status')!=status:
        raise ValueError('Cache status/report mismatch')

def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def catalog(source):
    locator = source / 'research/tpc-big-road/PAPER_MATERIALS_LINKS.md'
    enrichment = {p['directory']: p for p in json.loads(
        (source / 'synthesis/seven-island-monograph/SOURCE_CATALOG.json').read_text())['papers']}
    rows = []
    for line in locator.read_text().splitlines():
        if not line.startswith('| TPC |'):
            continue
        fields = [s.strip() for s in line.split('|')[1:-1]]
        name = re.search(r'\[([^]]+)\]', fields[1])[1]
        paths = {}
        for key, value in zip(['md', 'tex', 'pdf'], fields[3:6]):
            hit = re.search(r'\]\(([^)]+)\)', value)
            if hit:
                path = (locator.parent / hit[1]).resolve()
                if not path.is_relative_to(source) or not path.is_file():
                    raise ValueError(f'Invalid inventoried {key} source: {path}')
                paths[key] = str(path.relative_to(source))
        match = re.match(r'tpc-(\d+)-', name)
        number = int(match[1]) if match else 0
        status = fields[2].strip('`')
        ident = f'TPC-{number:03}' if number else 'TPC-MVP1'
        if status == 'source-inaccessible':
            ident += '-source-unavailable'
        enriched = enrichment[name]
        rows.append(dict(id=ident, directory=name, number=number, paths=paths,
                         prior_status=status, title=enriched['title'],
                         candidate_islands=enriched['candidate_islands'],
                         lexical_evidence=enriched['lexical_evidence']))
    if len(rows) != 420 or len({r['id'] for r in rows}) != 420:
        raise ValueError('Inventory must retain exactly 420 distinct directory identities')
    return sorted(rows, key=lambda r:(r['number'] if r['number'] else 10000, r['id']))

def source_snapshot(source):
    paths = set()
    for name in ['papers', 'research/tpc-big-road', 'synthesis']:
        paths.update(p for p in (source / name).rglob('*') if p.is_file()
                     and '__pycache__' not in p.parts and '.git' not in p.parts)
    paths.update(source.glob('*.md'))
    return {str(p.relative_to(source)): digest(p) for p in sorted(paths)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    parser.add_argument('--workers', type=int, default=6)
    parser.add_argument('--retry-failed', action='store_true')
    parser.add_argument('--ids', nargs='*')
    args = parser.parse_args()
    source = args.source.resolve()
    if source == VAULT or VAULT.is_relative_to(source):
        raise ValueError('Vault must be separate from the preserved repository')
    rows = catalog(source)
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=source, text=True).strip()
    snapshot = source_snapshot(source)
    baseline_path = CACHE / 'source_baseline.json'
    if baseline_path.exists():
        baseline=json.loads(baseline_path.read_text())
        if baseline['files'] != snapshot or baseline['repository_head'] != head:
            raise ValueError('Source baseline changed: review changes before rebuilding')
    else:
        save_json(baseline_path, dict(repository_head=head, source=str(source), files=snapshot,
                  purpose='Preservation check, not mathematical verification'))
    save_json(CACHE / 'inventory.json', rows)
    sys.path.insert(0, str(source / 'research/tpc-big-road'))
    import maintain_source_markdown as converter
    converter.ROOT = source
    from converter_extensions import install, NOTICE
    install(converter)
    by_directory = {r['directory']: r for r in rows}
    original_select = converter.select_paper
    def selected(number, paper_name=None):
        if number == 0 and paper_name == 'tpc-mvp1-fixed-shift-proof-architecture':
            return source / 'papers' / paper_name
        return original_select(number, paper_name)
    converter.select_paper = selected
    def selected_pdf(paper, source_commit='HEAD', *, source_path=None):
        # Inventory already resolves older descriptive PDF filenames. Retain
        # that exact selection; the converter still checks its committed hash.
        return source / by_directory[paper.name]['paths']['pdf']
    converter.preserved_pdf = selected_pdf
    fingerprint=hashlib.sha256(('\n'.join(digest(p) for p in [
        Path(__file__),Path(__file__).with_name('converter_extensions.py'),
        source/'research/tpc-big-road/maintain_source_markdown.py',
        source/'research/tpc-big-road/source_markdown_includes.py'])).encode()).hexdigest()
    def one(row):
        path = CACHE / 'papers' / (row['id'] + '.json')
        if path.exists():
            cached = json.loads(path.read_text())
            current=(cached.get('preparer_version')==PREPARER_VERSION
                     and cached.get('reader_fingerprint')==fingerprint)
            identity=all(cached.get(key)==value for key,value in row.items()) and cached.get('source_head')==head
            if current:
                if not identity or cached.get('content_integrity') != cache_integrity(cached):
                    raise ValueError('Cache identity/content integrity failure: '+row['id'])
                require_cache_payload(cached)
                if not (args.retry_failed and cached['conversion_status'] == 'CONVERSION_BLOCKED'):
                    return cached
            # Keep the prior generated cache for the raw audit trail. A fixed
            # adapter never reuses old successful-but-damaged output.
            old_hash=digest(path)
            history=CACHE/'cache_history'/row['id']/(old_hash+'.json')
            if not history.exists():
                history.parent.mkdir(parents=True,exist_ok=True)
                history.write_bytes(path.read_bytes())
        result = dict(row, source_head=head)
        if row['prior_status'] == 'source-inaccessible':
            result.update(conversion_status='SOURCE_UNAVAILABLE', markdown='', record='',
                          limitations=['No accessible original manuscript; no substitute invented.'])
        elif row['prior_status'] == 'full-source-md':
            md_path = source / row['paths']['md']
            record_path = source / 'papers' / row['directory'] / 'CONVERSION_RECORD.md'
            original = md_path.read_bytes()
            record = record_path.read_text()
            recorded = re.search(r'Reading layer:.*?SHA-256 `([a-f0-9]{64})`', record)
            if recorded is None or hashlib.sha256(original).hexdigest() != recorded[1]:
                raise ValueError(f'Existing reading-layer hash mismatch: {row["id"]}')
            result.update(conversion_status='REUSED_SOURCE_COMPLETE_MECHANICAL',
                          markdown=original.decode(), record=record,
                          md_sha256=hashlib.sha256(original).hexdigest(),
                          limitations=['Existing full-source mechanical conversion; not semantic certification.'])
        else:
            try:
                _, md, record, report = converter.convert(row['number'], source_commit=head,
                                                          paper_name=row['directory'])
                result.update(conversion_status=report['status'], markdown=md,
                              record=record + '\n## Vault-local reader adaptation\n\n' + NOTICE + '\n',
                              report=report, limitations=report['limitations'], adapter_notice=NOTICE)
            except Exception as exc:
                result.update(conversion_status='CONVERSION_BLOCKED', markdown='', record='',
                              limitations=[f'{type(exc).__name__}: {exc}'])
        result['reading_source_path'] = row['paths'].get('md') if row['prior_status'] == 'full-source-md' else (
            'papers/' + row['directory'] + '/paper/main.md')
        result['preparer_version']=PREPARER_VERSION
        result['reader_fingerprint']=fingerprint
        require_cache_payload(result)
        result['content_integrity']=cache_integrity(result)
        save_json(path, result)
        return result
    selected_rows = [r for r in rows if not args.ids or r['id'] in args.ids]
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(one, row): row for row in selected_rows}
        for done in as_completed(futures):
            result = done.result()
            results.append(result)
            print(result['id'], result['conversion_status'], flush=True)
            if result['conversion_status'] == 'CONVERSION_BLOCKED':
                print('  ', result['limitations'][0], flush=True)
    if source_snapshot(source) != snapshot:
        raise ValueError('Preserved source files changed during conversion')
    counts = {s:sum(r['conversion_status'] == s for r in results)
              for s in sorted({r['conversion_status'] for r in results})}
    save_json(CACHE / 'preparation_report.json', dict(counts=counts, rows=len(results),
              source_preserved=True, source_files=len(snapshot), source_head=head))
    print(json.dumps(counts, ensure_ascii=False), flush=True)

if __name__ == '__main__':
    main()
