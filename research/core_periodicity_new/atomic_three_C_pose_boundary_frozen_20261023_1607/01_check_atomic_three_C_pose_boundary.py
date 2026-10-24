"""Any actual atomic three-C left-step has entry-clock-zero boundary source.
D target: a protected incoming bud shields a second fresh predecessor output.
V target: signed1530. U/C targets: source common-output persistence.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json';HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';AP=W/'atomic_exit_bud_frozen_20261023_1325/02_atomic_exit_bud_maturation.json';PP=W/'atomic_predecessor_halfplanes_frozen_20261023_1505/manifest.json';VP=W/'atomic_three_C_left_boundary_frozen_20261023_1530/manifest.json';RP=W/'atomic_common_4C_frozen_20261023_1344/02_atomic_common_output_four_C.json';MP=W/'chronology_dcuv/counted_input_age_rules_complete.json'
G=json.loads(GP.read_text())['geometry'];HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};ROLES=json.loads(AP.read_text())['roles'];COMMON=json.loads(RP.read_text());MINS={(a,x,y):n for a,x,y,n in json.loads(MP.read_text())};IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)}
def rot(z,h):
 x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def base(b):return 0 if b in[0,1]else 4 if b in[4,5,6]else 7
T=(-1,0);th=1;r=(1,-1);q=(-1,-2)
assert rot(sub(q,T),-th)==(2,0)
assert {tuple(x[:2]):bool(x[2])for x in G[0]['requirements']}[(2,0)]is False
assert rot(sub(r,T),-th)==(1,2) # The protected incoming bud, missed by target D.
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
def one_SE(p,t):return one_WS(rot(p,1),rot(t,1))
rows=[];cases=[];Droles=[]
for ri,R in enumerate(ROLES):
 P=R['full_producer'];j=R['atomic_prefix_C'];ex=R['atomic_exit'];cp=G[P]['name'].count('C');ph=(-ex[2])%4;v=rot(ex[:2],ph);pp=(-v[0],-v[1]);lastD=j==0 and P in[0,1]
 assert add(pp,rot(ex[:2],ph))==(0,0)and(ph+ex[2])%4==0
 if lastD:Droles.append(dict(role=R,preceding_atom='D',previous_full_pose=[*pp,ph]));continue
 ol=rot(sub(q,pp),-ph);assert list(ol)in G[P]['outputs'];assert rot(sub(r,pp),-ph)==tuple(R['bud_full_output_slot'])
 if j==0:
  previous_atom='V'if P in[4,5,6]else'U';assert ol==((0,1)if previous_atom=='V'else(-1,2))
 else:
  previous_atom='C';bb=base(P);cc=tuple(G[bb]['endpoint'][:2]);ch=0
  for zz in range(j-1):cc=add(cc,rot((0,1),ch));ch=(ch-1)%4
  assert add(cc,rot((2,0),ch))==ol
 begin=len(rows);openrows=[];timely=[]
 for n in range(4):
  h=(-n)%4
  for b in IDS:
   cb=G[b]['name'].count('C')
   for inp in G[b]['inputs']:
    p=sub(q,rot(inp,h));rel=rot(sub(p,pp),-ph);dh=(h-ph)%4;k=(P,b,*rel,dh,*ol);ck=(mp[P],mp[b],*rel,dh,*ol,min(j+n,5))
    row=dict(incoming_role_index=ri,full_producer=P,producer_atomic_exit_C=j,producer_full_C=cp,producer_pose=[*pp,ph],fresh_q_full_output=ol,source_included_C_age=j+n,C_after_A=n,consumer_full=b,consumer_pose=[*p,h],consumer_input=inp,HB_key=k,count5_key=ck)
    if n<cp-j:why='CONSUMER_BEFORE_CONTAINING_FULL_SOURCE_EXIT'
    elif(sum(p)+h)%2:why='SECTOR'
    elif k in HB:why='SIGNED_HB'
    elif ck in COUNT:why='SIGNED_COUNT5'
    else:
     localr=rot(sub(r,p),-h);req={tuple(x[:2]):bool(x[2])for x in G[b]['requirements']}
     if localr in req:why='PROTECTED_INCOMING_BUD_IN_COMPLETE_CONSUMER_CONTEXT';row['protected_bud_consumer_local']=localr
     elif n+cb>3:why='CONSUMER_FULL_TAIL_ENDS_AFTER_D_TARGET_FULL_ENTRY'
     else:
      ep=add(p,rot(G[base(b)]['endpoint'][:2],h));row['consumer_BASE_exit']=[*ep,h];timely.append(row)
      if n==3 and not zero(ep,T,1):why='EXACT_ZERO_C_E_ENDPOINT_CONE_IMPOSSIBLE'
      elif n==2 and not one_SE(ep,T):why='EXACT_ONE_C_S_TO_E_ENDPOINT_CONE_IMPOSSIBLE'
      else:why='OPEN';openrows.append(row)
    row['reason']=why;rows.append(row)
 assert not openrows
 cases.append(dict(incoming_role_index=ri,role=R,fresh_q_full_output=ol,previous_atom=previous_atom,previous_atom_fresh_q_slot=(2,0)if previous_atom=='C'else ol,queries=len(rows)-begin,query_counts=dict(Counter(x['reason']for x in rows[begin:])),timely_main_avoiding_candidates_before_endpoint_test=timely,status='NO_FRESH_Q_RETIREMENT_BEFORE_TARGET_D'))
assert len(rows)==1196 and len(cases)==13 and len(Droles)==2
# If the preceding atom D is itself noninitial, its incoming older bud stays current
# at target relative(0,1,E), but the D target requires it WHITE local(2,1).
P0=(-1,-1);old=(0,-2);assert sub(T,P0)==(0,1)
assert rot(sub(old,T),-1)==(2,1)
for b in[0,1]:assert {tuple(x[:2]):bool(x[2])for x in G[b]['requirements']}[(2,1)]is False
# Source atomic common(2,0) persists to any3C E target with X=-1: its minimum
# atomic age3 and the signed E consuming-base endpoints x>=2 prevent strict retirement.
t=(2,0);tl=rot(sub(t,T),-1);assert tl==(0,3)
Eends=[z for z in COMMON['all16_retiring_base_endpoints']if z['heading']==1];assert len(Eends)==8 and all(z['end'][0]>=2 for z in Eends)
Uproof=[]
for R in COMMON['all15_atomic_source_roles']:
 j=R['atomic_birth_clock_shift'];assert j in[0,1];fullage=3+j;assert fullage<5
 for b in[7,8,9]:
  a=R['full_source'];A=tuple(R['atomic_start'][:2]);ah=R['atomic_start'][2];B=add(A,rot(T,ah));bh=(ah+1)%4;os=tuple(R['full_source_output'])
  assert add(B,rot((0,3),bh))==os
  ck=(mp[a],mp[b],*B,bh,*os,fullage);assert ck in COUNT
  Uproof.append(dict(source_role=R,target_full=b,target_input=[0,3],actual_full_source_C_age=fullage,signed_input_minimum=5,count5_key=ck,reason='SIGNED_KV_PRODUCED_UPPER_AGE_TOO_YOUNG'))
Creq={tuple(x[:2]):bool(x[2])for x in COMMON['literal_C'].get('entry_requirements',[]) }if'entry_requirements'in COMMON['literal_C']else{tuple(x[:2]):bool(x[2])for x in json.loads(AP.read_text())['C_entry_requirements']}
assert Creq[tl]is False and COMMON['literal_C']['residual_inputs']==[]
O=dict(status='AUTHOR_UNIVERSAL_ATOMIC_THREE_C_LEFT_POSE_BOUNDARY_PASS',scope='Any two actual atomic ENTRY cuts A0,N and B(-1,0,E) separated by3Cs inside one complete8 factor. B cannot be U or C. If B is D/V, A has factor-entry C clock, exactly first complete entry, second entry after factor-first plainD, or firstC inside factor-firstDC. The D-target part is new simultaneous predecessor-cohort shielding; V-target reuses signed1530. No first-contact/funding/outgoing-A-type premise; not arbitrary atomic words, all other gaps or capture.',A_pose=[0,0,0],B_pose=[*T,th],protected_incoming_bud=r,other_incoming_nonD_atom_output=q,all13_nonD_incoming_roles=cases,all1196_q_first_consumer_queries=rows,two_D_incoming_roles=Droles,older_D_bud=dict(previous_D_pose=[*P0,0],older_bud=old,target_local=[2,1],target_requirement='WHITE',relative_target=[0,1,1],C_gap=3),U_target45_minimum_age_cases=Uproof,C_target_current_common_output_white=dict(cell=t,target_local=tl,requirement='WHITE',C_residual_inputs=[]),common_source_E_base_endpoints=Eends,counts=dict(nonD_roles=13,queries=len(rows),query_reasons=dict(Counter(x['reason']for x in rows)),U_cases=len(Uproof)),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,AP,PP,VP,RP,MP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/atomic_three_C_pose_boundary.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(O['counts'])
