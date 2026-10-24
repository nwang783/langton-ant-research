"""Actual D board with an explicitly artificial residual-component coloring.
This is a local predicate noninductivity control, not reachable component labels.
"""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;geo=W/'chronology_dcuv/literal_residual_geometry.json'
J=json.loads(geo.read_text());G=J['geometry'];K={tuple(p)for p in J['core']}
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def edge(p):
 x,y=p
 return ((2*x-1,2*y-1),(2*x+1,2*y+1)) if(x+y)%2==0 else ((2*x-1,2*y+1),(2*x+1,2*y-1))
def components(cells):
 adj={}
 for c in cells:
  a,b=edge(c);adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
 parts=[]
 while adj:
  seed=next(iter(adj));todo=[seed];seen={seed}
  while todo:
   for v in adj[todo.pop()]:
    if v not in seen:seen.add(v);todo.append(v)
  parts.append(sorted(seen))
  for v in seen:del adj[v]
 return sorted(parts)
C={(-2,0),(0,-2)};I={(0,1)};seed=K|I|C
assert len(seed)==8 and not C&{tuple(r[:2])for r in G[0]['requirements']}
B=set(seed);p=(0,0);h=0;raw_exit=None;reads=[]
for t,want in enumerate(G[0]['word']+G[0]['marker']):
 actual='L' if p in B else 'R';assert actual==want,(t,p,want,actual)
 reads.append([t,*p,h,actual]);B.symmetric_difference_update({p});h=(h+(-1 if actual=='L'else 1))%4;p=add(p,rot((0,1),h))
 if t+1==len(G[0]['word']):raw_exit=(set(B),p,h)
B,p,h=raw_exit;assert(p,h)==((1,1),0)
K2={add(p,rot(c,h))for c in K};O={tuple(o)for o in G[0]['outputs']}
assert B==K2|O|C and not C&K2
old_parts=components(K|C);new_parts=components(K2|C)
assert len(old_parts)==1 and len(new_parts)==3 and len(components(C))==2
old_vertices={v for c in K for v in edge(c)};new_vertices={v for c in K2 for v in edge(c)}
rows=[]
for c in sorted(C):
 e=set(edge(c));assert e&old_vertices and not e&new_vertices
 rows.append(dict(cell=c,dual_edge=sorted(e),old_core_attachment=sorted(e&old_vertices),new_core_attachment=[]))
result=dict(status='EXACT_RELAXATION_LIMITATION_CONTROL',scope='The board and D raw-plus-marker are actual. ONLY the equal component label assigned to the two untouched remote residual cells is artificial; historical reachability of that coloring is not asserted. Therefore this refutes local induction from the core-graft predicate alone, not an actual-prefix component theorem.',initial_black=sorted(seed),packet=0,raw_length=len(G[0]['word']),marker=G[0]['marker'],raw_exit_head=[*p,h],raw_exit_black=sorted(B),artificial_component=sorted(C),core_before=sorted(K),core_after=sorted(K2),colored_edge_attachments=rows,before_core_plus_color_components=old_parts,after_core_plus_color_components=new_parts,full_direct_read_trace=reads,geometry_sha256=hashlib.sha256(geo.read_bytes()).hexdigest())
(W/'chronology_dcuv/D_core_graft_noninductivity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k]for k in['scope','initial_black','raw_exit_head','colored_edge_attachments']},indent=2))
