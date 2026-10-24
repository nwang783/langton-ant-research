"""Exact masks forbid the direct unary-child 3+2 U ancestry fork on simple centers.
No word search, count-kernel generation, age cap, or producer-depth expansion.
"""
from pathlib import Path
from itertools import combinations
import json,hashlib,collections
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];IDS=[0,1,4,5,6,7,8,9];P=set(map(tuple,G[7]['inputs']))
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def outputs(a,p,h):return{add(p,rot(o,h))for o in G[a]['outputs']}
def context(a,p,h):return{add(p,rot(r[:2],h))for r in G[a]['requirements']}
def prefix_pose(a,p,h,length):
 for ch in G[a]['word'][:length]:
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,rot((0,1),h))
 return(*p,h)
def center(pose):return add((2*pose[0],2*pose[1]),rot((-1,-1),pose[2]))
placements=[];rows=[]
for S in IDS:
 for h in range(4):
  poses={sub(t,rot(o,h))for t in P for o in G[S]['outputs']}
  for p in sorted(poses):
   if(sum(p)+h)%2:continue
   O=outputs(S,p,h);hit=O&P
   for tri in combinations(sorted(hit),3):
    got=set(tri);missing=P-got;placements.append(dict(source=S,pose=[*p,h],protected_triple=sorted(got)))
    for j in range(4):
     qposes={sub(t,rot(o,j))for t in missing for o in G[1]['outputs']}
     for r in sorted(qposes):
      if(sum(r)+j)%2 or not missing<=outputs(1,r,j):continue
      parent=add(r,rot((0,1),j))
      if parent not in O or parent in got:continue
      ctxhit=sorted(context(1,r,j)&got)
      row=dict(source=S,source_pose=[*p,h],protected_triple=sorted(got),DC_pose=[*r,j],DC_parent_cell=parent,DC_goal_pair=sorted(missing))
      if ctxhit:row.update(reason='DC_complete_context_hits_protected_source_identity',protected_context_hits=ctxhit)
      else:
       assert S in[6,9]
       # The first C exit is an actual internal atomic cut. DC's full exit
       # is a later actual cut at exactly the same corrected center vertex.
       first_C=len(G[4 if S==6 else 7]['word'])+15
       u=prefix_pose(S,p,h,first_C);v=prefix_pose(1,r,j,len(G[1]['word']))
       assert center(u)==center(v)==(-5,3)
       row.update(reason='two_nonadjacent_atomic_vertices_coincide',source_prefix_length=first_C,source_atomic_cut_pose=u,DC_exit_pose=v,doubled_common_center=center(u))
      rows.append(row)
counts=dict(collections.Counter(r['reason']for r in rows));assert len(placements)==132 and len(rows)==16
assert counts==dict(DC_complete_context_hits_protected_source_identity=14,two_nonadjacent_atomic_vertices_coincide=2)
assert {(r['source'],tuple(r['source_pose']),tuple(r['DC_pose']))for r in rows if r['reason']=='two_nonadjacent_atomic_vertices_coincide'}=={(6,(-6,3,1),(-4,0,0)),(9,(-7,2,1),(-4,0,0))}
# No max-three law is needed for enumeration: source may also create other
# target positions, whose identities are not among the protected triple.
D=[GP]
R=dict(status='AUTHOR_DIRECT_UNARY_FORK_EXCLUSION_PENDING_INDEPENDENT_AUDIT',scope='An actual complete recurrent-eight factor with simple corrected atomic center cannot contain an earlier full producer P supplying three current goal-U inputs and a later DC Q supplying the other two, where Q consumes one different output identity of P. Arbitrary support between P,Q,goal is allowed. D has only one output, so DC is the only unary child able to supply two. Distinct producers in one historical component, longer unary chains, and V/U children are not classified.',source_triple_count=len(placements),fork_count=len(rows),counts=counts,all_source_triple_placements=placements,all_forks=rows,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_direct_three_two_fork.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(dict(source_triples=len(placements),forks=len(rows),counts=counts),indent=2))
