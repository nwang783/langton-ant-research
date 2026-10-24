import itertools,json,random
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
def exc(B,r,limit=20000):
 x,y,h=0,r,1;n=0
 for k in range(limit):
  bit=(x,y) in B;B.symmetric_difference_update({(x,y)});h=(h+(3 if bit else 1))%4;dx,dy=D[h];x+=dx;y+=dy;n+=1
  if x<0:return y,n
 return None,n
results=[]
for q,lo,hi in [(7,-10,10),(9,-6,6),(11,-4,4)]:
 k=(q-1)//2;delta=k+1;best=None;counts={};tested=0
 for vals in itertools.product(range(lo,hi+1,2),repeat=k):
  r=[0,*vals];B=set();exits=[];times=[]
  for v in r:
   e,t=exc(B,v);exits.append(e);times.append(t)
   if e is None:break
  if exits[-1] is None:counts['UNKNOWN_INITIAL']=counts.get('UNKNOWN_INITIAL',0)+1;continue
  S=exits[k];r.extend(S-exits[j] for j in range(k));assert len(r)==q
  s=[S-r[(j+delta)%q] for j in range(q)];assert s[:delta]==exits
  completed=delta;reason='UNKNOWN_ROUND'
  for j in range(delta,100):
   e,t=exc(B,r[j%q]);exits.append(e);times.append(t)
   if e is None:reason='UNKNOWN_STEP';break
   if e!=s[j%q]:reason='WRONG_EXIT';break
   completed+=1
  tested+=1;counts[reason]=counts.get(reason,0)+1
  score=(completed,sum(times))
  if best is None or score>tuple(best['score']):best=dict(score=score,r=r,s=s,S=S,actual_exits=exits,times=times,reason=reason)
  if completed>q:print('ABOVE_Q',q,best,flush=True);break
 results.append(dict(q=q,range=[lo,hi,2],tested=tested,counts=counts,best=best));print(q,tested,counts,best,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2))
