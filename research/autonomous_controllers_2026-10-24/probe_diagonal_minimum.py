#!/usr/bin/env python3
from itertools import product
from collections import Counter
import json
import probe_boundary_extension as p
from probe_consecutive_port_generator import generate

def analyze(T,B0,B1):
 H=[(3,),T,B0,B1];kind,G=p.graph(H)
 if kind!='open':return {'bottom':[T,B0,B1],'lower':kind}
 cy=p.positive_clock_cycle(H,G)
 if cy:return {'bottom':[T,B0,B1],'lower':'clock','witness':cy}
 rel=p.relations(H,G);oc=lambda hs,d:sum((h+(1 if k%2==0 else-1))%4==d for k,h in enumerate(hs))
 W0=generate(oc(B1,1),B0.count(2),True,rel[0]);W1=generate(oc(B0,1),B1.count(2),True,rel[1]);cc=Counter();s=[]
 for a,b in product(W0,W1):
  hh=H+[a,b];k,g=p.graph(hh)
  if k=='open'and p.positive_clock_cycle(hh,g):k='clock'
  cc[k]+=1
  if k=='open':s.append([''.join('NESW'[x]for x in hs)for hs in hh[-2:]])
 return {'bottom':[''.join('NESW'[x]for x in hs)for hs in H],'relations':rel,'A_words':[[ ''.join('NESW'[x]for x in hs)for hs in W]for W in(W0,W1)],'counts':dict(cc),'survivors':s}
if __name__=='__main__':
 out=[]
 for b0,b1 in product([(0,),(0,2)],[(2,),(2,2)]):out.append(analyze((),b0,b1))
 for b0,b1 in product([(2,2,0),(2,2,0,2),(0,2,2),(0,2,2,2)],repeat=2):out.append(analyze((3,),b0,b1))
 print(json.dumps(out,indent=2));open('/tmp/diagonal_minimum.json','w').write(json.dumps(out,indent=2))
