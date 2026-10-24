"""Closed reverse interfaces of two retained actual DCV contact controls.

This is an exhaustive predecessor relation on three fixed literal suffixes,
not a trajectory-prefix search or an exclusion of their geometric gates.
"""
from pathlib import Path
from fractions import Fraction as Q
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
T10 = 'DCDCDCDV'       # full packets DC,DC,DC,D,V
T13 = 'DCDVCVCVCC'     # full packets DC,D,VC,VC,VCC

def add(p, q):
    return p[0] + q[0], p[1] + q[1]

def sub(p, q):
    return p[0] - q[0], p[1] - q[1]

def det(p, q):
    return p[0] * q[1] - p[1] * q[0]

def stream_owner(tokens, tick):
    lo = 0
    for i, a in enumerate(tokens):
        if tick < lo + len(W[a]):
            return dict(actual_atom_index0=i, actual_RAW_atom=a, actual_atom_start_tick0=lo,
                        canonical_physical_read=owner.describe(a, tick - lo))
        lo += len(W[a])
    return dict(actual_atom_index0=None, actual_RAW_atom='next actual word',
                next_word_tick0=tick - lo, next_word_read_number1=tick - lo + 1)

def raw(tokens):
    return ''.join(W[a] for a in tokens)

def direct_control(tokens):
    word = raw(tokens)
    context = lit.trace(word + lit.M)
    assert context['feasible']
    seed = {q for q, (turn, tick) in context['first'].items() if turn == 'L'}
    black = set(seed)
    p, h = (0, 0), 0
    raw_exit = None
    for tick, turn in enumerate(word + lit.M):
        assert (p in black) == (turn == 'L')
        if turn == 'L':
            black.remove(p)
        else:
            black.add(p)
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
        if tick + 1 == len(word):
            raw_exit = dict(position=p, heading=h, complete_black=sorted(black), mass=len(black))
    return dict(tokens=list(tokens), RAW_length=len(word), physical_reads_including_real_next_M11=len(word) + len(lit.M),
                initial_position=(0, 0), initial_heading=0, complete_initial_black=sorted(seed),
                all_unlisted_initial_cells_WHITE=True, initial_mass=len(seed),
                RAW_exit=raw_exit, actual_next_M11_exit=dict(position=p, heading=h,
                    complete_black=sorted(black), mass=len(black)))

positive = [direct_control(T10), direct_control('D' + T10), direct_control(T13)]
assert [r['initial_mass'] for r in positive] == [10, 10, 13]
assert [r['RAW_length'] for r in positive] == [103, 113, 149]
assert positive[0]['RAW_exit']['position'] == (2, -1)
assert positive[0]['RAW_exit']['heading'] == 1
assert positive[2]['RAW_exit']['position'] == (-1, 0)
assert positive[2]['RAW_exit']['heading'] == 3

nodes = [('T10', T10), ('D_T10', 'D' + T10), ('T13', T13)]
queries, edges = [], []
for name, suffix in nodes:
    for predecessor in 'DCVUFQB':
        tokens = predecessor + suffix
        tr = lit.trace(raw(tokens) + lit.M)
        row = dict(suffix_node=name, predecessor_RAW_atom=predecessor,
                   exact_tokens=list(tokens), feasible_on_some_complete_finite_board=tr['feasible'])
        if tr['feasible']:
            assert name == 'T10' and predecessor == 'D'
            edges.append(dict(from_suffix='T10', prepended_atom='D', to_suffix='D_T10'))
        else:
            assert tr['conflict_read'] < len(raw(tokens))
            row.update(immutable_conflict=tr,
                       earlier_actual_read_owner=stream_owner(tokens, tr['previous_read']),
                       later_actual_read_owner=stream_owner(tokens, tr['conflict_read']))
            assert row['earlier_actual_read_owner']['canonical_physical_read']['turn'] == tr['turn']
            assert row['later_actual_read_owner']['canonical_physical_read']['turn'] == tr['turn']
        queries.append(row)
assert len(queries) == 21 and len(edges) == 1
assert {(r['suffix_node'], r['predecessor_RAW_atom']) for r in queries if r['feasible_on_some_complete_finite_board']} == {('T10', 'D')}
assert len({(r['suffix_node'], r['predecessor_RAW_atom']) for r in queries}) == 21

paths = [R / 'core_periodicity_new/center_crossing_control_frozen_20261023_1407/manifest.json',
         R / 'core_periodicity_new/four_C_contact_gate_frozen_20261023_1455/manifest.json',
         R / 'audits/check_four_C_contact_independent.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',
         R / 'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json']
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_FIXED_DCV_CONTACT_REVERSE_INTERFACES_PENDING_REVIEW',
    scope='Only the two exact retained fixed DCV contact words and their exact seven-atom predecessor closure. Positive complete finite boards remain real. Their broader geometric gates, different histories and arbitrary ordinary-tail simplicity remain OPEN.',
    retained_control_words=dict(T10=list(T10), T13=list(T13)),
    three_actual_complete_finite_board_positive_replays=positive,
    all21_exact_predecessor_queries=queries,
    closed_reverse_relation_edges=edges,
    exact_terminal_nodes=['D_T10', 'T13'],
    arbitrary_prefix_argument='Any nonempty seven-atom left context has a last atom. T10 permits only lastD, giving D_T10, which has NO preceding seven atom. T13 has NO preceding seven atom immediately. The finite reverse relation is closed, not stopped at an arbitrary depth.',
    no_U_entry_first_foreign_lift_of_these_fixed_words=True,
    no_geometric_gate_exclusion=True,
    scope_warning='A different physical word through either geometric contact can have other predecessors. An actual ant can also approach through a return word OUTSIDE these seven atoms. Neither possibility is excluded.',
    source_reconciliation='Closed-head four-C rectangle attempts are already excluded by signed atomic1344; no new theorem is claimed from those failures. The retained10/13 controls are center contacts, not exact four-C pose returns.',
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'fixed_contact_control_predecessors.json').write_text(json.dumps(out, indent=2) + '\n')
print('Three actual complete positive boards:10/10/13 blacks,103/113/149 RAW reads.')
print('Exact21-query reverse closure: T10 <-D- D_T10, then no parent; T13 has no parent. No arbitrary depth cap.')
