"""Seven of eight canonical six-C first-center contacts force an earlier contact.
Full-source counts plus exact zero/one-C endpoint cones; no path search.
"""
from pathlib import Path
from fractions import Fraction as F
from math import ceil,floor
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';XP=W/'atomic_crossing_contexts_frozen_20261023_1414/02_atomic_center_crossing_contexts.json';HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';FP=W/'first_center_contact_frozen_20261023_1412/manifest.json'
G=json.loads(GP.read_text())['geometry'];X=json.loads(XP.read_text());A=X['atoms'];HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)};rank={'D':2,'C':2,'V':1,'U':0}
def rot(z,h):x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def base(b):return 0 if b in[0,1]else 4 if b in[4,5,6]else 7
def namebase(b):return G[base(b)]['name']
def zr(p,t,h):
 dx,dy=rot(sub(t,p),-h)
 return dx>=0 and dy>=0 and any(dy-dx-2*v>=0 and(dy-dx-2*v)%4==0 for v in range(dx+1))
def one_W_S(p,t):
 dx,dy=sub(t,p);B=-dx-1
 if B<0:return False
 # X consumption bounds every count except post-S U; its Y count is solved exactly.
 for dW in range(B+1):
  for vW in range((B-dW)//3+1):
   for uW in range((B-dW-3*vW)//4+1):
    for dS in range(B-dW-3*vW-4*uW+1):
     vS=B-dW-3*vW-4*uW-dS;z=dW+vW-dS-3*vS-dy
     if z>=0 and z%4==0:return True
 return False
def touch(S,b,p,h):
 d=A[S]['center_step_twice'];e=rot(A[namebase(b)]['center_step_twice'],h);c=(-1,-1);z=sub(add((2*p[0],2*p[1]),rot(c,h)),c);dd=det(d,e)
 if dd:return 0<=F(det(z,e),dd)<=1 and 0<=F(det(z,d),dd)<=1
 return det(z,d)==0 and all(max(min(c[k],c[k]+d[k]),min(c[k]+z[k],c[k]+z[k]+e[k]))<=min(max(c[k],c[k]+d[k]),max(c[k]+z[k],c[k]+z[k]+e[k]))for k in[0,1])
geoms=[];boxes=[];C0=(-1,-1)
for sa,S in A.items():
 for ta,T in A.items():
  if rank[sa]>=rank[ta]:continue # Signed n6 alpha(source)<alpha(target).
  d=S['center_step_twice'];e=rot(T['center_step_twice'],2);shift=sub(C0,rot(C0,2));corners=[add(shift,sub((s*d[0],s*d[1]),(t*e[0],t*e[1])))for s in[0,1]for t in[0,1]];bounds=[(ceil(F(min(q[k]for q in corners),2)),floor(F(max(q[k]for q in corners),2)))for k in[0,1]];dd=det(d,e);assert dd
  boxes.append(dict(source_atom=sa,target_atom=ta,parallelogram_corners_twice=corners,integer_bounds=bounds))
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if(x+y+2)%2:continue
    z=sub(add((2*x,2*y),rot(C0,2)),C0);s=F(det(z,e),dd);t=F(det(z,d),dd)
    if not(0<=s<1 and 0<t<=1):continue
    req={tuple(r[:2]):bool(r[2])for r in T['requirements']};I=set(map(tuple,T['inputs']));contacts=[];forced=[]
    for o in S['outputs']:
     local=rot(sub(o,(x,y)),2)
     if local in req:
      kind='INPUT'if local in I else'CORE'if req[local]else'WHITE';contacts.append(dict(output=o,target_local=local,role=kind))
      if kind!='INPUT':forced.append(o)
    geoms.append(dict(first_atom=sa,later_atom=ta,later_pose=[x,y,2],earlier_parameter=str(s),later_parameter=str(t),source_output_contacts=contacts,forced_prior_retirement_outputs=forced))
assert len(geoms)==8 and all(g['later_parameter']=='1'for g in geoms)
queries=[];cases=[]
for gi,cross in enumerate(geoms):
 SA=cross['first_atom'];bx,by,bh=cross['later_pose'];prods=[4,5,6]if SA=='V'else[7,8,9];slotsets=[]
 for o0 in cross['forced_prior_retirement_outputs']:
  o=tuple(o0);opts=[]
  for src in prods:
   assert list(o)in G[src]['outputs']
   for n in range(7):
    h=(-n)%4
    for b in IDS:
     cb=G[b]['name'].count('C')
     for inp in G[b]['inputs']:
      p=sub(o,rot(inp,h));key=(src,b,*p,h,*o);ck=(mp[src],mp[b],*p,h,*o,min(n,5));q=dict(geometry_index=gi,source_full=src,source_output=o,consumer_full=b,consumer_pose=[*p,h],input=inp,source_age=n,HB_key=key,count5_key=ck)
      if n<G[src]['name'].count('C'):why='BEFORE_SOURCE_FULL_EXIT'
      elif(sum(p)+h)%2:why='SECTOR'
      elif key in HB:why='SIGNED_HB'
      elif ck in COUNT:why='SIGNED_COUNT5'
      elif touch(SA,b,p,h):why='EARLIER_CLOSED_CONTACT'
      elif cross['later_atom']!='C'and n+cb>6:why='FULL_TAIL_ENDS_AFTER_LATER_BASE'
      else:
       ep=add(p,rot(G[base(b)]['endpoint'][:2],h));q['consuming_BASE_exit']=[*ep,h]
       if n==6 and not zr(ep,(bx,by),2):why='ZERO_C_BASE_EXIT_TO_TARGET_IMPOSSIBLE'
       elif n==5 and not one_W_S(ep,(bx,by)):why='ONE_C_BASE_EXIT_TO_TARGET_IMPOSSIBLE'
       else:why='UNRESOLVED_NONCONTACT_CLEARER';opts.append(q)
      q['reason']=why;queries.append(q)
  slotsets.append(dict(output=o,noncontact_timely_clearers=opts))
 hard=[s['output']for s in slotsets if not s['noncontact_timely_clearers']]
 r=dict(geometry_index=gi,geometry=cross,forced_slot_tests=slotsets,hard_outputs=hard)
 if cross['forced_prior_retirement_outputs']:assert hard;r['status']='FORCES_EARLIER_CLOSED_CONTACT'
 else:
  assert SA=='U'and cross['later_atom']=='V'and cross['later_pose']==[0,4,2]
  assert{tuple(c['output'])for c in cross['source_output_contacts']}=={(-1,2),(0,1)}
  r['status']='INPUT_ONLY_REMAINING_GATE'
 cases.append(r)
assert Counter(c['status']for c in cases)=={'FORCES_EARLIER_CLOSED_CONTACT':7,'INPUT_ONLY_REMAINING_GATE':1}
# Static old-cohort eligibility in the sole remaining gate is not chronological attainment.
pair_queries=[]
for s in[7,8,9]:
 for b in[4,5,6]:
  for o in[(-1,2),(0,1)]:
   key=(s,b,0,4,2,*o);ck=(mp[s],mp[b],0,4,2,*o,5);pair_queries.append(dict(source=s,target=b,source_output=o,full_source_age=6,HB_key=key,count5_key=ck,HB_excluded=key in HB,count5_excluded=ck in COUNT))
assert sum(q['HB_excluded']for q in pair_queries)==3 and not any(q['count5_excluded']for q in pair_queries)
O=dict(status='AUTHOR_SIX_C_FIRST_CONTACT_SEVEN_OF_EIGHT_REDUCTION_PASS',scope='Canonical FIRST center contact atCgap6 reduces to U-base0,N versus V-base(0,4,S), midpoint/endpoint touch. Other7 cases force an earlier CLOSED contact. Remaining old-cohort checks are static necessary controls, not attainment. No global fuel, renewal or capture.',canonical_boxes=boxes,geometries=geoms,cases=cases,clearance_queries=queries,remaining_gate_old_cohort_queries=pair_queries,counts=dict(geometries=8,excluded=7,remaining=1,clearance_queries=len(queries),query_reasons=dict(Counter(q['reason']for q in queries))),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,XP,HP,CP,FP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/six_C_first_contact_reduction.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(O['counts'])
