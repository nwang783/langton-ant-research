"""Independently verify an inductive BDD invariant for one guarded-XOR graph.
Does not call the search engine or import its code. No enumeration premise.
"""
from pathlib import Path
from functools import lru_cache
import sys,json
D=Path(sys.argv[1]);C=Path(sys.argv[2]);a=list(map(int,D.read_text().split()));it=iter(a);n,np,nt,nr=[next(it)for _ in range(4)];sp,sk,sv=[next(it)for _ in range(3)];T=[[next(it)for _ in range(8)]for _ in range(nt)];RE=[next(it)for _ in range(nr)];assert not list(it)
b=iter(map(int,C.read_text().split()));cn,cp,nn=[next(b)for _ in range(3)];assert(cn,cp)==(n,np);nodes=[tuple(next(b)for _ in range(3))for _ in range(nn)];roots=[next(b)for _ in range(np)];assert not list(b);assert nodes[:2]==[(n,0,0),(n,1,1)]
for i,(v,l,h)in enumerate(nodes[2:],2):
 assert 0<=v<n and 0<=l<i and 0<=h<i and l!=h
 assert nodes[l][0]>v and nodes[h][0]>v
assert all(0<=r<nn for r in roots)
checks=0;memo_states=0

def violating(f,g,k,v,flip,clear=0):
 global memo_states
 assert v&~k==0
 @lru_cache(None)
 def bad(f,g):
  if f==0 or g==1:return False
  if f==1 and g==0:return True
  top=min(nodes[f][0],nodes[g][0]);assert top<n
  bits=[(v>>top)&1]if(k>>top)&1 else[0,1]
  for bit in bits:
   ff=nodes[f][1+bit]if nodes[f][0]==top else f
   gg=nodes[g][1+(0 if((clear>>top)&1)else(bit^((flip>>top)&1)))]if nodes[g][0]==top else g
   if bad(ff,gg):return True
  return False
 r=bad(f,g);memo_states+=bad.cache_info().currsize;return r
assert not violating(1,roots[sp],sk,sv,0),'initial cube not contained'
checks+=1
for src,dst,k,v,flip,clear,goal,a in T:
 if goal:assert not violating(roots[src],0,k,v,0),('accepting colors reachable',src)
 else:assert not violating(roots[src],roots[dst],k,v,flip,clear),('transition not closed',src,dst,a)
 checks+=1
for dst in RE:
 assert not violating(roots[-1],roots[dst],0,0,0),('OUT inclusion fails',dst);checks+=1
# Count is not needed for validity, but checks literal cardinality controls.
@lru_cache(None)
def weight(i):
 if i<2:return i
 v,l,h=nodes[i];return(weight(l)<<(nodes[l][0]-v-1))+(weight(h)<<(nodes[h][0]-v-1))
states=sum(weight(r)<<nodes[r][0]for r in roots)
result={'status':'VERIFIED_INDUCTIVE_NO_HIT','variables':n,'positions':np,'nodes':nn,'states':states,'checks':checks,'memo_states':memo_states}
print(json.dumps(result))
if len(sys.argv)>3:Path(sys.argv[3]).write_text(json.dumps(result,indent=2))
