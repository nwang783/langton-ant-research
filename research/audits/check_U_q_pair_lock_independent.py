from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/U_q_pair_lock_frozen_20261023_1840';m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items()if b};q=-1+2j;b=-1+4j;c=2j;d=3j;rows=[];valid=[];G={}
for s in(0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];black={p for p,v in req.items()if v};I=black-K;O=(black^flip)-{e+rotation(p,h)for p in K};C=set(req)|K;G[s]=O
 for i in I:
  for h in range(4):
   p=q-rotation(i,h);ctx={p+rotation(z,h)for z in C}
   if(sum(xy(p))+h)%2:reason='sector'
   else:assert ctx&{b,c};valid.append(ctx);reason='protected'
   rows.append(dict(packet=s,input=xy(i),pose=(*xy(p),h),reason=reason,upper_hits=[name for name,z in [('b',b),('c',c),('d',d)]if z in ctx]))
assert Counter(r['reason']for r in rows)==dict(sector=46,protected=46)
cover=[]
for n in range(4):
 for combo in combinations((b,c,d),n):
  p=set(combo)
  if all(p&ctx for ctx in valid)and not any(x<=p for x in cover):cover.append(p)
assert cover==[{b,c}]
for s in(7,8,9):assert {q,b,c,d}<={-1+4j+rotation(p,1)for p in G[s]}
out=dict(status='PASS independent universal current-q lock under protected b,c and three producer applications',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(Counter(r['reason']for r in rows)),minimal_upper_cover=['b','c'],rows=rows,scope='Strict earlier retirement impossible while exact b,c survive; no simplicity, age, a/d-existence or historical-component premise. Source application uses separately signed max-three.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
