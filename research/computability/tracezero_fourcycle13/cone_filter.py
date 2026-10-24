#!/usr/bin/env python3
"""Exact separated optimization of the signed curvature cone coefficient."""
from fractions import Fraction as Q
from pathlib import Path
import json,itertools
root=Path(__file__).parent;data=json.loads((root/'inventory.json').read_text())
domains=data['domains'];F=tuple(data['first_map']);A=((0,-3),(3,0));k=13
I=((Q(1),Q(0)),(Q(0),Q(1)))
def mm(a,b):return tuple(tuple(sum(a[i][h]*b[h][j] for h in range(2)) for j in range(2)) for i in range(2))
def mv(a,x):return tuple(sum(a[i][j]*x[j] for j in range(2)) for i in range(2))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def inv(a):
 z=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 return ((a[1][1]/z,-a[0][1]/z),(-a[1][0]/z,a[0][0]/z))
def power(a,n):
 p=I
 for _ in range(n):p=mm(p,a)
 return p
B=((Q(0),Q(-1,3)),(Q(1,3),Q(0))) # A^(-T)
def coeff(b):return Q(sum(b),4),(Q(b[1]-b[3],2),Q(b[0]-b[2],2))
def constants(bs,t,q):
 C=sum(coeff(bs[j-1])[0]/k**j for j in range(1,t+1))
 C+=Q(1,k**t)*sum(coeff(bs[t+j-1])[0]/k**j for j in range(1,q+1))/(1-Q(1,k**q))
 ell=(Q(0),Q(0))
 for j in range(1,t+1):ell=add(ell,mv(power(B,j),coeff(bs[j-1])[1]))
 tail=(Q(0),Q(0))
 for j in range(1,q+1):tail=add(tail,mv(power(B,j),coeff(bs[t+j-1])[1]))
 Bq=power(B,q);D=tuple(tuple(I[i][j]-Bq[i][j] for j in range(2)) for i in range(2))
 ell=add(ell,mv(mm(power(B,t),inv(D)),tail))
 return (C,)+ell
def map_powers(G):
 fp=tuple(range(4));gp=fp;seen={};states=[]
 while (fp,gp) not in seen:
  seen[fp,gp]=len(states);states.append((fp,gp))
  fp=tuple(F[x] for x in fp);gp=tuple(G[x] for x in gp)
 t=seen[fp,gp];return states,t,len(states)-t
records=[];best=None
for bits in itertools.product((0,1),repeat=4):
 G=tuple((F[d]+2*bits[d])%4 for d in range(4));states,t,q=map_powers(G)
 weighted=[]
 for d in range(4):
  opts=[]
  for index,row in enumerate(domains[d]):
   w=row['word']
   if w[-1]!=G[d]:continue
   bs=[]
   for fp,gp in states:
    b=[0]*4;b[d]=sum(1 if (fp[v]-gp[u])%4==1 else -1 for u,v in zip(w,w[1:]));bs.append(b)
   opts.append((index,constants(bs,t,q)))
  weighted.append(opts)
 # With C=0, maximize ell_y at root N. Separate two source pairs exactly.
 pairs=[]
 for d1,d2 in [(0,1),(2,3)]:
  mp={}
  for i,x in weighted[d1]:
   for j,y in weighted[d2]:
    C=x[0]+y[0];v=x[2]+y[2]
    if C not in mp or v>mp[C][0]:mp[C]=(v,(i,j),x[1]+y[1])
  pairs.append(mp)
 local=None
 for C,(ey,ij,ex) in pairs[0].items():
  if -C not in pairs[1]:continue
  fy,kl,fx=pairs[1][-C];candidate=(ey+fy,ij+kl,ex+fx)
  if local is None or candidate[0]>local[0]:local=candidate
 rec=dict(last_map=G,domain_sizes=list(map(len,weighted)),forcing_preperiod=t,forcing_period=q,
  first_pair_charge_values=len(pairs[0]),second_pair_charge_values=len(pairs[1]),
  max_ell_y=None if local is None else str(local[0]),
  maximizing_indices=None if local is None else local[1],
  maximizing_ell_x=None if local is None else str(local[2]))
 records.append(rec)
 if local is not None and (best is None or local[0]>best[0]):best=(local[0],G,local[1],local[2])
out=dict(status='EXACT CONE COEFFICIENT INVENTORY',matrix=A,k=k,first_map=F,
 controllers=len(domains[0])**4,last_maps=len(records),
 global_max_ell_y=None if best is None else str(best[0]),
 global_maximizer=None if best is None else dict(last_map=best[1],indices=best[2],ell_x=str(best[3])),
 necessary_finite_seed_condition='C=0 and ell_y>=2 for normalized root N',records=records)
(root/'cone_filter.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
