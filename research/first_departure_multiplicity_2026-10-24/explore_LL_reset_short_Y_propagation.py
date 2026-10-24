"""Exact LL-root late-L3 supplier corner, full3x3 complete WHITE cap4 domain.
Not a period or radius scan: the square closes the two ACTUAL L3 suppliers
of the signed Y-X reset. OPEN models are not attained board factors/fronts.
"""
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict,deque
import json,time
base=Path(__file__).parent;lib={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],lib)
H=lib['H'];V=lib['V'];out=lib['out'];dom=lib['dom'];plainprop=lib['propagate'];check=lib['check']
raw=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0].split(' d={a:0 for a in ns}')[0]+" return'open'\n";dd={};exec(raw,dd);rankcheck=dd['check'];partial=Counter()
def prop(ds):
 z=plainprop(ds)
 if z is None:partial['port']+=1;return None
 h={p:a[0]for p,a in z.items()if len(a)==1};a=rankcheck(h)
 if a!='open':partial[a]+=1;return None
 return z

def classify(hs):
 ns=[(p,r)for p,h in hs.items()for r in range(len(h))];su={};pr={}
 for p,h in hs.items():
  for d,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   sr=[r for r in range(len(h))if out(h,r)==d];tr=[r for r,a in enumerate(hs[q])if a==d]
   assert len(sr)==len(tr)
   for a,b in zip(sr,tr):su[p,a]=q,b;pr[q,b]=p,a
 c={};cs=[]
 for n in ns:
  if n in pr:continue
  p=[];u=n;i=len(cs)
  while u not in c:
   c[u]=i;p.append(u)
   if u not in su:break
   u=su[u]
  cs.append(p)
 if len(c)!=len(ns):return'EVENT_CYCLE',None
 adj=defaultdict(set);ind=[0]*len(cs)
 for p,h in hs.items():
  for r in range(len(h)-1):
   a,b=c[p,r],c[p,r+1]
   if a!=b and b not in adj[a]:adj[a].add(b);ind[b]+=1
 q=deque(i for i in range(len(cs))if not ind[i]);n=0
 while q:
  a=q.popleft();n+=1
  for b in adj[a]:
   ind[b]-=1
   if not ind[b]:q.append(b)
 if n!=len(cs):return'BLOCK_PRECEDENCE_CYCLE',None
 x=((1,0),3);y=((1,1),3);a,b=c[x],c[y]
 if a==b:return('POSITIVE'if cs[a].index(x)<cs[a].index(y)else'NEGATIVE'),dict(blocks=cs,forced_same_block_difference=cs[a].index(y)-cs[a].index(x))
 def reachable(a,b):
  se={a};q=[a]
  while q:
   u=q.pop()
   if u==b:return True
   for z in adj[u]:
    if z not in se:se.add(z);q.append(z)
  return False
 if reachable(a,b):ans='POSITIVE'
 elif reachable(b,a):ans='NEGATIVE'
 else:ans='BOTH_ORDERS'
 return ans,dict(blocks=cs,rank_precedence={str(k):sorted(v)for k,v in adj.items()},X3_block=a,Y3_block=b)

stats=Counter();rows=[];t=time.time()
for rh in['EWW','EWWE']:
 fixed={(0,0):'NNSS',(1,0):'EEWW',(1,1):'SNNS',(0,1):rh};pts={(x,y)for x in range(3)for y in range(3)}
 ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in sorted(pts)});ct=Counter();samples={}
 def rec(ds):
  if all(len(a)==1 for a in ds.values()):
   hs={p:a[0]for p,a in ds.items()};a=check(hs)
   if a=='open':
    a,ob=classify(hs)
    if a not in ['POSITIVE','NEGATIVE','BOTH_ORDERS']:pass
    else:
     su={}
     for p,h in hs.items():
      for dr,dv in V.items():
       q=p[0]+dv[0],p[1]+dv[1]
       if q not in hs:continue
       sr=[r for r in range(len(h))if out(h,r)==dr];tr=[r for r,z in enumerate(hs[q])if z==dr]
       su.update({(p,r):(q,z)for r,z in zip(sr,tr)})
     cy=((1,1),2);ry=[cy]
     for _ in range(4):
      if cy not in su:break
      cy=su[cy];ry.append(cy)
     if len(ry)!=5 or cy!=((1,1),3):a='NOT_SHORT_Y'
     else:
      cx=((1,0),2);rx=[cx]
      for _ in range(4):
       if cx not in su:break
       cx=su[cx];rx.append(cx)
      isshort=len(rx)==5 and cx==((1,0),3)
      a='SHORT_BOTH'if isshort else'SHORT_Y_OPEN_X'
      ob=dict(Y_route=ry,X_route=rx)
   else:ob=None
   ct[a]+=1
   if a not in samples:samples[a]=dict(histories={str(p):h for p,h in hs.items()},details=ob)
   return
  p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   z=prop(ds|{p:[h]})
   if z is not None:rec(z)
 if ds is not None:rec(ds)
 rows.append(dict(root=rh,counts=dict(ct),first_samples=samples));stats.update(ct);print(rh,dict(ct),'partial',dict(partial),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(stats),partial_rejections=dict(partial),rows=rows),indent=2)+'\n');print('DONE',time.time()-t,dict(stats))
