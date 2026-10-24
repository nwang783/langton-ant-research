"""Scoped source-level partition of the unchanged217 SECOND-contact angles."""
from pathlib import Path
from collections import Counter
import hashlib
import json

ROOT=Path('/workspace/shared/langton')
HERE=Path(__file__).resolve().parent
original=json.loads((HERE/'small_second_ordinary_geometry.json').read_text())['conditional217_old_source_angle_interfaces']
classified=[]
for angle in original:
    old,n=angle['old_source'],angle['actual_old_source_to_FOREIGN_C_age']
    if old=='U':
        status='signed_all_old_U_sources_excluded'
    elif old=='V':
        assert 0<=n<=4
        status='signed_all_old_V_sources_excluded'
    elif n==0:
        assert old=='D'
        status='signed_old_D_zero_age_excluded'
    elif n==1:
        status='signed_old_D_C_age1_excluded'
    elif n==2:
        status='signed_old_D_C_age2_excluded'
    else:
        assert old in 'DC' and n==3
        status='remaining_angular_interface_only'
    classified.append(dict(angle=angle,source_level_status=status))
assert Counter(r['source_level_status'] for r in classified)=={
    'signed_all_old_U_sources_excluded':60,
    'signed_all_old_V_sources_excluded':59,
    'signed_old_D_zero_age_excluded':10,
    'signed_old_D_C_age1_excluded':32,
    'signed_old_D_C_age2_excluded':32,
    'remaining_angular_interface_only':24}
remaining=[r['angle'] for r in classified if r['source_level_status']=='remaining_angular_interface_only']
assert Counter(r['old_source'] for r in remaining)=={'D':12,'C':12}
assert all(r['first_ordinary'] in 'DVU' and r['actual_old_source_to_FOREIGN_C_age']==3
           and r['total_ordinary_C_before_second']==3
           and r['second_heading_relative_old_source']==3 for r in remaining)
paths=[
    HERE/'small_second_ordinary_geometry_manifest.json',
    HERE/'old_U_second_source_closure_manifest.json',
    ROOT/'audits/check_old_U_second_source_closure_independent.json',
    HERE/'zero_preforeign_C_old_DV_slice_manifest.json',
    ROOT/'audits/check_zero_C_old_DV_second_contact_independent.json',
    ROOT/'second_old_D_age1_2026-10-24/manifest.json',
    ROOT/'audits/check_old_D_second_age1_independent.json',
    ROOT/'second_old_C_age1_2026-10-24/manifest.json',
    ROOT/'audits/check_old_C_second_age1_independent.json',
    ROOT/'old_V_second_contact_age1_2026-10-24/manifest.json',
    ROOT/'old_V_age1_scope_qualification_2026-10-24/manifest.json',
    ROOT/'audits/check_old_V_second_age1_independent.json',
    ROOT/'second_old_sources_age2_bud_2026-10-24/manifest.json',
    ROOT/'audits/check_old_DCV_age2_beta_independent.json',
    ROOT/'old_V_age2_common_port_guard_2026-10-24/manifest.json',
    ROOT/'audits/check_old_V_age2_common_guard_independent.json',
    ROOT/'old_V_second_age3_2026-10-24/manifest.json',
    ROOT/'audits/check_old_V_age3_C_port_independent.json',
    ROOT/'second_contact_signed_obligations_2026-10-24/manifest.json',
    ROOT/'second_contact_signed_obligations_2026-10-24/core_status_qualification_manifest.json',
    ROOT/'audits/check_second_contact_current_obligations_independent.json']
assert all(p.exists() for p in paths)
out=dict(
    status='AUTHOR_FROZEN_REMAINING24_SECOND_CONTACT_ANGLES_PENDING_JOIN_REVIEW',
    scope='Only chronological FIRST new SECOND ordinary RAW contact after a genuine U-entry complete-eight prefix and its FIRST foreign plus one immediate ordinary RAW, with one actual finalM11. This is an original217 source-angle partition, not a position/attainment catalogue or second simplicity.',
    all217_original_angle_rows_with_disjoint_source_status=classified,
    exact_remaining24_angle_interfaces=remaining,
    exact_disjoint_counts=dict(Counter(r['source_level_status'] for r in classified)),
    conclusion='Any unresolved stipulated first SECOND-contact has outgoing OLD D or C, true source-entry-to-foreign age3, b1 D/V/U, and second heading W relative to the old source. Twelve angles per source type remain; no old U/V source or other age remains.',
    historical92_join_preserved=True,
    source_scope_warning='Actual old C must belong to a genuine containing full-eight producer, with actual C2 shifts. Later internal U entries after a selected old D/V do not contain that older source and are not substituted for required prior U ancestry.',
    mandatory_CORE_qualification='Absence from external CURRENT does not imply physical original death: same R-born identity can be alive in CORE. The bc2 V4 current-fact exclusions are unchanged.',
    no_future_tail_or_foreign_extension=True,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(HERE/'remaining_24_angles.json').write_text(json.dumps(out,indent=2)+'\n')
print('Original217 angles partition into193 signed source exclusions and24 remaining: oldD12/oldC12, all true preforeign age3.')
