"""Actual old C-source returned-contact reduction, protection only PREforeign.

Finite signed case join, exact transport-count solutions and literal fixed-word
contradictions. No postforeign maturation, trajectory tree or output relabelling.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import importlib.util
import hashlib
import json

ROOT = Path('/workspace/shared/langton')
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'literal', ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)
G = json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
words = {a: r['word'] for a, r in zip('DCVUFQB', json.loads((ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text())['macro_words'])}
catalogue = json.loads((HERE/'first_returned_atom_contact.json').read_text())
C_roles = json.loads((HERE/'first_foreign_C_source_exclusion.json').read_text())['C_full_producer_roles']
keep = (0, 1, 4, 5, 6, 7, 8, 9)


def add(p, q):
    return p[0]+q[0], p[1]+q[1]


def sub(p, q):
    return p[0]-q[0], p[1]-q[1]


def det(p, q):
    return p[0]*q[1]-p[1]*q[0]


def head_context(row, word):
    p = row['foreign_pose']
    return lit.trace(word), p


def local(q, pose):
    return lit.rot(sub(q, pose[:2]), -pose[2])


def orders(d, v, u):
    if d+v+u == 0:
        return [()]
    result = []
    for a, n in (('D', d), ('V', v), ('U', u)):
        if n:
            for suffix in orders(d-(a=='D'), v-(a=='V'), u-(a=='U')):
                result.append((a,)+suffix)
    return result


def counts_E(delta):
    # E displacement (d+3v+4u,-d-v). Its y equation bounds d,v exactly.
    x, y = delta
    total = -y
    if total < 0:
        return []
    result = []
    for v in range(total+1):
        d = total-v
        rest = x-d-3*v
        if rest >= 0 and rest % 4 == 0:
            result.append((d, v, rest//4))
    return result


def counts_W(delta):
    # W displacement (-d-3v-4u,d+v), the same exact bounded count equation.
    return counts_E((-delta[0], -delta[1]))


def allowed_last(foreign):
    return ('V', 'U') if foreign != 'B' else ('U',)


def closed_contact(a, b, c, d):
    u, v, z = sub(b, a), sub(d, c), sub(c, a)
    denominator = det(u, v)
    if denominator:
        s, t = Q(det(z, v), denominator), Q(det(z, u), denominator)
        return dict(s=str(s), t=str(t)) if 0 <= s <= 1 and 0 <= t <= 1 else None
    if det(z, u):
        return None
    k = 0 if u[0] else 1
    endpoints = (Q(c[k]-a[k], u[k]), Q(d[k]-a[k], u[k]))
    lo, hi = max(Q(0), min(endpoints)), min(Q(1), max(endpoints))
    return dict(s_interval=[str(lo), str(hi)]) if lo <= hi else None


source_cases = [(i, r) for i, r in enumerate(catalogue['old_source_contact_cases'])
                if r['source_atom'] == 'C']
assert len(source_cases) == 51
classified = []
protected_rows = []
one_C_rows = []
repair_rows = []
residues = []

# q is source-C entry core, physically deleted and not exported by any actual
# containing full producer, including its remaining real C tail.
q = (-1, -1)
white_source_roles = []
for role in C_roles:
    source_id = next(i for i in keep if G[i]['name'] == role['full_packet'])
    cp = role['C_pose_in_full_source']
    full_q = add(cp[:2], lit.rot(q, cp[2]))
    raw = lit.trace(G[source_id]['word'])
    assert raw['feasible'] and raw['last'][full_q][0] == 'L'
    endpoint = G[source_id]['endpoint']
    exit_core = {add(endpoint[:2], lit.rot(k, endpoint[2])) for k in lit.K}
    assert list(full_q) not in G[source_id]['outputs'] and full_q not in exit_core
    white_source_roles.append(dict(
        full_packet=role['full_packet'], C_index=role['C_index'],
        full_source_q=full_q, final_RAW_read=raw['last'][full_q],
        absent_from_full_output=True, absent_from_exit_core=True))
assert len(white_source_roles) == 7

for case_id, row in source_cases:
    n = row['source_to_foreign_C_age']
    context = lit.trace(words[row['foreign']]+words[row['returned_atom']]+lit.M)
    assert context['feasible']
    protected = []
    if n <= 2:
        protected.extend([((2, 0), 'C_common', 3), ((1, -1), 'incoming_exit_bud', 3)])
    if n <= 3:
        protected.append(((1, 2), 'C_exit_bud', 4))
    conflicts = []
    for cell, name, first_old_age in protected:
        z = local(cell, row['foreign_pose'])
        first = context['first'].get(z)
        if z in lit.K or first and first[0] == 'R':
            conflicts.append(dict(
                identity=name, cell=cell, earliest_old_consumer_age=first_old_age,
                foreign_local=z, first_combined_read=first,
                reason='current_residual_in_foreign_core' if z in lit.K else 'combined_before_white'))
    protected_rows.append(dict(case=case_id, protected_only_at_foreign_entry=True,
                               conflicts=conflicts))
    if conflicts:
        classified.append(dict(case=case_id, reason='PREforeign_protected_combined_context'))
        continue
    if n == 1:
        delta = sub(row['foreign_pose'][:2], (0, 1))
        solutions = counts_W(delta)
        controls = []
        for counts in solutions:
            for sequence in orders(*counts):
                if not sequence or sequence[-1] not in allowed_last(row['foreign']):
                    continue
                word = words['C']+''.join(words[a] for a in sequence)+words[row['foreign']]+words[row['returned_atom']]+lit.M
                trace = lit.trace(word)
                assert not trace['feasible']
                controls.append(dict(zero_W_sequence=sequence, conflict=trace))
        one_C_rows.append(dict(case=case_id, exact_W_displacement=delta,
                               count_solutions=solutions, forced_RAW_conflicts=controls,
                               no_allowed_last_packet=not controls))
        classified.append(dict(case=case_id, reason='age1_exact_W_counts_and_RAW'))
        continue
    assert n == 3
    if row['returned_atom'] == 'C':
        residues.append(dict(case=case_id, **row))
        classified.append(dict(case=case_id, reason='necessary_returned_C_residue'))
        continue
    # Foreign RAW and even its actual M11 miss q. The combined context first
    # needs it black later. q is in neither foreign entry nor exit active core.
    z = local(q, row['foreign_pose'])
    foreign_context = lit.trace(words[row['foreign']]+lit.M)
    assert z not in foreign_context['first']
    assert context['first'][z][0] == 'L' and z not in lit.K
    returned_pose = row['returned_pose']
    assert local(q, returned_pose) not in lit.K
    repair_rows.append(dict(case=case_id, source_deleted_q=q,
                            foreign_local_q=z, first_combined_read=context['first'][z],
                            foreign_complete_context_misses_q=True,
                            returned_local_q=local(q, returned_pose)))
    classified.append(dict(case=case_id, reason='age3_deleted_core_birth_and_RAW'))

assert Counter(row['reason'] for row in classified) == {
    'PREforeign_protected_combined_context': 24,
    'age1_exact_W_counts_and_RAW': 15,
    'age3_deleted_core_birth_and_RAW': 9,
    'necessary_returned_C_residue': 3,
}
assert sum(len(row['forced_RAW_conflicts']) for row in one_C_rows) == 22
assert sum(row['no_allowed_last_packet'] for row in one_C_rows) == 2

# q's actual current identity at foreign entry must have a later OLD full
# producer: source completion leaves it white; the foreign does not read it.
# Clock one: W head x<=0,y>=1 after C exit(0,1,W). Every full-output alignment
# violates a coordinate of that necessary cone, INCLUDING its own C tails.
birth_clock1 = []
for source_id in keep:
    for output in map(tuple, G[source_id]['outputs']):
        p = sub(q, lit.rot(output, 3))
        assert not (p[0] <= 0 and p[1] >= 1)
        birth_clock1.append(dict(full_producer=G[source_id]['name'], output=output,
                                 pose=(*p, 3), necessary_W_cone=False))

# Clock two: S head x<=-1. With full completion by clock three, only zero/one-C
# full producers are possible. Sector and x leave precisely r=(0,0) outputs at
# head(-1,-1,S). Its x equality forces no W bases and no S D/V; S U steps then
# give y=1-4u, never -1. This is an exact congruence, not a word cap.
birth_clock2 = []
clock2_residual_heads = []
for source_id in keep:
    for output in map(tuple, G[source_id]['outputs']):
        p = add(q, output)
        if G[source_id]['name'].count('C') > 1:
            reason = 'full_C_tails_cannot_complete_before_foreign_clock3'
        elif (sum(p)+2) % 2:
            reason = 'sector'
        elif p[0] > -1:
            reason = 'necessary_S_head_x'
        else:
            assert output == (0, 0) and p == (-1, -1)
            assert source_id in (4, 5, 7, 8)
            reason = 'x_equality_and_y1_minus4u_cannot_equal_minus1'
            clock2_residual_heads.append((G[source_id]['name'], p))
        birth_clock2.append(dict(full_producer=G[source_id]['name'], output=output,
                                 pose=(*p, 2), reason=reason))
assert len(clock2_residual_heads) == 4

# Clock three: no consumer C tail can finish before the foreign. Sector leaves
# eight odd base outputs. Five bases already meet the older C chord, violating
# the signed PREforeign U-entry simplicity. The three others are retained.
old_C_chord = ((-1, -1), (1, 1))
birth_clock3 = []
helpers = []
for source_id in (0, 4, 7):
    for output in map(tuple, G[source_id]['outputs']):
        p = sub(q, lit.rot(output, 1))
        start = add((2*p[0], 2*p[1]), lit.rot((-1, -1), 1))
        vector = lit.rot({0: (2, 2), 4: (2, 6), 7: (0, 8)}[source_id], 1)
        endpoint = add(p, lit.rot(G[source_id]['endpoint'][:2], 1))
        contact = closed_contact(*old_C_chord, start, add(start, vector))
        if (sum(p)+1) % 2:
            reason = 'sector'
        elif contact is not None:
            reason = 'earlier_PREforeign_source_C_base_contact'
        else:
            reason = 'exact_remaining_E_suffix_required'
            helpers.append(dict(base=G[source_id]['name'], output=output,
                                pose=(*p, 1), full_exit=(*endpoint, 1)))
        birth_clock3.append(dict(base=G[source_id]['name'], output=output,
                                 pose=(*p, 1), full_exit=(*endpoint, 1),
                                 reason=reason, old_C_contact=contact))
assert len(helpers) == 3
assert {(row['base'], tuple(row['output']), tuple(row['full_exit'])) for row in helpers} == {
    ('V', (0, 1), (1, -2, 1)),
    ('U', (-1, 2), (1, -2, 1)),
    ('U', (2, 1), (2, 1, 1)),
}

helper_suffix_rows = []
for repair in repair_rows:
    case_id = repair['case']
    row = catalogue['old_source_contact_cases'][case_id]
    for helper in helpers:
        delta = sub(row['foreign_pose'][:2], helper['full_exit'][:2])
        solutions = counts_E(delta)
        controls = []
        for counts in solutions:
            for sequence in orders(*counts):
                last = sequence[-1] if sequence else helper['base']
                if last not in allowed_last(row['foreign']):
                    continue
                word = words[helper['base']]+''.join(words[a] for a in sequence)+words[row['foreign']]+words[row['returned_atom']]+lit.M
                trace = lit.trace(word)
                assert not trace['feasible']
                controls.append(dict(E_sequence=sequence, conflict=trace))
        helper_suffix_rows.append(dict(case=case_id, helper=helper,
                                       exact_E_displacement=delta,
                                       count_solutions=solutions,
                                       allowed_last_RAW_conflicts=controls,
                                       no_allowed_last_packet=not controls))
assert len(helper_suffix_rows) == 27
assert sum(len(row['allowed_last_RAW_conflicts']) for row in helper_suffix_rows) == 12
assert all(not row['allowed_last_RAW_conflicts'] for row in helper_suffix_rows
           if row['helper']['full_exit'] == (2, 1, 1))
assert {(row['foreign'], tuple(row['foreign_pose']), row['returned_atom'],
         row['source_to_foreign_C_age']) for row in residues} == {
    ('F', (2, -5, 1), 'C', 3),
    ('Q', (4, -5, 1), 'C', 3),
    ('B', (5, -4, 1), 'C', 3),
}

dependencies = [
    HERE/'first_returned_atom_contact_manifest.json',
    HERE/'first_foreign_all_source_join_manifest.json',
    HERE/'first_foreign_C_source_exclusion_manifest.json',
    HERE/'complete8_foreign_adjacency_manifest.json',
    ROOT/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',
    ROOT/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',
    ROOT/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',
    ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json',
    ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json',
    ROOT/'word_stabilization/check_foreign_return_interfaces.py',
]
out = dict(
    status='AUTHOR_FROZEN_C_SOURCE_RETURNED_CONTACT_REDUCTION_PENDING_REVIEW',
    scope='Exactly one first foreign then its immediate raw ordinary atom; chronological first new contact with an actual old C. Bud protection is used only at foreign ENTRY against exact combined RAW constraints. No postforeign age law or residual reset. Three returned-C necessary residues remain, none asserted attainable.',
    classification_counts=dict(Counter(row['reason'] for row in classified)),
    classified_cases=classified, PREforeign_protected_combined_contexts=protected_rows,
    age1_exact_W_words=one_C_rows,
    deleted_core_white_in_all_actual_full_sources=white_source_roles,
    age3_deleted_core_repair_obligations=repair_rows,
    old_birth_clock1_queries=birth_clock1,
    old_birth_clock2_queries=birth_clock2,
    old_birth_clock3_queries=birth_clock3,
    old_birth_clock3_surviving_helpers=helpers,
    exact_E_helper_suffixes=helper_suffix_rows,
    necessary_remaining_cases=residues,
    dependencies={str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                  for path in dependencies})
(HERE/'returned_C_source_reduction.json').write_text(json.dumps(out, indent=2)+'\n')
print('51 C-source rows:', out['classification_counts'])
print('Age1 fixed-word conflicts22; age3 helper fixed-word conflicts12; necessary residues3.')
