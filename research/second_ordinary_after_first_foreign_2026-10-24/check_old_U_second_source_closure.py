"""Dependency-bound exhaustion of the OLD U outgoing-source branch only."""
from pathlib import Path
from collections import Counter
import hashlib, json

R = Path('/workspace/shared/langton')
H = Path(__file__).resolve().parent
base = json.loads((H / 'old_U_second_contact_LEFT_frontier.json').read_text())
G = json.loads((R / 'U_second_contact_creator_bud_guards_2026-10-24/creator_bud_guards.json').read_text())
Q = json.loads((R / 'U_second_V_original_q_frontier_2026-10-24/original_q_frontier.json').read_text())
T = json.loads((R / 'U_second_V_clock3_reflex_guard_2026-10-24/clock3_reflex_guard.json').read_text())
J = json.loads((R / 'U_second_V_first_helper_cohort_closure_2026-10-24/first_helper_cohort_closure.json').read_text())

def key(r):
    return (r['foreign'], tuple(r['foreign_pose']), r.get('first', r.get('FIRST_atom')),
            r.get('second', r.get('SECOND_atom')), tuple(r.get('second_pose', r.get('SECOND_pose'))),
            r.get('true_preforeign_age', r.get('true_preforeign_clock', r.get('true_preforeign_C_clock'))))

all60 = {key(r): r for r in base['exact60_necessary_only_remaining_states']}
assert len(all60) == 60
cuts = {}
for row in G['all60_typed_cases']:
    if row['classification'] != 'necessary_only_not_excluded_here':
        k = key(row)
        assert k in all60 and k not in cuts
        cuts[k] = row['classification']
assert len(cuts) == 48
assert {key(r) for r in G['remaining12_necessary_states']} == set(all60) - set(cuts)

for rows, label, expected_count in [
    (Q['one_coarse_state_excluded'], 'original_east_pair_FOREIGN_entry_core', 1),
    (T['cases'], 'clock3_reflex_Jordan_support', 2),
    (J['all9_exact_terminal_before_masks'], 'genuine_first_helper_cohort_clock4', 9)]:
    assert len(rows) == expected_count
    for row in rows:
        k = key(row)
        assert k in all60 and k not in cuts
        assert k[3] == 'V' and k[4] == (0, 4, 2)
        cuts[k] = label
assert len(cuts) == 60 and set(cuts) == set(all60)
assert Counter(cuts.values()) == {
    'genuine_s_BLACK_vs_combined_before_WHITE': 36,
    'source_deleted_g_no_rebirth_through_clock3': 12,
    'original_east_pair_FOREIGN_entry_core': 1,
    'clock3_reflex_Jordan_support': 2,
    'genuine_first_helper_cohort_clock4': 9}

paths = [H / 'small_second_ordinary_geometry_manifest.json',
         H / 'old_U_second_C_left_pair_guard_manifest.json',
         R / 'audits/check_old_U_second_C_left_guard_independent.json',
         H / 'old_U_second_contact_LEFT_frontier_manifest.json',
         R / 'audits/check_old_U_second_LEFT_frontier_independent.json',
         R / 'U_second_contact_creator_bud_guards_2026-10-24/manifest.json',
         R / 'audits/check_U_second_creator_bud_guards_independent.json',
         R / 'U_second_V_original_q_frontier_2026-10-24/manifest.json',
         R / 'U_second_V_clock3_reflex_guard_2026-10-24/manifest.json',
         R / 'U_second_V_first_helper_cohort_closure_2026-10-24/manifest.json',
         R / 'audits/check_second_V_first_helper_closure_independent.json',
         R / 'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_OLD_U_SECOND_SOURCE_GEOMETRIC_CLOSURE_PENDING_JOIN_REVIEW',
    scope='A finite-complete-board U-entry complete-eight prefix, its FIRST complete foreign F/Q/B, exactly ONE immediate ordinary RAW b1, and a SECOND ordinary RAW b2 plus actual final M11. If this second chord makes the chronological FIRST new contact, its outgoing old source is NOT a genuine preforeign U-base chord. No general second simplicity or later tail extension.',
    exact_old_U_SECOND_C_branch_already_closed_by='036ef9ca',
    exact_old_U_SECOND_DVU_geometric_frontier='474b5381:42 poses -> seven poses/60 typed states',
    all60_canonical_state_keys_with_disjoint_closure=[dict(key=k, exclusion=cuts[k]) for k in all60],
    exact_disjoint_remaining_frontier_cuts=dict(Counter(cuts.values())),
    no_remaining_old_U_source_states=True,
    geometric_lift='The signed one-return proxy is simple. An actual chronological first SECOND contact has outgoing old-piece ownership and the exact angle/parallelogram interface, including collinear onset and old vertices. SECOND C is separately excluded; all D/V/U necessary states exhaust into the60-key frontier and the disjoint signed cuts. Therefore its outgoing old source cannot be U.',
    explicit_open_branches=['old outgoing D','old outgoing C','old outgoing V'],
    no_general_SECOND_simplicity=True,
    no_THIRD_ordinary_or_SECOND_foreign_extension=True,
    no_postforeign_maturity_or_identity_reset=True,
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'old_U_second_source_closure.json').write_text(json.dumps(out, indent=2) + '\n')
print('Exact60-key disjoint closure36+12+1+2+9; SECOND C separately closed. Only OLD U outgoing-source branch excluded.')
