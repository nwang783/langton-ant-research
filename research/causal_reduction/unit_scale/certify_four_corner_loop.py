"""Exact constant43-black prepared closed-pose104 loop, all r>=3.
This proves a finite excursion family, not renewed corner markers or capture.
"""
from pathlib import Path
import json,sys,time,hashlib
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot,xor
from probe_perpendicular_highway_wake import H,shifted_seed
ctx=Context(max_operations=200000000);st=time.monotonic()
def S(c):return ctx.set('[r]->{[x,y]:r>=3 and ('+c+')}')
def corner(j,r):
 out=(0,0)
 for z in range(j):
  v=rot((2*r+3,2*r+6),z);out=(out[0]+v[0],out[1]+v[1])
 return out
def ccoeff(j):
 z=corner(j,0);o=corner(j,1);return(o[0]-z[0],o[1]-z[1]),z
def point(ax,bx,ay,by):return S(f'x={ax}*r+{bx} and y={ay}*r+{by}')
K=[tuple(q)for q in json.loads((P/'single_turn_highway_corner_certificate.json').read_text())['corner_relative_black']]
seed_families=[]
for x,y in shifted_seed(2,(1,0)):seed_families.append((0,x,0,y))
for j in range(1,4):
 a,b=ccoeff(j)
 for q in K:
  q=rot(q,j);seed_families.append((a[0],b[0]+q[0],a[1],b[1]+q[1]))
assert len(seed_families)==43
initial=S('false')
for rec in seed_families:
 z=point(*rec);assert initial.intersect(z).is_empty();initial=initial.union(z)
rows,_,_=trace(H,(1,0),1);F=[]
for j in range(4):
 a,b=ccoeff(j);D=rot((2,2),j)
 F.append((point(a[0],b[0],a[1],b[1]),(0,104*j,69*j),'R',f'cap{j}'))
 for z,(q,hh,c)in enumerate(rows):
  q=rot(q,j);bx=b[0]+q[0];by=b[1]+q[1]
  f=S(f'exists(i:0<=i<r and x={a[0]}*r+{bx}+{D[0]}*i and y={a[1]}*r+{by}+{D[1]}*i)')
  slope=104//D[0];tf=(slope,104*j-slope*a[0],69*j+1+z-slope*bx)
  F.append((f,tf,c,f'arm{j}:{z}'))
 for z,(q,hh,c)in enumerate(rows[:68 if j<3 else 60]):
  q=rot(q,j);f=point(a[0]+D[0],b[0]+q[0],a[1]+D[1],b[1]+q[1]);tf=(0,104*(j+1),69*j+1+z)
  F.append((f,tf,c,f'end{j}:{z}'))
def earlier(t,u):return f'{u[0]-t[0]}*x+{u[1]-t[1]}*r+{u[2]-t[2]}<0'
relations=0
for i,(f,tf,c,name)in enumerate(F):
 ctx.reset_operations();black=initial.intersect(f)
 for g,tg,cg,ng in F:
  meet=f.intersect(g)
  if meet.is_empty():continue
  prior=meet.intersect(S(earlier(tf,tg)))
  if not prior.is_empty():relations+=1;black=xor(black,prior)
 bad=f.subtract(black)if c=='L'else black
 assert bad.is_empty(),(name,str(bad))
 if i%100==0:print('verified',i,'of',len(F),'relations',relations,flush=True)
after=initial
for f,tf,c,name in F:after=xor(after,f)
assert initial.intersect(point(0,0,0,0)).is_empty();assert point(0,0,0,0).subtract(after).is_empty()
for r in(0,1):
 w=('R'+H*r+H[:68])*3+'R'+H*r+H[:60]
 rr,ep,eh=trace(w,(0,0),0);assert(ep,eh)==((0,0),0)
 assert len(w)==416*r+268 and w.count('R')-w.count('L')==48*r+44
retained=[];erased=[]
for i,rec in enumerate(seed_families):
 q=point(*rec)
 if q.subtract(after).is_empty():retained.append(i)
 else:assert q.intersect(after).is_empty();erased.append(i)
assert len(retained)==11 and len(erased)==32
out=dict(status='EXACT_ALL_R_CLOSED_POSE_EXCURSION',domain='r>=3',word='(R H^r H[:68])^3 R H^r H[:60]',length='416*r+268',initial_pose=[0,0,'N'],final_pose=[0,0,'N'],initial_mass=43,final_mass='48*r+87',charge='48*r+44',complete_xor_count='48*r+108',retained_input_cells=11,erased_input_cells=32,seed_families_ax_bx_ay_by=seed_families,initial_relation=str(initial.coalesce()),output_relation=str(after.coalesce()),read_families=len(F),prior_relations=relations,origin_final_black=True,next_unrepaired_turn='L',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-st)
(P/'four_corner_loop_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('seed_families_ax_bx_ay_by','initial_relation','output_relation')})
