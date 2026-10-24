"""Complete unit-square reset interface of a flow-two RLLR departure subpath.
Fixed four-corner cover, all named WHITE histories, exact rank clocks and all open ports.
No period, length, support or front scan; surviving rows are only necessary open modes.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def rr(h,dr,kind):return [r for r in range(len(h))if (h[r]if kind=='in'else out(h,r))==dr]
pos={'Z':(0,0),'A':(1,0),'B':(1,1),'Y':(0,1)};inv={p:u for u,p in pos.items()}
alpha={'Z':['NSS','NNSS','NSSN'],'A':['EEWW','EWWE'],'B':['SNNS','SSNN'],'Y':['EWW','EEWW','EWWE']}
def check(hs):
 nodes=[(u,r)for u,h in hs.items()for r in range(len(h))];es=[];succ={};edges=[];ins=[];outs=[]
 for u,h in hs.items():
  p=pos[u]
  for r in range(len(h)-1):es.append(((u,r),(u,r+1),4))
  for dr in H:
   q=(p[0]+V[dr][0],p[1]+V[dr][1]);sr=rr(h,dr,'out')
   if q in inv:
    v=inv[q];tr=rr(hs[v],dr,'in')
    if len(sr)!=len(tr):return 'port',None
    for j,(a,b) in enumerate(zip(sr,tr),1):
     s,t=(u,a),(v,b);succ[s]=t;es.extend([(s,t,1),(t,s,-1)]);edges.append([u,a,v,b,dr,j])
   else:
    for j,r in enumerate(sr,1):outs.append([u,r,q,dr,j])
   p0=(p[0]-V[dr][0],p[1]-V[dr][1])
   if p0 not in inv:
    for j,r in enumerate(rr(h,dr,'in'),1):ins.append([p0,u,r,dr,j])
 for s in nodes:
  cur=s;seen={s}
  for _ in nodes:
   if cur not in succ:break
   cur=succ[cur]
   if cur[0]==s[0]:
    if cur[1]!=s[1]+1:return 'skipped rank',None
    break
   if cur in seen:return 'closed internal event orbit',None
   seen.add(cur)
 dist={s:0 for s in nodes}
 for _ in nodes:
  changed=False
  for s,t,w in es:
   if dist[t]<dist[s]+w:dist[t]=dist[s]+w;changed=True
  if not changed:break
 else:return 'positive clock cycle',None
 # Every ingress has a full literal channel to an egress; no missing rank is suppressed.
 channels=[]
 for e in ins:
  cur=(e[1],e[2]);route=[]
  for _ in nodes:
   route.append(cur)
   if cur not in succ:break
   cur=succ[cur]
  else:raise AssertionError('unexpected internal cycle')
  last=next(o for o in outs if o[:2]==list(cur))
  channels.append(dict(ingress=e,route=route,egress=last,physical_steps=len(route)+1))
 return 'open',dict(edges=edges,ingresses=ins,egresses=outs,channels=channels)
rows=[];bad=Counter()
for z,a,b,y in product(alpha['Z'],alpha['A'],alpha['B'],alpha['Y']):
 hs=dict(Z=z,A=a,B=b,Y=y);result,data=check(hs);bad[result]+=1
 if result=='open':rows.append(dict(histories=hs,**data))
obj=dict(scope=__doc__,alphabets=alpha,count=36,rejections=dict(bad),necessary_open_rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n')
print(bad)
for r in rows:print(r['histories'])
