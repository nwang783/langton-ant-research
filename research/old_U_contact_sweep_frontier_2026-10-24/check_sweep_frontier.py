"""Quantitative sweep bags and the remaining unbounded-coordinate gap.

The finite-bag theorem is for an embedded old-U first-contact window. The
two-track nonregular example is a geometric certificate obstruction ONLY,
not an actual Langton-ant or U-entry countercontrol.
"""
from pathlib import Path
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

def s(p):
    return 2 * p[0] + p[1]

def t(p):
    return p[0] - 2 * p[1]

def add(p, q):
    return p[0] + q[0], p[1] + q[1]

def sub(p, q):
    return p[0] - q[0], p[1] - q[1]

def path(word, pose=(0, 0, 0)):
    p, h = pose[:2], pose[2]
    vertices, reads = [p], []
    for tick, turn in enumerate(word):
        reads.append(dict(position=p, turn=turn, tick0=tick))
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
        vertices.append(p)
    return vertices, reads, (*p, h)

drifts, footprints = [], []
for atom in 'DCVUFQB':
    for h in range(4):
        vertices, reads, end = path(W[atom], (0, 0, h))
        values = list(map(s, vertices))
        row = dict(atom=atom, heading=h, actual_head_drift=end[:2],
                   sweep_drift=s(end[:2]), transverse_drift=t(end[:2]),
                   exact_fine_vertex_sweep_interval=[min(values), max(values)],
                   RAW_read_count=len(reads))
        footprints.append(row)
        if atom in 'DCVU':
            assert row['sweep_drift'] != 0
            assert (row['sweep_drift'] > 0) == (h in (0, 1))
            drifts.append(row)
assert len(drifts) == 16
assert {a: [r['sweep_drift'] for r in drifts if r['atom'] == a] for a in 'DCVU'} == {
    'D': [3, 1, -3, -1], 'C': [1, 2, -1, -2],
    'V': [5, 5, -5, -5], 'U': [4, 8, -4, -8]}
ordinary_radius = max(abs(v) for r in footprints if r['atom'] in 'DCVU' for v in r['exact_fine_vertex_sweep_interval'])
foreign_radius = max(abs(v) for r in footprints if r['atom'] in 'FQB' for v in r['exact_fine_vertex_sweep_interval'])
marker_radius = max(abs(s(p)) for h in range(4) for p in path(lit.M, (0, 0, h))[0])
assert (ordinary_radius, foreign_radius, marker_radius) == (8, 14, 5)

# A heading epoch's ordinary entry s values are distinct integers, progressing
# by at least1, including its terminal C. K<=4 plus one foreign split yields
# at most6 such epochs; terminal contact C belongs to the last entry-heading
# epoch and creates no extra ordinary epoch inside the window.
epoch_count_bound = 6
heads_per_epoch = 2 * ordinary_radius + 1
ordinary_atom_bag_bound = epoch_count_bound * heads_per_epoch
all_blocks_bound = ordinary_atom_bag_bound + 2
read_occurrence_bag_bound = ordinary_atom_bag_bound * max(len(W[a]) for a in 'DCVU') + max(len(W[a]) for a in 'FQB') + len(lit.M)
assert (heads_per_epoch, ordinary_atom_bag_bound, all_blocks_bound, read_occurrence_bag_bound) == (17, 102, 104, 2941)

def concrete_control(n):
    tokens = ['U', 'F'] + ['D'] * n
    word = ''.join(W[a] for a in tokens)
    tr = lit.trace(word + lit.M)
    assert tr['feasible']
    seed = {q for q, (turn, tick) in tr['first'].items() if turn == 'L'}
    black = set(seed)
    p, h = (0, 0), 0
    all_reads, blocks, tick_global = [], [], 0
    for i, (a, body) in enumerate([(a, W[a]) for a in tokens] + [('actual final M11', lit.M)]):
        vertices, reads, end = path(body, (*p, h))
        block = dict(index0=i, symbol=a, entry=(p[0], p[1], h),
                     sweep_interval=[min(map(s, vertices)), max(map(s, vertices))],
                     RAW_or_prefix_read_count=len(reads), first_global_read_tick0=tick_global)
        for r in reads:
            q, turn = r['position'], r['turn']
            assert (q in black) == (turn == 'L')
            if turn == 'L':
                black.remove(q)
            else:
                black.add(q)
            all_reads.append(dict(position=q, turn=turn, block=i,
                                  global_tick0=tick_global + r['tick0']))
        blocks.append(block)
        p, h = end[:2], end[2]
        tick_global += len(body)
    # Build exact repeated-cell edges, actual chronological chain edges, and
    # test every edge against the proposed whole-block interval bags.
    last, edges = {}, []
    for i, read in enumerate(all_reads):
        if i:
            edges.append((i - 1, i, 'actual physical program order'))
        q = read['position']
        if q in last:
            edges.append((last[q], i, 'consecutive same physical cell'))
            assert all_reads[last[q]]['turn'] != read['turn']
        last[q] = i
    for i, j, kind in edges:
        A, B = blocks[all_reads[i]['block']], blocks[all_reads[j]['block']]
        assert max(A['sweep_interval'][0], B['sweep_interval'][0]) <= min(A['sweep_interval'][1], B['sweep_interval'][1])
        if kind == 'consecutive same physical cell':
            level = s(all_reads[i]['position'])
            assert all(A['sweep_interval'][0] <= level <= A['sweep_interval'][1] for A in (A, B))
    lo = min(b['sweep_interval'][0] for b in blocks)
    hi = max(b['sweep_interval'][1] for b in blocks)
    maximum = max(sum(b['RAW_or_prefix_read_count'] for b in blocks if b['sweep_interval'][0] <= level <= b['sweep_interval'][1]) for level in range(lo, hi + 1))
    assert maximum <= read_occurrence_bag_bound
    return dict(n=n, exact_tokens=tokens, complete_initial_black=sorted(seed),
                all_unlisted_initial_cells_WHITE=True, initial_mass=len(seed),
                all_physical_reads=tick_global, complete_final_black=sorted(black),
                complete_final_pose=(p[0], p[1], h),
                exact_maximum_read_bag=maximum, actual_constraint_edges=len(edges),
                no_old_U_contact_claimed=True)

