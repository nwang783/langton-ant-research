"""Literal/physical-event and Boolean-circuit controls for changing pair alignments."""
from pathlib import Path
import json,random,hashlib,collections
import check_pair_bypass_flexible_tiling as s
P=Path(__file__).parent;names,C,g,blocks=s.build(False)

def run(chosen):
 assert all(i+1 not in chosen for i in chosen)
 vals={};literal=[];word='';start=-1 if -1 in chosen else 0
 for i in range(-1,s.N):
  for k in range(2):vals[names[f'x{i}_{k}']]=chosen.get(i)==k
  vals[names[f'pair{i}']]=i in chosen
  if i>=0:vals[names[f'mono{i}']]=i not in chosen and i-1 not in chosen
  if i in chosen:literal+=blocks[i,chosen[i]];word+=s.s.PAL[s.pose(i)[2]+s.pose(i+1)[2]][chosen[i]+1]
  elif i>=0 and vals[names[f'mono{i}']]:literal+=blocks[i,-1];word+=s.pose(i)[2]
 p,h,c=s.pose(start);direct,end,head=s.s.old.core.trace(word,p,h);assert direct==literal
 last={};I=set();direct_bad=[]
 for t,(q,h,c)in enumerate(literal):
  if q not in last:
   if c=='L':I.add(q)
  elif last[q][1]==c:direct_bad.append((q,last[q][0],t))
  last[q]=(t,c)
 circuit_errors=[];active_list=[]
 for a,(q,ev)in enumerate(sorted(g.items())):
  prev=q in I;vals[names[f'input{a}']]=prev
  for b,(event,xs)in enumerate(sorted(ev.items())):
   act=any(vals[x]for x in xs);vals[names[f'a{a}_{b}']]=act
   if act:
    active_list.append((event[0],event[1],q,event[2]))
    if prev!=(event[2]=='L'):circuit_errors.append((q,event))
   prev=prev!=act;vals[names[f'b{a}_{b}']]=prev
 active_list.sort();assert[(q,c)for i,j,q,c in active_list]==[(q,c)for q,h,c in literal]
 failed=sum(not any(vals[abs(x)]==(x>0)for x in row)for row in C)
 assert failed==len(circuit_errors)
 assert bool(circuit_errors)==bool(direct_bad)
 return dict(bypasses=sorted(chosen.items()),length=len(word),input_mass=len(I),literal_legal=not direct_bad,failed_demand_clauses=failed,first_conflict=direct_bad[:1])

controls=[run({}),run({-1:0}),run({s.N-1:1}),run({-1:1,s.N-1:0}),run({0:0,3:1,8:0,11:1})]
rng=random.Random(10231421)
for density in(.02,.1,.4):
 for _ in range(10):
  chosen={}
  for i in range(-1,s.N):
   if i-1 not in chosen and rng.random()<density:chosen[i]=rng.randrange(2)
  controls.append(run(chosen))
assert controls[0]['literal_legal'] and controls[0]['input_mass']==97
out=dict(scope=__doc__,controls=controls,all_pass=True,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'pair_bypass_flexible_tiling'/'controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(dict(controls=len(controls),literal_legal=sum(x['literal_legal']for x in controls),identity=controls[0]))
