"""Small exact old-C age-one SECOND-contact slice with actual source roles.

After the selected C only one zero-C W run occurs before A. No unsupported
standalone-C source age or fictitious producer is introduced.
"""
from pathlib import Path
from itertools import permutations
from collections import Counter
import importlib.util
import hashlib
import json

R = Path('/workspace/shared/langton')
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('literal', R / 'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(spec); spec.loader.exec_module(lit)
spec = importlib.util.spec_from_file_location('ownership', R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner = importlib.util.module_from_spec(spec); spec.loader.exec_module(owner)
W = owner.WORDS

def add(p, q): return p[0] + q[0], p[1] + q[1]
def sub(p, q): return p[0] - q[0], p[1] - q[1]
def raw(tokens): return ''.join(W[a] for a in tokens)
def after(word, pose=(0, 0, 0)):
    p, h = pose[:2], pose[2]
    for turn in word:
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
    return (*p, h)
def z2(pose): return add((2 * pose[0], 2 * pose[1]), lit.rot((-1, -1), pose[2]))

assert after(W['C']) == (0, 1, 3)
assert (z2((0, 0, 0)), z2(after(W['C']))) == (z2((0, 0, 0)), z2(after(W['D'])))
Cgeo = lit.literal_geometry(W['C'])
assert Cgeo['inputs'] == [] and Cgeo['outputs'] == [[1, 2], [2, 0], [2, 1]]

roles, unfinished_roles = [], []
for full in ('DC', 'VC', 'VCC', 'UC', 'UCC'):
    fullbody = raw(full); tr = lit.trace(fullbody); fg = lit.literal_geometry(fullbody)
    for selected_index in range(1, full.count('C') + 1):
        prefix = full[0] + 'C' * (selected_index - 1)
        start = after(raw(prefix)); prior_birth_tick = len(raw(prefix)) - 2
        beta = add(start[:2], lit.rot((1, -1), start[2]))
        common = add(start[:2], lit.rot((2, 0), start[2]))
        j = selected_index - 1
        r = dict(containing_full_packet=full, selected_C_index1=selected_index,
            actual_prefix_before_selected_C=prefix, actual_selected_C_full_pose=start,
            selected_C_atomic_clock=0, containing_full_source_entry_clock=-j,
            containing_full_source_age_at_FOREIGN=1 + j,
            containing_full_completion_clock=full.count('C') - j,
            incoming_beta_full_cell=beta, incoming_beta_actual_R_tick0=prior_birth_tick,
            actual_incoming_bud_post_EXIT_age_at_FOREIGN=1,
            common_output_full_cell=common,
            common_actual_R_tick0=len(raw(prefix)) + 8)
        if r['containing_full_completion_clock'] > 1:
            r['exclusion'] = 'containing full source cannot finish by true atomic-to-FOREIGN clock1'
            unfinished_roles.append(r)
        else:
            assert tr['last'][beta] == ('R', prior_birth_tick)
            assert tr['last'][common] == ('R', len(raw(prefix)) + 8)
            assert list(beta) in fg['outputs'] and list(common) in fg['outputs']
            roles.append(r)
assert len(roles) == 5 and len(unfinished_roles) == 2
assert {(r['containing_full_packet'], r['selected_C_index1']) for r in roles} == {
    ('DC', 1), ('VC', 1), ('UC', 1), ('VCC', 2), ('UCC', 2)}

# Direction, sector and actual n/N headings are identical to signed old-D1
# geometry: C and D corrected chords coincide, true n=1, N=1+1[b1=C].
# Only the history/role proof changes, and is reconstructed above.
D = json.loads((R / 'second_old_D_age1_2026-10-24/D_age1_first_contact.json').read_text())
typed, count_rows, words = [], [], {}
for source in D['all69_foreign_alignments']:
    A, b1, b2 = source['foreign'], source['first'], source['second']
    pa, p2 = tuple(source['foreign_pose']), tuple(source['second_pose'])
    assert pa[2] == 3 and p2[2] == (0 if b1 == 'C' else 1)
    tr = lit.trace(W[A] + W[b1] + W[b2] + lit.M)
    reason = 'remaining'
    if not tr['feasible']: reason = 'immutable_local_context'
    else:
        for guard in ((2, 0), (1, -1)):
            q = lit.rot(sub(guard, pa[:2]), 1)
            first = tr['first'].get(q)
            if q in lit.K: reason = 'CURRENT_guard_in_FOREIGN_core'; break
            if first is not None and first[0] == 'R': reason = 'CURRENT_guard_before_WHITE'; break
    row = dict(foreign=A, first=b1, second=b2, foreign_pose=pa, second_pose=p2,
               true_atomic_preforeign_age=1, effective_N=1 + int(b1 == 'C'), classification=reason)
    typed.append(row)
    if reason != 'remaining': continue
    rem = pa[1] - 1
    if rem < 0: continue
    for dW in range(rem + 1):
        vW = rem - dW
        numerator = -dW - 3 * vW - pa[0]
        if numerator < 0 or numerator % 4: continue
        uW = numerator // 4
        if dW + vW + uW == 0: continue
        count_rows.append(dict(foreign=A, first=b1, second=b2, foreign_pose=pa,
                               second_pose=p2, dW=dW, vW=vW, uW=uW))
        for Y in sorted(set(permutations('D' * dW + 'V' * vW + 'U' * uW))):
            if Y[-1] not in ('VU' if A in 'FQ' else 'U'): continue
            old = 'C' + ''.join(Y)
            tokens = old + A + b1 + b2
            assert after(raw(old)) == pa
            if tokens in words: continue
            whole = lit.trace(raw(tokens) + lit.M)
            assert not whole['feasible']
            before = lit.trace(raw(old))
            words[tokens] = dict(tokens=list(tokens), old_W_run=list(Y), foreign=A,
                first=b1, second=b2, foreign_pose=pa, second_pose=p2,
                immutable_conflict=whole,
                conflict_stage='old_RAW_prefix' if not before['feasible'] else 'foreign_or_returned_RAW_or_actual_marker')
assert len(typed) == 69
assert Counter(r['classification'] for r in typed) == {
    'remaining': 45, 'CURRENT_guard_before_WHITE': 18, 'immutable_local_context': 6}
assert len(count_rows) == 75 and len(words) == 194

def physical_owner(tokens, tick):
    lo = 0
    for i, atom in enumerate(tokens):
        if tick < lo + len(W[atom]):
            return dict(actual_atom_index0=i, actual_atom=atom, atom_start_tick0=lo,
                        canonical=owner.describe(atom, tick - lo))
        lo += len(W[atom])
    j = tick - lo
    assert 0 <= j < len(lit.M)
    return dict(actual_atom='next actual word', next_word_tick0=j,
                next_word_read_number1=j + 1, turn=lit.M[j])
for tokens, record in words.items():
    c = record['immutable_conflict']
    record['previous_actual_read_owner'] = physical_owner(tokens, c['previous_read'])
    record['failing_actual_read_owner'] = physical_owner(tokens, c['conflict_read'])

paths = [R / 'second_old_D_age1_2026-10-24/manifest.json',
         R / 'audits/check_old_D_second_age1_independent.json',
         R / 'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',
         R / 'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',
         R / 'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',
         R / 'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_OLD_C_AGE1_SECOND_CONTACT_PENDING_REVIEW',
    scope='Only outgoing actual old C inside a genuine containing complete-eight packet, true atomic C-entry-to-FIRSTforeign age1, chronological FIRST SECOND ordinary RAW contact plus actual finalM11. No standalone-C source license, otherC age or second simplicity.',
    actual_C_LITERAL=Cgeo,
    five_actual_completed_containing_roles=roles,
    two_source_roles_excluded_by_full_completion=unfinished_roles,
    true_preFOREIGN_CURRENT_guardians=[dict(cell=(2, 0), source='selected C actual R8, atomic minimum3 with correct C2 shift'),
                                      dict(cell=(1, -1), source='actual previous BASE/C1 EXIT bud, postEXIT age1 by signed1325')],
    geometric_reuse='Selected C and D corrected chords are literally identical. True n=1 and effectiveN=1+1[b1=C] give the same exact16 parallelograms/23 b1-typed poses/69 A alignments; the selected-C containing-role clocks are NOT reused from D.',
    all69_literal_guarded_alignments=typed,
    exact75_W_endpoint_count_solutions=count_rows,
    all194_distinct_whole_words_all_immutable_conflicting=[words[t] for t in sorted(words)],
    exact_word_stage_counts=dict(Counter(r['conflict_stage'] for r in words.values())),
    all_length_endpoint_equation='After selected C:head(0,1,W). A=(-dW-3vW-4uW,1+dW+vW,W). Nonempty W run, lastV/U(orU forB). y fixes dW+vW and x fixes uW; all orders retained.',
    conclusion='No actual old C source at true preforeign age1 realizes the stipulated second first-contact. Every guarded possible one-C body word is already impossible on ANY board at its selected C entry, so no ancestor enumeration or ghost-source substitution is needed.',
    no_postforeign_maturity_or_identity_reset=True,
    no_general_SECOND_simplicity=True,
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'C_age1_first_contact.json').write_text(json.dumps(out, indent=2) + '\n')
print('Five actual completed C-source roles, two unfinished roles removed; same69 geometry labels give45 guarded cases.')
print('Exact75 W-run counts and194 all-order whole words, every one immutable-color inconsistent. No ancestry depth or standalone-C assumption.')
