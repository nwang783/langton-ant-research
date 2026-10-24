#!/usr/bin/env python3
from itertools import product
from collections import Counter
from pathlib import Path
import json
D=(1j,1,-1j,-1)
counts=Counter();legal=Counter();unique_nonzero=[]
for h0 in range(4):
 for c0 in (1,-1):
  parent=2*h0+(c0==-1);target=(h0+c0)%4
  for n in (1,5,9,13):
   for word in product((1,-1),repeat=n):
    z=0j;h=h0;hist={};possible=True;inc=[0]*8;selfpositions=[]
    for c in word:
     state=2*h+(c==-1);inc[state]+=1
     if state==parent:selfpositions.append(z)
     if hist.get(z)==c:possible=False
     hist[z]=c;h=(h+c)%4;z+=D[h]
    if h!=target or z!=D[target]:continue
    delta=inc[:];delta[parent]-=1;R=delta[::2];L=delta[1::2]
    A=L[0];B=L[1];zz=R[0]-B
    assert L==[A,B,A,B] and R==[B+zz,A+zz,B+zz,A+zz]
    assert min(A,B,A+zz,B+zz)>=0
    assert n==1+4*(A+B+zz) and sum(word)==c0+4*zz
    counts[n]+=1
    if possible:legal[n]+=1
    if len(selfpositions)==1 and selfpositions[0]!=0:
     unique_nonzero.append([n,parent,[int(selfpositions[0].real),int(selfpositions[0].imag)],possible])
out={'status':'PASS independent complete geometric incidence inventory','geometric_counts':dict(counts),'internally_legal_counts':dict(legal),'total_geometric':sum(counts.values()),'total_legal':sum(legal.values()),'unique_self_nonzero_geometric':len(unique_nonzero),'unique_self_nonzero_legal':sum(x[-1] for x in unique_nonzero),'scope':'Incidence theorem analytic; absence of legal unique-self nonzero offsets here is only a length<=13 control.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
