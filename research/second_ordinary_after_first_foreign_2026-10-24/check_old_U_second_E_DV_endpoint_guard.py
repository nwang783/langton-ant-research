"""All-length one-C endpoint guard for old-U/second east-facing D or V.

No trajectory depth is chosen. The exact contact parallelograms, SAME original
LEFT labels, and one-C N/W height equations determine all endpoint words.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import hashlib
import importlib.util
import json

R = Path('/workspace/shared/langton')
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('literal', R / 'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)
spec = importlib.util.spec_from_file_location('ownership', R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(owner)
W = owner.WORDS
LEFT = ((0, 0), (0, 1))

def add(p, q):
    return p[0] + q[0], p[1] + q[1]

def sub(p, q):
    return p[0] - q[0], p[1] - q[1]

def det(p, q):
    return p[0] * q[1] - p[1] * q[0]

def after(word, pose=(0, 0, 0)):
    p, h = pose[:2], pose[2]
    for turn in word:
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
    return (*p, h)

def z2(pose):
    return add((2 * pose[0], 2 * pose[1]), lit.rot((-1, -1), pose[2]))

def chord(atom, pose):
    return z2(pose), z2(after(W[atom], pose))

def fraction(q):
    return [q.numerator, q.denominator]

def floor(q):
    return q.numerator // q.denominator

def ceil(q):
    return -((-q.numerator) // q.denominator)

angles = json.loads((H / 'small_second_ordinary_geometry.json').read_text())['conditional217_old_source_angle_interfaces']
slice_angles = [r for r in angles if r['old_source'] == 'U'
                and r['second_ordinary'] in 'DV' and r['second_heading_relative_old_source'] == 1]
assert len(slice_angles) == 8
assert all(r['total_ordinary_C_before_second'] == 1 for r in slice_angles)
assert all(r['actual_old_source_to_FOREIGN_C_age'] == (0 if r['first_ordinary'] == 'C' else 1)
           for r in slice_angles)

# b1=C gives n=0, already independently excluded in the complete old-U
# zero-preforeign-C slice. For every remaining b1, true preforeign n=1.
assert {r['first_ordinary'] for r in slice_angles if r['actual_old_source_to_FOREIGN_C_age'] == 0} == {'C'}
n1_angles = [r for r in slice_angles if r['actual_old_source_to_FOREIGN_C_age'] == 1]
assert len(n1_angles) == 6

old_a, old_b = chord('U', (0, 0, 0))
old_v = sub(old_b, old_a)
boxes, all_geometry, surviving_heads = [], [], {}
for b2 in 'DV':
    c, d = chord(b2, (0, 0, 1))
    v = sub(d, c)
    den = det(old_v, v)
    assert den != 0
    corners = [tuple(Q(old_a[k] + s * old_v[k] - c[k] - t * v[k], 2)
                     for k in (0, 1)) for s in (0, 1) for t in (0, 1)]
    bounds = [(floor(min(p[k] for p in corners)), ceil(max(p[k] for p in corners)))
              for k in (0, 1)]
    boxes.append(dict(second=b2, exact_head_parallelogram=[[fraction(q) for q in p] for p in corners],
                      exhaustive_integer_bounds=bounds))
    before = lit.trace(W[b2] + lit.M)
    assert before['feasible']
    for x in range(bounds[0][0], bounds[0][1] + 1):
        for y in range(bounds[1][0], bounds[1][1] + 1):
            if (x + y - 1) % 2:
                continue
            z = sub(add(c, (2 * x, 2 * y)), old_a)
            s, t = Q(det(z, v), den), Q(det(z, old_v), den)
            if not (0 <= s < 1 and 0 < t <= 1):
                continue
            witnesses = []
            labels = []
            for original in LEFT:
                local = lit.rot(sub(original, (x, y)), -1)
                f = before['first'].get(local)
                r = dict(original=original, second_local_cell=local, entry_core=local in lit.K,
                         first_read=None if f is None else owner.describe(b2, f[1]))
                if local in lit.K or (f is not None and f[0] == 'R'):
                    witnesses.append(r)
                labels.append(r)
            row = dict(second=b2, pose=(x, y, 1), source_s=fraction(s), second_t=fraction(t),
                       fixed_LEFT_locations=labels, core_or_before_WHITE_witnesses=witnesses)
            all_geometry.append(row)
            if not witnesses:
                assert b2 not in surviving_heads
                surviving_heads[b2] = row['pose']
assert Counter(r['second'] for r in all_geometry) == {'D': 2, 'V': 6}
assert surviving_heads == {'D': (-1, 0, 1), 'V': (-3, 0, 1)}

# True n=1 means a plain source U or its own first C tail followed by exactly
# one C total. Every packet before that C is N-oriented and every packet
# after it is W-oriented. Full C-tail ownership is preserved: primitive C is
# an actual read interval, not an additional complete packet.
assert after(W['U']) == (0, 4, 0)
assert after(W['C']) == (0, 1, 3)
increments = {}
for h in (0, 3):
    increments[str(h)] = {a: after(W[a], (0, 0, h)) for a in 'DVU'}
assert increments['0'] == {'D': (1, 1, 0), 'V': (1, 3, 0), 'U': (0, 4, 0)}
assert increments['3'] == {'D': (-1, 1, 3), 'V': (-3, 1, 3), 'U': (-4, 0, 3)}

foreign_rows, endpoint_words = [], []
for b2, p2 in surviving_heads.items():
    for b1 in 'DVU':
        for A in 'FQB':
            displacement = after(W[A] + W[b1], (0, 0, 3))
            assert displacement[2] == 1
            ap = (p2[0] - displacement[0], p2[1] - displacement[1], 3)
            assert ap[1] <= 5
            r = dict(second=b2, first=b1, foreign=A, foreign_pose=ap,
                     one_C_prefix_height_lower_bound=5,
                     endpoint_count_solutions=[])
            if ap[1] == 5:
                # 5+dN+3vN+4uN+dW+vW=5 forces all five counts zero.
                # Consequently xA=-4uW. This is an exact unbounded-run
                # deduction; the equation determines uW, not a run cap.
                if ap[0] <= 0 and ap[0] % 4 == 0:
                    uW = -ap[0] // 4
                    assert uW > 0
                    tokens = ['U', 'C'] + ['U'] * uW + [A, b1, b2]
                    raw = ''.join(W[a] for a in tokens)
                    assert after(''.join(W[a] for a in tokens[:2 + uW])) == ap
                    tr = lit.trace(raw + lit.M)
                    assert not tr['feasible']
                    assert (tr['conflict_read'], tr['previous_read'], tr['turn'], tr['cell']) == (57, 29, 'L', [-1, 4])
                    r['endpoint_count_solutions'].append(dict(dN=0, vN=0, uN=0, dW=0, vW=0, uW=uW))
                    endpoint_words.append(dict(tokens=tokens, foreign_pose=ap,
                                               immutable_RAW_conflict=tr,
                                               previous_actual_read=owner.describe('C', 1),
                                               later_actual_read=owner.describe('U', 14)))
            foreign_rows.append(r)
assert len(foreign_rows) == 18
assert {tuple(r['tokens']) for r in endpoint_words} == {
    tuple('UCUFDD'), tuple('UCUUQVD'), tuple('UCUUQDV'), tuple('UCUUFVV')}
assert len(endpoint_words) == 4
cu = lit.trace(W['C'] + W['U'] + lit.M)
assert not cu['feasible'] and (cu['conflict_read'], cu['previous_read']) == (29, 1)
assert 29 < len(W['C']) + len(W['U'])

paths = [H / 'small_second_ordinary_geometry_manifest.json',
         R / 'audits/check_second_ordinary_small_interface_independent.json',
         H / 'zero_preforeign_C_old_U_slice_manifest.json',
         R / 'audits/check_zero_C_old_U_second_contact_independent.json',
         R / 'U_star_one_foreign_return_transfer_2026-10-24/manifest.json',
         R / 'audits/check_U_star_second_entry_transfer_independent.json',
         R / 'foreign_U_raw_ages34_2026-10-23/manifest.json',
         R / 'audits/check_foreign_U_raw_ages34_independent.json',
         R / 'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_OLD_U_SECOND_E_DV_ENDPOINT_GUARD_PENDING_REVIEW',
           scope='Chronological FIRST new SECOND-ordinary contact with outgoing old U-base source, where second RAW is D or V and heads E in the old creating-U N frame. Actual U-entry complete-eight prefix, FIRST foreign, b1, b2 and real final M11. No south/west or later-return conclusion.',
           signed8_angle_interfaces=slice_angles,
           zero_preforeign_age_branch_already_signed_excluded=True,
           remaining_true_preforeign_age=1,
           exact2_contact_parallelograms=boxes,
           exact8_geometries_six_current_LEFT_color_cuts=all_geometry,
           two_current_LEFT_compatible_second_heads=surviving_heads,
           actual_N_W_DVU_increments=increments,
           all_length_prefix_endpoint_identity=dict(x='dN+vN-dW-3vW-4uW',
                                                   y='5+dN+3vN+4uN+dW+vW',
                                                   counts='All six counts are nonnegative integers. C is the sole actual C interval; its y increment is one.'),
           exact18_foreign_head_obligations=foreign_rows,
           exact4_whole_endpoint_words_all_immutable_RAW_conflicts=endpoint_words,
           universal_actual_raw_C_U_conflict=cu,
           short_structural_proof='Every foreign obligation has y<=5. Any nonempty W run after the sole C must begin D/V, because actual raw C->U is impossible, and then y>=6. The exact equality case instead yields only U-only W runs, all conflicting. Empty W gives x>=0 and cannot attain these negative foreign heads.',
           no_postforeign_age_or_old_full_packet_reset=True,
           no_prepared_positive_or_U_entry_realization_claimed=True,
           conclusion='Old outgoing U cannot own a chronological first SECOND-atom contact by east-facing D/V.',
           dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'old_U_second_E_DV_endpoint_guard.json').write_text(json.dumps(out, indent=2) + '\n')
print('Eight E-facing D/V contact poses -> two LEFT-compatible heads; eighteen foreign obligations have y<=5.')
print('Exact one-C N/W endpoints -> four whole words, all actual C->U immutable RAW conflicts. No run-length cap or post-foreign maturity.')
