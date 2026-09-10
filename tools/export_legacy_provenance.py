#!/usr/bin/env python3
"""Export authentic, TPC-scoped legacy Git objects from a separate source repo.

This is an explicit one-time migration builder, not a scientific result
generator. It never changes the source repository. Packs contain original
commit/root/intermediate tree objects and only TPC/shared-context payloads;
unrelated RH project trees and blobs are not traversed or exported.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import re
import subprocess


ROOT_FILES = {
    "AGENTS.md", "README.md", "AUTO_REVIEW.md", "DERIVATION_PACKAGE.md",
    "IDEA_REPORT.md", "PROOF_PACKAGE.md", "REVIEW_STATE.json", "TPC_COMPASS.md",
    "TPC_HANDOFF.md", "codex_prompt.md",
}
CONTAINERS = {"papers", "research"}
OID = re.compile(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")


def selected(path: str) -> bool:
    return (path in ROOT_FILES or path.startswith("papers/tpc-")
            or path == "research/tpc-big-road"
            or path.startswith("research/tpc-big-road/"))


def git(repo: Path, *args: str, data: bytes | None = None) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=True).stdout


def tree(repo: Path, commit: str):
    for entry in git(repo, "ls-tree", "-r", "-t", "-z", "--full-tree", commit).split(b"\0"):
        if not entry:
            continue
        meta, raw_path = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split()
        yield mode, kind, oid, raw_path.decode("utf-8")


def sha256(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


@contextmanager
def committed_blobs(repo: Path):
    process = subprocess.Popen(["git", "-C", str(repo), "cat-file", "--batch"],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    def read(oid: str) -> bytes:
        process.stdin.write((oid + "\n").encode())
        process.stdin.flush()
        header = process.stdout.readline().decode().strip().split()
        if len(header) != 3 or header[:2] != [oid, "blob"]:
            raise ValueError("unexpected Git blob response")
        size = int(header[2])
        data = process.stdout.read(size)
        if len(data) != size or process.stdout.read(1) != b"\n":
            raise ValueError("truncated Git blob response")
        return data
    try:
        yield read
    finally:
        process.stdin.close()
        error = process.stderr.read()
        code = process.wait()
        if code or error:
            raise ValueError("Git blob reader failed")


def write_json(path: Path, value) -> None:
    if path.exists():
        raise ValueError(f"refusing to overwrite migration evidence: {path}")
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--target", type=Path, required=True)
    args = parser.parse_args()
    source, target = args.source.resolve(), args.target.resolve()
    if source == target or source in target.parents or target in source.parents:
        raise ValueError("migration source and target must be separate sibling repositories")
    commit = git(source, "rev-parse", args.commit + "^{commit}").decode().strip()
    if commit != args.commit or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("an exact existing source commit is required")
    destination = git(target, "remote", "get-url", "origin").decode().strip()
    if destination != "git@github.com:maris205/twin_primes.git":
        raise ValueError("unexpected migration target or non-SSH origin")
    evidence = target / "provenance"
    packs = evidence / "git-objects/pack"
    if packs.exists() and any(packs.iterdir()):
        raise ValueError("provenance pack directory is not empty")
    evidence.mkdir(exist_ok=True)
    packs.mkdir(parents=True, exist_ok=True)

    baseline, candidates, newline_differences = [], defaultdict(set), []
    candidates[commit].add("migration snapshot")
    with committed_blobs(source) as read_blob:
        for mode, kind, oid, path in tree(source, commit):
            if kind != "blob" or not selected(path):
                continue
            if mode not in {"100644", "100755"}:
                raise ValueError(f"unsupported current source mode {mode}: {path}")
            blob = read_blob(oid)
            worktree = (source / path).read_bytes()
            if blob != worktree:
                if blob != worktree.replace(b"\r\n", b"\n"):
                    raise ValueError(f"unexplained source worktree difference: {path}")
                newline_differences.append({"path": path,
                                            "worktree_sha256": sha256(worktree),
                                            "reason": "Git-canonical CRLF-to-LF representation"})
            baseline.append({"path": path, "mode": mode, "git_blob": oid,
                             "sha256": sha256(blob), "bytes": len(blob)})
            if path.endswith(".py") or path.endswith("/CONVERSION_RECORD.md"):
                for candidate in OID.findall(blob.decode("utf-8")):
                    candidates[candidate].add(path)
    candidate_ids = sorted(candidates)
    checked = git(source, "cat-file", "--batch-check=%(objectname) %(objecttype)",
                  data=("\n".join(candidate_ids) + "\n").encode()).decode().splitlines()
    commits = [line.split()[0] for line in checked if line.endswith(" commit")]
    if commit not in commits:
        raise ValueError("migration source commit missing from provenance selection")

    objects, snapshots = {}, []
    for number, historical in enumerate(commits, 1):
        root_tree = git(source, "rev-parse", historical + "^{tree}").decode().strip()
        objects[historical], objects[root_tree] = "commit", "tree"
        count, directories = 0, set()
        for mode, kind, oid, path in tree(source, historical):
            if path not in CONTAINERS and not selected(path):
                continue
            if kind not in {"blob", "tree"}:
                raise ValueError(f"unsupported historical Git object: {kind} {path}")
            if oid in objects and objects[oid] != kind:
                raise ValueError("inconsistent object type")
            objects[oid] = kind
            if kind == "blob":
                count += 1
                if path.startswith("papers/tpc-"):
                    directories.add(path.split("/")[1])
        snapshots.append({"commit": historical, "root_tree": root_tree,
                          "selected_files": count, "tpc_directories": len(directories),
                          "referenced_by": sorted(candidates[historical])})
        print(f"snapshot {number}/{len(commits)} {historical[:12]} files={count}", flush=True)

    print(f"Packing {len(objects)} authentic Git objects", flush=True)
    packed = git(source, "pack-objects", "--max-pack-size=40m", "--threads=2",
                 "--window=10", str(packs / "pack"),
                 data=("\n".join(sorted(objects)) + "\n").encode()).decode().splitlines()
    pack_files = []
    for pack_id in packed:
        if not re.fullmatch(r"[0-9a-f]{40}", pack_id):
            raise ValueError("invalid generated pack id")
        for suffix in ("pack", "idx"):
            path = packs / f"pack-{pack_id}.{suffix}"
            blob = path.read_bytes()
            pack_files.append({"path": str(path.relative_to(target)), "bytes": len(blob),
                               "sha256": sha256(blob)})
    write_json(evidence / "MIGRATION_SOURCE.json", {
        "schema": "TPC_MIGRATION_SOURCE_V1", "source_commit": commit,
        "source_repository": "git@github.com:maris205/prime_dynamics_theory.git",
        "target_repository": destination,
        "scope": "all tracked papers/tpc-*, research/tpc-big-road, and listed shared TPC root documents",
        "source_worktree_newline_differences": newline_differences,
        "files": sorted(baseline, key=lambda row: row["path"]),
    })
    write_json(evidence / "LEGACY_GIT_OBJECTS.json", {
        "schema": "TPC_LEGACY_GIT_OBJECTS_V1", "migration_source_commit": commit,
        "selection": "existing commits referenced by TPC Python code, conversion records, plus the migration source",
        "scope": "original commit/root/intermediate trees, TPC trees and blobs, and required shared root context; no RH project payloads",
        "partial_graph": True,
        "warning": "This is a path-scoped provenance archive, not a complete historical Git repository. Parent commits and unrelated subtrees may be absent.",
        "snapshots": snapshots,
        "objects": [{"oid": oid, "type": objects[oid]} for oid in sorted(objects)],
        "object_counts": dict(Counter(objects.values())),
        "pack_files": pack_files,
    })
    print(json.dumps({"source_files": len(baseline), "snapshots": len(snapshots),
                      "objects": len(objects), "pack_bytes": sum(p["bytes"] for p in pack_files)}, indent=2))


if __name__ == "__main__":
    main()
