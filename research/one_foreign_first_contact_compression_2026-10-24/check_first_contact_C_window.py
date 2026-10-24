"""Exact turn telescoping and source-relative first-contact C windows.

No word-depth search, physical field quotient, or postforeign age law is used.
Formal angles are A*pi/4+B*atan(1/3), checked as Gaussian rationals.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
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

def add(p, q):
    return p[0] + q[0], p[1] + q[1]

def sub(p, q):
    return p[0] - q[0], p[1] - q[1]

def det(p, q):
    return p[0] * q[1] - p[1] * q[0]

def dot(p, q):
    return p[0] * q[0] + p[1] * q[1]

def after(word, pose=(0, 0, 0)):
    p, h = pose[:2], pose[2]
    for turn in word:
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
    return (*p, h)

def z2(pose):
    return add((2 * pose[0], 2 * pose[1]), lit.rot((-1, -1), pose[2]))

def direction(atom, heading=0):
    return sub(z2(after(W[atom], (0, 0, heading))), z2((0, 0, heading)))

def ap(a, b):
    return a[0] + b[0], a[1] + b[1]

def am(a, b):
    return a[0] - b[0], a[1] - b[1]

def cmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]

def cpow(z, n):
    if n < 0:
        norm = dot(z, z)
        return cpow((Q(z[0], norm), Q(-z[1], norm)), -n)
    out = (Q(1), Q(0))
    for _ in range(n):
        out = cmul(out, z)
    return out

def angle_ray(angle):
    # arg(1+i)=pi/4 and arg(3+i)=beta. Positive scaling is irrelevant.
    return cmul(cpow((1, 1), angle[0]), cpow((3, 1), angle[1]))

def coeff_range(angle):
    # beta/(pi/4) lies STRICTLY between0 and1.
    A, B = angle
    return min(A, A + B), max(A, A + B)

def strict_range(angle, lo, hi):
    a, b = coeff_range(angle)
    return a >= lo and b <= hi and not (angle[1] == 0 and angle[0] in (lo, hi))

def verify_principal(u, v, expected):
    actual = (dot(u, v), det(u, v))
    ray = angle_ray(expected)
    assert det(actual, ray) == 0 and dot(actual, ray) > 0
    assert strict_range(expected, -4, 4)
    return dict(incoming=u, outgoing=v,
                exact_dot_det_rotation=actual,
                principal_angle_pi_over4_beta_coefficients=expected,
                coefficient_range_at_beta_endpoints=coeff_range(expected))

ALPHA = {'D': (1, 0), 'C': (1, 0), 'V': (0, 1), 'U': (0, 0)}
assert {a: direction(a) for a in 'DCVU'} == {
    'D': (2, 2), 'C': (2, 2), 'V': (2, 6), 'U': (0, 8)}
ordinary = []
for a, b in product('DCVU', repeat=2):
    expected = ap((2 * int(a == 'C'), 0), am(ALPHA[a], ALPHA[b]))
    hnext = 3 if a == 'C' else 0
    checked = verify_principal(direction(a), direction(b, hnext), expected)
    ordinary.append(dict(previous=a, next=b, actual_next_heading=hnext, **checked))
assert len(ordinary) == 16

# Derive genuine foreign piece directions from actual fine exits, never from
# the invalid collapsed whole Q/B chord.
foreign = {}
for A in 'FQB':
    fcut, end = after(W['F']), after(W[A])
    vertices = [z2((0, 0, 0)), z2(fcut)] + ([] if A == 'F' else [z2(end)])
    pieces = [sub(b, a) for a, b in zip(vertices, vertices[1:])]
    assert end[2] == 2
    foreign[A] = dict(actual_vertices=vertices, directions=pieces, actual_exit=end,
                      internal_F56_cut_is_not_a_marker=True)
assert foreign['F']['directions'] == [(-6, -2)]
assert foreign['Q']['directions'] == [(-6, -2), (0, -4)]
assert foreign['B']['directions'] == [(-6, -2), (2, -6)]

splices = []
for a, A, b in product('DVU', 'FQB', 'DCVU'):
    pieces = foreign[A]['directions']
    joins = [verify_principal(direction(a), pieces[0], ap((2, 1), ALPHA[a]))]
    total = ap((2, 1), ALPHA[a])
    if A != 'F':
        internal = (2, -1) if A == 'Q' else (2, 0)
        joins.append(verify_principal(pieces[0], pieces[1], internal))
        total = ap(total, internal)
    last_join = am({'F': (2, -1), 'Q': (0, 0), 'B': (0, -1)}[A], ALPHA[b])
    joins.append(verify_principal(pieces[-1], direction(b, 2), last_join))
    total = ap(total, last_join)
    expected_total = ap((4, 0), am(ALPHA[a], ALPHA[b]))
    assert total == expected_total
    splices.append(dict(previous_non_C_base=a, foreign=A, next_ordinary=b,
                        exact_principal_joins=joins,
                        whole_splice_angle_coefficients=total))
assert len(splices) == 36

# Actual C->foreign would introduce a -2pi wrap. It is not dropped by a
# generic positivity assumption: the signed complete-eight/foreign pair law
# excludes it in the present history. Raw CF/Q/B themselves are feasible.
CF_controls = []
for A, b in product('FQB', 'DCVU'):
    pieces = [lit.rot(v, 3) for v in foreign[A]['directions']]
    joins = [verify_principal(direction('C'), pieces[0], (-3, 1))]
    total = (-3, 1)
    if A != 'F':
        internal = (2, -1) if A == 'Q' else (2, 0)
        joins.append(verify_principal(pieces[0], pieces[1], internal))
        total = ap(total, internal)
    last = am({'F': (2, -1), 'Q': (0, 0), 'B': (0, -1)}[A], ALPHA[b])
    joins.append(verify_principal(pieces[-1], direction(b, 1), last))
    total = ap(total, last)
    formal_without_wrap = ap((6, 0), am(ALPHA['C'], ALPHA[b]))
    assert am(formal_without_wrap, total) == (8, 0)
    CF_controls.append(dict(previous='C', foreign=A, next_ordinary=b,
                            actual_principal_splice_coefficients=total,
                            false_unwrapped_coefficients=formal_without_wrap,
                            omitted_wrap_would_be_exactly_2pi=True))
raw_CF_feasible = []
for A in 'FQB':
    tr = lit.trace(W['C'] + W[A] + lit.M)
    assert tr['feasible']
    raw_CF_feasible.append(dict(foreign=A, complete_minimal_mass=sum(turn == 'L' for turn, tick in tr['first'].values()),
                                actual_RAW_C_foreign_plus_M11_feasible=True))

# Remaining foreign-piece-to-first-ordinary turns. These are the endpoint
# corrections when the source itself lies inside a foreign piece.
piece_endpoints = []
for piece, Aset, offset in [('Fprefix', 'FQB', (2, -1)),
                            ('Qtail', 'Q', (0, 0)),
                            ('Btail', 'B', (0, -1))]:
    for A, b in product(Aset, 'DCVU'):
        dirs = foreign[A]['directions']
        start = 0 if piece == 'Fprefix' else 1
        total = (0, 0)
        if start == 0 and A != 'F':
            total = ap(total, (2, -1) if A == 'Q' else (2, 0))
        total = ap(total, am({'F': (2, -1), 'Q': (0, 0), 'B': (0, -1)}[A], ALPHA[b]))
        expected = am(offset, ALPHA[b])
        assert total == expected
        piece_endpoints.append(dict(source_piece=piece, actual_foreign=A, next_ordinary=b,
                                    remaining_foreign_and_join_angle_coefficients=total))
assert len(piece_endpoints) == 20

def window_status(angle):
    # Jordan first-contact open turn is strictly (pi,3pi), i.e.(4,12).
    lo, hi = coeff_range(angle)
    if strict_range(angle, 4, 12):
        return True
    assert hi <= 4 or lo >= 12, ('No beta-dependent undecided case is permitted', angle)
    return False

windows = []
for source_class, sources in [('preFOREIGN_ordinary', 'DCVU'), ('postFOREIGN_ordinary', 'DCVU')]:
    for a, b in product(sources, 'DCVU'):
        offset = ap((4 if source_class == 'preFOREIGN_ordinary' else 0, 0), am(ALPHA[a], ALPHA[b]))
        allowed = [K for K in range(11) if window_status(ap((2 * K, 0), offset))
                   and not (a == 'C' and K == 0)]
        expected = ([K for K in range(5) if (K not in (0, 4) or
                    (K == 0 and ALPHA[a] != ALPHA[b] and {'U': 0, 'V': 1, 'D': 2, 'C': 2}[a] > {'U': 0, 'V': 1, 'D': 2, 'C': 2}[b]) or
                    (K == 4 and {'U': 0, 'V': 1, 'D': 2, 'C': 2}[a] < {'U': 0, 'V': 1, 'D': 2, 'C': 2}[b]))
                    and not (a == 'C' and K == 0)]
                    if source_class == 'preFOREIGN_ordinary' else
                    [K for K in range(2, 7) if K not in (2, 6) or
                     (K == 2 and {'U': 0, 'V': 1, 'D': 2, 'C': 2}[a] > {'U': 0, 'V': 1, 'D': 2, 'C': 2}[b]) or
                     (K == 6 and {'U': 0, 'V': 1, 'D': 2, 'C': 2}[a] < {'U': 0, 'V': 1, 'D': 2, 'C': 2}[b])])
        assert allowed == expected
        windows.append(dict(source_class=source_class, source_atom=a, contact_atom=b,
                            open_turn_offset_pi_over4_beta=offset,
                            allowed_C_counts_before_contact_ENTRY=allowed))
for piece, offset in [('Fprefix', (2, -1)), ('Qtail', (0, 0)), ('Btail', (0, -1))]:
    for b in 'DCVU':
        actual_offset = am(offset, ALPHA[b])
        allowed = [K for K in range(11) if window_status(ap((2 * K, 0), actual_offset))]
        expected = list(range(2, 6)) if piece == 'Fprefix' else list(range(3, 6 if piece == 'Qtail' and b == 'U' else 7))
        assert allowed == expected
        windows.append(dict(source_class=piece, contact_atom=b,
                            open_turn_offset_pi_over4_beta=actual_offset,
                            allowed_C_counts_before_contact_ENTRY=allowed))
assert len(windows) == 44
assert Counter(r['source_class'] for r in windows) == {
    'preFOREIGN_ordinary': 16, 'postFOREIGN_ordinary': 16,
    'Fprefix': 4, 'Qtail': 4, 'Btail': 4}
assert {c: sum(len(r['allowed_C_counts_before_contact_ENTRY']) for r in windows if r['source_class'] == c)
        for c in ('preFOREIGN_ordinary', 'postFOREIGN_ordinary', 'Fprefix', 'Qtail', 'Btail')} == {
    'preFOREIGN_ordinary': 56, 'postFOREIGN_ordinary': 58, 'Fprefix': 16, 'Qtail': 15, 'Btail': 16}

paths = [R / 'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',
         R / 'audits/check_foreign_kinked_barrier_turn_independent.json',
         R / 'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
         R / 'audits/check_complete8_foreign_adjacency_independent.json',
         R / 'seven_word_spatial_return_2026-10-23/first_foreign_all_source_join_manifest.json',
         R / 'audits/check_first_foreign_all_source_join_independent.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_ONE_FOREIGN_FIRST_CONTACT_C_WINDOW_PENDING_REVIEW',
    scope='An actual U-entry complete-eight prefix, its FIRST foreign A, then an arbitrary finite ordinary RAW suffix with actual marker contexts. The expanded proxy is simple strictly before its FIRST later contact. Necessary source-relative C windows only; no bound on atom counts, whole suffix C count, physical identities or global simplicity.',
    angle_convention='A formal pair(A,B) denotes A*pi/4+B*beta, beta=atan(1/3), strictly between0 andpi/4. alpha(U)=0,alpha(V)=beta,alpha(D/C)=pi/4 is DEFLECTION FROM NORTH, not the earlier note direction-angle alpha.',
    all16_ordinary_principal_joins=ordinary,
    true_foreign_piece_geometry=foreign,
    all36_nonC_foreign_principal_splices=splices,
    exact12_C_foreign_wrap_controls=CF_controls,
    actual_raw_C_foreign_controls=raw_CF_feasible,
    all20_foreign_piece_source_endpoint_offsets=piece_endpoints,
    all44_exact_source_target_C_window_rows=windows,
    Jordan_interface='Earliest positive contact plus outgoing old-piece ownership gives a simple closed loop. Opposite tangent rays would overlap before first contact, so closing principal turn delta is strictly(-pi,pi); same-direction collinear onset has delta0 and is retained. Every source-class open-turn lower bound is greater than -pi/2, so Jordan orientation must be+2pi, whence pi<T_open<3pi.',
    source_clock_conventions='K counts actual C RAW intervals from ordinary source ENTRY up to but EXCLUDING the contact atom ENTRY, including source C itself. For a foreign-piece source, K counts actual postFOREIGN Cs before contact ENTRY. A terminal contact C is not counted; no new fullproducer is assigned to internal fine cuts.',
    telescoping_identity='preA ordinary: T=(K+2)*pi/2+alpha(source)-alpha(target); postA ordinary: T=K*pi/2+alpha(source)-alpha(target). Foreign-piece offsets are in the exact table.',
    monotone_epoch_consequence='A candidate contact loop contains at most seven ordinary constant-heading epochs, plus at most two repaired foreign pieces. Epoch lengths, physical diameters and dormant boundary resources remain unbounded.',
    late_contact_consequence='After five postFOREIGN Cs, a first contact cannot have a preFOREIGN ordinary source. After seven postFOREIGN Cs it cannot have a foreign-piece source either. Any later first contact, if it exists, is with a postFOREIGN ordinary source within its last six-C window.',
    no_later_U_entry_or_old_reflex_enclosure_assumed=True,
    no_arbitrary_tail_simplicity_or_second_foreign_extension=True,
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
def serial(o):
    if isinstance(o, Q):
        return [o.numerator, o.denominator]
    raise TypeError(type(o))
(H / 'first_contact_C_window.json').write_text(json.dumps(out, indent=2, default=serial) + '\n')
print('Exact Gaussian-rational principal joins: ordinary16, foreign splices36, CF-wrap controls12, foreign-piece offsets20.')
print('44 source/target window rows: preA K<=4; postA ordinary K2..6; Fprefix2..5, Qtail3..6 with endpoint refinement, Btail3..6.')
