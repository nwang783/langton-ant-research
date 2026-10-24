"""Small derived four-corner palette; finite controls only until symbolic proof."""
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0))
def profile(a,cap,r):
 w=(a*r+cap)*4;p=(0,0);h=1;last={};I=set()
 for t,c in enumerate(w):
  if p in last and last[p][0]==c:return None
  if p not in last and c=='L':I.add(p)
  last[p]=(c,t);h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 if (p,h)!=((0,0),1):return None
 O={p for p,(c,t)in last.items()if c=='R'}
 return I,O,w

def rot(p,k):
 x,y=p
 for _ in range(k):x,y=-y,x
 return x,y

def matches(X,Y):
 for k in range(4):
  Z={rot(p,k)for p in Y};a=min(X);b=min(Z);d=(a[0]-b[0],a[1]-b[1])
  if {(x+d[0],y+d[1])for x,y in Z}==X:yield k,d
if __name__=='__main__':
 defs=[(a,c)for a in('LRRL','RLLR')for c in('R','LRR','RLR','RRL')]
 good=[q for q in defs if all(profile(*q,r)for r in(1,2,3,10))]
 records=[]
 for i,q in enumerate(good):
  for j,z in enumerate(good):
   for off in(-1,0,1):
    controls=[]
    for r in(3,4,10):
     X=profile(*q,r)[1];Y=profile(*z,r+off)[0];controls.append(list(matches(X,Y)))
    if all(controls):records.append(dict(source=q,target=z,target_r_offset=off,matches=controls))
 out=dict(scope=__doc__,legal_definitions=good,records=records)
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
