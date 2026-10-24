"""Exact ten-cell mixed RR1/3/1 stock-gate to even-LL-portal composition.
Three signed entry modes, all31 complete WHITE cap4 shared-reader words.
No height, clock, period or age filtering: every count-compatible row fails ranks.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b=Path(__file__).parent;L={};exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0],L);exact=L['exact'];rows=[];ct=Counter();lc=Counter()
profiles=[('EWW','EEW','SSN','NNS'),('EWW','EEWE','SSNS','NNSN'),('EWWE','EEW','SSNN','NNS')]
for Y,q,C,z in profiles:
 for n in range(5):
  for a in product('EW',repeat=n):
   D=''.join(a)
   hs={(1,1):'SN',(0,1):Y,(0,0):'NNSS',(1,0):'EE',(1,2):q,(0,2):C,(2,2):'SSNS',(2,3):'EWWW',(1,3):z,(0,3):D}
   ans,cert=exact(hs);ct[ans]+=1
   row=dict(portal_Y=Y,incoming_LEFT_q=q,C=C,upstream_LEFT_z=z,shared_reader_D=D,result=ans,certificate=cert)
   if ans!='port':
    assert ans=='rank';path=cert['path'];lc[len(path)-1]+=1
    assert path[0][0]==path[-1][0]and path[-1][1]!=path[0][1]+1
    row['histories']={str(p):h for p,h in hs.items()}
   rows.append(row)
assert ct=={'port':79,'rank':14} and lc=={16:13,4:1}
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,profiles=profiles,total_products=93,counts=dict(ct),literal_length_counts=dict(lc),rows=rows,warning='Immediate exact composition only. Longer one-use runs, changed readers, BLACK preparation, long portal returns or other source/sink words remain outside scope.'),indent=2)+'\n')
print('PASS93 complete products:79 ports+14 literal rank failures,13 length16 and1 length4')
