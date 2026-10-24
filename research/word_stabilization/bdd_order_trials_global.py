"""Local last-writer closure with exact short-macro grammar and oriented OUT.
A no-reuse exclusion here is sound; a path remains only an abstract witness.
All A C^k B feasibility guards are derived by literal parity replay.
"""
from bdd_local_gc import BDD,unit_test
from collections import deque
import sys,time,json
from verify_macro_word import D
DIR=((0,1),(1,0),(0,-1),(-1,0))
ALPHA=sys.argv[1] if len(sys.argv)>1 else 'CUVQB';TARGET=sys.argv[2] if len(sys.argv)>2 else 'Q';R=int(sys.argv[3]) if len(sys.argv)>3 else 2
q=tuple(map(int,sys.argv[4].split(','))) if len(sys.argv)>4 else ({'V':(1,2),'U':(0,2),'Q':(-3,1),'B':(-3,1)}[TARGET])
LIMIT=int(sys.argv[5]) if len(sys.argv)>5 else 2000000
P=[(x,y) for x in range(q[0]-R,q[0]+R+1) for y in range(q[1]-R,q[1]+R+1)]
ORDER=sys.argv[6] if len(sys.argv)>6 else 'radial'
if ORDER=='radial':P.sort(key=lambda p:(abs(p[0]-q[0])+abs(p[1]-q[1]),p[0],p[1]))
elif ORDER=='chebyshev':P.sort(key=lambda p:(max(abs(p[0]-q[0]),abs(p[1]-q[1])),p[0]+p[1],p[0]))
elif ORDER=='checker':P.sort(key=lambda p:((p[0]+p[1])%2,abs(p[0]-q[0])+abs(p[1]-q[1]),p))
elif ORDER=='diagonal':P.sort(key=lambda p:(p[0]+p[1],p[0]-p[1]))
elif ORDER=='reverse':P.reverse()
print('ORDER',ORDER,P,flush=True)
ix={p:i for i,p in enumerate(P)};qb=1<<ix[q];bb=BDD(len(P));coarse10=not any(k in ALPHA for k in 'UQ')
def feasible(mword):
 last={};x=y=h=0
 for k in mword:
  for c in D[k]['word']:
   if last.get((x,y))==c:return False
   last[x,y]=c;h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 return True
contexts=[(a,n) for a in ['',*[k for k in ALPHA if k!='C']] for n in range(5) if feasible(a+'C'*n)]
CT={}
for ctx in contexts:
 a,n=ctx
 for k in ALPHA:
  nc=(a,n+1) if k=='C' else (k,0)
  if nc in contexts and feasible(a+'C'*n+k):CT[ctx,k]=nc

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
 f=DIR[h];r=DIR[(h+1)%4];X=(2*x+f[0]-r[0]+1)//2;Y=(2*y+f[1]-r[1]-1)//2;c=coeff(X,Y);assert c is not None;return (*c,h)
def trace(head,k):
 x,y,h=pose(*head);tr=[]
 for c in D[k]['word']:
  tr.append(((x,y),c=='L'));h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 return tr,coord(x,y,h)
zero={(h,k):trace((0,0,h),k) for h in range(4) for k in ALPHA};centers=set()
for qx,qy in P:
 for tr,end in zero.values():
  for (rx,ry),c in tr:
   v=coeff(qx-rx,qy-ry)
   if v is not None:centers.add(v)
heads=[(*c,h) for c in sorted(centers) for h in range(4)];HS=set(heads);OUT=[('OUT',h) for h in range(4)];inside=list(heads);heads+=OUT
F={};initial={};T={};BOUND={(h,k):[] for h in range(4) for k in ALPHA}
def put_initial(head,ctx,root):
 key=(head,ctx);initial[key]=bb.union(initial.get(key,0),root)
for head in inside:
 a,b,h=head
 for k in ALPHA:
  tr,to=trace(head,k);to=to if to in HS else ('OUT',to[2]);seq=[(1<<ix[p],c) for p,c in tr if p in ix]
  known=black=odd=postblack=0
  for bit,c in seq:
   if not known&bit:known|=bit;black|=bit if c else 0
   else:assert bool((black^odd)&bit)==c
   odd^=bit;postblack=(postblack&~bit) if c else (postblack|bit)
  guard=bb.cube(known,black);T[head,k]=(to,guard,odd,any(bit==qb for bit,c in seq))
  nr=[c for p,c in tr if p==q]
  if nr and not nr[-1]:
   root=bb.cube(known,postblack)
   for ctx in contexts:
    if (k=='C' and ctx[1]>0) or (k!='C' and ctx==(k,0)):put_initial(to,ctx,root)
  for oldh in range(4):
   _,(da,db,endh)=zero[oldh,k]
   if endh==h and (a-da,b-db) not in centers:BOUND[oldh,k].append(head)
F=dict(initial);queue=deque(F);queued=set(queue);iters=0;t0=time.time()
while queue:
 key=queue.popleft();queued.remove(key);head,ctx=key;iters+=1
 if len(bb.nodes)>100000 and iters%100==0:
  before=len(bb.nodes);roots=list(F.values())+[x[1] for x in T.values()]+list(initial.values());mp=bb.collect(roots)
  F={h:mp[v] for h,v in F.items()};initial={h:mp[v] for h,v in initial.items()};T={hk:(to,mp[g],odd,t) for hk,(to,g,odd,t) in T.items()}
  print('GC',iters,before,'->',len(bb.nodes),'elapsed',round(time.time()-t0,1),flush=True)
  if len(bb.nodes)>LIMIT:print('LIVE NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
 images=[]
 for k in ALPHA:
  nc=CT.get((ctx,k))
  if nc is None:continue
  if head[0]=='OUT':
   oldh=head[1];_,(_,_,newh)=zero[oldh,k]
   images.append(((('OUT',newh),nc),F[key]))
   images.extend(((to,nc),F[key]) for to in BOUND[oldh,k])
  else:
   to,guard,odd,touches=T[head,k];target=head==(0,0,0) and k==TARGET
   if touches and not target:continue
   pre=bb.intersect(F[key],guard)
   if target and pre:
    print('ABSTRACT WITNESS',ALPHA,TARGET,R,q,'iterations',iters,'bddnodes',len(bb.nodes),'time',time.time()-t0,flush=True);sys.exit(0)
   if pre:images.append(((to,nc),bb.flip(pre,odd)))
 for to,img in images:
  old=F.get(to,0);new=bb.union(old,img)
  if new!=old:
   F[to]=new
   if to not in queued:queued.add(to);queue.append(to)
else:print('EXCLUDED',ALPHA,TARGET,R,q,'cells',len(P),'heads',len(heads),'contexts',len(contexts),'iterations',iters,'bddnodes',len(bb.nodes),'fullcolorstates',sum(bb.count(v) for v in F.values()),'time',time.time()-t0,flush=True)
