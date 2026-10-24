"""Exact even two-read one-use LL portal. A finite injective known-channel
calendar, not a supplied physical exterior factor or full front.
"""
from pathlib import Path
from collections import defaultdict,deque
import json
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
out,V,check=L['out'],L['V'],L['check'];hs={(0,0):'NNSS',(1,0):'EE',(1,1):'SN',(0,1):'EWWE'}
assert check(hs)=='open'
ev={(p,r)for p,h in hs.items()for r in range(len(h))};su={};pr={}
for p,h in hs.items():
 for d,v in V.items():
  q=p[0]+v[0],p[1]+v[1]
  if q not in hs:continue
  sr=[r for r in range(len(h))if out(h,r)==d];tr=[r for r,z in enumerate(hs[q])if z==d];assert len(sr)==len(tr)
  su.update({(p,r):(q,s)for r,s in zip(sr,tr)});pr.update({(q,s):(p,r)for r,s in zip(sr,tr)})
cs=[];ci={}
for e in sorted(ev):
 if e in pr:continue
 n=e;a=[];i=len(cs)
 while n not in ci:
  a.append(n);ci[n]=i
  if n not in su:break
  n=su[n]
 cs.append(a)
assert set(ci)==ev
ad=defaultdict(set);ind=[0]*len(cs)
for p,h in hs.items():
 for r in range(len(h)-1):
  u,v=ci[p,r],ci[p,r+1]
  if u!=v and v not in ad[u]:ad[u].add(v);ind[v]+=1
qu=deque(i for i in range(len(cs))if ind[i]==0);order=[]
while qu:
 u=qu.popleft();order.append(u)
 for v in ad[u]:
  ind[v]-=1
  if ind[v]==0:qu.append(v)
assert len(order)==len(cs)
phase=lambda p:2*(p[0]%2)if sum(p)%2==0 else 3-2*(p[0]%2)
times={};end=-100
for i in order:
 st=end+64;st+=(phase(cs[i][0][0])-st)%4
 for j,e in enumerate(cs[i]):times[e]=st+j
 end=st+len(cs[i])-1
assert len(times)==len(set(times.values()))==12
for e,f in su.items():assert times[f]==times[e]+1
for p,h in hs.items():
 for r in range(len(h)):
  assert times[p,r]%4==phase(p)
  if r:assert times[p,r]-times[p,r-1]>=4
path=[((0,1),1),((0,0),3),((1,0),1),((1,1),1),((0,1),2)]
assert all(su[e]==f for e,f in zip(path,path[1:]))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,histories={str(p):h for p,h in hs.items()},actual_four_L_cleanup=path,components=cs,component_order=order,injective_mod4_calendar={str(e):t for e,t in times.items()},incoming_one_use_to_B=True,outgoing_one_use_from_A=True,all_even=True,warning='All earlier WHITE R0s and optional L3s present. No real connectors, full P/d or completed boundary/front supplied.'),indent=2)+'\n');print('PASS12 all-even portal events, exact LLLL, five whole channels, distinct mod4 clocks')
