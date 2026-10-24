"""Independent all-width zone-graph closure, unpruned histories and Bellman-Ford.
No producer modules are imported. Finite weakening is treated as overapproximation.
"""
from pathlib import Path
from itertools import product,permutations
from collections import Counter,deque
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[1];P=Path(sys.argv[1]).resolve();J=json.loads(P.read_text());par=J['parameters'];N=par['full_drift'][0];CAP=par['cap'];K=2;BOUND=par['bound'];MOD=par['modulus'];dirs=(1j,1,-1j,-1);INF=10**6
raw=[];ports={};unpruned=0
for p in(0,1):
 locals_=[[h for m in range(CAP+1)for h in product((1,-1)if(p+c)%2==0 else(1j,-1j),repeat=m)]for c in range(N)]
 hs=[]
 for row in product(*locals_):
  unpruned+=1;v=tuple((Counter(h),Counter(x*(-1j if r%2==0 else 1j)for r,x in enumerate(h)))for h in row)
  if any(v[c][1][d]!=v[(c+int(d.real))%N][0][d]for c in range(N)for d in(1,-1)):continue
  hs.append(row);ports[p,row]=v
 raw.append(hs)
# Exact horizontal row arcs were already matched; only N/S cross a boundary.
def sig_old(p,row):
 v=ports[p,row];return tuple(v[c][1][1j]for c in range(N))+tuple(v[c][0][-1j]for c in range(N))
def sig_new(p,row):
 v=ports[p,row];return tuple(v[c][0][1j]for c in range(N))+tuple(v[c][1][-1j]for c in range(N))
adj={}
for p in(0,1):
 ix={}
 for row in raw[1-p]:ix.setdefault(sig_new(1-p,row),[]).append(row)
 for row in raw[p]:adj[p,row]=ix.get(sig_old(p,row),[])
def outheading(h,r):return h*(-1j if r%2==0 else 1j)
def successors(histories):
 events={(i,(c,r))for i,row in enumerate(histories)for c,h in enumerate(row)for r in range(len(h))};succ={}
 for i,row in enumerate(histories):
  for c,h in enumerate(row):
   for r,x in enumerate(h):
    d=outheading(x,r);to=i+int(d.imag);dc=(c+int(d.real))%N;w=(c+int(d.real))//N
    if 0<=to<len(histories):
     ordinal=sum(outheading(y,j)==d for j,y in enumerate(h[:r]));arr=[j for j,y in enumerate(histories[to][dc])if y==d]
     assert ordinal<len(arr);succ[i,(c,r)]=((to,(dc,arr[ordinal])),w)
 return events,succ
windowcache={}
def window_bad(hist):
 if hist in windowcache:return windowcache[hist]
 events,succ=successors(hist);done=set()
 for start in events:
  seq=[];at={};u=start
  while u in succ and u not in done and u not in at:at[u]=len(seq);seq.append(u);u=succ[u][0]
  if u in at:
   cyc=seq[at[u]:];vol=sum(succ[a][1]for a in cyc)
   if set(cyc)==events and vol==1:
    times={cyc[0]:0}
    for a in cyc[:-1]:b,w=succ[a];times[b]=times[a]+1-w*len(cyc)
    assert not all(all(times[i,(c,r)]<times[i,(c,r+1)]for r in range(len(h)-1))for i,row in enumerate(hist)for c,h in enumerate(row)),('POTENTIAL WINDOW FRONT',hist)
   windowcache[hist]=True;return True
  done.update(seq)
 for start in events:
  u=start;w=0;length=0
  while u in succ:
   u,k=succ[u];w+=k;length+=1;assert length<len(events)
   if u[0]==start[0]and u[1][0]==start[1][0]and((u[1][1]>start[1][1]and w>=1)or(u[1][1]<start[1][1]and w<=0)):
    windowcache[hist]=True;return True
 windowcache[hist]=False;return False

def normalize(state):
 p,index,paths,flat=state;ix=(index,);hist=tuple((p+i)%2 for i in range(len(ix)))
 rows=tuple((pa,tuple(tuple(dirs[d]for d in c['h'])for c in J['histories'][pa][a]))for pa,a in zip(hist,ix))
 return rows,tuple((tuple(a),tuple(b),w)for a,b,w in paths),tuple(None if b==INF else b for b in flat)
known={normalize(s):i for i,s in enumerate(J['states'])};assert len(known)==len(J['states'])
zonecache={};maximum_nodes=0;closurecalls=0

