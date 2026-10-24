from pathlib import Path
from collections import Counter
from itertools import combinations
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'global_biexterior_2026-10-23';dirs=(1j,1,-1j,-1)
def xy(q):return[int(q.real),int(q.imag)]
def white_components(B):
 if not B:return lambda v:True
 # Full finite graph with two separate diagonal parity components; every
 # vertex on this outer rectangle has an unobstructed ray to infinity.
 xmin,xmax=min(int(q.real)for q in B),max(int(q.real)for q in B);ymin,ymax=min(int(q.imag)for q in B),max(int(q.imag)for q in B)
 loX,hiX=2*xmin-3,2*xmax+3;loY,hiY=2*ymin-3,2*ymax+3
 vertices={complex(x,y)for x in range(loX,hiX+1,2)for y in range(loY,hiY+1,2)};parent={v:v for v in vertices}
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 for v in vertices:
  for delta in(2+2j,2-2j):
   w=v+delta
   if w in vertices and(v+w)/4 not in B:parent[find(w)]=find(v)
 ext={find(v)for v in vertices if v.real in(loX,hiX)or v.imag in(loY,hiY)}
 return lambda v: v not in vertices or find(v)in ext
def exterior(B,p,h):
 f=white_components(B);return(f(2*p+(-1-1j)*(-1j)**h),f(2*p+(1-1j)*(-1j)**h))
def rectangles(B):
 # Merge entire connected touching components at each round, not author's
 # sequential first-pair implementation. This is a permitted fixed order.
 boxes=[(int(q.real),int(q.real),int(q.imag),int(q.imag),frozenset([q]))for q in B]
 def touch(a,b):return max(0,a[0]-b[1],b[0]-a[1],a[2]-b[3],b[2]-a[3])<=1
 while True:
  components=[];todo=set(range(len(boxes)))
  while todo:
   comp={todo.pop()};front=list(comp)
   while front:
    i=front.pop();new={j for j in todo if touch(boxes[i],boxes[j])};todo-=new;comp|=new;front.extend(new)
   components.append(comp)
  if all(len(c)==1 for c in components):break
  boxes=[(min(boxes[i][0]for i in c),max(boxes[i][1]for i in c),min(boxes[i][2]for i in c),max(boxes[i][3]for i in c),frozenset().union(*(boxes[i][4]for i in c)))for c in components]
 for x0,x1,y0,y1,cells in boxes:
  assert x1-x0+y1-y0+2<=2*len(cells)
  assert{q for q in B if x0<=q.real<=x1 and y0<=q.imag<=y1}==set(cells)
 assert all(not touch(a,b)for a,b in combinations(boxes,2));return boxes
def inside(p,r):return r[0]<=p.real<=r[1]and r[2]<=p.imag<=r[3]
def clock2(B,p,h,c):
 sigma=(-1)**((int(p.real+p.imag)+h)%2)
 def f(v):return 3**abs(v)-1
 v=int(p.real+p.imag)-c;eps=1 if h in(0,1)else-1;J=f(v)if eps*v>=0 else-3*f(v)
 return -2*sigma*sum((-1)**(int(q.real+q.imag)%2)*f(int(q.real+q.imag)-c)for q in B)+J
stats=Counter();maxdelay=0

def check_start(B0,p0,h0,known=None):
 global maxdelay
 B=set(B0);p=p0;h=h0;m=len(B);ext=exterior(B,p,h)if known is None else known;stats['starts']+=1
 if all(ext):stats['already_biexterior']+=1;return 0
 stats['non_biexterior']+=1;rs=rectangles(B);which=[r for r in rs if inside(p,r)];assert len(which)==1;r=which[0];k=len(r[4]);width=r[1]-r[0]+1;height=r[3]-r[2]+1;area=width*height;rad=(width+height-1)//2;c=(r[0]+r[2]+r[1]+r[3])//2;bound=(area+2)*(3**rad-1)+1
 assert rad<=k-1 and area<=k*k and m-k+area<=m*m
 fixed={q for q in B if not inside(q,r)};firstclock=clock2(B,p,h,c);prevclock=firstclock;seen=set();t=0
 while True:
  assert inside(p,r);state=(frozenset(B-fixed),p,h);assert state not in seen;seen.add(state)
  assert clock2(B,p,h,c)-firstclock<=2*(area+2)*(3**rad-1)
  ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h];t+=1
  newclock=clock2(B,p,h,c);assert newclock-prevclock>=2;prevclock=newclock;stats['fine_clock_updates']+=1
  assert {q for q in B if not inside(q,r)}==fixed and len(B)<=m-k+area
  assert abs(p.real-p0.real)+abs(p.imag-p0.imag)<=width+height-1<=2*m-1
  if all(exterior(B,p,h)):break
  assert t<=bound
 assert t<=bound and t<=4*area*2**area;maxdelay=max(maxdelay,t);return t
