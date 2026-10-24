"""The five signed GLOBAL-M flow3 segment templates, source1->3/sink3->1.
Exact all-template reader corner closure; no period, drift or segment-length scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b=Path(__file__).parent;L={'__file__':str(b/'explore_two_flat_pair_reader_closure.py')};exec((b/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
H,V,rot,out,dom,propagate,check=[L[k]for k in['H','V','rot','out','dom','propagate','check']]
rows=[];counts=Counter()
for tr in ['RR','RLR','RLRR','RRLR','RRLRR']:
 for mids in product(['EEEW','EWEE'],repeat=tr[1:-1].count('R')):
  p=(0,0);ci='N';nodes=[];it=iter(mids)
  for i,t in enumerate(tr):
   if i==0:h=rot('EWWW',ci)
   elif i==len(tr)-1:h=rot('EEWE',ci)
   elif t=='R':h=rot(next(it),ci)
   else:h=rot('WEEE',ci)
   co=H[(H.index(ci)+(1 if t=='R'else -1))%4]
   assert out(h,0)==co
   nodes.append(dict(cell=p,turn=t,ci=ci,co=co,h=h));p=p[0]+V[co][0],p[1]+V[co][1];ci=co
  fixed={z['cell']:z['h']for z in nodes};pts=set(fixed)
  while True:
   cand={(p[0]+v[0],p[1]+v[1])for p in pts for v in V.values()}-pts
   add={q for q in cand if sum((q[0]+v[0],q[1]+v[1])in pts for v in V.values())>=2}
   if not add:break
   pts|=add
  ds=propagate({p:[fixed[p]]if p in fixed else dom(p)for p in sorted(pts)});ct=Counter();op=[]
  if ds is None:ct['primary_PORT']+=1
  else:
   def rec(ds):
    if all(len(v)==1 for v in ds.values()):
     hs={p:v[0]for p,v in ds.items()};a=check(hs);ct[a]+=1
     if a=='open':op.append({str(p):h for p,h in hs.items()})
     return
    p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
    for h in ds[p]:
     nd=propagate(ds|{p:[h]})
     if nd is not None:rec(nd)
   rec(ds)
  counts.update(ct);row=dict(template=tr,middle_RIGHT=mids,nodes=nodes,cells=sorted(pts),counts=dict(ct),open=op);rows.append(row)
  print(tr,mids,len(pts),dict(ct),'open',len(op),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(counts),rows=rows),indent=2)+'\n')
print('ALL',counts)
