"""Exact43-black alternating r,s,r,s104 closed loop, all r,s>=3.
Only this finite excursion is certified. Its later collisions/capture are separate.
"""
from pathlib import Path
import json,sys,time,hashlib
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot,xor
from probe_perpendicular_highway_wake import H,shifted_seed
from unequal_loop_geometry import corner,word,K
ctx=Context(max_operations=200000000);st=time.monotonic()
def S(c):return ctx.set('[r,s]->{[x,y]:r>=3 and s>=3 and ('+c+')}')
def ccoeff(j):
 b=corner(j,0,0);a=corner(j,1,0);c=corner(j,0,1)
 return(a[0]-b[0],c[0]-b[0],b[0],a[1]-b[1],c[1]-b[1],b[1])
def point(ax,cx,bx,ay,cy,by):return S(f'x={ax}*r+{cx}*s+{bx} and y={ay}*r+{cy}*s+{by}')
seed=[]
for x,y in shifted_seed(2,(1,0)):seed.append((0,0,x,0,0,y))
for j in range(1,4):
 ax,cx,bx,ay,cy,by=ccoeff(j)
 for q in K:
  x,y=rot(q,j);seed.append((ax,cx,bx+x,ay,cy,by+y))
initial=S('false')
for rec in seed:
 z=point(*rec);assert initial.intersect(z).is_empty();initial=initial.union(z)
assert len(seed)==43
rows,_,_=trace(H,(1,0),1);F=[]
for j in range(4):
 ax,cx,bx,ay,cy,by=ccoeff(j);dx,dy=rot((2,2),j);n='r'if j%2==0 else's';nr=int(j%2==0);ns=1-nr
 tr=104*((j+1)//2);ts=104*(j//2);tc=69*j
 F.append((point(ax,cx,bx,ay,cy,by),(0,tr,ts,tc),'R',f'cap{j}'))
 for z,(q,h,c)in enumerate(rows):
  q=rot(q,j);qx=bx+q[0];qy=by+q[1]
  f=S(f'exists(i:0<=i<{n} and x={ax}*r+{cx}*s+{qx}+{dx}*i and y={ay}*r+{cy}*s+{qy}+{dy}*i)')
  sx=104//dx;tf=(sx,tr-sx*ax,ts-sx*cx,tc+1+z-sx*qx)
  F.append((f,tf,c,f'arm{j}:{z}'))
 for z,(q,h,c)in enumerate(rows[:68 if j<3 else 60]):
  q=rot(q,j);f=point(ax+dx*nr,cx+dx*ns,bx+q[0],ay+dy*nr,cy+dy*ns,by+q[1]);tf=(0,tr+104*nr,ts+104*ns,tc+1+z)
  F.append((f,tf,c,f'end{j}:{z}'))
def earlier(t,u):return f'{u[0]-t[0]}*x+{u[1]-t[1]}*r+{u[2]-t[2]}*s+{u[3]-t[3]}<0'
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
assert initial.intersect(point(0,0,0,0,0,0)).is_empty();assert point(0,0,0,0,0,0).subtract(after).is_empty()
for r,s in((0,0),(1,0),(0,1),(3,5)):
 w=word(r,s);rr,ep,eh=trace(w,(0,0),0);assert(ep,eh)==((0,0),0)
 assert len(w)==208*(r+s)+268 and w.count('R')-w.count('L')==24*(r+s)+44
retained=[];erased=[]
for i,rec in enumerate(seed):
 q=point(*rec)
 if q.subtract(after).is_empty():retained.append(i)
 else:assert q.intersect(after).is_empty();erased.append(i)
assert len(retained)==11 and len(erased)==32
out=dict(status='EXACT_ALL_R_S_CLOSED_POSE_EXCURSION',domain='r>=3,s>=3',word='R H^r H[:68] R H^s H[:68] R H^r H[:68] R H^s H[:60]',length='208*(r+s)+268',initial_pose=[0,0,'N'],final_pose=[0,0,'N'],initial_mass=43,final_mass='24*(r+s)+87',charge='24*(r+s)+44',complete_xor_count='24*(r+s)+108',retained_input_cells=11,erased_input_cells=32,seed_families_ar_as_bx_cr_cs_by=seed,initial_relation=str(initial.coalesce()),output_relation=str(after.coalesce()),read_families=len(F),prior_relations=relations,origin_final_black=True,next_unrepaired_turn='L',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-st)
(P/'unequal_four_corner_loop_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('seed_families_ar_as_bx_cr_cs_by','initial_relation','output_relation')},flush=True)
