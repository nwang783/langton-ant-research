"""Independent literal geometry for the adaptive k9, a=3 record lemma."""
from pathlib import Path
from itertools import product
import json
R=Path(__file__).resolve().parents[1];D=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q
 for _ in range(h%4):x,y=y,-x
 return x,y
def tr(w,h=0):
 p=(0,0);last={};v=[];good=True
 for c in w:
  if last.get(p)==c:good=False
  last[p]=c;v.append((p,c));h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return v,p,h,good
images={'R':[],'L':[]}
for bits in product('RL',repeat=9):
 w=''.join(bits);v,p,h,good=tr(w)
 if good and (p,h)==((3,0),1):images['R'].append(w)
 if good and (p,h)==((-3,0),3):images['L'].append(w)
assert [len(images[c]) for c in 'RL']==[9,9]
def owners(q):
 out=set()
 for c in 'RL':
  for w in images[c]:
   for h in range(4):
    for z,_ in tr(w)[0]:
     z=rot(z,h);a,b=q[0]-z[0],q[1]-z[1]
     if a%3==b%3==0:
      x,y=a//3,b//3
      if (x+y+h)%2==0:out.add((x,y,h))
 return out
survivors=[];protected=[]
for a,b in product(images['R'],repeat=2):
 v,p,h,good=tr(a+b)
 if not good:continue
 first={}
 for q,c in v:first.setdefault(q,c)
 ws=[]
 for q,c in first.items():
  if c=='L':
   own=owners(q);assert own
   if all(y>=0 for x,y,h in own):ws.append(q)
 if ws:protected.append([a,b,ws])
 else:survivors.append([a,b])
expected=[['RRLRRRRLR','RLRLLLLRL'],['LLLRLLRLR','RLRRLRRRR'],['LLLRLLRLR','RLRLLLLRL'],['LLLLRRLLR','RLRRLRRRR'],['LLLLRRLLR','RLRLLLLRL']]
assert set(map(tuple,survivors))==set(map(tuple,expected))
top=[]
for c in 'RL':
 for w in images[c]:
  for h in range(4):
   v=[(rot(q,h),a) for q,a in tr(w)[0]]
   assert max(q[1] for q,a in v)<=3
   hits=[(q[0],a) for q,a in v if q[1]==3]
   if hits:
    assert (h+(1 if c=='R' else -1))%4==0
    assert hits in [[(0,'L'),(-1,'L')],[(0,'R'),(1,'R')]]
    top.append([c,w,h,hits])
assert len(top)==4
for w in ('LLLRLLRLR','LLLLRRLLR'):
 first={}
 for q,c in tr(w)[0]:first.setdefault(q,c)
 assert first[(0,0)]==first[(-1,0)]=='L'
assert expected[0][0][0]=='R'
out={'status':'independent finite ingredients pass; analytic record proof reviewed','images':images,'surviving_pairs':survivors,'forward_excluded_pairs':len(protected),'top_reachers':top,'forced_pair':expected[0],'scope':'For any finite-seed pure p(9n)=3p(n), h(9n)=h(n) trace, sufficiently high north records satisfy tau(3Y)=9*tau(Y) and the displayed pair at scaled time. This is a necessary condition, not exclusion.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
