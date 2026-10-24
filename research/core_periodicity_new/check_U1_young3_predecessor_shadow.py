"""Complete finite retirement/endpoint-cone table for young3 V/VC sources.
No packet-depth/head-box bound: the zero/one-C cones are all-word monotonicity.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';AP=R/'chronology_dcuv/counted_input_age_rules_complete.json';RP=R/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';G=json.loads(GP.read_text())['geometry'];mins={(a,x,y):r for a,x,y,r in json.loads(AP.read_text())};RJ=json.loads(RP.read_text());A=RJ['core_offsets'];T={(a,h):t for a,h,t in RJ['created_peaks']};keep=[0,1,4,5,6,7,8,9];goal=(0,-1,1);Sscore=28
# Deliberately use the weaker old JO minima (upper4), not exact-four holes/KV5.
assert mins[0,0,1]==3 and mins[4,0,3]==2 and mins[4,1,2]==3
assert all(v>=2 for v in mins.values())
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
base={a:0 if G[a]['name'].startswith('D')else 4 if G[a]['name'].startswith('V')else 7 for a in keep}
for a in keep:
 assert G[a]['inputs']==G[base[a]]['inputs']
 assert G[a]['word'].startswith(G[base[a]]['word'])
C=G[1]['word'][len(G[0]['word']):];p=(0,0);h=0;DIR=((0,1),(1,0),(0,-1),(-1,0))
for ch in C:h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
assert(p,h)==((0,1),3)
cone={h:[rot(G[a]['endpoint'][:2],h)for a in(0,4,7)]for h in range(4)}
assert all(q[1]>=0 for h in(0,3)for q in cone[h]) and rot((0,1),0)[1]==1
assert all(q[1]<=0 for h in(2,1)for q in cone[h]) and rot((0,1),2)[1]==-1
assert all(q[0]<=0 for q in cone[3])
# The two forbidden shadow cells map to U's BEFORE-white requirements.
ctx={tuple(q[:2]):q[2]for q in G[7]['requirements']}
for q in[(1,-1),(0,-3)]:assert ctx[rot(sub(q,goal[:2]),-goal[2])]==False
shadows={0:((1,-1),(2,0)),1:((1,-1),(2,3)),4:((0,-3),(1,0)),5:((1,-1),(2,5)),7:((0,-3),(0,1)),8:((1,-1),(1,6))}
rows=[];retirement_cases=[]
for a in keep:
 cc=G[a]['name'].count('C');ha=(-G[a]['endpoint'][2])%4;e=rot(G[a]['endpoint'][:2],ha);pa=(-e[0],-e[1]);assert ha==cc
 if cc==2:
  entering=2*sum(pa)+A[ha];assert entering==Sscore;rows.append(dict(predecessor=a,pose=[*pa,ha],reason='ENTERING_CORE_TIES_TARGET',core_value=entering));continue
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
      assert hc==2 and remaining==1 and base[b]==4 and inp==[0,3]
      assert be[1]-1<goal[1];why='AFTER_V_BASE_ONE_C_S_TO_E_STRICTLY_LOWERS_Y'
     elif cc==0 and age==3:
      assert hc==1 and remaining==0 and bc==0
      assert be[0]>goal[0]or be[1]<goal[1];why='FINAL_E_ZERO_CONE_OVERSHOOT'
     elif cc==1 and age==2:
      assert hc==3 and base[b]==4 and inp==[0,3]and pc==(4,-1)
      if s==4:
       assert sh==0 and age-(cc+cs)==1 and pc[1]<se[1]+1;why='BEFORE_CLEARER_ONE_C_N_TO_W_Y_NONDECREASE'
      else:
       assert sh==3 and age-(cc+cs)==0 and pc[0]>se[0];why='BEFORE_CLEARER_ZERO_C_W_X_NONINCREASE'
     elif cc==1 and age==3:
      assert hc==2 and remaining==1
      assert be[1]-1<goal[1];why='AFTER_BASE_ONE_C_S_TO_E_STRICTLY_LOWERS_Y'
     elif cc==1 and age==4:
      assert hc==1 and remaining==0 and bc==0
      assert be[0]>goal[0];why='FINAL_E_ZERO_CONE_OVERSHOOT'
     else:raise AssertionError((a,s,age,b,inp))
     retirement_cases.append(dict(predecessor=a,source=s,shadow=q,age=age,consumer=b,input=inp,consumer_pose=[*pc,hc],remaining_C=remaining,base_endpoint=be,reason=why))
  assert tested;per_source[s]=tested
 rows.append(dict(predecessor=a,pose=[*pa,ha],shadow=q,shadow_output_slot=slot,goal_shadow_local_slot=rot(sub(q,goal[:2]),-goal[2]),source_included_goal_age=total,retirement_candidates_per_source=per_source,reason='ALL_MANDATORY_RETIREMENTS_EXCLUDED_BY_COMPLETE_CONES'))
# If no predecessor, source I cells are actual initial residuals, not core.
for s in(4,5):
 for q in G[s]['inputs']:assert tuple(q)not in{(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}and 28+2*sum(q)==34>Sscore
J=dict(status='AUTHOR_COMPLETE_YOUNG3_PREDECESSOR_SHADOW_TABLE_PASS',scope='Sources V/VC0,N, Utarget(0,-1,E), sourceincluded age3. Six0/1C predecessors impossible on any board; two2C predecessors tie strict record threshold. No all-age U1 or capture claim.',rows=rows,retirement_cases=retirement_cases,cone_steps=cone,standalone_C_endpoint=[0,1,3],source_first_packet_funding=dict(input_heights=[3,3],I28_activations=[34,34],target_score=28),corollary_pending_review='Combining signed LN same-cohort young3 source classification and earlier VCC exit-core cut, no produced q age3 can occur at an unfunded U1 record. This is record-conditional, not a global q minimum.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,AP,RP,Path(__file__).resolve()]})
(R/'chronology_dcuv/U1_young3_predecessor_shadow.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(predecessors=len(rows),retirement_cases=len(retirement_cases),record_tie_cases=[r['predecessor']for r in rows if'core_value'in r]))
