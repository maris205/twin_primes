#!/usr/bin/env python3
"""Verify English document integrity and parity, not mathematical truth."""
import collections
import hashlib
import json
from pathlib import Path
import re
import subprocess
import check_paper

PROJECT = Path(__file__).resolve().parents[1]
PAPER = PROJECT / 'paper-en'

def require(ok, message):
    if not ok:
        raise ValueError(message)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    check_paper.PAPER = PAPER
    check_paper.main()
    baseline = json.loads((PAPER / 'chinese_baseline_lock.json').read_text())
    actual = {str(p.relative_to(PROJECT)): digest(p)
              for p in sorted((PROJECT / 'paper').rglob('*')) if p.is_file()}
    require(baseline == actual, 'Chinese baseline changed')
    image = PAPER / 'figures/tpc_route_en.png'
    require(digest(image) == '83c729864e69fc87569ec23ad0b1c7d6251fedd3b61f059881d17fec37ef24fa',
            'English map differs from user original')
    require((PAPER / 'references.bib').read_bytes() == (PROJECT / 'paper/references.bib').read_bytes(),
            'Bibliography differs')
    parity = {}
    for source in sorted((PROJECT / 'paper/sections').glob('*.tex')):
        translated = PAPER / 'sections' / source.name
        require(translated.exists(), 'Missing English section')
        zh, en = source.read_text(), translated.read_text()
        require(not re.search('[\u4e00-\u9fff]', en), 'Untranslated Chinese in English TeX')
        for name, pattern in [
            ('labels', r'\\label\{([^}]+)\}'),
            ('citations', r'\\cite\w*\{([^}]+)\}'),
            ('proofs', r'\\begin\{(proof)\}'),
            ('formal_statements', r'\\begin\{(theorem|proposition|lemma|corollary|condition|definition)\}')]:
            require(collections.Counter(re.findall(pattern, zh)) == collections.Counter(re.findall(pattern, en)),
                    f'{name} mismatch: {source.name}')
        parity[source.name] = 'labels/citations/proofs/formal statements match'
    require(len(list((PAPER / 'sections').glob('*.tex'))) == len(parity), 'Extra English sections')
    text = (PAPER / 'main.txt').read_text()
    require(not re.search(r'\?\?|\[\?\]|\[VERIFY\]', text), 'Unresolved PDF text marker')
    contents_page = re.search(r'^References\s+(\d+)\s*$', text, re.M)
    reference_pages = [i for i, page in enumerate(text.split('\f'), 1)
                       if re.search(r'^References\s*$', page, re.M)]
    require(contents_page is not None and reference_pages == [int(contents_page.group(1))],
            'Bibliography contents page does not match actual heading')
    fonts = subprocess.check_output(['pdffonts', str(PAPER / 'main.pdf')], text=True)
    (PAPER / 'fonts.txt').write_text(fonts)
    report = dict(scope='Translation document integrity; not semantic proof or novelty certification',
                  chinese_files_preserved=len(baseline), map_sha256=digest(image),
                  pdf_sha256=digest(PAPER / 'main.pdf'), section_parity=parity)
    (PAPER / 'translation_checks.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
