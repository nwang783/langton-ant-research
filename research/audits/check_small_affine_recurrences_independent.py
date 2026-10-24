"""Independent complete finite exclusion for binary affine pose recurrences.
Generate canonically BFS-labelled accessible state graphs recursively, build
all locally realizable ant prefixes by first-visit branching, and derive every
state's arbitrary offset pair. No original recurrence/automaton code imported.
"""
from collections import defaultdict,Counter
from pathlib import Path
import json,time
D=((0,1),(1,0),(0,-1),(-1,0))
SCALES=((-1,-1),(-1,1),(1,-1),(1,1))
def mul(a,p):return(a[0]*p[0]-a[1]*p[1],a[0]*p[1]+a[1]*p[0])
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def norm(seq):
 d={};out=[]
 for x in seq:
  if x not in d:d[x]=len(d)
  out.append(d[x])
 return tuple(out)
def partitions(m):
 def f(p):
  if len(p)==m:yield tuple(p);return
  for x in range(max(p)+2):yield from f(p+[x])
 yield from f([0])
def graphs(m):
 if m==1:yield((0,0),);return
 arcs=[0,1]
 def extend(discovered):
  if len(arcs)==2*m:
   if discovered==m:yield tuple(tuple(arcs[i:i+2])for i in range(0,2*m,2))
   return
  source=len(arcs)//2
  if source>=discovered:return
  for dest in range(min(m,discovered+1)):
   arcs.append(dest)
   yield from extend(max(discovered,dest+1))
   arcs.pop()
 yield from extend(2)
def states(T,L):
 s=[0]*L
 for n in range(1,L):s[n]=T[s[n//2]][n%2]
 return s
def prefixes(length):
 seen={};positions=[(0,0)]
 def rec(h):
  if len(positions)==length+1:yield tuple(positions);return
  p=positions[-1];old=seen.get(p)
  for turn in ((1-old,)if old is not None else(0,1)):
   seen[p]=turn;nh=(h+(1 if turn==0 else-1))%4
   positions.append(add(p,D[nh]));yield from rec(nh);positions.pop()
  if old is None:del seen[p]
  else:seen[p]=old
 yield from rec(0)
def reject(T,a,b,limit=64):
 s=states(T,limit+1);p=[(0,0)]*(limit+1)
 for n in range(1,limit+1):p[n]=add(mul(a,p[n//2]),b[s[n//2]][n%2])
 h=0;last={}
 for t in range(limit):
  step=sub(p[t+1],p[t])
  if step not in D:return('nonunit',t)
  nh=D.index(step);turn=(nh-h)%4
  if turn not in(1,3):return('nonquarter',t)
  if p[t]in last and last[p[t]]==turn:return('equal consecutive reads',t)
  last[p[t]]=turn;h=nh
 return None
results=[]
for m in range(1,5):
 start=time.monotonic();L=2**(m-1);index=defaultdict(set);Ts=list(graphs(m))
 for T in Ts:
  s=states(T,L);assert len(set(s))==m
  assert norm(s)==tuple(s)
  reps=tuple(s.index(i)for i in range(m))
  for part in partitions(m):index[norm(part[i]for i in s)].add((T,reps))
 models=set();outcomes=Counter();latest=-1;prefix_count=0
 for ps in prefixes(2**m-1):
  prefix_count+=1
  for a in SCALES:
   off=tuple(tuple(sub(ps[2*n+j],mul(a,ps[n]))for j in(0,1))for n in range(L))
   for T,reps in index.get(norm(off),()):
    b=tuple(off[n]for n in reps);key=(T,a,b)
    if key in models:continue
    models.add(key);r=reject(T,a,b)
    assert r is not None,('SURVIVOR',key)
    outcomes[r[0]]+=1;latest=max(latest,r[1])
 expected={1:8,2:128,3:1512,4:3924}[m]
 assert len(models)==expected,(m,len(models),expected)
 result={'states':m,'graphs':len(Ts),'legal_prefixes':prefix_count,'recurrences':len(models),'rejections':dict(outcomes),'latest_failure':latest,'elapsed_seconds':time.monotonic()-start}
 results.append(result);print(json.dumps(result),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'status':'PASS','scope':'Binary time; common scale a in{+-1+-i}; <=4 accessible stable-leading-zero states; arbitrary Gaussian integer offsets; no possible ant trajectory, irrespective of seed size.','results':results},indent=2)+'\n')
