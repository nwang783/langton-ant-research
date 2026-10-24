"""Separate extension of the signed D/V rail guard to plain D/V/U rails.

All S origins are regenerated. In particular V(0,1) no longer uses the
old D/V-only first-entry shortcut when U steps are admitted.
"""
from pathlib import Path
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
G = (-1, 0)

def add(p, q): return p[0] + q[0], p[1] + q[1]
def sub(p, q): return p[0] - q[0], p[1] - q[1]
def raw(tokens): return ''.join(W[a] for a in tokens)
def after(word, pose=(0, 0, 0)):
    p, h = pose[:2], pose[2]
    for turn in word:
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
    return (*p, h)

geom = {a: lit.literal_geometry(W[a]) for a in 'DVU'}
assert sum(len(g['outputs']) for g in geom.values()) == 16
source = lit.trace(raw('UCC'))
assert source['pose'] == (-1, 5, 2) and source['last'][G] == ('L', 1)
short_guards = {T: lit.trace(raw(T) + lit.M) for T in ('UCCU', 'UCCVU')}
assert not short_guards['UCCU']['feasible']
assert (short_guards['UCCU']['conflict_read'], short_guards['UCCU']['previous_read']) == (70, 30)
assert not short_guards['UCCVU']['feasible']
assert (short_guards['UCCVU']['conflict_read'], short_guards['UCCVU']['previous_read']) == (89, 1)
assert short_guards['UCCVU']['cell'] == list(G)

