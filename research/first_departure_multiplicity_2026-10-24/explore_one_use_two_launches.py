from pathlib import Path
from itertools import product
from collections import Counter
b=Path(__file__).parent;L={};exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0],L)
exact=L['exact'];ct=Counter();op=[]
for B,Y,A in product(['SN','SNN'],['EWW','EWWE','EEWW'],['SS','SSN','SSNN','SNNS','SNS','SNSN']):
 loc=[]
 for m in range(5):
  for z in product('EW',repeat=m):
   D=''.join(z);hs={(1,1):B,(0,1):Y,(0,0):A,(1,0):D}
   a,cert=exact(hs);ct[a]+=1
   if a=='open':loc.append(D)
 if loc:op.append((B,Y,A,loc))
print(dict(ct),'primaryopen',len(op))
for a in op:print(a)
