"""First returned ordinary atom after exactly one first foreign: geometry only.

Derives rational intersections from parallelogram boxes and the exact n+2
turning horizon.  No source-output lifetime is extended across the foreign.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import hashlib
import json
import importlib.util

ROOT = Path('/workspace/shared/langton')
HERE = Path(__file__).resolve().parent
GP = ROOT / 'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
WP = ROOT / 'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G = json.loads(GP.read_text())['geometry']
MACROS = json.loads(WP.read_text())['macro_words']
WORDS = {name: MACROS[i]['word'] for i, name in enumerate('DCVUFQB')}
M = G[0]['marker']
VEC = ((0, 1), (1, 0), (0, -1), (-1, 0))
STEPS = {'D': (2, 2), 'C': (2, 2), 'V': (2, 6), 'U': (0, 8)}
RANK = {'U': 0, 'V': 1, 'D': 2, 'C': 2}
LOCAL_PIECES = {
    'F': [((-1, -1), (-7, -3))],
    'Q': [((-1, -1), (-7, -3)), ((-7, -3), (-7, -7))],
    'B': [((-1, -1), (-7, -3)), ((-7, -3), (-5, -9))],
}


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def det(p, q):
    return p[0] * q[1] - p[1] * q[0]


def derive(word):
    p = (0, 0)
    h = 0
    for letter in word:
        h = (h + (-1 if letter == 'L' else 1)) % 4
        p = add(p, VEC[h])
    return p, h


def literal_context(word):
    """Exact symbolic first-color constraints, not a trajectory search."""
    p, h = (0, 0), 0
    first, parity = {}, set()
    for tick, letter in enumerate(word):
        initial_black = (letter == 'L') ^ (p in parity)
        if p in first and first[p] != initial_black:
            return dict(feasible=False, conflict_tick=tick, cell=p)
        first[p] = initial_black
        parity.symmetric_difference_update({p})
        h = (h + (-1 if letter == 'L' else 1)) % 4
        p = add(p, VEC[h])
    return dict(feasible=True, required_black=sum(first.values()),
                required_sites=len(first), end_pose=(*p, h))


def chord(atom, p=(0, 0), h=0):
    start = add((2*p[0], 2*p[1]), rot((-1, -1), h))
    return start, add(start, rot(STEPS[atom], h))


def closed_hit(a, b, c, d):
    u, v, z = sub(b, a), sub(d, c), sub(c, a)
    denominator = det(u, v)
    if denominator:
        s = Q(det(z, v), denominator)
        t = Q(det(z, u), denominator)
        return dict(kind='point', s=s, t=t) if 0 <= s <= 1 and 0 <= t <= 1 else None
    if det(z, u):
        return None
    k = 0 if u[0] else 1
    sa = Q(c[k]-a[k], u[k])
    sb = Q(d[k]-a[k], u[k])
    lo, hi = max(Q(0), min(sa, sb)), min(Q(1), max(sa, sb))
    return dict(kind='collinear', s_interval=(lo, hi)) if lo <= hi else None


def outgoing_first_hit(a, b, c, d):
    """Earlier parameter s<1, new t>0; parallel onset owned by old start."""
    hit = closed_hit(a, b, c, d)
    if hit is None:
        return None
    if hit['kind'] == 'point':
        return hit if 0 <= hit['s'] < 1 and 0 < hit['t'] <= 1 else None
    u, v = sub(b, a), sub(d, c)
    k = 0 if v[0] else 1
    # If the later segment enters at the old END, that vertex is owned by
    # the next outgoing old atom, not by this source. A genuine same-direction
    # onset enters at old START; zero-time overlap is impossible here by the
    # already-simple preceding foreign path.
    if u[k] * v[k] <= 0:
        return None
    t = Q(a[k]-c[k], v[k])
    return dict(kind='collinear_first_onset', s=Q(0), t=t) if 0 < t <= 1 else None


FOREIGN_ENDPOINTS = {name: derive(WORDS[name]) for name in 'FQB'}
assert FOREIGN_ENDPOINTS == {'F': ((-4, -2), 2), 'Q': ((-4, -4), 2), 'B': ((-3, -5), 2)}
ATOM_ENDPOINTS = {name: derive(WORDS[name]) for name in 'DCVU'}


def actual_foreign_pieces(foreign, p, h):
    return [(add((2*p[0], 2*p[1]), rot(a, h)),
             add((2*p[0], 2*p[1]), rot(b, h)))
            for a, b in LOCAL_PIECES[foreign]]


angle_rows = []
rows = []
discard_counts = Counter()
for source in 'DCVU':
    for target in 'DCVU':
        for n in range(5):
            if source == 'C' and n == 0:
                continue
            sign = (RANK[source] > RANK[target]) - (RANK[source] < RANK[target])
            allowed = n in (1, 2, 3) or n == 0 and sign > 0 or n == 4 and sign < 0
            if not allowed:
                continue
            effective = n + 2
            h = (2-n) % 4
            angle_rows.append(dict(source=source, returned_atom=target,
                                   source_to_foreign_C_age=n,
                                   effective_quarter_clock=effective,
                                   returned_heading=h))
            a, b = chord(source)
            u = sub(b, a)
            base = rot((-1, -1), h)
            v = rot(STEPS[target], h)
            # 2p = old_start + s*old_vector - target_start_offset
            #      - t*target_vector. Bounds are exact closed parallelograms.
            corners = [sub(add(a, (s*u[0], s*u[1])),
                           add(base, (t*v[0], t*v[1])))
                       for s in (0, 1) for t in (0, 1)]
            bounds = [((min(q[i] for q in corners)+1)//2,
                       max(q[i] for q in corners)//2) for i in (0, 1)]
            for x in range(bounds[0][0], bounds[0][1]+1):
                for y in range(bounds[1][0], bounds[1][1]+1):
                    if (x+y+h) % 2:
                        continue
                    p = x, y
                    contact = outgoing_first_hit(a, b, *chord(target, p, h))
                    if contact is None:
                        continue
                    for foreign in 'FQB':
                        hF = (-n) % 4
                        epF, ehF = FOREIGN_ENDPOINTS[foreign]
                        pF = sub(p, rot(epF, hF))
                        assert (hF+ehF) % 4 == h
                        pieces = actual_foreign_pieces(foreign, pF, hF)
                        assert pieces[-1][1] == chord(target, p, h)[0]
                        clearance = []
                        blocked = False
                        for piece_id, (c, d) in enumerate(pieces):
                            earlier = closed_hit(a, b, c, d)
                            if earlier is None:
                                continue
                            epS, ehS = ATOM_ENDPOINTS[source]
                            actual_adjacent = (
                                piece_id == 0 and earlier['kind'] == 'point'
                                and earlier['s'] == 1 and earlier['t'] == 0
                                and pF == epS and hF == ehS
                                and source in ('V', 'U'))
                            if not actual_adjacent:
                                blocked = True
                                break
                            clearance.append(dict(piece=piece_id, contact=earlier,
                                                  actual_initial_adjacency=True))
                        if blocked:
                            discard_counts['foreign_would_already_contact_old_source'] += 1
                            continue
                        rows.append(dict(
                            source_atom=source, returned_atom=target,
                            foreign=foreign, source_to_foreign_C_age=n,
                            effective_quarter_clock=effective,
                            foreign_pose=(*pF, hF), returned_pose=(*p, h),
                            contact=contact, exact_candidate_bounds=bounds,
                            legal_foreign_initial_adjacencies=clearance))

assert len(angle_rows) == 56

# Exact local returned-atom/foreign contacts are checked separately. These
# require no old source age and cannot be hidden in a first-contact hypothesis.
local_rows = []
for foreign in 'FQB':
    ep, eh = FOREIGN_ENDPOINTS[foreign]
    pieces = LOCAL_PIECES[foreign]
    for target in 'DCVU':
        target_chord = chord(target, ep, eh)
        contacts = []
        initial_adjacent_contacts = []
        for piece_id, (a, b) in enumerate(pieces):
            hit = closed_hit(a, b, *target_chord)
            if hit is None:
                continue
            terminal = piece_id == len(pieces)-1 and b == target_chord[0]
            adjacent_point = hit['kind'] == 'point' and hit['s'] == 1 and hit['t'] == 0
            adjacent_collinear_point = (hit['kind'] == 'collinear'
                                        and hit['s_interval'] == (Q(1), Q(1)))
            if terminal and (adjacent_point or adjacent_collinear_point):
                initial_adjacent_contacts.append(dict(earlier_piece=piece_id,
                                                       contact=hit))
            else:
                contacts.append(dict(earlier_piece=piece_id, contact=hit))
        assert not contacts and len(initial_adjacent_contacts) == 1
        local_rows.append(dict(foreign=foreign, returned_atom=target,
                               returned_pose=(*ep, eh), new_contacts=contacts,
                               allowed_initial_adjacency=initial_adjacent_contacts,
                               literal_pair=literal_context(WORDS[foreign]+WORDS[target]+M)))
assert all(row['literal_pair']['feasible'] for row in local_rows)

# Prepared finite literal controls are kept separate from old U-entry ancestry.
full_packet_successors = []
for foreign in 'FQB':
    for source_id in (0, 1, 4, 5, 6, 7, 8, 9):
        control = literal_context(WORDS[foreign]+G[source_id]['word']+M)
        assert control['feasible']
        full_packet_successors.append(dict(
            foreign=foreign, returned_full_packet=G[source_id]['name'],
            prepared_literal_pair=control,
            creator_history_claimed=False))
assert len(full_packet_successors) == 24

# Actual containing old fullproducer roles, with no clock reset at internal C.
C_roles = json.loads((HERE/'first_foreign_C_source_exclusion.json').read_text())['C_full_producer_roles']
source_role_annotations = []
for row_id, row in enumerate(rows):
    source, n = row['source_atom'], row['source_to_foreign_C_age']
    if source == 'C':
        roles = [dict(full_packet=role['full_packet'], C_index=role['C_index'],
                      full_source_C_age=n+role['atomic_to_full_consumer_age_shift'],
                      full_source_completed=(n >= 1+role['remaining_C_tails']))
                 for role in C_roles]
    else:
        source_ids = {'D': (0, 1), 'V': (4, 5, 6), 'U': (7, 8, 9)}[source]
        roles = [dict(full_packet=G[i]['name'], full_source_C_age=n,
                      full_source_completed=(n >= G[i]['name'].count('C')))
                 for i in source_ids]
    assert any(role['full_source_completed'] for role in roles)
    source_role_annotations.append(dict(case=row_id, roles=roles))


def encode(x):
    if isinstance(x, Q):
        return int(x) if x.denominator == 1 else str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


dependencies = [GP, WP, HERE/'first_foreign_all_source_join_manifest.json',
                HERE/'foreign_kinked_barrier_manifest.json',
                HERE/'complete8_foreign_adjacency_manifest.json',
                HERE/'first_foreign_C_source_exclusion_manifest.json',
                ROOT/'core_periodicity_new/first_center_contact_frozen_20261023_1412/manifest.json']
out = dict(
    status='DRAFT_EXACT_ONE_FOREIGN_RETURNED_ATOM_INTERFACE',
    scope='Chronological first new contact of the first raw ordinary D/C/V/U atom immediately following exactly one first complete foreign after an actual U-entry eight factor. Geometry only; no postforeign output lifetime or iterative simplicity claim.',
    clock_convention='n is the actual C count from earlier old atomic source entry inclusive to foreign entry exclusive. There is exactly one foreign, its true preceding-C bit is zero, and the returned ordinary entry immediately follows its RAW exit. Effective turning count is n+2.',
    angle_cases=angle_rows, old_source_contact_cases=rows,
    old_source_contact_counts=dict(Counter((r['source_atom'] for r in rows))),
    foreign_counts=dict(Counter(r['foreign'] for r in rows)),
    returned_atom_counts=dict(Counter(r['returned_atom'] for r in rows)),
    source_age_counts=dict(Counter(r['source_to_foreign_C_age'] for r in rows)),
    discarded_by_clearance=dict(discard_counts),
    local_foreign_returned_atom_cases=local_rows,
    prepared_full_packet_successor_controls=full_packet_successors,
    actual_old_fullproducer_clock_annotations=source_role_annotations,
    foreign_actual_endpoints=FOREIGN_ENDPOINTS,
    dependencies={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in dependencies})
(HERE/'first_returned_atom_contact.json').write_text(json.dumps(encode(out), indent=2)+'\n')
print('56 exact angle cases; geometric source-contact rows:', len(rows))
print('Source counts:', out['old_source_contact_counts'])
print('Foreign counts:', out['foreign_counts'])
print('Returned atoms:', out['returned_atom_counts'])
print('Source ages:', out['source_age_counts'])
print('Local foreign contacts:', [(r['foreign'], r['returned_atom'], r['new_contacts'])
                                  for r in local_rows if r['new_contacts']])
