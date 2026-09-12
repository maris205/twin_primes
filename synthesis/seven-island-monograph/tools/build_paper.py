#!/usr/bin/env python3
"""Build only this synthesis in an external scratch directory; preserve logs."""
import argparse
import pathlib
import shutil
import subprocess
import tempfile

PROJECT = pathlib.Path(__file__).resolve().parents[1]
PAPER = PROJECT / 'paper'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--snapshot', choices=['round0_original', 'round1', 'round2'])
    args = parser.parse_args()
    build = pathlib.Path(tempfile.mkdtemp(prefix='tpc-monograph-build-'))
    result = subprocess.run(['latexmk', '-xelatex', '-interaction=nonstopmode',
                             '-halt-on-error', f'-outdir={build}', 'main.tex'],
                            cwd=PAPER, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (PAPER / 'compile.log').write_bytes(result.stdout)
    if (build / 'main.log').exists():
        shutil.copy2(build / 'main.log', PAPER / 'main.log')
    print('Build scratch:', build)
    if result.returncode:
        print(result.stdout.decode(errors='replace')[-6000:])
        raise SystemExit(result.returncode)
    shutil.copy2(build / 'main.pdf', PAPER / 'main.pdf')
    if args.snapshot:
        for suffix in ['pdf', 'log']:
            shutil.copy2(PAPER / f'main.{suffix}', PAPER / f'main_{args.snapshot}.{suffix}')
    subprocess.run(['pdftotext', '-layout', str(PAPER / 'main.pdf'), str(PAPER / 'main.txt')], check=True)
    converted = subprocess.check_output(['pandoc', '-f', 'latex', '-t', 'markdown', '--wrap=none',
                    'main.tex'], cwd=PAPER, text=True)
    abstract = subprocess.check_output(['pandoc', '-f', 'latex', '-t', 'markdown', '--wrap=none',
                    'sections/abstract.tex'], cwd=PAPER, text=True)
    title = '# 孪生素数研究的七岛框架：精确结构、解析障碍与两类桥接问题\n\n'
    (PAPER / 'main.md').write_text(title + '统一中文研究母稿；公式编号与排版以 [PDF](main.pdf) 为准。引文键对应 [书目](references.bib)。\n\n## 摘要\n\n' + abstract + '\n' + converted)
    print(subprocess.check_output(['pdfinfo', str(PAPER / 'main.pdf')], text=True))

if __name__ == '__main__':
    main()
