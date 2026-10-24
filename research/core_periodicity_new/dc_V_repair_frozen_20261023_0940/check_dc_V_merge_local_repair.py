"""Positive exact-mask control, explicitly NOT a continuous-head ant word."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(gp.read_text())['geometry'];A=(2,0)
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def apply(R,a,p,h):
 g=G[a];I={add(p,rot(q,h))for q in g['inputs']};O={add(p,rot(q,h))for q in g['outputs']};ctx={add(p,rot(q[:2],h))for q in g['requirements']};assert I<=R and not(R-I)&ctx
 assert A not in I;assert not O&(R-I)
 return (R-I)|O,{'packet':a,'pose':[*p,h],'inputs':sorted(I),'outputs':sorted(O),'retained_other_current_identities':sorted(R-I),'raw_exit':[*add(p,rot(g['endpoint'][:2],h)),(h+g['endpoint'][2])%4]}
R0={tuple(q)for q in G[1]['outputs']};R1,e1=apply(R0,4,(3,5),2);R2,e2=apply(R1,0,(3,3),0);R3,e3=apply(R2,0,(4,1),3)
assert(3,4)not in R2 and(3,1)not in R3;assert len(R1)==len(R2)==len(R3)==8
# All source/consumer original identities are distinct; no helper input outside
# the V branch's eight-identity cohort or its unary descendants is needed here.
J={'status':'POSITIVE_COMPLETE_MASK_CONTROL_ONLY','scope':'All residual masks, other current identities, guards and replacement identities are retained. Heads are chosen independently, so this is not a literal word, actual C-clock realization, or ant trajectory.','source_residual_outputs':sorted(R0),'steps':[e1,e2,e3],'final_residual_cohort':sorted(R3),'no_imported_residual_input':True,'head_continuity':False,'explicit_cursor_gap':{'first_D_raw_exit':e2['raw_exit'],'next_D_start':e3['pose'],'one_C_gap_impossible':'At N before and W after one C, every DVU zero-C run and every single-C DC/VC/UC packet has nonnegative y displacement, but this gap needs y=-3. Thus this particular ordered pair needs at least5 Cs, not1.'},'input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest()}
assert e2['raw_exit']==[4,4,0]and e3['pose']==[4,1,3]
assert all(G[a]['endpoint'][1]>=0 for a in(0,4,7,1,5,8))
assert all(rot(G[a]['endpoint'][:2],3)[1]>=0 for a in(0,4,7))
(R/'chronology_dcuv/dc_V_merge_local_repair.json').write_text(json.dumps(J,indent=2)+'\n');print({'status':J['status'],'local_steps':[(e['packet'],e['pose'])for e in J['steps']],'CohortSize':len(R3),'real_head_continuity':False})
