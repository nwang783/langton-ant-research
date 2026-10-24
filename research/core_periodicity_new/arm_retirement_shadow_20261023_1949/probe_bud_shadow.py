import json
from fractions import Fraction
from collections import Counter
from pathlib import Path
ROOT=Path('/workspace/shared/langton/core_periodicity_new');G=json.load(open(ROOT/'chronology_dcuv/literal_residual_geometry.json'))['geometry'];IDS=(0,1,4,5,6,7,8,9);L={(0,0),(0,1),(1,0),(1,1)};t=(1,2);K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
def place(q,p,h):return add(p,rot(q,h))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and sum((p[i]-a[i])*(p[i]-b[i])for i in range(2))<=0

def touch(a,b,c,d):
 u=sub(b,a);v=sub(d,c);r=sub(c,a);z=cross(u,v)
 if z:
  s=Fraction(cross(r,v),z);v=Fraction(cross(r,u),z)
  return 0<=s<=1 and 0<=v<=1
 return any(on(p,a,b)and on(p,c,d)for p in(a,b,c,d))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def chords(a,p,h):
 out=[];base=0 if a in(0,1)else 4 if a in(4,5,6)else 7
 start=center(p,h);end=add(start,rot((2,2)if base==0 else(2,6)if base==4 else(0,8),h));out.append((start,end))
 ep=G[base]['endpoint'];p=place(ep[:2],p,h);h=(h+ep[2])%4
 for _ in range(G[a]['name'].count('C')):
  start=center(p,h);p=place((0,1),p,h);h=(h+3)%4;out.append((start,center(p,h)))
 return out

def pair_ok(source,helper):
 # Exact two-full-raw words, plus final marker; first-read consistency.
 p=(0,0);h=0;par=set();rq={};V=((0,1),(1,0),(0,-1),(-1,0))
 for ch in G[source]['word']+G[helper]['word']+G[0]['marker']:
  b=(ch=='L')^(p in par)
  if p in rq and rq[p]!=b:return False
  rq[p]=b;par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return True
for s in(7,):
 p=tuple(G[s]['endpoint'][:2]);h=G[s]['endpoint'][2]
 for a in IDS:
  if not pair_ok(s,a):print('PAIR INVALID',s,a);continue
  out={place(q,p,h)for q in G[a]['outputs']};past=chords(s,(0,0),0)+chords(a,p,h)
  for goal,pp,hh in[(0,(2,3),3),(1,(2,3),3)]:
   goalblack={place(q,pp,hh)for q in K|set(map(tuple,G[goal]['inputs']))};goalwhite={place(z[:2],pp,hh)for z in G[goal]['requirements']if not z[2]};guards=out&(goalblack|goalwhite)
   for z in sorted(guards):
    rows=[]
    for b in IDS:
     for bh in range(4):
      for inp in G[b]['inputs']:
       bp=sub(z,rot(inp,bh));ctx={place(zz[:2],bp,bh)for zz in G[b]['requirements']}
       reason='sector'if(sum(bp)+bh)%2 else'protected'if ctx&set(map(tuple,G[s]['outputs'])) else'past'if any(touch(*ch,*old)for ch in chords(b,bp,bh)for old in past+chords(goal,pp,hh))else'SURVIVE'
       rows.append((reason,b,bp,bh))
    surv=[x for x in rows if x[0]=='SURVIVE'];print('GUARD',s,a,'goal',goal,'z',z,'white',z in goalwhite,'surv',len(surv),surv,'counts',dict(Counter(x[0]for x in rows)))
