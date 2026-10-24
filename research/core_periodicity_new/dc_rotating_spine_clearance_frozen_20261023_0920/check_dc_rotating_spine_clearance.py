"""Complete finite geometry for the all-N rotating DC spine clearance lemma."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(gp.read_text())['geometry'];g=G[1];core={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def plus(p,q):return(p[0]+q[0],p[1]+q[1])
heads=[((0,0),0)]
for _ in range(4):
 p,h=heads[-1];heads.append((plus(p,rot((1,0),h)),(h+1)%4))
assert heads[-1]==heads[0]
inputs=[];outputs=[];contexts=[]
for p,h in heads:
 inputs.append(plus(p,rot((0,1),h)));outputs.append([plus(p,rot(q,h))for q in g['outputs']]);contexts.append({plus(p,rot(q[:2],h)):q[2]for q in g['requirements']})
for j in range(4):assert outputs[j][0]==inputs[j+1]
side=outputs[0][1:];assert side==[(2,3),(3,1),(3,2)]
for j in range(1,4):assert all(q not in contexts[j]for q in side)
assert all(contexts[4][q]is False for q in side)
assert len({q for out in outputs[:4]for q in out[1:]})==12
# Complete all-parameter claims use period4. The following arithmetic is control,
# not a substitute for the proof that each identity is fresh and retires once.
for N in range(4,1001):
 due=sum(3 for j in range(N)if j+4<N);assert due==3*max(N-4,0)
cp=R/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';rows=[tuple(map(int,s.split()))for s in cp.read_text().splitlines()];query=(1,1,1,0,1,2,0,3);hits=[r for r in rows if r[:8]==query];assert len(hits)==1
assert not any(r[:8]==query[:7]+(5,)for r in rows)
J={'status':'AUTHOR_COMPLETE_PERIOD4_CLEARANCE_GEOMETRY_PASS','scope':'Ordered residual identities, not physical black-lifetime tokens. Repeated A=(2,0),heading+1 DC spine; no all-age transfer exclusion or capture.','chosen_source_output':[2,0],'selected_target_input':[0,1],'relative_target_pose':[1,0,1],'minimum_C_age':7,'age3_excluded_query':hits[0],'overflow5_excluded':False,'four_producer_poses':[[*p,h]for p,h in heads[:4]],'spine_inputs':inputs,'spare_outputs_by_phase':[x[1:]for x in outputs[:4]],'source_spares':side,'intervening_spine_contexts_miss_all_spares':True,'fourth_descendant_requires_all_spares_white':True,'distinct_spare_slots_over_period':12,'all_N_retirements':'at least 3*max(N-4,0) distinct source-spare identities retired by support packet inputs before Nth producer','support_packet_bound':'ceil(3*max(N-4,0)/5), because every recurrent packet has at most5 residual inputs','additional_clock_bound':'C_birth_gap between first and Nth producer at least7*(N-1); at least6*(N-1) C macros lie in strict support packets','input_hashes':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[gp,cp,Path(__file__).resolve()]}}
(R/'chronology_dcuv/dc_rotating_spine_clearance.json').write_text(json.dumps(J,indent=2)+'\n');print({k:v for k,v in J.items()if k not in['input_hashes']})
