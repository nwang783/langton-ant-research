"""Exact F/Q/B covariance of the signed plain-D/V/U two-track hole guard."""
from pathlib import Path
from collections import Counter
import importlib.util
import hashlib
import json

ROOT = Path('/workspace/shared/langton')
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lit', ROOT / 'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)
spec = importlib.util.spec_from_file_location('owner', ROOT / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(owner)
WORDS = owner.WORDS
G = (-1, 0)


def raw(tokens):
    return ''.join(WORDS[a] for a in tokens)


def advance(word, pose=(0, 0, 0)):
    x, y, h = pose
    for turn in word:
        h = (h + (1 if turn == 'R' else -1)) % 4
        dx, dy = lit.DIRS[h]
        x, y = x + dx, y + dy
    return x, y, h


def control(foreign, xrail, yrail):
    body_tokens = 'UCC' + xrail + foreign + yrail
    body = raw(body_tokens)
    assert advance(body) == (0, -2, 0)
    actual = body + WORDS['U'][:13]
    tr = lit.trace(actual)
    assert tr['feasible']
    seed = {p for p, (turn, tick) in tr['first'].items() if turn == 'L'}
    black = set(seed)
    x, y, h = 0, 0, 0
    for turn in actual:
        assert ((x, y) in black) == (turn == 'L')
        if turn == 'L':
            black.remove((x, y))
        else:
            black.add((x, y))
        h = (h + (1 if turn == 'R' else -1)) % 4
        dx, dy = lit.DIRS[h]
        x, y = x + dx, y + dy
    assert (x, y) == G and h == 3 and G not in black
    bad = lit.trace(body + WORDS['U'] + lit.M)
    assert not bad['feasible']
    assert bad['cell'] == list(G)
    assert bad['previous_read'] == 1 and bad['conflict_read'] == len(body) + 13
    actual_prefix = WORDS['U'][:13] + 'R'
    mismatch = {
        a: next(t for t in range(14) if (WORDS[a] + lit.M)[t] != actual_prefix[t])
        for a in 'DCVUFQB'
    }
    return dict(
        foreign=foreign, S_rail=xrail, N_rail=yrail,
        exact_tokens_before_target=list(body_tokens),
        complete_initial_BLACK=sorted(seed), all_unlisted_initial_cells_WHITE=True,
        successful_actual_reads=len(actual), actual_next_pose=(x, y, h),
        actual_next_turn='R', attempted_U_requires_L_at_tick0=13,
        exact_conflict=bad, all_seven_current_marker_mismatch_ticks0=mismatch,
        completed_target_or_contact_claimed=False)


source = lit.trace(raw('UCC'))
assert source['pose'] == (-1, 5, 2)
assert source['last'][G] == ('L', 1)
extension = json.loads((HERE / 'plain_rail_extension.json').read_text())
assert len(extension['all16_regenerated_S_residual_origin_rows']) == 16
assert len(extension['all16_N_residual_origins_exit_too_high']) == 16

foreign_rows = []
for foreign, a, b, cd, cv in [('F', 4, 2, 0, -3), ('Q', 4, 4, 1, -4), ('B', 3, 5, 3, -5)]:
    trace = lit.trace(WORDS[foreign])
    assert trace['pose'] == (-a, -b, 2)
    raw_min_y = min(p[1] for p in trace['first'])
    assert raw_min_y == -b
    # DeltaD = cd + 2*DeltaU; DeltaV = cv - 2*DeltaU.
    assert cd + cv == 1 - a
    assert cd + 3 * cv == -7 - b
    assert advance(WORDS[foreign], (-1, 5, 2)) == (a - 1, b + 5, 0)
    foreign_rows.append(dict(
        foreign=foreign, actual_RAW_endpoint=(-a, -b, 2), actual_RAW_min_y=raw_min_y,
        endpoint_required=(0, -2, 0),
        delta_D_constant=cd, delta_D_delta_U_coefficient=2,
        delta_V_constant=cv, delta_V_delta_U_coefficient=-2,
        drop_X_equals_drop_Y_plus=7 + b,
        source_hole_local_to_foreign='(-dX-vX, 5-dropX)',
        maximum_possible_hole_local_y=-2-b,
        strict_RAW_miss_margin=2,
        hole_relative_to_actual_N_exit_core_y='dropX-b-5 = dropY+2 >= 2',
        source_hole_outside_actual_exit_K=True,
        same_sixteen_S_and_N_origin_exclusions_as_signed_extension=True))

controls = [
    control('F', 'VVVU', 'U'),
    control('Q', 'VVVV', 'D'),
    control('Q', 'VVVVU', 'DU'),
    control('B', 'VVVVVU', 'DDDU')]
assert Counter(c['foreign'] for c in controls) == {'F': 1, 'Q': 2, 'B': 1}

dependencies = [
    HERE / 'plain_rail_extension_manifest.json',
    ROOT / 'audits/check_two_track_plain_DVU_independent.json',
    ROOT / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in dependencies)
out = dict(
    status='AUTHOR_FROZEN_FOREIGN_COVARIANCE_PENDING_REVIEW',
    scope='Only UCC, X_S, A, Y_N, attempted U(0,-2,N), where A is exactly one F/Q/B and X,Y are arbitrary finite plain D/V/U rails. No additional C or foreign, no other target.',
    signed_S_N_hole_proof_unchanged=True,
    all_three_literal_foreign_covariance_rows=foreign_rows,
    actual_complete_finite_partial_prefix_controls=controls,
    proof='The signed source deletion and all sixteen S/N full-O origin exclusions are independent of A. Endpoint identities force g below every actual foreign RAW read and outside its actual exit K. Hence no valid later full-O, including core export, supplies g before the attempted U input at tick13/read14.',
    actual_next_read_for_controls='R on WHITE g, not required L; no seven-atom continuation from that marker.',
    no_completed_target_or_proxy_contact_counterexample=True,
    no_postforeign_maturity_or_general_DFA=True,
    dependencies={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies})
(HERE / 'foreign_covariance.json').write_text(json.dumps(out, indent=2) + '\n')
print('All three literal foreign words miss the source hole by margin two; exact endpoint identities preserve the signed S/N origin proof.')
print('Four complete finite partial prefixes replay. Each attempted final U fails at actual RAW tick13/read14 on the original source hole.')
