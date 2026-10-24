"""Independent literal port transducer of the first three (+2,0) rows."""
from collections import defaultdict
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0));ROOT=Path(__file__).resolve().parents[1]
def histories(r,n,a,b=None,upper_length=None):
 if r==0:
  ps=[a,a+1,a+2];qs=[a,a+2,a+3]
  if n==5:
   assert b is not None and b>=a+4 and b%2==0;ps.append(b+2);qs.append(b)
  else:assert n==4
 elif r==2:
  assert n==5 and b is not None and b>=a+4 and b%2==0
  ps=[a+2,b-1,b,b+2];qs=[a,b,b+1,b+2]
 else:raise ValueError(r)
 assert a>=0 and a%2==0
 length=max(ps+qs)+1 if upper_length is None else upper_length
 assert length>max(ps+qs)
 # Each tuple contains incoming directions, all turns alternate from R.
 rows={(0,0):[3],(1,0):[2],(0,1):[0 if j==r+2 else 2 for j in range(n)],(1,1):[]}
 for j in range(n):
  outgoing=2 if j==r else 0;rows[1,1].append((outgoing-(1 if j%2==0 else -1))%4)
 rows[1,2]=[0 if j in ps else 2 for j in range(length)];rows[0,2]=[]
 for j in range(length):
  outgoing=2 if j in qs else 0;rows[0,2].append((outgoing-(1 if j%2==0 else -1))%4)
 return rows,ps,qs

def transducer(rows):
 arrivals={};departures={};outgoing={}
 for cell,ins in rows.items():
  for j,h in enumerate(ins):
   ev=cell+(j,);o=(h+(1 if j%2==0 else -1))%4;outgoing[ev]=o
   arrivals.setdefault((cell,h),[]).append(ev);departures.setdefault((cell,o),[]).append(ev)
 succ={}
 for ev,o in outgoing.items():
  x,y,j=ev;dx,dy=D[o];cell=((x+dx)%2,y+dy)
  if cell not in rows:continue
  ordinal=departures[((x,y),o)].index(ev)
  assert len(departures[((x,y),o)])==len(arrivals.get((cell,o),[])),(ev,o,cell)
  succ[ev]=arrivals[cell,o][ordinal]
 inputs=arrivals[((1,2),2)];outputs=departures[((0,2),0)];result=[]
 for j,ev in enumerate(inputs):
  p=(1,2);path=[(1,3),p];word='S';events=[]
  while True:
   assert ev not in events,'sealed internal event cycle';events.append(ev)
   o=outgoing[ev];dx,dy=D[o];p=p[0]+dx,p[1]+dy;path.append(p);word+='NESW'[o]
   if p[1]==3:
    assert o==0 and p[0]%2==0;result.append({'input':j,'output':outputs.index(ev),'word':word,'length':len(word),'voltage':p[0]//2,'positions':path,'events':events});break
   assert p[1]in range(3);ev=succ[ev]
 return result
if __name__=='__main__':
 records=[]
 for n,a,b in [(4,0,None),(4,2,None),(4,4,None),(5,0,4),(5,2,6),(5,4,8)]:
  rows,p,q=histories(0,n,a,b)
  table=transducer(rows);records.append({'r':0,'n':n,'a':a,'b':b,'ports':table})
  if a==2:
   assert [(t['input'],t['output'],t['length'],t['voltage'])for t in table[:3]]==[(0,0,3,0),(1,1,3,1),(2,2,19,2)]
  if a>=4:assert [(t['output'],t['length'],t['voltage'])for t in table[:4]]==[(j,3,j%2)for j in range(4)]
 for a,b in[(0,4),(0,6),(2,6),(4,8)]:
  rows,p,q=histories(2,5,a,b);records.append({'r':2,'n':5,'a':a,'b':b,'ports':transducer(rows)})
 (ROOT/'audits/axis_lower_strip_paths_independent.json').write_text(json.dumps({'status':'PASS exact first-three-row port transducers','records':records},indent=2)+'\n')
 print(json.dumps({'status':'PASS','cases':len(records),'nineteen_step_words':[x['ports'][2]['word']for x in records if x['r']==0 and x['a']==2]}))
