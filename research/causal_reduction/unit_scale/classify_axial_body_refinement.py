"""Complete arbitrary child-choice classification of one exact supplied17-read body."""
from pathlib import Path
import json,hashlib
import certify_short_refinement_rup as core
P=Path(__file__).parent;U='RRLRRRRL';V='LLRLLRLL';W=U+'R'+V
rows,_,_=core.trace(W,(0,0),0)
blocks=[]
for p,h,c in rows:
 w=W if c=='R' else W.translate(str.maketrans('RL','LR'))
 rr,end,hh=core.trace(w,p,h)
 single,end0,hh0=core.trace(c,p,h)
 assert(end,hh)==(end0,hh0)
 blocks.append([single,rr])
last={};events=[];survivors=[];conflicts=[];nodes=0

def dfs(j,mask):
 global nodes
 nodes+=1
 if j==len(blocks):
  I=set();B=set();seen=set()
  for p,h,c in events:
   if p not in seen:
    seen.add(p)
    if c=='L':I.add(p);B.add(p)
   assert(p in B)==(c=='L')
   if p in B:B.remove(p)
   else:B.add(p)
  survivors.append(dict(mask=mask,length=len(events),input=sorted(I),output=sorted(B),active=[i for i in range(17) if mask>>i&1]))
  return
 for bit in(0,1):
  old=[];count=0;conflict=None
  for p,h,c in blocks[j][bit]:
   if p in last and last[p][1]==c:
    conflict=dict(cell=p,previous=last[p],current=[len(events),c]);break
   old.append((p,last.get(p)));last[p]=(len(events),c);events.append((p,h,c));count+=1
  mm=mask|(bit<<j)
  if conflict is not None:conflicts.append(dict(assigned=j+1,mask=mm,conflict=conflict))
  else:dfs(j+1,mm)
  for p,v in reversed(old):
   if v is None:del last[p]
   else:last[p]=v
  if count:del events[-count:]

dfs(0,0)
# Conflict assignment cubes are prefix leaves of this complete binary tree.
assert sum(1<<(17-x['assigned']) for x in conflicts)+len(survivors)==1<<17
out=dict(scope=__doc__,body=W,body_rows=rows,nodes=nodes,conflict_cubes=conflicts,survivors=survivors,covered_assignments=1<<17,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'axial_body_refinement_classification.json').write_text(json.dumps(out,indent=2)+'\n')
print(dict(nodes=nodes,conflict_cubes=len(conflicts),survivors=[dict(mask=x['mask'],active=x['active'],length=x['length'])for x in survivors]))
