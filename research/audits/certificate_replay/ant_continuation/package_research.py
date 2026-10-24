"""Package the completed research, with archive-entry SHA-256 hashes.

Run after building the Word report. Intermediate binaries, Python caches,
and complete third-party source prose are excluded. Those source notes have
pinned links and hashes in SOURCES.json.
"""
from pathlib import Path
import hashlib
import json
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPORT = ROOT / 'Langton_Ant_Research_Update_2026-10-21.docx'
OUT = ROOT / 'Langton_Ant_Continuation_2026-10-21.zip'
MANIFEST = HERE / 'MANIFEST.json'
SUFFIXES = {'.py', '.cpp', '.md', '.json', '.txt', '.tsv', '.png', '.gz', '.npz'}


def main():
    assert REPORT.is_file(), 'Build the Word report first.'
    paths = sorted(p for p in HERE.rglob('*') if
                   p.is_file() and p.suffix in SUFFIXES and
                   '__pycache__' not in p.parts and p != MANIFEST and
                   not p.name.startswith('source_'))
    paths.append(REPORT)
    entries = {p.relative_to(ROOT).as_posix(): p for p in paths}
    required = [
        'ant_continuation/global_structure/conditioned_rank_cuts.json.gz',
        'ant_continuation/factor_language/conditioned_macro_contexts.json',
        'ant_continuation/wake_clock/fold_farkas_certificate.json',
        'ant_continuation/SOURCES.json',
    ]
    assert all(name in entries for name in required)
    manifest = {
        'description': 'SHA-256 of each retained archive entry, excluding this manifest',
        'research_status': 'General finite-seed highway conjecture remains unsolved',
        'files': {name: hashlib.sha256(p.read_bytes()).hexdigest()
                  for name, p in sorted(entries.items())},
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + '\n')
    entries[MANIFEST.relative_to(ROOT).as_posix()] = MANIFEST
    with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as archive:
        for name, p in sorted(entries.items()):
            archive.write(p, name)
    with zipfile.ZipFile(OUT) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(entries)
        for name, digest in manifest['files'].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
    print(json.dumps({'archive': str(OUT), 'entries': len(entries),
                      'bytes': OUT.stat().st_size,
                      'sha256': hashlib.sha256(OUT.read_bytes()).hexdigest(),
                      'all_manifest_hashes_verified': True}, indent=2))


if __name__ == '__main__':
    main()
