from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'core_periodicity_new/active_center_edge_walk_frozen_20261023_1739';manifest=P/'manifest.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='b7d41cc3ce9b68c68943b7d7af6fbf1a448b69e434d1b833e8f0d677093ab328'
V=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
rot=lambda q,h:((q[0],q[1]),(q[1],-q[0]),(-q[0],-q[1]),(-q[1],q[0]))[h%4]
add=lambda a,b:(a[0]+b[0],a[1]+b[1]);z2=lambda p,h:add((2*p[0],2*p[1]),rot((-1,-1),h))
def edge(q,s):
 v=(1,1)if(sum(q)-s)%2==0 else(1,-1);return frozenset((add((2*q[0],2*q[1]),v),add((2*q[0],2*q[1]),(-v[0],-v[1]))))
checks=0
for px in(-2,0,1):
 for py in(-1,0,2):
  p=(px,py)
  for h in range(4):
   s=(sum(p)+h)%2;z=z2(p,h);d=rot((2,2),h)
   assert edge(p,s)==frozenset((z,add(z,d)))
   for u in edge(p,s):assert(u[0]+u[1]-2*(s+1))%4==0
   core={edge(add(p,rot(q,h)),s)for q in K};star={frozenset((z,add(z,rot((2,2),k))))for k in range(4)}
   assert core-star=={frozenset((add(z,d),add(add(z,d),rot((2,2),h+1))))}and star<=core
   for c in 'LR':
    nh=(h+(1 if c=='R'else-1))%4;np=add(p,V[nh]);assert z2(np,nh)==(add(z,d)if c=='R'else z);assert(sum(np)+nh)%2==s;checks+=1
words={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR','U':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR'};traces={}
for name,w in words.items():
 p=(0,0);h=0;first={};reads=[];rw=[z2(p,h)]
 for c in w:
  reads.append(p);first.setdefault(p,c);old=z2(p,h);e=edge(p,0);assert old in e;nh=(h+(1 if c=='R'else-1))%4;np=add(p,V[nh]);new=z2(np,nh)
  if c=='R':assert new in e and new!=old;rw.append(new)
  else:assert new==old
  p,h=np,nh
 F={q for q,c in first.items()if c=='L'};p=(0,0);h=0
 for c in w:
  assert (p in F)==(c=='L');F.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=add(p,V[h])
 rel=[((q[0]+1)//2,(q[1]+1)//2)for q in rw];traces[name]={'raw_length':len(w),'R_walk':rel,'exit':[*p,h]}
 if name=='D':assert rel==[(0,0),(1,1),(2,2),(3,1),(2,0),(1,1)]and(0,1)not in reads
out={'status':'PASS exact fine-step edge bijection and marked five-port core','manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'translated_local_checks':checks,'atomic_traces':traces,'scope':'No historical root embedding or fine-step simplicity. R adds and traverses; L deletes without moving corrected center. Even one D has an internal four-edge center loop.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
