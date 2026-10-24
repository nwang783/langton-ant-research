"""Fixed five-corner symbolic flow2 row, retaining odd LEFT mode and all exterior gates.
No period, drift, width, segment-length or front search.
"""
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict,deque
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
A={'X':'NNSS','Y':'NSSN'};B={'O':'WEE','U':'WEEW','V':'WWEE'}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def words(axis):return['']+[''.join(x)for n in range(1,5)for x in product(axis,repeat=n)]
def cnt(h,p,kin):return sum((x if kin=='in'else out(h,i))==p for i,x in enumerate(h))
NS=words('NS');EW=words('EW')
def fp(p,h):
 x,y=p;return {'E':((x,y-1),(x,y)),'W':((x-1,y),(x-1,y-1)),'N':((x,y),(x-1,y)),'S':((x-1,y-1),(x,y-1))}[h]
def check(hs):
 ns=[(p,r)for p,h in hs.items()for r in range(len(h))];es=[];succ={};eq={}
 for p,h in hs.items():
  for r in range(len(h)-1):es.append(((p,r),(p,r+1),4))
  ia='NS'if sum(p)%2==0 else'EW';oa='EW'if sum(p)%2==0 else'NS'
  for dr in oa:eq[p,dr]=cnt(h,dr,'out')
  for dr in ia:
   q=(p[0]-V[dr][0],p[1]-V[dr][1]);f=cnt(h,dr,'in')
   if (q,dr)in eq and eq[q,dr]!=f:return'port'
   eq[q,dr]=f
  for dr in H:
   q=(p[0]+V[dr][0],p[1]+V[dr][1]);sr=[r for r in range(len(h))if out(h,r)==dr]
   if q not in hs:continue
   tr=[r for r,x in enumerate(hs[q])if x==dr]
   if len(sr)!=len(tr):return'port'
   for x,y in zip(sr,tr):
    a,b=(p,x),(q,y);succ[a]=b;es.extend([(a,b,1),(b,a,-1)])
 for a in ns:
  cur=a;seen={a}
  for _ in range(len(ns)+1):
   if cur not in succ:break
   cur=succ[cur]
   if cur[0]==a[0]:
    if cur[1]!=a[1]+1:return'skipped_rank'
    break
   if cur in seen:return'event_cycle'
   seen.add(cur)
 d={a:0 for a in ns}
 for _ in ns:
  ch=False
  for a,b,k in es:
   if d[b]<d[a]+k:d[b]=d[a]+k;ch=True
  if not ch:break
 else:return'clock_cycle'
 adj=defaultdict(list)
 for(p,dr),f in eq.items():
  c,l=fp(p,dr);adj[l].append((c,f));adj[c].append((l,-f))
 val={(0,-1):0};q=deque([(0,-1)])
 while q:
  u=q.popleft()
  for v,w in adj[u]:
   if v in val:
    if val[v]!=val[u]+w:return'height_cycle'
   else:val[v]=val[u]+w;q.append(v)
 assert len(val)==len(adj)
 if any(z>0 for p,z in val.items()if sum(p)%2):return'global_C_max'
 return'open'
rows=[];n=0
for bp,a,b,an,bn in product('OUV','XY','OUV','XY','OUV'):
 base={(0,-1):B[bp],(0,0):A[a],(1,0):B[b],(1,1):A[an],(2,1):B[bn]}
 d0=[h for h in NS if cnt(h,'S','in')==cnt(B[b],'S','out')and cnt(h,'W','out')==cnt(B[bp],'W','in')]
 d1=[h for h in NS if cnt(h,'S','in')==cnt(B[bn],'S','out')and cnt(h,'W','out')==cnt(B[b],'W','in')]
 good=[];bad=Counter()
 for u,v in product(d0,d1):
  ee=[h for h in EW if cnt(h,'E','in')==cnt(u,'E','out')and cnt(h,'N','out')==cnt(v,'N','in')]
  for eh in ee:
   n+=1;ans=check(base|{(1,-1):u,(2,0):v,(2,-1):eh});bad[ans]+=1
   if ans=='open':good.append(dict(D0=u,D1=v,E=eh))
 rows.append(dict(Bprev=bp,A=a,B=b,Anext=an,Bnext=bn,open_completions=good,rejections=dict(bad)))
assert n==5700 and sum(bool(r['open_completions'])for r in rows)==8
assert all(r['B']in'OU'and r['Bprev']in'UV'for r in rows if r['open_completions'])
obj=dict(scope=__doc__,candidates=n,rows=rows,admissible_count=sum(bool(r['open_completions'])for r in rows),warning='Necessary fixed-window row language at global selected C height M. Open modes are not board factors or translating-front positives; global rank clocks and farther exterior ports remain open.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(n,'candidates;',obj['admissible_count'],'open five-corner words')
for r in rows:
 if r['open_completions']:print({k:v for k,v in r.items()if k!='rejections'})
