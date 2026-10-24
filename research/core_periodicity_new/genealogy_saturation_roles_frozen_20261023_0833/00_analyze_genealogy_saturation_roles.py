"""Finite role/age compatibility analysis. No new counted threshold is used.
A role is an actual source packet, its current residual output, and heading.
Only signed HB/count exclusions are removed; admitted edges remain relaxations.
"""
from pathlib import Path
import json,hashlib,collections,itertools
R=Path(__file__).resolve().parent;D=R/'chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];ids=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(ids)}
A={0:((0,1),3),1:((0,1),3),4:((1,2),3),5:((1,2),3),6:((0,3),5),7:((0,3),5),8:((0,3),5),9:((0,3),5)};phi=(0,5,6,3)
P={tuple(map(int,s.split()[:7]))for s in(D/'protected_patch2.tsv').read_text().splitlines()};CP=D/'critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';C={tuple(map(int,s.split()[:8]))for s in CP.read_text().splitlines()}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
roles=[(a,tuple(s),h)for a in ids for s in G[a]['outputs']for h in range(4)];ix={r:i for i,r in enumerate(roles)}
rawtight=[];tight=[];edges=[];exclusions=collections.Counter();blocked=[]
for ui,(a,s,h)in enumerate(roles):
 for b,(q,age)in A.items():
  for hh in range(4):
   dh=(hh-h)%4;z=rot(q,dh);p=(s[0]-z[0],s[1]-z[1]);t=(a,b,*p,dh,*s);ct=(mp[a],mp[b],*p,dh,*s)
   if(sum(p)-dh)%2:continue
   n=age+(h-hh-age)%4
   reason='HB'if t in P else 'counted'if (*ct,min(5,n))in C else None
   for r0 in G[b]['outputs']:
    r=tuple(r0);vi=ix[b,r,hh];dy=rot((r[0]-q[0],r[1]-q[1]),hh)[1];margin=3*n-4*dy+phi[h]-phi[hh]
    assert margin>=0,(ui,vi,n,dy,margin)
    if not margin:
     rawtight.append((ui,vi,n,dy))
     if reason:blocked.append({'source_role':ui,'target_role':vi,'C_gap':n,'dy':dy,'transfer_original':t,'counted_tuple':(*ct,min(5,n)),'reason':reason})
     else:tight.append((ui,vi,n,dy))
   if reason:
    exclusions[reason]+=1
    if reason=='HB'or n>=5:continue
    n+=4
    if (*ct,5)in C:continue
   for r0 in G[b]['outputs']:
    r=tuple(r0);vi=ix[b,r,hh];dy=rot((r[0]-q[0],r[1]-q[1]),hh)[1];edges.append((ui,vi,n,dy))
def scc(n,es):
 adj=[[]for _ in range(n)];rev=[[]for _ in range(n)]
 for u,v,*_ in es:adj[u].append(v);rev[v].append(u)
 seen=set();order=[]
 def dfs(v):
  seen.add(v)
  for w in adj[v]:
   if w not in seen:dfs(w)
  order.append(v)
 for v in range(n):
  if v not in seen:dfs(v)
 seen=set();out=[]
 for v in reversed(order):
  if v in seen:continue
  st=[v];seen.add(v);block=[]
  while st:
   u=st.pop();block.append(u)
   for w in rev[u]:
    if w not in seen:seen.add(w);st.append(w)
  if len(block)>1 or any(w==v for w in adj[v]):out.append(sorted(block))
 return out,order,adj
before,_,_=scc(len(roles),rawtight);after,order,adj=scc(len(roles),tight);assert not after
# Postorder gives every successor before its source in the acyclic tight graph.
longest=[0]*len(roles)
for u in order:longest[u]=max([0]+[1+longest[v]for v in adj[u]])
Q=D/'genealogy_saturation_roles';Q.mkdir(exist_ok=True)
J={'status':'AUTHOR_COMPLETE_ROLE_GRAPH_PASS_NO_TIGHT_CYCLE','scope':'All auxiliary selected-anchor producer-output roles. Removed transfers are exactly signed HB or cap5 counted exclusions. Allowed edges are not physical realizability assertions. No new threshold or bounded intervening-length claim.','roles':[[a,list(s),h]for a,s,h in roles],'selected_anchors':{a:[list(q),age]for a,(q,age)in A.items()},'potential_plus_y':phi,'raw_tight_edges':rawtight,'raw_tight_cyclic_SCCs':before,'tight_edges_after_signed_exclusions':tight,'tight_cyclic_SCCs_after_signed_exclusions':after,'longest_tight_path':max(longest),'topological_rank':longest,'blocked_tight_edges':blocked,'all_fundamental_edges':edges,'summary':{'roles':len(roles),'raw_tight_edges':len(rawtight),'raw_tight_cyclic_SCCs':len(before),'remaining_tight_edges':len(tight),'blocked_tight_edges':len(blocked),'all_fundamental_edges':len(edges),'max_tight_path':max(longest)},'inputs':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[D/'literal_residual_geometry.json',D/'protected_patch2.tsv',CP,Path(__file__).resolve()]}}
(Q/'graph.json').write_text(json.dumps(J,indent=2)+'\n')
with(Q/'fundamental_graph.dat').open('w')as f:
 f.write(f'{len(roles)} {len(edges)}\n')
 for e in edges:f.write(' '.join(map(str,e))+'\n')
print(J['summary']);print('raw_scc_roles',[[roles[v]for v in comp]for comp in before]);print('blocked transfer classes',len({tuple(e['counted_tuple'])for e in blocked}))
