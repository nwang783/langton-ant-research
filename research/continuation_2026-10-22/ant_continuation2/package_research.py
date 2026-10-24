"""Package the complete continuation and verify every archived entry hash."""
from pathlib import Path
import hashlib
import json
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPORT = ROOT / 'Langton_Ant_Research_Update_2026-10-22.docx'
OUT = ROOT / 'Langton_Ant_Continuation_2026-10-22.zip'
MANIFEST = HERE / 'MANIFEST.json'
SUFFIXES = {'.py', '.cpp', '.md', '.json', '.txt', '.tsv', '.png', '.gz', '.npz'}
OMIT = {'maxplus_port_head_sft_checkpoint.json'}


def digest_file(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            h.update(part)
    return h.hexdigest()


def main():
    assert REPORT.is_file()
    assert zipfile.is_zipfile(REPORT), 'The Word report must be a complete DOCX archive.'
    with zipfile.ZipFile(REPORT) as report_archive:
        assert report_archive.testzip() is None
        assert 'word/document.xml' in report_archive.namelist()
    entries = {}
    for directory in (ROOT / 'ant_continuation', HERE):
        for p in directory.rglob('*'):
            relative = p.relative_to(ROOT)
            if not p.is_file() or p.suffix not in SUFFIXES:
                continue
            if any(part.startswith('.') for part in relative.parts):
                continue
            if '__pycache__' in p.parts or p.name.startswith('source_'):
                continue
            if p.name in OMIT or p.name == 'MANIFEST.json':
                continue
            entries[relative.as_posix()] = p
    entries[REPORT.name] = REPORT
    required = [
        'ant_continuation/ant_exact.py',
        'ant_continuation/one_bit_certificate_restored.json',
        'ant_continuation/wake_clock/certify_four_scatterer_prefix.py',
        'ant_continuation2/chronology/eventual_mass_five.md',
        'ant_continuation2/planar_structure/exceptional_rectangle_template.json',
        'ant_continuation2/planar_structure/exceptional_rectangle_affine_certificate.json',
        'ant_continuation2/planar_structure/exceptional_affine_fields.json.gz',
        'ant_continuation2/independent_rectangle_audit.json',
        'ant_continuation2/SOURCES.json',
    ]
    assert all(name in entries for name in required)
    manifest = {
        'description': 'SHA-256 of every archive entry except this manifest',
        'research_status': 'Full finite-seed highway conjecture remains unresolved by this work',
        'main_partial_theorem': 'Every finite-seed orbit eventually has black mass at least five',
        'verification': 'Analytic reduction plus exact all-parameter Python certificates; not a Lean formalization',
        'files': {name: digest_file(p) for name, p in sorted(entries.items())},
        'omitted_duplicate_checkpoint': {
            'filename': 'maxplus_port_head_sft_checkpoint.json',
            'reason': 'Counterfield prefix retained in final refinement; unique weights/logs retained in metadata JSON',
        },
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
        for name, expected in manifest['files'].items():
            h = hashlib.sha256()
            with archive.open(name) as stream:
                for part in iter(lambda: stream.read(1 << 20), b''):
                    h.update(part)
            assert h.hexdigest() == expected, name
    print(json.dumps({'archive': str(OUT), 'entries': len(entries),
                      'bytes': OUT.stat().st_size, 'sha256': digest_file(OUT),
                      'all_manifest_hashes_verified': True}, indent=2))


if __name__ == '__main__':
    main()
