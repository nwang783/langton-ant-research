"""Independent finite local identities used in the all-width cap proof.
The arbitrary-k classification is an analytic induction on these sweeps, not
an extrapolation from the finite examples included as regression controls.
"""
import json
from pathlib import Path
DIRS=((0,1),(1,0),(0,-1),(-1,0))
W='LLRLRRRRLRRRRLLLLRLL'
def trace(w,p=(0,0),h=1):
 out=[]
 for c in w:
  out.append((p,h,c));h=(h+(1 if c=='R' else -1))%4
  d=DIRS[h];p=(p[0]+d[0],p[1]+d[1])
 return out,p,h

def run(w,initial,p=(0,0),h=1):
 toggles=set();visits=[]
 for q,hh,c in trace(w,p,h)[0]:
  bit=initial(q)
  assert bit is not None,('unguarded read',q,c)
  bit ^= q in toggles
  assert bit==(c=='L'),('mismatch',q,c,bit)
  toggles.symmetric_difference_update([q]);visits.append((q,hh,c))
 return toggles,visits

# Literal moving W20 guard. Unspecified points are not silently white.
def guard(q,p):
 x,y=p
 if y==0 and (x<=q-2 or x==q):return 1
 if y==1 and x<=q:return int(x==q)
 if y==2 and x<=q-1:return int(x==q-1)
 if y==3 and x<=q-1:return 0
 return None
mask,visits=run(W,lambda p:guard(0,p))
assert trace(W)[1:]==((-2,0),1)
for y in range(4):
 for x in range(-5,3):
  new=guard(-2,(x,y))
  if new is not None:
   old=guard(0,(x,y));assert old is not None
   assert new==(old^((x,y) in mask))
# For x<=-4 both guards have identical fixed values, and no W read has x<-3.
assert min(p[0] for p,_,_ in visits)==-3
assert all(guard(0,(-4,y))==guard(-2,(-4,y)) for y in range(4))
assert [(i,p,h) for i,(p,h,c) in enumerate(visits) if p==(0,0) and h==1]==[(0,(0,0),1)]
assert max(p[0] for p,_,_ in visits)==0

# Sweeps: entry and exit patterns are finite, translated identities.
outward={(0,1):0,(1,1):0,(1,0):1,(2,0):1}
backward={(0,1):1,(-1,1):1,(-1,0):0,(-2,0):0}
for word,patt,end in [('RRLL',outward,(2,1)),('LLRR',backward,(-2,1))]:
 _,v=run(word,patt.get,(0,1),0)
 assert trace(word,(0,1),0)[1:]==(end,0)
 assert len({p for p,_,_ in v})==4

# Finite controls independently bind all displayed formulas and exact final field.
controls=[]
for r in range(41):
 initial=lambda p,r=r: int(p[1]==0 and p[0]<r)
 if r==0:w='R';end=(0,-1);hh=2
 elif r%2==0:
  k=r//2;w='L'+'RRLL'*(k-1)+'RRLR';end=(r,-1);hh=2
 else:
  k=(r-1)//2;w='L'+'RRLL'*k+'RRRR'+'LLRR'*k+'L'+'RRRR'+'LL';end=(0,0);hh=1
 mask,v=run(w,initial)
 assert trace(w)[1:]==(end,hh)
 assert not any(p==(0,0) and h==1 for p,h,c in v[1:])
 assert max(p[0] for p,_,_ in v)<=r
 if r%2:
  assert len(w)==8*k+12
  assert max(p[1] for p,_,_ in v)==2
  for y in range(4):
   for x in range(-4,r+2):
    expected=int((y==0 and (x<=-2 or 0<=x<=r)) or (y==1 and x in (0,r)) or (y==2 and x in (-1,0)))
    assert (initial((x,y))^((x,y) in mask))==expected
  for x in range(-5,3):
   for y in range(4):
    req=guard(0,(x,y))
    if req is not None:assert req==(initial((x,y))^((x,y) in mask))
 controls.append({'gap':r,'length':len(w),'endpoint':[list(end),hh]})
result={'status':'PASS','local_identities':['east RRLL sweep','west LLRR sweep','W20 moving guard'],
 'regression_gaps':controls,'scope':'Local identities plus finite controls; the all-k induction is analytic in the reviewed proof.'}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'PASS','controls':len(controls)}))
