from pathlib import Path
from itertools import combinations
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();CROOT=ROOT/'core_periodicity_new';B=CROOT/'U_two_producer_unary_last_frozen_20261023_1922';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
for p,h in M['dependencies'].items():assert hashlib.sha256((CROOT/p).read_bytes()).hexdigest()==h
K={q for q,b in walk(mark)[2].items()if b};G={};IDS=(0,1,4,5,6,7,8,9);atomC=raws[1][len(raws[0]):]
for s in IDS:
 e,h,_,f=walk(raws[s]);req=walk(raws[s]+mark)[2];bl={q for q,b in req.items()if b};I=bl-K;O=(bl^f)-{e+rotation(q,h)for q in K};G[s]=dict(I=I,O=O,ctx=set(req),req=req,exit=(e,h))
def points(s,p,h):
 bs=0 if s in(0,1)else 4 if s in(4,5,6)else 7
 atoms=[raws[bs]]+[atomC]*((len(raws[s])-len(raws[bs]))//len(atomC));v=[2*p+rotation(-1-1j,h)]
 for a in atoms:
  e,hd,_,_=walk(a);p+=rotation(e,h);h=(h+hd)%4;v.append(2*p+rotation(-1-1j,h))
 return list(zip(v,v[1:]))
def det(x,y):return int(x.real*y.imag-x.imag*y.real)
def on(q,a,b):return det(q-a,b-a)==0 and (q-a).real*(q-b).real+(q-a).imag*(q-b).imag<=0
def hit(A,B):
 a,b=A;c,d=B;x=det(b-a,c-a);y=det(b-a,d-a);u=det(d-c,a-c);v=det(d-c,b-c)
 return(x*y<0 and u*v<0)or any(on(q,*s)for q,s in[(a,B),(b,B),(c,A),(d,A)])
def O(s,p,h):return{p+rotation(z,h):z for z in G[s]['O']}
def ctx(s,p,h):return{p+rotation(z,h)for z in G[s]['ctx']}
def end(s,p,h):e,hd=G[s]['exit'];return p+rotation(e,h),(h+hd)%4
F=G[7]['I'];a=-1+1j;q=-1+2j;b=-1+4j;c=2j;d=3j;sources=[]
for s in IDS:
 for h in range(4):
  poses={t-rotation(o,h)for t in F for o in G[s]['O']}
  for p in poses:
   if(sum(xy(p))+h)%2:continue
   os=O(s,p,h)
   for chosen in combinations(sorted(F&os.keys(),key=xy),3):sources.append((s,p,h,os,set(chosen)))
assert len(sources)==132;rows=[];latest3=[];whitepairs=[{a,b},{a,d},{q,b},{q,d}];goal=points(7,0j,0)
for s,p,h,os,chosen in sources:
 if s==1:
  assert(p,h)==(-3+1j,0)and q not in chosen and G[1]['req'][q-p]==False
  latest3.append((xy(p),h,sorted(map(xy,chosen))))
 missing=F-chosen
 for dh in range(4):
  poses={t-rotation(o,dh)for t in missing for o in G[1]['O']}
  for dp in poses:
   if(sum(xy(dp))+dh)%2 or not missing<=O(1,dp,dh).keys():continue
   if ctx(1,dp,dh)&chosen:reason='context'
   elif any(hit(A,B)for A in points(s,p,h)for B in points(1,dp,dh)):
    assert end(s,p,h)!=(dp,dh);reason='source_DC_contact'
   elif any(hit(A,B)for A in points(s,p,h)for B in goal):reason='source_goal_contact'
   elif any(hit(A,B)for A in points(1,dp,dh)for B in goal):
    assert end(1,dp,dh)!=(0j,0);reason='DC_goal_contact'
   elif -1+3j in os and any(pair<=chosen for pair in whitepairs):reason='white_shadow'
   elif s in(7,8,9)and(p,h)==(-1+1j,0)and chosen=={a,q,c}:reason='d_lock'
   elif s in(7,8,9)and(p,h)==(-1+4j,1)and chosen=={b,c,d}:reason='q_lock'
   elif s in(7,8,9)and any(os[t]in{2+0j,2+1j}for t in chosen&{b,c,d}):reason='east_upper'
   elif s in(7,8,9)and(p,h)==(2j,2)and chosen=={a,q,c}:reason='west_shadow'
   else:raise AssertionError((s,p,h,chosen,dp,dh))
   rows.append(dict(source=s,pose=(*xy(p),h),triple=sorted(map(xy,chosen)),DC=(*xy(dp),dh),reason=reason))
counts=Counter(r['reason']for r in rows);assert counts==dict(context=108,source_DC_contact=18,source_goal_contact=27,white_shadow=12,d_lock=4,q_lock=3,east_upper=3,west_shadow=6)
assert len(rows)==181 and len(latest3)==4 and len(G[0]['O'])==1
out=dict(status='PASS independent all two-producer/latest-D-or-DC configurations',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),source_triples=len(sources),pair_configurations=len(rows),counts=dict(counts),rows=rows,latest_DC_three=latest3,scope='Actual SIMPLE-center retained-eight factor, exactly2 genuine earlier producers. Latest unary producer excluded; entry IDs are not one producer, multiple producers can share a historical component. No general3-producer, U merger or fuel bound.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
