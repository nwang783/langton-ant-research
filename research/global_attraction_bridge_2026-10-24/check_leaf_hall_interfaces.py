"""Finite, fully chronological leaf-port matchings and Hall obstructions.
No universal gross leaf bound is assumed or concluded.
"""
from pathlib import Path
from collections import defaultdict, Counter, deque
import json, hashlib
P=Path(__file__).parent
SOURCE=json.loads((P/'WHOLE_LAST_EXIT_RENEWAL_CHECKED.json').read_text())
D=((0,1),(1,0),(0,-1),(-1,0))

def replay(name, stops):
 source=next(c for c in SOURCE['cases'] if c['name']==name)
 seed=list(map(tuple,source['seed']))
 B={q:-i-1 for i,q in enumerate(seed)}; p=(0,0); h=1
 events=[]; cuts={}; death={}
 for k in range(max(stops)+1):
  if k in stops: cuts[k]=(dict(B),p,h)
  if k==max(stops): break
  q=p; old=B.pop(q,None); letter='R' if old is None else 'L'
  if old is None: B[q]=k
  else: death[old]=k
  h=(h+(1 if letter=='R' else -1))%4
  p=(q[0]+D[h][0],q[1]+D[h][1])
  events.append(dict(time=k,cell=q,letter=letter,consumed=old,next=p,heading=h))
 assert ''.join(e['letter'] for e in events)==source['full_turn_word'][:len(events)]
 return dict(name=name,seed=seed,events=events,cuts=cuts,death=death)

def interval(R,s,t):
 B0,p0,h0=R['cuts'][s]; B1,root,h1=R['cuts'][t]
 events=R['events']; visits=defaultdict(list); last={}
 for k in range(s,t):
  q=events[k]['cell']; visits[q].append((k,events[k]['letter'])); last[q]=k
 assert root not in last
 parent={q:events[k]['next'] for q,k in last.items()}
 children=defaultdict(list)
 for q,r in parent.items(): children[r].append(q)
 leaves={q for q in last if not children[q]}
 C=set(B0)&last.keys(); O=set(B1)&last.keys()
 ports=[('C',q) for q in sorted(C)]+[('O',q) for q in sorted(O)]
 f={}
 for q,k in last.items():
  if k>s:
   u=events[k-1]['cell']
   if last[u]>k: f[q]=u
 assert len(set(f.values()))==len(f)
 assert all(v in f or last[v]==s for v in leaves)
 for q in last: assert len(children[q])+(q in f)<=2
 return locals()

def snapshot(I):
 return dict(start=I['s'],end=I['t'],root=I['root'],initial_pose=[I['p0'],I['h0']],final_heading=I['h1'],
  initial_full_field=sorted(I['B0'].items()),final_full_field=sorted(I['B1'].items()),
  complete_interval_word=''.join(e['letter'] for e in I['events'][I['s']:I['t']]),
  complete_interval_tree=sorted(I['parent'].items()),read_vertices=len(I['last']),leaves=sorted(I['leaves']),
  inputs=[[q,I['B0'][q],I['R']['death'][I['B0'][q]]] for q in sorted(I['C'])],
  outputs=[[q,I['B1'][q]] for q in sorted(I['O'])])

def node(I,q):
 k=I['last'][q]
 return dict(cell=q,reads=I['visits'][q],last=k,parent=I['parent'][q],children=I['children'][q],
  leaf=q in I['leaves'],input_owner=I['B0'].get(q),output_owner=I['B1'].get(q),
  f=I['f'].get(q),last_arrival_predecessor=I['events'][k-1]['cell'] if k>I['s'] else None)

def boundary(I,Q):
 """Every exterior-to-patch entry and patch-to-exterior exit, not just selected reads."""
 out=[]
 for e in I['events'][I['s']:I['t']]:
  a=e['cell'] in Q; b=e['next'] in Q
  if a!=b: out.append(dict(time=e['time'],cell=e['cell'],next=e['next'],letter=e['letter'],entry=b))
 return out

def ancestor_hall(I,L):
 paths=[]; union=set()
 for v in L:
  q=v; path=[]; eligible=[]
  while q!=I['root']:
   path.append(q)
   for typ,S in [('C',I['C']),('O',I['O'])]:
    if q in S: eligible.append((typ,q))
   q=I['parent'][q]
  union.update(eligible)
  paths.append(dict(leaf=v,ancestor_path=path,eligible_ports=eligible))
 assert len(L)>len(union)+1
 return dict(leaves=L,ports=sorted(union),deficiency_without_root=len(L)-len(union),
  deficiency_with_one_free_root=len(L)-len(union)-1,paths=paths,
  nodes=[node(I,q) for q in sorted(set(q for x in paths for q in x['ancestor_path']))])

