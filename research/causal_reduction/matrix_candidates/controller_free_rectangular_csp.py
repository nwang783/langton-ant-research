"""Discovery CSP for occurrence-dependent rectangular pure ant inflation.
Every macro occurrence may choose a different image. No controller is imposed.
SAT is only a finite prefix; UNKNOWN is never exclusion. Greedy deeper UNSAT
excludes only the chosen prefix, not its root or alternate earlier refinements.
"""
import collections, functools, itertools, json, pathlib, sys, time
D=((0,1),(1,0),(0,-1),(-1,0))
HERE=pathlib.Path(__file__).resolve().parent
@functools.lru_cache(None)
def trace(w,h0):
 x=y=0;h=h0;reads=[]
 for c in w:
  reads.append((x,y,h,c));h=(h+(1 if c=='R' else 3))%4
  dx,dy=D[h];x+=dx;y+=dy
 return tuple(reads),(x,y,h)
def seed(w,h0):
 last={};out=[]
 for x,y,h,c in trace(w,h0)[0]:
  p=x,y
  if last.get(p)==c:return None
  if p not in last and c=='L':out.append(p)
  last[p]=c
 return out
@functools.lru_cache(None)
def step(q,c):
 if q==0:return 1 if c=='R' else 4
 if q in (1,3):return -1 if c=='R' else q+1
 return q-1 if c=='R' else -1
@functools.lru_cache(None)
def transition(s):
 out=[]
 for start in range(5):
  q=start
  for c in s:
   q=step(q,c)
   if q<0:break
  out.append(q)
 return tuple(out)
@functools.lru_cache(None)
def image(states,tr):
 out=0
 for q in range(5):
  if states>>q&1 and tr[q]>=0:out|=1<<tr[q]
 return out
class Model:
 def __init__(self,k,a,b):
  self.k,self.a,self.b=k,a,b;self.opts={}
  for h in range(4):
   for c in 'RL':
    hh=(h+(1 if c=='R' else 3))%4;dx,dy=D[hh];target=(a*dx,b*dy,hh)
    self.opts[h,c]=[''.join(w) for w in itertools.product('RL',repeat=k) if trace(''.join(w),h)[1]==target and seed(''.join(w),h) is not None]
 def build(self,coarse,h0,fixed):
  N=len(coarse);cells=collections.defaultdict(dict);domains=[];options=[]
  for i,(x,y,h,c) in enumerate(trace(coarse,h0)[0]):
   ws=self.opts[h,c];options.append(ws)
   domains.append(1<<ws.index(fixed[i]) if i<len(fixed) else (1<<len(ws))-1)
   for j,w in enumerate(ws):
    by=collections.defaultdict(str)
    for X,Y,H,z in trace(w,h)[0]:by[self.a*x+X,self.b*y+Y]+=z
    for p,s in by.items():cells[p].setdefault(i,['']*len(ws))[j]=s
  constraints=[];adj=[[] for _ in range(N)]
  for p,vv in cells.items():
   entries=[(i,[transition(s) for s in ss]) for i,ss in sorted(vv.items())]
   ci=len(constraints);constraints.append((p,entries))
   for i,_ in entries:adj[i].append(ci)
  return domains,constraints,adj,options
 def solve(self,coarse,h0,fixed,nodecap=10000,fuelcap=None):
  start=time.time();dom,con,adj,options=self.build(coarse,h0,fixed);nodes=0;unknown=False;maxlb=0
  def propagate(d):
   nonlocal maxlb
   queue=collections.deque(range(len(con)));queued=set(queue);cost=[0]*len(con);total=0
   while queue:
    ci=queue.popleft();queued.discard(ci);p,entries=con[ci];F=[1]
    for i,tt in entries:
     nxt=0
     for j in range(len(tt)):
      if d[i]>>j&1:nxt|=image(F[-1],tt[j])
     if not nxt:return False
     F.append(nxt)
    lower=int(not(F[-1]&7))
    if lower>cost[ci]:
     total+=lower-cost[ci];cost[ci]=lower;maxlb=max(maxlb,total)
     if fuelcap is not None:
      if total>fuelcap:return False
      if total==fuelcap:
       for z in range(len(con)):
        if z not in queued:queue.append(z);queued.add(z)
    B=[0]*(len(entries)+1);B[-1]=7 if fuelcap is not None and total==fuelcap and not lower else 31
    for z in range(len(entries)-1,-1,-1):
     i,tt=entries[z];allowed=0
     for q in range(5):
      if any(d[i]>>j&1 and tt[j][q]>=0 and B[z+1]>>tt[j][q]&1 for j in range(len(tt))):allowed|=1<<q
     B[z]=allowed
    for z,(i,tt) in enumerate(entries):
     good=0
     for j in range(len(tt)):
      if d[i]>>j&1 and image(F[z],tt[j])&B[z+1]:good|=1<<j
     if not good:return False
     if good!=d[i]:
      d[i]=good
      for z in adj[i]:
       if z not in queued:queue.append(z);queued.add(z)
   return True
  def dfs(d):
   nonlocal nodes,unknown
   nodes+=1
   if nodes>nodecap:unknown=True;return None
   if not propagate(d):return None
   cs=[i for i,v in enumerate(d) if v.bit_count()>1]
   if not cs:return d
   i=max(cs,key=lambda z:(len(adj[z]),-d[z].bit_count(),-z))
   js=[j for j in range(len(options[i])) if d[i]>>j&1]
   js.sort(key=lambda j:options[i][j].count('L'))
   for j in js:
    e=d.copy();e[i]=1<<j;ans=dfs(e)
    if ans is not None:return ans
    if unknown:return None
   return None
  ans=dfs(dom)
  out=dict(status='SAT' if ans is not None else 'UNKNOWN' if unknown else 'UNSAT',nodes=nodes,variables=len(dom),constraints=len(con),fuelcap=fuelcap,max_node_fuel_lower_bound=maxlb,seconds=time.time()-start)
  if ans is not None:
   choice=[ws[(v&-v).bit_length()-1] for ws,v in zip(options,ans)];word=''.join(choice);black=seed(word,h0)
   assert word[:len(coarse)]==coarse and black is not None
   if fuelcap is not None:assert len(black)<=fuelcap
   finepos=[(x,y,h) for x,y,h,c in trace(word,h0)[0]]+[trace(word,h0)[1]]
   for n,(x,y,h,c) in enumerate(trace(coarse,h0)[0]):assert finepos[self.k*n]==(self.a*x,self.b*y,h)
   out.update(choices=choice,word=word,seed=black,seed_size=len(black))
  return out
if __name__=='__main__':
 nodecap=int(sys.argv[1]) if len(sys.argv)>1 else 1000
 maxlevel=int(sys.argv[2]) if len(sys.argv)>2 else 2
 M=Model(13,3,5);results=[]
 print('DOMAINS',{str(z):len(w) for z,w in M.opts.items()},flush=True)
 for h0 in (0,1):
  for c in 'RL':
   for w in M.opts[h0,c]:
    if w[0]!=c:continue
    coarse=w;fixed=[w]
    for level in range(2,maxlevel+1):
     ans=M.solve(coarse,h0,fixed,nodecap=nodecap);ans.update(root=w,heading=h0,level=level,scope='chosen-prefix' if level>2 else 'entire-root')
     results.append(ans)
     print('RESULT',h0,w,level,ans['status'],ans['nodes'],ans.get('seed_size'),round(ans['seconds'],3),flush=True)
     (HERE/'controller_free_rectangular_k13.json').write_text(json.dumps(results,indent=2))
     if ans['status']!='SAT':break
     coarse=ans['word'];fixed=ans['choices']
