"""Exact goal-reachability pruning of a guarded-reset finite graph.
OUT reentries materialized, then ignore guards to retain vertices reachable from
start and able to reach a goal source. Fresh unreachable dummy OUT is reserved.
"""
import json,sys,hashlib
from pathlib import Path
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());n=J['out']+1;T=[list(t)for t in J['transitions']];T +=[[J['out'],p,0,0,0,0,0,0,99]for p in J['reentry']];adj=[[]for _ in range(n)];rev=[[]for _ in range(n)];goals=set()
for a,b,k,v,f,c,r,g,w in T:
 if g:goals.add(a)
 else:adj[a].append(b);rev[b].append(a)
def close(initial,graph):
 seen=set(initial);stack=list(seen)
 while stack:
  for y in graph[stack.pop()]:
   if y not in seen:seen.add(y);stack.append(y)
 return seen
reachable=close([J['start'][0]],adj);coaccessible=close(goals,rev);live=sorted(reachable&coaccessible);assert J['start'][0]in live,'pure graph already no-hit';ix={p:i for i,p in enumerate(live)};OUT=len(live);NT=[]
for a,b,k,v,f,c,r,g,w in T:
 if a not in ix or (not g and b not in ix):continue
 NT.append([ix[a],ix.get(b,OUT),k,v,f,c,r,g,w])
N={'format':'guarded_reset_live_pruning_v1','base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'n':J['n'],'out':OUT,'start':[ix[J['start'][0]],*J['start'][1:]],'transitions':NT,'reentry':[],'retained_old_positions':live,'reachable_ignoring_guards':sorted(reachable),'coaccessible_ignoring_guards':sorted(coaccessible),'scope':'Exact goal-reachability pruning after explicit OUT materialization; final OUT is fresh unreachable dummy.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {OUT+1} {len(NT)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for row in NT:f.write(' '.join(map(str,row))+'\n')
 f.write('\n')
print(json.dumps({'old_positions':n,'new_positions':OUT+1,'old_transitions':len(T),'new_transitions':len(NT)}))
