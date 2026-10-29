"""Build the arXiv package in arxiv/: ASCII sources, the date line without "Draft",
and the pre-generated main.bbl (arXiv does not run BibTeX).

usage: python make_arxiv.py   (after a full local build that produced main.bbl)
"""
import io, os, re, shutil, tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "arxiv")
FILES = ["main.tex", "ai_workflow.tex", "roadmap.tex", "exploration_map.tex", "main.bbl"]
ACCENTS = {
    "\u00e0": r"{\`a}", "\u00e1": r"{\'a}", "\u00e4": r"{\"a}", "\u00f3": r"{\'o}",
    "\u00f6": r"{\"o}", "\u00fc": r"{\"u}", "\u0142": r"{\l}", "\u00e9": r"{\'e}",
}

os.makedirs(OUT, exist_ok=True)
for f in FILES:
    s = io.open(os.path.join(HERE, f), encoding="utf-8").read()
    for k, v in ACCENTS.items():
        s = s.replace(k, v)
    if f == "main.tex":
        s = re.sub(r"\\date\{Draft (v[0-9.]+), ", r"\\date{", s)
    bad = sorted(set(c for c in s if ord(c) > 127))
    assert not bad, (f, bad)
    io.open(os.path.join(OUT, f), "w", encoding="ascii", newline="\n").write(s)

tar = os.path.join(HERE, "arxiv_submission.tar.gz")
with tarfile.open(tar, "w:gz") as t:
    for f in FILES:
        t.add(os.path.join(OUT, f), arcname=f)
print("wrote", tar)
