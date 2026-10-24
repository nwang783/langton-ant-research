"""All local one-use-input flow3 launches after the signed GLOBAL-M RR/RLR reduction.
No period, drift or arbitrary segment-length scan. Complete WHITE cap4 words.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b=Path(__file__).parent;L={};exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0],L);exact,out=L['exact'],L['out']
rlr=[];ct=Counter()
for Z in ['SSNS','SSS']:
 for n in range(5):
  for v in product('EW',repeat=n):
   D=''.join(v);hs={(1,1):'SNNN',(0,1):'EWWW',(0,0):Z,(1,0):D};ans,cert=exact(hs);ct[ans]+=1
   if ans!='port':rlr.append(dict(Z=Z,D=D,result=ans,certificate=cert))
assert ct=={'port':57,'rank':5} and len(rlr)==5
assert {(r['Z'],r['D'])for r in rlr}=={('SSNS','EEWE'),('SSNS','WEEE'),('SSS','WEW'),('SSS','WEWW'),('SSS','WWWE')}
rr=[];rt=Counter();keep=[]
for Z,B in product(['NNS','NNSN'],['SSNS','SSS']):
 for Y in (['EEW','EEWE']if B=='SSNS'else['EWW','EWWE','EEWW']):
  hs={(0,0):Z,(1,0):'EWWW',(1,-1):B,(0,-1):Y};ans,cert=exact(hs);rt[ans]+=1
  row=dict(Z=Z,A='EWWW',B=B,Y=Y,result=ans,certificate=cert);rr.append(row)
  if ans=='open':keep.append((Z,B,Y))
assert rt=={'open':3,'port':7}
assert keep==[('NNS','SSNS','EEW'),('NNS','SSS','EEWW'),('NNSN','SSNS','EEWE')]
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,RLR_all62_counts=dict(ct),RLR_five_literal_failures=rlr,RR_all10_counts=dict(rt),RR_full_endpoint_rows=rr,warning='Three RR profiles are necessary local stock gates; no connected physical field, full voltage, complete front or fuel payment is certified.'),indent=2)+'\n')
print('PASS five RLR literal failures, ten complete RR endpoint rows->three necessary stock gates')
