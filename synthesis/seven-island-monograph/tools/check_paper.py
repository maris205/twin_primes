#!/usr/bin/env python3
"""Read-only document/source checks. This is not a theorem checker."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

PROJECT = Path(__file__).resolve().parents[1]
PAPER = PROJECT / 'paper'
ROOT = PROJECT.parents[1]

def require(ok, message):
    if not ok:
        raise ValueError(message)

def main():
    master = (PAPER / 'main.tex').read_text()
    includes = re.findall(r'\\input\{([^}]+)\}', master)
    require(all((PAPER / path).is_file() for path in includes), 'Missing TeX include')
    tex = master + '\n' + '\n'.join((PAPER / path).read_text() for path in includes)
    labels = re.findall(r'\\label\{([^}]+)\}', tex)
    require(len(labels) == len(set(labels)), 'Duplicate labels')
    references = set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', tex))
    require(references <= set(labels), f'Undefined labels: {references-set(labels)}')
    keys = {k.strip() for chunk in re.findall(r'\\cite\w*\{([^}]+)\}', tex) for k in chunk.split(',')}
    bib = set(re.findall(r'@\w+\{([^,]+),', (PAPER/'references.bib').read_text()))
    require(keys == bib, f'Citation-key mismatch: {keys ^ bib}')
    log = (PAPER/'main.log').read_text(errors='replace')
    require(not re.search(r'undefined|Missing character|Overfull|^!', log, re.M), 'Unresolved PDF/TeX error')
    require(not re.search(r'TODO|FIXME|\[VERIFY\]', tex), 'Unresolved writing placeholder')
    require((PAPER/'main.pdf').stat().st_size > 100000, 'Implausibly small PDF')
    fonts = subprocess.check_output(['pdffonts', str(PAPER/'main.pdf')], text=True)
    require(all(re.search(r'\s+yes\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$', line)
                for line in fonts.splitlines()[2:] if line.strip()), 'Nonembedded PDF font')
    matrix = json.loads((PROJECT/'CORE_SOURCE_MATRIX.json').read_text())
    for item in matrix['sources']:
        require(hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest() == item['sha256'], 'Changed core source')
    catalog = json.loads((PROJECT/'SOURCE_CATALOG.json').read_text())['papers']
    require(len(catalog) == len({p['directory'] for p in catalog}) == 420, 'Catalog coverage mismatch')
    for paper in catalog:
        for item in paper['sources']:
            require(hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest() == item['sha256'], 'Changed catalog source')
    info = subprocess.check_output(['pdfinfo', str(PAPER/'main.pdf')], text=True)
    print(json.dumps(dict(status='PASS', claim='Document rendering and source fidelity only; NOT mathematical proof verification',
                         pages=int(re.search(r'Pages:\s+(\d+)', info).group(1)),
                         citations=len(keys), labels=len(labels), core_sources=len(matrix['sources']),
                         catalog_directories=len(catalog), all_fonts_embedded=True,
                         missing_glyphs=0, overfull_boxes=0,
                         underfull_boxes=len(re.findall('Underfull', log)),
                         font_metadata_warnings=len(re.findall('Package fontspec Warning', log)),
                         pdf_sha256=hashlib.sha256((PAPER/'main.pdf').read_bytes()).hexdigest()), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
