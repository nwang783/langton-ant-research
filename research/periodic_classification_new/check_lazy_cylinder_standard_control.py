#!/usr/bin/env python3
"""Author positive controls for the new lazy exact cylinder graph criterion."""
from pathlib import Path
from collections import defaultdict
import json
from synthesize_white_cylinder_lazy import validate,D
ROOT=Path(__file__).resolve().parents[1]
word=(ROOT/'word_stabilization/standard_word.txt').read_text().strip()
results=[]
for copies in (1,2,3):
 text=word*copies;P=len(text);d=(2*copies,2*copies);p=(-1,0);h=0;hist=defaultdict(list)
 for t,ch in enumerate(text):
  k=p[0]//d[0];q=p[0]-k*d[0],p[1]-k*d[1];c=1 if ch=='R' else -1
  hist[q].append((t-k*P,c,h));h=(h+c)%4;ax,ay=D[h];p=p[0]+ax,p[1]+ay
 assert p==(-1+d[0],d[1]) and h==0
 for v in hist.values():
  v.sort();assert all(c==(1 if j%2==0 else -1) for j,(t,c,h) in enumerate(v))
 w=max(abs(y-x) for x,y in hist);ps=[(r,r+v) for v in range(-w,w+1) for r in range(d[0])];ss=[];chosen=[]
 for p in ps:
  ss.append([('0',[]),('actual',[(c,h) for t,c,h in hist[p]])]);chosen.append(1 if hist[p] else 0)
 ok,cert=validate(ps,ss,chosen,d);assert ok,cert
 results.append(dict(period=P,drift=d,classes=sum(bool(hist[p]) for p in ps),max_multiplicity=max(len(hist[p]) for p in ps),seed_mass=len(cert['seed']),replayed_periods=cert['replayed_periods']))
result=dict(status='PASS_AUTHOR_POSITIVE_CONTROLS',controls=results)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
