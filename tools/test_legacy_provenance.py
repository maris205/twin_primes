"""Regression tests for migration metadata trust boundaries."""
import json
from pathlib import Path
import tempfile
import unittest
from legacy_provenance import local_file, strict_json, validate_archive, ROOT

class ProvenanceTests(unittest.TestCase):
    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'input.json'
            path.write_text('{"x":1,"x":2}')
            with self.assertRaises(ValueError):
                strict_json(path)

    def test_nonfinite_json_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'input.json'
            path.write_text('{"x":NaN}')
            with self.assertRaises(ValueError):
                strict_json(path)

    def test_path_traversal_rejected(self):
        for name in ('../README.md', '/etc/passwd', './README.md', 'tools//file'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                local_file(ROOT, name)

    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'target').write_text('value')
            (root / 'link').symlink_to(root / 'target')
            with self.assertRaises(ValueError):
                local_file(root, 'link')

    def test_pack_boolean_size_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            name = 'provenance/git-objects/pack/pack-' + '0' * 40 + '.pack'
            path = root / name
            path.parent.mkdir(parents=True)
            path.write_bytes(b'x')
            data = {'schema': 'TPC_LEGACY_GIT_OBJECTS_V1', 'partial_graph': True,
                    'pack_files': [{'path': name, 'bytes': True, 'sha256': '0' * 64}]}
            (root / 'provenance/LEGACY_GIT_OBJECTS.json').write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, 'size mismatch'):
                validate_archive(root)

if __name__ == '__main__':
    unittest.main()
