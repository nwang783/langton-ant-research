"""Exact full passive-strip singleton-O exit and its next one-use Γ RIGHT escape.
All corner-forced readers retained; not a radius/period scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
plainprop,check,dom,V=[L[k]for k in ['propagate','check','dom','V']]
raw=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0].split(' d={a:0 for a in ns}')[0]+" return'open'\n";Q={};exec(raw,Q);rankcheck=Q['check'];part=Counter()
def prop(ds):
 z=plainprop(ds)
 if z is None:return None
 a=rankcheck({p:v[0]for p,v in z.items()if len(v)==1})
 if a!='open':part[a]+=1;return None
 return z
basefixed={(0,0):'NNSS',(0,1):'EEWW',(0,2):'NNSS',(1,0):'EWWE',(1,1):'SNNS',(1,2):'EWWE',(2,0):'NNSS',(2,1):'WWEE',(2,2):'NSSN',(1,-1):'NSS',(2,-2):'NNSS'}
rows=[];tm=time.time()
for post,nxt in product(['EEWW','EWWE'],['EE','EEW']):
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
   if z=='open':op.append({str(p):h for p,h in sorted(hs.items())})
   return
  p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   z=prop(ds|{p:[h]})
   if z is not None:rec(z)
 if ds is not None:rec(ds)
 rows.append(dict(post=post,next=nxt,cells=sorted(pts),counts=dict(ct),open=op));print(post,nxt,len(pts),dict(ct),'partial',dict(part),'elapsed',time.time()-tm,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,partial=dict(part),rows=rows,warning='Fixed passive source exit only; open profiles not actual calendar, factor or full front.'),indent=2)+'\n')
