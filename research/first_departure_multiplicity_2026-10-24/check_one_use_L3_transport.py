"""Uncapped GLOBAL-M reader closure for LRL one-use boundary blocks.
Exact port/alternation bound, not a multiplicity/period scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b=Path(__file__).parent;L={};exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0],L);out,exact=L['out'],L['exact'];rows=[];ct=Counter();openrows=[]
for s,t in product([0,1],repeat=2):
 k,l=2+t,2+s
 for n in range(1,2*(k+l)+2):
  for z in product('NS',repeat=n):
   if z.count('S')!=k or sum(out(z,r)=='W'for r in range(n))!=l:continue
   a=sum(z[r]=='S'for r in range(0,n,2));c=sum(z[r]=='N'for r in range(0,n,2));eps=n%2
   assert c==k+l-3*a+eps and n==2*(k+l-2*a)+eps
   if a<c:continue
   assert n<=5
   h=''.join(z);hs={(1,0):'WWE'+('W'if s else''),(1,1):'N',(2,1):'WWE'+('W'if t else''),(2,0):h};ans,cert=exact(hs);ct[ans]+=1
   row=dict(start_bit=s,end_bit=t,D=h,length=n,result=ans,certificate=cert);rows.append(row)
   if ans=='open':openrows.append((s,t,h))
assert len(rows)==14 and ct=={'rank':9,'open':5}
assert openrows==[(0,0,'SSNN'),(0,1,'SSS'),(1,1,'SSSN'),(1,1,'SSNNS'),(1,1,'SSSNN')]
# Independent of GLOBAL M, the LRRL closing physical edge matches bits.
rr=[]
for s,t in product([0,1],repeat=2):
 hs={(1,0):'WWE'+('W'if s else''),(1,1):'N',(2,1):'E',(2,0):'NNS'+('N'if t else'')};ans,cert=exact(hs)
 assert (ans=='open')==(s==t)
 rr.append(dict(start_bit=s,end_bit=t,result=ans,certificate=cert))
# Necessary local LL-drop countercontrol; outside fields still OPEN.
Q={'__file__':str(b/'check_even_reader_rail_and_merge_reset.py')};exec((b/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0],Q)
hs={(1,0):'WWEW',(1,1):'SSN',(2,0):'SNNN',(2,1):'EE'};assert Q['check'](hs)=='open';su,cs,order,tt=Q['graph'](hs)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,LRL_all14_maximum_compatible_reader_rows=rows,LRL_counts=dict(ct),LRRL_complete_bit_pairs=rr,LL_drop_necessary_control=dict(histories={str(p):h for p,h in hs.items()},components=cs,component_order=order,distinct_mod4_calendar={str(e):t for e,t in tt.items()},events=len(tt)),warning='Local complete-history constraints only, no field connectors, whole period/front or resource charge.'),indent=2)+'\n')
print('PASS14 uncapped maximum-reader cases,5 LRL profiles/no bit fall;4 LRRL bit pairs;LL-drop open13-event calendar')
