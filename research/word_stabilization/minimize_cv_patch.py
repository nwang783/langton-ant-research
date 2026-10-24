import itertools,collections,json
from verify_cv_nose import WORDS,DIR,start_pose,trace,coarse,PATCH,NOSE
BASE={h:{k:(trace(start_pose(*h),w)[0],coarse(trace(start_pose(*h),w)[1])) for k,w in WORDS.items()} for a in range(-4,5) for b in range(-4,5) for h in [(a,b,d) for d in range(4)]}
def run(P,cap=100000):
 ix={p:i for i,p in enumerate(P)};qb=1<<ix[NOSE]
 centers={h[:2] for h,dd in BASE.items() if any(any(q in ix for q,c in tr) for tr,to in dd.values())};heads={(*c,h) for c in centers for h in range(4)};out=None
 T={};S=set();boundary=[]
 for head in heads:
  for k,(tr,to) in BASE[head].items():
   to=to if to in heads else out;seq=[(1<<ix[q],c) for q,c in tr if q in ix];T[head,k]=to,seq
   nr=[c for q,c in tr if q==NOSE]
   if nr and not nr[-1]:
    known=black=0
    for bit,c in seq:known|=bit;black=(black&~bit) if c else (black|bit)
    S.add((to,known,black))
  a,b,h=head;da,db=((1,0),(0,-1),(-1,0),(0,1))[h]
  if (a-da,b-db) not in centers:boundary.append(head)
 Q=collections.deque(S)
 while Q:
  head,known,black=Q.popleft()
  if len(S)>cap:return None,len(S)
  if head==out:ns=[(h,known,black) for h in boundary]
  else:
   ns=[]
   for k in WORDS:
    to,seq=T[head,k];target=head==(0,0,0) and k=='V'
    if not target and any(bit==qb for bit,c in seq):continue
    nk,nb=known,black
    for bit,c in seq:
     if nk&bit and bool(nb&bit)!=c:break
     nk|=bit;nb=(nb&~bit) if c else (nb|bit)
    else:
     if target:return False,len(S)
     ns.append((to,nk,nb))
  for s in ns:
   if s not in S:S.add(s);Q.append(s)
 return True,len(S)
rest=[p for p in PATCH if p!=NOSE]
for n in range(1,10):
 found=[]
 for subset in itertools.combinations(rest,n-1):
  P=[NOSE,*subset];yes,count=run(P)
  if yes:found.append((P,count))
 print('SIZE',n,'solutions',found,flush=True)
 if found:
  open('/workspace/shared/langton/word_stabilization/cv_minimal_patch.json','w').write(json.dumps(found,indent=2));break
