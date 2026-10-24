from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'BLANK_PERMANENT_OUTPUT_CIRCUIT_COUNTERCONTROL.md';F=D/'blank_permanent_boundary_cycle_certificate.json';assert sha(P).startswith('c9ae6a4c')and sha(F).startswith('3bb74c05')and sha(D/'certify_blank_permanent_boundary_cycle.py').startswith('3369386d');J=json.loads(F.read_text())
for f,h in J['dependencies'].items():assert sha(Path(f))==h
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);sim,cert,geometry,xy=[ns[k]for k in('sim','cert','geometry','xy')];z=cert(sim(set(),9977,0j,0,cuts={7689,9977}),J['certified_tail_word']);assert z['word']==J['full_blank_prefix_word']and (z['p'],z['h'],z['d'])==(-15+10j,3,-2-2j)and len(z['B'])==715 and sorted(map(xy,z['B']))==J['full_capture_field'];q,_,_,_=geometry(z['p'],z['h'],z['tail']);assert sorted(map(xy,q))==sorted(J['tail_read_positions'])and max(p.real for p in q)==-14
# Build the ENTIRE finite alpha/beta/root graph independently before selection.
selected=[]
for cut in (7689,9977):
 B,p,h=(z['B'],z['p'],z['h'])if cut==9977 else z['snap'][cut];assert (sorted(map(xy,B)),xy(p),h)==((J['full_field_at_closing_cut'],J['head_at_closing_cut'],J['heading_at_closing_cut'])if cut==7689 else(J['full_capture_field'],J['capture_head'],J['capture_heading']))
 edges=[];adj=defaultdict(list)
 for r,l in z['dead'].items():
  if l>=cut:continue
  assert r>=0 and z['word'][r]=='R'and z['word'][l]=='L'and z['pts'][r]==z['pts'][l]
  edges.extend([dict(u=r,v=l,type='alpha',owner=r,consumer=l),dict(u=r+1,v=l+1,type='beta',owner=r,consumer=l)])
 for r in B.values():edges.append(dict(u=r,v=r+1,type='output',owner=r))
 for i,e in enumerate(edges):adj[e['u']].append(i);adj[e['v']].append(i)
 assert set(adj)==set(range(cut+1))and len(adj[0])==len(adj[cut])==1 and all(len(adj[i])==2 for i in range(1,cut))
 todo=[1695];vs=set();es=set()
 while todo:
  u=todo.pop()
  if u in vs:continue
  vs.add(u)
  for i in adj[u]:es.add(i);e=edges[i];todo.append(e['v']if e['u']==u else e['u'])
 ee=[edges[i]for i in es];assert len(vs)==len(ee)==66 and 0 not in vs and cut not in vs and sorted(vs)==J['selected_boundary_vertices'];assert sorted(ee,key=str)==sorted(J['selected_boundary_edges'],key=str);selected.append((vs,sorted(ee,key=str)))
assert selected[0]==selected[1];es=selected[0][1];assert Counter(e['type']for e in es)==dict(alpha=30,beta=30,output=6)
roots={e['owner']for e in es if e['type']=='output'};assert roots=={7338,7537,7543,7549,7686,7687}
for r in J['all55_actual_owned_lifetimes']:
 b,l=r['owner'],r['consumer'];assert z['dead'][b]==l and xy(z['pts'][b])==r['cell']and l-b==r['age'];assert r['alpha_in_circuit']==any(e['type']=='alpha'and e['owner']==b for e in es)and r['beta_in_circuit']==any(e['type']=='beta'and e['owner']==b for e in es)
assert len(J['all55_actual_owned_lifetimes'])==55 and sum(r['alpha_in_circuit']and r['beta_in_circuit']for r in J['all55_actual_owned_lifetimes'])==5
for row in J['complete_root_physical_histories']:
 b=row['phase'];p=complex(*row['cell']);assert b in roots and z['B'][p]==b and b not in z['dead']and p.real>=-3;actual=[(i,z['heads'][i],z['word'][i])for i,x in enumerate(z['pts'])if x==p];assert actual==[(r['time'],r['incoming_heading'],r['turn'])for r in row['all_reads']]
def ends(p):
 x,y=int(p.real),int(p.imag)
 return ((2*x-1,2*y+1),(2*x+1,2*y-1))if(x+y)%2==0 else((2*x-1,2*y-1),(2*x+1,2*y+1))
adj=defaultdict(list);sub=defaultdict(list)
for p in z['B']:
 a,b=ends(p);adj[a].append((b,p));adj[b].append((a,p))
for r in roots:
 a,b=ends(z['pts'][r]);sub[a].append(b);sub[b].append(a)
assert len(sub)==6 and all(len(v)==2 for v in sub.values());todo=[next(iter(sub))];verts=set();cells=set()
while todo:
 u=todo.pop()
 if u in verts:continue
 verts.add(u)
 for v,p in adj[u]:cells.add(p);todo.append(v)
c=J['complete_containing_w_component'];assert len(cells)==501 and len(verts)==446 and sorted(map(xy,cells))==c['black_edges']and sorted(map(list,verts))==c['vertices']and len(cells)-len(verts)+1==56
for row in c['all_future_clearance']:
 p=complex(*row['cell']);assert p in cells;hits=[]
 for i,a in enumerate(q):
  v=(p-a)/z['d']
  if v.imag==0 and v.real.is_integer():assert v.real<0;hits.append([i,int(v.real)])
 assert hits==row['all_tail_footprint_lifts']
O={'status':'PASS actual blank-origin permanent66-event/6-output circuit and complete501-edge frozen w component','proof':sha(P),'certificate':sha(F),'script':sha(S),'capture_mass':715,'capture_cut':9977,'infinite_tail_tests':z['tests'],'circuit_counts':dict(Counter(e['type']for e in es)),'whole_w_edges':501,'whole_w_vertices':446,'analytic_review':['Independent literal blank simulation builds every R->nextL lifetime and the entire finite graph at7689 and9977. The selected closed66-event component, including all60 alpha/beta copies and6 actual output steps, is identical at both cuts. Fifty-five physical finite lifetimes are retained, five with both copies and fifty with their other copy elsewhere. No input roots exist.','The complete715-cell9977 state has independently certified canonical104 future and exact drift(-2,-2). Every infinite phase ray lies x<=-14; six marked lastR cells lie x>=-3 and are unvisited since their births. Hence they are permanent, not merely current at a long observation cutoff. Their unchanged output edges prevent the boundary circuit from later rejoining the head component.','All six w edges form a simple6-cycle, but they are not an isolated physical component. Full-field incidence BFS finds501 edges/446 vertices/cycle rank56; all501 exact future ray systems miss. No branches or older black strands are cropped.','This genuinely refutes finite-prefix no-input output-forest and head-connectedness shortcuts. It is a contractible transient in an orbit that then captures standard104, NOT a periodic WHITE S1 counterexample, alternative controller, or proof about unrestricted winding.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
