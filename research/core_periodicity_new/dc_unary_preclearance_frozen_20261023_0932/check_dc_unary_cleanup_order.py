"""Complete finite original-identity geometry for unary-D preclearance.
This is not a literal realization or an exclusion of helper-supported spines.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(gp.read_text());G=J['geometry'];core={tuple(q)for q in J['core']}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def plus(p,q):return(p[0]+q[0],p[1]+q[1])
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
O=[tuple(q)for q in G[1]['outputs']];ctx={tuple(q[:2]):q[2]for q in G[0]['requirements']};choices=[]
for j,q in enumerate(O[1:],1):
 for h in range(4):
  p=sub(q,rot((0,1),h))
  if(sum(p)-h)%2:continue
  obs=[]
  for k,z in enumerate(O):
   if k==j:continue
   v=rot(sub(z,p),-h)
   if v in ctx:obs.append({'source_output_index':k,'reason':'core'if v in core else'white'if not ctx[v]else'other_black_context'})
  choices.append({'retired_index':j,'pose':[*p,h],'blockers':obs})
paths=[]
def rec(rem,path):
 if rem=={0}:paths.append(path);return
 for c in choices:
  if c['retired_index']in rem and all(b['source_output_index']not in rem for b in c['blockers']):rec(rem-{c['retired_index']},path+[c])
rec(set(range(4)),[])
assert len(paths)==1;path=paths[0];assert [c['retired_index']for c in path]==[1,3,2]
poses=[c['pose']for c in path];assert poses==[[2,4,2],[3,3,2],[4,1,3]]
outs=[plus(tuple(c['pose'][:2]),rot((2,0),c['pose'][2]))for c in path];assert outs==[(0,4),(1,3),(4,3)]
for i,q in enumerate(outs):
 for c in path[i+1:]:assert rot(sub(q,c['pose'][:2]),-c['pose'][2])not in ctx
 assert rot(sub(q,(1,0)),-1)not in {tuple(v[:2])for v in G[1]['requirements']}
# JO: the first produced D input has age>=3, and h=2 gives n=2 mod4.
first=min(n for n in range(3,10)if n%4==2);assert first==6
# After the first D raw endpoint, a zero-C path is a nonnegative sum of
# rot(D=(1,1),V=(1,3),U=(0,4),h2), hence its x coordinate cannot increase.
p0=plus(tuple(poses[0][:2]),rot((1,1),poses[0][2]));assert p0==(1,3)
delta=sub(tuple(poses[1][:2]),p0);assert delta==(2,0)
assert all(rot(tuple(G[a]['endpoint'][:2]),2)[0]<=0 for a in(0,4,7))
second=first+4;third=second+3;continuation=third+2;assert(first,second,third,continuation)==(6,10,13,15)
Q={'status':'AUTHOR_COMPLETE_UNARY_PRECLEARANCE_GEOMETRY_AND_CLOCK_PASS','scope':'Conditional: main source output(2,0) stays current; each original source spare is retired by a D packet before the next DC continuation. Other helper packets and replacements are allowed. No physical realization or all-chain exclusion.','source_DC_outputs':O,'all_six_sector_D_consumer_poses':choices,'unique_original_identity_clearance_order':path,'replacement_D_outputs':outs,'replacements_miss_later_cleanup_and_continuation_contexts':True,'minimum_source_C_clocks':[first,second,third],'minimum_precleared_first_continuation_C_age':continuation,'zero_C_obstruction':{'first_D_raw_exit':p0,'second_D_start':poses[1][:2],'required_displacement':delta,'zero_C_DVU_heading2_x_displacements':[rot(tuple(G[a]['endpoint'][:2]),2)[0]for a in(0,4,7)]},'input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest()}
(R/'chronology_dcuv/dc_unary_cleanup_order.json').write_text(json.dumps(Q,indent=2)+'\n');print(json.dumps(Q,indent=2))
