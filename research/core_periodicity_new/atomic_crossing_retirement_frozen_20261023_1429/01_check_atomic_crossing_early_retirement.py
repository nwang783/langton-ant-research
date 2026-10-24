"""Early source-cohort retirement cannot be hidden before V/U proper crossings.
Exact ages<=5 from signed full-producer clauses; no path enumeration/cap.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';XP=W/'atomic_crossing_contexts_frozen_20261023_1414/02_atomic_center_crossing_contexts.json';HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
G=json.loads(GP.read_text())['geometry'];X=json.loads(XP.read_text());HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)}
def rot(z,h):x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def base(b):return 'D'if b in[0,1]else'V'if b in[4,5,6]else'U'
def zero_reach(p,t,h):
 dx,dy=rot(sub(t,p),-h)
 return dx>=0 and dy>=0 and any(dy-dx-2*v>=0 and(dy-dx-2*v)%4==0 for v in range(dx+1))
def closed_contact(S,b,p,h):
 d=X['atoms'][S]['center_step_twice'];e=rot(X['atoms'][base(b)]['center_step_twice'],h);c0=(-1,-1);z=sub(add((2*p[0],2*p[1]),rot(c0,h)),c0);dd=det(d,e)
 if dd:
  t=Fraction(det(z,e),dd);u=Fraction(det(z,d),dd);return 0<=t<=1 and 0<=u<=1
 if det(z,d):return False
 return all(max(min(c0[k],c0[k]+d[k]),min(c0[k]+z[k],c0[k]+z[k]+e[k]))<=min(max(c0[k],c0[k]+d[k]),max(c0[k]+z[k],c0[k]+z[k]+e[k]))for k in[0,1])
queries=[];cases=[]
for ci,cross in enumerate(X['crossings']):
 S=cross['first_atom']
 if S not in['V','U']:continue
 bx,by,bh=cross['later_pose'];N={1:3,3:5}[bh];producers=[4,5,6]if S=='V'else[7,8,9];slot_options=[]
 for o0 in cross['strict_prior_retirement_outputs']:
  o=tuple(o0);options=[]
  for s in producers:
   assert list(o)in G[s]['outputs']
   for n in range(N+1):
    h=(-n)%4
    for b in IDS:
     cb=G[b]['name'].count('C')
     for inp in G[b]['inputs']:
      p=sub(o,rot(inp,h));key=(s,b,*p,h,*o);ck=(mp[s],mp[b],*p,h,*o,min(n,5));q=dict(source_full=s,source_atom=S,source_output=o,consumer_full=b,input=inp,consumer_pose=[*p,h],full_source_age=n,HB_key=key,count5_key=ck,crossing_index=ci,crossing_clock=N)
      if n<G[s]['name'].count('C'):reason='BEFORE_SOURCE_FULL_EXIT'
      elif(sum(p)+h)%2:reason='SECTOR'
      elif key in HB:reason='SIGNED_HB'
      elif ck in COUNT:reason='SIGNED_COUNT5'
      elif closed_contact(S,b,p,h):reason='EARLIER_CLOSED_CHORD_CONTACT'
      elif cross['later_atom']!='C'and n+cb>N:reason='CONSUMER_TAIL_ENDS_AFTER_LATER_BASE'
      else:
       e=rot(G[b]['endpoint'][:2],h);end=add(p,e);eh=(h+G[b]['endpoint'][2])%4;q['full_exit']=[*end,eh]
       if n+cb==N and eh==bh and not zero_reach(end,(bx,by),bh):reason='ZERO_C_TO_CROSSING_IMPOSSIBLE'
       else:reason='UNRESOLVED_NONCONTACT_RETIRER';options.append(q)
      q['reason']=reason;queries.append(q)
  slot_options.append(dict(source_output=o,possible_noncontact_retirements=options))
 hard=[r['source_output']for r in slot_options if not r['possible_noncontact_retirements']]
 result=dict(crossing_index=ci,source_atom=S,later_atom=cross['later_atom'],later_pose=cross['later_pose'],entry_C_gap=N,forced_slot_options=slot_options,hard_slots=hard)
 assert hard,result
 result['proof']='SINGLE_SLOT_FORCES_EARLIER_CONTACT'
 cases.append(result)
assert len(cases)==38 and all(r['entry_C_gap']in[3,5]for r in cases)
assert Counter(r['proof']for r in cases)=={'SINGLE_SLOT_FORCES_EARLIER_CONTACT':38}
assert all(q['full_source_age']>=3 for q in queries if q['reason']=='EARLIER_CLOSED_CHORD_CONTACT')
assert sum(r['entry_C_gap']==3 for r in cases)==19
O=dict(status='AUTHOR_V_U_EARLY_PROPER_CROSSING_IMPLIES_PRIOR_CONTACT_PASS',scope='If first atom V/U at0,N and a later proper crossing has entry C gap3(E) or5(W), there was an EARLIER nonadjacent CLOSED center-chord contact with the first chord. Exact source-full clocks0..5 and all tails retained. No global first-contact angle bound, endpoint-case exclusion, arbitrary-gap prohibition, fuel or capture theorem.',cases=cases,queries=queries,counts=dict(cases=len(cases),queries=len(queries),by_proof=dict(Counter(r['proof']for r in cases)),query_reasons=dict(Counter(q['reason']for q in queries))),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,XP,HP,CP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/atomic_crossing_early_retirement.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(O['counts'])
