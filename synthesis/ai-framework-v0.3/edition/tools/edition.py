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
from urllib.parse import unquote
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
REPO = WORKSPACE / 'twin_primes'
ORIGINAL = REPO / 'synthesis/seven-island-monograph'
BASELINE = WORKSPACE / 'tpc_english_revision'
PAPER = ROOT / 'paper'
LOCK = ROOT / 'baseline_lock.json'
FORMAL = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|condition|proof)\}.*?\\end\{\1\}', re.S)
DISPLAY = re.compile(r'\\\[.*?\\\]|\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}', re.S)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def paper_sources():
    files = list(PAPER.glob('*.tex')) + [PAPER / 'references.bib']
    files += list((PAPER / 'sections').glob('*.tex'))
    files += [p for p in (PAPER / 'figures').glob('*') if p.is_file()]
    return {str(p.relative_to(PAPER)): digest(p) for p in sorted(files)}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def protected_files():
    files = {p for folder in ('paper', 'paper-en')
             for p in (ORIGINAL / folder).rglob('*') if p.is_file()}
    files.update(p for p in BASELINE.rglob('*') if p.is_file())
    files.update(WORKSPACE / 'tpc_obsidian_vault' / name for name in (
        '00_开始阅读.md', '99_维护/验收报告.md', '99_维护/使用与更新说明.md',
        '99_维护/validation_results.json', '_tools/validate_vault.py'))
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
    source_snapshot = paper_sources()
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
    (PAPER / 'main.md').write_text('# A Source-Traceable Framework for AI-Assisted Research on the Twin Prime Conjecture\n\n'
        'Liang Wang, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430070, P.R. China; wangliang.f@gmail.com.\n\nEnglish revision v0.3. PDF numbering and layout are authoritative.\n\n## Abstract\n\n'
        + convert('sections/abstract.tex') + '\n' + convert('main.tex'))
    check_preservation()
    require(paper_sources() == source_snapshot, 'Paper sources changed during compilation')
    (ROOT / 'build_manifest.json').write_text(json.dumps(
        dict(round=round_number, pdf_sha256=digest(PAPER / 'main.pdf'),
             source_files=source_snapshot), indent=2) + '\n')
    print(run(['pdfinfo', str(PAPER / 'main.pdf')]))
    print('Scratch:', scratch)


def checks():
    preserved = check_preservation()
    build_manifest = json.loads((ROOT / 'build_manifest.json').read_text())
    require(build_manifest['source_files'] == paper_sources(), 'Paper changed since last build')
    require(build_manifest['pdf_sha256'] == digest(PAPER / 'main.pdf'), 'PDF differs from recorded build')
    formal_count = 0
    preserved_display_count = 0
    for original in sorted((BASELINE / 'paper/sections').glob('*.tex')):
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
    require((PAPER / 'references.bib').read_text().startswith((BASELINE / 'paper/references.bib').read_text()), 'Original bibliography entries modified')
    for name in ('math_commands.tex', 'figures/tpc_route_en.png'):
        require(digest(PAPER / name) == digest(BASELINE / 'paper' / name), 'Shared asset changed: ' + name)
    log = (PAPER / 'main.log').read_text()
    warnings = [line for line in log.splitlines() if re.search(
        r'Overfull|Underfull|undefined|Missing character|multiply defined', line)]
    require(not warnings, 'Unresolved layout/reference warnings: ' + repr(warnings))
    fonts = (PAPER / 'fonts.txt').read_text().splitlines()[2:]
    require(fonts and all(re.search(r'\s+yes\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$', line) for line in fonts), 'Unembedded font')
    text = (PAPER / 'main.txt').read_text()
    require('\ufffd' not in text, 'Replacement glyph in extracted text')
    for required in ('Liang Wang', 'School of Artificial Intelligence and Automation',
                     'Huazhong University of Science and Technology', 'Wuhan 430070, P.R. China',
                     'wangliang.f@gmail.com', 'AI-Assisted', 'Research agenda'):
        require(required in text, 'Required author/framing content missing: ' + required)
    require('??' not in text and '[?]' not in text and '[VERIFY]' not in text, 'Unresolved text placeholder')
    info = run(['pdfinfo', str(PAPER / 'main.pdf')])
    require(re.search(r'^Author:\s+Liang Wang\s*$', info, re.M), 'PDF author metadata mismatch')
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
                  build_source_hashes_verified=True,
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
    destination = ROOT / 'english_v0.3_source.zip'
    manifest = {str(p.relative_to(ROOT)): digest(p) for p in files}
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in files:
            archive.write(p, str(p.relative_to(ROOT)))
        archive.writestr('SOURCE_MANIFEST.json', json.dumps(manifest, indent=2) + '\n')
    differences = []
    for revised in sorted(PAPER.rglob('*.tex')):
        relative = revised.relative_to(PAPER)
        baseline = BASELINE / 'paper' / relative
        old = baseline.read_text().splitlines(keepends=True) if baseline.exists() else []
        differences.extend(difflib.unified_diff(old, revised.read_text().splitlines(keepends=True),
                           fromfile='english-v0.2/' + str(relative),
                           tofile='english-v0.3/' + str(relative)))
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


