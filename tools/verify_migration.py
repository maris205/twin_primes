#!/usr/bin/env python3
"""Read-only verification of the migration baseline, adaptations and Git packs."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from legacy_provenance import ROOT, strict_json, local_file, file_sha256, validate_archive

ADAPTED = {
    'README.md': 'New TPC-only landing page; old original retained in provenance.',
    'AGENTS.md': 'TPC-only repository protocol and new SSH remote.',
    'TPC_HANDOFF.md': 'Migration note and current TPC-only coverage; dated history retained.',
    'research/tpc-big-road/TPC_HISTORY_SUMMARY.md': 'Current coverage scoped to 420 TPC directories.',
    'research/tpc-big-road/PAPER_MATERIALS_INDEX.md': 'Remove unrelated RH rows and refresh current counts.',
    'research/tpc-big-road/PAPER_MATERIALS_LINKS.md': 'Remove unrelated RH links and refresh timestamp.',
    'research/tpc-big-road/PAPER_MATERIALS_REMAINING.md': 'Regenerate TPC-only maintenance backlog.',
    'research/tpc-big-road/TPC_CONVERSION_BATCH_2026-09-07.md': 'Refresh TPC inventory context and timestamp.',
    'research/tpc-big-road/refresh_source_markdown_inventory.py': 'Replace mixed-repository count with exact TPC directory coverage guard.',
    'research/tpc-big-road/test_source_markdown_inventory.py': 'TPC-only backlog fixtures and expectations.',
}

def baseline(root):
    source = strict_json(local_file(root, 'provenance/MIGRATION_SOURCE.json'))
    if source.get('schema') != 'TPC_MIGRATION_SOURCE_V1':
        raise ValueError('unexpected source schema')
    seen, changes = set(), []
    for row in source['files']:
        name = row['path']
        if name in seen:
            raise ValueError('duplicate source file')
        seen.add(name)
        path = local_file(root, name)
        digest = file_sha256(path)
        if digest != row['sha256']:
            if name not in ADAPTED:
                raise ValueError('unapproved source change: ' + name)
            changes.append({'path': name, 'source_sha256': row['sha256'],
                            'migrated_sha256': digest, 'reason': ADAPTED[name]})
        elif path.stat().st_size != row['bytes']:
            raise ValueError('source size mismatch: ' + name)
        if bool(path.stat().st_mode & 0o111) != (row['mode'] == '100755'):
            raise ValueError('source executable mode mismatch: ' + name)
    expected_papers = {p for p in seen if p.startswith('papers/')}
    actual_papers = {str(p.relative_to(root)) for p in (root / 'papers').rglob('*')
                     if p.is_file() or p.is_symlink()}
    if actual_papers != expected_papers:
        raise ValueError('extra or missing scientific paper files')
    if any(not p.name.startswith('tpc-') for p in (root / 'papers').iterdir()):
        raise ValueError('non-TPC main paper directory')
    return source, sorted(changes, key=lambda r: r['path'])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--adaptation-patch', action='store_true',
                        help='print a one-time adaptation receipt patch; does not write')
    args = parser.parse_args()
    source, changes = baseline(ROOT)
    receipt = ROOT / 'provenance/MIGRATION_ADAPTATIONS.json'
    if args.adaptation_patch:
        if receipt.exists():
            raise ValueError('adaptation receipt already exists')
        value = json.dumps({'source_commit': source['source_commit'], 'files': changes}, indent=2) + '\n'
        print('*** Begin Patch\n*** Add File: ' + str(receipt))
        print('\n'.join('+' + line for line in value.splitlines()))
        print('*** End Patch')
        return
    adaptation = strict_json(local_file(ROOT, 'provenance/MIGRATION_ADAPTATIONS.json'))
    if adaptation != {'source_commit': source['source_commit'], 'files': changes}:
        raise ValueError('adaptation receipt mismatch')
    early = strict_json(local_file(ROOT, 'provenance/EARLY_BRANCHES.json'))
    names = set()
    for branch in early['branches']:
        for row in branch['files']:
            if row['path'] in names or not row['path'].startswith('legacy/branches/'):
                raise ValueError('invalid early-branch inventory')
            names.add(row['path'])
            if file_sha256(local_file(ROOT, row['path'])) != row['sha256']:
                raise ValueError('early-branch digest mismatch')
    actual = {str(p.relative_to(ROOT)) for p in (ROOT / 'legacy').rglob('*')
              if p.is_file() or p.is_symlink()}
    if actual != names:
        raise ValueError('early-branch file inventory mismatch')
    archive = validate_archive(verify_packs=True)
    dirs = list((ROOT / 'papers').iterdir())
    rows = re.findall(r'^\| TPC \| `([^`]+)` \|',
                      (ROOT / 'research/tpc-big-road/PAPER_MATERIALS_INDEX.md').read_text(), re.M)
    if len(rows) != len(dirs) or set(rows) != {p.name for p in dirs}:
        raise ValueError('TPC index directory coverage mismatch')
    print(json.dumps({'status': 'PASS', 'source_files': len(source['files']),
                      'unchanged_files': len(source['files']) - len(changes),
                      'explicit_adaptations': len(changes), 'paper_directories': len(dirs),
                      'early_branch_files': len(names), 'legacy_snapshots': len(archive['snapshots']),
                      'authentic_git_objects': len(archive['objects']),
                      'claim': 'archive fidelity only, not mathematical verification'}, indent=2))

if __name__ == '__main__':
    main()
