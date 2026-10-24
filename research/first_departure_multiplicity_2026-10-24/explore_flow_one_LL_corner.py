from pathlib import Path
from itertools import product
from collections import Counter
import json
base=Path(__file__).parent;lib={'__file__':str(base/'check_even_reader_rail_and_merge_reset.py')};exec((base/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0],lib)
check,out,V=[lib[k] for k in ['check','out','V']]
def words(axis):return ['']+[''.join(x)for n in range(1,5)for x in product(axis,repeat=n)]
ct=Counter();ans=[]
for q,p,x,y in product(['WWE','WWEW'],['SSN','SSNS'],words('NS'),words('EW')):
 hs={(1,0):q,(1,1):p,(2,0):x,(2,1):y}
 z=check(hs);ct[z]+=1
 if z=='open':ans.append(hs)
print(ct,'open',len(ans));print(ans[:20])
