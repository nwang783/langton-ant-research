"""D-first W/gap5 proper contact has a last-clock V/U clearance gate.
Existing signed age5 relation and atomic-exit bud maturation only.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';XP=W/'atomic_crossing_contexts_frozen_20261023_1414/02_atomic_center_crossing_contexts.json';BP=W/'atomic_exit_bud_frozen_20261023_1325/manifest.json';HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
G=json.loads(GP.read_text())['geometry'];X=json.loads(XP.read_text());K=set(map(tuple,json.loads(GP.read_text())['core']));HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)}
def rot(z,h):x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def base(b):return'D'if b in[0,1]else'V'if b in[4,5,6]else'U'
def zr(p,t,h):
 dx,dy=rot(sub(t,p),-h)
 return dx>=0 and dy>=0 and any(dy-dx-2*v>=0 and(dy-dx-2*v)%4==0 for v in range(dx+1))
def touch(b,p,h):
 d=(2,2);e=rot(X['atoms'][base(b)]['center_step_twice'],h);c=(-1,-1);z=sub(add((2*p[0],2*p[1]),rot(c,h)),c);dd=det(d,e)
 if dd:return 0<=Fraction(det(z,e),dd)<=1 and 0<=Fraction(det(z,d),dd)<=1
 return det(z,d)==0 and all(max(min(c[k],c[k]+d[k]),min(c[k]+z[k],c[k]+z[k]+e[k]))<=min(max(c[k],c[k]+d[k]),max(c[k]+z[k],c[k]+z[k]+e[k]))for k in[0,1])
cross=next(r for r in X['crossings']if r['first_atom']=='D'and r['later_pose']==[1,0,3]);assert cross['later_atom']=='V'and cross['strict_prior_retirement_outputs']==[[2,0]]
rows=[];late=[];budrows=[]
for s in[0,1]:
 for n in range(6):
  h=(-n)%4
  for b in IDS:
   cb=G[b]['name'].count('C')
   for inp in G[b]['inputs']:
    p=sub((2,0),rot(inp,h));key=(s,b,*p,h,2,0);ck=(mp[s],mp[b],*p,h,2,0,n);r=dict(source_full=s,consumer_full=b,source_output=[2,0],source_age=n,consumer_pose=[*p,h],input=inp,HB_key=key,count5_key=ck)
    if n<G[s]['name'].count('C'):why='BEFORE_SOURCE_FULL_EXIT'
    elif(sum(p)+h)%2:why='SECTOR'
    elif key in HB:why='SIGNED_HB'
    elif ck in COUNT:why='SIGNED_COUNT5'
    elif touch(b,p,h):why='EARLIER_CLOSED_CONTACT'
    elif n+cb>5:why='FULL_TAIL_ENDS_AFTER_LATER_V_BASE'
    else:
     e=add(p,rot(G[b]['endpoint'][:2],h));eh=(h+G[b]['endpoint'][2])%4;r['full_exit']=[*e,eh]
     if n+cb==5 and not zr(e,(1,0),3):why='ZERO_C_RETURN_IMPOSSIBLE'
     elif n==3:
      assert b in[4,5]and p==(0,1)and h==1
      ve=add(p,rot(G[4]['endpoint'][:2],h));bud=add(ve,rot((1,-1),h));assert ve==(3,0)and bud==(2,-1)
      local=rot(sub(bud,(1,0)),-3);assert local in K and 5-n==2
      why='NEW_V_BASE_EXIT_BUD_CURRENT_IN_TARGET_CORE';r['new_atomic_bud']=list(bud);r['target_core_local']=list(local);r['post_bud_exit_C']=2;budrows.append(r)
     else:
      assert n==5 and cb==0 and b in[4,7]and e==(1,0)and eh==3
      assert(b,p)==(4,(4,-1))or(b,p)==(7,(5,0));why='LAST_CLOCK_DIRECT_PREDECESSOR_GATE';late.append(r)
    r['reason']=why;rows.append(r)
assert len(rows)==276 and len(late)==4 and len(budrows)==4
O=dict(status='AUTHOR_D_FIRST_W5_LAST_CLOCK_CLEARANCE_GATE_PASS',scope='Conditional D-base-first proper W crossing at entryCgap5 with NO earlier nonadjacent closed contact. Old source2,0 must clear atclock5 in immediately preceding V(4,-1,W) orU(5,0,W). Not realizability, first-source-only, endpoint exclusion, finite fuel or capture.',source_pose=[0,0,0],crossing_pose=[1,0,3],queries=rows,late_gates=late,age_three_shadow_rejections=budrows,counts=dict(queries=len(rows),late_gates=len(late),new_bud_rejections=len(budrows),reasons=dict(Counter(r['reason']for r in rows))),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,XP,BP,HP,CP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/D_first_W5_clearance_gate.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(O['counts'])
