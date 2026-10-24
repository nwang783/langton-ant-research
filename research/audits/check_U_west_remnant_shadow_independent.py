from pathlib import Path
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_west_remnant_shadow_frozen_20261023_1914';m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
for p,h in m['dependencies'].items():assert hashlib.sha256((ROOT/'core_periodicity_new'/p).read_bytes()).hexdigest()==h
K={q for q,b in walk(mark)[2].items()if b};protected={0j,1+0j,1+1j};w=1j;rows=[];survive=[]
for s in (0,1,4,5,6,7,8,9):
 e,h,_,f=walk(raws[s]);req=walk(raws[s]+mark)[2];black={q for q,b in req.items()if b};I=black-K;O=(black^f)-{e+rotation(q,h)for q in K};ctx=set(req)|K
 if s in (7,8,9):assert protected|{w}<=O
 for i in I:
  for hd in range(4):
   p=w-rotation(i,hd);full={p+rotation(q,hd)for q in ctx}
   if(sum(xy(p))+hd)%2:reason='sector'
   elif full&protected:reason='protected'
   else:
    bs=0 if s in(0,1) else 4 if s in(4,5,6) else 7
    e0,h0,_,_=walk(raws[bs]);pe=p+rotation(e0,hd);he=(h0+hd)%4;ce=2*pe+rotation(-1-1j,he)
    assert ce==-1+3j;reason='source_chord_interior';survive.append((s,(*xy(p),hd)))
   rows.append(dict(packet=s,input=xy(i),pose=(*xy(p),hd),reason=reason))
assert Counter(r['reason']for r in rows)==dict(sector=46,protected=40,source_chord_interior=6)
assert set(survive)=={(0,(0,2,2)),(1,(0,2,2)),(4,(0,4,2)),(5,(0,4,2)),(7,(-1,5,2)),(8,(-1,5,2))}
for s in(7,8,9):
 req=walk(raws[s]+mark)[2];I={q for q,b in req.items()if b}-K
 assert {2j+rotation(q,2)for q in(-1+1j,-1+2j,2j)}==protected
 assert req[rotation(w-2j,2)]==False
out=dict(status='PASS independent west-remnant lifetime lock and exact three-cohort exclusion',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(Counter(r['reason']for r in rows)),rows=rows,survivors=survive,source_chord_doubled=[[-1,-1],[-1,7]],common_survivor_base_exit=[-1,3],scope='Retain exact original west pair and r0,0 after any prior east-cycle break. Old w0,1 cannot retire by U-entry suffix simplicity. No intact-cycle, first-break, age, blanket west-pair or global U-budget premise.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
