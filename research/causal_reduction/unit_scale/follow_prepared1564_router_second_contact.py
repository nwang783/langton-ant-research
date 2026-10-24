"""One actual next contact on the complete retained56-cell router state."""
from pathlib import Path
import sys,json,hashlib
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch,plan
z=json.loads((P/'prepared1564_router_crossing.json').read_text());H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H'];R={H[i:]+H[:i]for i in range(104)};V=((0,1),(1,0),(0,-1),(-1,0))
B=set(map(tuple,z['black']));p=tuple(z['pose'][0]);h=z['pose'][1];t=z['time'];cut=t+z['next_mismatch'];hist='';word=[]
for t in range(t,cut+100000):
 if t>=cut+208 and t%104==0 and hist[:104]==hist[104:] and hist[-104:]in R:
  w=hist[-104:];s=State(frozenset(B),p,h);nxt=first_mismatch(s,w);qs,d=plan(s,w)
  if nxt is None or nxt>1040:
   result=dict(status='CERTIFIED_CAPTURE'if nxt is None else'EXACT_INTERMEDIATE_FLIGHT',time=t,pose=[p,h],period_word=w,drift=d,next_mismatch=nxt,black=sorted(B),word_from_contact=''.join(word),contact_time=cut)
   break
 c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;u,v=V[h];p=p[0]+u,p[1]+v;hist=(hist+c)[-208:]
 if t>=cut:word.append(c)
else:result=dict(status='NO QUALIFYING TAIL IN DECLARED LOCAL CONTROL',time=t+1,pose=[p,h])
result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();(P/'prepared1564_router_second_contact.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k not in['period_word','black','word_from_contact']})
