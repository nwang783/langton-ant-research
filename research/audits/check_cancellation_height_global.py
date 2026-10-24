"""Independent exact finite checks of the cancellation-height identities."""
import random,json
from collections import Counter
from pathlib import Path
V=[(0,1),(1,0),(0,-1),(-1,0)]
def chi(p):return 1 if (p[0]+p[1])%2==0 else -1
def advance(p,h,c):
 h=(h+(1 if c=='R' else -1))%4;dx,dy=V[h];return (p[0]+dx,p[1]+dy),h

def dep(w,p=(0,0),h=0):
 sig=chi(p)*(1 if h%2==0 else -1);d=Counter()
 for c in w:
  d[p]+=-sig*chi(p)*(1 if c=='R' else -1);p,h=advance(p,h,c)
 return {p:v for p,v in d.items() if v},p,h

def mixed(K):
 d=Counter()
 for (x,y),n in K.items():
  for dx,dy,sg in [(0,0,1),(1,0,-1),(0,1,-1),(1,1,1)]:d[x+dx,y+dy]+=sg*n
 return {p:v for p,v in d.items()if v}

def add(*ds):
 c=Counter()
 for d in ds:
  for p,v in d.items():c[p]+=v
 return {p:v for p,v in c.items()if v}

def stack(w,p=(0,0),h=0,check_each=False):
 letters=[];poses=[(p,h)];K=Counter();old=Counter()
 for c in w:
  pp,hh=poses[-1];letters.append(c);poses.append(advance(pp,hh,c))
  if len(letters)>=4 and letters[-4:]==[c]*4:
   cyc=poses[-5:-1];q=min(p[0]for p,h in cyc),min(p[1]for p,h in cyc)
   assert poses[-1]==poses[-5];K[q]+=1;del letters[-4:];del poses[-4:]
  assert all(K[q]>=old[q]for q in old);old=K.copy() if check_each else old
 return ''.join(letters),dict(K)

rng=random.Random(192837);face_checks=0
for p in [(0,0),(1,0),(3,-2),(-4,7)]:
 for h in range(4):
  for a in 'RL':
   d,end,hh=dep(a*4,p,h);r,K=stack(a*4,p,h)
   assert not r and end==p and hh==h and d==mixed(K) and sum(K.values())==1;face_checks+=1

random_checks=0
for trial in range(1000):
 p=(rng.randrange(-5,6),rng.randrange(-5,6));h=rng.randrange(4);w=''.join(rng.choice('RL')for _ in range(rng.randrange(1,400)))
 r,K=stack(w,p,h);d,end,eh=dep(w,p,h);dr,re,rh=dep(r,p,h)
 assert (end,eh)==(re,rh) and d==add(dr,mixed(K));random_checks+=1
 s=rng.randrange(len(w)+1);u,v=w[:s],w[s:];_,pu,hu=dep(u,p,h)
 _,Ku=stack(u,p,h);_,Kv=stack(v,pu,hu)
 assert all(K.get(q,0)>=Ku.get(q,0)+Kv.get(q,0)for q in set(Ku)|set(Kv))

ant_checks=0
for tr in range(12):
 B=set() if tr==0 else {(x,y)for x in range(-4,5)for y in range(-4,5)if rng.random()<.3};B0=set(B);p=(0,0);h=0;w=''
 for t in range(2000):
  c='L' if p in B else 'R';B.symmetric_difference_update([p]);p,h=advance(p,h,c);w+=c
  if (t+1)%100==0:
   r,K=stack(w);dr,_,_=dep(r);lhs=add({q:-chi(q)for q in B},{q:chi(q)for q in B0})
   assert lhs==add(dr,mixed(K));mass=-sum(chi(q)*v for q,v in dr.items())-4*sum(chi(q)*v for q,v in K.items())
   assert mass==len(B)-len(B0);ant_checks+=1
out={'status':'PASS','local_face_cases':face_checks,'arbitrary_word_identities_and_split_inequalities':random_checks,'actual_ant_field_and_mass_checks':ant_checks,'scope':'Finite verification of exact identities; the unbounded theorem follows from the local deletion identity and induction.'}
print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
