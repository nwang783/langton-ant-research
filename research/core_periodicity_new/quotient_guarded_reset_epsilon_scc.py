"""Exact epsilon-SCC quotient of a finite guarded-reset graph.
Explicitly materializes OUT reentries as identity edges, collapses SCCs of
zero-guard/zero-effect/non-goal transitions, and reserves a fresh unreachable
last OUT node so the existing engine's special OUT rule remains harmless.
CLI MODEL.json PREFIX. Proof of graph reachability equivalence is elementary;
independent checker still required before relying on a no-hit certificate.
"""
import json,sys,hashlib
from pathlib import Path
from collections import deque
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());np=J['out']+1;T=[list(t)for t in J['transitions']];T +=[[J['out'],p,0,0,0,0,0,0,99]for p in J['reentry']];adj=[[]for _ in range(np)];rev=[[]for _ in range(np)]
for a,b,k,v,f,c,r,g,w in T:
 if k==0 and f==0 and c==0 and g==0:adj[a].append(b);rev[b].append(a)
seen=set();order=[]
for a in range(np):
 if a in seen:continue
 seen.add(a);stack=[(a,0)]
 while stack:
  x,i=stack[-1]
  if i==len(adj[x]):order.append(x);stack.pop();continue
  y=adj[x][i];stack[-1]=(x,i+1)
  if y not in seen:seen.add(y);stack.append((y,0))
cl=[-1]*np;classes=[]
for a in reversed(order):
 if cl[a]>=0:continue
 cid=len(classes);members=[];todo=[a];cl[a]=cid
 while todo:
  x=todo.pop();members.append(x)
  for y in rev[x]:
   if cl[y]<0:cl[y]=cid;todo.append(y)
 classes.append(sorted(members))
new=set();mapping=[]
for i,(a,b,k,v,f,c,r,g,w)in enumerate(T):
 row=(cl[a],cl[b],k,v,f,c,r,g,w)
 if row[0]==row[1]and k==f==c==g==0:continue
 new.add(row)
new=sorted(new);OUT=len(classes);start=[cl[J['start'][0]],*J['start'][1:]];N={'format':'guarded_reset_epsilon_scc_quotient_v1','base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'n':J['n'],'out':OUT,'start':start,'transitions':new,'reentry':[],'classes':classes,'old_to_class':cl,'scope':'Exact epsilon-SCC reachability quotient. Actual OUT is materialized as ordinary identity edges; last OUT is a fresh unreachable dummy.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {OUT+1} {len(new)} 0\n");f.write(' '.join(map(str,start))+'\n')
 for row in new:f.write(' '.join(map(str,row))+'\n')
 f.write('\n')
print(json.dumps({'old_positions':np,'new_positions':OUT+1,'old_transitions':len(T),'new_transitions':len(new),'largest_scc':max(map(len,classes))}))
