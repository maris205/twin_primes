#!/usr/bin/env python3
"""Preserve and verify the scoped editorial/wiki import, never mathematical truth.

--record-originals creates the import manifest once from the original workspace.
Normal verification is read-only; --report writes only a derived validation receipt.
"""
import argparse
from collections import Counter
import contextlib
import hashlib
import importlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote

REPO = Path(__file__).resolve().parents[1]
WORKSPACE = REPO.parent
MANIFEST = REPO / "docs/EDITORIAL_MATERIALS_MANIFEST.json"
GROUPS = (
    ("wiki", "reading/tpc_obsidian_vault", "tpc_obsidian_vault"),
    ("english-v0.2", "synthesis/wiki-informed-english-v0.2/edition", "tpc_english_revision"),
    ("original-synthesis", "synthesis/seven-island-monograph", "twin_primes/synthesis/seven-island-monograph"),
    ("ai-v0.3", "synthesis/ai-framework-v0.3/edition", "tpc_ai_framework"),
)
EXCLUDED_PARTS = {".build", "__pycache__", ".ipynb_checkpoints", ".pytest_cache",
                  "node_modules", ".venv", "venv", ".git"}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    files = {}
    exclusions = Counter()
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        reason = next((part for part in relative.parts if part in EXCLUDED_PARTS), None)
        if reason:
            if path.is_file():
                exclusions[reason] += 1
            continue
        require(not path.is_symlink(), "Unexpected link: " + str(path))
        if path.is_file():
            files[str(relative)] = {"sha256": digest(path), "bytes": path.stat().st_size}
    return files, dict(exclusions)


def record_originals():
    require(not MANIFEST.exists(), "Refusing to replace the original import manifest")
    groups = []
    for ident, destination, source in GROUPS:
        files, excluded = inventory(WORKSPACE / source)
        require(files, "Empty original group: " + ident)
        groups.append(dict(id=ident, repo_path=destination, original_workspace_path=source,
                           files=files, excluded_local_cache_files=excluded))
    aliases = []
    for language in ("paper", "paper-en"):
        prefix = "synthesis/seven-island-monograph/" + language
        local = REPO / prefix / ".ipynb_checkpoints/main-checkpoint.pdf"
        canonical = REPO / prefix / "main.pdf"
        require(digest(local) == digest(canonical), "Checkpoint is not an exact PDF duplicate")
        aliases.append(dict(excluded_path=str(local.relative_to(REPO)),
                            canonical_path=str(canonical.relative_to(REPO)),
                            sha256=digest(canonical)))
    wiki = WORKSPACE / "tpc_obsidian_vault"
    raw_audits = []
    for source in sorted((wiki / ".build").glob("*_RAW.md")):
        retained = wiki / "99_维护/原始审阅" / (source.name + ".txt")
        require(digest(source) == digest(retained), "Cached raw review not retained verbatim")
        raw_audits.append(dict(excluded_cache_source=str(source.relative_to(wiki)),
                               retained_wiki_path=str(retained.relative_to(wiki)),
                               sha256=digest(retained)))
    value = dict(scope="Complete scoped editorial/wiki artifacts, excluding regenerable local caches",
                 groups=groups, excluded_notebook_pdf_aliases=aliases,
                 raw_audits_retained_outside_cache=raw_audits)
    MANIFEST.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    return value


