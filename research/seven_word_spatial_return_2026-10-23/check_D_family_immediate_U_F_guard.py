"""A narrow actual predecessor cut, without an exterior-path assumption.

The only new ancestry claim is that an immediately preceding plain U cannot
fund either F target at C age three.  Generic U/UC ancestry remains open.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
R = Path('/workspace/shared/langton')
H = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('lit', R/'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(sp); sp.loader.exec_module(lit)
so = importlib.util.spec_from_file_location('owner', R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner = importlib.util.module_from_spec(so); so.loader.exec_module(owner)
GP = R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G = json.loads(GP.read_text())['geometry']
KEEP = (0, 1, 4, 5, 6, 7, 8, 9)

def add(p, q): return p[0]+q[0], p[1]+q[1]

def inverse_predecessor(g):
    end = g['endpoint']; h = (-end[2]) % 4
    q = lit.rot(end[:2], h)
    return (-q[0], -q[1], h)

adjacency = []
for p in KEEP:
    for d in (0, 1):
        tr = lit.trace(G[p]['word'] + G[d]['word'] + lit.M)
        row = dict(predecessor=G[p]['name'], next_source=G[d]['name'],
                   predecessor_pose_in_next_source_frame=inverse_predecessor(G[p]),
                   complete_actual_pair_feasible=tr['feasible'])
        if not tr['feasible']:
            assert p in (6, 9)
            # In the following source's own frame, its specified D input is
            # read at context tick11: own C-tail tick1, or next RAW tick1.
            off = tr['conflict_read'] - len(G[p]['word'])
            assert off == 11
            row.update(immutable_conflict=tr,
                       physical_read_ownership=owner.describe(G[d]['name'], off))
            assert row['physical_read_ownership']['owner_tick0'] == 1
            assert row['physical_read_ownership']['owner_read_number1'] == 2
        else:
            assert p not in (6, 9)
        adjacency.append(row)
assert len(adjacency) == 16

u_pose = inverse_predecessor(G[7]); assert u_pose == (0, -4, 0)
# Both are genuine last-R U output identities and belong to the original
# directed cycle. The signed exact-renewal theorem keeps every cycle ID
# current until its first break at source-entry age four.
u_raw = lit.trace(G[7]['word'])
cycle_cells = ((2, 0), (2, 1))
for q in cycle_cells:
    assert list(q) in G[7]['outputs']
    assert u_raw['last'][q][0] == 'R'
physical_cycle = [add(u_pose[:2], q) for q in cycle_cells]
assert physical_cycle == [(2, -4), (2, -3)]

cases = []
for case, source, foreign_pose, returned in (
    (15, 'D',  (2, -5, 1), ('C', (0, -1, 3))),
    (15, 'DC', (2, -5, 1), ('C', (0, -1, 3))),
    (30, 'D',  (3, -4, 1), ('V', (1, 0, 3))),
    (30, 'DC', (3, -4, 1), ('V', (1, 0, 3))),
    (75, 'DC', (3, -4, 1), ('C', (1, 0, 3))),
):
    core = {add(foreign_pose[:2], lit.rot(q, foreign_pose[2])) for q in lit.K}
    hit = sorted(set(physical_cycle) & core)
    assert hit
    raw = lit.trace(owner.WORDS['F'])
    owned = []
    for physical in hit:
        rel = (physical[0]-foreign_pose[0], physical[1]-foreign_pose[1])
        local = lit.rot(rel, -foreign_pose[2])
        assert local in lit.K
        c, tick = raw['first'][local]
        assert c == 'L' and tick < len(owner.WORDS['F'])
        owned.append(dict(physical_cell=physical, F_local_cell=local,
                          actual_first_read=(c, tick),
                          physical_read_ownership=owner.describe('F', tick)))
    cases.append(dict(catalogue_id=case, actual_selected_full_source=source,
                      source_entry=(0, 0, 0), immediately_previous_full_packet='U',
                      previous_U_entry=u_pose, foreign='F', foreign_entry=foreign_pose,
                      returned_atom=returned,
                      actual_U_entry_to_F_entry_C_age=3,
                      first_U_cycle_break_C_age=4,
                      original_U_east_cycle_IDs_current_before_F=True,
                      residual_cycle_IDs_in_actual_F_entry_core=owned,
                      contradiction='A current residual identity cannot lie in the actual entry K core.'))
assert len(cases) == 5

# These are useful negative-scope controls: Q/B do not share this core hit.
compatible_cores = []
for a, pose in (('Q', (5, -4, 1)), ('B', (6, -3, 1))):
    K = {add(pose[:2], lit.rot(q, pose[2])) for q in lit.K}
    assert not (set(physical_cycle) & K)
    compatible_cores.append(dict(foreign=a, foreign_entry_in_D_frame=pose,
                                 old_east_cycle_core_hit=False,
                                 ancestry_status='OPEN; absence of this obstruction is not attainment.'))

# DC does not supply a fresh birth for this required BLACK input: it can be
# an older surviving residual identity. Record, rather than erase, that port.
beta = (1, -1)
dc = lit.trace(G[1]['word']); assert beta not in dc['first']
for a, pose in (('F', (3, -4, 1)), ('Q', (5, -4, 1)), ('B', (6, -3, 1))):
    rel = (beta[0]-pose[0], beta[1]-pose[1]); local = lit.rot(rel, -pose[2])
    raw = lit.trace(owner.WORDS[a]); full = lit.trace(owner.WORDS[a]+owner.WORDS['C']+lit.M)
    assert local not in raw['first']
    assert full['first'][local] == ('L', len(owner.WORDS[a])+1)

DP = R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json'
deps = [GP, DP,
        R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',
        H/'first_returned_five_label_frontier_manifest.json',
        R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out = dict(status='AUTHOR_FROZEN_NARROW_PREDECESSOR_GUARD_PENDING_REVIEW',
           scope='Actual U-entry eight history before its first foreign, at the five remaining first-returned-contact targets. This excludes only an immediately preceding plain U for the two F target poses, not generic earlier U ancestry, UC predecessors, Q/B targets, or returned-path contact.',
           all16_exact_D_family_predecessor_pairs=adjacency,
           five_immediate_plain_U_before_D_family_F_exclusions=cases,
           Q_B_plain_U_predecessor_core_controls=compatible_cores,
           retained_old_beta_port=dict(physical_cell_in_D_frame=beta,
                                      DC_RAW_never_reads=True,
                                      foreign_RAW_never_reads=True,
                                      returned_C_input_tick0=1,
                                      returned_C_input_read_number1=2,
                                      possible_origin='Older surviving entry identity; no forced rebirth follows.'),
           dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps})
(H/'D_family_immediate_U_F_guard.json').write_text(json.dumps(out, indent=2)+'\n')
print('16 exact predecessor pairs; five narrow immediate-U/F core exclusions; Q/B and older beta retained.')
