from pathlib import Path
from itertools import product
from collections import Counter
b=Path(__file__).parent;L={};exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0],L)
out,exact=L['out'],L['exact']
for root,q in product(['EWW','EWWE'],['E','EE','EEW','EEWE']):
 k=sum(out(root,r)=='N' for r in range(len(root)));l=q.count('E');op=[];ct=Counter();count=0
 for n in range(1,2*(k+l)+2):
  for z in product('NS',repeat=n):
   if z.count('N')!=k or sum(out(z,r)=='E'for r in range(n))!=l:continue
   count+=1;c=''.join(z);hs={(1,1):'SN',(0,1):root,(0,0):'NNSS',(1,0):'EE',(1,2):q,(0,2):c}
   a,cert=exact(hs);ct[a]+=1
   if a=='open':op.append(c)
 print(root,q,'countdomain',count,'results',dict(ct),'open',op)
