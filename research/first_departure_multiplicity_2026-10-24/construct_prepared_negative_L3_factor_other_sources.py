"""Constructive router for ONE fixed nine-cell late-L3 target.
Not a front/period/radius scan. Fresh connector paths are chosen around the
current finite obstacle hull; failure is a router restriction, not a theorem.
All board colors and known middle ranks are retained. Prepared input explicit.
"""
from pathlib import Path
from collections import deque,Counter
from heapq import heappush,heappop
import json,copy,time
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
base=Path(__file__).parent;j=json.loads((base/'check_fixed_LL_L3_supplier_controls.json').read_text());ob=next(r for r in j['rows']if r['kind']=='negative')
import ast
hs={ast.literal_eval(p):h for p,h in ob['histories'].items()};K=set(hs)
blocks=[[ (tuple(p),r)for p,r in x['events']]for x in ob['complete_literal_channels']]
def turn(h,L):return H[(H.index(h)+(-1 if L else 1))%4]
def step(s,L=None):
 p,h=s['head'];inside=p in K
 if inside:
  r=s['count'].get(p,0)
  if r>=len(hs[p])or hs[p][r]!=h:return False
  expect=bool(r%2)
  if(p in s['black'])!=expect:return False
  if L is not None and L!=expect:return False
  L=expect
 else:
  r=s['count'].get(p,0)
  if r>=4:return False
  if not r:
   if L is None:raise RuntimeError('fresh choice required')
   if L:s['seed'].add(p);s['black'].add(p)
  else:
   actual=p in s['black']
   if L is not None and L!=actual:return False
   L=actual
 s['count'][p]=r+1
 if p in s['black']:s['black'].remove(p)
 else:s['black'].add(p)
 co=turn(h,L);q=p[0]+V[co][0],p[1]+V[co][1]
 s['trace'].append(dict(cell=p,incoming=h,turn='L'if L else'R',rank=r,known=inside))
 s['head']=q,co
 return True

def forced(s):
 """Run every forced known/previously read cell until a genuinely fresh cell."""
 seen=0
 while s['head'][0]in K or s['count'].get(s['head'][0],0):
  if all(s['count'].get(p,0)==len(h)for p,h in hs.items()):return True
  if not step(s):return False
  seen+=1
  if seen>10000:return False
 return True

def available(s,block):
 c=s['count'].copy()
 for p,r in block:
  if c.get(p,0)!=r:return False
  c[p]=r+1
 return True

def reverse_stub(s,target):
 p,h=target;stub=[];seen=set()
 while True:
  q=p[0]-V[h][0],p[1]-V[h][1]
  if q in K:return None
  if not s['count'].get(q,0):return q,h,list(reversed(stub))
  if q in seen or s['count'][q]>=4:return None
  seen.add(q);L=q in s['black'];hi=H[(H.index(h)+(1 if L else-1))%4]
  stub.append((q,hi));p,h=q,hi

def fresh_path(s,goal,outhead,bias):
 start=s['head'];q0,h0=start;used={p for p,c in s['count'].items()if c};obstacles=K|used
 assert q0 not in obstacles and goal not in obstacles
 pts=obstacles|{q0,goal};xmin=min(p[0]for p in pts)-3;xmax=max(p[0]for p in pts)+3;ymin=min(p[1]for p in pts)-3;ymax=max(p[1]for p in pts)+3
 serial=0;Q=[];heappush(Q,(abs(q0[0]-goal[0])+abs(q0[1]-goal[1]),0,serial,start,[start],frozenset([q0])))
 best={start:0};expand=0
 while Q:
  _,g,_,(p,h),path,vis=heappop(Q)
  if p==goal and turn(h,False)==outhead or p==goal and turn(h,True)==outhead:return path
  expand+=1
  if expand>30000:return None
  for L in ([False,True]if bias==0 else[True,False]):
   co=turn(h,L);v=V[co];q=p[0]+v[0],p[1]+v[1]
   if q in obstacles or q in vis or not(xmin<=q[0]<=xmax and ymin<=q[1]<=ymax):continue
   st=q,co;ng=g+1
   if best.get(st,10**9)<ng:continue
   best[st]=ng;serial+=1
   # Tie bias is only a literal route choice, never a theorem cutoff.
   heappush(Q,(ng+abs(q[0]-goal[0])+abs(q[1]-goal[1]),ng,serial,st,path+[st],vis|{q}))
 return None

