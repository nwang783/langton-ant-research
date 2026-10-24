"""Refine saved necessary local clock controls by exact event collisions.
This does not realize any exterior ant path or add off-Gamma event order.
"""
from pathlib import Path
from collections import defaultdict,deque,Counter
import ast,json
src=Path(__file__).with_name('canonical_three_child_square_closure.py').read_text();tree=ast.parse(src)
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0))
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name=='outs'],type_ignores=[]),'out','exec'))
def check(row):
 hh={ast.literal_eval(p):s for p,s in row['headings'].items()};oo={p:outs(h)for p,h in hh.items()};ns=[(p,r)for p,h in hh.items()for r in range(len(h))];ad=defaultdict(list)
 for p,h in hh.items():
  for o in ('EW'if h[0]in'NS'else'NS'):
   dx,dy=V[o];w=(p[0]+dx,p[1]+dy)
   if w not in hh:continue
   a=[(p,r)for r,x in enumerate(oo[p])if x==o];b=[(w,r)for r,x in enumerate(hh[w])if x==o]
   if len(a)!=len(b):return 'ports'
   for x,y in zip(a,b):ad[x].append((y,1));ad[y].append((x,-1))
 seen={};cs=[]
 for n in ns:
  if n in seen:continue
  seen[n]=0;cc=[n];q=deque([n])
  while q:
   u=q.popleft()
   for v,d in ad[u]:
    z=seen[u]+d
    if v in seen:
     if seen[v]!=z:return 'equalities'
    else:seen[v]=z;cc.append(v);q.append(v)
  ts=defaultdict(list)
  for p,r in cc:ts[seen[p,r]].append((p,r))
  if any(len(v)>1 for v in ts.values()):return 'same_time_collision'
  for t in ts:
   if t+1 not in ts:continue
   p,r=ts[t][0];w,s=ts[t+1][0];o=oo[p][r];dx,dy=V[o]
   if w!=(p[0]+dx,p[1]+dy)or hh[w][s]!=o:return 'consecutive_pose_collision'
  cs.append(dict(length=len(cc),span=max(ts)-min(ts)))
 return cs
s=Path(__file__).with_name('canonical_duplicator_local_parent_return.json');a=json.loads(s.read_text());rr=[];counts=Counter()
for row in a['rows']:
 r=check(row)
 if isinstance(r,str):counts[r]+=1
 else:rr.append(dict(**row,equality_components=r));counts['retained']+=1
out=dict(scope=__doc__,source_count=len(a['rows']),counts=counts,rows=rr)
Path(__file__).with_name('canonical_duplicator_local_parent_return_collision_refinement.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2));print('first component sizes',rr[0]['equality_components']if rr else None)
