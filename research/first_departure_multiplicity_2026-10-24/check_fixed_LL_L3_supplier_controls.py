"""Two exact complete3x3 WHITE cap4 local late-supplier controls.
They are necessary port/height/injective-channel-clock networks, NOT ant
factors or complete translating fronts. No exterior connector is supplied.
"""
from pathlib import Path
from collections import defaultdict,deque
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def phase(p):return 2*(p[0]%2)if sum(p)%2==0 else 3-2*(p[0]%2)
def fp(p,h):
 x,y=p;return {'E':((x,y-1),(x,y)),'W':((x-1,y),(x-1,y-1)),'N':((x,y),(x-1,y)),'S':((x-1,y-1),(x,y-1))}[h]
base={(0,0):'NNSS',(0,1):'EWW',(0,2):'SSNS',(1,0):'EEWW',(1,1):'SNNS',(1,2):'EEE',(2,0):'NNS'}
rows=[]
for kind,extra in [('positive',{(2,1):'EE',(2,2):'N'}),('negative',{(2,1):'WEE',(2,2):'NSN'})]:
 hs=base|extra;events={(p,r)for p,h in hs.items()for r in range(len(h))};succ={};prev={};eq={}
 for p,h in hs.items():
  assert len(h)<=4
  for dr,v in V.items():
   sr=[r for r in range(len(h))if out(h,r)==dr];q=p[0]+v[0],p[1]+v[1]
   if q in hs:
    tr=[r for r,a in enumerate(hs[q])if a==dr];assert len(sr)==len(tr)
    for r,s in zip(sr,tr):succ[p,r]=q,s;prev[q,s]=p,r
  for dr in('EW'if sum(p)%2==0 else'NS'):eq[p,dr]=sum(out(h,r)==dr for r in range(len(h)))
  for dr in('NS'if sum(p)%2==0 else'EW'):
   q=p[0]-V[dr][0],p[1]-V[dr][1];f=h.count(dr)
   if(q,dr)in eq:assert eq[q,dr]==f
   eq[q,dr]=f
 adj=defaultdict(list)
 for(p,dr),f in eq.items():
  c,l=fp(p,dr);adj[l].append((c,f));adj[c].append((l,-f))
 val={(0,-1):0};q=deque(val)
 while q:
  u=q.popleft()
  for v,f in adj[u]:
   if v in val:assert val[v]==val[u]+f
   else:val[v]=val[u]+f;q.append(v)
 assert len(val)==len(adj)
 assert max(v for p,v in val.items()if sum(p)%2)==0
 assert max(v+1 for p,v in val.items()if sum(p)%2==0)<=0
 blocks=[];cid={}
 for e in sorted(events):
  if e in prev:continue
  u=e;cs=[];i=len(blocks)
  while u not in cid:
   cid[u]=i;cs.append(u)
   if u not in succ:break
   u=succ[u]
  blocks.append(cs)
 assert len(cid)==len(events)
 orderadj=defaultdict(set);ind=[0]*len(blocks)
 for p,h in hs.items():
  for r in range(len(h)-1):
   a,b=cid[p,r],cid[p,r+1]
   if a!=b and b not in orderadj[a]:orderadj[a].add(b);ind[b]+=1
 q=deque(i for i in range(len(blocks))if not ind[i]);order=[]
 while q:
  a=q.popleft();order.append(a)
  for b in orderadj[a]:
   ind[b]-=1
   if not ind[b]:q.append(b)
 assert len(order)==len(blocks)
 T={};end=-100;scheduled=[]
 for c in order:
  bl=blocks[c];p=bl[0][0];start=end+40;start+=(phase(p)-start)%4
  for i,e in enumerate(bl):T[e]=start+i
  end=start+len(bl)-1;scheduled.append(dict(component=c,start=start,events=bl))
 assert len(set(T.values()))==len(T)
 for e,f in succ.items():assert T[f]==T[e]+1
 for p,h in hs.items():
  for r in range(len(h)):
   assert T[p,r]%4==phase(p)
   if r:assert T[p,r]-T[p,r-1]>=4
 X=((1,0),3);Y=((1,1),3);tail=T[Y]-T[X]
 assert (tail>0)==(kind=='positive')
 if kind=='negative':
  route=[Y,((2,1),2),((2,0),2),X]
  early=[((1,0),2),((1,1),2),((2,1),1),((2,2),2)]
  assert all(succ[a]==b for a,b in zip(route,route[1:]))and tail==-3
  assert all(succ[a]==b for a,b in zip(early,early[1:]))
 else:route=None;early=None
 rows.append(dict(kind=kind,histories={str(p):h for p,h in hs.items()},stream={str(p):v for p,v in val.items()},complete_literal_channels=scheduled,times=[dict(cell=p,rank=r,time=t)for(p,r),t in sorted(T.items())],tail_Y3_minus_X3=tail,negative_late_chain=route,required_earlier_middle_chain=early))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows),indent=2)+'\n');print('PASS fixed supplier controls',[(r['kind'],r['tail_Y3_minus_X3'])for r in rows])
