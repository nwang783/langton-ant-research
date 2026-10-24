import json
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
def excursion(B,r,limit=20000):
 x,y,h=0,r,1;word=''
 for k in range(limit):
  bit=(x,y) in B;B.symmetric_difference_update({(x,y)});word+='L' if bit else 'R';h=(h+(3 if bit else 1))%4;dx,dy=D[h];x+=dx;y+=dy
  if x<0:return y,word
 return None,word
best=[];counts={};tested=0;unknown=0
for a in range(-100,101,2):
 for b in range(-100,101,2):
  B=set();e0,w0=excursion(B,0);e1,w1=excursion(B,a);e2,w2=excursion(B,b)
  if None in (e0,e1,e2):unknown+=1;continue
  c=e2+1;d=c-1-e1;r=[0,a,b,c,d];S=c-1;s=[S-r[(j+3)%5] for j in range(5)]
  assert s[:3]==[e0,e1,e2]
  trace=[dict(entry=0,exit=e0,word=w0),dict(entry=a,exit=e1,word=w1),dict(entry=b,exit=e2,word=w2)];completed=3;reason='UNKNOWN_ROUND_CAP'
  for j in range(3,100):
   e,w=excursion(B,r[j%5]);trace.append(dict(entry=r[j%5],exit=e,word=w))
   if e is None:reason='UNKNOWN_STEP_CAP';break
   if e!=s[j%5]:reason='WRONG_EXIT';break
   completed+=1
  tested+=1;counts[reason]=counts.get(reason,0)+1
  score=(completed,len(B))
  if not best or score>best[0]['score']:best=[dict(score=score,r=r,s=s,S=S,trace=trace,reason=reason)]
  elif score==best[0]['score'] and len(best)<30:best.append(dict(score=score,r=r,s=s,S=S,trace=trace,reason=reason))
print(tested,counts,'initial_unknown',unknown,'best',best[0]['score'])
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(tested=tested,counts=counts,initial_unknown=unknown,best=best),indent=2))
