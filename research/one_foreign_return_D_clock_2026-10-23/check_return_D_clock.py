"""Exact one-foreign returned D/DC old-w mechanism: foreign clock at least8.
Two precise clock exclusions, no age iteration or physical attainment claim.
"""
from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};VEL=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();rq={};rd={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in rq or rq[p]==b;rq[p]=b;rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
rows=[]
for gi in(0,1):
 rp=(0,2);rh=2;_,_,_,_,prd=derive(G[gi]['word']+M);assert at((0,1),rp,rh)==(0,1)
 for j in(4,5,6):
  _,_,ep,dh,_=derive(W[j]['word']);assert dh==2;ap=sub(rp,ep);rq,_,_,_,rd=derive(W[j]['word']+M);assert not L&{at(q,ap,0)for q in rq}
  guard=(2,4)if j==4 else(1,3);local=sub(guard,ap);assert rq[local]is False
  if j==4:assert ap==(4,4)and rd[local][0]==[44,'R']
  elif j==5:assert ap==(4,6)and rd[local][0]==[58,'R']
  else:assert ap==(3,7)and rd[local][0]==[68,'R']
  # At clock0: only N bases, x=d+v, y=4+d+3v+4u.
  sols=[]
  for d in range(ap[0]+1):
   v=ap[0]-d;rem=ap[1]-4-d-3*v
   if rem>=0 and rem%4==0:sols.append(dict(d=d,v=v,u=rem//4))
  if j in(4,5):assert not sols
  else:assert sols==[dict(d=3,v=0,u=0)] # would end D, forbidden before B
  rows.append(dict(foreign='DCVUFQB'[j],foreign_pose=[*ap,0],returned_packet=G[gi]['name'],returned_pose=[0,2,2],same_original_w_tag=[0,1],first_physical_return_read=prd[(0,1)][0],required_guard=guard,foreign_guard_local=local,guard_first_read=rd[local][0],zero_C_head_solutions=sols,clock4_obstruction='first_successor_common_bud_endpoint_budget'if j==4 else'original_creator_exit_bud_no_retirement_through4',necessary_foreign_C_age_at_least=8))
# Plain V/U are the only actual last full packets before F(4,4,N).
# Neither can itself consume the common bud; it must retire earlier.
b=(2,4);last=[]
for i in(4,7):
 p=sub((4,4),tuple(G[i]['endpoint'][:2]));inputs={at(q,p,0)for q in map(tuple,G[i]['inputs'])};assert b not in inputs
 last.append(dict(type=G[i]['name'],pose=[*p,0]))
assert last==[dict(type='V',pose=[3,1,0]),dict(type='U',pose=[4,0,0])]
# First actual post-U atom starts(0,4,N), clock0, and R8 births b, even for
# UC/UCC's internal first C. Bind this signed source-clock interface literally.
common=[]
for i in range(4):
 _,_,_,_,rd=derive(W[i]['word']);assert rd[(2,0)][-1]==[8,'R'];common.append(dict(atom='DCVU'[i],start=[0,4,0],clock=0,R_phase=8,global_bud=b))
endpoint_rows=[]
for target in((3,1),(4,0)):
 for age,h in((3,1),(4,0)):
  for i in(0,4,7):
   for slot in map(tuple,G[i]['inputs']):
    p=sub(b,rot(slot,h));out=at(tuple(G[i]['endpoint'][:2]),p,h)
    if age==4:
     assert out[1]>=4>target[1];why='N_endpoint_above_target';bound=dict(minimum_later_y=out[1])
    else:
     assert out[0]>=2
     if out[0]+1>target[0]:why='required_C4_exceeds_target_x';bound=dict(minimum_later_x=out[0]+1)
     elif target==(3,1):
      assert out==(2,3);why='exact_x_budget_after_C4_y3_above_target1';bound=dict(minimum_later_y=3)
     elif out[0]==3:
      assert out[1]==4;why='C4_uses_all_x_and_y4_above_target0';bound=dict(minimum_later_y=4)
     else:
      assert target==(4,0)and out==(2,3);why='one_extra_x_can_lower_y_only_to2';bound=dict(minimum_later_y=2)
    endpoint_rows.append(dict(target_last_full_entry=[*target,0],C_age=age,consumer=G[i]['name'],input_slot=slot,pose=[*p,h],base_endpoint=[*out,h],exclusion=why,**bound))
assert len(endpoint_rows)==32
D=[GP,QP,R/'foreign_U_port_interfaces_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'foreign_renewal_bud_obstruction_2026-10-23/manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='One first foreign with COMPLETE context missing original U star, then D/DC at(0,2,S) consuming/absorbing original w=(0,1), requires foreign source-entry C clock>=8. Clocks0 and4 excluded by exact head equations and genuine creator/first-successor bud identities. Returned D physical read belongs to following phase1; DC owns RAW11. No attainment at8, returned-path simplicity, postforeign permanence or further age iteration.',six_returned_D_DC_cases=rows,last_full_predecessors_before_F44=last,genuine_first_successor_common_bud=common,clock3_4_first_consumer_endpoint_rows=endpoint_rows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'return_D_clock.json').write_text(json.dumps(o,indent=2)+'\n');print('All6 returned D/DC cases need foreign clock>=8: clock0 head/adjacency; clock4 common-bud32 endpoints or creator exitbud.')
