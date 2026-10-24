"""Fixed-color overlap diagnostic for a deep-SW inverse-standard tail.
No path or launch is inferred from a finite mismatch mask.
"""
from pathlib import Path
from collections import defaultdict
import json
P=Path(__file__).resolve().parent;G=P.parents[1]/'nonlinear_global_budget_2026-10-23'
H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H'];I=H[::-1].translate(str.maketrans('RL','LR'))
N=json.loads((G/'prepared_wave_five_band_normal_form.json').read_text());J=json.loads((G/'prepared_travelling_wave_certificate.json').read_text())
V=((0,1),(1,0),(0,-1),(-1,0));bulk={tuple(j)for j in N['full_black_orbit_profiles']};cap={tuple(q)for q in N['finite_XOR_cap']}
def trace(w,p,h):
 rows=[]
 for i,c in enumerate(w):
  rows.append((i,p,h,c));h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
 return rows,p,h
wr,_,_=trace(J['word'],tuple(N['pose'][0]),N['pose'][1]);ray={}
for _,(x,y),_,_ in wr:
 key=x-y,x%14;k=x//14;ray[key]=min(k,ray.get(key,k))
def future(p):
 x,y=p;return (x-y,x%14)in ray and x//14>=ray[x-y,x%14]
def bcolor(p):return (p[0]-p[1],p[0]%2)in bulk
q=(-214,-216);ir,_,_=trace(I,q,1);orb=defaultdict(list)
for i,p,h,c in ir:
 x,y=p;orb[x-y,x%2].append((i-104*(x//2),x//2,c))
def need(p):
 x,y=p;K=x//2;cand=[(t,c)for t,k,c in orb.get((x-y,x%2),[])if k<=K]
 return min(cand)[1] if cand else None
badbulk=[]
for key,slots in orb.items():
 ch=min(slots)[2]
 if (ch=='L')!=(key in bulk):badbulk.append([key,ch])
assert not badbulk
start=tuple(N['pose'][0]);h=N['pose'][1];p=(start[0]-V[h][0],start[1]-V[h][1]);h=(h+2)%4
flips=set();out=[];history=[]
for n in range(121):
 bad=[]
 for z in cap^flips:
  nc=need(z)
  if future(z)and nc is not None and (bcolor(z)^(z in cap)^(z in flips))!=(nc=='L'):bad.append(z)
 if n<32 or n%12==0:out.append({'depth':n,'pose':[p,h],'future_fixed_tail_mismatches':sorted(bad)})
 if n==120:break
 c='L'if bcolor(p)^(p in cap)^(p in flips)else'R';history.append([n,p,h,c,future(p)])
 flips.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
result={'scope':__doc__,'canonical_I_start':[q,1],'steady_bulk_mismatches':badbulk,'samples':out,'actual_inverse_first_120':history}
(P/'inverse_wave_tail_overlap.json').write_text(json.dumps(result,indent=2)+'\n')
print('bulk mismatch',badbulk)
for z in out:print(z)
