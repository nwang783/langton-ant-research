"""Exact first-C-of-VCC/UCC returned-C residue family, not a depth search.

The second source C is mandatory and immediate. Remaining S/E count equations
have a fixed downward budget and give every possible complete-eight order.
"""
from pathlib import Path
import json
import hashlib
import importlib.util

ROOT = Path('/workspace/shared/langton')
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lit', ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)
G = json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
words = {a: r['word'] for a, r in zip('DCVUFQB', json.loads((ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text())['macro_words'])}


def orders(d, v, u):
    if d+v+u == 0:
        return [()]
    return [(a,)+suffix for a, n in (('D', d), ('V', v), ('U', u)) if n
            for suffix in orders(d-(a=='D'), v-(a=='V'), u-(a=='U'))]


families = []
for foreign, (X, Y) in {'F': (2, -5), 'Q': (4, -5), 'B': (5, -4)}.items():
    budget = -Y
    count_solutions = []
    controls = []
    # S begins(-1,1). Its final C contributes(0,-1), so the exact downward
    # budget e+3f+4g+k+l=-Y bounds ALL e,f,g,k,l; x then fixes m uniquely.
    for e in range(budget+1):
        for f in range((budget-e)//3+1):
            for g in range((budget-e-3*f)//4+1):
                if e+f+g == 0:
                    continue  # The third C must attach to an actual S base.
                remaining = budget-e-3*f-4*g
                for l in range(remaining+1):
                    k = remaining-l
                    four_m = X+1+e+f-k-3*l
                    if four_m < 0 or four_m % 4:
                        continue
                    m = four_m//4
                    count_solutions.append((e, f, g, k, l, m))
                    for S_word in orders(e, f, g):
                        for E_word in orders(k, l, m):
                            if not E_word or E_word[-1] not in (('V', 'U') if foreign != 'B' else ('U',)):
                                continue
                            for source_id in (6, 9):
                                literal_word = (G[source_id]['word']
                                    + ''.join(words[a] for a in S_word)+words['C']
                                    + ''.join(words[a] for a in E_word)
                                    + words[foreign]+words['C']+lit.M)
                                result = lit.trace(literal_word)
                                assert not result['feasible']
                                controls.append(dict(
                                    old_full_source=G[source_id]['name'],
                                    old_C_index=1, S_sequence=S_word,
                                    actual_S_turning_packet=S_word[-1]+'C',
                                    E_sequence=E_word, foreign=foreign,
                                    returned_word='raw_C', conflict=result))
    assert len(count_solutions) == {'F': 10, 'Q': 10, 'B': 6}[foreign]
    assert len(controls) == {'F': 24, 'Q': 40, 'B': 16}[foreign]
    families.append(dict(foreign=foreign, foreign_pose_in_old_C_chart=(X,Y,1),
                         fixed_postsource_S_pose=(-1,1,2),
                         downward_budget=budget, count_solutions=count_solutions,
                         all_fixed_word_conflicts=controls))
assert sum(len(row['all_fixed_word_conflicts']) for row in families) == 80

dependencies = [HERE/'returned_C_source_reduction_manifest.json',
                HERE/'first_returned_atom_contact_manifest.json',
                HERE/'complete8_foreign_adjacency_manifest.json',
                ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json',
                ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json',
                ROOT/'word_stabilization/check_foreign_return_interfaces.py']
out = dict(
    status='AUTHOR_FROZEN_DOUBLE_TAIL_OLD_C_ROLE_EXCLUSION_PENDING_REVIEW',
    scope='Only first C inside actual VCC or UCC, among the three necessary age-three raw-C returned-contact interfaces. Its second source C is mandatory immediately; all remaining S/E endpoint orders fail literally. No exclusion for the other five containing old-C roles, nonempty W stages there, later returned atoms or a second foreign.',
    actual_parser_reason_for_no_W='The selected old source is C1 of VCC/UCC; its C2 follows immediately inside that SAME fullpacket. No zero-C W base can be inserted there.',
    source_full_words={G[i]['name']:G[i]['word'] for i in (6,9)},
    families=families,
    all_word_conflict_count=80,
    dependencies={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()
                  for path in dependencies})
(HERE/'returned_C_double_tail_source.json').write_text(json.dumps(out,indent=2)+'\n')
print('Two actual containing source roles;26 exact count tuples;80 whole-word conflicts.')
