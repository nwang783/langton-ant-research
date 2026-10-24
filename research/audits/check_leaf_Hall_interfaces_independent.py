from pathlib import Path
from collections import defaultdict,Counter,deque
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'LEAF_HALL_INTERFACES_MANIFEST.json';assert sha(mf)=='6cbceb9fe823fc3004f1d5c61641136d17f44e09aba4d4d4ac49cb99f35cf32c';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
J=json.loads((D/'LEAF_HALL_INTERFACES_CHECKED.json').read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);sim,xy=ns['sim'],ns['xy'];key=lambda p:(p.real,p.imag);traces={}
for row in J['source_histories']:
 cuts={0,1579,5710,6042}if row['name']=='empty'else{40071,109168};seed={complex(*p)for p in row['seed']};z=sim(seed,row['physical_reads']+1,h=1,cuts=cuts);assert z['word'][:row['physical_reads']]==row['full_word'];traces[row['name']]=z
assert sum(row['physical_reads']for row in J['source_histories'])==115210
intervals={}
for row in J['intervals']:
 s,t=row['start'],row['end'];z=traces['empty'if t<=6042 else'MT_100'];B0,p0,h0=z['snap'][s];B1,root,h1=z['snap'][t];vis=defaultdict(list);last={}
 for k in range(s,t):q=z['pts'][k];vis[q].append((k,z['word'][k]));last[q]=k
 assert root not in last;parent={q:z['pts'][k+1]for q,k in last.items()};children=defaultdict(list)
 for q,p in parent.items():children[p].append(q)
 leaves={q for q in last if not children[q]};C=set(B0)&set(last);O=set(B1)&set(last);ports={('C',q)for q in C}|{('O',q)for q in O};f={q:z['pts'][k-1]for q,k in last.items()if k>s and last[z['pts'][k-1]]>k};assert len(set(f.values()))==len(f)
 for q in last:assert len(children[q])+int(q in f)<=2
 assert all(q in f or last[q]==s for q in leaves)
 assert row['root']==xy(root)and row['initial_pose']==[xy(p0),h0]and row['final_heading']==h1
 assert row['initial_full_field']==[[xy(q),i]for q,i in sorted(B0.items(),key=lambda x:key(x[0]))]and row['final_full_field']==[[xy(q),i]for q,i in sorted(B1.items(),key=lambda x:key(x[0]))]
 assert row['complete_interval_word']==z['word'][s:t]and row['complete_interval_tree']==[[xy(q),xy(p)]for q,p in sorted(parent.items(),key=lambda x:key(x[0]))]
 assert row['read_vertices']==len(last)and row['leaves']==sorted(map(xy,leaves))
 assert row['inputs']==[[xy(q),B0[q],z['dead'][B0[q]]]for q in sorted(C,key=key)]and row['outputs']==[[xy(q),B1[q]]for q in sorted(O,key=key)]
 intervals[s,t]=dict(s=s,t=t,z=z,B0=B0,B1=B1,root=root,vis=vis,last=last,parent=parent,children=children,leaves=leaves,C=C,O=O,ports=ports,f=f)
A=intervals[0,1579];B=intervals[5710,6042];MT=intervals[40071,109168]
def nodecheck(I,row):
 q=complex(*row['cell']);k=I['last'][q];assert row['reads']==[list(x)for x in I['vis'][q]]and row['last']==k and row['parent']==xy(I['parent'][q]);assert {tuple(x)for x in row['children']}=={tuple(xy(p))for p in I['children'][q]};assert row['leaf']==(q in I['leaves']);assert row['input_owner']==I['B0'].get(q)and row['output_owner']==I['B1'].get(q);assert row['f']==(xy(I['f'][q])if q in I['f']else None);assert row['last_arrival_predecessor']==(xy(I['z']['pts'][k-1])if k>I['s']else None)
def boundarycheck(I,Q,rows):
 z=I['z'];ans=[]
 for k in range(I['s'],I['t']):
  q,p=z['pts'][k:k+2]
  if(q in Q)!=(p in Q):ans.append(dict(time=k,cell=xy(q),next=xy(p),letter=z['word'][k],entry=p in Q))
 assert ans==rows
 return len(ans)
def portset(x):return{(typ,complex(*q))for typ,q in x}
def pathcheck(I,path):
 ps=list(map(lambda q:complex(*q),path))
 for a,b in zip(ps,ps[1:]):assert I['f'].get(a)==b or I['parent'].get(b)==a
 return ps
# Entire finite matching, preserving two separate lifetime ports at one site.
repair=J['blank_double_port_repair'];assert repair['old_input']==[[0,7],2997,5809]and repair['new_output']==[[0,7],5881]
for row in repair['nodes']:nodecheck(B,row)
for row in repair['assignments']:
 path=pathcheck(B,row['path']);assert path[0]==complex(*row['leaf'])and path[-1]==complex(*row['port'][1]);assert (row['port'][0],path[-1]) in B['ports'] and path[0] in B['leaves']
