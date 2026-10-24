"""All49 ordered pairs of the exact seven supplied cap6 zero-fuel profiles.
No assumption that pairwise compatibility alone implies whole-cycle realization.
"""
from pathlib import Path
from itertools import product
import json,hashlib
from finite_component_profile_lift import lift
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
SRC=ROOT/'reframe_finite_seed_2026-10-24/cap6_seven_zero_fuel_profiles.json'
j=json.loads(SRC.read_text());M={a['index']:a for a in j['profiles']};assert len(M)==7
single=[]
for a in M.values():
 x=lift([a],True);assert x['status']=='ACTUAL_FINITE_BOARD_LIFT'and set(x['initial_black'])==set(map(tuple,a['minimal_seed']));single.append(x)
pairs=[lift([M[a],M[b]],True)for a,b in product(sorted(M),repeat=2)]
E=[tuple(a['macros'])for a in pairs if a['status']=='ACTUAL_FINITE_BOARD_LIFT']
# Exact Kahn certificate, if the compatible-pair graph is acyclic.
left=set(M);order=[]
while left:
 zero=sorted(v for v in left if not any(a in left and b==v for a,b in E))
 if not zero:break
 order+=zero;left-=set(zero)
out=dict(status='EXACT supplied seven-profile full-board composition matrix',source_sha256={str(SRC.relative_to(ROOT)):hashlib.sha256(SRC.read_bytes()).hexdigest()},single_profiles=single,all_49_ordered_pairs=pairs,compatible_edges=E,pair_graph_topological_prefix=order,pair_graph_cyclic_remainder=sorted(left),scope='A positive pair is a real fixed complete finite-board execution with lifetime provenance. A negative pair excludes every unread exterior by complete-port/read-parity conflict. Any surviving graph cycle still needs a whole-cycle archive test.')
(OUT/'seven_cap6_profiles_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'compatible_edges':E,'topological_prefix':order,'cyclic_remainder':sorted(left),'positive_pairs':[{k:a[k]for k in['macros','initial_mass','maximum_complete_active_mass','final_pose']}for a in pairs if a['status']=='ACTUAL_FINITE_BOARD_LIFT']},indent=2))
