"""Complete all-eight predecessor shadow exclusion for V/VC young3 sources.
Extends the signed1220 table; no record cuts, depth or head box. VCC branch
uses its independently signed unique VC,D continuation plus all8 raw cuts.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';AP=R/'chronology_dcuv/counted_input_age_rules_complete.json';G=json.loads(GP.read_text())['geometry'];mins={(a,x,y):r for a,x,y,r in json.loads(AP.read_text())};keep=[0,1,4,5,6,7,8,9];goal=(0,-1,1);DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
base={a:0 if G[a]['name'].startswith('D')else 4 if G[a]['name'].startswith('V')else 7 for a in keep}
for a in keep:
 assert G[a]['inputs']==G[base[a]]['inputs']
 assert G[a]['word'].startswith(G[base[a]]['word'])
C=G[1]['word'][len(G[0]['word']):];p=(0,0);h=0
for ch in C:h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
assert(p,h)==((0,1),3)
cone={h:[rot(G[a]['endpoint'][:2],h)for a in(0,4,7)]for h in range(4)}
assert all(q[1]>=0 for h in(0,3)for q in cone[h])
assert all(q[1]<=0 for h in(2,1)for q in cone[h])
assert all(q[0]<=0 for q in cone[3])and all(q[0]>=0 for q in cone[1])
ctx={tuple(q[:2]):q[2]for q in G[7]['requirements']}
for q in[(1,-1),(0,-3)]:assert ctx[rot(sub(q,goal[:2]),-goal[2])]==False
shadows={0:((1,-1),(2,0)),1:((1,-1),(2,3)),4:((0,-3),(1,0)),5:((1,-1),(2,5)),6:((1,-1),(-1,5)),7:((0,-3),(0,1)),8:((1,-1),(1,6)),9:((1,-1),(-2,6))}
rows=[];cases=[]
for a in keep:
 cc=G[a]['name'].count('C');ha=(-G[a]['endpoint'][2])%4;e=rot(G[a]['endpoint'][:2],ha);pa=(-e[0],-e[1]);assert ha==cc
 q,slot=shadows[a];assert list(slot)in G[a]['outputs']and add(pa,rot(slot,ha))==q
 total=3+cc;per_source={}
 for s in(4,5):
  se=tuple(G[s]['endpoint'][:2]);sh=G[s]['endpoint'][2];cs=G[s]['name'].count('C');assert q not in map(tuple,G[s]['inputs'])and q not in map(tuple,G[s]['outputs'])
  tested=0
  for age in range(total+1):
   if age<cc+cs:continue
   hc=(ha-age)%4;remaining=total-age
   for b in keep:
    bc=G[b]['name'].count('C')
    if bc>remaining:continue
    for inp in G[b]['inputs']:
     if age<mins[b,*inp]:continue
     pc=sub(q,rot(inp,hc));be=add(pc,rot(G[base[b]]['endpoint'][:2],hc));tested+=1
     if cc==0 and age==2:
      assert hc==2 and remaining==1 and base[b]==4 and inp==[0,3]and be[1]-1<goal[1];why='AFTER_V_BASE_ONE_C_S_TO_E_STRICTLY_LOWERS_Y'
     elif cc==0 and age==3:
      assert hc==1 and remaining==0 and bc==0 and(be[0]>goal[0]or be[1]<goal[1]);why='FINAL_E_ZERO_CONE_OVERSHOOT'
     elif cc==1 and age==2:
      assert hc==3 and base[b]==4 and inp==[0,3]and pc==(4,-1)
      if s==4:assert sh==0 and age-(cc+cs)==1 and pc[1]<se[1]+1;why='BEFORE_CLEARER_ONE_C_N_TO_W_Y_NONDECREASE'
      else:assert sh==3 and age-(cc+cs)==0 and pc[0]>se[0];why='BEFORE_CLEARER_ZERO_C_W_X_NONINCREASE'
     elif cc==1 and age==3:
      assert hc==2 and remaining==1 and be[1]-1<goal[1];why='AFTER_BASE_ONE_C_S_TO_E_STRICTLY_LOWERS_Y'
     elif cc==1 and age==4:
      assert hc==1 and remaining==0 and bc==0 and be[0]>goal[0];why='FINAL_E_ZERO_CONE_OVERSHOOT'
     elif cc==2 and age==2:
      assert s==4 and sh==0 and hc==0 and remaining==3 and base[b]==4 and inp==[0,3]and pc==(1,-4)
      assert age-(cc+cs)==0 and pc[1]<se[1];why='BEFORE_CLEARER_ZERO_C_N_Y_NONDECREASE'
     elif cc==2 and age==3:
      assert hc==3 and remaining==2 and pc[0]>=2 and pc[1]<=0
      if s==4:assert sh==0 and age-(cc+cs)==1 and pc[1]<se[1]+1;why='BEFORE_CLEARER_ONE_C_N_TO_W_Y_NONDECREASE'
      else:assert sh==3 and age-(cc+cs)==0 and pc[0]>se[0];why='BEFORE_CLEARER_ZERO_C_W_X_NONINCREASE'
     elif cc==2 and age==4:
      assert hc==2 and remaining==1 and be[1]-1<goal[1];why='AFTER_BASE_ONE_C_S_TO_E_STRICTLY_LOWERS_Y'
     elif cc==2 and age==5:
      assert hc==1 and remaining==0 and bc==0 and be[0]>goal[0];why='FINAL_E_ZERO_CONE_OVERSHOOT'
     else:raise AssertionError((a,s,age,b,inp))
     cases.append(dict(predecessor=a,source=s,shadow=q,age=age,consumer=b,input=inp,consumer_pose=[*pc,hc],remaining_C=remaining,base_endpoint=be,reason=why))
  assert tested;per_source[s]=tested
 rows.append(dict(predecessor=a,pose=[*pa,ha],shadow=q,shadow_output_slot=slot,goal_shadow_local_slot=rot(sub(q,goal[:2]),-goal[2]),source_included_goal_age=total,retirement_candidates_per_source=per_source))
# VCC source: signed1026 all-word continuation is uniquely VC,D. Check every
# complete predecessor and every U/UC/UCC tail without relying on a DFA.
vcc_cuts=[]
for a in keep:
 ph=(-G[a]['endpoint'][2])%4;e=rot(G[a]['endpoint'][:2],ph);pp=(-e[0],-e[1])
 for tail in(7,8,9):
  suffix=[6,5,0,tail];word=G[a]['word']+''.join(G[b]['word']for b in suffix)+G[tail]['marker'];p=pp;h=ph;last={};bad=None
  for t,ch in enumerate(word):
   if p in last and last[p][1]==ch:bad=dict(cell=p,previous_read=last[p][0],conflicting_read=t,turn=ch);break
   last[p]=(t,ch);h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
  assert bad;vcc_cuts.append(dict(predecessor=a,tail=tail,start_pose=[*pp,ph],conflict=bad,suffix_conflict_phase=bad['conflicting_read']-len(G[a]['word'])))
assert len(vcc_cuts)==24
J=dict(status='AUTHOR_ALL_EIGHT_PREDECESSORS_EXCLUDED_FOR_YOUNG3_SOURCES_PASS',scope='Actual complete recurrent8 factor; ordered residual q age3, all U tails. With signed LN same-source classification and1026 VCC unique continuation, its producer must be FIRST factor packet. This is not a global input minimum or capture.',V_VC_predecessor_rows=rows,all_retirement_cases=cases,VCC_unique_continuation=[5,0],VCC_predecessor_literal_cuts=vcc_cuts,cone_steps=cone,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,AP,Path(__file__).resolve()]})
(R/'chronology_dcuv/U_young3_boundary_shadow.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(predecessors=len(rows),retirement_cases=len(cases),new_c2_cases=sum(c['predecessor']in(6,9)for c in cases),vcc_raw_cuts=len(vcc_cuts),max_vcc_suffix_conflict_phase=max(c['suffix_conflict_phase']for c in vcc_cuts)))
