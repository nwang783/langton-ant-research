"""No-author-import literal enumeration of direct unary 3+2 ancestry forks."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new/U_direct_three_two_fork_frozen_20261023_1820';M=json.loads((D/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((D/f['file']).read_bytes()).hexdigest()==f['sha256']
ids=(0,1,4,5,6,7,8,9);K={q for q,b in walk(mark)[2].items()if b};G={}
for src in ids:
 e,h,_,flip=walk(raws[src]);req=walk(raws[src]+mark)[2];B={q for q,b in req.items()if b};G[src]=dict(I=B-K,O=(B^flip)-{e+rotation(q,h)for q in K},context=set(req))
P=G[7]['I'];assert G[1]['I']=={1j};triples=[];forks=[]
place=lambda S,p,h:{p+rotation(q,h)for q in S}
for src in ids:
 for h in range(4):
  for p in {q-rotation(o,h)for q in P for o in G[src]['O']}:
   if (sum(xy(p))+h)%2:continue
   O=place(G[src]['O'],p,h)
   for tri in combinations(sorted(P&O,key=xy),3):
    tri=set(tri);pair=P-tri;triples.append((src,*xy(p),h,tuple(sorted(map(xy,tri)))))
    for hh in range(4):
     for q in {t-rotation(o,hh)for t in pair for o in G[1]['O']}:
      if (sum(xy(q))+hh)%2 or not pair<=place(G[1]['O'],q,hh):continue
      parent=q+rotation(1j,hh)
      if parent not in O or parent in tri:continue
      hit=tri&place(G[1]['context'],q,hh)
      rec=dict(source=(src,*xy(p),h),child=(1,*xy(q),hh),parent_cell=xy(parent),triple=sorted(map(xy,tri)),pair=sorted(map(xy,pair)),protected_context_hits=sorted(map(xy,hit)))
      if hit:rec['reason']='context'
      else:
       base=4 if src==6 else 7 if src==9 else None;assert base is not None
       prefix=len(raws[base])+15
       ep,eh,_,_=walk(raws[src][:prefix]);Pcut=p+rotation(ep,h);Ph=(h+eh)%4
       eq,eh,_,_=walk(raws[1]);Qcut=q+rotation(eq,hh);Qh=(hh+eh)%4
       cp=2*Pcut+rotation(-1-1j,Ph);cq=2*Qcut+rotation(-1-1j,Qh);assert cp==cq==-5+3j
       rec.update(reason='repeated_actual_center',source_prefix=prefix,source_cut=(xy(Pcut),Ph),child_cut=(xy(Qcut),Qh),doubled_center=xy(cp))
      forks.append(rec)
assert len(triples)==132 and len(forks)==16 and Counter(r['reason']for r in forks)==dict(context=14,repeated_actual_center=2)
A=json.loads((D/'02_U_direct_three_two_fork.json').read_text());assert {(r['source'][0],r['source'][1:],r['child'][1:])for r in forks}=={(r['source'],tuple(r['source_pose']),tuple(r['DC_pose']))for r in A['all_forks']}
out=dict(status='PASS independent literal direct-unary 3+2 fork exclusion on simple centers',manifest_sha256=hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),chosen_source_triples=132,forks=16,context_exclusions=14,repeated_vertex_exclusions=2,rows=forks,scope='Actual center-simple complete-eight factor; source P supplies three final identities and direct unary child DC supplies two. No longer unary chain, V/U child or general historical-component theorem.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