def expanded_matching(I):
 """Finite certificate only: f steps plus reversed last-exit edges, all capacities distinct."""
 adj={q:sorted(I['children'][q])+([I['f'][q]] if q in I['f'] else []) for q in I['last']}
 ports=I['ports']; bynode=defaultdict(list)
 for j,port in enumerate(ports): bynode[port[1]].append(j)
 ll=sorted(I['leaves']); reaches=[]; predecessors=[]
 for v in ll:
  prev={v:None}; Q=deque([v]); rr=[]
  while Q:
   q=Q.popleft(); rr.extend(bynode[q])
   for z in adj[q]:
    if z not in prev: prev[z]=q; Q.append(z)
  reaches.append(sorted(rr)); predecessors.append(prev)
 fixed={}
 if (I['s'],I['t'])==(5710,6042):
  fixed={ports.index(('O',(0,7))):ll.index((0,8)),ports.index(('C',(0,7))):ll.index((0,7))}
 match=dict(fixed)
 def augment(i,seen):
  for j in reaches[i]:
   if j in seen or j in fixed: continue
   seen.add(j)
   if j not in match or augment(match[j],seen): match[j]=i; return True
  return False
 unmatched=[i for i in range(len(ll)) if i not in fixed.values() and not augment(i,set())]
 if unmatched: print('EXPANDED UNMATCHED',I['s'],I['t'],[ll[i] for i in unmatched])
 out=[]
 for j,i in sorted(match.items(),key=lambda z:z[1]):
  target=ports[j][1]; path=[]; q=target; prev=predecessors[i]
  while q is not None: path.append(q); q=prev[q]
  path.reverse(); labels=[]
  for a,b in zip(path,path[1:]):
   if I['f'].get(a)==b: labels.append('last-arrival predecessor f')
   else: assert I['parent'][b]==a; labels.append('tree child')
  out.append(dict(leaf=ll[i],port=ports[j],path=path,edge_kinds=labels))
 assert len({tuple((z['port'][0],tuple(z['port'][1]))) for z in out})==len(out)
 U=set(unmatched); V=set(); Q=deque(unmatched)
 while Q:
  i=Q.popleft()
  for j in reaches[i]:
   if j in V: continue
   V.add(j)
   if j in match and match[j] not in U: U.add(match[j]); Q.append(match[j])
 if U:
  print('EXPANDED HALL',len(U),len(V),[ll[i] for i in sorted(U)], [ports[j] for j in sorted(V)])
 return dict(count=len(out),total_leaves=len(ll),reserved_double_ports=sorted(fixed.items()),free_root_used=False,assignments=out,Hall_failure=dict(leaves=[ll[i] for i in sorted(U)],ports=[ports[j] for j in sorted(V)],deficiency=len(U)-len(V)))

def first_mark_chain(I,v):
 q=v; path=[]
 while True:
  path.append(q)
  if q in I['C'] or q in I['O'] or q not in I['f']: break
  q=I['f'][q]
 ports=[(typ,q) for typ,S in [('C',I['C']),('O',I['O'])] if q in S]
 return path,ports

def lifetime_axis_components(I,parity):
 """Pair consecutive R,L at each site; pair adjacent event times in one parity."""
 pm={}; openR={}; endpoints={}
 for k in range(I['s'],I['t']):
  e=I['events'][k]; q=e['cell']
  if e['letter']=='R': openR[q]=k
  elif q in openR:
   b=openR.pop(q); pm[b]=k; pm[k]=b
  else: endpoints[k]=('C',q)
 for q,k in openR.items(): endpoints[k]=('O',q)
 assert len(endpoints)==len(I['ports'])
 tm={}
 for k in range(I['s']+parity,I['t']-1,2): tm[k]=k+1; tm[k+1]=k
 edge_endpoints={k for k in range(I['s'],I['t']) if k not in tm}
 seen=set(); components=[]
 for k in range(I['s'],I['t']):
  if k in seen: continue
  Q=[k]; seen.add(k); component=[]
  while Q:
   j=Q.pop(); component.append(j)
   for l in [pm.get(j),tm.get(j)]:
    if l is not None and l not in seen: seen.add(l); Q.append(l)
  component.sort()
  marked=[j for j in component if j in endpoints]; partial=[j for j in component if j in edge_endpoints]
  incoming_leaves=[j for j in component if I['last'][I['events'][j]['cell']]==j and I['events'][j]['cell'] in I['leaves'] and tm.get(j)==j-1]
  assert len(marked)+len(partial) in (0,2)
  components.append(dict(times=component,ports=[(j,endpoints[j]) for j in marked],partial_endpoints=partial,incoming_leaf_last_reads=incoming_leaves))
 return dict(pm=pm,tm=tm,components=components,paths=sum(bool(c['ports'] or c['partial_endpoints']) for c in components),cycles=sum(not(c['ports'] or c['partial_endpoints']) for c in components),endpoint_count=len(endpoints)+len(edge_endpoints))

