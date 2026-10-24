"""Exact one-parameter incidence-arrangement certificate, including an infinite tail.
No bounded simulation alone is promoted: the arrangement bound is proved in
README.md. All integer arithmetic below is exact.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm,floor,ceil
import json,hashlib,time
from probe_continuation import initial,D
P=Path(__file__).resolve().parent
words=json.loads((P/'family_words.json').read_text())
# Family: cell = a*n+b+v*j, 0<=j<count_a*n+count_b; None means infinite.
# The block/phase labels fix chronology.
def family(a,b,v,c,block,phase):return (tuple(a),tuple(b),tuple(v),c,block,phase)
def block(w,a,b,h,v,c,k):
 x,y=b;hh=h;out=[]
 for t,ch in enumerate(w):
  out.append(family(a,(x,y),v,c,k,t));hh=(hh+(1 if ch=='R'else-1))%4;dx,dy=D[hh];x+=dx;y+=dy
 if v!=(0,0):assert (x-b[0],y-b[1],hh)==(v[0],v[1],h)
 return out,(x,y,hh)
reads=[]
for args in [('RL',(0,0),(0,0),0,(1,1),(1,0),0),
 (words['P'],(1,1),(0,0),0,(0,0),(0,1),1),
 (words['V'],(1,1),(-8,-6),0,(-1,-1),(1,-9),2),
 (words['C'],(0,0),(1,3),0,(0,0),(0,1),3),
 (words['W'],(0,0),(-2,2),2,(-1,1),(1,0),4),
 (words['D'],(-1,1),(-2,2),2,(0,0),(0,1),5),
 (words['H'],(-1,1),(-13,6),3,(-2,-2),None,6)]:
 rr,end=block(*args);reads+=rr
 expected=[(1,1,0),(-8,-6,0),(-9,-7,0),(-2,2,2),(-3,3,2),(-13,6,3),(-15,4,3)][args[-1]]
 assert end==expected,(args[-1],end,expected)
cap=initial(1)
sources=[family((0,0),q,(0,0),(0,1),-1,0)for q in cap]
# Seven arms at j_original=2..n, reindexed j=0..n-2.
for v,c in [((1,-1),(0,0)),((1,1),(0,-1)),((1,1),(-1,0)),((-1,-1),(-2,1)),((-1,1),(-2,0)),((-1,-1),(-1,0)),((1,-1),(-2,0))]:
 sources.append(family((0,0),(2*v[0]+c[0],2*v[1]+c[1]),v,(1,-1),-1,0))
seed_families=list(sources)
sources+=reads
# Geometry/ordering partition only, so duplicate phase geometries may be removed.
def unique(seq):
 return list({(a,b,v,c,k):(a,b,v,c,k,t)for a,b,v,c,k,t in seq}.values())
targets=unique(reads);sources=unique(sources)
atoms=set();modulus=1
def atom(a,b,c):
 g=gcd(gcd(abs(a),abs(b)),abs(c))
 if not g:return
 a//=g;b//=g;c//=g
 if next(v for v in(a,b,c)if v)!=abs(next(v for v in(a,b,c)if v)):a=-a;b=-b;c=-c
 atoms.add((a,b,c))
for ta,tb,tv,tc,tk,tt in targets:
 if tv!=(0,0):
  atom(0,1,0)
  if tc is not None:atom(-tc[0],1,-tc[1])
 for sa,sb,sv,sc,sk,st in sources:
  if sk>tk:continue
  if sv==(0,0):
   atom(ta[0]-sa[0],tv[0],tb[0]-sb[0]);atom(ta[1]-sa[1],tv[1],tb[1]-sb[1]);continue
  assert sv[0]!=0
  den=abs(sv[0]);sgn=1 if sv[0]>0 else-1;modulus=lcm(modulus,den)
  q=(sgn*(ta[0]-sa[0]),sgn*tv[0],sgn*(tb[0]-sb[0]))
  atom(*q)
  if sc is not None:atom(q[0]-den*sc[0],q[1],q[2]-den*sc[1])
  atom(den*(ta[1]-sa[1])-sv[1]*q[0],den*tv[1]-sv[1]*q[1],den*(tb[1]-sb[1])-sv[1]*q[2])
  if sk==tk and sv!=(0,0) and tv!=(0,0):atom(q[0],q[1]-den,q[2])
# Important: constant targets have j=0. Keeping j as a formal variable only
# enlarges the partition; it cannot omit a chronology case.
lines={(F(-a,b),F(-c,b))for a,b,c in atoms if b}
N=11
for a,b,c in atoms:
 if not b and a:N=max(N,floor(F(-c,a))+1)
by={}
for slope,intercept in lines:
 if slope not in by:by[slope]=[intercept,intercept]
 else:by[slope]=[min(by[slope][0],intercept),max(by[slope][1],intercept)]
slopes=sorted(by)
# Every pair of nonparallel boundaries is separated by >2M once n>=N.
for i,a in enumerate(slopes):
 for A in slopes[i+1:]:N=max(N,floor((2*modulus+by[a][1]-by[A][0])/(A-a))+1)
period=modulus
for slope in slopes:period=lcm(period,modulus*slope.denominator)
assert all((A-a)*N+by[A][0]-by[a][1]>2*modulus for i,a in enumerate(slopes)for A in slopes[i+1:])
# A j beyond every boundary, plus one full congruence period, samples the
# unbounded last arrangement region. Earlier finite blocks are fully replayed.
def horizon(n):return max(1,max(floor(a*n+b)for a,b in lines)+2*modulus+3)
def replay(n):
 H=horizon(n)
 w='RL'*n+words['P']+words['V']*(n-9)+words['C']+words['W']*n+words['D']+words['H']*H
 B=initial(n);x=y=h=0
 explicit_seed=set()
 for a,b,v,count,k,phase in seed_families:
  for j in range(count[0]*n+count[1]):explicit_seed.add((a[0]*n+b[0]+v[0]*j,a[1]*n+b[1]+v[1]*j))
 assert explicit_seed==B
 def event_positions():
  for k in range(7):
   fs=[f for f in reads if f[4]==k];count=fs[0][3];cnt=H if count is None else count[0]*n+count[1]
   for j in range(cnt):
    for a,b,v,c,kk,phase in fs:yield(a[0]*n+b[0]+v[0]*j,a[1]*n+b[1]+v[1]*j)
 positions=iter(event_positions())
 for t,c in enumerate(w):
  assert next(positions)==(x,y),(n,t,'template disagreement')
  assert ((x,y)in B)==(c=='L'),(n,t,(x,y,h),c)
  B.symmetric_difference_update({(x,y)});h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 assert next(positions,None)is None
 assert (x,y,h)==(-n-13-2*H,n+6-2*H,3)
 return dict(n=n,tail_periods=H,updates=len(w))
if __name__=='__main__':
 start=time.time();print(dict(target_families=len(targets),source_families=len(sources),atoms=len(atoms),lines=len(lines),slopes=len(slopes),stable_threshold=N,modulus=modulus,period=period),flush=True)
 cases=[replay(n)for n in range(11,N+period)]
 raw=json.loads((P.parent.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
 assert words['H'] in raw+raw
 out=dict(scope='All n>=11, complete infinite continuation',target_families=len(targets),source_families=len(sources),atoms=len(atoms),lines=len(lines),slopes=[str(s)for s in slopes],stable_threshold=N,modulus=modulus,period=period,cases=cases,word_sha256=hashlib.sha256(json.dumps(words,sort_keys=True).encode()).hexdigest(),seconds=time.time()-start)
 (P/'affine_family_certificate.json').write_text(json.dumps(out,indent=2));print('PASS',len(cases),'finite representatives,',sum(c['updates']for c in cases),'literal reads',flush=True)
