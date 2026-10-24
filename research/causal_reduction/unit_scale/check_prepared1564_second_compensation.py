"""Second geometric compensation: shift the newerSE rail and C approach together.
The router2 endpoint is unchanged. This is one supplied90-cell itinerary, not
an inventory over caps. Whole finite fields and exact future tests are retained.
"""
from pathlib import Path
import json,runpy,sys,hashlib
P=Path(__file__).resolve().parent;R=runpy.run_path(str(P/'check_prepared1564_router_geometry.py'));H,V,c=R['H'],R['V'],R['corner'];sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch,plan
z=json.loads((P/'prepared1564_compensated_crossing.json').read_text());seed=set(map(tuple,z['seed']));seed-=set(map(tuple,z['routers'][2]['extra']));seed-=set(map(tuple,z['routers'][1]['extra']));S=R['infer'](H*30)['input']
new2=c(27,'R',103)+H*16+c(14,'R',0);a=R['infer'](H*30+new2+H*30);assert a['bad']is None;extra2={(x-60+750,y-60+815)for x,y in a['input']-S};seed|=extra2;assert len(seed)==67
B=set(seed);p=(-15,10);h=3;t=0;seen=set();history=''
def step():
 global p,h,t,history
 seen.add(p);ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;x,y=V[h];p=p[0]+x,p[1]+y;t+=1;history=(history+ch)[-208:];return ch
end=z['end_time']-84
while t<end:step()
assert(p,h)==(tuple(z['end_pose'][0]),z['end_pose'][1]);assert history[-104:]==z['events'][-1]['word']
w=c(68,'R',0)+H*12+c(88,'R',0);b=R['infer'](H*30+w+H*30);assert b['bad']is None;extra4={(x-60+1000,y-60+951)for x,y in b['input']-S};assert not(extra4&seen)and not(extra4&B);seed|=extra4;B|=extra4
ow=z['events'][-1]['word'];phase=next(i for i in range(104)if H[i:]+H[:i]==ow)
for ch in ow[:104-phase]+H*294+w:assert step()==ch
assert(p,h)==((971,982),3)
events=[dict(stage='second_compensated_C_router_exact',time=t,pose=[p,h],mass=len(B))];print(events[-1],flush=True)
rots={H[i:]+H[:i]for i in range(104)};target=(-205,-194,3);lastcontact=t;pending=H
while True:
 if(*p,h)==target:events.append(dict(stage='C_FIRST_CONTACT',time=t,pose=[p,h]));break
 if pending:
  ss=State(frozenset(B),p,h);nxt=first_mismatch(ss,pending);qs,d=plan(ss,pending);events.append(dict(stage='exact_flight',time=t,pose=[p,h],drift=d,next_mismatch=nxt,word=pending));print({k:v for k,v in events[-1].items()if k!='word'},flush=True)
  if nxt is None:break
  for i in range(nxt):
   assert step()==pending[i%104]
   if(*p,h)==target:break
  if(*p,h)==target:continue
  lastcontact=t;events.append(dict(stage='contact',time=t,pose=[p,h]));step();history='';pending=None
 else:
  if t-lastcontact>=100000:events.append(dict(stage='LOCAL_CONTROL_UNRESOLVED',time=t));break
  if len(history)==208 and history[:104]==history[104:]and history[-104:]in rots:pending=history[-104:];continue
  step()
out=dict(scope=__doc__,initial_mass=len(seed),seed=sorted(seed),router2_word=new2,router2_extra=sorted(extra2),final_router_word=w,final_extra=sorted(extra4),events=events,end_time=t,end_pose=[p,h],black=sorted(B),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(P/'prepared1564_second_compensation.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',len(seed),events[-1])
