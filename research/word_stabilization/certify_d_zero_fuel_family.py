"""Literal finite ingredients for the all-n family U C C V D^n, n>=1.
The parameter proof is in d_zero_fuel_family.md, not a finite extrapolation.
"""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
q=json.loads(SOURCE.read_text());M=q['macro_words'];D=M[0]['word'];P=M[3]['word']+M[1]['word']*2+M[2]['word']
DIR=((0,1),(1,0),(0,-1),(-1,0))
def trace(w,start=(0,0,0)):
 x,y,h=start;out=[]
 for i,c in enumerate(w):
  out.append(((x,y),c,i));h=(h+(1 if c=='R'else-1))%4;x+=DIR[h][0];y+=DIR[h][1]
 return out,(x,y,h)
def replay(w):
 tr,end=trace(w);last={};first={};B=set()
 for p,c,t in tr:
  assert last.get(p,('?',-1))[0]!=c,(p,c,t,last[p])
  first.setdefault(p,(c,t));last[p]=(c,t)
 seed=sorted(p for p,(c,t) in first.items() if c=='L')
 return tr,end,seed
pre,pose=trace(P);one,end=trace(D,pose);v=(end[0]-pose[0],end[1]-pose[1]);assert pose[2]==end[2] and v==(-1,-1)
# Exact possible same-cell separations between two D copies.
seps=[]
for a,ca,ta in one:
 for b,cb,tb in one:
  dx=a[0]-b[0];dy=a[1]-b[1]
  if dx*v[1]==dy*v[0]:
   k=dx//v[0]
   if k>=0:seps.append(k)
K=max(seps);assert K==2
# Exact possible period indices whose reads meet P.
collisions=[]
for p,c,t in pre:
 for a,ca,ta in one:
  dx=p[0]-a[0];dy=p[1]-a[1]
  if dx*v[1]==dy*v[0]:
   k=dx//v[0]
   if k>=0:collisions.append((k,t,ta))
J=max(k for k,t,ta in collisions);assert J==1
# A first conflict after period J+K+1 would translate entirely inside a
# pure D^(K+2) window. This is a finite cover of all possible conflicts.
replay(D*(K+2));replay(P+D*(J+K+3))
# Exact fresh-L phase sets: beyond J and K all possible predecessors have
# stable existence. Thus one stable copy represents every later copy.
fresh=[]
tr,end,seed=replay(P+D*(J+K+3));seen=set()
for p,c,t in tr:
 if t>=len(P) and (t-len(P))%len(D)==0:fresh.append([])
 if t>=len(P) and p not in seen and c=='L':fresh[-1].append((t-len(P))%len(D))
 seen.add(p)
assert fresh==[[]]+[[1]]*(len(fresh)-1),fresh
# Bind the real port overapproximation, without asserting infinite physical
# extension: every finite type sequence 3,1,1,2,0,0,... has a graph path.
E=q['quotient_edges'];states={u for u,a,v in E}|{v for u,a,v in E}
def step(S,a):return {v for u,b,v in E if u in S and b==a}
S=states
for a in (3,1,1,2,0):S=step(S,a)
assert S
S0=set(S);orbit=[]
while frozenset(S) not in orbit:
 orbit.append(frozenset(S));S=step(S,0);assert S
# Independent complete finite-seed replay of shortest control.
tr,end,seed=replay(P+D);black=set(map(tuple,seed));x=y=h=0
for t,c in enumerate(P+D):
 assert ('L' if (x,y) in black else 'R')==c
 if (x,y) in black:black.remove((x,y))
 else:black.add((x,y))
 h=(h+(1 if c=='R'else-1))%4;x+=DIR[h][0];y+=DIR[h][1]
assert len(seed)==11 and len(black)==25
last={};reused=[]
for p,c,t in tr:
 if t>=len(P) and c=='L' and p not in {z[0] for z in tr[len(P):t]}:
  assert p in last;reused.append({'local_phase':t-len(P),'cell':p,'previous':last[p]})
 last[p]=(t,c)
result={'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'D':D,'P':P,'D_entry_pose':pose,'D_drift':v,'max_D_copy_overlap':K,'max_prefix_D_copy_overlap':J,'finite_cover_D_copies':J+K+3,'first_L_fresh_phases':fresh,'minimal_entry_mass_formula':'n+10 for n>=1','length_formula':'76+10n','shortest_seed':seed,'shortest_final_black':sorted(black),'shortest_end_pose':(x,y,h),'shortest_reused_first_L':reused,'port_start_states':sorted(S0),'D_state_set_orbit_length':len(orbit),'scope':'all n>=1 literal feasibility and finite seed; quotient path only, not infinite finite-support realization'}
(ROOT/'d_zero_fuel_family_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
