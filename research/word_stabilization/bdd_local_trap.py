"""Symbolic complete-color local last-writer abstraction (discovery verifier).
Uses a compact reduced ordered BDD implemented here, no external dependencies.
Transfer = intersection with exact macro input guard, then XOR odd read set.
An abstract witness is NOT necessarily a physically feasible macro word.
"""
from collections import deque
from functools import lru_cache
import json,sys,time,random
from verify_macro_word import D
DIR=((0,1),(1,0),(0,-1),(-1,0))
class BDD:
 def __init__(self,n):self.n=n;self.nodes=[(n,0,0),(n,1,1)];self.unique={}
 def node(self,v,l,h):
  if l==h:return l
  key=(v,l,h)
  if key not in self.unique:self.unique[key]=len(self.nodes);self.nodes.append(key)
  return self.unique[key]
 @lru_cache(None)
 def union(self,a,b):
  if a==b or not b:return a
  if not a:return b
  if a==1 or b==1:return 1
  if a>b:return self.union(b,a)
  va,la,ha=self.nodes[a];vb,lb,hb=self.nodes[b];v=min(va,vb)
  if va!=v:la=ha=a
  if vb!=v:lb=hb=b
  return self.node(v,self.union(la,lb),self.union(ha,hb))
 @lru_cache(None)
 def intersect(self,a,b):
  if a==b or b==1:return a
  if a==1:return b
  if not a or not b:return 0
  if a>b:return self.intersect(b,a)
  va,la,ha=self.nodes[a];vb,lb,hb=self.nodes[b];v=min(va,vb)
  if va!=v:la=ha=a
  if vb!=v:lb=hb=b
  return self.node(v,self.intersect(la,lb),self.intersect(ha,hb))
 @lru_cache(None)
 def flip(self,a,mask):
  if a<2 or not mask:return a
  v,l,h=self.nodes[a];l=self.flip(l,mask);h=self.flip(h,mask)
  return self.node(v,h,l) if mask>>v&1 else self.node(v,l,h)
 def cube(self,known,black):
  x=1
  for v in reversed(range(self.n)):
   if known>>v&1:x=self.node(v,0,x) if black>>v&1 else self.node(v,x,0)
  return x
 def evaluate(self,a,color):
  while a>=2:
   v,l,h=self.nodes[a];a=h if color>>v&1 else l
  return bool(a)
 def count(self,a):
  @lru_cache(None)
  def rec(x,lo):
   if x<2:return x*(1<<(self.n-lo))
   v,l,h=self.nodes[x];return (1<<(v-lo))*(rec(l,v+1)+rec(h,v+1))
  return rec(a,0)

def unit_test():
 rng=random.Random(9);b=BDD(7)
 for _ in range(100):
  k1=rng.randrange(128);v1=rng.randrange(128)&k1;k2=rng.randrange(128);v2=rng.randrange(128)&k2;flip=rng.randrange(128)
  x=b.cube(k1,v1);y=b.cube(k2,v2);a=b.union(x,y);c=b.intersect(x,y);f=b.flip(a,flip)
  for v in range(128):
   t1=(v&k1==v1);t2=(v&k2==v2)
   assert b.evaluate(a,v)==(t1 or t2) and b.evaluate(c,v)==(t1 and t2)
   assert b.evaluate(f,v)==b.evaluate(a,v^flip)
  assert b.count(a)==sum(b.evaluate(a,v) for v in range(128))

