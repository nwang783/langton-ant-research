"""Scoped partition of the original217 angle interfaces, not a new catalogue."""
from pathlib import Path
from collections import Counter
import hashlib, json

R = Path('/workspace/shared/langton')
H = Path(__file__).resolve().parent
angles = json.loads((H / 'small_second_ordinary_geometry.json').read_text())['conditional217_old_source_angle_interfaces']
classified = []
for row in angles:
    source, n = row['old_source'], row['actual_old_source_to_FOREIGN_C_age']
    if source == 'U':
        label = 'signed_old_U_source_closed'
    elif n == 0:
        assert source in 'DV'
        label = 'signed_old_DV_zero_preforeign_C_slice'
    elif n == 1:
        label = 'signed_old_DCV_true_age1_slices'
    else:
        assert source in 'DCV'
        label = 'remaining_angular_interface_only'
    classified.append(dict(angle=row, source_level_status=label))
assert Counter(r['source_level_status'] for r in classified) == {
    'signed_old_U_source_closed': 60,
    'signed_old_DV_zero_preforeign_C_slice': 17,
    'signed_old_DCV_true_age1_slices': 48,
    'remaining_angular_interface_only': 92}
remaining = [r['angle'] for r in classified if r['source_level_status'] == 'remaining_angular_interface_only']
assert Counter(r['old_source'] for r in remaining) == {'D': 28, 'C': 28, 'V': 36}
assert Counter(r['first_ordinary'] for r in remaining) == {'D': 26, 'C': 14, 'V': 26, 'U': 26}
for row in remaining:
    n = row['actual_old_source_to_FOREIGN_C_age']
    assert n >= 2
    if row['old_source'] in 'DC': assert n <= 3
    else:
        assert n <= 4
        if n == 4:
            assert row['first_ordinary'] != 'C' and row['second_ordinary'] in 'DC'

paths = [H / 'small_second_ordinary_geometry_manifest.json',
         H / 'old_U_second_source_closure_manifest.json',
         R / 'audits/check_old_U_second_source_closure_independent.json',
         H / 'zero_preforeign_C_old_DV_slice_manifest.json',
         R / 'audits/check_zero_C_old_DV_second_contact_independent.json',
         R / 'second_old_D_age1_2026-10-24/manifest.json',
         R / 'audits/check_old_D_second_age1_independent.json',
         R / 'second_old_C_age1_2026-10-24/manifest.json',
         R / 'audits/check_old_C_second_age1_independent.json',
         R / 'old_V_second_contact_age1_2026-10-24/manifest.json',
         R / 'old_V_age1_scope_qualification_2026-10-24/manifest.json',
         R / 'audits/check_old_V_second_age1_independent.json']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_SECOND_CONTACT_92_ANGLE_FRONTIER_PENDING_JOIN_REVIEW',
    scope='Only chronological FIRST new SECOND ordinary RAW contact after a U-entry complete-eight prefix and its FIRST foreign plus one immediate ordinary RAW; actual finalM11. A partition of signed217 angular interfaces, not a position catalogue or second simplicity.',
    all217_original_angles_with_disjoint_source_status=classified,
    exact_remaining92_angular_interfaces=remaining,
    remaining_counts_by_old_source=dict(Counter(r['old_source'] for r in remaining)),
    exact_disjoint_partition=[60, 17, 48, 92],
    conclusion='Any remaining first SECOND-contact must have outgoing OLD D/C/V with true preforeign age>=2. OldD/C ages are2 or3; oldV ages2/3/4, with4 requiring no first-return C and SECOND D/C.',
    no_genuine_geometric_positions_or_ancestry_claimed_for_remaining_rows=True,
    no_bounded_epoch_length_or_finite_geometry_quotient=True,
    old_source_ancestry_warning='The selected D/C/V must lie inside the original prior-U factor. Later internal U entries do not contain earlier selected source chords; both D/V age1 scope qualifications are preserved.',
    no_THIRD_or_arbitrary_tail_extension=True,
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'remaining_92_angles.json').write_text(json.dumps(out, indent=2) + '\n')
print('217=60 oldU+17 oldDV zeroage+48 oldDCV age1+92 remaining angle interfaces;D28/C28/V36, all true preforeign ages>=2.')
