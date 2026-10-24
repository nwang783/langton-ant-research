"""The protected main output blocks all second-cohort clearance before W5 helpers.
Closes the signed D-first W5 late-helper gate; exact finite full-source cases.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json';HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';LP=W/'D_first_W5_gate_frozen_20261023_1437/manifest.json'
G=json.loads(GP.read_text())['geometry'];HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)}
def rot(z,h):
 x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def base(b):return 0 if b in[0,1]else 4 if b in[4,5,6]else 7
STEP={0:(2,2),4:(2,6),7:(0,8)}
def contact_original_D(b,p,h):
 c=(-1,-1);d=(2,2);e=rot(STEP[base(b)],h);z=sub(add((2*p[0],2*p[1]),rot(c,h)),c);dd=det(d,e)
 if dd:
  s=F(det(z,e),dd);t=F(det(z,d),dd)
  return 0<=s<=1 and 0<=t<=1,dict(source_parameter=str(s),consumer_parameter=str(t))
 return det(z,d)==0 and all(max(min(c[k],c[k]+d[k]),min(c[k]+z[k],c[k]+z[k]+e[k]))<=min(max(c[k],c[k]+d[k]),max(c[k]+z[k],c[k]+z[k]+e[k]))for k in[0,1]),dict(parallel=True,collinear=det(z,d)==0)
def zero(p,t,h):
 x,y=rot(sub(t,p),-h)
 return x>=0 and y>=0 and any(y-x-2*v>=0 and(y-x-2*v)%4==0 for v in range(x+1))
def one_WS(p,t):
 dx,dy=sub(t,p);B=-dx-1
 if B<0:return False
 for dw in range(B+1):
  for vw in range((B-dw)//3+1):
   for uw in range((B-dw-3*vw)//4+1):
    for ds in range(B-dw-3*vw-4*uw+1):
     vs=B-dw-3*vw-4*uw-ds;z=dw+vw-ds-3*vs-dy
     if z>=0 and z%4==0:return True
 return False
def one_NW(p,t):return one_WS(rot(p,3),rot(t,3))
main=(2,0);goal=(1,0);gh=3;helpers=[(4,(4,-1)),(7,(5,0))]
# The three branches partition source fullD/DC and, after fullD, all8 successors.
branches=[]
for src in[4,5,6,7,8,9]:branches.append(dict(branch='PLAIN_D_NEXT_V_U',source_full=src,source_pose=(1,1),source_output=(0,0),global_q=(1,1),prior_retirement_reason='FINAL_CORE_AND_IMMEDIATE_HELPER_HAS_NO_Q_INPUT'))
for src in[0,1]:branches.append(dict(branch='PLAIN_D_NEXT_D_DC',source_full=src,source_pose=(1,1),source_output=(2,0),global_q=(3,1),prior_retirement_reason='Q_WHITE_IN_HELPER_CONTEXT'))
branches.append(dict(branch='SOURCE_FULL_DC',source_full=1,source_pose=(0,0),source_output=(3,1),global_q=(3,1),prior_retirement_reason='Q_WHITE_IN_HELPER_CONTEXT'))
rows=[];cases=[]
for bi,br in enumerate(branches):
 src=br['source_full'];S=br['source_pose'];q=br['global_q'];o=br['source_output'];cs=G[src]['name'].count('C');assert list(o)in G[src]['outputs']and add(S,o)==q
 for helper,goalH in helpers:
  hreq={tuple(t[:2]):bool(t[2])for t in G[helper]['requirements']};hi=set(map(tuple,G[helper]['inputs']));ql=rot(sub(q,goalH),-3);ml=rot(sub(main,goalH),-3)
  assert ml in hi and ql not in hi
  if br['branch']=='PLAIN_D_NEXT_V_U':
   # Its identity cannot be retired in the last helper; final V needs that cell CORE.
   assert rot(sub(q,goal),-gh)==(1,0)
   for goalbase in[4,7]:
    assert {tuple(t[:2]):bool(t[2])for t in G[goalbase]['requirements']}[(1,0)]is True and[1,0]not in G[goalbase]['inputs']
  else:assert ql in hreq and not hreq[ql]
  begin=len(rows);timely=[];openrows=[]
  for n in range(6):
   h=(-n)%4
   for b in IDS:
    cb=G[b]['name'].count('C')
    for inp in G[b]['inputs']:
     p=sub(q,rot(inp,h));rp=sub(p,S);key=(src,b,*rp,h,*o);ck=(mp[src],mp[b],*rp,h,*o,n)
     row=dict(branch_index=bi,branch=br['branch'],source_full=src,source_pose=[*S,0],source_output=o,global_q=q,helper_full=helper,helper_pose=[*goalH,3],source_age=n,consumer_full=b,consumer_pose=[*p,h],consumer_input=inp,HB_key=key,count5_key=ck)
     if n<cs:why='BEFORE_SOURCE_FULL_EXIT'
     elif(sum(p)+h)%2:why='SECTOR'
     elif key in HB:why='SIGNED_HB'
     elif ck in COUNT:why='SIGNED_COUNT5'
     else:
      contact,wit=contact_original_D(b,p,h)
      req={tuple(t[:2]):bool(t[2])for t in G[b]['requirements']};mainlocal=rot(sub(main,p),-h)
      if contact:why='EARLIER_NONADJACENT_CLOSED_ORIGINAL_D_CONTACT';row['contact_witness']=wit
      elif mainlocal in req:
       why='PROTECTED_MAIN_CURRENT_THROUGH_CONSUMER_COMPLETE_CONTEXT';row['main_consumer_local']=mainlocal;row['main_local_role']='TRUE_INPUT'if list(mainlocal)in G[b]['inputs']else'CORE_OR_WHITE'
      elif n+cb>5:why='CONSUMER_FULL_TAIL_FINISHES_AFTER_HELPER_ENTRY'
      else:
       ep=add(p,rot(G[base(b)]['endpoint'][:2],h));row['consumer_BASE_exit']=[*ep,h];timely.append(row)
       if n==5 and not zero(ep,goalH,3):
        assert ep[1]==2 and ep[0]<=3 and goalH[0]>=4 and goalH[1]<=0
        why='EXACT_ZERO_C_ENDPOINT_CONE_IMPOSSIBLE'
       elif n==4 and not one_NW(ep,goalH):
        assert ep==(4,4)and goalH[1]<=0
        why='EXACT_ONE_C_N_TO_W_ENDPOINT_CONE_IMPOSSIBLE'
       else:why='OPEN';openrows.append(row)
     row['reason']=why;rows.append(row)
  assert not openrows
  cases.append(dict(branch_index=bi,branch=br,helper_full=helper,helper_pose=[*goalH,3],q_helper_local=ql,main_helper_input_local=ml,query_counts=dict(Counter(r['reason']for r in rows[begin:])),timely_noncontact_main_avoiding_candidates_before_endpoint_test=timely,status='NO_Q_RETIREMENT_BEFORE_PROTECTED_MAIN_HELPER'))
assert len(rows)==2484 and len(cases)==18
O=dict(status='AUTHOR_D_W5_LATE_HELPER_HISTORY_EXCLUDED_PASS',scope='Actual complete8 factor, Dbase0,N and later Vbase(1,0,W) after5Cs with no earlier closed contact with originalD chord. Signed1437 forces last helperV/U and main2,0 current until it. Nine exhaustive source/first-successor cases each force another fresh q to retire before helper;2484 exact consumers impossible. Thus proper D/W5 FIRST contact excluded. Conditional same-helper assembly also applies to a Ubase at the same final pose if independently supplied. No arbitrary later transfers, other gaps, global fuel or capture.',main_original_D_output=main,final_pose=[*goal,gh],helpers=[dict(full=h,pose=[*p,3])for h,p in helpers],branches=branches,cases=cases,all2484_q_first_consumer_queries=rows,counts=dict(branches=9,helper_cases=18,queries=len(rows),query_reasons=dict(Counter(r['reason']for r in rows))),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,LP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/D_W5_helper_history_exclusion.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(O['counts'])