if __name__=='__main__':
 unit_test()
 ALPHA=sys.argv[1] if len(sys.argv)>1 else 'CV'
 TARGET=sys.argv[2] if len(sys.argv)>2 else 'V'
 R=int(sys.argv[3]) if len(sys.argv)>3 else 1
 LIMIT=int(sys.argv[4]) if len(sys.argv)>4 else 3000000
 q=(1,2) if TARGET=='V' else (0,2)
 if R==-2:P=[(0,0),(0,2),(1,2),(2,0),(2,1)]
 elif R==-1:P=[(0,0),(0,3),(1,2),(1,3),(1,4),(2,0),(2,1)]
 elif R==0:P=[(1,1),(1,2),(2,1),(2,2)]
 else:P=[(x,y) for x in range(q[0]-R,q[0]+R+1) for y in range(q[1]-R,q[1]+R+1)]
 ix={p:i for i,p in enumerate(P)};qb=1<<ix[q];bb=BDD(len(P));coarse10=not any(k in ALPHA for k in 'UQ')
 def coeff(x,y):
  if coarse10:
   if (x+3*y)%10 or (-3*x+y)%10:return None
   return (x+3*y)//10,(-3*x+y)//10
  if (x+y)%2:return None
  return (x+y)//2,(x-y)//2
 def pose(a,b,h):
  f=DIR[h];r=DIR[(h+1)%4];x,y=((a-3*b,3*a+b) if coarse10 else (a+b,a-b))
  return ((-1+2*x-f[0]+r[0])//2,(1+2*y-f[1]+r[1])//2,h)
 def coord(x,y,h):
  f=DIR[h];r=DIR[(h+1)%4];X=(2*x+f[0]-r[0]+1)//2;Y=(2*y+f[1]-r[1]-1)//2
  c=coeff(X,Y);assert c is not None;return (*c,h)
 def trace(head,k):
  x,y,h=pose(*head);tr=[]
  for c in D[k]['word']:
   tr.append(((x,y),c=='L'));h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
  return tr,coord(x,y,h)
 zero={(h,k):trace((0,0,h),k) for h in range(4) for k in ALPHA}
 centers=set()
 for qx,qy in P:
  for tr,end in zero.values():
   for (rx,ry),c in tr:
    v=coeff(qx-rx,qy-ry)
    if v is not None:centers.add(v)
 heads=[(*c,h) for c in sorted(centers) for h in range(4)];OUT=None;HS=set(heads);heads.append(OUT)
 boundary=set();initial={h:0 for h in heads};T={}
 for head in heads[:-1]:
  a,b,h=head
  for k in ALPHA:
   tr,to=trace(head,k);to=to if to in HS else OUT;seq=[(1<<ix[p],c) for p,c in tr if p in ix]
   known=black=odd=0;postblack=0;valid=True
   for bit,c in seq:
    if not known&bit:known|=bit;black|=bit if c else 0
    elif bool((black^odd)&bit)!=c:valid=False
    odd^=bit
    postblack=(postblack&~bit) if c else (postblack|bit)
   assert valid
   guard=bb.cube(known,black);T[head,k]=(to,guard,odd,any(bit==qb for bit,c in seq))
   nr=[c for p,c in tr if p==q]
   if nr and not nr[-1]:initial[to]=bb.union(initial[to],bb.cube(known,postblack))
   for oldh in range(4):
    _,(da,db,endh)=zero[oldh,k]
    if endh==h and (a-da,b-db) not in centers:boundary.add(head)
 F=dict(initial);queue=deque(h for h in heads if F[h]);queued=set(queue);iters=0;t0=time.time()
 while queue:
  head=queue.popleft();queued.remove(head);iters+=1
  if len(bb.nodes)>LIMIT:print('NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
  if head==OUT:images=[(h,F[head]) for h in boundary]
  else:
   images=[]
   for k in ALPHA:
    to,guard,odd,touches=T[head,k];target=head==(0,0,0) and k==TARGET
    if touches and not target:continue
    pre=bb.intersect(F[head],guard)
    if target and pre:
     print('ABSTRACT WITNESS',ALPHA,TARGET,R,'iterations',iters,'bddnodes',len(bb.nodes),'time',time.time()-t0,flush=True);sys.exit(0)
    if pre:images.append((to,bb.flip(pre,odd)))
  for to,img in images:
   new=bb.union(F[to],img)
   if new!=F[to]:
    F[to]=new
    if to not in queued:queued.add(to);queue.append(to)
 else:
  print('EXCLUDED',ALPHA,TARGET,R,'cells',len(P),'heads',len(heads),'iterations',iters,'bddnodes',len(bb.nodes),'fullcolorstates',sum(bb.count(v) for v in F.values()),'time',time.time()-t0,flush=True)
