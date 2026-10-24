"""Complete all-predecessor retirement bridge for one DC→V age3 role.
Actual all-word cones, not a bounded search. Older JO upper4 rules suffice.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';AP=R/'chronology_dcuv/counted_input_age_rules_complete.json';RP=R/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';G=json.loads(GP.read_text())['geometry'];mins={(a,x,y):v for a,x,y,v in json.loads(AP.read_text())};RJ=json.loads(RP.read_text());T={(a,h):v for a,h,v in RJ['created_peaks']};keep=[0,1,4,5,6,7,8,9];q=(1,-1);source=1;goal=(0,1,1);DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
base={a:0 if G[a]['name'].startswith('D')else 4 if G[a]['name'].startswith('V')else 7 for a in keep}
for a in keep:assert G[a]['inputs']==G[base[a]]['inputs']and G[a]['word'].startswith(G[base[a]]['word'])
C=G[1]['word'][len(G[0]['word']):];p=(0,0);h=0
for ch in C:h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
assert(p,h)==((0,1),3)
cone={h:[rot(G[a]['endpoint'][:2],h)for a in(0,4,7)]for h in range(4)}
assert all(p[1]<=0 for h in(2,1)for p in cone[h])and all(p[0]>=0 for p in cone[1])and all(p[0]<=0 for p in cone[3])
ctx={tuple(p[:2]):p[2]for p in G[4]['requirements']};ql=rot(sub(q,goal[:2]),-goal[2]);assert ql==(2,1)and ctx[ql]==False
assert {tuple(p[:2]):p[2]for p in G[5]['requirements']}[ql]==False
assert q not in map(tuple,G[1]['inputs'])and q not in map(tuple,G[1]['outputs'])
se=tuple(G[1]['endpoint'][:2]);sh=G[1]['endpoint'][2];assert(se,sh)==((1,2),3)
rows=[];cases=[]
for a in keep:
 cc=G[a]['name'].count('C');ha=(-G[a]['endpoint'][2])%4;e=rot(G[a]['endpoint'][:2],ha);pa=(-e[0],-e[1]);assert ha==cc
 slots=[tuple(o)for o in G[a]['outputs']if add(pa,rot(o,ha))==q];assert len(slots)==1
 total=3+cc;startage=cc+1;tested=0
 for age in range(startage,total+1):
  hc=(ha-age)%4;remaining=total-age
  for b in keep:
   bc=G[b]['name'].count('C')
   if bc>remaining:continue
   for inp in G[b]['inputs']:
    if age<mins[b,*inp]:continue
    pc=sub(q,rot(inp,hc));be=add(pc,rot(G[base[b]]['endpoint'][:2],hc));tested+=1
    if cc==0 and age==2:
     assert hc==2 and remaining==1 and base[b]==4 and inp==[0,3]and be[1]-1<goal[1];why='AFTER_V_BASE_ONE_C_S_TO_E_STRICTLY_BELOW_GOAL'
    elif cc==0 and age==3:
     assert hc==1 and remaining==0 and bc==0 and be[0]>goal[0];why='FINAL_E_ZERO_CONE_CANNOT_MOVE_LEFT'
    elif cc==1 and age==2:
     assert hc==3 and base[b]==4 and inp==[0,3]and pc==(4,-1)and age-startage==0 and pc[0]>se[0];why='BEFORE_CLEARER_ZERO_C_W_CANNOT_MOVE_RIGHT'
    elif cc==1 and age==3:
     assert hc==2 and remaining==1 and be[1]-1<goal[1];why='AFTER_BASE_ONE_C_S_TO_E_STRICTLY_BELOW_GOAL'
    elif cc==1 and age==4:
     assert hc==1 and remaining==0 and bc==0 and be[0]>goal[0];why='FINAL_E_ZERO_CONE_CANNOT_MOVE_LEFT'
    elif cc==2 and age==3:
     assert hc==3 and remaining==2 and age-startage==0 and pc[0]>=2>se[0];why='BEFORE_CLEARER_ZERO_C_W_CANNOT_MOVE_RIGHT'
    elif cc==2 and age==4:
     assert hc==2 and remaining==1 and be[1]-1<goal[1];why='AFTER_BASE_ONE_C_S_TO_E_STRICTLY_BELOW_GOAL'
    elif cc==2 and age==5:
     assert hc==1 and remaining==0 and bc==0 and be[0]>goal[0];why='FINAL_E_ZERO_CONE_CANNOT_MOVE_LEFT'
    else:raise AssertionError((a,age,b,inp))
    cases.append(dict(predecessor=a,predecessor_C=cc,shadow_output_slot=slots[0],age=age,consumer=b,input=inp,consumer_pose=[*pc,hc],base_endpoint=be,remaining_C=remaining,reason=why))
 assert tested;rows.append(dict(predecessor=a,entering_pose=[*pa,ha],shadow_output_slot=slots[0],shadow_goal_age=total,retirement_cases=tested))
# Precise origin/goal roles and full unfunded entry argument.
assert add(goal[:2],rot((0,3),goal[2]))==(3,1)and[3,1]in G[1]['outputs']
H=sum(goal[:2]);S=2*H+T[4,1];assert H==1 and S==28 and G[1]['inputs']==[[0,1]]
activation=28+2*sum(G[1]['inputs'][0]);assert activation==S+2
J=dict(status='AUTHOR_DC_AGE3_V_BOUNDARY_PREDECESSOR_SHADOW_PASS',scope='Only DCsource(0,0,N), oldoutput(3,1)→V/VCinput(0,3) atgoal(0,1,E), exactCage3, actual complete recurrent8 factor. No predecessor possible on any board. Thus sourceDC must be factorFIRST; its I28 activation funds V1. Not allV1 or capture.',universal_predecessor_shadow=dict(cell=q,goal_white_slot=ql,source_DC_exit=[*se,sh],source_DC_leaves_shadow_current=True),predecessors=rows,retirement_cases=cases,cone_steps=cone,record_corollary=dict(goal_head_height=H,goal_score=S,first_source_input_height=H,I28_activation=activation,activation_margin=2),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,AP,RP,Path(__file__).resolve()]})
(R/'chronology_dcuv/v1_DC_age3_boundary_shadow.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(predecessors=len(rows),retirement_cases=len(cases),first_source_input_activation=activation,target_score=S))
