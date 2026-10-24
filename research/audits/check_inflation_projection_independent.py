import itertools,json
from collections import Counter
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
def tr(w):
 p=(0,0);h=0;reads=[];last={};good=True
 for a in w:
  reads.append(p)
  if last.get(p)==a:good=False
  last[p]=a;h=(h+(1 if a=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return reads,p,h,good
images=[]
for z in itertools.product('RL',repeat=9):
 w=''.join(z);r,p,h,g=tr(w)
 if g and (p,h) in [((3,0),1),((-3,0),3)]:images.append((w,r,'R' if h==1 else 'L'))
assert len(images)==18
project=lambda p:((p[0]+1)//3,(p[1]+1)//3)
def odd(seq):return {p for p,n in Counter(seq).items() if n%2}
exception={}
for w,r,c in images:
 error=odd(map(project,odd(r)))^{(0,0)}
 if error:
  a=min(x for x,y in error);b=min(y for x,y in error);assert error=={(a,b),(a+1,b),(a,b+1),(a+1,b+1)};exception[w]=(a,b)
assert exception=={'RRLRRRRLR':(0,-1),'RLRLLLLRL':(0,0),'LRLRRRRLR':(-1,0),'LLRLLLLRL':(-1,-1)}
reads=tr('RRLRRRRLR'+'RLRLLLLRL')[0];assert odd(map(project,odd(reads)))=={(0,-1),(1,0),(2,-1),(2,0)}
weights={'RRRLRRLRL':1,'RRLRRRRLR':3,'RLRRLRRRR':1,'LLLRLLRLR':2,'RLLLLRLLR':1,'LRRLRRLRL':3}
def mul(a,b):
 p=0
 for k in range(2):
  if b>>k&1:p^=a<<k
 if p&4:p^=7
 return p
v={(a,b):0 for a in (-1,0,1) for b in (-1,0,1)}
for w,weight in weights.items():
 assert any(w==s for s,r,c in images)
 for p in odd(tr(w)[0]):
  q=project(p);res=(p[0]-3*q[0],p[1]-3*q[1]);v[res]^=mul(weight,(1,2,3)[sum(q)%3])
assert not any(v.values());rhs=0
for b in weights.values():rhs^=b
assert rhs==3
intersection=set(images[0][1])
for w,r,c in images:intersection&=set(r)
assert intersection=={(0,0)}
assert {(c,w[0]) for w,r,c in images}==set(itertools.product('RL',repeat=2))
out={'status':'independent literal inventory and F4 verification passed','images':18,'exceptional_plaquettes':exception,'F4_weighted_coefficients':{str(k):a for k,a in v.items()},'F4_right_side':rhs,'common_read_intersection':[[0,0]],'scope':'Auxiliary board/read projection obstructions only; no k9 inflation exclusion.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
