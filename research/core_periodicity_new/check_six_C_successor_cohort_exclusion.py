"""The first successor's output(0,0) blocks the sole six-C first-contact gate.
Actual complete successor and consumers; exact shifted positions, ordinary clocks,
earlier CLOSED contact, and zero/one-C endpoint semigroups. No path search.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json';HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
SP=W/'six_C_successor_frozen_20261023_1505/manifest.json';RP=W/'six_C_contact_frozen_20261023_1454/manifest.json'
G=json.loads(GP.read_text())['geometry'];HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)}
def rot(z,h):
 x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def base(b):return 0 if b in[0,1]else 4 if b in[4,5,6]else 7
STEPS={0:(2,2),4:(2,6),7:(0,8)}
def touch_original_U(b,p,h):
 # Twice the original U chord is c=(-1,-1), d=(0,8).
 # The consumer BASE occurs strictly after the first successor, hence is nonadjacent.
 c=(-1,-1);d=(0,8);e=rot(STEPS[base(b)],h);z=sub(add((2*p[0],2*p[1]),rot(c,h)),c);dd=det(d,e)
 if dd:
  ss=F(det(z,e),dd);tt=F(det(z,d),dd)
  return 0<=ss<=1 and 0<=tt<=1,dict(source_parameter=str(ss),consumer_parameter=str(tt))
 overlap=det(z,d)==0 and all(max(min(c[k],c[k]+d[k]),min(c[k]+z[k],c[k]+z[k]+e[k]))<=min(max(c[k],c[k]+d[k]),max(c[k]+z[k],c[k]+z[k]+e[k]))for k in[0,1])
 return overlap,dict(parallel=True,collinear=det(z,d)==0)
def zero_run(p,t,h):
 dx,dy=rot(sub(t,p),-h)
 return dx>=0 and dy>=0 and any(dy-dx-2*v>=0 and(dy-dx-2*v)%4==0 for v in range(dx+1))
def one_W_S(p,t):
 # Pre-C W and post-C S D/V/U runs, with the C center-corrected/head step(0,1,W).
 # Head displacement is dx=-dW-3vW-4uW-dS-vS-1,
 # dy=dW+vW-dS-3vS-4uS. X bounds the five counts; solve uS exactly.
 dx,dy=sub(t,p);B=-dx-1
 if B<0:return False
 for dw in range(B+1):
  for vw in range((B-dw)//3+1):
   for uw in range((B-dw-3*vw)//4+1):
    for ds in range(B-dw-3*vw-4*uw+1):
     vs=B-dw-3*vw-4*uw-ds;z=dw+vw-ds-3*vs-dy
     if z>=0 and z%4==0:return True
 return False
S=(0,4);B=(0,4);bh=2;q=(0,4);target_local=rot(sub(q,B),-bh)
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
assert target_local==(0,0)and target_local in K
assert {tuple(t[:2]):bool(t[2])for t in G[4]['requirements']}[target_local]is True
queries=[];cases=[]
for src in[4,5,6,7,8,9]:
 cs=G[src]['name'].count('C');assert[0,0]in G[src]['outputs']
 before=len(queries);openrows=[];timely_noncontact=[]
 for n in range(7):
  h=(-n)%4
  for b in IDS:
   cb=G[b]['name'].count('C')
   for inp in G[b]['inputs']:
    p=sub(q,rot(inp,h));rel=sub(p,S);key=(src,b,*rel,h,0,0);ck=(mp[src],mp[b],*rel,h,0,0,min(n,5))
    row=dict(successor_full=src,successor_C_count=cs,successor_pose=[*S,0],fresh_full_output=[0,0],global_output=q,consumer_full=b,consumer_C_count=cb,consumer_pose=[*p,h],consumer_input=inp,source_included_C_age=n,HB_key=key,count5_key=ck)
    if n<cs:why='BEFORE_SUCCESSOR_FULL_EXIT'
    elif(sum(p)+h)%2:why='SECTOR'
    elif key in HB:why='SIGNED_HB'
    elif ck in COUNT:why='SIGNED_COUNT5'
    else:
     contact,witness=touch_original_U(b,p,h)
     if contact:why='EARLIER_NONADJACENT_CLOSED_CONTACT_WITH_ORIGINAL_U';row['contact_witness']=witness
     elif n+cb>6:why='CONSUMER_FULL_TAIL_ENDS_AFTER_TARGET_FULL_ENTRY'
     else:
      ep=add(p,rot(G[base(b)]['endpoint'][:2],h));row['consumer_BASE_exit']=[*ep,h];timely_noncontact.append(row)
      if n==6 and not zero_run(ep,B,2):
       assert ep==(0,2)
       why='EXACT_ZERO_C_ENDPOINT_CONE_IMPOSSIBLE'
      elif n==5 and not one_W_S(ep,B):
       assert ep in[(0,5),(-2,5)]
       why='EXACT_ONE_C_W_TO_S_ENDPOINT_CONE_IMPOSSIBLE'
      else:why='OPEN';openrows.append(row)
    row['reason']=why;queries.append(row)
 assert not openrows
 counts=Counter(r['reason']for r in queries[before:]);cases.append(dict(successor_full=src,successor_full_output=[0,0],forced_goal_core_cell=q,query_count=len(queries)-before,query_counts=dict(counts),timely_noncontact_candidates_before_endpoint_test=timely_noncontact,status='NO_TIMELY_NONCONTACT_RETIREMENT'))
assert len(queries)==966 and len(cases)==6
O=dict(status='AUTHOR_SIX_C_FIRST_CONTACT_COMPLETELY_EXCLUDED_BY_SUCCESSOR_COHORT_PASS',scope='Actual complete-eight factor. The sole remaining canonical six-C FIRST center contact, plainU0,N to V(0,4,S), is impossible: signed first-successor reduction forces successor V/U base at(0,4,N), whose fresh output(0,0) global(0,4) must retire before goalcore; all966 first-consumer cases exclude timely noncontact retirement. First-contact only, not all six-C pose transfers, global selfavoidance, V1/U1 or capture.',original_U_pose=[0,0,0],original_U_center_chord_twice=[[-1,-1],[-1,7]],successor_pose=[0,4,0],target_V_pose=[0,4,2],target_entry_C_clock=6,fresh_successor_output_global=q,target_local_role='CORE_0_0',successor_cases=cases,all966_first_consumer_queries=queries,counts=dict(queries=len(queries),successor_cases=len(cases),query_reasons=dict(Counter(r['reason']for r in queries))),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,SP,RP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/six_C_successor_cohort_exclusion.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(O['counts']);print([(c['successor_full'],c['query_counts'])for c in cases])
