"""Literal geometry and finite boundary algebra for the conditional shuttle.
No cap existence is asserted. Infinite horizontal arm classes are solved by
integer incidence, not truncated simulated arms.
"""
import json
from pathlib import Path
W='LLRLRRRRLRRRRLLLLRLL';S='RLLR';dirs=((0,1),(1,0),(0,-1),(-1,0))
def trace(w):
 x=y=0;h=1;out=[]
 for i,c in enumerate(w):
  out.append((x,y,c,i));h=(h+(1 if c=='R' else -1))%4;dx,dy=dirs[h];x+=dx;y+=dy
 return out,(x,y,h)
WT,we=trace(W);ST,se=trace(S);assert we==(-2,0,1) and se==(2,0,1)
rows=[]
for side,inc,out,step,oy,expect in [('left',WT,ST,2,4,[2,1,-1,0]),('right',ST,WT,-2,0,[-2,-1,1,0])]:
 onsets=[x+step for x,y,c,i in inc]+[x for x,y,c,i in out];lo=min(onsets)-2;hi=max(onsets)+2
 def groups(x):
  d={r:[] for r in range(4)}
  for ev,first,offset,sgn,length in ((inc,1,0,-1,len(inc)),(out,0,oy,1,len(out))):
   for a,b,c,i in ev:
    if (x-a)%step==0:
     k=(x-a)//step
     if k>=first:d[(b+offset)%4].append((-(b+offset),sgn*length*k+i,c))
  return {r:''.join(v[2] for v in sorted(g)) for r,g in d.items()}
 charge=[0]*4;delta=0
 for x in range(lo,hi+1):
  for r,s in groups(x).items():
   e=s.count('R')-s.count('L');charge[r]+=(-1 if x%2 else 1)*e;delta+=e
 assert charge==expect and delta==(2 if side=='left' else -2)
 # Beyond all arm onsets, every incidence has k>=its threshold. A shift
 # by step shifts each incoming phase negatively and outgoing phase positively;
 # their relative within-layer order stays incoming-before-outgoing.
 for parity in (0,1):
  x=(hi+4+parity if side=='left' else lo-4-parity)
  g=groups(x);assert g==groups(x+step)
  assert all(not s or s[0]=='R' and all(a!=b for a,b in zip(s,s[1:])) and s.count('R')==s.count('L') for s in g.values())
 rows.append(dict(side=side,arm_excess=delta,alternating_x_charge=charge,finite_boundary_columns=[lo,hi]))
# All eight local pose identities are linear in a(y-1),a(y),a(y+1),A(y).
# Check a basis and both x parities, enough for the universal integer identity.
def g(x,y,h,a):
 def antideriv(k):return sum(a.get(j,0) for j in range(k)) if k>=0 else -sum(a.get(j,0) for j in range(k,0))
 s=(-1 if x%2 else 1);v=a.get(y,0);A=2*antideriv(y)
 return (A,A+s*v,A+2*v,A-s*v)[h]
cases=0
for ay in (-1,0,1):
 a={ay:1}
 for x in (0,1):
  for h in range(4):
   for turn in (1,-1):
    hh=(h+turn)%4;dx,dy=dirs[hh]
    assert (g(x+dx,dy,hh,a)-g(x,0,h,a)+turn*((-1)**x)*a.get(0,0))%4==0;cases+=1
out=dict(status='PASS',rows=rows,local_charge_basis_cases=cases,scope='conditional all-period gluing and cap budgets only; no valid cap supplied')
Path('/workspace/shared/langton/audits/mixed_shuttle_charges_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
