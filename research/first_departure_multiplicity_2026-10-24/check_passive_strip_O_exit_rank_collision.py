"""Exact full passive-strip singleton-O exit and its next Γ RIGHT.
All corner-forced readers retained; not a radius/period scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
plainprop,check,dom,V,out=[L[k]for k in ['propagate','check','dom','V','out']]
raw=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0].split(' d={a:0 for a in ns}')[0]+" return'open'\n";Q={};exec(raw,Q);rankcheck=Q['check'];part=Counter()
prop=plainprop
basefixed={(0,0):'NNSS',(0,1):'EEWW',(0,2):'NNSS',(1,0):'EWWE',(1,1):'SNNS',(1,2):'EWWE',(2,0):'NNSS',(2,1):'WWEE',(2,2):'NSSN',(1,-1):'NSS',(2,-2):'NNSS'}
rows=[];tm=time.time()
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
   cur=(p,r);pa=[cur];seen={cur}
   while cur in su:
    cur=su[cur];pa.append(cur)
    if cur[0]==p:
     if cur[1]!=r+1:bad.append(pa)
     break
    if cur in seen:break
    seen.add(cur)
 assert bad
 return min(bad,key=lambda z:(len(z),z))
for post,nxt in product(['EEWW','EWWE'],['EEWW','EWWE','EWE','EWEW']):
 fixed=basefixed|{(2,-1):post,(3,-2):nxt};pts=set(fixed)
 while True:
  ca={(p[0]+v[0],p[1]+v[1])for p in pts for v in V.values()}-pts
  ad={q for q in ca if sum((q[0]+v[0],q[1]+v[1])in pts for v in V.values())>=2}
  if not ad:break
  pts|=ad
 ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in sorted(pts)});ct=Counter();op=[]
 def rec(ds):
  if all(len(a)==1 for a in ds.values()):
   hs={p:a[0]for p,a in ds.items()};z=check(hs);ct[z]+=1
   assert z=='skipped_rank'
   op.append(dict(histories={str(p):h for p,h in sorted(hs.items())},literal_wrong_rank_path=collision(hs)))
   return
  p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   z=prop(ds|{p:[h]})
   if z is not None:rec(z)
 if ds is not None:rec(ds)
 rows.append(dict(post=post,next=nxt,cells=sorted(pts),counts=dict(ct),rank_collision_certificates=op));print(post,nxt,len(pts),dict(ct),'partial',dict(part),'elapsed',time.time()-tm,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,partial=dict(part),rows=rows,warning='Exact passive-strip exit role reduction is a separate human dependency. All count-compatible patches have literal rank collisions; arbitrary older exterior cannot insert reads into those actual channels.'),indent=2)+'\n')

from collections import Counter
total=Counter()
for r in rows:total.update(r['counts'])
assert set(total)=={'skipped_rank'}
print('PASS all complete count-compatible passive O exits',dict(total))