def verify(compare_originals=False):
    manifest = json.loads(MANIFEST.read_text())
    summary = {}
    for group in manifest["groups"]:
        root = REPO / group["repo_path"]
        actual, excluded = inventory(root)
        require(actual == group["files"], "Imported files differ: " + group["id"])
        require(all(item["bytes"] < 50 * 1024 * 1024 for item in actual.values()),
                "Unexpected large file needs explicit review")
        if compare_originals:
            original, _ = inventory(WORKSPACE / group["original_workspace_path"])
            require(original == group["files"], "Original workspace changed: " + group["id"])
        summary[group["id"]] = dict(files=len(actual), bytes=sum(v["bytes"] for v in actual.values()))
    for row in manifest["excluded_notebook_pdf_aliases"]:
        require(digest(REPO / row["canonical_path"]) == row["sha256"], "Canonical PDF changed")
    wiki = REPO / "reading/tpc_obsidian_vault"
    for row in manifest["raw_audits_retained_outside_cache"]:
        require(digest(wiki / row["retained_wiki_path"]) == row["sha256"], "Raw audit changed")
    generated = json.loads((wiki / "99_维护/generated_manifest.json").read_text())
    require(not generated.get("build_incomplete"), "Wiki generation was incomplete")
    for path, expected in generated["files"].items():
        require(digest(wiki / path) == expected, "Wiki generated-file mismatch: " + path)
    sources = json.loads((wiki / "99_维护/source_manifest.json").read_text())["source_files"]
    for name, entry in sources.items():
        require(digest(wiki / entry["vault_path"]) == entry["sha256"], "Source-copy mismatch: " + name)
    require(len(list((wiki / "03_全文").glob("*.md"))) == 419, "Fulltext coverage changed")
    require(len(list((wiki / "02_论文").glob("*.md"))) == 420, "Directory identity coverage changed")
    require(len(list((wiki / "04_知识卡片").glob("K*.md"))) == 14, "Card coverage changed")
    # The v0.3 snapshot and its primary mathematical inputs were already published.
    result = subprocess.run(
        [sys.executable, "-B", str(REPO / "synthesis/ai-framework-v0.3/tools/verify_bundle.py")],
        text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    require(result.returncode == 0, "Existing v0.3 bundle validation failed: " + result.stdout)
    ai_result = json.loads(result.stdout)
    protected_count = 0
    if compare_originals:
        original_ai = WORKSPACE / "tpc_ai_framework"
        lock = json.loads((original_ai / "baseline_lock.json").read_text())
        for path, expected in lock.items():
            require(digest(WORKSPACE / path) == expected, "Protected original changed: " + path)
        protected_count = len(lock)
    links = 0
    for name in ("docs/EDITORIAL_MATERIALS.md", "reading/README.md",
                 "synthesis/wiki-informed-english-v0.2/README.md",
                 "synthesis/ai-framework-v0.3/README.md"):
        document = REPO / name
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document.read_text()):
            if re.match(r"(?:https?|mailto):|#", target):
                continue
            require((document.parent / unquote(target.split("#", 1)[0])).exists(),
                    "Broken repository-facing link: " + target)
            links += 1
    return dict(status="PASS", scope="Artifact and source fidelity; no mathematical certification",
                groups=summary, wiki_generated_files_checked=len(generated["files"]),
                wiki_source_copies_checked=len(sources), repository_facing_links_checked=links,
                raw_audits_retained=len(manifest["raw_audits_retained_outside_cache"]),
                original_protected_files_checked=protected_count,
                ai_v0_3_final_pdf_sha256=ai_result["final_pdf_sha256"])


def wiki_navigation():
    """Run the existing link checker with its only cache write redirected to /tmp."""
    wiki = REPO / "reading/tpc_obsidian_vault"
    sys.path.insert(0, str(wiki / "_tools"))
    checker = importlib.import_module("validate_vault")
    scratch = Path(tempfile.mkdtemp(prefix="tpc-import-wiki-links-"))
    checker.CACHE = scratch
    old_argv = sys.argv
    output = io.StringIO()
    try:
        sys.argv = ["validate_vault.py"]  # No --report and no prior-cache reuse.
        with contextlib.redirect_stdout(output):
            checker.main()
    finally:
        sys.argv = old_argv
    transcript = output.getvalue()
    print(transcript)
    start = transcript.find("{")
    require(start >= 0, "No navigation summary returned")
    parsed = json.loads(transcript[start:])
    require(parsed["status"] == "PASS", "Navigation did not pass")
    return dict(status=parsed["status"], note_count=parsed["note_count"],
                internal_links=parsed["internal_links"],
                unreachable_core_notes=parsed["unreachable_core_notes"],
                cache_write_location=str(scratch),
                scope="Fresh Markdown/Obsidian internal navigation parsing, not desktop or proof verification")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record-originals", action="store_true")
    parser.add_argument("--compare-originals", action="store_true")
    parser.add_argument("--wiki-links", action="store_true", help="Requires Pandoc; fresh internal link parsing")
    parser.add_argument("--report", action="store_true", help="Write derived import verification receipt only")
    args = parser.parse_args()
    if args.record_originals:
        record_originals()
    report = verify(args.compare_originals)
    if args.wiki_links:
        report["fresh_wiki_navigation"] = wiki_navigation()
        # Detect any unexpected mutation by the imported checker.
        verify(args.compare_originals)
    if args.report:
        (REPO / "docs/EDITORIAL_MATERIALS_VALIDATION.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
