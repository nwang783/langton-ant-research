"""Exact source-exhaustion join for ONE foreign after a U-entry eight factor.

This is a finite dependency/case join, not a new ant-prefix enumeration.  The
source exclusions are separately audited theorems with their own actual
producer clocks.  A new returned-eight or second-foreign interval is not used.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json

ROOT = Path('/workspace/shared/langton')
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((HERE / name).read_text())


dependency_manifests = {
    'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json':
        '127a00884b4a06af35a807ab76f6f6499b9427d56350a931c03cc0e8de65524d',
    'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json':
        '92909b5493022d5d48b5da8a11581e1c4409f66380fecc4c0a0db3746d9e97b9',
    'seven_word_spatial_return_2026-10-23/foreign_first_contact_manifest.json':
        '8c922bd6545d543d6939aa200fb6ee70d9a4424079131925502f8738fbcaa35a',
    'seven_word_spatial_return_2026-10-23/foreign_tail_first_contact_manifest.json':
        '364870f37fdab340789d094421ad986b55848bcf137f73ec957f9839cb9be010',
    'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json':
        '735023bebfa154bd936e9546023367b541006ea1d9f57bb2eb7240bf040017ea',
    'seven_word_spatial_return_2026-10-23/first_foreign_U_source_exclusion_manifest.json':
        '18c60b120c83069c2f39901c0c5289ad89d0600d919e0d3e223a26d88df7ca4d',
    'seven_word_spatial_return_2026-10-23/first_foreign_C_source_exclusion_manifest.json':
        '37e71e6bd55f1bd9ea748e2fb9221bf474309e494ba788f35e56419ca2bdd384',
    'word_stabilization/DV_foreign_prefix_guard_frozen_20261023_2220/manifest.json':
        'fbd81fc5e622c6caa5c23c4f3e8493de4e3461cc3444ba006e8d681c3adb8ebf',
    'word_stabilization/DV_foreign_tail_guard_frozen_20261023_2237/manifest.json':
        '35f51ab959f5356dd1007e08c26ebc1e957006899c8194e95c50e3d089865976',
}
for name, expected in dependency_manifests.items():
    path = ROOT / name
    assert sha(path) == expected, name
    manifest = json.loads(path.read_text())
    # Recheck every directly bound artifact, not only the manifest's existence.
    files = manifest.get('files', {})
    artifact_rows = (files.items() if isinstance(files, dict) else
                     ((row.get('frozen', row.get('path')), row['sha256'])
                      for row in files))
    for filename, artifact_sha in artifact_rows:
        assert sha(path.parent / filename) == artifact_sha, (name, filename)

audit_bindings = {
    'check_foreign_first_contact_independent.json':
        dependency_manifests['seven_word_spatial_return_2026-10-23/foreign_first_contact_manifest.json'],
    'check_foreign_tail_first_contact_independent.json':
        dependency_manifests['seven_word_spatial_return_2026-10-23/foreign_tail_first_contact_manifest.json'],
    'check_complete8_foreign_adjacency_independent.json':
        dependency_manifests['seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json'],
    'check_first_foreign_U_source_assembly_independent.json':
        dependency_manifests['seven_word_spatial_return_2026-10-23/first_foreign_U_source_exclusion_manifest.json'],
    'check_first_foreign_C_source_independent.json':
        dependency_manifests['seven_word_spatial_return_2026-10-23/first_foreign_C_source_exclusion_manifest.json'],
    'check_DV_foreign_prefix_guard_independent.json':
        dependency_manifests['word_stabilization/DV_foreign_prefix_guard_frozen_20261023_2220/manifest.json'],
    'check_DV_foreign_tail_guard_independent.json':
        dependency_manifests['word_stabilization/DV_foreign_tail_guard_frozen_20261023_2237/manifest.json'],
}
audit_report_hashes = {}
for name, expected_manifest in audit_bindings.items():
    path = ROOT / 'audits' / name
    report = json.loads(path.read_text())
    assert report['status'].startswith('PASS'), name
    assert report['manifest_sha256'] == expected_manifest, name
    audit_report_hashes[str(path.relative_to(ROOT))] = sha(path)


prefix = read('foreign_first_contact_interface.json')
tails = read('foreign_tail_first_contact.json')
cases = []
for geometry_id, row in enumerate(prefix['rows']):
    for foreign in 'FQB':
        for age, previous_C in zip(row['permitted_C_ages'], row['preceding_C_bits']):
            cases.append(dict(
                piece='F_prefix', foreign=foreign,
                source=row['source_atom'], geometry_id=geometry_id,
                foreign_pose=row['foreign_pose'], C_age=age,
                previous_C=previous_C,
                contact=dict(kind='point', s=row['source_parameter'],
                             t=row['foreign_parameter'])))
for foreign, rows in tails['rows'].items():
    for geometry_id, row in enumerate(rows):
        for age, previous_C in zip(row['permitted_C_ages'], row['preceding_C_bits']):
            cases.append(dict(
                piece=foreign + '_tail', foreign=foreign,
                source=row['source_atom'], geometry_id=geometry_id,
                foreign_pose=row['foreign_pose'], C_age=age,
                previous_C=previous_C, contact=row['contact'],
                legal_F_entry_adjacent_source_endpoint=
                    row['legal_F_entry_adjacent_source_endpoint']))

assert len(cases) == 375
assert Counter(row['source'] for row in cases) == {
    'D': 56, 'C': 53, 'V': 122, 'U': 144}
assert Counter(row['previous_C'] for row in cases) == {0: 186, 1: 189}

for row in cases:
    if row['previous_C']:
        reason = 'complete8_foreign_adjacency'
    elif row['source'] == 'U':
        reason = 'first_foreign_U_source_exclusion'
    elif row['source'] == 'C':
        reason = 'first_foreign_C_source_exclusion'
    elif row['piece'] == 'F_prefix':
        reason = 'DV_foreign_prefix_guard'
    else:
        assert row['source'] in ('D', 'V')
        reason = 'DV_foreign_tail_guard'
    row['exclusion_dependency'] = reason

reason_counts = Counter(row['exclusion_dependency'] for row in cases)
assert reason_counts == {
    'complete8_foreign_adjacency': 189,
    'first_foreign_U_source_exclusion': 72,
    'first_foreign_C_source_exclusion': 25,
    'DV_foreign_prefix_guard': 60,
    'DV_foreign_tail_guard': 29,
}

# A foreign has one segment (F), or two noncollinear consecutive segments.
# Their exact determinants are invariant under the true integer rotations.
foreign_pieces = {
    'F': [((-1, -1), (-7, -3))],
    'Q': [((-1, -1), (-7, -3)), ((-7, -3), (-7, -7))],
    'B': [((-1, -1), (-7, -3)), ((-7, -3), (-5, -9))],
}
determinants = {}
for foreign, pieces in foreign_pieces.items():
    assert all(a != b for a, b in pieces)
    if len(pieces) == 2:
        a, b = pieces[0]
        c, d = pieces[1]
        assert b == c
        u = (b[0] - a[0], b[1] - a[1])
        v = (d[0] - c[0], d[1] - c[1])
        determinant = u[0] * v[1] - u[1] * v[0]
        assert determinant == {'Q': 24, 'B': 40}[foreign]
        determinants[foreign] = determinant
        # Noncollinear segments sharing one endpoint have no second contact.

# Check the first old/new join is not a retraced collinear old terminal base.
# Signed adjacency leaves only plain V or U immediately before the foreign.
initial_join_determinants = {}
for source, vector in {'V': (2, 6), 'U': (0, 8)}.items():
    initial_join_determinants[source] = (
        vector[0] * -2 - vector[1] * -6)
assert initial_join_determinants == {'V': 32, 'U': 48}

out = dict(
    status='AUTHOR_FROZEN_EXACT_JOIN_PENDING_INDEPENDENT_REVIEW',
    scope='One first complete foreign after an actual finite U-entry complete-eight factor. No returned-eight, second-foreign or global language-coverage extension.',
    total_clock_labels=len(cases),
    source_counts=dict(Counter(row['source'] for row in cases)),
    preceding_C_counts=dict(Counter(row['previous_C'] for row in cases)),
    disjoint_exclusion_counts=dict(reason_counts),
    cases=cases,
    foreign_pieces=foreign_pieces,
    foreign_internal_determinants=determinants,
    initial_join_determinants=initial_join_determinants,
    dependency_manifests=dependency_manifests,
    independent_dependency_reports=audit_report_hashes,
    analytic_interface=[
        'The actual old atomic path is injective by the U-entry theorem.',
        'Each appended foreign repaired proxy is internally injective.',
        'The only permitted contact at foreign parameter zero is its actual common endpoint with the old terminal atom; this join is noncollinear.',
        'Any other contact has an earliest positive new parameter. An old vertex is assigned to its outgoing old atom. The old terminal endpoint cannot be a later foreign contact, because it is the foreign initial point and the foreign proxy is internally injective.',
        'A contact at the shared F-prefix/tail endpoint is assigned to the F prefix. A first contact strictly later on a tail has no earlier F-prefix contact except genuine initial adjacency.',
        'The signed catalogues exhaust this chronological first contact. The five disjoint dependency classes exhaust all 375 clock labels.',
        'Consequently the old path plus this one complete first foreign is injective. No later return interval is assumed simple.',
    ],
)
(HERE / 'first_foreign_all_source_join.json').write_text(
    json.dumps(out, indent=2) + '\n')
print('375 clock labels:', dict(reason_counts))
print('Foreign internal determinants:', determinants)
print('Every source manifest, directly frozen artifact, and independent report is bound.')
