#!/usr/bin/env python3
"""Read-only integrity checks for this Git delivery; not theorem verification."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
EDITION = ROOT / "edition"
PDF_SHA256 = "916693565d81741756af7fcd6151a9e583b1f96a03cd50d2628149be745e0f41"
ZIP_SHA256 = "a1c73088829d00c7995cfc98e4f172e21e76c56fd988e7409a0225a33392a118"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(directory):
    require(not any(p.is_symlink() for p in directory.rglob("*")), "Unexpected symlink")
    return {str(p.relative_to(directory)): digest(p)
            for p in sorted(directory.rglob("*")) if p.is_file()}


def verify(original=None):
    manifest = json.loads((ROOT / "IMPORT_MANIFEST.json").read_text())
    require(inventory(EDITION) == manifest["files"], "Delivery snapshot differs from manifest")
    if original is not None:
        require(inventory(original) == manifest["files"], "Original workspace edition changed")
        baseline = json.loads((original / "baseline_lock.json").read_text())
        for path, expected in baseline.items():
            require(digest(original.parent / path) == expected, "Protected source changed: " + path)

    require(digest(EDITION / "paper/main.pdf") == PDF_SHA256, "Wrong final PDF")
    require(digest(EDITION / "paper/main_round2.pdf") == PDF_SHA256, "PDF alias mismatch")
    require(digest(EDITION / "english_v0.3_source.zip") == ZIP_SHA256, "Wrong source ZIP")
    build = json.loads((EDITION / "build_manifest.json").read_text())
    require(build["pdf_sha256"] == PDF_SHA256, "Build receipt PDF mismatch")
    for path, expected in build["source_files"].items():
        require(digest(EDITION / "paper" / path) == expected, "Build source changed: " + path)

    matrix = json.loads((EDITION / "CORE_SOURCE_MATRIX.json").read_text())
    for entry in matrix["sources"]:
        path = REPO / entry["path"]
        require(path.resolve().is_relative_to(REPO), "Source path escapes repository")
        require(digest(path) == entry["sha256"], "Mathematical source changed: " + entry["id"])
        subprocess.run(["git", "ls-files", "--error-unmatch", "--", entry["path"]],
                       cwd=REPO, check=True, stdout=subprocess.DEVNULL)

    with zipfile.ZipFile(EDITION / "english_v0.3_source.zip") as archive:
        require(archive.testzip() is None, "Source ZIP CRC failure")
        sources = json.loads(archive.read("SOURCE_MANIFEST.json"))
        require(set(archive.namelist()) == set(sources) | {"SOURCE_MANIFEST.json"},
                "Unexpected source ZIP contents")
        for path, expected in sources.items():
            require(not Path(path).is_absolute() and ".." not in Path(path).parts,
                    "Unsafe ZIP member path")
            require(hashlib.sha256(archive.read(path)).hexdigest() == expected,
                    "ZIP member hash mismatch: " + path)
            require(digest(EDITION / path) == expected, "ZIP differs from edition: " + path)

    visual = json.loads((EDITION / "visual_receipt.json").read_text())
    require(visual["pdf_sha256"] == PDF_SHA256, "Historical visual receipt PDF mismatch")
    require(visual["pages_inspected"] == list(range(1, 31)), "Historical page coverage incomplete")
    require(digest(EDITION / visual["raw_report"]) == visual["raw_report_sha256"],
            "Historical raw visual report changed")
    review_log = (EDITION / "paper/PAPER_IMPROVEMENT_LOG.md").read_text()
    for number in (1, 2):
        raw = (EDITION / f"reviews/ROUND{number}_RAW.md").read_text().rstrip("\n")
        require(raw in review_log, "Raw editorial review missing from historical log")
    portable = json.loads((EDITION / "portable_build.json").read_text())
    require(portable["final_pdf_sha256"] == PDF_SHA256 and
            portable["archive_sha256"] == ZIP_SHA256,
            "Historical portable receipt mismatch")

    links = 0
    for name in ("README.md", "SOURCES.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", (ROOT / name).read_text()):
            if re.match(r"(?:https?|mailto):|#", target):
                continue
            require((ROOT / unquote(target.split("#", 1)[0])).exists(),
                    "Broken repository-facing link: " + target)
            links += 1
    return dict(status="PASS", scope="Git delivery integrity, not mathematical certification",
                snapshot_files=len(manifest["files"]), tracked_primary_sources=len(matrix["sources"]),
                portable_source_members=len(sources), repository_facing_links=links,
                final_pdf_sha256=PDF_SHA256, source_zip_sha256=ZIP_SHA256,
                historical_review_hash_bindings_verified=True,
                original_workspace_and_protected_sources_checked=original is not None)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original", type=Path,
                        help="Optional original workspace edition for copy/preservation comparison")
    args = parser.parse_args()
    print(json.dumps(verify(args.original), indent=2))
