"""Actual finite sharpness control for atomic three-C bud maturation."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};keep=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(keep)};word=[0,0,0,1,5,5,0,4]
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def cells(Z,p,h):return{add(p,rot(z,h))for z in Z}
need={};par=set();poses=[];p=(0,0);h=0
for a in word:
 poses.append([*p,h])
 for x,y,b,*_ in G[a]['requirements']:
  z=add(p,rot((x,y),h));r=bool(b)^(z in par);assert z not in need or need[z]==r;need[z]=r
 par^=cells(G[a]['raw_odd'],p,h);p=add(p,rot(G[a]['endpoint'][:2],h));h=(h+G[a]['endpoint'][2])%4
B={z for z,r in need.items()if r};initial=set(B);assert K<=B and len(B)==14
R={z:dict(initial=True)for z in B-K};C=0;rows=[];checks=0
for i,(a,pose)in enumerate(zip(word,poses)):
 p=tuple(pose[:2]);h=pose[2];assert B==set(R)|cells(K,p,h)and not set(R)&cells(K,p,h);ins=cells(G[a]['inputs'],p,h);ir=[]
 for z in sorted(ins):
  origin=R[z];age=None if origin.get('initial')else C-origin['C'];ir.append(dict(cell=z,age=age,origin=origin))
  if age is not None:
   rel=rot(sub(p,origin['head']),-origin['heading']);dh=(h-origin['heading'])%4;key=(origin['packet'],a,*rel,dh,*origin['slot']);ck=(mp[origin['packet']],mp[a],*rel,dh,*origin['slot'],min(5,age));assert key not in HB and ck not in COUNT;checks+=1
 for z in ins:del R[z]
 for slot in G[a]['outputs']:
  z=add(p,rot(slot,h));assert z not in R;R[z]=dict(packet=a,step=i,head=p,heading=h,slot=slot,C=C)
 xx,yy,hh=*p,h;copy=set(B);raw_exit=None
 for k,ch in enumerate(G[a]['word']+G[a]['marker']):
  z=xx,yy;black=z in copy;assert ch==('L'if black else'R'),(i,k,z)
  if black:copy.remove(z)
  else:copy.add(z)
  hh=(hh+(-1 if black else 1))%4;u,v=rot((0,1),hh);xx+=u;yy+=v
  if k+1==len(G[a]['word']):raw_exit=(xx,yy,hh,set(copy))
 xx,yy,hh,B=raw_exit;assert B==set(R)|cells(K,(xx,yy),hh)and not set(R)&cells(K,(xx,yy),hh)
 if i+1<len(word):assert[xx,yy,hh]==poses[i+1]
 rows.append(dict(packet=a,head=pose,C=C,inputs=ir,raw_exit=[xx,yy,hh]));C+=G[a]['name'].count('C')
assert rows[-1]['head']==[0,1,1]and C==3 and len(B)==35
final={tuple(r['cell']):r for r in rows[-1]['inputs']};assert set(final)=={(2,0),(3,1)}
assert final[2,0]['age']==final[3,1]['age']==3
assert final[2,0]['origin']['step']==0 and final[3,1]['origin']['step']==1
assert final[2,0]['origin']['slot']==final[3,1]['origin']['slot']==[2,0]
O=dict(status='AUTHOR_ACTUAL_THREE_C_BUD_MATURATION_SHARP_CONTROL_PASS',scope='Actual fourteen-cell finite complete-eight factor, not minimality or renewal. Final V consumes first and SECOND D exit buds at exactly3 postexitCs. Shows atomic maturation3 cannot be raised universally; no global fuel/capture claim.',word=word,initial_actual_board=sorted(initial),initial_mass=14,final_mass=len(B),raw_length=sum(len(G[a]['word'])for a in word),C_before_final_V=3,produced_HB_count_queries=checks,rows=rows,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,Path(__file__).resolve()]});(W/'chronology_dcuv/atomic_bud_three_C_sharp_control.json').write_text(json.dumps(O,indent=2)+'\n');print(json.dumps({k:v for k,v in O.items()if k not in['rows','initial_actual_board','dependencies']},indent=2))