def portable():
    """Rebuild the source-only package without workspace dependencies."""
    check_preservation()
    archive_path = ROOT / 'english_v0.3_source.zip'
    scratch = Path(tempfile.mkdtemp(prefix='tpc-ai-portable-source-'))
    with zipfile.ZipFile(archive_path) as archive:
        require(archive.testzip() is None, 'Corrupt source ZIP')
        manifest = json.loads(archive.read('SOURCE_MANIFEST.json'))
        require(set(archive.namelist()) == set(manifest) | {'SOURCE_MANIFEST.json'},
                'Unexpected portable source member')
        for name, expected in manifest.items():
            relative = Path(name)
            require(not relative.is_absolute() and '..' not in relative.parts,
                    'Unsafe archive path: ' + name)
            require(hashlib.sha256(archive.read(name)).hexdigest() == expected,
                    'Portable source hash mismatch: ' + name)
        archive.extractall(scratch)
    source = scratch / 'paper'
    process = subprocess.run(
        ['latexmk', '-pdf', '-no-shell-escape', '-interaction=nonstopmode',
         '-halt-on-error', 'main.tex'],
        cwd=source, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (ROOT / 'portable_compile.log').write_bytes(process.stdout)
    require(process.returncode == 0, 'Portable source build failed')
    log = (source / 'main.log').read_text()
    warnings = [line for line in log.splitlines()
                if re.search(r'Overfull|Underfull|undefined|Missing character|multiply defined', line)]
    require(not warnings, 'Portable build warnings: ' + repr(warnings))
    extracted = run(['pdftotext', '-layout', str(source / 'main.pdf'), '-'])
    require(extracted == (PAPER / 'main.txt').read_text(),
            'Portable PDF text/layout differs from final edition')
    receipt = dict(status='PASS', scope='Standalone source build, not mathematical verification',
                   archive_sha256=digest(archive_path), final_pdf_sha256=digest(PAPER / 'main.pdf'),
                   rebuilt_pdf_sha256=digest(source / 'main.pdf'),
                   identical_extracted_text=True, warnings=warnings, scratch=str(scratch))
    (ROOT / 'portable_build.json').write_text(json.dumps(receipt, indent=2) + '\n')
    check_preservation()
    print(json.dumps(receipt, indent=2))


def delivery():
    """Check final aliases, review retention, render identity, and companion links."""
    checks()
    require(digest(PAPER / 'main.pdf') == digest(PAPER / 'main_round2.pdf'),
            'Final PDF alias mismatch')
    require(digest(PAPER / 'main_round0_original.pdf') == digest(BASELINE / 'paper/main.pdf'),
            'Preserved baseline PDF mismatch')
    state = json.loads((PAPER / 'PAPER_IMPROVEMENT_STATE.json').read_text())
    require(state['status'] == 'completed', 'Final review/visual state is not complete')
    log = (PAPER / 'PAPER_IMPROVEMENT_LOG.md').read_text()
    for number in (1, 2):
        raw = (ROOT / 'reviews' / f'ROUND{number}_RAW.md').read_text().rstrip('\n')
        require(raw in log, f'Round {number} raw report not retained verbatim in log')
    render = json.loads((ROOT / 'render_manifest.json').read_text())
    visual = json.loads((ROOT / 'visual_receipt.json').read_text())
    pdf_hash = digest(PAPER / 'main.pdf')
    require(render['pdf_sha256'] == visual['pdf_sha256'] == pdf_hash,
            'Render or visual receipt belongs to a different PDF')
    page_numbers = [entry['page'] for entry in render['pages']]
    require(visual['pages_inspected'] == page_numbers, 'Incomplete recorded visual coverage')
    for entry in render['pages']:
        require(digest(Path(entry['image'])) == entry['sha256'], 'Rendered page changed')
    require(digest(ROOT / 'reviews/FINAL_VISUAL_RAW.md') == visual['raw_report_sha256'],
            'Visual raw report changed')
    portable_receipt = json.loads((ROOT / 'portable_build.json').read_text())
    require(portable_receipt['final_pdf_sha256'] == pdf_hash and
            portable_receipt['archive_sha256'] == digest(ROOT / 'english_v0.3_source.zip'),
            'Portable build receipt is stale')
    documents = ['README.md', 'FRAMEWORK_SOURCE_MAP.md', 'WIKI_REVISION_CROSSWALK.md',
                 'CORE_SOURCE_MATRIX.md', 'BUILD_SOURCE.md', 'QA_REPORT.md',
                 'REVISION_PLAN.md', 'EXTERNAL_REFERENCE_CHECK.md',
                 'refine-logs/EXPERIMENT_PLAN.md', 'refine-logs/EXPERIMENT_TRACKER.md']
    checked_links = 0
    for name in documents:
        document = ROOT / name
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', document.read_text()):
            target = target.strip().strip('<>')
            if re.match(r'(?:https?|mailto):|#', target):
                continue
            path = unquote(target.split('#', 1)[0])
            require((document.parent / path).exists(), f'Broken local link in {name}: {target}')
            checked_links += 1
    result = dict(status='PASS', scope='Delivery integrity and documented presentation coverage only',
                  pdf_sha256=pdf_hash, pages_with_recorded_visual_inspection=len(page_numbers),
                  companion_local_links_checked=checked_links,
                  raw_reviews_retained=True, portable_receipt_current=True)
    (ROOT / 'delivery_check.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['init', 'build', 'check', 'render', 'package', 'portable', 'delivery'])
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
    elif args.action == 'portable':
        portable()
    elif args.action == 'delivery':
        delivery()
    else:
        package()