# Every3x3 mask and every head in the surrounding5x5 square, both sectors.
cells=[complex(x,y)for x in range(-1,2)for y in range(-1,2)]
for bits in range(512):
 B={q for i,q in enumerate(cells)if bits>>i&1};component=white_components(B);rs=rectangles(B)
 for x in range(-2,3):
  for y in range(-2,3):
   for h in range(4):
    p=complex(x,y);ext=tuple(component(2*p+q*(-1j)**h)for q in(-1-1j,1-1j));stats['geometric_tests']+=1
    if not all(ext):assert any(inside(p,r)for r in rs)
    if len(B)<4:assert all(ext)
    check_start(B,p,h,ext)
# Widely separated inert clusters verify actual complete exterior cancellation.
for B0 in[{complex(x,y)for x in range(-2,3)for y in range(-2,3)},set(cells),{complex(x,y)for x in range(-2,3)for y in range(-2,3)if abs(x)+abs(y)==2}]:
 B=B0|{100+100j,101+100j,100+101j,101+101j}
 for p in(0j,1,1j,-1,-1j):
  for h in range(4):check_start(B,p,h)
# Reconstruct the actual blank orbit to the alternating trap without importing
# its saved seed, then compare the full entry board and exact port flags.
B=set();p=0j;h=0;flags=[]
for tick in range(586):
 if tick==582:
  witness=json.loads((D/'alternating_trap_witness.json').read_text());assert sorted(map(xy,B))==witness['entry_B'];assert(p,h)==(7+1j,2);assert check_start(B,p,h)==3
 if tick>=582:flags.append(exterior(B,p,h))
 if tick<585:B.symmetric_difference_update({p});h=(h+(-1 if p not in B else 1))%4;p+=dirs[h]
assert flags==[(True,False),(False,False),(False,True),(True,True)]and(p,h,len(B))==(7,1,73)
note=D/'simultaneous_white_exterior_return.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='e76114b0df91a4ed2a1b086103c7c43e4dfeaf4dfd0b79d1e71a64d42d1424f9'
out={'status':'PASS global simultaneous-white-exterior return theorem and independent exact controls','note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'counts':dict(stats),'max_delay':maxdelay,'blank_582_585_flags':flags,'analytic_review':['Finite WHITE components have enclosing simple BLACK cycles in the opposite planar lattice. Incident black midpoints have Chebyshev distance<=1, placing each cycle inside one fixed terminal rectangle. An active vertex based outside that rectangle cannot be strictly enclosed, including the extremal-line equality case.','Terminal rectangles are pairwise cell-distance>=2, so a unit head cannot relay between them. Induction retains the entire outside board and confines every pre-return read to the same original rectangle.','Merging semiperimeters gives a+b<=2k, area<=k^2. Head displacement<=a+b-1, return mass<=m-k+area<=m^2.','Centered retained strict clock has pre-return total range<=(area+2)(3^ceil((a+b-2)/2)-1). Exactly tau-1 internal-to-internal updates give stated tau bound. Finite-state alternative counts all4area2^area complete pre-return states.','Empty or singleton boards are already bi-exterior; initial exterior states use tau0 and never invoke negative exponent. Infinite checkpoint recurrence follows by applying the theorem to any state after a hypothetical final checkpoint. One ordinary step followed by first return defines a total positive-time complete-state map.'],'scope':'Arbitrary finite-support actual ants, both sectors and all words. This is a complete-state global section, not a finite summary, monotone return mass/topology, standard capture or invariant pruning theorem.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(stats,maxdelay)
