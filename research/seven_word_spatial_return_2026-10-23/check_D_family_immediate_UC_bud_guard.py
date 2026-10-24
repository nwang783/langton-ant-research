"""Immediate-UC birth-history guard; no maturity law is used after foreign.

The physical before-WHITE contradiction keeps its exact continuation owner.
An old BLACK beta port is not silently reset to a fresh source output.
"""
from pathlib import Path
from collections import Counter
import hashlib
import importlib.util
import json
R = Path('/workspace/shared/langton'); H = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('lit', R/'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(sp); sp.loader.exec_module(lit)
so = importlib.util.spec_from_file_location('owner', R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner = importlib.util.module_from_spec(so); so.loader.exec_module(owner)
GP = R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
CP = R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
G = json.loads(GP.read_text())['geometry']; KEEP = (0, 1, 4, 5, 6, 7, 8, 9)
COUNT = {tuple(map(int, line.split()[:8])) for line in CP.read_text().splitlines()}

def add(p, q): return p[0]+q[0], p[1]+q[1]

def inverse_predecessor(g):
    end = g['endpoint']; h = (-end[2]) % 4; p = lit.rot(end[:2], h)
    return (-p[0], -p[1], h)

uc_pose = inverse_predecessor(G[8]); assert uc_pose == (-5, 0, 1)
local_bud = (1, 3); bud = add(uc_pose[:2], lit.rot(local_bud, uc_pose[2]))
assert bud == (-2, -1)
u = lit.trace(G[7]['word']); uc = lit.trace(G[8]['word'])
assert list(local_bud) in G[8]['outputs']
assert u['last'][local_bud][0] == 'R'
assert uc['last'][local_bud] == u['last'][local_bud]

queries = []
for age in range(5):
    h = (-age) % 4
    for cid in KEEP:
        for inp in map(tuple, G[cid]['inputs']):
            z = lit.rot(inp, h); p = (local_bud[0]-z[0], local_bud[1]-z[1])
            key = (KEEP.index(8), KEEP.index(cid), *p, h, *local_bud, age)
            reason = 'sector' if (sum(p)+h) % 2 else 'signed_COUNT5'
            if reason == 'signed_COUNT5': assert key in COUNT
            queries.append(dict(actual_full_source='UC', source_output=local_bud,
                                consumer=G[cid]['name'], actual_input=inp,
                                consumer_pose_in_UC_frame=(*p, h),
                                full_source_entry_C_age=age, exclusion=reason,
                                exact_COUNT5_key=key))
assert len(queries) == 115

cases = []
for case, source, foreign, pose in (
    (15, 'D', 'F', (2, -5, 1)),
    (15, 'DC', 'F', (2, -5, 1)),
    (75, 'DC', 'F', (3, -4, 1)),
    (76, 'DC', 'Q', (5, -4, 1)),
    (77, 'DC', 'B', (6, -3, 1)),
):
    tr = lit.trace(owner.WORDS[foreign]+owner.WORDS['C']+lit.M)
    assert tr['feasible']
    rel = (bud[0]-pose[0], bud[1]-pose[1]); local = lit.rot(rel, -pose[2])
    raw = lit.trace(owner.WORDS[foreign]); assert local not in raw['first']
    turn, tick = tr['first'][local]; assert turn == 'R'
    physical_owner = owner.describe(foreign+'C', tick)
    assert physical_owner['turn'] == 'R'
    # UC's own C adds exactly one before the selected D-family entry.
    selected_source_clock = 1
    foreign_clock = selected_source_clock+3
    assert foreign_clock == 4
    cases.append(dict(catalogue_id=case, selected_actual_full_source=source,
                      selected_source_entry=(0, 0, 0), immediately_previous_full_packet='UC',
                      UC_entry_in_selected_source_frame=uc_pose,
                      original_U_base_exit_bud_in_UC_frame=local_bud,
                      original_bud_last_R_tick0=u['last'][local_bud][1],
                      UC_own_C_preserves_original_bud_ID=True,
                      current_bud_in_selected_source_frame=bud,
                      selected_source_C_clock_from_UC_entry=selected_source_clock,
                      actual_foreign=foreign, actual_foreign_entry=pose,
                      actual_UC_entry_to_foreign_entry_C_age=foreign_clock,
                      bud_current_at_foreign_entry_by_all115_preforeign_queries=True,
                      foreign_RAW_never_reads_bud=True,
                      combined_first_read=('R', tick),
                      canonical_actual_physical_owner=physical_owner,
                      contradiction='Original BLACK before foreign versus actual first R/WHITE requirement; no intermediate read can repair it.'))
assert len(cases) == 5

# The returned-V D30 context genuinely misses this bud; keep it open.
pose = (3, -4, 1); rel = (bud[0]-pose[0], bud[1]-pose[1]); q = lit.rot(rel, -pose[2])
d30 = lit.trace(owner.WORDS['F']+owner.WORDS['V']+lit.M)
assert d30['feasible'] and q not in d30['first']

# This older port is not the protected UC bud. It remains genuinely unconstrained
# in a generic DC-entry history, unlike the deleted-core VC/UC source guards.
beta = (1, -1)
assert beta not in lit.trace(G[1]['word'])['first']

deps = [GP, CP, CP.parent/'manifest.json',
        H/'first_returned_five_label_frontier_manifest.json',
        H/'D_family_immediate_U_F_guard_manifest.json',
        R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out = dict(status='AUTHOR_FROZEN_IMMEDIATE_UC_BUD_GUARD_PENDING_REVIEW',
           scope='Actual U-entry complete-eight history before its first foreign; only an immediate UC predecessor of selected D/DC is tested. Excludes D15 and the three DC/C1 targets; D30 returned-V, arbitrary earlier UC/U ancestry, and all five target geometries in general remain open.',
           all115_source_UC_bud_input_queries=queries,
           query_reason_counts=dict(Counter(q['exclusion'] for q in queries)),
           five_actual_source_role_before_WHITE_exclusions=cases,
           explicit_D30_control=dict(foreign='F', foreign_entry=pose,
                                     returned_atom='V', bud=bud,
                                     combined_context_misses_bud=True,
                                     status='OPEN under this guard.'),
           retained_generic_DC_port=dict(beta=beta, DC_RAW_never_reads=True,
                                         origin_not_forced_to_be_new=True),
           no_maturation_or_COUNT5_applied_after_foreign=True,
           dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps})
(H/'D_family_immediate_UC_bud_guard.json').write_text(json.dumps(out, indent=2)+'\n')
print('115 exact preforeign bud queries:', out['query_reason_counts'])
print('Five role exclusions; returned-C RAW versus next actual word ownership retained; D30 open.')
