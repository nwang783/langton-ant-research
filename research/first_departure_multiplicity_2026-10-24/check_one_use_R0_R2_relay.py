"""Exact local target ranks and symbolic all-copy relay controls.
The calendars below are arithmetic controls, not physical ant fronts.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(h,r): return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def rot(h,k): return ''.join(H[(H.index(z)+k)%4] for z in h)
local=[]
for k in range(4):
 for h,inc,dep,r in [('E','E','S',0),('WWE','E','N',2),('WWEW','E','N',2)]:
  hh=rot(h,k); ii=rot(inc,k); oo=rot(dep,k)
  assert [a for a,z in enumerate(hh) if z==ii]==[r]
  assert [a for a in range(len(hh)) if out(hh,a)==oo]==[0]
  local.append(dict(word=hh,incoming=ii,outgoing=oo,arrival_rank=r,departure_rank=0))
controls=[]
for n in range(1,6):
 for cs in product(range(1,4),repeat=n):
  # Arbitrary >=8 same-cell R0-to-R2 ages, with congruent all-lift sum.
  ds=[8+4*((i+sum(cs))%3) for i in range(n)]
  P=sum(ds)-sum(cs); t0=[0]
  for i in range(n): t0.append(t0[-1]+cs[i]-ds[(i+1)%n])
  assert t0[-1]==-P
  t2=[t0[i]+ds[i] for i in range(n)]
  assert all(t2[(i+1)%n]-(P if i==n-1 else 0)==t0[i]+cs[i] for i in range(n))
  units=[]
  for i,c in enumerate(cs): units.extend(t0[i]+j for j in range(c))
  assert len({u%P for u in units})==len(units)
  for t in range(P):
   N=sum(1 for i in range(n) for k in range(-8,9) if t0[i]+k*P<t+.5<t2[i]+k*P)
   B=sum(1 for u in units for k in range(-8,9) if u+k*P<t+.5<u+k*P+1)
   assert N==1+B and B in [0,1]
  for i in range(n):
   assert t0[i]-t0[i+1]>=5
   nxt=t2[(i+1)%n]-(P if i==n-1 else 0)
   assert t2[i]-nxt>=5
   if n>=2: assert 8<=ds[i]<=P-5*(n-1)+3<P
   else: assert ds[i]==P+cs[0]
  controls.append(dict(n_LEFT=n,c=cs,Delta=ds,P=P))
p=Path(__file__).with_suffix('.json')
p.write_text(json.dumps(dict(scope=__doc__,rotated_local_target_rows=local,arithmetic_controls=len(controls),controls=controls,warning='No board, physical inter-component connectors or complete translating front is supplied.'),indent=2)+'\n')
print('PASS',len(local),'local rows and',len(controls),'all-copy arithmetic controls')
