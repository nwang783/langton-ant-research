"""Exact forced Gamma contact after genuine XY cap, with all complete
WHITE next helper/target histories. No assumed even continuation mode.
Finite typed-junction cover; no period, width or radius scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import ast,json,time
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
prop,check,dom,out,V=L['propagate'],L['check'],L['dom'],L['out'],L['V'];j=json.loads((base/'check_LL_cyclic_supplier_reactivation_modes.json').read_text());rows=[];tot=Counter();tm=time.time()
def collision(hs):
 su={}
 for p,h in hs.items():
  for d,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   sr=[r for r in range(len(h))if out(h,r)==d];tr=[r for r,z in enumerate(hs[q])if z==d];assert len(sr)==len(tr)
   su.update({(p,r):(q,t)for r,t in zip(sr,tr)})
 bad=[]
 for p,h in hs.items():
  for r in range(len(h)):
   cur=(p,r);path=[cur];seen={cur}
   while cur in su:
    cur=su[cur];path.append(cur)
    if cur[0]==p:
     if cur[1]!=r+1:bad.append(path)
     break
    if cur in seen:break
    seen.add(cur)
 assert bad
 return min(bad,key=lambda z:(len(z),z))
for rs in j['roots']:
 for a in rs['cyclic_necessary_profiles']:
  for c in ['WEE','WEEW']:
   fixed={ast.literal_eval(p):h for p,h in a['histories'].items()}|{(1,-1):'SNNS',(2,-1):c,(0,-1):'EEWW'}
   pts=set(fixed)|{(0,-2),(1,-2),(2,-2)}
   ds=prop({p:([fixed[p]]if p in fixed else ['SSNN','SNNS','SNS','SNSN']if p==(0,-2)else dom(p))for p in sorted(pts)});ct=Counter();op=[]
   def rec(ds):
    if all(len(z)==1 for z in ds.values()):
     hs={p:z[0]for p,z in ds.items()};v=check(hs);ct[v]+=1
     assert v=='skipped_rank'
     op.append(dict(J=hs[(0,-2)],E=hs[(1,-2)],F=hs[(2,-2)],literal_wrong_rank_path=collision(hs)))
     return
    p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
    for h in ds[p]:
     z=prop(ds|{p:[h]})
     if z is not None:rec(z)
   if ds is not None:rec(ds)
   rows.append(dict(root=rs['root'],reaction=a['kind'],C=c,counts=dict(ct),rank_collision_certificates=op));tot.update(ct);print(rs['root'],a['kind'],c,dict(ct),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(tot),rows=rows,warning='Exact next-Gamma role reduction is a human dependency. Every count-compatible patch is rejected before heights/clocks; farther exterior cannot insert events into the literal channels.'),indent=2)+'\n');assert dict(tot)=={'skipped_rank':528};print('PASS all528 complete typed-next-RIGHT patches have literal wrong-rank witnesses',time.time()-tm)
