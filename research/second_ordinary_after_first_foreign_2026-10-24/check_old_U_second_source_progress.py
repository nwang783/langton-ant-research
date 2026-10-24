"""Exact key-level integration of signed60-state frontier and48 cohort cuts."""
from pathlib import Path
from collections import Counter
import json, hashlib

R = Path('/workspace/shared/langton')
H = Path(__file__).resolve().parent
F = H / 'old_U_second_contact_LEFT_frontier.json'
G = R / 'U_second_contact_creator_bud_guards_2026-10-24/creator_bud_guards.json'
source = json.loads(F.read_text())['exact60_necessary_only_remaining_states']
guards = json.loads(G.read_text())

def key(r):
    return (r['foreign'], tuple(r['foreign_pose']), r['first'], r['second'],
            tuple(r['second_pose']), r.get('true_preforeign_age', r.get('true_preforeign_clock')))

assert len(source) == len({key(r) for r in source}) == 60
assert len(guards['all60_typed_cases']) == 60
assert {key(r) for r in source} == {key(r) for r in guards['all60_typed_cases']}
classification = {key(r): r['classification'] for r in guards['all60_typed_cases']}
assert Counter(classification.values()) == {
    'genuine_s_BLACK_vs_combined_before_WHITE': 36,
    'source_deleted_g_no_rebirth_through_clock3': 12,
    'necessary_only_not_excluded_here': 12}
remaining = [r for r in source if classification[key(r)] == 'necessary_only_not_excluded_here']
assert {key(r) for r in remaining} == {key(r) for r in guards['remaining12_necessary_states']}
assert len(remaining) == 12
assert all(r['second'] == 'V' and tuple(r['second_pose']) == (0, 4, 2) for r in remaining)
assert Counter(r['true_preforeign_age'] for r in remaining) == {3: 3, 4: 9}
assert Counter(r['first'] for r in remaining) == dict.fromkeys('DCVU', 3)
paths = [H / 'old_U_second_contact_LEFT_frontier_manifest.json',
         R / 'audits/check_old_U_second_LEFT_frontier_independent.json',
         R / 'U_second_contact_creator_bud_guards_2026-10-24/manifest.json',
         R / 'audits/check_U_second_creator_bud_guards_independent.json']
out = dict(status='AUTHOR_FROZEN_SCOPED_OLD_U_SECOND_SOURCE_PROGRESS_PENDING_JOIN_REVIEW',
    scope='Only old outgoing U-base source of chronological FIRST new SECOND-ordinary contact. Exact signed60 typed states minus signed48 source-cohort cuts. No other old source or second simplicity conclusion.',
    original60_frontier_unmodified=True,
    exact_disjoint_source_guard_counts=dict(Counter(classification.values())),
    all60_canonical_keys_with_source_guard=[dict(key=key(r), classification=classification[key(r)]) for r in source],
    remaining12_necessary_only_states=remaining,
    conclusion='Only SECOND V(0,4,S) remains for an old-U contact: three b1=C/trueage3 cases and nine b1=D/V/U/trueage4 cases. These are not actual-history attainments.',
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'old_U_second_source_progress.json').write_text(json.dumps(out, indent=2) + '\n')
print('Bijective60-key join;36 bud-WHITE+12 deleted-g cuts leave exactly12 necessary SECOND V(0,4,S) states.')
