"""Exact strong bisimulation quotient of finite age-Petri controls.

Edge labels are complete (C count, input tail vector, output count vector).
Per-control goal requirement sets are observable labels. Initial controls map
to their classes. No resource vector is coarsened or capped.
CLI INPUT.dat PREFIX.
"""
from pathlib import Path
import sys,json,hashlib,collections
src,out=map(Path,sys.argv[1:3])
with src.open()as f:
 m,np,ne,ni,ng=map(int,f.readline().split());d=5*m
 initial=list(map(int,f.readline().split()));assert len(initial)==ni
 goals=[tuple(map(int,f.readline().split()))for _ in range(ng)]
 edges=[tuple(map(int,f.readline().split()))for _ in range(ne)]
 assert not f.read().strip()
adj=[[]for _ in range(np)];obs=[set()for _ in range(np)]
for p,*r in goals:assert len(r)==d;obs[p].add(tuple(r))
ops=[];oi={}
for ei,e in enumerate(edges):
 p,q,a,c,*r=e;assert len(r)==d+m
 op=(c,*r)
 if op not in oi:oi[op]=len(ops);ops.append(op)
 adj[p].append((oi[op],q,ei))
def compress(keys):
 mp={};ans=[]
 for k in keys:
  if k not in mp:mp[k]=len(mp)
  ans.append(mp[k])
 return ans,len(mp)
ob=[tuple(sorted(v))for v in obs];cl,nc=compress(ob);history=[]
while True:
 sig=[(ob[p],tuple(sorted({(op,cl[q])for op,q,ei in adj[p]})))for p in range(np)]
 new,nn=compress(sig);history.append(nn);print('partition',len(history),'classes',nn,flush=True)
 if nn==nc:
  assert new==cl
  break
 cl,nc=new,nn
reps=[None]*nc
for p,c in enumerate(cl):
 if reps[c]is None:reps[c]=p
qe=[];qops=[]
for c,p in enumerate(reps):
 seen=set()
 for op,q,ei in adj[p]:
  key=(op,cl[q])
  if key in seen:continue
  seen.add(key);e=edges[ei]
  qe.append((c,cl[q],e[2],*ops[op]));qops.append(op)
qg=[(c,*r)for c,p in enumerate(reps)for r in ob[p]];qi=sorted({cl[p]for p in initial})
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{m} {nc} {len(qe)} {len(qi)} {len(qg)}\n');f.write(' '.join(map(str,qi))+'\n')
 for e in qg+qe:f.write(' '.join(map(str,e))+'\n')
N=dict(format='record_age_petri_control_bisimulation_v1',source_file=str(src.resolve()),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),places=m,old_controls=np,new_controls=nc,old_edges=ne,new_edges=len(qe),class_map=cl,representatives=reps,edge_operation_ids=qops,operations=ops,history=history,scope='Exact strong bisimulation of finite controls by complete resource-update labels(c,I,O) and complete per-control goal requirement sets. Initial controls map to their classes. Original packet labels are representative metadata only; full original model language constraints are preserved in the control quotient. No count/age abstraction is added.')
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
print(dict(old_controls=np,new_controls=nc,old_edges=ne,new_edges=len(qe),operations=len(ops)),flush=True)
