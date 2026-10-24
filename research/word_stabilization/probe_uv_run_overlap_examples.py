from itertools import product
from pathlib import Path
import json
from verify_macro_word import check,rot
words=[''.join(w)for n in range(1,8)for w in product('UV',repeat=n)];best=[];mx=0;feasible=0
for x in words:
 for f in'QB':
  if f=='B'and x[-1]=='V':continue
  for y in words:
   try:r=check(x+f+y)
   except AssertionError:continue
   feasible+=1;seq=[]
   for a in r['blocks']:
    px,py,h=a['pose'];dx,dy=rot((-1,1),h);seq.append((2*px+dx,2*py+dy))
   shared=set(seq[:len(x)])&set(seq[len(x)+1:]);n=len(shared)
   if n>mx:mx=n;best=[];print('MAX',mx,x+f+y,flush=True)
   if n==mx and n and len(best)<20:best.append({'word':x+f+y,'centers_doubled':sorted(shared)})
print('feasible',feasible,'max',mx,'examples',best[:5])
Path(__file__).with_name('uv_run_overlap_examples.json').write_text(json.dumps({'feasible':feasible,'max':mx,'examples':best},indent=2))
