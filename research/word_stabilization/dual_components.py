import sys
from collections import deque
sys.path.insert(0,'/workspace/shared/langton/word_stabilization')
from verify_macro_word import check,D

def edge(p):
 x,y=p
 if (x+y)%2==0:return ((x+y)//2-1,(x-y)//2),((x+y)//2,(x-y)//2)
 return ((x+y-1)//2,(x-y-1)//2),((x+y-1)//2,(x-y+1)//2)
def finite_vertices(B):
 edges={frozenset(edge(p)) for p in B};pts=set().union(*edges) if edges else {(0,0)}
 xmin=min(p[0] for p in pts)-1;xmax=max(p[0] for p in pts)+1;ymin=min(p[1] for p in pts)-1;ymax=max(p[1] for p in pts)+1
 outside=set();todo=deque([(xmin,ymin)])
 while todo:
  p=todo.popleft()
  if p in outside:continue
  outside.add(p)
  for d in [(1,0),(-1,0),(0,1),(0,-1)]:
   q=p[0]+d[0],p[1]+d[1]
   if xmin<=q[0]<=xmax and ymin<=q[1]<=ymax and frozenset((p,q)) not in edges and q not in outside:todo.append(q)
 return {(x,y) for x in range(xmin,xmax+1) for y in range(ymin,ymax+1)}-outside
if __name__=='__main__':
 for w in sys.argv[1:]:
  r=check(w);B=set(map(tuple,r['seed']));i=0;print(w,'initial',finite_vertices(B))
  for b in r['blocks']:
   n=len(D[b['macro']]['word']);
   for t,x,y,c,j,k,a in r['trace'][i:i+n]:B.symmetric_difference_update([(x,y)])
   i+=n;print(b['macro'],finite_vertices(B))
