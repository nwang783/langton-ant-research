"""One geometrically compensated crossing itinerary for the supplied1564 wave.
The changed pre-cross channel and old perpendicular rail are translated by
one common crossing class. No phase/cap search. Complete finite field retained.
"""
from pathlib import Path
import runpy,json,sys,hashlib
P=Path(__file__).resolve().parent;G=P.parents[1]/'nonlinear_global_budget_2026-10-23';R=runpy.run_path(str(P/'check_prepared1564_router_geometry.py'));H,V=R['H'],R['V'];c=R['corner']
sys.path.insert(0,str(P.parents[1]/'computability'));from periodic_tail_checker import State,first_mismatch,plan
I=runpy.run_path(str(P/'check_prepared1564_connected_itinerary.py'))
routers=[c(88,'R',0)+H*17+c(56,'L',0),c(24,'L',30)+H*16+c(27,'R',103),c(68,'R',0)+H*5+c(68,'R',102)]
origins=[(400,351),(750,815),(1204,1183)];n=100;S=R['infer'](H,(-15,10),3)['input'];seed=S|{(-239,-220)};local=[]
for w,org in zip(routers,origins):
 z=R['infer'](H*30+w+H*30);assert z['bad'] is None
 extra=z['input']-R['infer'](H*30)['input'];extra={(x-60+org[0],y-60+org[1])for x,y in extra};seed|=extra;local.append(dict(word=w,extra=sorted(extra),extra_count=len(extra),origin=org,endpoint=list(R['trace'](w))[-1][1:3]))
B=set(seed);p=(-15,10);h=3;time=0;events=[];targets={(400,351,1):'router1',(750,815,1):'router2',(-203,-209,2):'B_first_contact',(-188,-209,1):'B_phase0',(1204,1183,1):'router3'}
seen_targets=set();recent='';Rots={H[i:]+H[:i]for i in range(104)};afterB=False;cap3=False;Bcheck=None;history=[]
def step():
 global p,h,time,recent
 ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;u,v=V[h];p=p[0]+u,p[1]+v;time+=1;recent=(recent+ch)[-208:];return ch
while time<700000:
 key=(*p,h)
 if key in targets and key not in seen_targets:
  seen_targets.add(key);label=targets[key];events.append(dict(stage=label,time=time,pose=[p,h],mass=len(B)));print('EVENT',events[-1],flush=True)
  if label=='B_first_contact':
   Bcheck=[]
   for i,ch in enumerate(I['wb']):
    got=step()
    if got!=ch:Bcheck=[i,ch,got];break
   if Bcheck:events.append(dict(stage='B_response_MISMATCH',detail=Bcheck,time=time,pose=[p,h]));break
   afterB=True;events.append(dict(stage='B_response_exact',time=time,pose=[p,h],mass=len(B)))
  if label=='router3':
   cap3=True
   for i,ch in enumerate(routers[2]):
    got=step()
    if got!=ch:events.append(dict(stage='router3_MISMATCH',index=i,want=ch,got=got,time=time,pose=[p,h]));break
   else:events.append(dict(stage='router3_exact',time=time,pose=[p,h]));continue
   break
 if cap3 and time%104==0 and recent[:104]==recent[104:]and recent[-104:]in Rots:
  word=recent[-104:];ss=State(frozenset(B),p,h);nxt=first_mismatch(ss,word);qs,d=plan(ss,word)
  events.append(dict(stage='post_router3_exact_flight',time=time,pose=[p,h],drift=d,next_mismatch=nxt,word=word));break
 if afterB and not cap3 and time%104==0 and recent[:104]==recent[104:]and recent[-104:]in Rots:
  # Only halt early if the actualB response fails to return to its plannedstation.
  word=recent[-104:];ss=State(frozenset(B),p,h);nxt=first_mismatch(ss,word)
  if nxt is None:events.append(dict(stage='premature_exact_capture',time=time,pose=[p,h],word=word));break
 step()
out=dict(scope=__doc__,n=n,station_parameters=[200,400,600],initial_mass=len(seed),seed=sorted(seed),routers=local,events=events,end_time=time,end_pose=[p,h],black=sorted(B),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'prepared1564_compensated_crossing.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',len(seed),time,events[-1])
