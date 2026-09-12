#!/usr/bin/env python3
"""Build the separate English edition, preserving the Chinese baseline."""
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import tempfile

PROJECT = pathlib.Path(__file__).resolve().parents[1]
PAPER = PROJECT / 'paper-en'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    baseline = {str(p.relative_to(PROJECT)): digest(p)
                for p in sorted((PROJECT / 'paper').rglob('*')) if p.is_file()}
    lock = PAPER / 'chinese_baseline_lock.json'
    if lock.exists() and json.loads(lock.read_text()) != baseline:
        raise RuntimeError('Chinese baseline changed since first English build')
    lock.write_text(json.dumps(baseline, indent=2) + '\n')
    build = pathlib.Path(tempfile.mkdtemp(prefix='tpc-english-build-'))
    result = subprocess.run(['latexmk', '-pdf', '-interaction=nonstopmode',
                             '-halt-on-error', f'-outdir={build}', 'main.tex'],
                            cwd=PAPER, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (PAPER / 'compile.log').write_bytes(result.stdout)
    if (build / 'main.log').exists():
        shutil.copy2(build / 'main.log', PAPER / 'main.log')
    print('Build scratch:', build)
    if result.returncode:
        print(result.stdout.decode(errors='replace')[-6500:])
        raise SystemExit(result.returncode)
    shutil.copy2(build / 'main.pdf', PAPER / 'main.pdf')
    subprocess.run(['pdftotext', '-layout', str(PAPER / 'main.pdf'), str(PAPER / 'main.txt')], check=True)
    convert = lambda name: subprocess.check_output(
        ['pandoc', '-f', 'latex', '-t', 'markdown', '--wrap=none', name], cwd=PAPER, text=True)
    title = '# A Seven-Island Framework for Twin-Prime Research\n\n'
    subtitle = 'Exact Structures, Analytic Obstructions, and Two Bridging Problems\n\n'
    (PAPER / 'main.md').write_text(title + subtitle +
        'Complete English synthesis. The [PDF](main.pdf) is authoritative for equation numbering and layout; citation keys refer to the [bibliography](references.bib).\n\n## Abstract\n\n' +
        convert('sections/abstract.tex') + '\n' + convert('main.tex'))
    after = {str(p.relative_to(PROJECT)): digest(p)
             for p in sorted((PROJECT / 'paper').rglob('*')) if p.is_file()}
    if after != baseline:
        raise RuntimeError('Chinese files changed during English build')
    print(subprocess.check_output(['pdfinfo', str(PAPER / 'main.pdf')], text=True))
    log = (PAPER / 'main.log').read_text()
    print('Layout warnings:', '\n'.join(line for line in log.splitlines()
          if re.search(r'Overfull|Underfull|undefined|Missing character', line)))

if __name__ == '__main__':
    main()
