"""Annotate signed LA roles with necessary sibling identity retirements.
This is a literal intersection quotient, never a realizability assertion.
"""
from pathlib import Path
from collections import Counter,deque
import hashlib,json
W=Path(__file__).resolve().parent
GP=W/'genealogy_saturation_roles_frozen_20261023_0833/01_graph.json'
LP=W/'chronology_dcuv/literal_residual_geometry.json'
J=json.loads(GP.read_text());L=json.loads(LP.read_text());G=L['geometry']
K={tuple(p)for p in L['core']};roles=J['roles'];A=J['selected_anchors']
positive={1,5,6,8,9}
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def scc(es):
 N=len(roles);adj=[[]for _ in roles];rev=[[]for _ in roles]
 for u,v,*_ in es:adj[u].append(v);rev[v].append(u)
 seen=set();order=[]
 def dfs(u):
  seen.add(u)
  for v in adj[u]:
   if v not in seen:dfs(v)
  order.append(u)
 for u in range(N):
  if u not in seen:dfs(u)
 seen=set();out=[]
 for u in reversed(order):
  if u in seen:continue
  seen.add(u);st=[u];c=[]
  while st:
   v=st.pop();c.append(v)
   for z in rev[v]:
    if z not in seen:seen.add(z);st.append(z)
  if len(c)>1 or u in adj[u]:out.append(sorted(c))
 return sorted(out)
transfers={};records=[];strictfree=[];allfree=[]
for ei,(u,v,n,dy)in enumerate(J['all_fundamental_edges']):
 a,s,h=roles[u];b,r,hh=roles[v];key=(u,b,hh)
 if key not in transfers:
  q,_=A[str(b)];dh=(hh-h)%4;z=rot(q,dh)
  pose=(s[0]-z[0],s[1]-z[1],dh)
  req={(x,y):black for x,y,black,*_ in G[b]['requirements']}
  assert set(p for p,black in req.items()if black)==K|{tuple(p)for p in G[b]['inputs']}
  core=[];white=[];inputs=[];untouched=[]
  for t in G[a]['outputs']:
   if t==s:continue
   z=rot((t[0]-pose[0],t[1]-pose[1]),-dh)
   row=[t,list(z)]
   if z in K:core.append(row)
   elif z in req and not req[z]:white.append(row)
   elif list(z)in G[b]['inputs']:inputs.append(row)
   else:untouched.append(row)
  transfers[key]=len(records)
  records.append(dict(source_role=u,target_packet=b,target_heading=hh,source_normalized_target_pose=pose,core=core,white=white,other_inputs=inputs,untouched=untouched))
 t=records[transfers[key]]
 if not t['core']and not t['white']:
  strictfree.append((u,v,n,dy,ei))
  if not t['other_inputs']:allfree.append((u,v,n,dy,ei))
posstrict=[e for e in strictfree if roles[e[0]][0]in positive and roles[e[1]][0]in positive]
posall=[e for e in allfree if roles[e[0]][0]in positive and roles[e[1]][0]in positive]
assert len(allfree)==728 and len(strictfree)==1892 and len(posall)==48 and len(posstrict)==540
pscc=scc(posall);assert len(pscc)==1 and len(pscc[0])==4
assert {tuple([roles[u][0],*roles[u][1],roles[u][2]])for u in pscc[0]}=={(1,2,0,h)for h in range(4)}
cyclicedges=[e for e in posall if e[0]in pscc[0]and e[1]in pscc[0]]
assert len(cyclicedges)==4 and all(e[2]==7 for e in cyclicedges)
for u,v,*_ in cyclicedges:assert(roles[v][2]-roles[u][2])%4==1
O=dict(status='AUTHOR_LITERAL_INTERSECTION_PASS_NOT_GLOBAL_FUEL',scope='Necessary retirement of OTHER outputs of an actual source packet before or by the selected-input consumer. Larger allowed ages share the same intersections. No physical realization, retirement freshness, disjoint charge, or finite budget is asserted.',inputs={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,LP,Path(__file__).resolve()]},roles=roles,transfers=records,edge_transfer_index=[transfers[(u,roles[v][0],roles[v][2])]for u,v,*_ in J['all_fundamental_edges']],strict_clearance_free_edges=strictfree,by_target_clearance_free_edges=allfree,positive_C_strict_free_edges=posstrict,positive_C_by_target_free_edges=posall,positive_C_by_target_free_cyclic_SCCs=pscc,positive_C_by_target_free_cyclic_edges=cyclicedges,summary=dict(roles=len(roles),fundamental_edges=len(J['all_fundamental_edges']),transfer_classes=len(records),strict_clearance_free_edges=len(strictfree),by_target_clearance_free_edges=len(allfree),positive_C_strict_free_edges=len(posstrict),positive_C_by_target_free_edges=len(posall),positive_C_by_target_free_cyclic_SCC_sizes=[len(c)for c in pscc],all_by_target_free_cyclic_SCC_sizes=[len(c)for c in scc(allfree)]))
P=W/'chronology_dcuv/genealogy_sibling_clearance.json';P.write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(O['summary'],indent=2));print(P)
