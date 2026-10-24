"""Named complete-board controls for the actual cap6 corner writer's output trap.
No all-return file or generic board scan is used. Both graph sectors are retained.
"""
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import rot,cursor,ends,sector,vertices,comp,step
SRC=ROOT/'reframe_finite_seed_2026-10-24/cap6_resource_obstruction.json'
W0=json.loads(SRC.read_text())['cycles'][0];W=W0['word'];assert W=='RRRRLRLRRL'
D0={(-1,1),(-1,2)};D={(-2,1),(-2,2)};S={(0,-1),(1,-1),(1,0)};T={(-1,0)}
def tr(C,p,h):return {(p[0]+v[0],p[1]+v[1])for q in C for v in[rot(tuple(q),h)]}
def zcursor(p,h):
 a,b=rot((-1,-1),h);return 2*p[0]+a,2*p[1]+b
def components(B,k):
 out=[];seen=set()
 for q in sorted(B):
  if q not in seen:
   C=comp(B,k,ends(q,k)[0]);seen|=C;out.append(sorted(C))
 return out

def run(name,seed,expected_exit):
 B=set(seed);p=(0,0);h=0;k=sector(p,h);assert k==1
 trace=[];first_exit=None;initial=set(B)
 for t in range(20):
  C=comp(B,k,cursor(p,h));Z=comp(B,1-k,zcursor(p,h))
  if len(C)>6 and first_exit is None:first_exit=t
  if t<10:
   a=W0['transitions'][t];assert C==tr(a['input_component'],p,h)
   assert a['turn']==('L'if p in B else'R')
  if t==10:
   assert(p,h)==((-1,3),0)and not C
   assert comp(B,k,(-3,3))==D
   assert D|S|T<=B and B-(D|S|T)==initial-D0
   output=dict(pose=[p,h],full_black=sorted(B),w_components=components(B,k),z_components=components(B,1-k))
  c='L'if p in B else'R';ww=cursor(p,h);u,v=ends(p,k);other=v if u==ww else u
  imported=comp(B,k,other)if c=='R'and other not in vertices(C,k)|{ww}else set()
  trace.append(dict(cut=t,pose=[p,h],w_cursor=ww,z_cursor=zcursor(p,h),active_w_mass=len(C),active_z_mass=len(Z),turn=c,imported_w_component=sorted(imported)))
  p,h=step(B,p,h)
 assert first_exit==expected_exit and first_exit<=19
 return dict(name=name,initial_black=sorted(initial),initial_mass=len(initial),writer_word=W,writer_output=output,first_active_w_cap6_exit=first_exit,trace=trace)

controls=[run('minimal actual corner writer',D0,17),run('writer plus fully pre-funded next identical input corner',D0|{(-2,4),(-2,5)},14),run('minimal writer plus remote unread isolated component',D0|{(100,100)},17)]
# Forced geometry of the universal output class (independent of sampled fields).
r=(-1,5);u=(-3,7);DV=vertices(D,1)
first_q=[(-1,3),(0,3),(0,2),(-1,2)]
first_other=[]
for q in first_q:
 a,b=ends(q,1);assert r in(a,b);first_other.append(b if a==r else a)
assert [x in DV for x in first_other]==[False,False,False,True]
G=D|set(first_q[1:]);assert len(G)==5 and comp(G,1,r)==G and u not in vertices(G,1)
# After the forced L at(-1,3), root u is isolated; r is one of its four neighbors.
assert all(abs(a-b)==2 for a,b in zip(r,u))
out=dict(status='PASS named full-board cap6 corner-writer output trap',source_sha256={str(SRC.relative_to(ROOT)):hashlib.sha256(SRC.read_bytes()).hexdigest()},fixed_sector=dict(w=1,z=0),universal_output_geometry=dict(head=[-1,3],heading=0,empty_w_cursor=r,complete_corner=sorted(D),corner_vertices=sorted(DV),four_mandatory_R_cells=first_q,four_R_other_endpoints=first_other,first_corner_contact_R=3,forced_five_edge_archive=sorted(G),following_empty_cursor=u,following_four_R_contains_old_archive_vertex=r),controls=controls,scope='The arbitrary-exterior <=9-update output-trap theorem is analytic. These3 named full-board controls preserve all initial fuel and both graph roles; same-word WW failure is weaker than the universal continuation obstruction.')
(OUT/'corner_writer_port_trap_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'controls':[{'name':a['name'],'initial_mass':a['initial_mass'],'first_exit':a['first_active_w_cap6_exit']}for a in controls],'geometry':out['universal_output_geometry']},indent=2))
