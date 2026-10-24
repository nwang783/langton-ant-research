from pathlib import Path
from itertools import product
from collections import Counter
base=Path(__file__).parent;lib={'__file__':str(base/'check_even_reader_rail_and_merge_reset.py')};exec((base/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0],lib)
check,out,V=[lib[k]for k in['check','out','V']]
NS=['']+[''.join(a)for n in range(1,5)for a in product('NS',repeat=n)]
for root,q in product(['EWW','EWWE'],['E','EE','EEW','EEWE']):
 ct=Counter();op=[]
 for c in NS:
  hs={(1,1):'SN',(0,1):root,(0,0):'NNSS',(1,0):'EE',(1,2):q,(0,2):c}
  a=check(hs);ct[a]+=1
  if a=='open':op.append(c)
 print(root,q,ct,op)