rc=boundarycheck(B,{complex(*r['cell'])for r in repair['nodes']},repair['boundary_crossings'])
assert B['f'][8j]==-1+8j and B['parent'][7j]==-1+7j and B['parent'][-1+7j]==-1+8j
# Exact ancestor-only Hall neighbors, independent of any matching algorithm.
hall=J['ancestor_only_Hall_failure'];neighbors=set()
for row in hall['paths']:
 q=complex(*row['leaf']);assert q in A['leaves'];path=[];pp=[]
 while q!=A['root']:
  path.append(xy(q));pp.extend((typ,q)for typ in['C','O']if q in A[typ]);q=A['parent'][q]
 assert path==row['ancestor_path']and set(pp)==portset(row['eligible_ports']);neighbors.update(pp)
assert neighbors=={('O',10+1j)}and len(hall['leaves'])==3
for row in hall['nodes']:nodecheck(A,row)
assert A['B1'][10+1j]==1577 and len(A['leaves'])==81 and len(A['O'])==163 and len(A['last'])==322 and A['root']==11+2j
# MT first-mark chains: four leaves, exactly one eligible output.
fh=J['first_mark_Hall_failure'];union=set()
for row in fh['chains']:
 q=complex(*row['leaf']);assert q in MT['leaves'];path=[]
 while True:
  path.append(xy(q))
  if q in MT['C']or q in MT['O']or q not in MT['f']:break
  q=MT['f'][q]
 pp={(typ,q)for typ in['C','O']if q in MT[typ]};assert path==row['path']and pp==portset(row['eligible_ports']);union|=pp
assert union=={('O',197+232j)}and MT['B1'][197+232j]==71039
for row in fh['nodes']:nodecheck(MT,row)
fc=boundarycheck(MT,{complex(*q)for q in fh['leaves']},fh['boundary_crossings'])
assert [MT['last'][q]for q in[197+231j,198+231j,198+232j,197+232j]]==[71006,71021,71036,71039]
# The genuine zero-port descendant subtree is complete, not a chosen crop.
st=J['zero_port_descendant_subtree'];qs={complex(*row['cell'])for row in st['nodes']};root=complex(*st['root']);assert qs=={234+169j,234+168j,234+170j}and set(MT['children'][root])==qs-{root};assert all(not MT['children'][q]for q in qs-{root})and all(q not in MT['C']|MT['O']for q in qs)
for row in st['nodes']:nodecheck(MT,row)
sc=boundarycheck(MT,qs,st['boundary_crossings'])
# Reconstruct the COMPLETE lifetime/axis matching graph from actual birth IDs.
components=[];z=A['z'];s,t=A['s'],A['t'];pm={};endpoints={}
for k in range(s,t):
 if z['word'][k]=='L':
  born=z['events'][k]
  if born>=s:assert z['pts'][born]==z['pts'][k]and z['word'][born]=='R';pm[k]=born;pm[born]=k
  else:endpoints[k]=('C',z['pts'][k])
for k in range(s,t):
 if z['word'][k]=='R'and k not in pm:endpoints[k]=('O',z['pts'][k])
assert set(endpoints.values())==A['ports'];tm={}
for k in range(s,t-1,2):tm[k]=k+1;tm[k+1]=k
partial=set(range(s,t))-set(tm);seen=set()
for k in range(s,t):
 if k in seen:continue
 todo=[k];seen.add(k);cc=[]
 while todo:
  u=todo.pop();cc.append(u)
  for g in[pm,tm]:
   if u in g and g[u]not in seen:seen.add(g[u]);todo.append(g[u])
 cc.sort();ep=[q for q in cc if q in endpoints];pe=[q for q in cc if q in partial];assert len(ep)+len(pe)in[0,2];components.append((cc,ep,pe))
