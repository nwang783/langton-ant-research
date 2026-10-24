"""Brute raw path controls for the analytic all-k axis-slot formula."""
from pathlib import Path
from itertools import product
import json,hashlib
checks=0;wordcount=0
for k in range(1,10):
 for horizontal in [False,True]:
  groups={};H=(k+int(horizontal))//2;V=k-H
  for signs in product([-1,1],repeat=k):
   x=y=0;prefix=[]
   for i,s in enumerate(signs):
    prefix.append((x,y))
    if(i%2==0)==horizontal:x+=s
    else:y+=s
   groups.setdefault((x,y),[]).append(prefix);wordcount+=1
  for(x,y),paths in groups.items():
   E=(H+x)//2;W=H-E;N=(V+y)//2;S=V-N
   for alpha,beta in product(range(-3,4),repeat=2):
    if not(alpha or beta):continue
    ph=E if alpha>=0 else W;pv=N if beta>=0 else S
    for j in range(k):
     hj=(j+int(horizontal))//2;vj=j-hj
     value=abs(alpha)*(2*min(hj,ph)-hj)+abs(beta)*(2*min(vj,pv)-vj)
     assert value==max(alpha*p[j][0]+beta*p[j][1]for p in paths)
     checks+=1
root=Path(__file__).resolve().parents[1];source=root/'computability/dual_record_finite_support_bridge.md'
result={'status':'PASS independent exhaustive raw path controls for dual prefix formula','lengths':[1,9],'covectors':'all nonzero integer pairs in [-3,3]^2','raw_words':wordcount,'exact_prefix_maximum_checks':checks,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