def connect(s,target,bias):
 b=reverse_stub(s,target)
 if b is None:return None
 goal,oh,stub=b;p=fresh_path(s,goal,oh,bias)
 if p is None:return None
 z=copy.deepcopy(s)
 for i,(cell,hi)in enumerate(p):
  assert z['head']==(cell,hi)
  co=p[i+1][1]if i+1<len(p)else oh
  L=turn(hi,True)==co
  if not step(z,L):return None
 for cell,hi in stub:
  if z['head']!=(cell,hi)or not step(z):return None
 if z['head']!=target:return None
 if not forced(z):return None
 z['routes'].append(dict(target=target,fresh_cells=len(p),used_stub=len(stub),bias=bias))
 return z

start_time=time.time();nodes=0;fail=Counter();bestdone=0

def dfs(s):
 global nodes,bestdone
 nodes+=1
 done=sum(min(s['count'].get(p,0),len(h))for p,h in hs.items())
 if done>bestdone:
  bestdone=done;print('PROGRESS',done,'/',sum(map(len,hs.values())),'reads',len(s['trace']),'nodes',nodes,flush=True)
 if done==sum(map(len,hs.values())):return s
 if nodes>5000:fail['router_node_budget']+=1;return None
 av=[]
 for block in blocks:
  p,r=block[0]
  if s['count'].get(p,0)>r or not available(s,block):continue
  hi=hs[p][r];q=s['head'][0];av.append((abs(q[0]-p[0])+abs(q[1]-p[1]),p,r,hi))
 for _,p,r,hi in sorted(av):
  for bias in[0,1]:
   z=connect(s,(p,hi),bias)
   if z is None:fail['no_connector_or_forced_conflict']+=1;continue
   sol=dfs(z)
   if sol is not None:return sol
 return None

# Remaining exact rank-DAG source channels, not arbitrary seed/head scans.
sol=None;attempts=[];initial=None
for p,hi in [((0,2),'S'),((2,0),'N'),((2,1),'W')]:
 nodes=0;bestdone=0;fail=Counter();initial=(p,hi)
 s=dict(head=initial,black=set(),seed=set(),count={},trace=[],routes=[])
 assert forced(s)
 sol=dfs(s)
 attempts.append(dict(initial=initial,success=sol is not None,nodes=nodes,best_known_reads=bestdone,failures=dict(fail)))
 print('ATTEMPT',attempts[-1],flush=True)
 if sol:break
obj=dict(scope=__doc__,success=sol is not None,all_attempts=attempts,planner_nodes=nodes,best_known_reads=bestdone,failures=dict(fail),seconds=time.time()-start_time)
if sol:
 # Full independent-style literal replay from explicit seed and initial pose.
 B=set(sol['seed']);p,h=initial;hist={};word=''
 for e in sol['trace']:
  L=p in B;assert e['cell']==p and e['incoming']==h and e['turn']==('L'if L else'R')
  hist.setdefault(p,[]).append(h);word+='L'if L else'R'
  if L:B.remove(p)
  else:B.add(p)
  h=turn(h,L);p=p[0]+V[h][0],p[1]+V[h][1]
 assert (p,h)==sol['head'] and B==sol['black']
 assert all(''.join(hist[p])==q for p,q in hs.items())and max(map(len,hist.values()))<=4
 obj.update(word=word,initial_pose=[*initial[0],initial[1]],initial_black=sorted(sol['seed']),final_pose=[*p,h],final_black=sorted(B),reads=len(word),max_multiplicity=max(map(len,hist.values())),known_histories={str(p):''.join(hist[p])for p in K},trace=sol['trace'],routes=sol['routes'])
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('RESULT',{k:v for k,v in obj.items()if k not in['trace','word','routes','initial_black','final_black','known_histories']},flush=True)
