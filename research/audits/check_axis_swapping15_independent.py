"""Independent exhaustive inventories and digit-based residual replay."""
from itertools import product
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];src=P/'computability/axis_swapping_k15';J=json.loads((src/'inventory.json').read_text());records=json.loads((src/'records.json').read_text())
compass=[1j,1,-1j,-1]
def replay(w,h):
 p=0j;colors={};last={}
 for t,d in enumerate(w):
  ratio=d/h;assert ratio in(1j,-1j);black=ratio==1j
  if p in colors and colors[p]!=black:return {'status':'CONFLICT','time':t,'previous':last[p],'cell':[int(p.real),int(p.imag)],'turn':3 if black else 1}
  colors[p]=not black;last[p]=t;p+=d;h=d
 return None
inventories=[];raw_counts=[];alien=[]
for axis,target,first in [(1,3,1j),(1j,5j,1)]:
 raw=0;accepted=[];hits=[]
 for bits in product([-1,1],repeat=15):
  w=tuple(first*(1j if i%2 else 1)*s for i,s in enumerate(bits))
  if sum(w)!=target:continue
  raw+=1
  if all(replay(w,h)is not None for h in [first*1j,first*-1j]):continue
  p=0j;extra=[]
  for t,d in enumerate(w[:-1],1):
   p+=d
   if p.real%3==0 and p.imag%5==0 and p not in(0,target):extra.append((t,int(p.real),int(p.imag)))
  accepted.append(w);hits.append(extra)
 raw_counts.append(raw);inventories.append(accepted);alien.append(hits)
assert raw_counts==[1470,490] and list(map(len,inventories))==[242,186]
for own,key in zip(inventories,['E','N']):assert set(own)=={tuple(compass[d]for d in w)for w in J[key]}
assert sum(bool(h)for h in alien[0])==0 and sum(bool(h)for h in alien[1])==24
savedE=[tuple(compass[d]for d in w)for w in J['E']];savedN=[tuple(compass[d]for d in w)for w in J['N']]
alienN={w for w,h in zip(inventories[1],alien[1])if h}
assert {savedN[i]for i in J['north_original_indices']}==alienN
expected={(r['east'],r['north'],r['root'],r['heading']):{k:v for k,v in r.items()if k not in['east','north','root','heading']}for r in records};assert len(expected)==23232
count=0;latest=0
for ie,E in enumerate(savedE):
 for jn,N in enumerate(savedN):
  if N not in alienN:continue
  phi={1:E,1j:N,-1:tuple(-d for d in E),-1j:tuple(-d for d in N)}
  # Four refinements fix every possible half-turn axis-swapping first map.
  for root in [1,1j]:
   d=root
   for _ in range(4):d=phi[d][0]
   assert d==root
   def letters():
    for t in range(15**4):
     d=root
     for place in [3375,225,15,1]:d=phi[d][t//place%15]
     yield d
   for h in [root*1j,root*-1j]:
    conflict=replay(letters(),h);assert conflict is not None
    key=(ie,jn,compass.index(root),compass.index(h));assert conflict==expected[key]
    count+=1;latest=max(latest,conflict['time'])
assert count==23232 and latest==169
out={'status':'PASS finite-support family exclusion via signed vertex-only theorem plus complete residual replay','raw_images':raw_counts,'internally_legal_images':list(map(len,inventories)),'vertex_only_pairs':242*162,'residual_pairs':242*24,'residual_cases':count,'latest_zero_based_conflict':latest,'sha256':{str((src/f).relative_to(P)):hashlib.sha256((src/f).read_bytes()).hexdigest()for f in ['inventory.json','records.json','result.json']}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
