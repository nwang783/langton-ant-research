"""All-length, all-order D/V rails in one explicit two-track old-U window.

Template UCC, X_S, F, Y_N, U(0,-2,N), with X/Y arbitrary plain D/V.
Exact endpoint equations and actual full-output/core ledgers exclude it.
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
G = (-1, 0)

def add(p, q):
    return p[0] + q[0], p[1] + q[1]

def sub(p, q):
    return p[0] - q[0], p[1] - q[1]

def after(word, pose=(0, 0, 0)):
    p, h = pose[:2], pose[2]
    for turn in word:
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
    return (*p, h)

source_word = W['U'] + 2 * W['C']
source = lit.trace(source_word)
assert source['feasible'] and source['pose'] == (-1, 5, 2)
assert source['first'][G] == source['last'][G] == ('L', 1)
source_geo = lit.literal_geometry(source_word)
source_exit_K = {add((-1, 5), lit.rot(q, 2)) for q in lit.K}
assert G not in source_exit_K and list(G) not in source_geo['outputs']

geometry = {a: lit.literal_geometry(W[a]) for a in 'DVF'}
assert geometry['D']['outputs'] == [[2, 0]]
assert geometry['V']['outputs'] == [[0, 0], [0, 1], [1, 0], [2, 0], [2, 1], [2, 2]]
assert geometry['D']['endpoint'] == [1, 1, 0]
assert geometry['V']['endpoint'] == [1, 3, 0]
assert geometry['F']['endpoint'] == [-4, -2, 2]
assert min(q[1] for q in lit.trace(W['F'])['first']) == -2

# S entries along X have x=-1-dprefix-vprefix <=-1. A new residual
# output at G requires entry G+o. For V, the only possibilities at x<=-1
# have o.x=0 and hence x=-1, forcing an EMPTY preceding prefix; their
# required y0/1 disagrees with the actual first head y5.
south_origins = []
for a in 'DV':
    for ox, oy in geometry[a]['outputs']:
        p = (G[0] + ox, G[1] + oy)
        if p[0] > -1:
            reason = 'strictly_right_of_all_S_rail_heads'
        else:
            assert p[0] == -1 and ox == 0 and oy in (0, 1)
            assert p[1] != 5
            reason = 'x_equal_minus1_forces_first_rail_entry_y5_not_required_y0_or1'
        south_origins.append(dict(full_plain_source=a, fresh_output_slot=[ox, oy],
                                  required_S_entry=p, exclusion=reason))
assert len(south_origins) == 7

# N entries in Y producing G through a true O must complete at y>=1.
# Every remaining N D/V atom has positive y drift, whereas the final U
# entry is at y=-2. This retains the full completion cut, not a RAW/core
# write mistakenly treated as an external residual producer.
north_origins = []
for a in 'DV':
    dy = geometry[a]['endpoint'][1]
    for ox, oy in geometry[a]['outputs']:
        p = (G[0] - ox, G[1] - oy)
        end = after(W[a], (*p, 0))
        assert end[1] >= 1
        north_origins.append(dict(full_plain_source=a, fresh_output_slot=[ox, oy],
                                  required_N_entry=p, actual_full_exit=end,
                                  cannot_reach_final_target_y=-2))
assert len(north_origins) == 7

target = lit.trace(W['U'] + lit.M)
assert target['first'][(-1, 2)] == ('L', 13)
assert (-1, 2) not in lit.K
assert add((0, -2), (-1, 2)) == G

def prefix_control(X, Y):
    dx, vx = X.count('D'), X.count('V')
    dy, vy = Y.count('D'), Y.count('V')
    assert dx == dy and vx == vy + 3 and vx >= 3
    tokens = 'UCC' + X + 'F' + Y
    raw = ''.join(W[a] for a in tokens)
    assert after(raw) == (0, -2, 0)
    partial = raw + W['U'][:13]
    tr = lit.trace(partial)
    assert tr['feasible']
    seed = {q for q, (turn, tick) in tr['first'].items() if turn == 'L'}
    black = set(seed)
    p, h = (0, 0), 0
    for turn in partial:
        assert (p in black) == (turn == 'L')
        if turn == 'L':
            black.remove(p)
        else:
            black.add(p)
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
    assert p == G and h == 3 and G not in black
    full = lit.trace(raw + W['U'] + lit.M)
    assert not full['feasible'] and full['conflict_read'] == len(raw) + 13
    assert full['previous_read'] == 1 and full['cell'] == list(G) and full['turn'] == 'L'
    actual_new_marker_prefix = W['U'][:13] + 'R'
    # At this new marker, none of the seven atoms can be completed. D's
    # short RAW needs its actual next marker, so compare RAW+M11, not bareD.
    rejections = {}
    for a in 'DCVUFQB':
        c = W[a] + lit.M
        mismatch = next(i for i in range(len(actual_new_marker_prefix)) if c[i] != actual_new_marker_prefix[i])
        assert mismatch <= 13
        rejections[a] = mismatch
    return dict(X=X, Y=Y, exact_tokens_before_target=list(tokens),
                complete_initial_black=sorted(seed), all_unlisted_initial_cells_WHITE=True,
                initial_mass=len(seed), all_successful_physical_reads=len(partial),
                successful_prefix_RAWs_complete=True,
                target_U_successful_RAW_ticks0=[0, 12],
                actual_next_read_pose=(p[0], p[1], h), actual_next_cell_WHITE=True,
                intended_U13_L_conflict=full,
                intended_read_owner=owner.describe('U', 13),
                actual_next_turn='R',
                all7_impossible_at_current_marker_by_actual_prefix=rejections,
                no_completed_target_U_or_proxy_contact_claimed=True)

controls = [prefix_control(X, Y) for X, Y in [
    ('VVV', ''), ('VVVV', 'V'), ('V' * 10, 'V' * 7),
    ('VDVV', 'D'), ('VVDVV', 'DV')]]

# Exact endpoint algebra. For arbitrary X/Y ordering, only their counts
# enter these identities; no word-count cap is used in the proof.
endpoint_checks = []
for d in range(4):
    for v in range(3, 7):
        pF = (-1 - d - v, 5 - d - 3 * v, 2)
        Fend = after(W['F'], pF)
        target_head = (Fend[0] + d + (v - 3), Fend[1] + d + 3 * (v - 3), 0)
        assert target_head == (0, -2, 0)
        pulled = lit.rot(sub(G, pF[:2]), 2)
        assert pulled == (-d - v, 5 - d - 3 * v)
        assert pulled[1] <= -4
        assert pulled not in lit.trace(W['F'])['first']
        local_exit = sub(G, Fend[:2])
        assert local_exit == (d + v - 4, d + 3 * v - 7)
        assert local_exit[1] >= 2 and local_exit not in lit.K
        endpoint_checks.append(dict(dX=d, vX=v, dY=d, vY=v - 3,
            actual_foreign_entry=pF, actual_foreign_exit=Fend,
            G_in_FOREIGN_entry_frame=pulled, G_relative_FOREIGN_exit=local_exit))

paths = [R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',
         R / 'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json',
         R / 'old_U_contact_sweep_frontier_2026-10-24/manifest.json',
         R / 'one_foreign_first_contact_compression_2026-10-24/manifest.json']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_ALL_ORDER_TWO_TRACK_DV_CORE_GUARD_PENDING_REVIEW',
    scope='Only UCC, X_S, F, Y_N, attempted U(0,-2,N), with X,Y arbitrary finite plain D/V words, correct actual endpoint and final context. No other foreign, rail U, C connector, old source, or arbitrary-tail simplicity conclusion.',
    actual_source_g_deletion=dict(cell=G, last_source_UCC_read_tick0=1,
        owner=owner.describe('UCC', 1), source_full_exit=(-1, 5, 2),
        absent_from_source_full_O_and_exit_K=True),
    exact_plain_full_geometries=geometry,
    all7_S_rail_residual_birth_origins_excluded=south_origins,
    all7_N_rail_residual_birth_origins_too_far_north=north_origins,
    all_length_endpoint_identities=dict(
        foreign_entry='(-1-dX-vX,5-dX-3vX,S)',
        target_entry='(3-dX-vX+dY+vY,7-dX-3vX+dY+3vY,N)',
        forced_target='(0,-2,N)', equivalent_count_constraints='dY=dX, vY=vX-3, vX>=3',
        two_unbounded_tracks='S and N; fixed UCC source and F connector; one residual transverse endpoint relation after sweep synchronization'),
    exact_FOREIGN_hole_miss_inequality='G local to F is(-dX-vX,5-dX-3vX), whose y<=-4; actual F RAW min local y=-2. It is outside entryK and exitK; G exit-relative y=dX+3vX-7>=2.',
    residual_to_physical_interface='After source deletion and absence of later full O at G, G cannot be BLACK outside the actual current K. A core-to-residual export must itself be a genuine later full O with its actual last R. At Fentry and targetUentry G is outside K. No physical-WHITE permanence at intermediate cores is asserted.',
    final_actual_U_requirement=dict(cell=G, target_local_input=(-1, 2),
        first_required_BLACK_owner=owner.describe('U', 13)),
    genuine_complete_finite_prefix_controls=controls,
    pure_V_all_n_specialization='X=V^n,Y=V^(n-3),n>=3; intended U first fails at global36n+73 against sourceL1 on G. Samples are not the all-n proof; the count/last-full-output argument covers every n and all D/V orders.',
    conclusion='No complete finite board realizes this all-length two-track template through target U RAW. Five actual partial-prefix controls instead force R at its tick13 and thereby leave the seven-atom language at that attempted marker.',
    no_full_target_U_or_actual_proxy_contact_countercontrol=True,
    no_postforeign_maturity=True,
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'DV_rail_core_guard.json').write_text(json.dumps(out, indent=2) + '\n')
print('All-order endpoint constraints dY=dX,vY=vX-3; seven S births absent, seven N births exit too high, F misses deleted G.')
print('Five genuine complete finite partial-prefix controls reach WHITE G; attempted U13L fails and actual R excludes every seven-atom continuation at that marker.')
