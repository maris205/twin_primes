#!/usr/bin/env python3
"""Render the exact current PDF externally and record every page hash."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

PAPER = Path(__file__).resolve().parents[1] / 'paper'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    pdf = PAPER / 'main.pdf'
    original = digest(pdf)
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    count = int(re.search(r'Pages:\s+(\d+)', info).group(1))
    directory = Path(tempfile.mkdtemp(prefix='tpc-monograph-final-visual-'))
    command = ['pdftoppm', '-r', '105', '-png', str(pdf), str(directory / 'page')]
    subprocess.run(command, check=True)
    pages = sorted(directory.glob('page-*.png'))
    if len(pages) != count or digest(pdf) != original:
        raise ValueError('PDF changed during rendering or incomplete page sequence')
    result = dict(pdf='main.pdf', pdf_sha256=original, page_count=count, command=command,
                  purpose='Rendering provenance, not proof verification',
                  pages=[dict(page=i, image=str(path), sha256=digest(path)) for i,path in enumerate(pages,1)])
    (PAPER / 'render_manifest.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(directory=str(directory), pages=count, pdf_sha256=original)))

if __name__ == '__main__':
    main()
