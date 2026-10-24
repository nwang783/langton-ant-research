#!/usr/bin/env python3
"""Actual blank input, permanently frozen output-only lifetime boundary circuit.
The full finite field, complete physical w component, and exact future tail remain.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,sys,hashlib
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch,plan,multiplier
from check_rigid_reachability import State
V=[(0,1),(1,0),(0,-1),(-1,0)]
CAPTURE=9977;CLOSE=7689;ROOT_PHASES=[7338,7537,7543,7549,7686,7687]

def graph(T,lives,owners):
 edges=[]
 for r,l in lives:
  assert l<T
  edges.append({'u':r,'v':l,'type':'alpha','owner':r,'consumer':l})
  edges.append({'u':r+1,'v':l+1,'type':'beta','owner':r,'consumer':l})
 for r in owners.values():edges.append({'u':r,'v':r+1,'type':'output','owner':r})
 adj=defaultdict(list)
 for i,e in enumerate(edges):adj[e['u']].append(i);adj[e['v']].append(i)
 assert set(adj)==set(range(T+1))
 assert len(adj[0])==len(adj[T])==1 and all(len(adj[i])==2 for i in range(1,T))
 todo=[1695];seen=set();selected=set()
 while todo:
  u=todo.pop()
  if u in seen:continue
  seen.add(u)
  for i in adj[u]:
   selected.add(i);e=edges[i];todo.append(e['v']if e['u']==u else e['u'])
 assert 0 not in seen and T not in seen and len(seen)==len(selected)==66
 es=[edges[i]for i in sorted(selected)]
 assert sorted(e['owner']for e in es if e['type']=='output')==ROOT_PHASES
 return seen,es

def wedge(p):
 x,y=p
 return((2*x-1,2*y+1),(2*x+1,2*y-1))if(x+y)%2==0 else((2*x-1,2*y-1),(2*x+1,2*y+1))

B={};p=(0,0);h=0;E=[];lives=[];saved={}
for t in range(CAPTURE+104):
 if t in[CLOSE,CAPTURE]:saved[t]=(dict(B),p,h,list(lives))
 c='L'if p in B else'R';row={'time':t,'position':p,'incoming_heading':h,'turn':c}
 if c=='L':
  r=B.pop(p);assert E[r]['turn']=='R'and E[r]['position']==p;row['actual_R_owner']=r;lives.append((r,t))
 else:B[p]=t
 E.append(row);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
BC,pc,hc,LC=saved[CAPTURE];BE,pe,he,LE=saved[CLOSE]
vc,ec=graph(CAPTURE,LC,BC);ve,ee=graph(CLOSE,LE,BE)
assert vc==ve and sorted(ec,key=lambda e:(e['type'],e['u'],e['v']))==sorted(ee,key=lambda e:(e['type'],e['u'],e['v']))
assert max(vc)==7688
roots=[{'phase':r,'cell':E[r]['position']}for r in ROOT_PHASES]
for z in roots:
 assert BC[z['cell']]==BE[z['cell']]==z['phase']
 assert all(tuple(e['position'])!=tuple(z['cell'])for e in E[z['phase']+1:CAPTURE])
W=''.join(e['turn']for e in E[CAPTURE:]);standard=json.loads((R.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert W==standard
state=State(frozenset(BC),pc,hc);assert first_mismatch(state,W)is None
qs,d=plan(state,W);assert pc==(-15,10)and hc==3 and d==(-2,-2)and len(BC)==715
assert max(x for x,y in qs)==-14 and all(z['cell'][0]>=-3 for z in roots)
# Output-only w subgraph is a simple6-cycle. It is NOT the complete component.
sub=defaultdict(list)
for z in roots:
 a,b=wedge(z['cell']);sub[a].append(b);sub[b].append(a)
assert len(sub)==6 and all(len(v)==2 for v in sub.values())
# Full physical component, with every branch and unread cell retained.
adj=defaultdict(list)
for q in BC:
 a,b=wedge(q);adj[a].append((b,q));adj[b].append((a,q))
todo=[next(iter(sub))];vertices=set();cells=set()
while todo:
 u=todo.pop()
 if u in vertices:continue
 vertices.add(u)
 for v,q in adj[u]:cells.add(q);todo.append(v)
assert len(cells)==501 and len(vertices)==446
clearance=[]
for q in sorted(cells):
 ks=[]
 for i,r in enumerate(qs):
  k=multiplier((q[0]-r[0],q[1]-r[1]),d)
  if k is not None:assert k<0;ks.append((i,k))
 clearance.append({'cell':q,'all_tail_footprint_lifts':ks})
selected_lives={e['owner']:(e['owner'],e['consumer'])for e in ec if e['type']!='output'}
assert len(selected_lives)==55 and Counter(e['type']for e in ec)=={'alpha':30,'beta':30,'output':6}
J={'status':'AUTHOR EXACT PERMANENT BLANK COUNTERCONTROL; independent audit pending','scope':'No initial BLACK cells; permanent contractible output-only lifetime circuit in a transient before standard capture. NOT a translating WHITE boundary-winding counterexample.','initial_state':{'black':[],'head':[0,0],'heading':0},'closing_cut':CLOSE,'full_field_at_closing_cut':sorted(BE),'head_at_closing_cut':pe,'heading_at_closing_cut':he,'selected_boundary_vertices':sorted(vc),'selected_boundary_edges':ec,'selected_boundary_root_events':roots,'all55_actual_owned_lifetimes':[{'owner':r,'consumer':l,'cell':E[r]['position'],'age':l-r,'alpha_in_circuit':any(e['type']=='alpha'and e['owner']==r for e in ec),'beta_in_circuit':any(e['type']=='beta'and e['owner']==r for e in ec)}for r,l in sorted(selected_lives.values())],'selected_events':[{**E[i]}for i in sorted(vc)],'complete_root_physical_histories':[{**z,'all_reads':[e for e in E[:CAPTURE]if e['position']==z['cell']]}for z in roots],'capture_cut':CAPTURE,'full_capture_field':sorted(BC),'capture_head':pc,'capture_heading':hc,'full_blank_prefix_word':''.join(e['turn']for e in E[:CAPTURE]),'certified_tail_word':W,'tail_read_positions':qs,'tail_full_drift':d,'exact_all_future_checker_result':None,'six_output_w_cycle_vertices':sorted(sub),'complete_containing_w_component':{'black_edges':sorted(cells),'vertices':sorted(vertices),'edge_count':501,'vertex_count':446,'cycle_rank':56,'all_future_clearance':clearance},'dependencies':{str(R.parent/'computability'/f):hashlib.sha256((R.parent/'computability'/f).read_bytes()).hexdigest()for f in['periodic_tail_checker.py','check_rigid_reachability.py']}}
(R/'blank_permanent_boundary_cycle_certificate.json').write_text(json.dumps(J,indent=2)+'\n')
print('PASS blank permanent66-event/6-root circuit from cut7689; full501-edge archive retained; exact standard tail from9977')
