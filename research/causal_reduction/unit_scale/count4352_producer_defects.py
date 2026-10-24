"""Exact adjacent bad-ten count for the affine 394-cell prefix family.
Checks genuine inverse-ten history against all affine seed cells for N>=1,
and then derives the count from finite literal seams and stationary bodies.
"""
from pathlib import Path
import json,hashlib
from check4352_noncrossing_producer import setup,H,W,V
from check_prepared1564_router_geometry import infer
P=Path(__file__).resolve().parent
J=json.loads((P/'prepared4352_uniform_support_manifest.json').read_text())
factors={(H*2)[i:i+10]for i in range(len(H))}
# Source at the origin, W; exact time reversal keeps the board unchanged.
B=set(infer(H*30,(0,0),3)['input']);p=(1,0);h=1;inv=[];reads=[]
for i in range(10):
 c='L'if p in B else'R';reads.append(p);inv.append(c);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
history=''.join('L'if c=='R'else'R'for c in inv[::-1])
# Every non-source affine seed misses these ten exact reverse reads.
checks=0
for x,y in J['seed_families'][13:]:
 for q in reads:
  sx=x[0]-J['initial_pose']['x_N_constant'][0];cx=x[1]-J['initial_pose']['x_N_constant'][1]-q[0]
  sy=y[0]-J['initial_pose']['y_N_constant'][0];cy=y[1]-J['initial_pose']['y_N_constant'][1]-q[1]
  cand=None;possible=True
  for slope,constant in[(sx,cx),(sy,cy)]:
   if slope==0:
    if constant:possible=False;break
   elif (-constant)%slope:possible=False;break
   else:
    n=(-constant)//slope
    if cand is not None and cand!=n:possible=False;break
    cand=n
  assert not(possible and(cand is None or cand>=1));checks+=1

def run_word(w,hist):
 bad=hist not in factors;K=bad_tens=0
 for c in w:
  hist=(hist+c)[-10:];nb=hist not in factors;K+=bad and nb;bad_tens+=nb;bad=nb
 return K,bad_tens,hist
# Once a full H/W has passed its last ten history is independent of entry.
assert run_word(H*2,H[-10:])[0]==0
waveK=run_word(W,W[-10:])[0];assert waveK==1972
results=[]
for n in(1,2,3):
 hist=history;total=0;reports=[]
 for s in J['stages']:
  count=s['count_N_constant'][0]*n+s['count_N_constant'][1]
  # Each repeated body's first traversal establishes its final-ten history;
  # all further traversals have the exactly checked stationary contribution.
  k0,b0,h1=run_word(s['word'],hist)
  k1,b1,h2=run_word(s['word'],h1);assert h1==h2
  assert count>=1
  K=k0+(count-1)*k1;total+=K;hist=h1
  reports.append({'kind':s['kind'],'count':count,'first_K':k0,'stationary_K':k1,'total_K':K})
 results.append({'N':n,'total_K':total,'stages':reports})
# The all-N count is an affine symbolic sum, not extrapolation of controls.
hist=history; symbolic=[0,0]
for s in J['stages']:
 k0,b0,h1=run_word(s['word'],hist); k1,b1,h2=run_word(s['word'],h1); assert h1==h2
 a,b=s['count_N_constant']; assert a>=0 and a+b>=1
 symbolic[0]+=a*k1; symbolic[1]+=k0+(b-1)*k1; hist=h1
assert symbolic[0]==1972
constant=symbolic[1]
assert all(r['total_K']==symbolic[0]*r['N']+symbolic[1] for r in results)
out={'status':'PASS exact symbolic count','inverse_turn_word':''.join(inv),'true_previous_ten':history,'affine_reverse_seed_exclusions':checks,'wave_cyclic_K':1972,'prefix_total_K_N_constant':symbolic,'checks':results,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_producer_defects.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
