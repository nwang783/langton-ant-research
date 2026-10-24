from collections import defaultdict,deque
import json
DIR=[(0,1),(1,0),(0,-1),(-1,0)]
def rot(p,h):
 x,y=p;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def plus(p,q):return p[0]+q[0],p[1]+q[1]
def edge(q,primal=True):
 x,y=q
 d=(1,1) if ((x+y)%2==0)==primal else (1,-1)
 return ((2*x-d[0],2*y-d[1]),(2*x+d[0],2*y+d[1]))
def wp(p,h):
 a=rot((1,-1),h);return 2*p[0]+a[0],2*p[1]+a[1]
def nbr(v):
 x,y=v
 return [(x+2,y+2),(x+2,y-2),(x-2,y+2),(x-2,y-2)]
def mid(a,b):return (a[0]+b[0])//4,(a[1]+b[1])//4
# Work on actual white dual graph; components are represented only when split.
# Infinite ambient graph is truncated well beyond all read supports, boundary wired.
B=set();p=(0,0);h=0;path=[]
for t in range(2000):
 q=p;L=q in B;path.append((q,h,'L' if L else 'R'))
 if L:B.remove(q);h=(h-1)%4
 else:B.add(q);h=(h+1)%4
 p=plus(p,DIR[h])
# Sufficient finite vertex universe with exterior wired: bounding actual dual endpoints+8.
vs=[v for q,h,l in path for v in edge(q,False)]
lo=[min(v[i]for v in vs)-8 for i in (0,1)];hi=[max(v[i]for v in vs)+8 for i in (0,1)]
V={(x,y)for x in range(lo[0],hi[0]+1,2)for y in range(lo[1],hi[1]+1,2)if(x+y)%4==0}
O=('outside',); V.add(O)
N={v:[]for v in V};W={}
for v in V-{O}:
 for n in nbr(v):
  q=mid(v,n)
  if n in V:N[v].append((n,q))
  else:N[v].append((O,None));N[O].append((v,None))
# Symmetric boundary sentinel edges never toggled.
labels={v:0 for v in V};groups={0:set(V)};active=0;new=0;created={0:-1};B=set();A=defaultdict(set)
events=[];w0=wp((0,0),0)
assert w0 in V
for t,(q,h,l)in enumerate(path):
 w=wp(q,h);assert labels[w]==active
 a,b=edge(q,False);assert w in(a,b);other=b if w==a else a
 u,v=edge(q,True)
 # Detect primal cycle status via finite current occupied graph after excluding q.
 def connected(u,v):
  seen={u};Q=deque([u])
  while Q:
   x=Q.popleft()
   for y in A[x]:
    if {x,y}=={u,v}:continue
    if y==v:return True
    if y not in seen:seen.add(y);Q.append(y)
  return False
 cyc=connected(u,v)
 if l=='R':
  B.add(q);A[u].add(v);A[v].add(u)
  if not cyc:continue
  # R removes a bridge in white dual; split active component using exact BFS.
  old=active;seen={other};Q=deque([other])
  while Q:
   x=Q.popleft()
   for y,c in N[x]:
    if y in seen or labels[y]!=old or(c is not None and c in B):continue
    seen.add(y);Q.append(y)
  assert w not in seen
  new+=1;groups[new]=seen;created[new]=t
  for x in seen:labels[x]=new
  groups[old]-=seen
  ev={'time':t,'kind':'seal','archive':new,'cell':q,'side_vertices':len(seen),'infinite':O in seen,'active_vertices':len(groups[old])}
  
  if new in (30,38):
   ev['vertices_doubled']=sorted(seen)
   ev['internal_white_cells']=sorted({c for x in seen for y,c in N[x] if y in seen and c is not None and c not in B})
   ev['boundary_black_cells']=sorted({c for x in seen for y,c in N[x] if y not in seen and c is not None})
  events.append(ev)
 else:
  B.remove(q);A[u].remove(v);A[v].remove(u)
  target=labels[other]
  if target==active:
   assert not cyc
   continue
  assert cyc
  # An L may release any adjacent archived white component.
  live=[x for x in groups if x!=active and O not in groups[x] and len(groups[x])>1]
  ev={'time':t,'kind':'release','archive':target,'cell':q,'born':created[target],'release_vertices':len(groups[target]),'newest_live':max(live,key=lambda x:created[x]) if live else None,'live_archives':len(live)}
  events.append(ev)
  for x in groups[target]:labels[x]=active
  groups[active]|=groups[target];del groups[target]
  if target==38:
   print('RELEASE38',json.dumps(ev));break
else:print('No nonLIFO')
print('events',len(events),'grid',len(V),'last',t)
open('/workspace/shared/langton/causal_white_archive_2026-10-23/probe_pockets_detail_events.json','w').write(json.dumps(events,indent=2)+'\n')
print(json.dumps(events[-30:],indent=2))