south, north = [], []
for atom in 'DVU':
    g = geom[atom]
    dy = g['endpoint'][1]
    for ox, oy in g['outputs']:
        # Every S-rail head is(-1-d-v,5-d-3v-4u). An O source of G
        # must start at G+o, hence d+v=-ox; this bounds the candidate
        # prefix counts exactly, not the whole rail length.
        head = (G[0] + ox, G[1] + oy)
        if ox > 0:
            classification = 'requires_head_right_of_all_S_rail_heads'
            solutions = []
        else:
            assert ox in (-1, 0)
            solutions = []
            for d in range(-ox + 1):
                v = -ox - d
                rem = 5 - d - 3 * v - head[1]
                if rem >= 0 and rem % 4 == 0:
                    solutions.append(dict(d=d, v=v, u=rem // 4))
            if not solutions:
                classification = 'no_nonnegative_prefix_count_solution'
            elif solutions == [dict(d=0, v=0, u=1)]:
                classification = 'unique_prefix_U_contains_forbidden_UCCU'
            else:
                assert atom == 'U' and (ox, oy) == (-1, 2)
                assert solutions == [dict(d=0, v=1, u=0)]
                classification = 'unique_prefix_V_contains_forbidden_UCCVU'
        south.append(dict(full_plain_source=atom, fresh_O_slot=(ox, oy),
            required_S_entry=head, all_possible_prior_rail_count_solutions=solutions,
            exclusion=classification))
        nhead = (G[0] - ox, G[1] - oy)
        end = after(W[atom], (*nhead, 0))
        assert dy - oy >= 1 and end[1] >= 1
        north.append(dict(full_plain_source=atom, fresh_O_slot=(ox, oy),
            required_N_entry=nhead, genuine_full_exit=end,
            exit_Y_minus_target_Y=end[1] + 2))
assert len(south) == len(north) == 16
assert Counter(r['exclusion'] for r in south) == {
    'requires_head_right_of_all_S_rail_heads': 11,
    'no_nonnegative_prefix_count_solution': 2,
    'unique_prefix_U_contains_forbidden_UCCU': 2,
    'unique_prefix_V_contains_forbidden_UCCVU': 1}

def physical_prefix_control(X, Y):
    dX, vX, uX = (X.count(a) for a in 'DVU')
    dY, vY, uY = (Y.count(a) for a in 'DVU')
    delta_u = uY - uX
    assert dY - dX == 2 * delta_u
    assert vY - vX == -3 - 2 * delta_u
    dropX, dropY = dX + 3 * vX + 4 * uX, dY + 3 * vY + 4 * uY
    assert dropX == dropY + 9 and dropX >= 9
    tokens = 'UCC' + X + 'F' + Y
    body = raw(tokens)
    assert after(body) == (0, -2, 0)
    partial = body + W['U'][:13]
    tr = lit.trace(partial)
    assert tr['feasible']
    seed = {p for p, (turn, tick) in tr['first'].items() if turn == 'L'}
    black = set(seed); p, h = (0, 0), 0
    for turn in partial:
        assert (p in black) == (turn == 'L')
        if turn == 'L': black.remove(p)
        else: black.add(p)
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
    assert p == G and h == 3 and G not in black
    full = lit.trace(body + W['U'] + lit.M)
    assert not full['feasible']
    assert full['previous_read'] == 1 and full['conflict_read'] == len(body) + 13
    actual_prefix = W['U'][:13] + 'R'
    seven_mismatches = {a: next(i for i in range(14) if (W[a] + lit.M)[i] != actual_prefix[i])
                        for a in 'DCVUFQB'}
    return dict(X=X, Y=Y, delta_U_count=delta_u,
        exact_tokens_before_target=list(tokens), complete_initial_black=sorted(seed),
        all_unlisted_initial_cells_WHITE=True, successful_actual_reads=len(partial),
        source_g_L1_remains_deleted=True, actual_next_pose=(p[0], p[1], h),
        actual_next_turn='R', attempted_target_U_L13_conflict=full,
        all_seven_impossible_by_current_actual_prefix=seven_mismatches,
        no_completed_U_or_proxy_contact_claimed=True)

controls = [physical_prefix_control(X, Y) for X, Y in [
    ('VVVU', 'U'), ('VVVUV', 'VU'), ('VVVVUU', 'VUU'),
    ('VVVVV', 'DDU'), ('VVDDU', 'V')]]
assert {r['delta_U_count'] for r in controls} == {-1, 0, 1}

# The affine endpoint identity is verified coefficientwise: sourceUCC plus
# F gives(3,7,N); X contributes negative standard drifts, Y positive.
unit = {'D': (1, 1), 'V': (1, 3), 'U': (0, 4)}
assert all(after(W[a])[:2] == d for a, d in unit.items())
assert after(W['F'], (-1, 5, 2)) == (3, 7, 0)
assert min(p[1] for p in lit.trace(W['F'])['first']) == -2

paths = [H / 'manifest.json', R / 'audits/check_two_track_UCC_F_guard_independent.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',
         R / 'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_TWO_TRACK_PLAIN_DVU_EXTENSION_PENDING_REVIEW',
    scope='Exact named template UCC,X_S,F,Y_N,attemptedU(0,-2,N), now arbitrary plain D/V/U rails. Two unbounded tracks, fixed source and connector. No rail C, other foreign, other target, or arbitrary-tail simplicity.',
    frozen_DV_result_unchanged=True,
    all_plain_full_geometries=geom,
    two_exact_immutable_short_prefix_guards=short_guards,
    all16_regenerated_S_residual_origin_rows=south,
    all16_N_residual_origins_exit_too_high=north,
    all_order_endpoint_identities=dict(
        target='(3-dX-vX+dY+vY,7-dX-3vX-4uX+dY+3vY+4uY,N)',
        endpoint_required='(0,-2,N)', equivalent='deltaD=2deltaU;deltaV=-3-2deltaU',
        source_rail_drop='dropX=9+dropY>=9',
        FOREIGN_g_local='(-dX-vX,5-dropX),y<=-4 below F RAWminY=-2',
        FOREIGN_exit_relative_g_Y='dropX-7>=2, outside N exitK'),
    source_hole='G=(-1,0), actual creatingU L1/read2, preserved by ownCC and outside fullO/exitK. First possible later current BLACK must be a genuine later completed full O; core export is not omitted.',
    generalized_V_origin_warning='V output(0,1) no longer forces first-entry y5 when U steps are allowed. Its unique prefix is U and is separately excluded by literal UCCU. The old DV-only shortcut is NOT reused.',
    actual_complete_finite_prefix_controls_with_rail_U=controls,
    conclusion='All-length/all-order named plain-DVU two-track language is empty through the attempted final U RAW: its input G at local(-1,2),actualU13/read14 must beBLACK but has no valid completed residual origin. Actual positive partial prefixes forceR and leave the seven-atom language at that marker.',
    no_postforeign_age_or_general_geometry_DFA=True,
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'plain_rail_extension.json').write_text(json.dumps(out, indent=2) + '\n')
print('All16 S origins regenerated:11 right-cone+2 arithmetic+2 UCCU+1 UCCVU; all16 N exits exceed targetY.')
print('Plain D/V/U endpoint balance gives dropX>=9, F misses hole. Five actual finite prefixes cover deltaU=-1/0/+1; finalU is not attained.')
