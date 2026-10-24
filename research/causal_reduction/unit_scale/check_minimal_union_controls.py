"""Literal controls for the exact union of the two retained minimal geometries."""
from pathlib import Path
import json,random,hashlib
import check_flexible_minimal_union as f
P=Path(__file__).parent;names,C,groups,blocks,domains,bad=f.build(False)

def test(selected,initial_flip=0):
 assert all(i+1 not in selected for i in selected)
 vals={v:False for v in names.values()};rr=[];word='';start=-1 if -1 in selected else 0;eps=initial_flip;vals[names[f'h{start}']]=bool(eps)
 for i in range(-1,f.N):
  vals[names[f'pair{i}']]=i in selected
  if i in selected:
   k=5*eps+selected[i];e,d,w=domains[i][k];assert e==eps;vals[names[f'x{i}_{k}']]=True;rr+=blocks[i,k];word+=w;eps=d;vals[names[f'h{i+2}']]=bool(eps)
  elif i>=0 and i-1 not in selected:
   vals[names[f'mono{i}']]=True;vals[names[f'z{i}_{eps}']]=True;rr+=blocks[i,10+eps];word+=blocks[i,10+eps][0][2];eps=0;vals[names[f'h{i+1}']]=False
 p,h,c=f.geom.pose(start);direct,end,head=f.geom.s.old.core.trace(word,p,(h+2*initial_flip)%4);assert direct==rr
 I=set();last={};literal_bad=[]
 for t,(q,h,c)in enumerate(rr):
  if q not in last:
   if c=='L':I.add(q)
  elif last[q][1]==c:literal_bad.append((q,last[q][0],t))
  last[q]=(t,c)
 active_events=[];failed=0
 for a,(q,ev)in enumerate(sorted(groups.items())):
  prev=q in I;vals[names[f'input{a}']]=prev
  for b,(event,xs)in enumerate(sorted(ev.items())):
   active=any(vals[x]for x in xs);vals[names[f'a{a}_{b}']]=active
   if active:active_events.append((event[0],event[1],q,event[2]));failed+=prev!=(event[2]=='L')
   prev=prev!=active;vals[names[f'b{a}_{b}']]=prev
 active_events.sort();assert[(q,c)for i,j,q,c in active_events]==[(q,c)for q,h,c in rr]
 assert sum(not any(vals[abs(x)]==(x>0)for x in row)for row in C)==failed
 assert bool(failed)==bool(literal_bad)
 return dict(tiles=sorted(selected.items()),initial_flip=initial_flip,length=len(rr),input_mass=len(I),literal_legal=not literal_bad,failed_demand_clauses=failed,first_conflict=literal_bad[:1])

pair=f.geom.pose(29)[2]+f.geom.pose(30)[2];kp=next(k for k,w in enumerate(f.s.pal[pair]['0']['flip'])if w==pair+'LRRR')
controls=[test({}),test({104*r+29:kp for r in range(7)}),test({-1:3,f.N-1:4}),test({0:0,3:3,8:1,11:4},1)]
rng=random.Random(103314)
for density in(.03,.15,.4):
 for _ in range(10):
  selected={}
  for i in range(-1,f.N):
   if i-1 not in selected and rng.random()<density:selected[i]=rng.randrange(5)
  controls.append(test(selected,rng.randrange(2)))
assert controls[0]['literal_legal']and controls[0]['input_mass']==97
assert controls[1]['literal_legal']and controls[1]['input_mass']==90
horizon={}
for i in range(104):
 for k in range(10):
  for q,h,c in blocks[i,k]:horizon.setdefault((q[0]-q[1],q[0]%2),set()).add(q[0]//2)
assert max(max(v)-min(v)for v in horizon.values())==4
out=dict(scope=__doc__,controls=controls,phase_extrema=[dict(orbit=a,minimum=min(v),maximum=max(v))for a,v in sorted(horizon.items())],all_pass=True,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'flexible_minimal_union'/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(dict(controls=len(controls),positives=sum(x['literal_legal']for x in controls),max_period_overlap=4))
