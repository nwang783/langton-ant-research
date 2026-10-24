from pathlib import Path
from itertools import product
from collections import Counter
b=Path(__file__).parent;L={};exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0],L)
out,exact=L['out'],L['exact'];ct=Counter();op=[];n=0
for m in range(1,13):
 for z in product('EW',repeat=m):
  if z.count('E')!=3 or sum(out(z,r)=='N'for r in range(m))!=3:continue
  n+=1;d=''.join(z);hs={(1,1):'SNNN',(0,1):'EWWW',(0,0):'SSNS',(1,0):d}
  a,cert=exact(hs);ct[a]+=1
  if a=='open':op.append(d)
print(n,ct,len(op),op)
