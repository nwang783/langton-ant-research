from itertools import combinations_with_replacement,product
from pathlib import Path
import json,hashlib

def vectors(n):
 return [tuple(v) for size in range(n+1) for v in combinations_with_replacement(range(5),size)]
def tails(v):return tuple(sum(a>=j for a in v) for j in range(5))
def dominates(a,b):return all(x>=y for x,y in zip(a,b))
boards=vectors(4);inputs=vectors(2);targets=vectors(3)
checks=0
for board in boards:
 bt=tails(board)
 for inp in inputs:
  it=tails(inp)
  survivors=set()
  # Direct independent allocation of every actual consumed subset.
  for mask in range(1<<len(board)):
   consumed=tuple(a for i,a in enumerate(board)if mask>>i&1)
   if len(consumed)==len(inp) and dominates(tails(consumed),it):
    survivors.add(tuple(a for i,a in enumerate(board)if not(mask>>i&1)))
  for c in range(3):
   for O in range(3):
    outcomes=[tails(tuple(min(4,a+c)for a in s)+(c,)*O) for s in survivors]
    for target in targets:
     t=tails(target)
     D=(max(0,t[0]-O,t[c+1]),)+tuple(t[j+c]if j+c<=4 else 0 for j in range(1,5))
     pred=tuple(x+y for x,y in zip(it,D))
     actual=any(dominates(o,t)for o in outcomes)
     claimed=dominates(bt,pred)
     assert actual==claimed,(board,inp,c,O,target,pred,outcomes)
     checks+=1
res={'status':'PASS exact age-tail predecessor formula versus exhaustive token-subset allocation','checks':checks,'before_max_tokens':4,'input_max_tokens':2,'target_max_tokens':3,'ages':5,'C_counts':[0,1,2],'output_counts':[0,1,2],'proof':'Nested threshold matching combines consumed and surviving obligations by adding their tail vectors; outputs at age c cover low thresholds, while older obligations pull back by c.','auditor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
