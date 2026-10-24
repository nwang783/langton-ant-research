"""Occurrence-disjoint ACTUAL known-successor component packing of the exact
last-supplier square, not arbitrary overlapping windows. Finite physical
DAG is necessary; a positive outcome is an abstract clock, not a connector.
"""
from pathlib import Path
from collections import defaultdict,deque,Counter
import json,ast
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
V,out=L['V'],L['out'];src=json.loads((base/'check_LL_cyclic_supplier_reactivation_modes.json').read_text());j=json.loads((base/'explore_even_nested_reader_last_supplier_square.json').read_text());rows=[];tot=Counter()
def components(hs):
 ev={(p,r)for p,h in hs.items()for r in range(len(h))};su={};pr={}
 for p,h in hs.items():
  for d,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   ss=[r for r in range(len(h))if out(h,r)==d];tt=[r for r,z in enumerate(hs[q])if z==d];assert len(ss)==len(tt)
   for r,s in zip(ss,tt):su[p,r]=q,s;pr[q,s]=p,r
 cs=[];ci={}
 for e in sorted(ev):
  if e in pr:continue
  a=[];n=e;k=len(cs)
  while n not in ci:
   a.append(n);ci[n]=k
   if n not in su:break
   n=su[n]
  cs.append(a)
 assert set(ci)==ev
 adj=defaultdict(set);ind=[0]*len(cs)
 for p,h in hs.items():
  for r in range(len(h)-1):
   a,b=ci[p,r],ci[p,r+1]
   if a!=b and b not in adj[a]:adj[a].add(b);ind[b]+=1
 qu=deque(k for k in range(len(cs))if not ind[k]);order=[]
 while qu:
  a=qu.popleft();order.append(a)
  for b in adj[a]:
   ind[b]-=1
   if ind[b]==0:qu.append(b)
 return len(order)==len(cs),cs,order
prior=[(rs['root'],a)for rs in src['roots']for a in rs['cyclic_necessary_profiles']]
for row,(root,a)in zip(j['rows'],prior):
 assert row['root']==root and row['reaction']==a['kind']
 fixed={ast.literal_eval(p):h for p,h in a['histories'].items()}|{(1,-1):'SNNS',(2,-1):'WEEW'};ct=Counter();good=[]
 for r in row['open']:
  hs=fixed|{(2,-2):r['F'],(3,-1):r['G'],(3,-2):r['H']};ok,cs,order=components(hs);ans='whole_component_DAG'if ok else'component_precedence_cycle';ct[ans]+=1
  if ok:good.append(r|dict(components=cs,component_order=order))
 total_even=sum(all(len(r[n])%2==0 for n in'FGH')for r in good)
 rows.append(dict(root=root,reaction=a['kind'],counts=dict(ct),even_component_DAGs=total_even,survivors=good));tot.update(ct)
print(dict(tot),'all-even survivors',[r['even_component_DAGs']for r in rows])
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(tot),rows=rows,warning='DAG supplies disjoint complete-component ordering only; phase assignment/physical connecting fields and full orbit still open.'),indent=2)+'\n')
