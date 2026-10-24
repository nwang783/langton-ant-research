"""Whole-circuit/literal controls for variable-tiling heading flips and unit-square recuts."""
from pathlib import Path
import json,random,hashlib
import check_flexible_heading_backward as f
import check_unit_square_flexible_classification as u
P=Path(__file__).parent

def circuit(names,C,groups,vals,literal):
 last={};I=set();direct_bad=[]
 for t,(q,h,c)in enumerate(literal):
  if q not in last:
   if c=='L':I.add(q)
  elif last[q][1]==c:direct_bad.append((q,last[q][0],t))
  last[q]=(t,c)
 failed=0;active_events=[]
 for a,(q,ev)in enumerate(sorted(groups.items())):
  prev=q in I;vals[names[f'input{a}']]=prev
  for b,(event,xs)in enumerate(sorted(ev.items())):
   active=any(vals[x]for x in xs);vals[names[f'a{a}_{b}']]=active
   if active:
    active_events.append((event[0],event[1],q,event[2]));failed+=prev!=(event[2]=='L')
   prev=prev!=active;vals[names[f'b{a}_{b}']]=prev
 active_events.sort();assert[(q,c)for i,j,q,c in active_events]==[(q,c)for q,h,c in literal]
 assert sum(not any(vals[abs(x)]==(x>0)for x in row)for row in C)==failed
 assert bool(failed)==bool(direct_bad)
 return dict(length=len(literal),input_mass=len(I),literal_legal=not direct_bad,failed_demand_clauses=failed,first_conflict=direct_bad[:1])

names,C,groups,blocks,domains,bad=f.build(False)
def heading_test(selected,initial_flip=0):
 assert all(i+1 not in selected for i in selected)
 vals={v:False for v in names.values()};literal=[];word='';start=-1 if -1 in selected else 0;eps=initial_flip
 vals[names[f'h{start}']]=bool(eps)
 for i in range(-1,f.N):
  vals[names[f'pair{i}']]=i in selected
  if i in selected:
   k=3*eps+selected[i];vals[names[f'x{i}_{k}']]=True;literal+=blocks[i,k];word+=domains[i][k][2];eps=1;vals[names[f'h{i+2}']]=True
  elif i>=0 and i-1 not in selected:
   vals[names[f'mono{i}']]=True;vals[names[f'z{i}_{eps}']]=True;literal+=blocks[i,6+eps];word+=blocks[i,6+eps][0][2];eps=0;vals[names[f'h{i+1}']]=False
 p,h,c=f.geom.pose(start);direct,end,head=f.geom.s.old.core.trace(word,p,(h+2*initial_flip)%4);assert direct==literal
 return dict(tiling=sorted(selected.items()),initial_flip=initial_flip,**circuit(names,C,groups,vals,literal))

pair=f.geom.pose(29)[2]+f.geom.pose(30)[2]
kp=next(k for k,w in enumerate(f.s.pal[pair]['0']['flip'])if w==pair+'LRRR')
heading_controls=[heading_test({}),heading_test({-1:0}),heading_test({f.N-1:2}),heading_test({-1:2,f.N-1:1}),heading_test({104*r+29:kp for r in range(7)})]
rng=random.Random(20261023)
for density in(.03,.15,.4):
 for _ in range(8):
  selected={}
  for i in range(-1,f.N):
   if i-1 not in selected and rng.random()<density:selected[i]=rng.randrange(3)
  heading_controls.append(heading_test(selected,rng.randrange(2)))
assert heading_controls[0]['input_mass']==97 and heading_controls[0]['literal_legal']
assert heading_controls[4]['input_mass']==90 and heading_controls[4]['literal_legal']

un,uc,ug,ub=u.build(False)
def square_test(selected):
 vals={};literal=[]
 for i in range(u.N):
  for k in(0,1):vals[un[f'x{i}_{k}']]=(i in selected)==bool(k)
  literal+=ub[i,int(i in selected)]
 return dict(square_indices=sorted(selected),**circuit(un,uc,ug,vals,literal))
square_controls=[square_test(set()),square_test({104*r+31 for r in range(7)})]
for mask in range(128):
 selected={104*r+31 for r in range(7)if mask>>r&1};z=square_test(selected);assert z['literal_legal'] and z['input_mass']==97-len(selected);square_controls.append(z)
for _ in range(20):square_controls.append(square_test({i for i in range(u.N)if rng.random()<.1}))
# Actual complete phase footprints, including across-period flips.
horizon={}
for i in range(104):
 for k in range(6):
  for q,h,c in blocks[i,k]:horizon.setdefault((q[0]-q[1],q[0]%2),set()).add(q[0]//2)
assert max(max(v)-min(v)for v in horizon.values())==3
out=dict(scope=__doc__,heading_controls=heading_controls,square_controls=square_controls,heading_phase_extrema=[dict(orbit=a,minimum=min(v),maximum=max(v))for a,v in sorted(horizon.items())],all_pass=True,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'flexible_heading_backward'/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(dict(heading_controls=len(heading_controls),heading_positives=sum(x['literal_legal']for x in heading_controls),square_controls=len(square_controls),square_positives=sum(x['literal_legal']for x in square_controls),max_period_overlap=3))
