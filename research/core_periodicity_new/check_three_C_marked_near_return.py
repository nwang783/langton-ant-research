"""Universal noninitial marked-pose avoidance at C distance3.
Full eight-source/eight-predecessor retirement table; no record or old-output
survival premise. All target packets use one common before-white marker cell.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';AP=R/'chronology_dcuv/counted_input_age_rules_complete.json';G=json.loads(GP.read_text())['geometry'];mins={(a,x,y):v for a,x,y,v in json.loads(AP.read_text())};keep=[0,1,4,5,6,7,8,9];q=(1,-1);goal=(0,1,1);DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
base={a:0 if G[a]['name'].startswith('D')else 4 if G[a]['name'].startswith('V')else 7 for a in keep}
for a in keep:assert G[a]['inputs']==G[base[a]]['inputs']and G[a]['word'].startswith(G[base[a]]['word'])
C=G[1]['word'][len(G[0]['word']):];p=(0,0);h=0
for ch in C:h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
assert(p,h)==((0,1),3)
cone={h:[rot(G[a]['endpoint'][:2],h)for a in(0,4,7)]for h in range(4)}
assert all(p[1]>=0 for h in(0,3)for p in cone[h])and all(p[1]<=0 for h in(2,1)for p in cone[h])
assert all(p[0]>=0 for p in cone[1])and all(p[0]<=0 for p in cone[3])
# All eight next markers prescribe q WHITE; all eight source words miss q.
ql=rot(sub(q,goal[:2]),-goal[2]);assert ql==(2,1);target_rows=[];source_rows=[]
for a in keep:
 ctx={tuple(p[:2]):p[2]for p in G[a]['requirements']};assert ctx[ql]==False and q not in ctx
 assert q not in map(tuple,G[a]['inputs'])and q not in map(tuple,G[a]['outputs'])
 target_rows.append(dict(target_packet=a,goal_white_slot=ql,goal_white_requirement=[v for v in G[a]['requirements']if tuple(v[:2])==ql][0]))
 cs=G[a]['name'].count('C');sx,sy,sh=G[a]['endpoint'];assert sh==(-cs)%4
 if cs==0:assert sh==0 and sy>=1
 elif cs==1:assert sh==3 and sx<=1
 source_rows.append(dict(source_packet=a,C_count=cs,raw_endpoint=[sx,sy,sh],complete_context_misses_local_shadow=True))
rows=[];cases=[]
for a in keep:
 cc=G[a]['name'].count('C');ha=(-G[a]['endpoint'][2])%4;e=rot(G[a]['endpoint'][:2],ha);pa=(-e[0],-e[1]);assert ha==cc
 slots=[tuple(o)for o in G[a]['outputs']if add(pa,rot(o,ha))==q];assert len(slots)==1
 total=3+cc;counts={}
 for s in keep:
  cs=G[s]['name'].count('C');se=tuple(G[s]['endpoint'][:2]);sh=G[s]['endpoint'][2];startage=cc+cs;tested=0
  for age in range(startage,total+1):
   hc=(ha-age)%4;remaining=total-age
   for b in keep:
    bc=G[b]['name'].count('C')
    if bc>remaining:continue
    for inp in G[b]['inputs']:
     if age<mins[b,*inp]:continue
     pc=sub(q,rot(inp,hc));be=add(pc,rot(G[base[b]]['endpoint'][:2],hc));tested+=1
     if cc==0 and age==2:
      assert hc==2 and remaining==1 and base[b]==4 and inp==[0,3]and be[1]-1<goal[1];why='AFTER_V_BASE_ONE_C_S_TO_E_STRICTLY_BELOW_TARGET'
     elif cc==0 and age==3:
      assert hc==1 and remaining==0 and bc==0 and be[0]>goal[0];why='FINAL_E_ZERO_CONE_CANNOT_MOVE_LEFT'
     elif cc==1 and age==2:
      assert hc==3 and base[b]==4 and inp==[0,3]and pc==(4,-1)
      if cs==0:assert sh==0 and age-startage==1 and se[1]+1>pc[1];why='BEFORE_CLEARER_ONE_C_N_TO_W_Y_NONDECREASE'
      else:assert cs==1 and sh==3 and age-startage==0 and pc[0]>se[0];why='BEFORE_CLEARER_ZERO_C_W_CANNOT_MOVE_RIGHT'
     elif cc==1 and age==3:
      assert hc==2 and remaining==1 and be[1]-1<goal[1];why='AFTER_BASE_ONE_C_S_TO_E_STRICTLY_BELOW_TARGET'
     elif cc==1 and age==4:
      assert hc==1 and remaining==0 and bc==0 and be[0]>goal[0];why='FINAL_E_ZERO_CONE_CANNOT_MOVE_LEFT'
     elif cc==2 and age==2:
      assert cs==0 and sh==0 and hc==0 and remaining==3 and base[b]==4 and inp==[0,3]and pc==(1,-4)
      assert age-startage==0 and se[1]>pc[1];why='BEFORE_CLEARER_ZERO_C_N_CANNOT_MOVE_DOWN'
     elif cc==2 and age==3:
      assert hc==3 and remaining==2 and pc[0]>=2 and pc[1]<=0
      if cs==0:assert sh==0 and age-startage==1 and se[1]+1>pc[1];why='BEFORE_CLEARER_ONE_C_N_TO_W_Y_NONDECREASE'
      else:assert cs==1 and sh==3 and age-startage==0 and pc[0]>se[0];why='BEFORE_CLEARER_ZERO_C_W_CANNOT_MOVE_RIGHT'
     elif cc==2 and age==4:
      assert hc==2 and remaining==1 and be[1]-1<goal[1];why='AFTER_BASE_ONE_C_S_TO_E_STRICTLY_BELOW_TARGET'
     elif cc==2 and age==5:
      assert hc==1 and remaining==0 and bc==0 and be[0]>goal[0];why='FINAL_E_ZERO_CONE_CANNOT_MOVE_LEFT'
     else:raise AssertionError((a,s,age,b,inp))
     cases.append(dict(predecessor=a,source=s,shadow_age_at_first_consumer=age,consumer=b,input=inp,consumer_pose=[*pc,hc],base_endpoint=be,remaining_C=remaining,reason=why))
  assert tested;counts[s]=tested
 rows.append(dict(predecessor=a,entering_pose=[*pa,ha],C_count=cc,shadow_output_slot=slots[0],shadow_goal_age=total,retirement_cases_by_source=counts))
J=dict(status='AUTHOR_UNIVERSAL_THREE_C_MARKED_NEAR_RETURN_EXCLUSION_PASS',scope='Actual complete recurrent8 factor, noninitial markedA=(0,0,N), later markedB=(0,1,E), exactly3C fromAincluded toBexcluded. Source/target packet arbitrary; no record, protected goal identity, initial origin or old-output survival premise. Such B is impossible. Rotations/translations follow.',source_packets=source_rows,target_packets=target_rows,predecessors=rows,all_retirement_cases=cases,cone_steps=cone,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,AP,Path(__file__).resolve()]})
(R/'chronology_dcuv/three_C_marked_near_return.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(source_types=len(source_rows),predecessor_types=len(rows),target_types=len(target_rows),retirement_cases=len(cases)))
