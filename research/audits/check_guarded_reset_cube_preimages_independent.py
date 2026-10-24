"""Exhaustive boolean control for the proposed exact cube/resource product.
Checks only cube semantics; no record graph or resource exclusion is inferred.
"""
from itertools import product
from pathlib import Path
import json
n=3;full=(1<<n)-1
cubes=[]
for code in product((-1,0,1),repeat=n):
 mask=sum((a>=0)<<i for i,a in enumerate(code));value=sum((a==1)<<i for i,a in enumerate(code));cubes.append((mask,value))
count=empty=0
for modes in product(range(4),repeat=n): # identity,flip,reset0,reset1
 F=sum((a==1)<<i for i,a in enumerate(modes));C=sum((a>=2)<<i for i,a in enumerate(modes));R=sum((a==3)<<i for i,a in enumerate(modes))
 for K,V in cubes:
  for M,W in cubes:
   expected=[]
   for b in range(1<<n):
    if (b&K)!=V:continue
    out=0
    for i,a in enumerate(modes):
     bit=(b>>i)&1
     if a==1:bit=1-bit
     elif a==2:bit=0
     elif a==3:bit=1
     out|=bit<<i
    if out&M==W:expected.append(b)
   pred=None
   if not ((W^R)&M&C):
    N=M&~C;A=(W^F)&N
    if not ((A^V)&N&K):pred=(N|K,A|(V&K))
   actual=[] if pred is None else [b for b in range(1<<n) if b&pred[0]==pred[1]]
   assert actual==expected,(modes,K,V,M,W,actual,expected)
   count+=1;empty+=not actual
# Cube containment criterion independently checked by finite truth sets.
contain=0
for M,W in cubes:
 for N,Z in cubes:
  criterion=(M&~N)==0 and ((W^Z)&M)==0
  aset={b for b in range(1<<n) if b&M==W};bset={b for b in range(1<<n) if b&N==Z}
  assert criterion==(bset<=aset);contain+=1
out=dict(status='PASS exact guarded-reset cube preimages and containment',bits=n,all_guard_map_goal_cases=count,empty_preimages=empty,cube_containment_pairs=contain,scope='Analytic product-layer control only. No concrete V1/U1 model or no-hit invariant audited.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
