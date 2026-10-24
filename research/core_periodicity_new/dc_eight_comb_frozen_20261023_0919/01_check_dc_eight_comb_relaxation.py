"""Author finite controls for the explicit residual-only comb; not an ant simulation."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;J=json.loads((W/'genealogy_saturation_roles_frozen_20261023_0833/01_graph.json').read_text());roles=J['roles'];E=J['all_fundamental_edges'];G=json.loads((W/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];offs=[(x,y-1)for x,y in G[1]['outputs']];assert offs==[(2,-1),(2,2),(3,0),(3,1)]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
roots=[]
for r in range(8):
 h=(-r)%4;roots.append(rot((100,100+(1-h)%2+10*(r//4)),h))
T={p:None for p in roots};counts=[]
for k in range(16000):
 r=k%8;j=k//8;h=(-r)%4;parent=add(roots[r],rot((3*j,j),h));birth=T.pop(parent);assert birth is None or k-birth==8
 head=add(parent,rot((0,-1),h));assert(sum(head)+h)%2==0 and h==(-k)%4
 for d in offs:
  p=add(parent,rot(d,h));assert p not in T,(k,p);T[p]=k
 assert len(T)==8+3*(k+1)
for h in range(4):
 u=roles.index([1,[3,2],h]);assert[u,u,8,rot((3,1),h)[1]]in E
core={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};shift=(3,1);block=[(tuple(o),(o[0]-shift[0],o[1]-shift[1]))for o in G[1]['outputs']if tuple(o)!= (3,2)and(o[0]-shift[0],o[1]-shift[1])in core];assert block==[((2,0),(-1,-1)),((3,1),(0,0))]
O=dict(status='AUTHOR_RESIDUAL_REWRITE_CONTROLS_PASS_NOT_PHYSICAL_LEDGER',initial_residual_roots=8,checked_C_events=16000,final_residual_mass=len(T),parent_C_age=8,spine_shift=[3,1],role_transfer=[1,1,3,1,0,3,2,8],mandatory_core_blockers=block,scope='Exact DC residual masks, birth headings/sectors and marginal spine roles; deliberately omits live-cursor continuity and five-core disjointness. Not a full ant or packet-ledger realization.')
(W/'chronology_dcuv/dc_eight_comb_relaxation.json').write_text(json.dumps(O,indent=2)+'\n');print(O)
