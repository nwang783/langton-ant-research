"""Author controls: exact unary masks and guards with explicit FREE CORE TRANSPORT.
NOT a physical word; no endpoint continuity or signed DCV word theorem is claimed.
"""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;P=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(P.read_text());K={tuple(p)for p in G['core']};geo=G['geometry'];Q=W/'genealogy_saturation_roles_frozen_20261023_0833/01_graph.json';J=json.loads(Q.read_text());roles=J['roles'];E={tuple(e)for e in J['all_fundamental_edges']}
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
base=[]
for r in range(12):
 h=(-r)%4;l=r//4;base.append(rot((100+10*l,-100+h%2),h))
S={add(base[r],rot((0,1),-r)):None for r in range(12)}
assert len(S)==12
lastpost=None;jumps=0;events=0
for C in range(16000):
 todo=[]
 if C>=7:
  r=(C-7)%12;j=(C-7)//12;h=(-r)%4
  todo.append((0,add(base[r],rot((j+1,-3*j),h)),(h+1)%4,7,r,j))
 r=C%12;j=C//12;h=(-r)%4
 todo.append((1,add(base[r],rot((j,-3*j),h)),h,5,r,j))
 for a,head,h,age,r,j in todo:
  assert h==(-C)%4 and(sum(head)+h)%2==0
  core={add(head,rot(p,h))for p in K};ins={add(head,rot(p,h))for p in geo[a]['inputs']};outs={add(head,rot(p,h))for p in geo[a]['outputs']}
  assert not any(p in S for p in core)
  for x,y,black,*_ in geo[a]['requirements']:
   p=add(head,rot((x,y),h));assert(p in S or p in core)==black,(C,a,r,j,p,black)
  assert len(ins)==1
  birth=S.pop(next(iter(ins)));assert birth is None and a==1 and j==0 or birth is not None and C-birth==age
  for p in outs:assert p not in S;S[p]=C
  dx,dy,dh=geo[a]['endpoint'];posthead=add(head,rot((dx,dy),h));posth=(h+dh)%4
  postcore={add(posthead,rot(p,posth))for p in K};assert not any(p in S for p in postcore)
  raw={add(head,rot(p,h))for p in geo[a]['raw_odd']}
  assert core^ins^outs^postcore==raw
  if lastpost is not None and lastpost!=(head,h):jumps+=1
  lastpost=(posthead,posth);events+=1
 assert len(S)==12+3*(C+1)
for h in range(4):
 u=roles.index([1,[2,0],h]);v=roles.index([0,[2,0],(h+1)%4]);assert(u,v,7,rot((2,-1),h+1)[1])in E
 for out in geo[1]['outputs']:
  u=roles.index([0,[2,0],(h+1)%4]);v=roles.index([1,out,h]);assert(u,v,5,rot((out[0],out[1]-1),h)[1])in E
U=[]
for a,head,h in[(1,(0,0),0),(0,(1,0),1)]:
 for x,y,*_ in geo[a]['requirements']:
  p=add(head,rot((x,y),h));U.append(3*p[0]+p[1])
O=dict(status='AUTHOR_GUARDED_UNARY_RELAXATION_PASS_NOT_PHYSICAL',initial_residual_roots=12,checked_C_events=16000,packet_instances=events,final_residual_mass=len(S),core_size=5,DC_to_D_age=7,D_to_DC_age=5,per_stream_DC_head_shift=[1,-3],zero_additional_sibling_retirements=True,role_edges_pass=True,local_context_band_3x_plus_y=[min(U),max(U)],parallel_band_separation=30,endpoint_continuity_failures=jumps,scope='All actual D/DC input/output masks, complete guards, disjoint current/post cores, birth clocks and sectors. Free five-core transport is explicitly inserted between packets. NOT a physical word; does not satisfy the actual head endpoint relation or challenge signed DCV finite-factor bounds.',dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[P,Q,Path(__file__).resolve()]})
T=W/'chronology_dcuv/dc_d_guarded_comb_relaxation.json';T.write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(O,indent=2))
