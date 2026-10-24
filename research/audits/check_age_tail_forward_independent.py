from itertools import combinations_with_replacement
from pathlib import Path
import json,hashlib

def vs(n):return[tuple(v)for k in range(n+1)for v in combinations_with_replacement(range(5),k)]
def tails(v):return tuple(sum(a>=j for a in v)for j in range(5))
def dom(a,b):return all(x>=y for x,y in zip(a,b))
checks=0
for b in vs(6):
 x=tails(b)
 for inp in vs(3):
  I=tails(inp)
  if not dom(x,I):continue
  survivors=[]
  for mask in range(1<<len(b)):
   got=tuple(a for j,a in enumerate(b)if mask>>j&1)
   if len(got)==len(inp) and dom(tails(got),I):survivors.append(tuple(a for j,a in enumerate(b)if not(mask>>j&1)))
  assert survivors
  for c in range(3):
   for O in range(4):
    results={tails(tuple(min(4,a+c)for a in s)+(c,)*O)for s in survivors}
    pred=tuple(x[0]-I[0]+O if j<=c else min(x[l]-I[l]for l in range(j-c+1))for j in range(5))
    assert pred in results and all(dom(pred,z)for z in results),(b,inp,c,O,pred,results)
    checks+=1
J={'status':'PASS greatest simultaneous surviving-age tails versus every consumption allocation','checks':checks,'before_max_tokens':6,'input_max_tokens':3,'output_counts':[0,1,2,3],'C_counts':[0,1,2],'auditor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(J))
