"""Two exact even-reader interfaces: an expanding rail and an all-even
merge reset with injective complete-component clocks. No real connector,
complete period, prepared factor, front or regenerative controller claimed.
"""
from pathlib import Path
from collections import defaultdict,deque
import json,ast
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
V,out,check=L['V'],L['out'],L['check'];j=json.loads((base/'check_LL_cyclic_supplier_reactivation_modes.json').read_text())
a=next(a for r in j['roots']if r['root']=='EWWE'for a in r['cyclic_necessary_profiles']if a['kind']=='P')
fixed={ast.literal_eval(p):h for p,h in a['histories'].items()}|{(1,-1):'SNNS',(2,-1):'WEEW'}
def phase(p):return 2*(p[0]%2)if sum(p)%2==0 else 3-2*(p[0]%2)
def graph(hs):
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
  z=[];n=e;k=len(cs)
  while n not in ci:
   z.append(n);ci[n]=k
   if n not in su:break
   n=su[n]
  cs.append(z)
 assert set(ci)==ev
 adj=defaultdict(set);ind=[0]*len(cs)
 for p,h in hs.items():
  for r in range(len(h)-1):
   u,v=ci[p,r],ci[p,r+1]
   if u!=v and v not in adj[u]:adj[u].add(v);ind[v]+=1
 qu=deque(i for i in range(len(cs))if ind[i]==0);order=[]
 while qu:
  u=qu.popleft();order.append(u)
  for v in adj[u]:
   ind[v]-=1
   if ind[v]==0:qu.append(v)
 assert len(order)==len(cs)
 times={};end=-200
 for i in order:
  st=end+128;st+=(phase(cs[i][0][0])-st)%4
  for k,e in enumerate(cs[i]):times[e]=st+k
  end=st+len(cs[i])-1
 assert len(times)==len(set(times.values()))==len(ev)
 for e,f in su.items():assert times[f]==times[e]+1
 for p,h in hs.items():
  for r in range(len(h)):
   assert times[p,r]%4==phase(p)
   if r:assert times[p,r]-times[p,r-1]>=4
 return su,cs,order,times
rows=[]
for mode,F,G in [('expanding','NNSS','NNSS'),('merge_reset','SSNN','SNNS')]:
 hs=fixed|{(2,-2):F,(3,-1):G,(3,-2):'WEEW'};assert check(hs)=='open'
 su,cs,order,tt=graph(hs)
 if mode=='expanding':
  paths=[[((3,-2),1),((3,-1),1),((2,-1),0)],[((2,-1),3),((2,-2),3),((3,-2),2)]]
  assert tt[(3,-2),1]==tt[(2,-1),0]-2 and tt[(3,-2),2]==tt[(2,-1),3]+2
 else:
  paths=[[((3,-2),0),((3,-1),1),((2,-1),3),((2,-2),1),((3,-2),1)]]
  assert tt[(3,-2),1]==tt[(2,-1),3]+2
 for path in paths:
  assert all(su[e]==f for e,f in zip(path,path[1:]))
 b={p:(p[0]+V[out(h,0)][0],p[1]+V[out(h,0)][1])for p,h in hs.items()}
 if mode=='merge_reset':assert b[(3,-2)]==(3,-1)and b[(3,-1)]==(2,-1)and b[(2,-1)]==(2,0)
 assert all(len(h)==4 for h in hs.values())and len(tt)==56
 rows.append(dict(mode=mode,histories={str(p):h for p,h in sorted(hs.items())},exact_paths=paths,firstR_edges={str(p):q for p,q in b.items()},components=cs,whole_component_order=order,injective_mod4_calendar={str(e):t for e,t in tt.items()},events=len(tt),all_even=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,controls=rows,rail_invariant='Delta12(next)>=Delta12(current)+12; finite FULL quotient rules out infinite exact-mode rail',warning='No board/physical connector fills the inter-component time gaps; no global zero-output implication or renewal charge.'),indent=2)+'\n');print('PASS both complete56-event even controls, exact rail growth and RLLL role-reset, injective whole-component clocks')
