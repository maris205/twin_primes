#!/usr/bin/env python3
"""Preserve, build, and validate this separate editorial edition.

Generated logs/manifests are written only inside this revision directory.
Original editions and primary sources are always read-only.
"""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
REPO = WORKSPACE / 'twin_primes'
ORIGINAL = REPO / 'synthesis/seven-island-monograph'
PAPER = ROOT / 'paper'
LOCK = ROOT / 'baseline_lock.json'
FORMAL = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|condition|proof)\}.*?\\end\{\1\}', re.S)
DISPLAY = re.compile(r'\\\[.*?\\\]|\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}', re.S)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def protected_files():
    files = {p for folder in ('paper', 'paper-en')
             for p in (ORIGINAL / folder).rglob('*') if p.is_file()}
    matrix = json.loads((ROOT / 'CORE_SOURCE_MATRIX.json').read_text())
    files.update(REPO / entry['path'] for entry in matrix['sources'])
    files.update((WORKSPACE / 'tpc_obsidian_vault/04_知识卡片').glob('K*.md'))
    files.update(ORIGINAL / name for name in ('CORE_SOURCE_MATRIX.json', 'SOURCE_CATALOG.json'))
    return {str(p.relative_to(WORKSPACE)): digest(p) for p in sorted(files)}


def initialize():
    require(not LOCK.exists(), 'Refusing to replace existing baseline lock')
    LOCK.write_text(json.dumps(protected_files(), indent=2, ensure_ascii=False) + '\n')
    print('Frozen source files:', len(json.loads(LOCK.read_text())))


def check_preservation():
    original_lock = json.loads(LOCK.read_text())
    require(original_lock == protected_files(), 'Protected source file set or bytes changed')
    matrix = json.loads((ROOT / 'CORE_SOURCE_MATRIX.json').read_text())
    for entry in matrix['sources']:
        require(digest(REPO / entry['path']) == entry['sha256'], 'Primary source hash mismatch: ' + entry['id'])
    return len(original_lock)


def run(args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True, stderr=subprocess.STDOUT)


