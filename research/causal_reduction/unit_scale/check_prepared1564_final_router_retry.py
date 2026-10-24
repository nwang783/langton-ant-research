"""A single fresh C-target retry from the actual compensated65-cell capture.
Unused oldthird cap is removed. Every historical field is otherwise retained.
Exact future-word checks distinguish intermediate flights from true capture.
"""
from pathlib import Path
import json,runpy,sys,hashlib
P=Path(__file__).resolve().parent;R=runpy.run_path(str(P/'check_prepared1564_router_geometry.py'));H,V=R['H'],R['V'];sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch,plan
z=json.loads((P/'prepared1564_compensated_crossing.json').read_text());B=set(map(tuple,z['black']));seed=set(map(tuple,z['seed']));unused=set(map(tuple,z['routers'][2]['extra']));assert unused<=B and unused<=seed;B-=unused;seed-=unused;assert len(seed)==65
w=R['corner'](68,'R',0)+H*12+R['corner'](68,'R',102);loc=R['infer'](H*30+w+H*30);assert loc['bad'] is None;S=R['infer'](H*30)['input'];extra={(x-60+1000,y-60+951)for x,y in loc['input']-S};assert len(extra)==23 and not(extra&B)
# Exact strict-past guard, replaying the suppliedoriginalseed once.
old=set(map(tuple,z['seed']));q=(-15,10);g=3;seen=set()
for _ in range(z['end_time']):
 seen.add(q);ch='L'if q in old else'R';old.symmetric_difference_update({q});g=(g+(1 if ch=='R'else-1))%4;a,b=V[g];q=q[0]+a,q[1]+b
assert(q,g)==(tuple(z['end_pose'][0]),z['end_pose'][1]);assert old==set(map(tuple,z['black']));assert not(extra&seen) and not(unused&seen)
B|=extra;seed|=extra;p=q;h=g;t=z['end_time'];history='';events=[]
def step():
 global p,h,t,history
 c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;a,b=V[h];p=p[0]+a,p[1]+b;t+=1;history=(history+c)[-208:];return c
ow=z['events'][-1]['word'];phase=next(i for i in range(104)if H[i:]+H[:i]==ow)
for c in ow[:104-phase]+H*294+w:assert step()==c
assert(p,h)==((970,983),3);events.append(dict(stage='fresh_C_router_exact',time=t,pose=[p,h],mass=len(B)));print(events[-1],flush=True)
rots={H[i:]+H[:i]for i in range(104)};target=(-205,-194,3);lastcontact=t;pending=H
while True:
 if (*p,h)==target:
  events.append(dict(stage='C_FIRST_CONTACT',time=t,pose=[p,h]));break
 if pending:
  nxt=first_mismatch(State(frozenset(B),p,h),pending);qs,d=plan(State(frozenset(B),p,h),pending);events.append(dict(stage='exact_flight',time=t,pose=[p,h],drift=d,next_mismatch=nxt,word=pending));print({k:v for k,v in events[-1].items()if k!='word'},flush=True)
  if nxt is None:break
  for i in range(nxt):
   assert step()==pending[i%104]
   if (*p,h)==target:break
  if (*p,h)==target:continue
  lastcontact=t;events.append(dict(stage='contact',time=t,pose=[p,h]));step();history='';pending=None
 else:
  if t-lastcontact>=100000:events.append(dict(stage='LOCAL_CONTROL_UNRESOLVED',time=t));break
  if len(history)==208 and history[:104]==history[104:]and history[-104:]in rots:pending=history[-104:];continue
  step()
out=dict(scope=__doc__,initial_mass=len(seed),seed=sorted(seed),fresh_extra=sorted(extra),strict_past_overlap=[],events=events,end_time=t,end_pose=[p,h],black=sorted(B),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(P/'prepared1564_final_router_retry.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',events[-1])
