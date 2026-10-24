"""Exact local first-F-port rank classification, no global-front scan."""
from itertools import product
from pathlib import Path
import json
rows=[];negative=[]
# F is the C face whose R uses incoming N and outgoing E.
for n in range(1,5):
 for hs in product((0,2),repeat=n):
  os=[(h+(1 if j%2==0 else-1))%4 for j,h in enumerate(hs)]
  rf=sum(h==0 for j,h in enumerate(hs)if j%2==0)
  rg=sum(h==2 for j,h in enumerate(hs)if j%2==0)
  if not rf or rf<rg or not hs.count(0)or not os.count(1):continue
  first_in=hs.index(0);first_out=os.index(1)
  neg=first_out<first_in
  row=dict(incoming=list(hs),rF=rf,rG=rg,first_F_input_rank=first_in,first_F_output_rank=first_out,first_output_before_first_input=neg)
  if neg:
   assert (rf,rg)==(1,1)and hs[:3]==(2,2,0)
   assert first_out==1 and first_in==2
   negative.append(row)
  else:assert not(hs[:3]==(2,2,0))
  rows.append(row)
assert len(negative)==3
res=dict(status='PASS local first-port negativity iff flat R0(other),L1(same incoming R0),R2(F)',rows=rows,negative_rows=negative)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(dict(status=res['status'],rows=len(rows),negative_rows=len(negative))))
