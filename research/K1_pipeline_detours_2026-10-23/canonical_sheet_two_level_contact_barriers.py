"""Local geometric side barriers for the exact canonical sheet repair.
All 30 complete WHITE cap-four histories and every nonempty sheet.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json
H='NESW';checks=[]
for n in range(1,5):
 for z in product('EW',repeat=n):
  h=''.join(z);rs=Counter(h[::2]);ls=Counter(h[1::2]);a=-max(rs['E'],rs['W'])
  C=dict(NE=rs['W']+a,SW=rs['E']+a);L=dict(NW=a-ls['E'],SE=a-ls['W'])
  rc={'E':C['SW'],'W':C['NE'],'N':C['NE'],'S':C['SW']}
  inc=Counter();outc=Counter();es=[]
  for r,x in enumerate(h):
   y=H[(H.index(x)+(1 if r%2==0 else -1))%4];inc[x]+=1;outc[y]+=1
   es.append(dict(rank=r,incoming=x,outgoing=y,il=rc[x]-inc[x]+1,ol=rc[y]-outc[y]+1))
  for j in range(min(L.values())+1,max(C.values())+1):
   pairs=[]
   for e in es:
    if e['il']!=j:continue
    r=e['rank'];s=3-r if n>=3 and r in(1,2) else r;f=es[s]
    assert f['ol']==j
    turn='R' if (H.index(f['outgoing'])-H.index(e['incoming']))%4==1 else 'L'
    pairs.append(dict(in_rank=r,out_rank=s,turn=turn))
   if not pairs:continue
   low=max(L.values())<=j-2;high=min(C.values())>=j+1
   # At a two-port smoothing the two diagonal sectors of the opposite
   # species lie on the same side. At four ports, R/R leaves the L
   # diagonal centrally connected, L/L leaves the C diagonal connected.
   if low:assert pairs and all(p['turn']=='R' for p in pairs)
   if high:assert pairs and all(p['turn']=='L' for p in pairs)
   if low and len(pairs)==2:assert set(C.values())=={j} and set(L.values())=={j-2} and n==4
   if high and len(pairs)==2:assert set(C.values())=={j+1} and set(L.values())=={j-1} and n==4
   checks.append(dict(headings=h,j=j,C=C,L=L,pairs=pairs,L_contact_preserved=low,C_contact_preserved=high))
assert len(checks)>30
out=dict(scope=__doc__,sheets_checked=len(checks),low_contact_cases=sum(r['L_contact_preserved'] for r in checks),high_contact_cases=sum(r['C_contact_preserved'] for r in checks),checks=checks)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',out['sheets_checked'],'nonempty local sheets, low-L',out['low_contact_cases'],'high-C',out['high_contact_cases'])
