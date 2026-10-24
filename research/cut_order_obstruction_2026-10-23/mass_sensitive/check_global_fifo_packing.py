from collections import deque,Counter
from pathlib import Path
from math import isqrt
import json
ROOT=Path(__file__).resolve().parent
summary={'status':'PASS','initial_root_counts':[5,6,9,16],'updates':0,'output_identities':0,'age_checks':0,'global_bound_checks':0}
for q in summary['initial_root_counts']:
 # queue: i,j,birth,root,depth. Board holds live identity positions, not historic vertices.
 Q=deque((i,0,None,i,0)for i in range(q));B={(2*i,0):(None,i)for i in range(q)}
 counts=Counter();maxdist=0
 for k in range(12000):
  assert len(B)==q+3*k and len(Q)>=q
  i,j,b,r,d=Q.popleft();p=(2*i,2*j)
  assert B.pop(p)==(b,r)
  if b is not None:assert k-b>=q;summary['age_checks']+=1
  spine=(j==0 and i>=q-1)
  children=[(i+1,0),(i,1)]if spine else[(i,j+1)]
  buds=[p,(p[0]+1,p[1]+1)]if spine else[p,(p[0]+1,p[1]),(p[0]+1,p[1]+1)]
  outs=[(2*x,2*y)for x,y in children]+buds
  assert len(set(outs))==4 and all(z not in B for z in outs)
  for z in outs:
   dist=max(abs(z[0]-p[0]),abs(z[1]-p[1]));assert dist<=2
   if b is not None:assert 5*dist<=2*(k-b)
   root=(2*r,0);rd=max(abs(z[0]-root[0]),abs(z[1]-root[1]))
   assert 5*rd<=10+2*k
   maxdist=max(maxdist,rd)
   B[z]=(k,r);summary['output_identities']+=1
  for x,y in children:Q.append((x,y,k,r,d+1))
  counts[d]+=1
  # All historic distances dominate the current maximum; enough to verify the bound.
  assert maxdist<=2*isqrt(2*(k+1))+2
  assert maxdist<=(2*(k+1)+13)//3
  if k%128==0:
   for z,(born,root)in B.items():
    rd=max(abs(z[0]-2*root),abs(z[1]))
    assert rd<=(2*(k+1)+13)//3
   summary['global_bound_checks']+=1
  # Completed depths have exactly q+d vertices.
  if Q and Q[0][4]>d:assert counts[d]==q+d
  summary['updates']+=1
 assert len(B)==q+3*12000
(ROOT/'check_global_fifo_packing.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
