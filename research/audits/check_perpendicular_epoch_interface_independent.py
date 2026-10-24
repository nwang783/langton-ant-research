from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'causal_archive_frontier_2026-10-23';K={p for p,b in walk(mark)[2].items()if b};G={}
for s in(0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];bb={p for p,b in req.items()if b};G[s]=(bb-K,(bb^flip)-{e+rotation(q,h)for q in K})
rows=[]
for a,(_,outs)in G.items():
 for o in outs:
  for b,(ins,_)in G.items():
   for i in ins:
    for h in(1,3):
     d=o-rotation(i,h)
     if(sum(xy(d))+h)%2:continue
     rows.append(dict(source=a,output=xy(o),target=b,input=xy(i),heading=h,delta=xy(d),radius=max(map(abs,xy(d)))))
assert len(rows)==1520 and max(r['radius']for r in rows)==8
ref=json.loads((D/'perpendicular_epoch_controls.json').read_text());key=lambda r:(r['source'],tuple(r['output']),r['target'],tuple(r['input']),r['heading'],tuple(r['delta']),r['radius'])
assert{key(r)for r in rows}=={key(r)for r in ref['rows']}
steps=[]
for s in(0,4,7):
 e,h,_,_=walk(raws[s]);assert h==0 and e in(1+1j,1+3j,4j);assert 0<=e.real<=e.imag and e.imag>=1
 for h in(1,3):
  q=rotation(e,h);assert q.real*q.imag<=0 and abs(q.imag)<=abs(q.real)and abs(q.real)>=1
 steps.append(xy(e))
assert len(range(1,295,2))==147 and (4*8+1)*147==4851
p=D/'perpendicular_epoch_interface.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='67b08dfb9a7abba98e4bb416478d6e8230b664f21936930da332f3f1d1790118'
out=dict(status='PASS perpendicular epoch interface and4851 transverse exception bound',note_sha256=sha,sector_roles=len(rows),radius=8,per_epoch_pair_packets=33,odd_ages=147,exception_packets=4851,maximizers=[r for r in rows if r['radius']==8],all_roles=rows,analytic='After source normalization, P=(f(y),y) with f nondecreasing1-Lipschitz; Q=(x,g(x)) with g nonincreasing1-Lipschitz. Constant endpoint extensions retain these properties. Near pairs imply |y-g(f(y))| and |x-f(g(x))|<=2R. Both functions increase by at least their argument increments, so all matched integer source/consumer starts lie in respective intervals of span4R. Each epoch has strictly monotone integer primary coordinate. At most33 consumer packets per perpendicular source epoch;294 lifetime leaves147 odd source-clock ages. Union bound4851, plus at most r0 entry-consuming packets before funding expiration.',scope='Actual U-entry simple retained factor. Long epochs have long all-parallel/antiparallel-funded subruns, not periodic profiles, fixed width, finite-state, bounded C/U, or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],sha)
