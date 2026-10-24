from pathlib import Path
from itertools import product
from collections import Counter
b=Path(__file__).parent;L={'__file__':str(b/'check_even_reader_rail_and_merge_reset.py')};exec((b/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0],L)
check,out,V=L['check'],L['out'],L['V'];ct=Counter();ops=[]
# B SNNN at(1,1) one->three, Y EWWW at(0,1), Z SSNS at(0,0) three->one.
# Complete 1-preserving predecessor q=(1,2) must LEFT EEW/EEWE by entry gate.
# Reader C=(0,2) and D=(1,0) complete by actual port counts.
NS=['']+[''.join(z)for n in range(1,5)for z in product('NS',repeat=n)]
EW=['']+[''.join(z)for n in range(1,5)for z in product('EW',repeat=n)]
for q,c,d in product(['EEW','EEWE'],NS,EW):
 hs={(1,1):'SNNN',(0,1):'EWWW',(0,0):'SSNS',(1,2):q,(0,2):c,(1,0):d}
 a=check(hs);ct[a]+=1
 if a=='open':ops.append((q,c,d))
print(ct,ops)
