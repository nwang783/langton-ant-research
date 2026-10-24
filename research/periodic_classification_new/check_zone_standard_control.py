#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import json
from probe_diagonal_zone_general import transitions,INF
D=[(0,1),(1,0),(0,-1),(-1,0)]
root=Path(__file__).resolve().parents[1];word=(root/'word_stabilization/standard_word.txt').read_text().strip()
results=[]
for copies in (1,2,3):
 text=word*copies;P=len(text);n=2*copies;p=(-1,0);h=0;hist=defaultdict(list)
 for t,ch in enumerate(text):
  k=p[0]//n;q=p[0]-k*n,p[1]-k*n;c=1 if ch=='R' else -1
  hist[q].append((t-k*P,c,h));h=(h+c)%4;dx,dy=D[h];p=p[0]+dx,p[1]+dy
 for es in hist.values():
  es.sort();assert all(c==(1 if j%2==0 else -1) for j,(t,c,h) in enumerate(es))
 lo=min(y-x for x,y in hist)-1;hi=max(y-x for x,y in hist)+1
 old=[() for _ in range(n)];states={((),())};records=[];terminal=False
 for row in range(lo,hi+1):
  new=[tuple(h for t,c,h in hist[i,i+row]) for i in range(n)];times={(i,j):t for i in range(n) for j,(t,c,h) in enumerate(hist[i,i+row])}
  outputs=set();matching=0
  for paths,flat in states:
   out,reason=transitions(paths,flat,old,new,(row-1)%2,phase_times=times,P=P)
   if out==['POTENTIAL_COMPLETE_FRONT']:terminal=True;break
   for np,nd in out:
    if np:
     anchor=times[np[0][0]]
     order=sorted(np,key=lambda path:(times[path[0]]-anchor)%P)
     if list(np)!=order:continue
     vv=sorted({j for a,b,w in np for j in (a,b)});z={e:(times[e]-anchor)//P for e in vv}
     if not all(nd[i*len(vv)+j]>=INF or z[a]-z[b]<=nd[i*len(vv)+j] for i,a in enumerate(vv) for j,b in enumerate(vv)):continue
    outputs.add((np,nd));matching+=1
  records.append(dict(row=row,surviving_actual_zones=len(outputs),terminal=terminal))
  if terminal:break
  assert outputs,('actual_front_lost',copies,row,records)
  states=outputs;old=new
 assert terminal
 results.append(dict(period=P,full_drift=[n,n],rows=records))
result=dict(status='PASS_AUTHOR_POSITIVE_CONTROLS',controls=results)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
