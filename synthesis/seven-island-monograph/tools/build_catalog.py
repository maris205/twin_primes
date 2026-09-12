#!/usr/bin/env python3
"""Generate a transparent lexical locator, never a semantic proof audit."""
import hashlib
import json
from pathlib import Path
import re

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
WORDS = {
    '1': ['sieve', 'arithmetic baseline', '筛法'],
    '2': ['gram', 'poisson', 'fourier', 'operator', 'kloosterman', 'bdh', '算子'],
    '3': ['fixed atom', 'fixed-atom', 'determinant-two', '指定原子'],
    '4': ['pair-native', 'pair-to', 'opened-d', 'h1', 'occurrence', '出现项'],
    '5': ['dynamical', 'dynamics', 'borel', 'distinguished-seed', 'nonautonomous', '动力学'],
    '7': ['hénon', 'henon', 'semiconjug', 'geometric lifting', '半共轭'],
}

def main():
    index = (ROOT / 'research/tpc-big-road/PAPER_MATERIALS_INDEX.md').read_text()
    names = re.findall(r'^\| TPC \| `([^`]+)` \|', index, re.M)
    actual = {p.name for p in (ROOT / 'papers').iterdir() if p.is_dir() and p.name.startswith('tpc-')}
    if len(names) != 420 or set(names) != actual or len(set(names)) != len(names):
        raise ValueError('unexpected archive coverage; re-audit scope')
    rows = []
    for name in names:
        directory = ROOT / 'papers' / name
        candidates = [directory / p for p in ('README.md', 'paper/main.tex', 'main.tex')]
        sources, hits = [], []
        title = name
        for path in candidates:
            if not path.is_file():
                continue
            raw = path.read_bytes()
            text = raw.decode('utf-8', errors='replace')
            sources.append({'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(raw).hexdigest()})
            if path.name == 'README.md':
                first = next((s.lstrip('# ').strip() for s in text.splitlines() if s.startswith('# ')), '')
                if first:
                    title = first
            for number, line in enumerate(text.splitlines(), 1):
                for island, terms in WORDS.items():
                    found = [term for term in terms if term in line.lower()]
                    if found and not any(h['island'] == island for h in hits):
                        hits.append({'island': island, 'path': str(path.relative_to(ROOT)),
                                     'line': number, 'terms': found, 'excerpt': line[:220]})
        rows.append({'directory': name, 'title': title, 'sources': sources,
                     'candidate_islands': sorted(h['island'] for h in hits), 'lexical_evidence': hits,
                     'semantic_review': 'NOT_ASSERTED', 'use_in_manuscript': 'SEE_CORE_SOURCE_MATRIX'})
    payload = {'method': 'Case-insensitive literal keyword locator over root README and manuscript source; not semantic classification.',
               'scope': '420 main TPC directories; not early-branch duplicates', 'papers': rows}
    (PROJECT / 'SOURCE_CATALOG.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    lines = ['# 全目录来源检索表', '', '420 个现有目录全部列入。候选岛号来自 README／TeX 的字面匹配，不是人工数学归类，不代表定理成立。',
             '图像桥／Gate 名称不得仅凭关键词识别；岛6不自动赋予任何材料。精确命题以 CORE_SOURCE_MATRIX.md 为准。', '',
             '| 原目录 | 标题／入口 | 候选岛号（检索用） | 审核状态 |', '|---|---|---|---|']
    for row in rows:
        name = row['directory']
        title = row['title'].replace('|', '\\|').replace('\n', ' ')
        islands = ', '.join(row['candidate_islands']) or '待人工定位'
        lines.append(f'| [{name}](../../papers/{name}) | {title} | {islands} | 未作全文语义认证 |')
    (PROJECT / 'SOURCE_CATALOG.md').write_text('\n'.join(lines) + '\n')
    print(f'catalog: {len(rows)} directories; semantic classification/review NOT asserted')

if __name__ == '__main__':
    main()
