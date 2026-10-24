"""Sound conservative three-input V fresh-fuel disjunction search.
Flags record prior physical reads, not coset novelty. All patch colors and
initial poses are unconstrained; every history uses only the five macros.
An abstract witness is inconclusive, never a physical counterexample.
"""
import sys,json,time
from collections import deque
sys.path.insert(0,'/workspace/shared/langton/word_stabilization')
from bdd_local_gc import BDD,unit_test
from verify_macro_word import D
DIR=((0,1),(1,0),(0,-1),(-1,0));ALPHA='CUVQB';TARGET='V';coarse10=False
MARK=[(-1,0),(-1,-1),(1,2)]
P=list(dict.fromkeys(tuple(t['p']) for t in D['V']['trace']))
if len(sys.argv)>2 and sys.argv[2]=='union':P=sorted({(x,y) for q in MARK for x in range(q[0]-1,q[0]+2) for y in range(q[1]-1,q[1]+2)})
LIMIT=int(sys.argv[1]) if len(sys.argv)>1 else 500000
ix={p:i for i,p in enumerate(P)};bb=BDD(len(P))
PORT=json.load(open('/workspace/shared/langton/word_stabilization/minimized_actual_ports.json'))
contexts=PORT['states'];CT={(a,k):b for a,k,b in PORT['transitions']};SOURCE_CTX=PORT['source_contexts']
print('THREE INPUT DISJUNCTION','cells',len(P),'contexts',len(contexts),'cap',LIMIT,flush=True)
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
  guard=bb.cube(known,black);T[head,k]=(to,guard,odd,sum((1<<j) for j,p in enumerate(MARK) if any(cell==p for cell,c in tr)))
  for oldh in range(4):
   _,(da,db,endh)=zero[oldh,k]
   if endh==h and (a-da,b-db) not in centers:BOUND[oldh,k].append(head)

F={(head,ctx,0):1 for head in heads for ctx in contexts};queue=deque(F);queued=set(queue);iters=0;t0=time.time()
print('INITIAL STATES',len(F),'heads',len(heads),flush=True)
while queue:
 key=queue.popleft();queued.remove(key);head,ctx,flag=key;iters+=1
 if len(bb.nodes)>150000 and iters%200==0:
  before=len(bb.nodes);mp=bb.collect(list(F.values())+[x[1] for x in T.values()])
  F={h:mp[v] for h,v in F.items()};T={hk:(to,mp[g],odd,t) for hk,(to,g,odd,t) in T.items()}
  print('GC',iters,before,'->',len(bb.nodes),'elapsed',round(time.time()-t0,1),flush=True)
  if len(bb.nodes)>LIMIT:print('LIVE NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
 images=[]
 for k in ALPHA:
  nc=CT.get((ctx,k))
  if nc is None:continue
  if head[0]=='OUT':
   oldh=head[1];_,(_,_,newh)=zero[oldh,k]
   images.append(((('OUT',newh),nc,flag),F[key]))
   images.extend(((to,nc,flag),F[key]) for to in BOUND[oldh,k])
  else:
   to,guard,odd,touched=T[head,k];pre=bb.intersect(F[key],guard)
   if head==(0,0,0) and k=='V' and flag==7 and pre:
    print('ABSTRACT ALL-STALE V', 'iterations',iters,'bddnodes',len(bb.nodes),'states',len(F),'time',time.time()-t0,flush=True);sys.exit(0)
   if pre:images.append(((to,nc,flag|touched),bb.flip(pre,odd)))
 for to,img in images:
  old=F.get(to,0);new=bb.union(old,img)
  if new!=old:
   F[to]=new
   if to not in queued:queued.add(to);queue.append(to)
else:print('EXCLUDED ALL-STALE V','cells',len(P),'heads',len(heads),'contexts',len(contexts),'iterations',iters,'bddnodes',len(bb.nodes),'states',len(F),'time',time.time()-t0,flush=True)
