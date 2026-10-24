"""Finite candidate consumer implication closure, not an actual-prefix search.
Seeds are signed U target retirement shadows. Domain is the exact 17 target
complete-context cells that cannot contain a current old residual at target.
"""
from pathlib import Path
import json,collections,hashlib
W=Path(__file__).resolve().parent
geo=W/'chronology_dcuv/literal_residual_geometry.json'
G=json.loads(geo.read_text())['geometry'];IDS=[0,1,4,5,6,7,8,9]
P={(-1,1),(-1,2),(-1,4),(0,2),(0,3)}
C={tuple(r[:2]) for r in G[7]['requirements']};domain=C-P

def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
placements={}
for w in sorted(domain):
 rows=[]
 for a in IDS:
  for h in range(4):
   for slot,i in enumerate(G[a]['inputs']):
    p=sub(w,rot(i,h));ctx={add(p,rot(r[:2],h))for r in G[a]['requirements']}
    ins={add(p,rot(i,h))for i in G[a]['inputs']};outs={add(p,rot(o,h))for o in G[a]['outputs']}
    reason='sector' if(sum(p)+h)%2 else 'protected_context' if(ctx&P) else None
    rows.append(dict(packet=a,pose=[*p,h],input_slot=slot,inputs=sorted(ins),outputs=sorted(outs),reason=reason))
 assert len(rows)==92
 placements[w]=rows
F={(-1,3),(1,1)};rounds=[]
while True:
 new=[];round_rows=[]
 for w in sorted(domain-F):
  cnt=collections.Counter();live=[]
  for r in placements[w]:
   if r['reason']:reason=r['reason']
   elif set(map(tuple,r['inputs']))&F:reason='already_forbidden_input'
   elif set(map(tuple,r['outputs']))&F:reason='fresh_already_forbidden_output'
   else:reason=None;live.append(r)
   cnt[reason or 'survives']+=1
  round_rows.append(dict(cell=w,counts=dict(cnt),survivors=live))
  if not live:new.append(w)
 rounds.append(dict(prior_forbidden=sorted(F),new_forbidden=new,queries=round_rows))
 if not new:break
 F.update(new)
result=dict(status='FINITE_CLOSURE_COMPLETE_NOT_REACHABILITY',scope='Exact 17-cell target complete-context domain, protecting all five goal input identities. All actual current identities in the two seeds are excluded by signed retirement shadows. Complete consumer enumeration closes implications; no age, head-path or packet-depth restriction.',seed_cells=[[-1,3],[1,1]],domain=sorted(domain),closed_forbidden=sorted(F),new_forbidden=sorted(F-{(-1,3),(1,1)}),rounds=rounds,geometry_sha256=hashlib.sha256(geo.read_bytes()).hexdigest())
out=W/'chronology_dcuv/U_protected_shadow_closure.json';out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(domain_size=len(domain),rounds=len(rounds),closed_forbidden=sorted(F),new_forbidden=result['new_forbidden']),indent=2))
