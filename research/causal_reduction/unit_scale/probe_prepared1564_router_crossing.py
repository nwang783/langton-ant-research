"""Actual first forced crossing in the supplied1564 routing itinerary.
Retains the full56-cell seed and complete evolving field. A detected104 flight
is subjected to exact future arithmetic; a finite next-contact is not capture.
"""
from pathlib import Path
import json,sys,runpy,hashlib
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch,plan
R=runpy.run_path(str(P/'check_prepared1564_router_geometry.py'));H,V=(R[x]for x in['H','V'])
caps=json.loads((P/'prepared1564_router_geometry.json').read_text())
n=100;T1,T2=200,400
S=R['infer'](H,(-15,10),3)['input'];seed=S|{(-17-2*(11+n),2-2*(11+n))}
for c,org in zip(caps[:2],[(2*T1,2*T1-49),(2*T2-50,2*T2+15)]):
 seed|={(x+org[0],y+org[1])for x,y in c['extra_relative_router']}
assert len(seed)==56
B=set(seed);p=(-15,10);h=3;recent='';cut=205680;letters=[]
for t in range(cut+100000):
 if t>=cut+208 and t%104==0 and recent[:104]==recent[104:] and recent[104:]in {H[i:]+H[:i]for i in range(104)}:
  w=recent[-104:];s=State(frozenset(B),p,h);nxt=first_mismatch(s,w);qs,d=plan(s,w)
  if nxt is None or nxt>1040:
   result=dict(status='CERTIFIED_CAPTURE'if nxt is None else'EXACT_INTERMEDIATE_FLIGHT',time=t,pose=[p,h],period_word=w,drift=d,next_mismatch=nxt,initial_mass=len(seed),seed=sorted(seed),black=sorted(B),word_from_first_conflict=''.join(letters),first_conflict_time=cut)
   break
 c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;u,v=V[h];p=(p[0]+u,p[1]+v);recent=(recent+c)[-208:]
 if t>=cut:letters.append(c)
else:result=dict(status='NO QUALIFYING TAIL WITHIN DECLARED LOCAL CONTROL',time=t+1,pose=[p,h],initial_mass=len(seed))
result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(P/'prepared1564_router_crossing.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items()if k not in['seed','black','period_word','word_from_first_conflict']})
