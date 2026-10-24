"""The three specific physically lifted cap6 resource profiles, all nine pairs.
This is a supplied-candidate composition test, not a generic trajectory scan.
"""
from pathlib import Path
from itertools import product
import json,hashlib
from finite_component_profile_lift import lift
from active_flight import cursor,ends,vertices,comp
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
SRC=ROOT/'reframe_finite_seed_2026-10-24/physical_cap6_resource_obstructions.json'
j=json.loads(SRC.read_text());M={a['index']:a for ob in j['obstructions']for a in ob['cycles']}
assert set(M)=={2818,33389,33390}
single=[]
for a in M.values():
 x=lift([a],True);assert x['status']=='ACTUAL_FINITE_BOARD_LIFT'and set(x['initial_black'])==set(map(tuple,a['minimal_seed']));single.append(x)
pairs=[lift([M[a],M[b]],True)for a,b in product(sorted(M),repeat=2)]
for a in single:
 F=set(map(tuple,a['final_black']));p,h=a['final_pose'];r=cursor(p,h)
 U=set()
 for dx,dy in product((-2,2),repeat=2):U|=comp(F,1,(r[0]+dx,r[1]+dy))
 x,y=ends(p,1);u=y if x==r else x
 a['mandatory_output_budget']=dict(forced_imported_edges=sorted(U),forced_mass=len(U),first_tip_in_forced_field=u in vertices(U,1),trapped=len(U)>2 or(len(U)==2 and u not in vertices(U,1)))
 assert len(U)==({2818:2,33389:1,33390:2}[a['macros'][0]])
out=dict(status='EXACT supplied cap6 profile pair composition controls',source_sha256={str(SRC.relative_to(ROOT)):hashlib.sha256(SRC.read_bytes()).hexdigest()},single_profiles=single,all_nine_ordered_pairs=pairs,scope='A positive pair is one actual fixed finite initial board with no mid-run changes and explicit lifetime provenance. A negative pair is an arbitrary-exterior complete-component port/read-parity contradiction. Neither outcome classifies intervening profiles or proves indefinite regeneration.')
(OUT/'three_cap6_profiles_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'singles':[{k:a[k]for k in['macros','initial_mass','maximum_complete_active_mass','final_pose']}for a in single],'pairs':[{k:a[k]for k in['status','macros','conflict_cell','initial_mass']if k in a}for a in pairs]},indent=2))
