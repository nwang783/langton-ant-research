"""Finite static genealogy-fork test; never a head-continuous history search.
One U-family producer supplies three goal U inputs; a unary DC child supplies
other two and consumes a different source output. Unspecified support paths
are not bounded or searched; survivors are only necessary relaxation controls.
"""
from pathlib import Path
import json,collections,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)}
CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
P=set(map(tuple,G[7]['inputs']));a=(-1,1);q=(-1,2);b=(-1,4);c=(0,2);d=(0,3)
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def dot(p,q):return p[0]*q[0]+p[1]*q[1]
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and dot(sub(p,a),sub(p,b))<=0
def contact(A,B):
 p,q=A;r,s=B;x1=cross(sub(q,p),sub(r,p));x2=cross(sub(q,p),sub(s,p));y1=cross(sub(s,r),sub(p,r));y2=cross(sub(s,r),sub(q,r))
 return ((x1>0>x2 or x2>0>x1)and(y1>0>y2 or y2>0>y1))or any(on(v,*e)for v,e in[(p,B),(q,B),(r,A),(s,A)])
def outputs(a,p,h):return{add(p,rot(o,h)):tuple(o)for o in G[a]['outputs']}
def ctx(a,p,h):return{add(p,rot(r[:2],h))for r in G[a]['requirements']}
def chords(a,p,h):
 e=G[{0:0,1:0,4:4,5:4,6:4,7:7,8:7,9:7}[a]]['endpoint'];count=G[a]['name'].count('C');A=add((2*p[0],2*p[1]),rot((-1,-1),h));p=add(p,rot(e[:2],h));B=add((2*p[0],2*p[1]),rot((-1,-1),h));ret=[(A,B)]
 for i in range(count):
  A=B;p=add(p,rot((0,1),h));h=(h-1)%4;B=add((2*p[0],2*p[1]),rot((-1,-1),h));ret.append((A,B))
 return ret
T=chords(7,(0,0),0)
def excluded(a,ap,ah,o,b,bp,bh):
 z=rot(sub(bp,ap),-ah);return(mp[a],mp[b],*z,(bh-ah)%4,*o,5)in COUNT
sources=[]
for S in[7,8,9]:
 for h in range(4):
  poses={sub(t,rot(o,h))for t in P for o in G[S]['outputs']}
  for p in sorted(poses):
   if(sum(p)+h)%2:continue
   O=outputs(S,p,h);got=set(O)&P
   if len(got)==3:sources.append((S,p,h,O,got))
rows=[];counts=collections.Counter()
for S,p,h,O,got in sources:
 missing=P-got
 for j in range(4):
  qposes={sub(t,rot(o,j))for t in missing for o in G[1]['outputs']}
  for r in sorted(qposes):
   if(sum(r)+j)%2:continue
   QO=outputs(1,r,j)
   if not missing<=set(QO):continue
   par=add(r,rot((0,1),j))
   if par not in O or par in got:continue
   row=dict(source_packet=S,source_pose=[*p,h],source_goal_inputs=sorted(got),DC_pose=[*r,j],parent_cell=par,DC_goal_inputs=sorted(missing))
   if ctx(1,r,j)&got:reason='DC_context_hits_protected_source_goal_input'
   elif any(contact(x,y)for x in chords(S,p,h)for y in chords(1,r,j)):reason='source_child_center_contact'
   elif any(contact(x,y)for x in chords(S,p,h)for y in T):reason='source_goal_center_contact'
   elif any(contact(x,y)for x in chords(1,r,j)for y in T):reason='child_goal_center_contact'
   elif excluded(S,p,h,O[par],1,r,j):reason='source_to_DC_overflow_count_clause'
   elif any(excluded(S,p,h,O[t],7,(0,0),0)for t in got):reason='source_to_goal_overflow_count_clause'
   elif any(excluded(1,r,j,QO[t],7,(0,0),0)for t in missing):reason='child_to_goal_overflow_count_clause'
   else:reason='static_survivor_not_actual_history'
   row['reason']=reason;counts[reason]+=1;rows.append(row)
result=dict(status='FINITE_STATIC_FORK_QUERY_COMPLETE_NOT_REACHABILITY',scope=__doc__,source_three_target_placements=len(sources),fork_candidates=len(rows),counts=dict(counts),rows=rows,geometry_sha256=hashlib.sha256(GP.read_bytes()).hexdigest(),count5_sha256=hashlib.sha256(CP.read_bytes()).hexdigest())
(W/'chronology_dcuv/U_three_plus_two_DC_fork.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k]for k in['source_three_target_placements','fork_candidates','counts']},indent=2))
