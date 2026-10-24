#!/usr/bin/env python3
"""Reconstruct the complete phase72 return layer and its drift-orbit normal form."""
from pathlib import Path
import json,hashlib
D4=((0,1),(1,0),(0,-1),(-1,0))
def step(B,p,h):
 b=p in B;B.symmetric_difference_update({p});h=(h+(-1 if b else 1))%4;u=D4[h];return(p[0]+u[0],p[1]+u[1]),h

def run(B,p,h,t):
 B=set(B)
 for _ in range(t):p,h=step(B,p,h)
 return B,p,h

def shift(B,d,k=1):return{(x+k*d[0],y+k*d[1])for x,y in B}
B,p,h=run(set(),(0,0),0,9977);entry=p;eh=h
_,q,hh=run(B,p,h,104);d=(q[0]-p[0],q[1]-p[1]);assert d==(-2,-2)
S=[];tmp=set(B);q=p;hh=h
for _ in range(104):
 if q not in S:S.append(q)
 q,hh=step(tmp,q,hh)
base=B&set(S);base1,_,_=run(base,p,h,104);W=base1^shift(base,d)
head=(p[0]-2,p[1]-8);depth=11;anchor=52262;obs=(head[0]+depth*d[0],head[1]+depth*d[1])
R,r,rh=run(base|{obs},p,h,anchor)
R1,r1,rh1=run(R,r,rh,104);e=(r1[0]-r[0],r1[1]-r[1]);assert e==(2,2)and rh1==rh
V=R1^shift(R,e)
L=W^shift(V,d)
# The source final layer has another translation by phaseLag=4.
L=shift(L,d,4)
def orbit(q):
 x,y=q;t=x-y;a=x%2;k=(a-x)//2
 assert (a-2*k,a-t-2*k)==q
 return(t,a),k
rows={}
for q in L:
 j,k=orbit(q);rows.setdefault(j,set()).add(k)
P=set();C=set();profiles=[]
for j,ks in sorted(rows.items()):
 t,a=j;p0=min(ks);odd=len(ks)%2
 if odd:P.add((a-2*p0,a-t-2*p0))
 residual=ks^{p0}if odd else ks
 bit=0
 for k in range(min(residual)if residual else 0,max(residual)if residual else -1):
  bit^=k in residual
  if bit:C.add((a-2*k,a-t-2*k))
 profiles.append({'t':t,'x_parity':a,'L_cells':len(ks),'odd':odd,'min_k':min(ks),'max_k':max(ks)})
assert L==P^C^shift(C,d)
q=len(P);assert q>0
controls=[]
for n in[0,1,2,5,17,80]:
 layers=set()
 for i in range(n):layers^=shift(L,d,i)
 straight=set()
 for i in range(n):straight^=shift(P,d,i)
 assert layers==straight^C^shift(C,d,n)
 assert len(straight)==q*n
 controls.append({'n':n,'actual_layer_mass':len(layers),'straight_mass':len(straight),'cap_error_bound':2*len(C)})
out={'status':'PASS','incoming_drift':d,'reverse_drift':e,'entry':entry,'phase_head':head,'anchor':anchor,
     'W_mass':len(W),'V_mass':len(V),'L_mass':len(L),'nonzero_orbit_profile_count':q,
     'finite_coboundary_cap_mass':len(C),'profiles':profiles,'controls':controls,
     'W':sorted(W),'V':sorted(V),'L':sorted(L),'P':sorted(P),'C':sorted(C),
     'scope':'Exact complete finite masks and GF2 drift-orbit algebra. Arbitrary-base return-map construction is analytic, not asserted by finite controls.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in{'W','V','L','P','C','profiles'}},indent=2))
