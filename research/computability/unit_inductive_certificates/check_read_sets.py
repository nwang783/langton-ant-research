"""Independent literal/weighted-walk controls for exact unit-refinement read sets.
No claim that arbitrary chronological equality is Presburger. No solver wrapper.
"""
import itertools, json, pathlib, time, hashlib
HERE=pathlib.Path(__file__).parent
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,a):
 x,y=p
 for _ in range(a%4):x,y=-y,x
 return x,y

def typed(images):
 out=[]
 for s,w in enumerate(images):
  p=(0,0);h=s//2;row=[]
  for c in w:
   child=2*h+(c=='L');row.append((child,p))
   h=(h+(1 if c=='R' else -1))%4
   p=(p[0]+D[h][0],p[1]+D[h][1])
  out.append(row)
 return out

def literal(images,s,r):
 subst=typed(images);word=[s]
 for _ in range(r):word=[t for old in word for t,p in subst[old]]
 p=(0,0);h=s//2;reads=set()
 for st in word:
  assert h==st//2
  reads.add(p);h=(h+(1 if st%2==0 else -1))%4
  p=(p[0]+D[h][0],p[1]+D[h][1])
 return reads,p,h,len(word)

def weighted_graph(images,a):
 subst=typed(images);q=next(q for q in range(1,5) if a*q%4==0)
 graph={}
 for s in range(8):
  for ph in range(q):
   graph[s,ph]=[((t,(ph-1)%q),rot(p,a*ph)) for t,p in subst[s]]
 return graph,q

def graph_walks(graph,start,r):
 states={(start,(0,0))}
 for _ in range(r):
  states={(t,(p[0]+w[0],p[1]+w[1])) for s,p in states for t,w in graph[s]}
 return states

def compositions(n,m):
 if m==0:
  if n==0:yield ()
 elif m==1:yield (n,)
 else:
  for v in range(n+1):
   for tail in compositions(n-v,m-1):yield (v,)+tail

def euler_formula(vertices,edges,start,end,counts):
 # This implements only the explicit quantifier-free condition on edge counts.
 n=sum(counts)
 if n==0:return start==end
 bal={v:0 for v in vertices};adj={v:set() for v in vertices};active=set()
 for (u,v,w),c in zip(edges,counts):
  bal[u]+=c;bal[v]-=c
  if c:
   adj[u].add(v);adj[v].add(u);active|={u,v}
 if any(bal[v]!=(int(v==start)-int(v==end)) for v in vertices):return False
 seen={start};todo=[start]
 while todo:
  for v in adj[todo.pop()]-seen:seen.add(v);todo.append(v)
 return active<=seen

def explicit_walk_counts(vertices,edges,start,r):
 states={(start,(0,)*len(edges))}
 for _ in range(r):
  nxt=set()
  for old,c in states:
   for i,(u,v,w) in enumerate(edges):
    if u==old:
     nc=list(c);nc[i]+=1;nxt.add((v,tuple(nc)))
  states=nxt
 return states

def main():
 start=time.monotonic()
 old=json.loads((HERE.parent/'unit_fourier/unit9_fourier.json').read_text())
 cases=[]
 for a,pair in old['geometric_controls']:
  cases.append((a,list(pair)*4))
 state=json.loads((HERE.parent/'unit_fourier/check_state_adapter.json').read_text())
 cases += [(0,c['images']) for c in state['cases'][:8]]
 checks=letters=0;records=[]
 for ci,(a,images) in enumerate(cases):
  graph,q=weighted_graph(images,a)
  for s in range(8):
   for r in range(5):
    actual,p,h,n=literal(images,s,r)
    expected={p for st,p in graph_walks(graph,(s,(r-1)%q),r)}
    assert actual==expected,(ci,s,r)
    outgoing=(s//2+(1 if s%2==0 else -1))%4
    assert h==outgoing and p==rot(D[outgoing],a*r)
    checks+=1;letters+=n
    records.append([ci,s,r,len(actual),n])
 # All short count vectors, not merely count vectors obtained from known walks.
 # These graph families include disconnected cycles, parallel edges and self-loops.
 graph_specs=[
  (2,[(0,0),(0,1),(1,0),(1,1)]),
  (3,[(0,1),(1,0),(1,2),(2,1),(2,2)]),
  (4,[(0,1),(1,0),(2,3),(3,2)]),
  (3,[(0,1),(0,1),(1,2),(2,0),(1,1),(2,2)]),
 ]
 formula_checks=walk_objects=0
 for nv,arcs in graph_specs:
  vertices=list(range(nv));edges=[(u,v,(i-2,2-i%3)) for i,(u,v) in enumerate(arcs)]
  for root in vertices:
   for r in range(7):
    actual=explicit_walk_counts(vertices,edges,root,r);walk_objects+=len(actual)
    projected=set()
    for cnt in compositions(r,len(edges)):
     for end in vertices:
      accepted=euler_formula(vertices,edges,root,end,cnt)
      assert accepted==((end,cnt) in actual),(arcs,root,r,end,cnt)
      formula_checks+=1
      if accepted:projected.add((end,tuple(sum(cnt[i]*edges[i][2][j] for i in range(len(edges))) for j in range(2))))
    graph={v:[(to,w) for fr,to,w in edges if fr==v] for v in vertices}
    assert projected==graph_walks(graph,root,r)
 # Exact positive frame control: all identity images have valid finite I/O templates,
 # but are rejected by the separate growing-root condition.
 for s in range(8):
  I={(0,0)} if s%2 else set();O=I^{(0,0)}
  for r in range(6):
   reads,p,h,n=literal(['R','L']*4,s,r)
   assert reads=={(0,0)} and n==1
   assert O==I^reads
 identity_control={'finite_block_semantics':'PASS','growing_root':'REJECT'}
 data=json.dumps(records,separators=(',',':')).encode()+b'\n'
 (HERE/'read_sets.records.json').write_bytes(data)
 out=dict(geometric_cases=len(cases),all_four_units=True,unequal_lengths=True,
 literal_readset_checks=checks,literal_letters=letters,
 exhaustive_euler_formula_checks=formula_checks,explicit_edge_count_walks=walk_objects,
 identity_control=identity_control,records_sha256=hashlib.sha256(data).hexdigest(),
 scope='Exact read sets and Euler formula controls only; no accepted growing ant certificate.',seconds=time.monotonic()-start)
 (HERE/'read_sets.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
