"""The single fresh half of the derived retry router, followed physically.
The second corner's13 bits are NOT installed: they were already-read cells.
This tests an actual standard/standard wake crossing, with full history.
"""
from pathlib import Path
import json,sys,runpy,hashlib
P=Path(__file__).resolve().parent;R=runpy.run_path(str(P/'check_prepared1564_router_geometry.py'));H,V=(R[x]for x in['H','V']);sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch,plan
z=json.loads((P/'prepared1564_router_crossing.json').read_text());seed=set(map(tuple,z['seed']));w=R['corner'](14,'R',0);c=R['infer'](H*30+w+H*30);S=R['infer'](H*30)['input'];assert c['bad'] is None
extra={(x-60+500,y-60+537)for x,y in c['input']-S};assert len(extra)==13
B=set(seed);p=(-15,10);h=3;seen=set();at=247226
for t in range(at):
 seen.add(p);ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;u,v=V[h];p=p[0]+u,p[1]+v
assert(p,h)==((500,537),1);assert not(extra&seen);assert not(extra&B);B|=extra;seed|=extra
for ch in w:
 assert('L'if p in B else'R')==ch;B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;u,v=V[h];p=p[0]+u,p[1]+v
nxt=first_mismatch(State(frozenset(B),p,h),H);assert nxt is not None
cut=at+len(w)+nxt;start=at+len(w);hist='';word=[];rots={H[i:]+H[:i]for i in range(104)}
for t in range(start,cut+100000):
 if t>=cut+208 and t%104==0 and hist[:104]==hist[104:] and hist[-104:]in rots:
  ow=hist[-104:];s=State(frozenset(B),p,h);nx=first_mismatch(s,ow);qs,d=plan(s,ow)
  if nx is None or nx>1040:
   result=dict(status='CERTIFIED_CAPTURE'if nx is None else'EXACT_INTERMEDIATE_FLIGHT',time=t,pose=[p,h],period_word=ow,drift=d,next_mismatch=nx,black=sorted(B),word_from_contact=''.join(word),contact_time=cut)
   break
 ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;u,v=V[h];p=p[0]+u,p[1]+v;hist=(hist+ch)[-208:]
 if t>=cut:word.append(ch)
else:result=dict(status='NO QUALIFYING TAIL IN DECLARED LOCAL CONTROL',time=t+1,pose=[p,h])
result.update(initial_seed=sorted(seed),initial_mass=len(seed),fresh_extra=sorted(extra),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(P/'prepared1564_fresh_crossing.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k not in['period_word','black','word_from_contact','initial_seed','fresh_extra']})
