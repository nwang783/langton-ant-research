"""One derived fresh retry cap after the first forced crossing, not a cap scan.
Two clockwise one-read corners target the still-unreached B endpoint channel.
Every added cell is checked against ALL strict-past reads of the56-cell run.
"""
from pathlib import Path
import json,runpy,sys,hashlib
P=Path(__file__).resolve().parent;R=runpy.run_path(str(P/'check_prepared1564_router_geometry.py'));H,V=(R[x]for x in['H','V'])
sys.path.insert(0,str(P.parents[1]/'computability'));from periodic_tail_checker import State,first_mismatch,plan
z=json.loads((P/'prepared1564_router_crossing.json').read_text());seed=set(map(tuple,z['seed']));w=R['corner'](14,'R',0)+H*8+R['corner'](14,'R',0)
c=R['infer'](H*30+w+H*30);S=R['infer'](H*30)['input'];assert c['bad'] is None
extra={(x-60+500,y-60+537)for x,y in c['input']-S}
B=set(seed);p=(-15,10);h=3;seen=set();at=247226
for t in range(at):
 seen.add(p);ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;u,v=V[h];p=p[0]+u,p[1]+v
assert(p,h)==((500,537),1)
old=extra&seen;unneeded=extra&B;needed=extra-B
result=dict(extra_count=len(extra),extra=sorted(extra),strict_past_overlap=sorted(old),already_black=sorted(unneeded),needed_count=len(needed),start=[p,h],start_time=at,word=w)
# The complete prescribed router plus following clean104 flight must agree.
# If preloading touches the past, no interpretation as an initial cap is made.
if not old:
 seed|=extra;B|=extra;bad=None
 for i,ch in enumerate(w):
  got='L'if p in B else'R'
  if got!=ch:bad=[i,p,h,ch,got];break
  B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;u,v=V[h];p=p[0]+u,p[1]+v
 result['router_bad']=bad;result['end']=[p,h];result['seed_mass']=len(seed)
 if bad is None:
  result['next_H_mismatch']=first_mismatch(State(frozenset(B),p,h),H)
  result['seed']=sorted(seed);result['black']=sorted(B);result['end_time']=at+len(w)
result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();(P/'prepared1564_retry_cap.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k not in['word','seed','black','extra']})
