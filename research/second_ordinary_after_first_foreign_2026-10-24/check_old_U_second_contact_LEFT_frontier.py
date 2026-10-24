"""Small exact original-LEFT frontier for SECOND D/V/U old-U contacts.

Uses the signed one-return simplicity and fixed-LEFT identity transfer only.
No general corner overapproximation or post-foreign maturity is substituted.
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
LEFT = {(0, 0), (0, 1)}
STAR = LEFT | {(1, 0), (1, 1)}

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

def transform(q, pose):
    return add(pose[:2], lit.rot(q, pose[2]))

def closed_intersection(a, b, c, d):
    u, v, z = sub(b, a), sub(d, c), sub(c, a)
    den = det(u, v)
    if den:
        s, t = Q(det(z, v), den), Q(det(z, u), den)
        if 0 <= s <= 1 and 0 <= t <= 1:
            return dict(kind='point', old_s=fraction(s), new_t=fraction(t))
        return None
    if det(z, u):
        return None
    k = 0 if u[0] else 1
    lo, hi = sorted((Q(c[k] - a[k], u[k]), Q(d[k] - a[k], u[k])))
    lo, hi = max(Q(0), lo), min(Q(1), hi)
    return None if lo > hi else dict(kind='collinear', old_s_interval=[fraction(lo), fraction(hi)])

old_a, old_b = chord('U', (0, 0, 0))
old_v = sub(old_b, old_a)
signed_angles = json.loads((H / 'small_second_ordinary_geometry.json').read_text())['conditional217_old_source_angle_interfaces']
angles = [r for r in signed_angles if r['old_source'] == 'U' and r['second_ordinary'] in 'DVU']
assert len(angles) == 44
assert all(0 <= r['actual_old_source_to_FOREIGN_C_age'] <= 4 for r in angles)

# Exact geometry before first-atom/foreign positions are introduced.
boxes, geometries, parallel_start_rejections = [], [], []
for b2 in 'DVU':
    for N in sorted({r['total_ordinary_C_before_second'] for r in angles if r['second_ordinary'] == b2}):
        h = (2 - N) % 4
        c, d = chord(b2, (0, 0, h))
        v = sub(d, c)
        den = det(old_v, v)
        corners = [tuple(Q(old_a[k] + s * old_v[k] - c[k] - t * v[k], 2)
                         for k in (0, 1)) for s in (0, 1) for t in (0, 1)]
        bounds = [(floor(min(p[k] for p in corners)), ceil(max(p[k] for p in corners)))
                  for k in (0, 1)]
        boxes.append(dict(second=b2, effective_N=N, heading=h, parallel=not den,
                          exact_closed_head_parallelogram=[[fraction(q) for q in p] for p in corners],
                          exhaustive_integer_bounds=bounds))
        before = lit.trace(W[b2] + lit.M)
        assert before['feasible']
        for x in range(bounds[0][0], bounds[0][1] + 1):
            for y in range(bounds[1][0], bounds[1][1] + 1):
                if (x + y - N) % 2:
                    continue
                cc, dd = add(c, (2 * x, 2 * y)), add(d, (2 * x, 2 * y))
                z = sub(cc, old_a)
                if den:
                    s, t = Q(det(z, v), den), Q(det(z, old_v), den)
                    if not (0 <= s < 1 and 0 < t <= 1):
                        continue
                    kind = 'nonparallel point'
                else:
                    # The ONLY parallel case is same-direction U at N=2.
                    assert b2 == 'U' and N == 2 and v == old_v
                    if det(z, old_v):
                        continue
                    assert x == 0
                    start_s = Q(z[1], old_v[1])
                    if 0 <= start_s < 1:
                        parallel_start_rejections.append(dict(second_pose=(x, y, h),
                            old_source_parameter_at_SECOND_entry=fraction(start_s),
                            reason='CUT2 already lies on the earlier U chord; this contradicts signed one-atom OPEN simplicity before any second read.'))
                        continue
                    # Earliest positive new time at old source s=0. y=4
                    # merely starts at the old terminal and moves away: no
                    # positive-time old-outgoing intersection exists.
                    t, s = -start_s, Q(0)
                    if not (0 < t <= 1):
                        continue
                    kind = 'same-direction collinear first onset'
                labels, left_obstructions, other_white = [], [], []
                for original in sorted(STAR):
                    local = lit.rot(sub(original, (x, y)), -h)
                    f = before['first'].get(local)
                    r = dict(original_U_cell=original, second_local_cell=local,
                             known_same_CURRENT_outside_entry_K=original in LEFT,
                             known_same_physically_BLACK=True,
                             lies_in_actual_entry_K=local in lit.K,
                             first_read=None if f is None else owner.describe(b2, f[1]))
                    if original in LEFT and (local in lit.K or (f is not None and f[0] == 'R')):
                        left_obstructions.append(r)
                    elif original not in LEFT and f is not None and f[0] == 'R':
                        assert local not in lit.K
                        other_white.append(r)
                    labels.append(r)
                classification = ('LEFT_current_core_or_WHITE' if left_obstructions else
                                  'other_original_physically_BLACK_but_before_WHITE' if other_white else
                                  'LEFT_and_all_original_BLACK_compatible')
                geometries.append(dict(second=b2, effective_N=N, second_pose=(x, y, h),
                    contact_kind=kind, source_s=fraction(s), second_t=fraction(t),
                    all_original_ID_before_locations=labels, LEFT_obstructions=left_obstructions,
                    other_original_before_WHITE_obstructions=other_white, classification=classification))
assert len(boxes) == 11
assert Counter(r['second'] for r in geometries) == {'D': 8, 'V': 16, 'U': 18}
assert len(parallel_start_rejections) == 2
assert {tuple(r['second_pose']) for r in parallel_start_rejections} == {(0, 0, 0), (0, 2, 0)}
assert Counter(r['classification'] for r in geometries) == {
    'LEFT_current_core_or_WHITE': 29,
    'other_original_physically_BLACK_but_before_WHITE': 3,
    'LEFT_and_all_original_BLACK_compatible': 10}

# Three E-facing poses remain at this point. D/V are independently excluded
# by the earlier all-length endpoint theorem. For U, the remaining pose has y=-1,
# and all A+b1 inverse heads have y<=4. The exact true-one-C old-prefix
# equation yA=5+dN+3vN+4uN+dW+vW rules them out immediately.
east_U_heads, seven = [], []
for geo in geometries:
    if geo['classification'] != 'LEFT_and_all_original_BLACK_compatible':
        continue
    b2, N, p2 = geo['second'], geo['effective_N'], geo['second_pose']
    if p2[2] == 1:
        assert N == 1
        if b2 == 'U':
            assert p2[1] == -1
            for b1 in 'DVU':
                for A in 'FQB':
                    displacement = after(W[A] + W[b1], (0, 0, 3))
                    ap = (p2[0] - displacement[0], p2[1] - displacement[1], 3)
                    assert ap[1] <= 4
                    east_U_heads.append(dict(second_U_pose=p2, foreign=A, first=b1,
                                             true_preforeign_age=1, foreign_pose=ap,
                                             strict_height_contradiction=[ap[1], 5]))
            # b1=C gives actual raw C->U, independently impossible; do not
            # pretend that n=0 is a true one-C preforeign interval.
        else:
            assert b2 in 'DV'
        continue
    seven.append(geo)
assert len(east_U_heads) == 9
assert len(seven) == 7
cu = lit.trace(W['C'] + W['U'] + lit.M)
assert not cu['feasible'] and (cu['conflict_read'], cu['previous_read']) == (29, 1)

# Each remaining pose and the signed (b1,n,N) interface determine A's pose.
# All are genuinely later than the old U, so no immediate U->A adjacency
# exception can apply when checking the already-simple prior proxy.
typed, counts = [], Counter()
for geo in seven:
    b2, N, p2 = geo['second'], geo['effective_N'], geo['second_pose']
    for angle in angles:
        if angle['second_ordinary'] != b2 or angle['total_ordinary_C_before_second'] != N:
            continue
        n, b1 = angle['actual_old_source_to_FOREIGN_C_age'], angle['first_ordinary']
        ha = (-n) % 4
        for A in 'FQB':
            displacement = after(W[A] + W[b1], (0, 0, ha))
            assert displacement[2] == p2[2]
            ap = (p2[0] - displacement[0], p2[1] - displacement[1], ha)
            raw = W[A] + W[b1] + W[b2]
            full = lit.trace(raw + lit.M)
            afirst = lit.trace(W[A] + lit.M)
            assert afirst['feasible']
            ahits = [dict(original_U_cell=q, FOREIGN_local_cell=lit.rot(sub(q, ap[:2]), -ha),
                          first_read=owner.describe(A, afirst['first'][lit.rot(sub(q, ap[:2]), -ha)][1]))
                     for q in sorted(STAR) if lit.rot(sub(q, ap[:2]), -ha) in afirst['first']]
            Fcut = after(W['F'], ap)
            aend = after(W[A], ap)
            vertices = [z2(ap), z2(Fcut)] + ([] if A == 'F' else [z2(aend)])
            prior_contacts = []
            for part, (c, d) in enumerate(zip(vertices, vertices[1:])):
                hit = closed_intersection(old_a, old_b, c, d)
                if hit is not None:
                    prior_contacts.append(dict(part='foreign piece', piece_index=part, intersection=hit))
            hit = closed_intersection(old_a, old_b, *chord(b1, aend))
            if hit is not None:
                prior_contacts.append(dict(part='first ordinary chord', intersection=hit))
            if not full['feasible']:
                reason = 'immutable_local_RAW_context_conflict'
            elif ahits:
                reason = 'FOREIGN_complete_context_hits_original_star_below_age5'
            elif prior_contacts:
                reason = 'already_signed_simple_prior_proxy_contacts_old_U'
            else:
                reason = 'necessary_only_unresolved'
            row = dict(second=b2, effective_N=N, true_preforeign_age=n,
                       foreign=A, foreign_pose=ap, first=b1, second_pose=p2,
                       local_literal_context_feasible=full['feasible'],
                       local_context_conflict=None if full['feasible'] else full,
                       FOREIGN_original_star_hits=ahits,
                       prior_proxy_old_U_contacts=prior_contacts,
                       classification=reason)
            typed.append(row)
            counts[reason] += 1
assert len(typed) == 84
assert counts == {'immutable_local_RAW_context_conflict': 9,
                  'FOREIGN_complete_context_hits_original_star_below_age5': 15,
                  'necessary_only_unresolved': 60}
remaining = [r for r in typed if r['classification'] == 'necessary_only_unresolved']
assert Counter(r['second'] for r in remaining) == {'D': 9, 'V': 27, 'U': 24}
assert Counter(r['true_preforeign_age'] for r in remaining) == {3: 42, 4: 18}
assert any(r['foreign'] == 'F' and tuple(r['foreign_pose']) == (4, -3, 1)
           and r['first'] == 'D' and r['second'] == 'U' and tuple(r['second_pose']) == (1, 2, 3)
           for r in remaining)

paths = [H / 'small_second_ordinary_geometry_manifest.json',
         R / 'audits/check_second_ordinary_small_interface_independent.json',
         H / 'old_U_second_C_left_pair_guard_manifest.json',
         R / 'audits/check_old_U_second_C_left_guard_independent.json',
         H / 'old_U_second_E_DV_endpoint_guard_manifest.json',
         R / 'audits/check_old_U_second_E_DV_endpoint_independent.json',
         R / 'U_star_one_foreign_return_transfer_2026-10-24/manifest.json',
         R / 'audits/check_U_star_second_entry_transfer_independent.json',
         R / 'foreign_U_raw_ages34_2026-10-23/manifest.json',
         R / 'audits/check_foreign_U_raw_ages34_independent.json',
         R / 'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
         R / 'audits/check_first_foreign_returned_simplicity_independent.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_OLD_U_SECOND_CONTACT_LEFT_FRONTIER_PENDING_REVIEW',
    scope='Chronological FIRST new SECOND ordinary RAW D/V/U contact with outgoing old U-base source. U-entry complete-eight prefix, FIRST foreign, exactly two immediate RAWs plus actual final M11. A necessary-only frontier; no second simplicity or ancestry realization.',
    signed44_angle_interfaces=angles,
    clock_warning='All true preforeign n<=4. N=n+1[b1=C] is an effective tangent clock only. There is no n>=5 remainder in this scope.',
    physical_transfer_interface='SAME original LEFT is CURRENT outside CUT2 K. All four originals are physically BLACK at CUT2, but RIGHT may be CORE and is never asserted CURRENT.',
    exact11_contact_parallelograms=boxes,
    same_direction_parallel_SECOND_entry_already_old_rejections=parallel_start_rejections,
    exact42_outgoing_owned_contact_poses=geometries,
    geometry_classification_counts=dict(Counter(r['classification'] for r in geometries)),
    exact9_east_U_foreign_heads_impossible_below_one_C_height=east_U_heads,
    actual_RAW_C_U_conflict=cu,
    exact7_remaining_geometric_poses=seven,
    all84_foreign_first_second_typed_alignments=typed,
    disjoint_typed_classification_counts=dict(counts),
    exact60_necessary_only_remaining_states=remaining,
    conclusion='Every old-U-source first SECOND contact, if it exists, is in one of these seven poses/60 typed states, with true preforeign age3 or4. SECOND C is separately excluded; n<=2 is excluded for every second letter.',
    no_postforeign_maturity_or_three_way_corner_substitution=True,
    no_genuine_U_entry_attainment_claimed=True,
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'old_U_second_contact_LEFT_frontier.json').write_text(json.dumps(out, indent=2) + '\n')
print('42 exact D/V/U poses: 29 original-LEFT cuts, three other-original WHITE cuts, 10 local survivors.')
print('E endpoint guards leave seven poses; 84 typed states split 9 RAW + 15 foreign-hit + 60 necessary residues at true ages 3/4.')
