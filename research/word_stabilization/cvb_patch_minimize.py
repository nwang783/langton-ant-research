"""Conservative antichain local-last-writer closure for C/V/B. Discovery only."""
from collections import deque
import json,sys,random,time
from verify_macro_word import D,rot
from cv_lattice import pose
ALPHA='CVB';NOSE=(1,2)
BASE={}
for a in range(-7,8):
 for b in range(-7,8):
  for h in range(4):
   p=pose(a,b,h);dd={}
   for k in ALPHA:
    tr=[]
    for z in D[k]['trace']:
     dx,dy=rot(z['p'],h);tr.append(((p[0]+dx,p[1]+dy),z['c']=='L'))
    da,db=((1,0),(0,-1),(-1,0),(0,1))[h]
    to=(a,b,(h-1)%4) if k=='C' else ((a+da,b+db,h) if k=='V' else (a-2*da,b-2*db,(h+2)%4))
    dd[k]=tr,to
   BASE[a,b,h]=dd

def run(P,cap=1000000,certificate=False):
 ix={p:i for i,p in enumerate(P)};qb=1<<ix[NOSE];centers={head[:2] for head,dd in BASE.items() if any(any(q in ix for q,c in tr) for tr,to in dd.values())};heads={(*c,h) for c in centers for h in range(4)};out=None
 T={};initial=set();boundary=[]
 for head in heads:
  for k,(tr,to) in BASE[head].items():
   to=to if to in heads else out;seq=[(1<<ix[q],c) for q,c in tr if q in ix];T[head,k]=to,seq
   nr=[c for q,c in tr if q==NOSE]
   if nr and not nr[-1]:
    known=black=0
    for bit,c in seq:known|=bit;black=(black&~bit) if c else (black|bit)
    initial.add((to,known,black))
  a,b,h=head;da,db=((1,0),(0,-1),(-1,0),(0,1))[h]
  if (a-da,b-db) not in centers or (a-2*da,b-2*db) not in centers:boundary.append(head)
 A={h:[] for h in [*heads,out]};Q=deque();steps=0
 def dominated(k,b,kk,bb):return kk&k==kk and (b^bb)&kk==0
 def add(st):
  h,k,b=st
  if any(dominated(k,b,kk,bb) for kk,bb in A[h]):return
  A[h]=[(kk,bb) for kk,bb in A[h] if not dominated(kk,bb,k,b)]
  A[h].append((k,b));Q.append(st)
 for st in initial:add(st)
 while Q:
  head,k,b=Q.popleft()
  if (k,b) not in A[head]:continue
  steps+=1
  if steps>cap:return None,steps,None
  if head==out:
   for hh in boundary:add((hh,k,b))
   continue
  for letter in ALPHA:
   to,seq=T[head,letter];target=head==(0,0,0) and letter=='V'
   if not target and any(bit==qb for bit,c in seq):continue
   nk,nb=k,b
   for bit,c in seq:
    if nk&bit and bool(nb&bit)!=c:break
    nk|=bit;nb=(nb&~bit) if c else (nb|bit)
   else:
    if target:return False,steps,None
    add((to,nk,nb))
 count=sum(len(v) for v in A.values())
 if certificate:return True,(steps,count),{'patch':P,'centers':sorted(centers),'initial':sorted(initial,key=repr),'antichain':[(h,k,b) for h,patterns in A.items() for k,b in patterns]}
 return True,(steps,count),None
if __name__=='__main__':
 P=[(x,y) for x in range(-1,4) for y in range(0,5)];seed=int(sys.argv[1]) if len(sys.argv)>1 else 0;rng=random.Random(seed)
 print('BASE',run(P)[:2],flush=True)
 changed=True
 while changed:
  changed=False;order=[p for p in P if p!=NOSE];rng.shuffle(order)
  for p in order:
   test=[q for q in P if q!=p];yes,n,_=run(test,200000)
   print('DELETE?',p,yes,n,flush=True)
   if yes:P=test;changed=True
 print('MINIMAL',P,flush=True);yes,n,cert=run(P,certificate=True);print('CLOSURE',yes,n,flush=True)
 json.dump(cert,open('/workspace/shared/langton/word_stabilization/cvb_patch_certificate_'+str(seed)+'.json','w'),indent=2)
