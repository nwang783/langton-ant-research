"""Exact per-cell regular constraints for free geometric inflation refinement.
The coarse word is fixed; choices of fine macro are otherwise independent.
Capped solver outcomes remain UNKNOWN. A SAT prefix is not an infinite orbit.
"""
import json,pathlib,sys,collections,itertools,time
from search_complementary_roots import D,spec
HERE=pathlib.Path(__file__).resolve().parent
A=(2,3);K=7
OPTS={'R':['RLRLLRR','RLLRRLR','LRRLRLR'],'L':['RRRLRLR','LLRLLRR','LLLRRLR']}

def trace(w):
 x=y=h=0;reads=[]
 for c in w:
  reads.append((x,y,h,c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return reads,(x,y,h)

def feasible(w):
 last={}
 for x,y,h,c in trace(w)[0]:
  if last.get((x,y))==c:return False
  last[x,y]=c
 return True

def prefixes(n):
 out=[]
 def rec(choices,w):
  i=len(choices)
  if i==n:out.append((choices,w));return
  opts=[v for c in'RL'for v in OPTS[c]if v[0]==c]if i==0 else OPTS[w[i]]
  for v in opts:
   ww=w+v
   if feasible(ww):rec(choices+[v],ww)
 rec([],'');return out

def rotate(x,y,h):
 for _ in range(h):x,y=y,-x
 return x,y

def build(coarse,fixed):
 N=len(coarse);reads,_=trace(coarse);cells=collections.defaultdict(dict);domains=[]
 for i,(x,y,h,c)in enumerate(reads):
  ws=OPTS[c];domains.append((1<<ws.index(fixed[i]))if i<len(fixed)else 7)
  for j,w in enumerate(ws):
   by=collections.defaultdict(str)
   for X,Y,H,z in trace(w)[0]:
    X,Y=rotate(X,Y,h);p=A[0]*x-A[1]*y+X,A[1]*x+A[0]*y+Y;by[p]+=z
   for p,s in by.items():cells[p].setdefault(i,['','',''])[j]=s
 constraints=[];adj=[[]for _ in range(N)]
 for p,vv in cells.items():
  if len(vv)<2:continue
  entries=[]
  for i,ss in sorted(vv.items()):
   transitions=[]
   for s in ss:
    tr=[]
    for state in range(3):
     q=state
     for c in s:
      z=1 if c=='R'else 2
      if q==z:q=-1;break
      q=z
     tr.append(q)
    transitions.append(tr)
   entries.append((i,transitions))
  index=len(constraints);constraints.append((p,entries))
  for i,_ in entries:adj[i].append(index)
 return domains,constraints,adj

def image(states,tr):
 out=0
 for q in range(3):
  if states>>q&1 and tr[q]>=0:out|=1<<tr[q]
 return out

def propagate(dom,constraints,adj,queue=None):
 queue=collections.deque(range(len(constraints))if queue is None else queue);queued=set(queue)
 while queue:
  ci=queue.popleft();queued.discard(ci);p,entries=constraints[ci];F=[1]
  for i,tt in entries:
   nxt=0
   for j in range(3):
    if dom[i]>>j&1:nxt|=image(F[-1],tt[j])
   if not nxt:return False
   F.append(nxt)
  B=[0]*(len(entries)+1);B[-1]=7
  for z in range(len(entries)-1,-1,-1):
   i,tt=entries[z];allowed=0
   for q in range(3):
    if any(dom[i]>>j&1 and tt[j][q]>=0 and B[z+1]>>tt[j][q]&1 for j in range(3)):allowed|=1<<q
   B[z]=allowed
  for z,(i,tt)in enumerate(entries):
   good=0
   for j in range(3):
    if dom[i]>>j&1 and image(F[z],tt[j])&B[z+1]:good|=1<<j
   if not good:return False
   if good!=dom[i]:
    dom[i]=good
    for c in adj[i]:
     if c not in queued:queue.append(c);queued.add(c)
 return True

def solve(coarse,fixed,nodecap=100000):
 dom,con,adj=build(coarse,fixed);nodes=0;unknown=False
 def dfs(d,queue=None):
  nonlocal nodes,unknown
  nodes+=1
  if nodes>nodecap:unknown=True;return None
  if not propagate(d,con,adj,queue):return None
  candidates=[i for i,b in enumerate(d)if b.bit_count()>1 and adj[i]]
  if not candidates:return d
  i=max(candidates,key=lambda z:(len(adj[z]),-d[z].bit_count(),-z))
  for j in range(3):
   if d[i]>>j&1:
    e=d.copy();e[i]=1<<j;ans=dfs(e,adj[i])
    if ans is not None:return ans
    if unknown:return None
  return None
 ans=dfs(dom)
 out=dict(status='SAT'if ans is not None else'UNKNOWN'if unknown else'UNSAT',nodes=nodes,variables=len(dom),constraints=len(con))
 if ans is not None:
  choice=[OPTS[c][(b&-b).bit_length()-1]for c,b in zip(coarse,ans)];word=''.join(choice)
  assert word[:len(coarse)]==coarse and feasible(word)
  finepos=[(x,y,h)for x,y,h,c in trace(word)[0]]+[trace(word)[1]]
  for n,(x,y,h,c)in enumerate(trace(coarse)[0]):assert finepos[K*n]==(A[0]*x-A[1]*y,A[1]*x+A[0]*y,h)
  out.update(choices=choice,word=word)
 return out

if __name__=='__main__':
 start=time.time();ps=prefixes(K);results=[];tot=collections.Counter();print('PREFIXES',len(ps),flush=True)
 for j,(fixed,w)in enumerate(ps):
  r=solve(w,fixed);r.update(prefix=j,fixed=fixed,coarse=w);results.append(r);tot[r['status']]+=1
  if j%20==0 or r['status']!='UNSAT':print('RESULT',j,r['status'],r['nodes'],dict(tot),flush=True)
  if r['status']=='SAT':break
 out=dict(scale=A,k=K,prefix_count=len(ps),tested=len(results),counts=dict(tot),results=results,seconds=time.time()-start)
 (HERE/'free_inflation_k7_csp.json').write_text(json.dumps(out,indent=2));print('DONE',out['tested'],dict(tot),out['seconds'],flush=True)
