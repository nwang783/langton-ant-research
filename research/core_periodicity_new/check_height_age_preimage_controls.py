from itertools import product
from random import Random
from pathlib import Path
import json

def tails(a):return [sum(a[j:])for j in range(5)]
def le(a,b):return all(x<=y for x,y in zip(a,b))
def brute(x,inp,t,c,O):
 need=sum(inp)
 for eat in product(*[range(v+1)for v in x]):
  if sum(eat)!=need or not le(tails(inp),tails(eat)):continue
  after=[0]*5
  for j in range(5):after[min(4,j+c)]+=x[j]-eat[j]
  after[c]+=O
  if le(tails(t),tails(after)):return True
 return False
R=Random(321994);n=40000
for k in range(n):
 x=[0]*5;inp=[0]*5;t=[0]*5
 for _ in range(R.randrange(8)):x[R.randrange(5)]+=1
 for _ in range(R.randrange(5)):inp[R.randrange(5)]+=1
 for _ in range(R.randrange(7)):t[R.randrange(5)]+=1
 c=R.randrange(5);O=R.randrange(5);X=tails(x);I=tails(inp);T=tails(t)
 p=[I[0]+max(0,T[0]-O,T[c+1]if c<4 else 0)]+[I[j]+(T[j+c]if j+c<5 else 0)for j in range(1,5)]
 assert le(p,X)==brute(x,inp,t,c,O),(x,inp,t,c,O,p)
r={'status':'PASS','controls':n,'method':'Separate exhaustive consumed-submultiset matching for every random source/input/goal; c0..4, output0..4, source mass0..7. This checks the claimed unique minimal backward predecessor, not any record exclusion.'}
Path('chronology_dcuv/delayed_height_probe/height_age_preimage_controls.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
