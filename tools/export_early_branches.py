#!/usr/bin/env python3
"""One-time TPC-only early-branch export; source repository is read-only."""
import argparse
from collections import Counter
import io
import json
from pathlib import Path
import tarfile
from export_legacy_provenance import git, tree, selected, sha256

EARLY = ('two-scale-prime-sieve-correlations', 'rough-pair-parity-transitions',
         'short-box-centered-sieve-kernels')
BRANCHES = ('twin-prime-correlations', 'rough-pair-parity',
            'short-box-sieve-kernels', 'structured-sieve-low-conductor')

def early(path):
    return any(path == 'papers/' + p or path.startswith('papers/' + p + '/') for p in EARLY)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    receipt = root / 'provenance/EARLY_BRANCHES.json'
    if receipt.exists() or (root / 'legacy').exists():
        raise ValueError('refusing to overwrite early-branch export')
    metadata = root / 'provenance/LEGACY_GIT_OBJECTS.json'
    archive = json.loads(metadata.read_text())
    objects = {r['oid']: r['type'] for r in archive['objects']}
    previous = set(objects)
    branches = []
    commits = {r['commit'] for r in archive['snapshots']}
    for branch in BRANCHES:
        commit = git(args.source, 'rev-parse', 'refs/remotes/origin/' + branch).decode().strip()
        commits.add(commit)
        paths = [p for _, k, _, p in tree(args.source, commit)
                 if k == 'blob' and (early(p) or p.startswith('papers/tpc-'))]
        destination = root / 'legacy/branches' / branch
        destination.mkdir(parents=True)
        payload = git(args.source, 'archive', commit, '--', *paths)
        with tarfile.open(fileobj=io.BytesIO(payload)) as tar:
            tar.extractall(destination, filter='data')
        files = [{'path': str((destination / p).relative_to(root)),
                  'source_path': p, 'sha256': sha256((destination / p).read_bytes())}
                 for p in paths]
        branches.append({'branch': branch, 'commit': commit, 'files': files})
    snapshots = {r['commit']: r for r in archive['snapshots']}
    for commit in sorted(commits):
        rt = git(args.source, 'rev-parse', commit + '^{tree}').decode().strip()
        objects[commit], objects[rt] = 'commit', 'tree'
        count, directories = 0, set()
        for _, kind, oid, path in tree(args.source, commit):
            if path in {'papers', 'research'} or selected(path) or early(path):
                objects[oid] = kind
                if kind == 'blob':
                    count += 1
                    if path.startswith('papers/'):
                        directories.add(path.split('/')[1])
        row = snapshots.setdefault(commit, {'commit': commit, 'root_tree': rt,
                                            'referenced_by': ['early TPC branch']})
        row.update(selected_files=count, tpc_directories=len(directories))
    new = sorted(set(objects) - previous)
    if new:
        packed = git(args.source, 'pack-objects', '--max-pack-size=40m', '--threads=2',
                     str(root / 'provenance/git-objects/pack/pack'),
                     data=('\n'.join(new) + '\n').encode()).decode().splitlines()
        for pack in packed:
            for ext in ('pack', 'idx'):
                p = root / f'provenance/git-objects/pack/pack-{pack}.{ext}'
                archive['pack_files'].append({'path': str(p.relative_to(root)),
                                             'bytes': p.stat().st_size, 'sha256': sha256(p.read_bytes())})
    archive['snapshots'] = [snapshots[c] for c in sorted(snapshots)]
    archive['objects'] = [{'oid': oid, 'type': objects[oid]} for oid in sorted(objects)]
    archive['object_counts'] = dict(Counter(objects.values()))
    archive['selection'] += '; four early TPC branch tips and original pre-rename TPC paths'
    # Generated export metadata, not a hand-edited scientific artifact.
    metadata.write_text(json.dumps(archive, indent=2) + '\n')
    receipt.write_text(json.dumps({'branches': branches}, indent=2) + '\n')
    print(json.dumps({'branches': len(branches), 'files': sum(len(b['files']) for b in branches),
                      'supplemental_objects': len(new)}))

if __name__ == '__main__':
    main()