blank=replay('empty',{0,1579,5710,6042}); mt=replay('MT_100',{40071,109168})
A=interval(blank,0,1579); B=interval(blank,5710,6042); M=interval(mt,40071,109168)
assert len(A['leaves'])==81 and len(A['O'])==163 and not A['C']
H=ancestor_hall(A,[(8,-2),(9,-1),(9,1)])
assert H['ports']==[('O',(10,1))]

# Exact double-port local repair, with whole paths and old/new lifetime IDs.
v=(0,8); u=(-1,8); w=(0,7)
assert B['f'][v]==u and B['parent'][w]==(-1,7) and B['parent'][(-1,7)]==u
assert v in B['leaves'] and w in B['leaves'] and w in B['C'] and w in B['O']
repair=dict(nodes=[node(B,q) for q in [v,u,(-1,7),w]],
 assignments=[dict(leaf=v,port=('O',w),path=[v,u,(-1,7),w]),dict(leaf=w,port=('C',w),path=[w])],
 old_input=[w,B['B0'][w],blank['death'][B['B0'][w]]],new_output=[w,B['B1'][w]],
 boundary_crossings=boundary(B,{v,u,(-1,7),w}))
assert repair['old_input'][1]!=repair['new_output'][1]

# A complete first-mark Hall failure: four leaves, one output, no input.
L=[(197,231),(197,232),(198,231),(198,232)]; chains=[]; union=set()
for v in L:
 assert v in M['leaves']; path,pp=first_mark_chain(M,v); union.update(pp); chains.append(dict(leaf=v,path=path,eligible_ports=pp))
assert union=={('O',(197,232))}
FH=dict(leaves=L,chains=chains,ports=sorted(union),deficiency_without_root=3,deficiency_with_one_free_root=2,
 nodes=[node(M,q) for q in sorted(set(q for c in chains for q in c['path']))],boundary_crossings=boundary(M,set(L)))

# Descendant subtree with two leaves but neither endpoint color port.
star=[(234,169),(234,168),(234,170)]
assert set(M['children'][star[0]])==set(star[1:]) and all(not M['children'][q] for q in star[1:])
assert all(q not in M['C'] and q not in M['O'] for q in star)
ST=dict(root=star[0],nodes=[node(M,q) for q in star],leaves=2,ports=0,boundary_crossings=boundary(M,set(star)))

# Smallest concrete unpaid same-axis/lifetime cycle, complete chronology preserved.
AC=lifetime_axis_components(A,0)
cy=next(c for c in AC['components'] if c['times']==[1420,1421,1448,1449])
assert not cy['ports'] and not cy['partial_endpoints'] and cy['incoming_leaf_last_reads']==[1449]
cycle=dict(**cy,events=[A['events'][k] for k in cy['times']],
 lifetime_pairs=[(1420,1448),(1421,1449)],axis_pairs=[(1420,1421),(1448,1449)],
 leaf_node=node(A,(10,-13)),other_node=node(A,(10,-12)),boundary_crossings=boundary(A,{(10,-12),(10,-13)}))
assert AC['endpoint_count']==2*AC['paths']

fs=['WHOLE_LAST_EXIT_RENEWAL_MANIFEST.json','WHOLE_LAST_EXIT_ENDPOINT_ADDENDUM.json','../audits/check_whole_last_exit_renewal_independent.json','LEAF_PREDECESSOR_OBSTRUCTION_MANIFEST.json','../audits/check_leaf_predecessor_obstruction_independent.json']
for f in fs: assert (P/f).exists(),f
out=dict(status='AUTHOR exact finite matching and Hall interfaces; independent audit pending',
 source_histories=[dict(name=R['name'],seed=R['seed'],physical_reads=len(R['events']),full_word=''.join(e['letter'] for e in R['events'])) for R in [blank,mt]],
 intervals=[snapshot(I) for I in [A,B,M]],
 blank_double_port_repair=repair,ancestor_only_Hall_failure=H,first_mark_Hall_failure=FH,
 zero_port_descendant_subtree=ST,lifetime_axis_cycle=cycle,
 lifetime_axis_decomposition=dict(paths=AC['paths'],cycles=AC['cycles'],endpoint_count=AC['endpoint_count']),
 finite_expanded_matchings=[dict(interval=[I['s'],I['t']],**expanded_matching(I)) for I in [A,B]],
 dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in fs},
 scope='Exact finite no-reuse certificates and failures of specified local matching rules, not a counterexample or proof of the gross whole-interval leaf bound. All fields and all boundary crossings retained.')
(P/'LEAF_HALL_INTERFACES_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS author finite checks',len(blank['events'])+len(mt['events']), 'reads;',[(len(I['leaves']),len(I['C']),len(I['O'])) for I in [A,B,M]])
print('Hall defects',H['deficiency_with_one_free_root'],FH['deficiency_with_one_free_root'],'expanded matches',[x['count'] for x in out['finite_expanded_matchings']])
