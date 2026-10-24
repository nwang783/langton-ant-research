from pathlib import Path
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_core_last_helper_frozen_20261023_1727';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items()if b};P={-1+1j,-1+2j,-1+4j,2j,3j};r=-1+0j;c=-.5-.5j;G={};rows=[]
for s in(0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];black={q for q,b in req.items()if b};G[s]=black-K,(black^flip)-{e+rotation(q,h)for q in K},set(req)|K,e,h
for s,(I,O,C,e,dh)in G.items():
 for i in I:
  for h in range(4):
   p=r-rotation(i,h);ctx={p+rotation(q,h)for q in C};hit=ctx&P
   if(sum(xy(p))+h)%2:reason='sector'
   elif hit:reason='protected'
   else:
    end=p+rotation(e,h);hh=(h+dh)%4
    if(end,hh)==(0j,0):
     assert(s,p,h)in((0,-1-1j,0),(4,-1-3j,0),(7,-4j,0));reason='immediate'
    else:
     assert s in(7,8,9)and(p,h)==(-2-1j,1);a=p+rotation(c,h);b=a+rotation(4j,h);assert a==-2.5-.5j and b==1.5-.5j and(a+c)/2!=b
     assert (c-a)/(b-a)==.5;reason='simple_contact'
   rows.append(dict(packet=s,input=xy(i),pose=(*xy(p),h),reason=reason))
assert Counter(q['reason']for q in rows)==dict(sector=46,protected=40,immediate=3,simple_contact=3)
assert r in K and not(P&set(walk(mark)[2]))
for s in(8,9):
 O={1+5j+rotation(q,2)for q in G[s][1]};assert{r,-1j,* (P-{-1+2j})}<=O and-1+2j not in O
helperI=[{p+q for q in G[s][0]}for s,p in((0,-1-1j),(4,-1-3j),(7,-4j))];assert[(-1j in I)for I in helperI]==[False,True,True]
out=dict(status='PASS independent simple-path U core last-helper inventory and literal boundary scope',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(Counter(q['reason']for q in rows)),cases=rows,scope='All five exact goal input identities protected and an extra residual at(-1,0), within same simple complete-eight factor. Exact immediate D/V/U predecessor only; no age clause, merger or impossibility claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
