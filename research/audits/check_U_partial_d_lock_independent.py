from pathlib import Path
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_partial_d_lock_frozen_20261023_1832'
m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items() if b}; P={-1+1j,-1+2j,2j}; d=3j;c=-.5-.5j;goal_exit=c+4j
G={};rows=[]
for s in(0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];black={q for q,b in req.items()if b}
 G[s]=(black-K,(black^flip)-{e+rotation(q,h)for q in K},set(req)|K)
for s,(I,O,C)in G.items():
 for i in I:
  for h in range(4):
   p=d-rotation(i,h);ctx={p+rotation(q,h)for q in C}
   if(sum(xy(p))+h)%2:reason='sector';t=None
   elif ctx&P:reason='protected';t=None
   else:
    base=0 if s in(0,1) else 4 if s in(4,5,6) else 7
    v={0:1+1j,4:1+3j,7:4j}[base]
    a=p+rotation(c,h);b=a+rotation(v,h);t=(goal_exit-a)/(b-a)
    assert t.imag==0 and 0<=t.real<=1
    assert(s,p,h)in((0,4j,2),(4,6j,2),(7,-1+7j,2),(7,1+4j,3),(8,1+4j,3),(9,1+4j,3))
    reason='future_goal_exit'
   rows.append(dict(packet=s,input=xy(i),pose=(*xy(p),h),reason=reason,parameter=None if t is None else t.real))
assert Counter(r['reason']for r in rows)==dict(sector=46,protected=40,future_goal_exit=6)
assert goal_exit!=c
for s in(7,8,9):assert P|{d}<={-1+1j+q for q in G[s][1]}
# Goal U base occurs after every strict retiring base; its exit cannot be
# the ordinary adjacent shared vertex, which is the goal entry c.
out=dict(status='PASS independent partial U d lifetime lock and source application',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(Counter(r['reason']for r in rows)),cases=rows,goal_exit_doubled=xy(2*goal_exit),scope='Simple actual complete-eight factor; protect exact a,q,c, not b. Direct U-family source application uses source-entry suffix simplicity and separately signed max-three producer theorem.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
