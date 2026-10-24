"""Package the reviewed research records without superseded search inputs."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'ant_global'
OUTPUT = ROOT / 'Langton_Ant_Research_2026-10-21.zip'

EXCLUDE_NAMES = {
    'jillhewar_pinned.md', 'ke_pinned.md',
    'conversion_row_screen.py', 'conversion_row_profiles.json',
    'conversion_row_screen.json', 'prepare_conversion_chronology.py',
    'conversion_chronology_inputs.txt', 'conversion_chronology_results.txt',
    'conversion_full_row_profiles.json', 'conversion_full_row_screen.json',
    'conversion_full_chronology_inputs.txt',
    'conversion_full_chronology_results.txt',
    'conversion_positive_control.json', 'conversion_positive_control.txt',
    'conversion_candidates.json', 'clock_conversion_screen.json',
    'check_cap_words', 'gate_scan', 'check_cap_shift',
    'check_cap_shift_stronger', 'check_cap_shift_prefix',
    'check_cap_shift_old_colors', 'check_adaptive_cut',
    'manifest_sha256.json',
    'marker_exit_exploratory.json', 'cap_shift_old_32_W4.json',
}

def selected(path):
    if not path.is_file() or '__pycache__' in path.parts:
        return False
    if path.name in EXCLUDE_NAMES:
        return False
    if path.name.startswith('cap_words_'):
        # These earlier binaries predate the retained refined source.
        return False
    if path.name.startswith('conversion_ports_replay_'):
        return False
    if path.name in {'conversion_chronology', 'check_cap_words_refined'}:
        return True
    return path.suffix in {'.md', '.txt', '.json', '.py', '.cpp'}

files = sorted(p for p in SRC.rglob('*') if selected(p))
manifest = {
    'status': 'Full highway conjecture remains unproved; reviewed local results and restricted exclusions only.',
    'created_date': '2026-10-21',
    'files': {
        str(p.relative_to(SRC)): {
            'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
        } for p in files
    },
}
manifest_path = SRC / 'manifest_sha256.json'
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
with zipfile.ZipFile(OUTPUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in files + [manifest_path]:
        z.write(p, str(p.relative_to(ROOT)))
    z.write(Path(__file__), 'make_ant_bundle.py')
with zipfile.ZipFile(OUTPUT) as z:
    assert z.testzip() is None
    for rel, rec in manifest['files'].items():
        assert hashlib.sha256(z.read('ant_global/' + rel)).hexdigest() == rec['sha256']
print(json.dumps({'path': str(OUTPUT), 'files': len(files)+2,
                  'bytes': OUTPUT.stat().st_size,
                  'sha256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}))
