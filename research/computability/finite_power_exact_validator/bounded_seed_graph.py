"""Exact bounded-mass finite-support XOR solver, given decidable bounded neighbors.
The all-level ant -> automatic graph constructor is NOT implemented here.
"""
from collections import deque
import itertools,json,pathlib,random,time
HERE=pathlib.Path(__file__).parent

def solve(neighbors,one_edges,pins,M,one_edges_infinite=False):
 assert M>=0
 if one_edges_infinite:return dict(possible=False,reason='infinitely many one edges')
 C={p for e in one_edges for p in e}|{p for p,c in pins}
 if M==0:
  good=not one_edges and all(c==0 for p,c in pins)
  return dict(possible=good,board=[] if good else None,reason='zero mass')
 small=[];known={};large=set();probes=0
 for c in sorted(C):
  if c in known:continue
  seen={c};queue=deque([c]);too_large=False
  while queue and not too_large:
   u=queue.popleft();probes+=1
   for v in neighbors(u):
    if v in seen:continue
    seen.add(v)
    if len(seen)>M:too_large=True;break
    queue.append(v)
  if too_large:large.add(c)
  else:
   j=len(small);small.append(seen)
   for v in seen:known[v]=j
 const=len(small);weights=[len(s) for s in small]+[0]
 where=lambda p:known[p] if p in known else const
 adj=[[] for _ in weights]
 for u,v in one_edges:
  a,b=where(u),where(v);adj[a].append((b,1));adj[b].append((a,1))
 for u,b in pins:
  a=where(u);adj[a].append((const,b));adj[const].append((a,b))
 parity={};values={};cost=0
 for start in range(len(weights)):
  if start in parity:continue
  parity[start]=0;queue=[start];component=[]
  for u in queue:
   component.append(u)
   for v,b in adj[u]:
    val=parity[u]^b
    if v in parity:
     if parity[v]!=val:return dict(possible=False,reason='inconsistent finite XOR system',probes=probes)
    else:parity[v]=val;queue.append(v)
  if const in component:flip=parity[const]
  else:
   costs=[sum(weights[u] for u in component if parity[u]^flip) for flip in (0,1)]
   flip=int(costs[1]<costs[0])
  for u in component:values[u]=parity[u]^flip
  cost+=sum(weights[u] for u in component if values[u])
 if cost>M:return dict(possible=False,reason='minimum cost exceeds bound',minimum_truncated_cost=cost,probes=probes)
 B=set().union(*(small[j] for j in range(len(small)) if values[j]))
 assert len(B)==cost
 assert all(v in B for u in B for v in neighbors(u))
 assert all((u in B)^(v in B) for u,v in one_edges)
 assert all(int(u in B)==b for u,b in pins)
 return dict(possible=True,board=sorted(B),mass=cost,small_components=len(small),
  large_critical_vertices=len(large),probes=probes)

def brute(points,zero_edges,one_edges,pins,M):
 best=None
 for k in range(M+1):
  for B0 in itertools.combinations(points,k):
   B=set(B0)
   if any((u in B)^(v in B) for u,v in zero_edges):continue
   if any(not((u in B)^(v in B)) for u,v in one_edges):continue
   if any(int(u in B)!=b for u,b in pins):continue
   return B
 return None

def main():
 start=time.monotonic();rng=random.Random(202610230400);checks=0;success=0;maxprobes=0
 points=list(itertools.product(range(3),repeat=2));pairs=list(itertools.combinations_with_replacement(points,2))
 for case in range(300):
  zero=[e for e in pairs if rng.randrange(18)==0]
  ones=[e for e in pairs if rng.randrange(27)==0]
  pins=[(rng.choice(points),rng.randrange(2)) for _ in range(rng.randrange(4))]
  adj={p:set() for p in points}
  for u,v in zero:adj[u].add(v);adj[v].add(u)
  for M in range(7):
   got=solve(lambda p:adj.get(p,()),ones,pins,M);want=brute(points,zero,ones,pins,M)
   assert got['possible']==(want is not None),(case,M,got,want)
   if want is not None:
    assert got.get('mass',0)==len(want),(case,M,got,want);success+=1
   maxprobes=max(maxprobes,got.get('probes',0));checks+=1
 # Infinite components are not explored to exhaustion. Remote location does
 # not affect the proof or solver, and an unconstrained component is omitted.
 big=10**100
 def ray(p):
  x,y=p
  if y==0 and x>=0:return [(x+1,0)]+([(x-1,0)] if x>0 else [])
  if y==big and big<=x<=big+2:return [(q,big) for q in (x-1,x+1) if big<=q<=big+2]
  return []
 cases=[]
 for M in range(1,10):
  # A black pin on the ray is impossible at any finite tested bound.
  a=solve(ray,[],[((0,0),1)],M);assert not a['possible'];cases.append(a)
  # Opposite colors force the remote 3-cell component black, ray white.
  b=solve(ray,[((0,0),(big,big))],[],M);assert b['possible']==(M>=3)
  if M>=3:assert b['mass']==3
  cases.append(b)
 out=dict(random_graphs=300,complete_brute_comparisons=checks,successful_cases=success,
  maximum_neighbor_probes=maxprobes,infinite_remote_controls=len(cases),records=cases,
  scope='Exact bounded-mass graph solver tested; all-level ant automatic graph compilation not implemented.',seconds=time.monotonic()-start)
 (HERE/'bounded_seed_graph.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
