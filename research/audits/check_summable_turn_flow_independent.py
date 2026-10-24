from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(D/'SUMMABLE_BALANCED_TURN_FLOW_MANIFEST.json')=='28a356641c60aa440e20db3389928b556723eeaf77b5d5c525c6dbe65454d391';m=json.loads((D/'SUMMABLE_BALANCED_TURN_FLOW_MANIFEST.json').read_text())
for kind in('files','dependencies'):
 for f,h in m[kind].items():assert sha(D/f)==h
J=json.loads((D/'SUMMABLE_BALANCED_TURN_FLOW_CHECKED.json').read_text());vectors=[1j,1,-1j,-1];faces=lambda p:[p,p-1,p-1-1j,p-1j]
mat=[[F(3 if j==i else -1 if(j-i)%4==2 else 1,4)for j in range(4)]for i in range(4)]
for i in range(4):assert[mat[i][j]+mat[(i+1)%4][j]for j in range(4)]==[F(j in(i,(i+1)%4))for j in range(4)]
for i in(0,1):assert[mat[i][j]+mat[i+2][j]for j in range(4)]==[F(1,2)]*4
assert[sum(mat[i][j]for i in range(4))for j in range(4)]==[F(1)]*4
checks=0;log=[];profiles=[]
for r in(F(1,3),F(1,2),F(2,3),F(9,10)):
 A=lambda p:r**(abs(int(p.real))+abs(int(p.imag)));mass=lambda p:sum(A(q)for q in faces(p));norm=4*((1+r)/(1-r))**2
 for x,y in product(range(-20,21),repeat=2):
  p=complex(x,y);ff=faces(p);aa=[A(q)for q in ff];tt=[sum(mat[i][j]*aa[j]for j in range(4))for i in range(4)];u=max(aa)
  assert sorted(a/u for a in aa)==sorted([F(1),r,r,r*r])and min(tt)>=0 and (r==F(1,3)or min(tt)>0)
  assert sorted(t/u for t in tt)==sorted([(3+2*r-r*r)/4,(1+r)**2/4,(1+r)**2/4,(3*r-1)*(r+1)/4])
  for sector in range(2):
   axis=(x+y+sector)%2;outflow={};letters={1:F(0),-1:F(0)}
   for hi in(axis,axis+2):
    incoming=F(0)
    for turn in(-1,1):
     ho=(hi+turn)%4;corner=-vectors[hi]+vectors[ho];ci={1+1j:0,-1+1j:1,-1-1j:2,1-1j:3}[corner];val=tt[ci];incoming+=val;letters[turn]+=val;outflow[ho]=outflow.get(ho,F(0))+val
    assert incoming==sum(A(q)for q in set(ff)&set(faces(p-vectors[hi])))
   for ho,val in outflow.items():assert val==sum(A(q)for q in set(ff)&set(faces(p+vectors[ho])))
   assert letters[1]==letters[-1]==mass(p)/2;checks+=1
  for dx,dy in product((-1,1),repeat=2):assert mass(p)<=2*(mass(p+dx)+mass(p+dy*1j))
  if r==F(1,2):log.append([x,y,*map(str,tt)])
 assert mass(0j)/norm==(1-r)**2/4;profiles.append(dict(r=str(r),norm=str(norm),origin=str(mass(0j)/norm)))
assert hashlib.sha256(json.dumps(log,separators=(',',':')).encode()).hexdigest()==J['finite_exact_log_sha256'];assert profiles[1]==dict(r='1/2',norm='36',origin='1/16')
review=['The four-corner linear matrix is checked symbolically: adjacent corner sums equal exactly the shared-face edge pair, opposite corner sums equal one-half total node mass, and all four sum to total surrounding face mass. Fixed checkerboard direction makes those opposite pairs precisely R andL in both sectors, with every incoming/outgoing incidence conserved.','All radial adjacent face quadruples are u times(1,r,r,r²), up to rotation/reflection. Numerators are3+2r-r², twice(1+r)², and(3r-1)(r+1). Thus every turn is nonnegative for1/3<=r<1 and positive forr>1/3, uniformly over the whole lattice, not by sample extrapolation.','The exact tensor-product face sum is((1+r)/(1-r))², with each face contributing to four node masses. Total turn/head occupation mass is therefore4 times this sum; r1/2 normalization36 and origin1/16 follow. The stationary four-corner visit inequalities also follow directly because each adjacent mass ratio is at leastr, so2 times two predecessor masses is at least4r times local mass.','This is only a stationary directed edge/turn-frequency relaxation, NOT a finite seed, actual R/L visit alternation, deterministic ant orbit, recurrence example, or global attraction counterexample. It rules out deriving vanishing localized frequency from one-site equalR/L balance and conservation alone. The finite confined-interval theorem remains untouched.']
out=dict(status='PASS explicit all-lattice summable balanced-turn FLOW relaxation countercontrol, NOT AN ANT ORBIT',manifest=sha(D/'SUMMABLE_BALANCED_TURN_FLOW_MANIFEST.json'),dependencies=m['dependencies'],symbolic_corner_matrix=[[str(z)for z in row]for row in mat],exact_sector_vertex_checks=checks,parameter_controls=profiles,analytic_review=review,scope=m['scope'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
