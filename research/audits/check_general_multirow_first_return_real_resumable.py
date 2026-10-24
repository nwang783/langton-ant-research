"""Independent all-width zone-graph closure, unpruned histories and Bellman-Ford.
No producer modules are imported. Complete rows are filtered only by the independently derived zero transverse cut flux. Strict bounds use independent infinitesimal Bellman-Ford; finite weakening is overapproximation.
"""
from pathlib import Path
from itertools import product,permutations
from collections import Counter,deque
import json,sys,hashlib,time,ast,os,fcntl,socket
from functools import lru_cache
started=time.monotonic();D=(1j,1,-1j,-1)
ROOT=Path(__file__).resolve().parents[1];P=Path(sys.argv[1]).resolve();J=json.loads(P.read_text());par=J['parameters'];N,SLOPE=par['full_drift'];CAP=par['cap'];K=par['window'];assert K>=2; BOUND=par['bound'];SCALE=par['clock_scale'];MOD=par['modulus'];dirs=(1j,1,-1j,-1);INF=10**9
raw=[];ports={};unpruned=0
base=[SLOPE*c//N for c in range(N)]
# Recover every edge from the physical lattice and the full-drift translation.
def move(c,d):
 x=c+int(d.real);w=x//N;dc=x-w*N
 dr=base[c]+int(d.imag)-w*SLOPE-base[dc]
 assert -1<=dr<=1
 return dc,dr,w
internal=[(c,d,*move(c,d))for c in range(N)for d in dirs if move(c,d)[1]==0]
up=[(c,d,*move(c,d))for c in range(N)for d in dirs if move(c,d)[1]==1]
down=[(c,d,*move(c,d))for c in range(N)for d in dirs if move(c,d)[1]==-1]
for p in(0,1):
 locals_=[[h for m in range(CAP+1)for h in product((1,-1)if(p+c+base[c])%2==0 else(1j,-1j),repeat=m)]for c in range(N)]
 hs=[]
 unpruned+=len(locals_[0])**N
 localports=[[(Counter(h),Counter(x*(-1j if r%2==0 else 1j)for r,x in enumerate(h)))for h in choices]for choices in locals_]
 partial=[];partialports=[]
 def extend(c):
  if c==N:
   row=tuple(partial);v=tuple(partialports)
   flux=sum(v[c][1][d]for c,d,dc,dr,w in up)-sum(v[dc][0][d]for c,d,dc,dr,w in down)
   if flux==0:hs.append(row);ports[p,row]=v
   return
  for h,v in zip(locals_[c],localports[c]):
   partial.append(h);partialports.append(v)
   if all(partialports[u][1][d]==partialports[dc][0][d]for u,d,dc,dr,w in internal if max(u,dc)<=c):extend(c+1)
   partial.pop();partialports.pop()
 extend(0)
 raw.append(hs)
def sig_old(p,row):
 v=ports[p,row]
 return tuple(v[c][1][d]for c,d,dc,dr,w in up)+tuple(v[dc][0][d]for c,d,dc,dr,w in down)
def sig_new(p,row):
 v=ports[p,row]
 return tuple(v[dc][0][d]for c,d,dc,dr,w in up)+tuple(v[c][1][d]for c,d,dc,dr,w in down)
adj={}
for p in(0,1):
 ix={}
 for row in raw[1-p]:ix.setdefault(sig_new(1-p,row),[]).append(row)
 for row in raw[p]:adj[p,row]=ix.get(sig_old(p,row),[])
print('static',unpruned,list(map(len,raw)),flush=True)
def outheading(h,r):return h*(-1j if r%2==0 else 1j)
def successors(histories):
 events={(i,(c,r))for i,row in enumerate(histories)for c,h in enumerate(row)for r in range(len(h))};succ={}
 for i,row in enumerate(histories):
  for c,h in enumerate(row):
   for r,x in enumerate(h):
    d=outheading(x,r);dc,dr,w=move(c,d);to=i+dr
    if 0<=to<len(histories):
     ordinal=sum(outheading(y,j)==d for j,y in enumerate(h[:r]));arr=[j for j,y in enumerate(histories[to][dc])if y==d]
     assert ordinal<len(arr);succ[i,(c,r)]=((to,(dc,arr[ordinal])),w)
 return events,succ
def normalize(state):
 p,indices,paths,flat=state;ix=tuple(indices);assert len(ix)==K-1;hist=tuple((p-K+2+i)%2 for i in range(len(ix)))
 rows=tuple((pa,tuple(tuple(dirs[d]for d in c['h'])for c in J['histories'][pa][a]))for pa,a in zip(hist,ix))
 return rows,tuple((tuple(a),tuple(b),w)for a,b,w in paths),tuple(None if b==INF else b for b in flat)
known={normalize(s):i for i,s in enumerate(J['states'])};assert len(known)==len(J['states'])
# Independently verified actual-position first-return engine.
tree=ast.parse((ROOT/'audits/check_first_return_windows_independent.py').read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='ref');exec(compile(ast.Module(body=[fn],type_ignores=[]),'independent_ref','exec'))
@lru_cache(maxsize=300000)
def bad(p,hist):
 hs=tuple(tuple(tuple(dirs.index(h)for h in col)for col in row)for row in hist)
 return ref(hs,N,SLOPE,(p-K+2)%2)
for p in(0,1):
 assert set(raw[p])=={tuple(tuple(dirs[d]for d in c['h'])for c in row)for row in J['histories'][p]}
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
 if terminal and (len(cycles)!=1 or groups or cycles[0][1]!=1%MOD):zonecache[key]=set();return set()
 if not terminal and not groups:zonecache[key]={((),())};return {((),())}
 groups.sort(key=lambda z:z[0][0])
 oldvars=sorted({r for a,b,w in paths for r in(a,b)});nold=len(oldvars);assert len(flat)==nold*nold
 ns=sorted(nodes);ix={a:i for i,a in enumerate(ns)};n=len(ns);maximum_nodes=max(maximum_nodes,n)
 # Independent infinitesimal Bellman-Ford: weight (b,-s) represents b-s*epsilon.
 # Counts of strict arcs accumulate, unlike the producer's OR encoding.
 arcs=[]
 for i,a in enumerate(oldvars):
  for j,b in enumerate(oldvars):
   code=flat[i*nold+j]
   if code is not None:arcs.append((ix[0,b],ix[0,a],((code+1)//2,-(code%2))))
 for a,b,w in physical:
  arcs.extend([(ix[a],ix[b],(1-SCALE*w,0)),(ix[b],ix[a],(SCALE*w,-1))])
 for c,h in enumerate(new):
  for j in range(len(h)-1):arcs.append((ix[1,(c,j+1)],ix[1,(c,j)],(0,-1)))
 closure=[];closurecalls+=1
 for start in range(n):
  dist=[None]*n;dist[start]=(0,0)
  for iteration in range(n):
   changed=False
   for a,b,w in arcs:
    if dist[a] is not None:
     z=(dist[a][0]+w[0],dist[a][1]+w[1])
     if dist[b] is None or z<dist[b]:dist[b]=z;changed=True
   if not changed:break
  if changed:zonecache[key]=set();return set()
  closure.append(dist)
 assert not terminal,('POTENTIAL WHOLE FRONT',key)
 nextpaths=tuple((path[0][1],path[-1][1],w)for path,w in groups)
 newvars=sorted({r for a,b,w in nextpaths for r in(a,b)})
 mat=[]
 for a in newvars:
  for b in newvars:
   value=closure[ix[1,b]][ix[1,a]]
   code=None if value is None else 2*value[0]-int(value[1]<0)
   mat.append(None if code is None or code>2*BOUND else max(code,-2*BOUND))
 answer={(nextpaths,tuple(mat))};zonecache[key]=answer;return answer
initial=(tuple(((i-K+2)%2,tuple(()for c in range(N)))for i in range(K-1)),(),());assert initial in known
# A closed candidate graph may be checked source-by-source: order is irrelevant.
# Every possible new row is still enumerated and its exact independent transition tested.
# Separately verify every listed state is reachable from the unique initial state.
states=[None]*len(known)
for state,i in known.items():states[i]=state
expected=[set()for _ in states]
for u,v,j in J['edges']:
 p=J['states'][u][0];row=tuple(tuple(dirs[d]for d in c['h'])for c in J['histories'][1-p][j]);expected[u].add((v,row))
reach={known[initial]};queue=deque(reach)
while queue:
 for v,row in expected[queue.popleft()]:
  if v not in reach:reach.add(v);queue.append(v)
assert reach==set(range(len(states)))
codehash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
refhash=hashlib.sha256((ROOT/'audits/check_first_return_windows_independent.py').read_bytes()).hexdigest()
certhash=hashlib.sha256(P.read_bytes()).hexdigest()
cpdir=ROOT/'audits/replay_checkpoints';cpdir.mkdir(exist_ok=True)
stem=P.name.replace('.certificate.json','')+'_sources_'+codehash[:12]
checkpoint=cpdir/(stem+'.json');lockfile=cpdir/(stem+'.lock')
lock=lockfile.open('a+');fcntl.flock(lock.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
lock.seek(0);lock.truncate();lock.write(json.dumps(dict(pid=os.getpid(),host=socket.gethostname(),start_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),code_sha256=codehash)));lock.flush();os.fsync(lock.fileno())
bind=dict(certificate_sha256=certhash,checker_sha256=codehash,physical_reference_sha256=refhash)
progress=dict(bindings=bind,next_source=0,attempted_extensions=0,validated_edges=0,shortest_path_closures=0,largest_transition_nodes=0,elapsed_seconds=0.0,chain_sha256=hashlib.sha256(json.dumps(bind,sort_keys=True).encode()).hexdigest())
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
if checkpoint.exists():
 saved=json.loads(checkpoint.read_text());checksum=saved.pop('checkpoint_sha256');assert digest(saved)==checksum
 assert saved['bindings']==bind and 0<=saved['next_source']<=len(states)
 assert saved['validated_edges']==sum(len(e)for e in expected[:saved['next_source']])
 progress=saved
print('RESUMABLE',str(checkpoint),'starting source',progress['next_source'],'of',len(states),flush=True)
lasttime=time.monotonic()
for u in range(progress['next_source'],len(states)):
 state=states[u];rows,paths,flat=state;p,old=rows[-1];actual=set();attempts=0;beforeclosures=closurecalls
 for new in adj[p,old]:
  attempts+=1;hist=tuple(h for p,h in rows)+(new,)
  if bad(p,hist):continue
  if len(zonecache)>50000:zonecache.clear()
  for np,nf in zone(old,new,paths,flat):
   target=(rows[1:]+((1-p,new),),np,nf);assert target in known,('UNCOVERED STATE',u,target)
   actual.add((known[target],new))
 assert actual==expected[u],('OUTGOING SET MISMATCH',u,len(actual),len(expected[u]))
 progress['next_source']=u+1;progress['attempted_extensions']+=attempts;progress['validated_edges']+=len(actual)
 progress['shortest_path_closures']+=closurecalls-beforeclosures;progress['largest_transition_nodes']=max(progress['largest_transition_nodes'],maximum_nodes)
 now=time.monotonic();progress['elapsed_seconds']+=now-lasttime;lasttime=now
 record=dict(source=u,extensions=attempts,outgoing_edges=len(actual),outgoing_digest=digest(sorted((v,tuple(tuple(dirs.index(d)for d in c)for c in row))for v,row in actual)))
 progress['chain_sha256']=hashlib.sha256((progress['chain_sha256']+json.dumps(record,sort_keys=True)).encode()).hexdigest()
 saved={**progress,'checkpoint_sha256':digest(progress)};tmp=checkpoint.with_suffix('.tmp')
 with tmp.open('w')as f:f.write(json.dumps(saved,indent=2)+'\n');f.flush();os.fsync(f.fileno())
 os.replace(tmp,checkpoint)
 if(u+1)%100==0 or u+1==len(states):print('sources',u+1,'/',len(states),'extensions',progress['attempted_extensions'],'edges',progress['validated_edges'],flush=True)
assert progress['next_source']==len(states)
out=dict(status='PASS independent complete zero-flux multirow fixed-real frontier closure with durable per-source validation',seconds=progress['elapsed_seconds'],cap=CAP,full_drift=[N,SLOPE],window=K,clock_scale=SCALE,bound=BOUND,modulus=MOD,unpruned_histories=unpruned,internally_matched_rows=sum(map(len,raw)),states=len(states),edges=progress['validated_edges'],attempted_extensions=progress['attempted_extensions'],shortest_path_closures=progress['shortest_path_closures'],largest_transition_nodes=progress['largest_transition_nodes'],bindings=bind,checkpoint=str(checkpoint),completed_source_chain=progress['chain_sha256'],scope='Every listed source has its COMPLETE possible outgoing set independently reconstructed; initial reachability is separately verified. Same physical first-return and Bellman-Ford engines as original checker. Specified full drift and cap only; no primitive quotient or general capture inference.')
Q=ROOT/'audits'/(P.name.replace('.certificate.json','_resumable_independent.json'));Q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
