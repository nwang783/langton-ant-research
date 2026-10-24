"""Fixed terminal LL portal: an eight-cell upper-side completion obstruction.
Complete WHITE cap-four histories, exact physical ordinal returns and clocks.
GLOBAL-M is used only to derive the five Q-square modes; arbitrary older stock
and every 0..4-read history at the two final readers are retained.
"""
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict,deque
import json
b=Path(__file__).parent
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def words(ax):return ['']+[''.join(w) for n in range(1,5) for w in product(ax,repeat=n)]
def fp(p,h):
 x,y=p
 return {'E':((x,y-1),(x,y)),'W':((x-1,y),(x-1,y-1)),'N':((x,y),(x-1,y)),'S':((x-1,y-1),(x,y-1))}[h]
def analyze(hs):
 nodes=[(p,r) for p,h in hs.items() for r in range(len(h))];su={};edges=[];flow={}
 for p,h in hs.items():
  for r in range(len(h)-1):edges.append(((p,r),(p,r+1),4,'same_cell'))
  for dr in ('EW' if sum(p)%2==0 else 'NS'):
   flow[p,dr]=sum(out(h,r)==dr for r in range(len(h)))
  for dr in ('NS' if sum(p)%2==0 else 'EW'):
   q=p[0]-V[dr][0],p[1]-V[dr][1];n=h.count(dr)
   if (q,dr) in flow and flow[q,dr]!=n:return 'port',None
   flow[q,dr]=n
  for dr,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   sr=[r for r in range(len(h)) if out(h,r)==dr];tr=[r for r,a in enumerate(hs[q]) if a==dr]
   if len(sr)!=len(tr):return 'port',None
   for r,s in zip(sr,tr):
    a,e=(p,r),(q,s);su[a]=e;edges.extend([(a,e,1,'actual'),(e,a,-1,'actual_reverse')])
 for a in sorted(su):
  path=[a];cur=a;seen={a}
  while cur in su:
   cur=su[cur];path.append(cur)
   if cur[0]==a[0]:
    if cur[1]!=a[1]+1:return 'rank',dict(path=path)
    break
   assert cur not in seen
   seen.add(cur)
 d={a:0 for a in nodes};pred={}
 for _ in nodes:
  changed=None
  for a,e,w,label in edges:
   if d[e]<d[a]+w:d[e]=d[a]+w;pred[e]=(a,e,w,label);changed=e
  if changed is None:break
 else:
  cur=changed
  for _ in nodes:cur=pred[cur][0]
  start=cur;cycle=[]
  while True:
   ed=pred[cur];cycle.append(ed);cur=ed[0]
   if cur==start:break
  cycle.reverse()
  assert sum(e[2] for e in cycle)>0
  assert all(cycle[i][1]==cycle[(i+1)%len(cycle)][0] for i in range(len(cycle)))
  return 'clock',dict(cycle=cycle,total=sum(e[2] for e in cycle))
 adj=defaultdict(list)
 for (p,dr),f in flow.items():
  c,l=fp(p,dr);adj[l].append((c,f));adj[c].append((l,-f))
 val={(0,-1):0};queue=deque([(0,-1)])
 while queue:
  u=queue.popleft()
  for v,w in adj[u]:
   if v in val:assert val[v]==val[u]+w
   else:val[v]=val[u]+w;queue.append(v)
 assert len(val)==len(adj)
 bad=[(p,z) for p,z in val.items() if sum(p)%2 and z>0]
 if bad:return 'higher_C',dict(higher_C=bad,face_values=[[p,z] for p,z in sorted(val.items())])
 return 'open',dict(successor_edges=[[a,e] for a,e in sorted(su.items())],face_values=[[p,z] for p,z in sorted(val.items())])
# Shift the physical Q face (1,2) to bottom-left (0,-1); this preserves parity.
stage1=[];ct1=Counter();tops=[]
for r,a,z in product(['SNN','SNNS'],words('NS'),words('EW')):
 hs={(0,-1):'WWEE',(1,-1):r,(0,0):a,(1,0):z}
 res,cert=analyze(hs);ct1[res]+=1
 if res!='port':stage1.append(dict(R=r,U=a,W=z,result=res,certificate=cert))
 if res=='open':tops.append((r,a,z))
assert ct1=={'port':1869,'rank':43,'clock':1,'higher_C':4,'open':5}
assert tops==[('SNN','SSNN','EE'),('SNN','SSNN','EEW'),('SNNS','SNN','WWE'),('SNNS','SNNS','WWEE'),('SNNS','SSNN','EEWW')]
# Z,Y are the upper boundary of the specified portal. L,K are complete unknown
# readers, NOT first-used/last-used, and may be empty or have any 1..4 reads.
ct2=Counter();stage2=[]
for (r,a,z),ll,k in product(tops,words('EW'),words('NS')):
 hs={(-2,-1):'EEWW',(-1,-1):'SNNS',(0,-1):'WWEE',(1,-1):r,(0,0):a,(1,0):z,(-1,0):ll,(-2,0):k}
 res,cert=analyze(hs);ct2[res]+=1
 if res!='port':stage2.append(dict(R=r,U=a,W=z,L=ll,K=k,result=res,certificate=cert))
assert ct2=={'port':4695,'rank':100,'clock':10}
assert all(row['result'] in ['rank','clock'] for row in stage2)
obj=dict(scope=__doc__,physical_translation=[-1,-3],Q_square_counts=dict(ct1),Q_square_modes=tops,Q_square_nonport_rows=stage1,
 upper_eight_counts=dict(ct2),upper_eight_nonport_rows=stage2,
 warning='Only this fixed terminal-LL/even-root portal is excluded under its signed complete WHITE cap-four and GLOBAL-M premises. No all-cap maximum, arbitrary mixed boundary exclusion, initial fuel or regeneration claim.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n')
print('PASS Q square1922 -> five modes; eight-cell4805 ->4695port+100rank+10positive-clock; no completion')
