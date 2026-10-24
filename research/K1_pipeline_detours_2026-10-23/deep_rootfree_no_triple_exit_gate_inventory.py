"""Filter signed110 one-face inventories by complete WHITE-even/no-G3 collar.
Classify actual within-face R0-exit paths. Fixed local gate inventory only.
"""
from pathlib import Path
import json,hashlib
r=Path(__file__).parent;src=r/'canonical_max_face_child_ports.json';base=json.loads(src.read_text())['rows'];H='NESW'
def out(h):return[H[(H.index(x)+(1 if i%2==0 else-1))%4]for i,x in enumerate(h)]
rows=[];exits=[]
for z in base:
 hs=z['headings']
 if any(len(h)%2 for h in hs.values()):continue
 if any(3 in[h.count(c)for c in H]+[out(h).count(c)for c in H]for h in hs.values()):continue
 assert hs['A']=='NNSS'
 rows.append(z)
 edges={}
 for v,d,w,i in [('A','W','Z','W'),('Z','N','Y','N'),('Y','E','B','E'),('B','S','A','S')]:
  s=[(v,j)for j,x in enumerate(out(hs[v]))if x==d];t=[(w,j)for j,x in enumerate(hs[w])if x==i]
  assert len(s)==len(t);edges.update(zip(s,t))
 for child in z['potential_children']:
  p=(child,0);path=[p]
  for _ in range(20):
   if p==('A',2)or p not in edges:break
   p=edges[p];path.append(p)
  assert len(path)<20
  exits.append(dict(headings=hs,exit=child,forced_adjacent=p==('A',2),actual_boundary_prefix=path,terminal=p,has_flow4=any(4 in[h.count(c)for c in H]+[out(h).count(c)for c in H]for h in hs.values())))
assert len(rows)==17 and sum(bool(z['potential_children'])for z in rows)==12 and len(exits)==16
forced=[z for z in exits if z['forced_adjacent']];opened=[z for z in exits if not z['forced_adjacent']]
assert len(forced)==12 and len(opened)==4
assert sum(x['has_flow4']for x in exits)==1
assert all(x['forced_adjacent']for x in exits if x['has_flow4'])
obj=dict(scope=__doc__,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),profile_count=len(rows),profiles_with_possible_cycle_exit=12,exit_count=len(exits),forced_count=len(forced),open_count=len(opened),rows=rows,exits=exits,open_exits=opened,warning='Necessary local profiles; unforced exits may still return adjacently. No gate-span bound, temporal phase cut, external realization or front exclusion is inferred.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:obj[k]for k in ['profile_count','profiles_with_possible_cycle_exit','exit_count','forced_count','open_count']},indent=2));print(json.dumps(opened,indent=2))
