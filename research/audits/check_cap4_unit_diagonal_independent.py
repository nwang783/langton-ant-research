"""Reconstruct diagonal strip adjacency from physical edges, then check parity."""
from pathlib import Path
from itertools import product
from collections import Counter,deque
import json,hashlib
P=Path(__file__).resolve().parents[1];folder=P/'periodic_classification_new';J=json.loads((folder/'cap4_unit_diagonal_transfer_certificate.json').read_text());comp=[1j,1,-1j,-1]
states={}
for parity in[0,1]:
 alphabet=(-1,1)if parity==0 else(-1j,1j)
 for m in range(5):
  for hs in product(alphabet,repeat=m):
   ins=Counter(hs);outs=Counter(h*((-1j)if i%2==0 else 1j)for i,h in enumerate(hs));key=(parity,hs)
   # At representative (0,t), outgoing d lands in row t+dy-dx
   # and crosses the full-drift seam by the integer dx.
   volt=int(sum(d.real*n for d,n in outs.items()))
   states[key]=(ins,outs,volt)
adj={s:set()for s in states}
for a,(ai,ao,av)in states.items():
 for b,(bi,bo,bv)in states.items():
  if a[0]==b[0]:continue
  if all((ao[d]==bi[d]if int(d.imag-d.real)==1 else bo[d]==ai[d])for d in comp):adj[a].add(b)
seed=[(0,()),(1,())];reach=set(seed);queue=deque(seed)
while queue:
 for t in adj[queue.popleft()]:
  if t not in reach:reach.add(t);queue.append(t)
potential={}
for s in reach:
 p,hs=s
 if p==0:
  r=Counter(hs[::2]);assert r[1]==r[-1]
  assert not hs or len(hs)in[3,4]
  if hs:assert all(states[s][0][h]>0 for h in[1,-1])and all(states[s][1][h]>0 for h in[1j,-1j])
  potential[s]=int(bool(hs))
 else:
  l=Counter(hs[1::2]);assert l[1j]==l[-1j]
  assert len(hs)in[0,1,4]
  potential[s]=int(len(hs)==4 or hs==(-1j,))
for s in reach:
 for t in adj[s]:assert t in reach and(potential[t]-potential[s]-states[t][2])%2==0
assert all(potential[s]==0 for s in seed)
keys={(r['parity'],tuple(comp[h]for h in r['headings'])):(r['parity'],r['index'])for r in J['records']};assert set(keys)==set(states)
for r in J['records']:
 s=(r['parity'],tuple(comp[h]for h in r['headings']));ins,outs,vol=states[s]
 assert r['incoming']==[ins[h]for h in comp]and r['outgoing']==[outs[h]for h in comp]and r['voltage']==vol
 assert set(map(tuple,r['successors']))=={keys[t]for t in adj[s]}
 assert r['reachable']==(s in reach)and r['potential']==potential.get(s)
assert(len(states),sum(map(len,adj.values())),len(reach),sum(len(adj[s])for s in reach))==(62,148,24,84)
out={'status':'PASS all-width cap-four full-unit-diagonal parity obstruction','states':len(states),'edges':sum(map(len,adj.values())),'reachable_states':len(reach),'reachable_edges':sum(len(adj[s])for s in reach),'empty_potentials':[potential[s]for s in seed],'scope':'Full drift(1,1) and its quarter rotations, all periods and widths; not arbitrary larger diagonal full drift.','sha256':{f:hashlib.sha256((folder/f).read_bytes()).hexdigest()for f in['cap_four_unit_diagonal_drift.md','cap4_unit_diagonal_transfer_certificate.json']}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
