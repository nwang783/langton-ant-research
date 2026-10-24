"""A complete-boundary three-C V-left-step starts at the first or second boundary.
No first-center-contact, funding-score, path-depth or source-type hypothesis.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';PP=W/'exit_bud_halfplane_frozen_20261023_1309/manifest.json';RP=W/'atomic_common_4C_frozen_20261023_1344/manifest.json';AP=W/'atomic_exit_bud_frozen_20261023_1325/02_atomic_exit_bud_maturation.json'
G=json.loads(GP.read_text())['geometry'];HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)};C=json.loads(AP.read_text())['C_word']
def rot(z,h):x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def base(a):return 0 if a in[0,1]else 4 if a in[4,5,6]else 7
B=(-1,0);bh=1;bud=(1,-1);selected=rot(sub(bud,B),-bh);assert selected==(1,2)
queries=[];surv=[];fourC=[]
for b in[4,5,6]:
 assert list(selected)in G[b]['inputs']
 for a in IDS:
  h=(-G[a]['endpoint'][2])%4;pp=rot(G[a]['endpoint'][:2],h);p=(-pp[0],-pp[1]);o=rot(sub(bud,p),-h);assert list(o)in G[a]['outputs'];q=rot(sub(B,p),-h);dh=(bh-h)%4;n=3+G[a]['name'].count('C');key=(a,b,*q,dh,*o);ck=(mp[a],mp[b],*q,dh,*o,min(n,5));r=dict(previous_full=a,previous_pose=[*p,h],previous_output=o,target_full=b,target_relative_pose=[*q,dh],source_included_C_age=n,HB_key=key,count5_key=ck)
  if key in HB:r['reason']='SIGNED_HB'
  elif ck in COUNT:r['reason']='SIGNED_COUNT5'
  else:
   assert a in[0,6,9]
   if a in[6,9]:
    ep=add(p,rot(G[base(a)]['endpoint'][:2],h));hh=h
    # The second/last C entry follows the first C.
    ep=add(ep,rot((0,1),hh));hh=(hh-1)%4
    assert ep==B and hh==bh
    r['last_C_entry']=[*ep,hh];r['last_C_entry_clock']=-1;r['later_same_pose_clock']=3;r['forbidden_atomic_pose_return_gap']=4;r['reason']='SIGNED_ATOMIC_FOUR_C_FULL_POSE_NONRETURN';fourC.append(r)
   else:
    assert p==(-1,-1)and h==0 and b in[4,5]
    r['reason']='PLAIN_D_PREDECESSOR_MUST_BE_FACTOR_FIRST';surv.append(r)
  queries.append(r)
assert len(queries)==24 and len(surv)==2 and len(fourC)==6
# If that plain D predecessor had its own predecessor, its incoming fresh bud persists
# at target relative(0,1,E), X=0 under signed1309, but target requires the cell white.
oldP=(-1,-1);olderbud=add(oldP,(1,-1));assert olderbud==(0,-2);relB=sub(B,oldP);assert relB==(0,1)
white=[]
for b in[4,5,6]:
 z=rot(sub(olderbud,B),-bh);req={tuple(r[:2]):bool(r[2])for r in G[b]['requirements']};assert z==(2,1)and req[z]is False;white.append(dict(target_full=b,cell=olderbud,target_local=z,requirement='WHITE',P_relative_target=[*relB,bh],signed_halfplane_X=0,C_gap=3))
O=dict(status='AUTHOR_GENERAL_THREE_C_LEFT_STEP_FIRST_OR_SECOND_BOUNDARY_PASS',scope='Within one complete-eight factor, any complete marked boundaryA0,N followed afterexact3Cs by V/VC/VCC(-1,0,E) must be FIRST orSECOND packet entry; second is preceded by factor-first plainD and targetV/VC. No outgoing-source-type/first-center-contact/funding premise. First-boundary exception retained.',A_pose=[0,0,0],B_pose=[-1,0,1],predecessor_bud=bud,selected_target_input=selected,all24_previous_packet_target_tail_queries=queries,six_forbidden_four_C_atomic_returns=fourC,two_plain_D_predecessor_cases=surv,plain_D_older_bud_white_cases=white,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,PP,RP,AP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/three_C_left_step_boundary.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(dict(clauses=24,closed_four_C_cases=6,plain_D_cases=2,older_bud_white_checks=3))