def build(round_number):
    check_preservation()
    scratch = Path(tempfile.mkdtemp(prefix='tpc-wiki-revision-build-'))
    source = scratch / 'source'
    source.mkdir()
    for name in ('main.tex', 'math_commands.tex', 'notation.tex', 'references.bib'):
        shutil.copy2(PAPER / name, source / name)
    for folder in ('sections', 'figures'):
        shutil.copytree(PAPER / folder, source / folder)
    output = scratch / 'build'
    output.mkdir()
    command = ['latexmk', '-pdf', '-no-shell-escape', '-interaction=nonstopmode',
               '-halt-on-error', f'-outdir={output}', 'main.tex']
    process = subprocess.run(command, cwd=source, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (PAPER / 'compile.log').write_bytes(process.stdout)
    if (output / 'main.log').exists():
        shutil.copy2(output / 'main.log', PAPER / 'main.log')
    require(process.returncode == 0, 'LaTeX failed; inspect paper/compile.log')
    for name in ('main.pdf', 'main.aux', 'main.bbl', 'main.toc'):
        require((output / name).exists(), 'Missing build artifact: ' + name)
    for name in ('main.pdf', 'main.aux', 'main.bbl', 'main.toc'):
        shutil.copy2(output / name, PAPER / name)
    shutil.copy2(PAPER / 'main.pdf', PAPER / f'main_round{round_number}.pdf')
    (PAPER / 'main.txt').write_text(run(['pdftotext', '-layout', str(PAPER / 'main.pdf'), '-']))
    (PAPER / 'fonts.txt').write_text(run(['pdffonts', str(PAPER / 'main.pdf')]))
    convert = lambda name: run(['pandoc', '-f', 'latex', '-t', 'markdown', '--wrap=none', name], PAPER)
    (PAPER / 'main.md').write_text('# A Seven-Island Framework for Twin-Prime Research\n\n'
        'English revision v0.2. PDF numbering and layout are authoritative.\n\n## Abstract\n\n'
        + convert('sections/abstract.tex') + '\n' + convert('main.tex'))
    check_preservation()
    print(run(['pdfinfo', str(PAPER / 'main.pdf')]))
    print('Scratch:', scratch)


def checks():
    preserved = check_preservation()
    formal_count = 0
    preserved_display_count = 0
    for original in sorted((ORIGINAL / 'paper-en/sections').glob('*.tex')):
        old = original.read_text()
        new = (PAPER / 'sections' / original.name).read_text()
        before = [match.group(0) for match in FORMAL.finditer(old)]
        after = [match.group(0) for match in FORMAL.finditer(new)]
        require(before == after, 'Formal block changed: ' + original.name)
        formal_count += len(before)
        for match in DISPLAY.finditer(old):
            require(match.group(0) in new, 'Original displayed mathematics changed: ' + original.name)
            preserved_display_count += 1
        for pattern in (r'\\label\{([^}]+)\}', r'\\cite\{([^}]+)\}'):
            for item in re.findall(pattern, old):
                require(item in re.findall(pattern, new), 'Original label/citation lost: ' + item)
    for name in ('references.bib', 'math_commands.tex', 'figures/tpc_route_en.png'):
        require(digest(PAPER / name) == digest(ORIGINAL / 'paper-en' / name), 'Shared asset changed: ' + name)
    log = (PAPER / 'main.log').read_text()
    warnings = [line for line in log.splitlines() if re.search(
        r'Overfull|Underfull|undefined|Missing character|multiply defined', line)]
    require(not warnings, 'Unresolved layout/reference warnings: ' + repr(warnings))
    fonts = (PAPER / 'fonts.txt').read_text().splitlines()[2:]
    require(fonts and all(re.search(r'\s+yes\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$', line) for line in fonts), 'Unembedded font')
    text = (PAPER / 'main.txt').read_text()
    require('\ufffd' not in text, 'Replacement glyph in extracted text')
    require('??' not in text and '[?]' not in text and '[VERIFY]' not in text, 'Unresolved text placeholder')
    info = run(['pdfinfo', str(PAPER / 'main.pdf')])
    pages = int(re.search(r'Pages:\s+(\d+)', info).group(1))
    page_texts = text.split('\f')
    reference_pages = [i for i, page in enumerate(page_texts, 1)
                       if page.lstrip().startswith('References\n')]
    toc = (PAPER / 'main.toc').read_text()
    toc_reference = re.search(r'\\contentsline \{section\}\{References\}\{(\d+)\}', toc)
    require(toc_reference and reference_pages == [int(toc_reference.group(1))], 'References TOC/page mismatch')
    bib_keys = re.findall(r'\\bibitem(?:\[.*?\])?\{([^}]+)\}', (PAPER / 'main.bbl').read_text(), re.S)
    source_bib_keys = re.findall(r'@\w+\{([^,]+),', (PAPER / 'references.bib').read_text())
    require(set(bib_keys) == set(source_bib_keys), 'Bibliography entry loss')
    for tex in (PAPER / 'sections').glob('*.tex'):
        require('sections/' + tex.name in (PAPER / 'main.tex').read_text(), 'Orphaned section: ' + tex.name)
    result = dict(status='PASS', purpose='Preservation and presentation, not theorem certification',
                  protected_files=preserved, unchanged_formal_blocks=formal_count,
                  preserved_displayed_math_blocks=preserved_display_count,
                  references=len(bib_keys), reference_start_page=reference_pages[0],
                  embedded_font_entries=len(fonts), pages=pages,
                  pdf_sha256=digest(PAPER / 'main.pdf'), warnings=warnings)
    (ROOT / 'validation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


def render():
    pdf = PAPER / 'main.pdf'
    original_hash = digest(pdf)
    count = int(re.search(r'Pages:\s+(\d+)', run(['pdfinfo', str(pdf)])).group(1))
    directory = Path(tempfile.mkdtemp(prefix='tpc-wiki-revision-pages-'))
    subprocess.run(['pdftoppm', '-r', '105', '-png', str(pdf), str(directory / 'page')], check=True)
    images = sorted(directory.glob('page-*.png'))
    require(len(images) == count and digest(pdf) == original_hash, 'Incomplete rendering or changed PDF')
    manifest = dict(pdf_sha256=original_hash, pages=[dict(page=i, image=str(p), sha256=digest(p))
                    for i, p in enumerate(images, 1)])
    (ROOT / 'render_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Rendered', count, 'pages into', directory)


def package():
    """Create a portable source-only ZIP and a complete editorial TeX diff."""
    checks()
    files = sorted(PAPER.glob('*.tex')) + [PAPER / 'references.bib']
    files += sorted((PAPER / 'sections').glob('*.tex'))
    files += sorted(p for p in (PAPER / 'figures').glob('*') if p.is_file())
    files += [ROOT / 'BUILD_SOURCE.md']
    destination = ROOT / 'english_v0.2_source.zip'
    manifest = {str(p.relative_to(ROOT)): digest(p) for p in files}
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in files:
            archive.write(p, str(p.relative_to(ROOT)))
        archive.writestr('SOURCE_MANIFEST.json', json.dumps(manifest, indent=2) + '\n')
    differences = []
    for revised in sorted(PAPER.rglob('*.tex')):
        relative = revised.relative_to(PAPER)
        baseline = ORIGINAL / 'paper-en' / relative
        old = baseline.read_text().splitlines(keepends=True) if baseline.exists() else []
        differences.extend(difflib.unified_diff(old, revised.read_text().splitlines(keepends=True),
                           fromfile='english-v0.1/' + str(relative),
                           tofile='english-v0.2/' + str(relative)))
    (ROOT / 'REVISION_DIFF.patch').write_text(''.join(differences))
    with zipfile.ZipFile(destination) as archive:
        require(archive.testzip() is None, 'Source ZIP checksum failure')
        require(set(archive.namelist()) == set(manifest) | {'SOURCE_MANIFEST.json'}, 'Unexpected ZIP member')
        for name, expected in manifest.items():
            require(hashlib.sha256(archive.read(name)).hexdigest() == expected, 'ZIP source mismatch: ' + name)
    receipt = dict(archive=destination.name, sha256=digest(destination), source_files=len(files),
                   bytes=destination.stat().st_size, member_hashes_verified=True)
    (ROOT / 'source_package.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['init', 'build', 'check', 'render', 'package'])
    parser.add_argument('--round', type=int, choices=[1, 2], default=1)
    args = parser.parse_args()
    if args.action == 'init':
        initialize()
    elif args.action == 'build':
        build(args.round)
    elif args.action == 'check':
        checks()
    elif args.action == 'render':
        render()
    else:
        package()
