"""Read-only validation and environment for original Git provenance objects."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def strict_json(path: Path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    def constant(value):
        raise ValueError(f"non-finite JSON constant: {value}")
    return json.loads(path.read_text(), object_pairs_hook=pairs, parse_constant=constant)


def local_file(root: Path, relative: str) -> Path:
    if not isinstance(relative, str):
        raise ValueError("file path must be text")
    parts = PurePosixPath(relative)
    if parts.is_absolute() or ".." in parts.parts or str(parts) != relative:
        raise ValueError("unsafe or noncanonical relative path")
    path = root / relative
    if not path.is_file() or path.resolve() != path.absolute():
        raise ValueError(f"missing or symlinked evidence: {relative}")
    return path


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def environment(root: Path = ROOT):
    result = os.environ.copy()
    # Resolve legacy objects without importing their commits into this repo's
    # branch history or permanently changing Git configuration.
    result["GIT_ALTERNATE_OBJECT_DIRECTORIES"] = str(root / "provenance/git-objects")
    result["PYTHONDONTWRITEBYTECODE"] = "1"
    return result


def validate_archive(root: Path = ROOT, *, verify_packs: bool = False):
    archive = strict_json(local_file(root, "provenance/LEGACY_GIT_OBJECTS.json"))
    if archive.get("schema") != "TPC_LEGACY_GIT_OBJECTS_V1" or archive.get("partial_graph") is not True:
        raise ValueError("unexpected legacy provenance schema or graph claim")
    records = archive.get("pack_files")
    if not isinstance(records, list) or not records:
        raise ValueError("missing provenance packs")
    names = set()
    for row in records:
        name = row.get("path")
        if (not isinstance(name, str) or not re.fullmatch(
                r"provenance/git-objects/pack/pack-[0-9a-f]{40}\.(pack|idx)", name)):
            raise ValueError("invalid provenance pack path")
        if name in names:
            raise ValueError("duplicate provenance pack path")
        names.add(name)
        path = local_file(root, name)
        if type(row.get("bytes")) is not int or row["bytes"] <= 0 or path.stat().st_size != row["bytes"]:
            raise ValueError(f"provenance size mismatch: {name}")
        expected = row.get("sha256")
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise ValueError("invalid provenance digest")
        if file_sha256(path) != expected:
            raise ValueError(f"provenance digest mismatch: {name}")
    actual = {str(path.relative_to(root)) for path in (root / "provenance/git-objects").rglob("*")
              if path.is_file() or path.is_symlink()}
    if actual != names:
        raise ValueError("unlisted or missing provenance object files")
    for name in names:
        sibling = name[:-5] + ".idx" if name.endswith(".pack") else name[:-4] + ".pack"
        if sibling not in names:
            raise ValueError("unpaired provenance pack/index")
    objects = archive.get("objects")
    if not isinstance(objects, list) or not objects:
        raise ValueError("missing object inventory")
    expected_objects = {}
    for row in objects:
        oid, kind = row.get("oid"), row.get("type")
        if (not isinstance(oid, str) or not re.fullmatch(r"[0-9a-f]{40}", oid)
                or kind not in {"commit", "tree", "blob"} or oid in expected_objects):
            raise ValueError("invalid or duplicate object inventory row")
        expected_objects[oid] = kind
    if verify_packs:
        observed = {}
        for name in sorted(names):
            if not name.endswith(".idx"):
                continue
            result = subprocess.run(["git", "verify-pack", "-v", str(root / name)],
                                    cwd=root, text=True, capture_output=True, check=True)
            for line in result.stdout.splitlines():
                fields = line.split()
                if fields and re.fullmatch(r"[0-9a-f]{40}", fields[0]):
                    if len(fields) < 3 or fields[1] not in {"commit", "tree", "blob"}:
                        raise ValueError("unrecognized packed object type")
                    if fields[0] in observed:
                        raise ValueError("duplicate object across provenance packs")
                    observed[fields[0]] = fields[1]
        if observed != expected_objects:
            raise ValueError("packed object inventory mismatch")
    return archive
