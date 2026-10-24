"""Discovery solver: exact local read constraints, arbitrary image count and fuel cap.
SAT is only a finite prefix. UNKNOWN is never a mathematical exclusion.
"""
import json,pathlib,sys,collections,time,functools
from search_complementary_roots import D
HERE=pathlib.Path(__file__).resolve().parent
@functools.lru_cache(None)
def trace(w):
 x=y=h=0;reads=[]
 for c in w:
  reads.append((x,y,h,c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return reads,(x,y,h)
def seed(w):
 last={};out=[]
 for x,y,h,c in trace(w)[0]:
  p=x,y
  if last.get(p)==c:return None
  if p not in last and c=='L':out.append(p)
  last[p]=c
 return out
def rotate(x,y,h):
 for _ in range(h):x,y=y,-x
 return x,y
def step(q,c):
 if q==0:return 1 if c=='R'else 4
 if q in(1,3):return -1 if c=='R'else q+1
 return q-1 if c=='R'else -1
def image(states,tr):
 out=0
 for q in range(5):
  if states>>q&1 and tr[q]>=0:out|=1<<tr[q]
 return out
class Model:
 def __init__(self,k,a,opts):self.k=k;self.a=tuple(a);self.opts=opts
 def build(self,coarse,fixed):
  N=len(coarse);cells=collections.defaultdict(dict);domains=[]
  for i,(x,y,h,c)in enumerate(trace(coarse)[0]):
   ws=self.opts[c];domains.append(1<<ws.index(fixed[i])if i<len(fixed)else(1<<len(ws))-1)
   for j,w in enumerate(ws):
    by=collections.defaultdict(str)
    for X,Y,H,z in trace(w)[0]:
     X,Y=rotate(X,Y,h);p=self.a[0]*x-self.a[1]*y+X,self.a[1]*x+self.a[0]*y+Y;by[p]+=z
    for p,s in by.items():cells[p].setdefault(i,['']*len(ws))[j]=s
  constraints=[];adj=[[]for _ in range(N)]
  for p,vv in cells.items():
   entries=[]
   for i,ss in sorted(vv.items()):
    transitions=[]
    for s in ss:
     tr=[]
     for state in range(5):
      q=state
      for c in s:
       q=step(q,c)
       if q<0:break
      tr.append(q)
     transitions.append(tr)
    entries.append((i,transitions))
   index=len(constraints);constraints.append((p,entries))
   for i,_ in entries:adj[i].append(index)
  return domains,constraints,adj
 def solve(self,coarse,fixed,nodecap=100000,fuelcap=None):
  dom,con,adj=self.build(coarse,fixed);nodes=0;unknown=False;maxlb=0;start=time.time()
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
    end=31
    if fuelcap is not None and total==fuelcap and not lower:end=7
    B=[0]*(len(entries)+1);B[-1]=end
    for z in range(len(entries)-1,-1,-1):
     i,tt=entries[z];allowed=0
     for q in range(5):
      if any(d[i]>>j&1 and tt[j][q]>=0 and B[z+1]>>tt[j][q]&1 for j in range(len(tt))):allowed|=1<<q
     B[z]=allowed
    for z,(i,tt)in enumerate(entries):
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
   candidates=[i for i,b in enumerate(d)if b.bit_count()>1]
   if not candidates:return d
   i=max(candidates,key=lambda z:(len(adj[z]),-d[z].bit_count(),-z))
   choices=[j for j in range(len(self.opts[coarse[i]]))if d[i]>>j&1]
   # This is only search ordering, never a pruning rule.
   choices.sort(key=lambda j:self.opts[coarse[i]][j].count('L'))
   for j in choices:
    e=d.copy();e[i]=1<<j;ans=dfs(e)
    if ans is not None:return ans
    if unknown:return None
   return None
  ans=dfs(dom)
  out=dict(status='SAT'if ans is not None else'UNKNOWN'if unknown else'UNSAT',nodes=nodes,variables=len(dom),constraints=len(con),fuelcap=fuelcap,max_node_fuel_lower_bound=maxlb,seconds=time.time()-start)
  if ans is not None:
   choice=[self.opts[c][(b&-b).bit_length()-1]for c,b in zip(coarse,ans)];word=''.join(choice);black=seed(word)
   assert word[:len(coarse)]==coarse and black is not None
   if fuelcap is not None:assert len(black)<=fuelcap
   finepos=[(x,y,h)for x,y,h,c in trace(word)[0]]+[trace(word)[1]]
   for n,(x,y,h,c)in enumerate(trace(coarse)[0]):assert finepos[self.k*n]==(self.a[0]*x-self.a[1]*y,self.a[1]*x+self.a[0]*y,h)
   out.update(choices=choice,word=word,seed=black,seed_size=len(black))
  return out
if __name__=='__main__':
 k=9;a=(3,0);nodecap=int(sys.argv[1])if len(sys.argv)>1 else 10000
 r=next(z for z in json.load(open(HERE/f'free_inflations_k{k}.json'))['results']if z['scale']==list(a));M=Model(k,a,r['images']);results=[]
 for c in'RL':
  for w in M.opts[c]:
   if w[0]!=c:continue
   coarse=w;fixed=[w]
   for level in range(2,5):
    ans=M.solve(coarse,fixed,nodecap=nodecap);ans.update(root=w,level=level);results.append(ans)
    print('RESULT',w,level,ans['status'],ans['nodes'],ans.get('seed_size'),round(ans['seconds'],2),flush=True)
    if ans['status']!='SAT':break
    coarse=ans['word'];fixed=ans['choices']
   (HERE/'free_inflation_k9_generic_csp.json').write_text(json.dumps(results,indent=2))
