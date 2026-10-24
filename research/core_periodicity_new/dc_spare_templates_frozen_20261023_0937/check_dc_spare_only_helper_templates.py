"""Complete local all-input template enumeration, no cursor realization claim."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(gp.read_text())['geometry'];ids=(0,1,4,5,6,7,8,9)
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
A=(2,0);orig={tuple(q)for q in G[1]['outputs']};S=orig-{A}
def enum(current,anchor,allowed):
 # Any candidate consuming an anchor is fixed by its heading and which I slot
 # equals that anchor. Thus this finite set contains every possible helper.
 candidates=set()
 for a in ids:
  for h in range(4):
   for q in anchor:
    for ii in G[a]['inputs']:
     p=sub(q,rot(ii,h))
     if(sum(p)-h)%2==0:candidates.add((a,*p,h))
 rows=[];accept=[]
 for a,x,y,h in sorted(candidates):
  p=(x,y);g=G[a];I={add(p,rot(q,h))for q in g['inputs']};ctx={add(p,rot(q[:2],h))for q in g['requirements']};B=(current-I)&ctx
  reason='ACCEPT'if I<=allowed and not B else'INPUT_OUTSIDE_ALLOWED'if not I<=allowed else'CURRENT_NONINPUT_IN_CONTEXT'
  row={'packet':a,'name':g['name'],'pose':[x,y,h],'inputs':sorted(I),'outside_inputs':sorted(I-allowed),'blocking_current_noninputs':sorted(B),'result':reason};rows.append(row)
  if reason=='ACCEPT':accept.append(row)
 return rows,accept
rows,acc=enum(orig,S,S)
assert[(r['packet'],r['pose'])for r in acc]==[(0,[2,4,2]),(4,[3,5,2])]
vp=(3,5);vh=2;VI={add(vp,rot(q,vh))for q in G[4]['inputs']};VO={add(vp,rot(q,vh))for q in G[4]['outputs']};assert VI=={(2,3),(3,2)}
Rafter=(orig-VI)|VO;assert len(Rafter)==8
rows2,acc2=enum(Rafter,{(3,1)},Rafter-{A});assert acc2==[]
# The obvious remaining D, at(4,1,W), is blocked by the fresh V output(3,4).
drow=next(r for r in rows2 if r['packet']==0 and r['pose']==[4,1,3]);assert(3,4)in map(tuple,drow['blocking_current_noninputs'])
# Direct D branch: retain its replacements instead of silently dropping them.
R1=(orig-{(2,3)})|{(0,4)};r1,a1=enum(R1,{(3,1),(3,2)},R1-{A});assert[(r['packet'],r['pose'])for r in a1]==[(0,[3,3,2])]
R2=(R1-{(3,2)})|{(1,3)};r2,a2=enum(R2,{(3,1)},R2-{A});assert[(r['packet'],r['pose'])for r in a2]==[(0,[4,1,3])]
J={'status':'AUTHOR_COMPLETE_ALL_INPUT_TEMPLATE_PASS','scope':'Static complete-context necessary conditions only. MainA remains a current ordered residual identity. No literal helper path, imported initial root, or global branching claim.','source_outputs':sorted(orig),'initial_original_spare_only_candidates':rows,'initial_accepted_helpers':acc,'V_merge_inputs':sorted(VI),'V_merge_outputs':sorted(VO),'after_V_current_cohort':sorted(Rafter),'remaining_original_C_candidates_without_import_or_retirement':rows2,'remaining_original_C_accepted_helpers':acc2,'direct_D_branch_second':a1,'direct_D_branch_third':a2,'implication':'After the V merger, before the remaining original C=(3,1) retires, either some fresh V output has retired or the packet retiring C consumes an identity outside the fixed eight-identity post-V cohort. MainA must stay current throughout.','input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest()}
(R/'chronology_dcuv/dc_spare_only_helper_templates.json').write_text(json.dumps(J,indent=2)+'\n');print({'initial_candidates':len(rows),'accepted_first':[(r['name'],r['pose'],r['inputs'])for r in acc],'after_V_candidates':len(rows2),'after_V_accepted':len(acc2),'replacement_blocking_remaining_D':[3,4]})
