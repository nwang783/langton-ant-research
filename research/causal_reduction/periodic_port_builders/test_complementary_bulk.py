"""Exploratory controls only: complementary six-row columns, no endcaps."""
import json,pathlib
D=((0,1),(1,0),(0,-1),(-1,0));entries=(0,2,4);exits=(1,5,3)

def trial(P,n,limit=100000):
 C={(x,y)for x in range(2*n)for y in range(6)if (P>>y&1)^(x%2)};history=[];steps=0
 for j in range(30):
  x,y,h=0,entries[j%3],1;word=[]
  while x>=0:
   if len(word)>=limit:return dict(status='TIME_CAP',completed=j,steps=steps)
   if not(-10<=y<=15):return dict(status='HEIGHT_ESCAPE',completed=j,steps=steps,pose=(x,y,h))
   p=x,y;black=p in C
   if black:C.remove(p)
   else:C.add(p)
   z='L'if black else'R';word.append(z);h=(h+(-1 if black else 1))%4;dx,dy=D[h];x+=dx;y+=dy;steps+=1
  history.append(dict(exit=y,steps=len(word),word=''.join(word),mass=len(C)))
  if y!=exits[j%3]:return dict(status='PORT_MISMATCH',completed=j,steps=steps,history=history)
 return dict(status='THIRTY_EXCURSIONS_ONLY',completed=30,steps=steps,history=history,field=sorted(C))
if __name__=='__main__':
 patterns=[P for P in range(64)if sum((1 if y%2==0 else-1)*(P>>y&1)for y in range(6))%4==0]
 assert len(patterns)==20
 out=[dict(P=P,n=n,**trial(P,n))for P in patterns for n in(1,2,3,5,10,20)]
 path=pathlib.Path(__file__).resolve().parent/'complementary_bulk_controls.json';path.write_text(json.dumps(out,indent=2))
 from collections import Counter
 print(Counter(r['status']for r in out));print('max complete excursions',max(r['completed']for r in out))
 print([(r['P'],r['n'],r['completed'])for r in out if r['completed']])