paths=sum(bool(ep or pe)for cc,ep,pe in components);cycles=len(components)-paths;assert J['lifetime_axis_decomposition']==dict(paths=paths,cycles=cycles,endpoint_count=len(endpoints)+len(partial));assert len(endpoints)+len(partial)==2*paths
cy=J['lifetime_axis_cycle'];cc=next(c for c,e,p in components if c==[1420,1421,1448,1449]);assert all(k not in endpoints and k not in partial for k in cc)and pm[1420]==1448 and pm[1421]==1449 and tm[1420]==1421 and tm[1448]==1449;assert A['last'][10-13j]==1449 and 10-13j in A['leaves'];assert all(z['pts'][k]not in{10-12j,10-13j}for k in range(1422,1448))
for row in[cy['leaf_node'],cy['other_node']]:nodecheck(A,row)
ccross=boundarycheck(A,{10-12j,10-13j},cy['boundary_crossings'])
# Explicit certificates establish all27 matching and exactly80/81 expanded.
matching=[]
for row in J['finite_expanded_matchings']:
 I=intervals[tuple(row['interval'])];usedP=set();usedL=set();reach={}
 for leaf in I['leaves']:
  todo=[leaf];reached={leaf}
  while todo:
   q=todo.pop();nxt=I['children'][q]+([I['f'][q]]if q in I['f']else[])
   for v in nxt:
    if v not in reached:reached.add(v);todo.append(v)
  reach[leaf]=reached
 for a in row['assignments']:
  leaf=complex(*a['leaf']);port=(a['port'][0],complex(*a['port'][1]));assert leaf in I['leaves']and port in I['ports']and leaf not in usedL and port not in usedP;usedL.add(leaf);usedP.add(port);pp=pathcheck(I,a['path']);assert pp[0]==leaf and pp[-1]==port[1]and port[1]in reach[leaf]
  labels=['last-arrival predecessor f'if I['f'].get(u)==v else'tree child'for u,v in zip(pp,pp[1:])];assert labels==a['edge_kinds']
 assert len(usedL)==row['count']and len(I['leaves'])==row['total_leaves']and not row['free_root_used']
 hf=row['Hall_failure'];ll={complex(*q)for q in hf['leaves']};rr=set().union(*(reach[q]for q in ll))if ll else set();pp={p for p in I['ports']if p[1]in rr};assert pp==portset(hf['ports'])and len(ll)-len(pp)==hf['deficiency']
 if I is B:
  assert len(usedL)==27 and usedL==I['leaves']and len(I['C'])==47 and len(I['O'])==67
  assign={complex(*a['leaf']):(a['port'][0],complex(*a['port'][1]))for a in row['assignments']};assert assign[8j]==('O',7j)and assign[7j]==('C',7j)
 else:
  assert len(usedL)==80 and ll=={3-8j,4-9j}and pp=={('O',4-8j)};assert rr=={complex(x,y)for x in range(2,6)for y in[-9,-8]};assert 0j not in rr
 matching.append(dict(interval=row['interval'],matched=len(usedL),leaves=len(I['leaves']),Hall_leaves=sorted(map(xy,ll)),Hall_ports=[(typ,xy(q))for typ,q in sorted(pp,key=lambda v:(v[0],key(v[1])))],full_reachable_Hall_vertices=sorted(map(xy,rr))))
O=dict(status='PASS exact finite chronological leaf-port matching and Hall obstructions; gross numerical bound remains OPEN',manifest=sha(mf),script=sha(S),full_replayed_reads=115210,interval_counts=[dict(interval=[s,t],vertices=len(I['last']),leaves=len(I['leaves']),C=len(I['C']),O=len(I['O']))for(s,t),I in intervals.items()],all_expanded_matching_checks=matching,lifetime_axis=dict(paths=paths,cycles=cycles,endpoints=len(endpoints)+len(partial),unpaid_cycle=cc),proper_patch_crossing_counts=dict(repaired_patch=rc,MT_square=fc,MT_subtree=sc,unpaid_axis_component=ccross),analytic_review=[
'All literalEMPTY andMT100 originalseeds are replayed fromtime0 for115210 certifiedprefixupdates, with whole endpointfields, everyintervalread, birth/deathIDs andlast-exittrees compared. Freshfinalroots are checked. C andO are distinctcapacity-one lifetimes evenwhenoccupyingoneBLACK-to-BLACK cell; no croppedpatch ororiginal-seed-only charge is substituted.',
'The blank5710..6042 repair uses C(0,7)=R2997/death5809 and O(0,7)=R5881 for two distinctleaves. All27 explicitassignments have actualf/treechild paths and27 distinctports; bothlocalassignments are preserved, not stolen fromthe rest. All properpatch crossings andexternalreads remain.',
'At EMPTY0..1579, three specifiedunmarkedleaves have exactlyone ancestorpath port O(10,1)=R1577. Their completepaths/visits reconstruct, so evenonefreeglobalroot leavesdeficit1. This disprovesancestor-only charging, not81<=163+1.',
'MT100first-markf chaining sendsfouractualleaves tooneoutputR71039 at197,232, withlasttimes71006/71021/71036/71039. ItsHall deficit is3withoutroot,2withroot. Theactualzeroportthree-vertexdescendantsubtree at234,169 has2leaves; noone-free-rootpersubtree rulecanignoreitsboundarychronology.',
'The entire1579-event trueR-nextL andone-axisadjacency matchings formdegree<=2 paths/cycles, withallC/O andpartialendpointsretained. Exactcomponent1420/1421/1448/1449 isclosed, hasnoport/partialendpoint, andcontainsa last-exitleaf. Its26 interveningreadsareoutside, so thisisnotanactualtimecycle,boundedantorbit orstandaloneclosedpatch.',
'The enlargedf+reversedtree-edge graph hasan explicit80-real-portmatching at1579 andexactHall2-to1 catchment{2,3,4,5}x{-9,-8}, disjointfrominitialhead. Thefullreachablevertexset ischecked. Onefreeglobalcapacity canrepair thisonefinitecase; no universal+1 Hall theorem is inferred.',
'All statements arefinite exactcontrols or elementarymatching identities. Earlierboundedno-counterdiagnostics remainUNKNOWN andarenotpremises. Thegrosswhole-intervalleaf<=C+O+1 inequality, recurringdroughtresourcebound, universalcapture andcanonicalclassification remainOPEN.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(O['interval_counts'],O['lifetime_axis']);print(sha(S.with_suffix('.json')))
