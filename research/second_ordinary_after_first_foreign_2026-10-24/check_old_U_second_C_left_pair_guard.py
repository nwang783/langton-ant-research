"""Exact eight-pose lift of the signed original-LEFT transfer.

This checks geometry and actual raw-C before colors only. It does not rerun or
extend the foreign transfer enumeration, and uses no post-foreign age law.
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

def floor(q):
    return q.numerator // q.denominator

def ceil(q):
    return -((-q.numerator) // q.denominator)

def fraction(q):
    return [q.numerator, q.denominator]

old_a, old_b = chord('U', (0, 0, 0))
assert (old_a, old_b) == ((-1, -1), (-1, 7))
old_v = sub(old_b, old_a)
c_before = lit.trace(W['C'] + lit.M)
assert c_before['feasible']

# Reuse only the independently signed angle interface. Its n is the actual
# source-entry-to-FOREIGN count; effective N additionally counts b1=C.
signed_angles = json.loads((H / 'small_second_ordinary_geometry.json').read_text())['conditional217_old_source_angle_interfaces']
angles = [r for r in signed_angles if r['old_source'] == 'U' and r['second_ordinary'] == 'C']
assert len(angles) == 16
assert Counter(r['first_ordinary'] for r in angles) == dict.fromkeys('DCVU', 4)
for row in angles:
    n = row['actual_old_source_to_FOREIGN_C_age']
    N = row['total_ordinary_C_before_second']
    assert n == N - int(row['first_ordinary'] == 'C')
    assert 1 <= N <= 4 and 0 <= n <= 4
    assert row['second_heading_relative_old_source'] == (2 - N) % 4

boxes, poses = [], []
for N in range(1, 5):
    h = (2 - N) % 4
    c, d = chord('C', (0, 0, h))
    v = sub(d, c)
    den = det(old_v, v)
    assert den != 0  # No parallel or collinear U/C case is omitted.
    # 2p = old_a + s*old_v - c - t*v. The closed contact parameter
    # square gives an exact parallelogram, not an arbitrary spatial cap.
    corners = [tuple(Q(old_a[k] + s * old_v[k] - c[k] - t * v[k], 2)
                     for k in (0, 1)) for s in (0, 1) for t in (0, 1)]
    bounds = [(floor(min(p[k] for p in corners)), ceil(max(p[k] for p in corners)))
              for k in (0, 1)]
    boxes.append(dict(effective_N=N, heading=h,
                      exact_closed_head_parallelogram=[[fraction(q) for q in p] for p in corners],
                      exhaustive_integer_head_bounds=bounds))
    for x in range(bounds[0][0], bounds[0][1] + 1):
        for y in range(bounds[1][0], bounds[1][1] + 1):
            # Every primitive has even length except C. Both foreign lengths
            # are even, so head checkerboard parity equals N modulo two.
            if (x + y - N) % 2:
                continue
            cc, dd = add(c, (2 * x, 2 * y)), add(d, (2 * x, 2 * y))
            z = sub(cc, old_a)
            s, t = Q(det(z, v), den), Q(det(z, old_v), den)
            if not (0 <= s < 1 and 0 < t <= 1):
                continue
            entries, obstructions = [], []
            for original in LEFT:
                local = lit.rot(sub(original, (x, y)), -h)
                first = c_before['first'].get(local)
                r = dict(original_U_birth_cell=original, second_C_local_cell=local,
                         lies_in_actual_second_entry_K=local in lit.K)
                if first is not None:
                    turn, tick = first
                    r['actual_first_read'] = owner.describe('C', tick)
                    r['required_initial_BLACK'] = turn == 'L'
                else:
                    r['actual_first_read'] = None
                if local in lit.K:
                    r['contradiction'] = 'Signed fixed LEFT is CURRENT outside this entry K, but this pose puts that SAME identity inside K.'
                    obstructions.append(r)
                elif first is not None and first[0] == 'R':
                    assert first[1] < len(W['C'])
                    assert r['actual_first_read']['owner'] == 'own C-tail 1 RAW'
                    r['contradiction'] = 'SAME original identity is still physically BLACK; actual first RAW read requires WHITE.'
                    obstructions.append(r)
                entries.append(r)
            assert obstructions
            poses.append(dict(effective_N=N, second_C_pose=(x, y, h),
                              source_parameter_s=fraction(s), second_parameter_t=fraction(t),
                              both_fixed_LEFT_current_id_locations=entries,
                              actual_core_or_RAW_WHITE_obstructions=obstructions))

expected = {(1, (-1, 0, 1)), (1, (-1, 2, 1)),
            (2, (-1, -1, 0)), (2, (-1, 1, 0)),
            (3, (0, -1, 3)), (3, (0, 1, 3)),
            (4, (0, 0, 2)), (4, (0, 2, 2))}
assert {(r['effective_N'], r['second_C_pose']) for r in poses} == expected
assert len(poses) == 8 and all(r['second_parameter_t'] == [1, 1] for r in poses)
assert all(r['source_parameter_s'] in ([0, 1], [1, 2]) for r in poses)

paths = [H / 'small_second_ordinary_geometry_manifest.json',
         R / 'audits/check_second_ordinary_small_interface_independent.json',
         R / 'U_star_one_foreign_return_transfer_2026-10-24/manifest.json',
         R / 'audits/check_U_star_second_entry_transfer_independent.json',
         R / 'foreign_U_raw_ages34_2026-10-23/manifest.json',
         R / 'audits/check_foreign_U_raw_ages34_independent.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
transfer = json.loads(paths[3].read_text())
assert transfer['status'].startswith('PASS')
assert transfer['author_manifest'] == hashlib.sha256(paths[2].read_bytes()).hexdigest()

out = dict(status='AUTHOR_FROZEN_OLD_U_SECOND_RAW_C_LEFT_PAIR_GUARD_PENDING_REVIEW',
           scope='Chronological FIRST new contact of SECOND ordinary RAW C with a genuine outgoing old U-base chord, after a U-entry complete-eight prefix, its FIRST foreign, and one immediate ordinary RAW. Actual next M11 is valid. No later RAW or second-foreign extension.',
           exact_source_chord_doubled=[old_a, old_b],
           signed16_angle_interfaces=angles,
           exact4_contact_parallelograms=boxes,
           exact8_outgoing_owned_C_poses_all_excluded=poses,
           source_clock_use='True source-entry-to-FOREIGN age n = N - 1[b1=C] is at most 4. Apply BEFORE-foreign first-effect >=5, then the signed fixed-LEFT transfer. Never apply maturity at N or across foreign.',
           original_identity_interface='At SECOND entry both original U(0,0),U(0,1) are physically BLACK SAME birth labels and CURRENT outside that actual entry K.',
           conclusion='No chronological first new SECOND-atom contact with outgoing old U-base source can be made by SECOND RAW C.',
           no_postforeign_maturity_or_new_producer=True,
           no_general_second_simplicity=True,
           dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'old_U_second_C_left_pair_guard.json').write_text(json.dumps(out, indent=2) + '\n')
print('16 signed angle interfaces; four exact parallelograms; eight outgoing-owned C poses, all blocked by SAME original LEFT current IDs.')
print('Only true pre-foreign n <= 4 is used. All WHITE conflicts are inside actual C RAW; no future read or maturity is imported.')