def zone(old,new,paths,flat):
 global maximum_nodes,closurecalls
 key=(old,new,paths,flat)
 if key in zonecache:return zonecache[key]
 nodes={(0,r)for a,b,w in paths for r in(a,b)}|{(1,(c,r))for c,h in enumerate(new)for r in range(len(h))};succ={};incoming={};physical=[]
 def add(a,b,w,physical_edge):
  assert a in nodes and b in nodes and a not in succ and b not in incoming
  succ[a]=(b,w);incoming[b]=a
  if physical_edge:physical.append((a,b,w))
 for a,b,w in paths:
  if a!=b:add((0,a),(0,b),w,False)
  else:assert w==0
 _,phys=successors((old,new))
 for a,(b,w)in phys.items():
  if not(a[0]==0 and b[0]==0):add(a,b,w,True)
 groups=[];used=set();cycles=[]
 for s in sorted(nodes):
  if s in incoming:continue
  walk=[s];used.add(s);u=s;w=0
  while u in succ:
   u,z=succ[u];w+=z;assert u not in used;used.add(u);walk.append(u)
  assert s[0]==u[0]==1;groups.append((walk,w%MOD))
 for s in sorted(nodes-used):
  if s in used:continue
  walk=[];w=0;u=s
  while u not in used:
   walk.append(u);used.add(u);u,z=succ[u];w+=z
  assert u==s;cycles.append((walk,w%MOD))
 terminal=bool(cycles)
 if terminal:
  if len(cycles)!=1 or groups or cycles[0][1]!=1%MOD:zonecache[key]=set();return set()
  walk,w=cycles[0];anchor=min(x for x in walk if x[0]==1);j=walk.index(anchor);walk=walk[j:]+walk[:j];orders=[((walk,w),)]
 elif not groups:zonecache[key]={((),())};return {((),())}
 else:
  groups.sort(key=lambda z:z[0][0]);orders=((groups[0],)+rest for rest in permutations(groups[1:]))
 starts={(0,a):i for i,(a,b,w)in enumerate(paths)};owners={r:i for i,(a,b,w)in enumerate(paths)for r in(a,b)};oldvars=sorted(owners);nold=len(oldvars);assert len(flat)==nold*nold
 ns=sorted(nodes);ix={a:i for i,a in enumerate(ns)};n=len(ns);maximum_nodes=max(maximum_nodes,n);assert 3*n<INF
 answer=set()
 for order in orders:
  walk=[a for path,w in order for a in path];rank={a:i for i,a in enumerate(walk)};assert len(rank)==len(nodes)
  oldorder=[starts[a]for a in walk if a in starts]
  if paths:
   assert len(oldorder)==len(paths);cut=oldorder[0]
   if oldorder!=list(range(cut,len(paths)))+list(range(cut)):continue
  else:assert not oldorder;cut=0
  # Bounds z_u-z_v<=b are ordinary directed edges v->u of weight b.
  edges=[]
  for i,a in enumerate(oldvars):
   for j,b in enumerate(oldvars):
    value=flat[i*nold+j]
    if value is not None:
     value+=int(owners[b]<cut)-int(owners[a]<cut);assert abs(value)<=BOUND+1
     edges.append((ix[0,b],ix[0,a],value))
  for a,b,w in physical:
   diff=-w+int(rank[b]<rank[a]);edges.extend([(ix[a],ix[b],diff),(ix[b],ix[a],-diff)])
  for c,h in enumerate(new):
   for j in range(len(h)-1):edges.append((ix[1,(c,j+1)],ix[1,(c,j)],-int(rank[1,(c,j+1)]<rank[1,(c,j)])))
  # Independent Bellman-Ford closure. None is true mathematical infinity.
  closure=[];bad=False;closurecalls+=1
  for start in range(n):
   dist=[None]*n;dist[start]=0
   for round_ in range(n):
    changed=False
    for a,b,w in edges:
     if dist[a]is not None and(dist[b]is None or dist[b]>dist[a]+w):dist[b]=dist[a]+w;changed=True
    if not changed:break
   if changed:bad=True;break
   closure.append(dist)
  if bad:continue
  assert not terminal,('POTENTIAL WHOLE FRONT',key)
  nextpaths=tuple((path[0][1],path[-1][1],w)for path,w in order);newvars=sorted({r for a,b,w in nextpaths for r in(a,b)})
  mat=[]
  for a in newvars:
   for b in newvars:
    value=closure[ix[1,b]][ix[1,a]]
    mat.append(None if value is None or value>BOUND else max(value,-BOUND))
  answer.add((nextpaths,tuple(mat)))
 zonecache[key]=answer;return answer
initial=(tuple((i%2,tuple(()for c in range(N)))for i in range(K-1)),(),());assert initial in known
seen={initial};todo=deque([initial]);edges=set();attempts=0
while todo:
 state=todo.popleft();rows,paths,flat=state;p,old=rows[-1]
 for new in adj[p,old]:
  attempts+=1;hist=tuple(h for p,h in rows)+(new,)
  # Axis producer has no extra finite-window rule; certify its larger zone graph directly.
  for np,nf in zone(old,new,paths,flat):
   target=(rows[1:]+((1-p,new),),np,nf);assert target in known,('UNCOVERED STATE',target)
   edges.add((known[state],known[target],new))
   if target not in seen:seen.add(target);todo.append(target)
assert seen==set(known)
expected=set()
for u,v,j in J['edges']:
 p=seenp=J['states'][u][0];last=(p+K-2)%2;h=tuple(tuple(dirs[d]for d in c['h'])for c in J['histories'][1-last][j]);expected.add((u,v,h))
assert edges==expected
out=dict(status='PASS complete all-width frontier clock-zone exclusion',cap=CAP,full_drift=[N,0],window=K,bound=BOUND,modulus=MOD,unpruned_histories=unpruned,horizontally_matched_rows=sum(map(len,raw)),states=len(seen),edges=len(edges),attempted_extensions=attempts,independent_zone_transitions=len(zonecache),shortest_path_closures=closurecalls,largest_transition_nodes=maximum_nodes,scope='Specified full axis drift and quarter rotations, every period and width, stated cap only; no primitive quotient inference.',certificate_sha256=hashlib.sha256(P.read_bytes()).hexdigest())
Q=ROOT/'audits'/(P.name.replace('.certificate.json','_independent.json'));Q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