controls = [concrete_control(n) for n in (1, 10, 100)]

# A precise obstruction to inferring a finite *geometry* state alphabet from
# a bounded number of tracks. It is deliberately not an ant color history.
X, Y = 'DDDDD', 'VVV'
xp, yp = path(''.join(W[a] for a in X))[2][:2], path(''.join(W[a] for a in Y))[2][:2]
assert xp == (5, 5) and yp == (3, 9)
assert s(xp) == s(yp) == 15
assert t(xp) == -5 and t(yp) == -15
coordinate_examples = []
for n, m in ((1, 1), (2, 2), (2, 1), (1, 2), (5, 5), (10, 9)):
    p1 = (n * xp[0] + m * yp[0], n * xp[1] + m * yp[1])
    p2 = (n * yp[0] + m * xp[0], n * yp[1] + m * xp[1])
    delta = sub(p1, p2)
    assert s(delta) == 0 and t(delta) == 10 * (n - m)
    assert (p1 == p2) == (n == m)
    coordinate_examples.append(dict(A_blocks=n, B_blocks=m, first_track_endpoint=p1,
        second_track_endpoint=p2, transverse_gap=t(delta), endpoint_coincidence=n == m))

paths = [R / 'one_foreign_first_contact_compression_2026-10-24/manifest.json',
         R / 'audits/check_one_foreign_contact_C_window_independent.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',
         R / 'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_BOUNDED_OLD_U_CONTACT_SWEEP_BAGS_PENDING_REVIEW',
    scope='Embedded actual old-U-to-first-contact window containing one FIRST foreign and total source-to-target-entry C count<=4. Exact bounded literal-constraint bags and chronology. No finite geometry quotient, arbitrary earlier D/C/V ancestry, or actual ant counterexample to such a quotient.',
    sweep_coordinate='s=2x+y', transverse_coordinate='t=x-2y',
    all16_actual_ordinary_sweep_drifts=drifts,
    all28_literal_RAW_fine_vertex_sweep_intervals=footprints,
    exact_radii=dict(ordinary=ordinary_radius, foreign=foreign_radius, final_actual_M11=marker_radius),
    uniform_bounds=dict(ordinary_heading_epochs=epoch_count_bound,
        ordinary_atoms_per_epoch_per_integer_level=heads_per_epoch,
        ordinary_atoms_per_bag=ordinary_atom_bag_bound,
        all_blocks_including_foreign_and_final_prefix=all_blocks_bound,
        literal_read_occurrences_per_bag=read_occurrence_bag_bound,
        read_constraint_graph_pathwidth_at_most=read_occurrence_bag_bound - 1),
    exact_graph_construction='One vertex per actual fine read. Program-order edges join consecutive physical reads; color edges join consecutive visits to the SAME physical cell. An atom block interval is the min/max s of all its fine vertices, including its actual exit. At sweep level l include ALL read vertices of every block whose interval contains l. Read vertices have connected bag intervals; both edge classes are covered.',
    chronological_order_rule='Epoch index determines interepoch chronology; within N/E epochs increasing s is forward, within S/W decreasing s is forward. Actual atom tick0 then fixes every fine read. Foreign and final-M11 blocks have their actual chronological slots. M11 is one actual future prefix, not replayed after every atom.',
    finite_color_part='Given a correct embedded/coincidence certificate, the active color/equality partition and read-order data have bounded finite size. Initial field bits, if prescribed, are supplied at their physical sites; unread archive is not recolored or deleted.',
    genuine_complete_finite_word_regressions=controls,
    geometric_finite_state_obstruction=dict(not_an_actual_ant_history=True,
        first_track_block_X=dict(tokens=list(X), displacement=xp, sweep=15, transverse=-5),
        second_track_block_Y=dict(tokens=list(Y), displacement=yp, sweep=15, transverse=-15),
        block_A='first track X, second track Y', block_B='first track Y, second track X',
        exact_gap_after_A_n_B_m='10*(n-m)', endpoint_coincidence_iff='n=m',
        finite_examples=coordinate_examples,
        nonregularity='A geometry verifier reading finite block labels A^n B^m and requiring endpoint coincidence would recognize {A^n B^n}. Its unbounded transverse gap is not determined by a bounded number of active tracks. This refutes the implication bounded bag cardinality -> finite geometry state, not a stronger ant-specific quotient.'),
    exact_remaining_obligation='Either retain boundedly many unbounded integer transverse-gap registers, or prove an additional genuine-U-history invariant allowing their finite quotient. The present result proves neither the quotient nor a physical countercontrol to it.',
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'sweep_frontier.json').write_text(json.dumps(out, indent=2) + '\n')
print('Exact sweep radii ordinary8/foreign14/finalM5; <=102 ordinary atoms,104 blocks,2941 actual reads per bag.')
print('All actual graph edges are covered in U,F,D^n finite controls n1/10/100. Geometry gap example is abstract, not an ant history.')
