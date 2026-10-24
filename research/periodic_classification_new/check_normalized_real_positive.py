#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import json
from frontier_drift_geometry import Geometry
from probe_general_drift_zone_core import splice
from probe_normalized_real_zone_core import transitions,INF
D=[(0,1),(1,0),(0,-1),(-1,0)]
root=Path(__file__).parent;word=(root.parent/'word_stabilization/standard_word.txt').read_text().strip();controls=[]
for copies in (1,2,3):
 P=104*copies;n=2*copies;g=Geometry(n,n);hist=defaultdict(list);p=(-1,0);h=0
 for t,ch in enumerate(word*copies):
  k=p[0]//n;q=(p[0]-k*n,p[1]-k*n);hist[q].append((t-k*P,h,ch));h=(h+(1 if ch=='R' else -1))%4;dx,dy=D[h];p=(p[0]+dx,p[1]+dy)
 assert p==(-1+n,n) and h==0
 lo=min(y-x for x,y in hist);hi=max(y-x for x,y in hist);old=[() for _ in range(n)];paths=();flat=();steps=0;terminal=False
 for row in range(lo,hi+2):
  new=[];clocks={}
  for c in range(n):
   es=sorted(hist[c,c+row]);hs=tuple(h for t,h,ch in es);assert all(ch==('R' if j%2==0 else 'L') for j,(t,h,ch) in enumerate(es));new.append(hs)
   for j,(t,h,ch) in enumerate(es):clocks[c,j]=Fraction(8*t,P)
  outs,reason=transitions(paths,flat,old,new,(row-1)%2,lambda a,b,c,d,e:splice(a,b,c,d,e,g),2,16,8);assert outs,(copies,row,reason)
  steps+=1
  if outs==['POTENTIAL_COMPLETE_FRONT']:
   terminal=True;break
  assert len(outs)==1;paths,flat=outs[0];vs=sorted({e for a,b,w in paths for e in (a,b)});nv=len(vs)
  for i,a in enumerate(vs):
   for j,b in enumerate(vs):
    code=flat[i*nv+j]
    if code>=INF:continue
    bound=(code+1)//2 if code&1 else code//2;diff=clocks[a]-clocks[b]
    assert diff<bound if code&1 else diff<=bound,(copies,row,a,b,diff,code)
  old=new
 assert terminal,copies
 controls.append(dict(period=P,full_drift=[n,n],rows=hi-lo+1,transitions=steps,status='ACCEPTED_NECESSARY_RELAXATION_WITH_EXACT_CLOCK_WITNESS'))
out=dict(status='AUTHOR_POSITIVE_CONTROLS_PASS',controls=controls);(root/'normalized_real_positive.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
