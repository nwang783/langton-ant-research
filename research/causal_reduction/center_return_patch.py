"""Conservative symbolic patch search for a repeated five-macro entry pose.
Unknown cells are unconstrained. OUT permits arbitrary reentry, so a found path
is not a physical counterexample. A closed exhaustion would be a sound exclusion.
"""
import sys,json,time
from collections import deque
sys.path.insert(0,'/workspace/shared/langton/word_stabilization')
from verify_macro_word import D
DIR=((0,1),(1,0),(0,-1),(-1,0));WORDS={m:D[m]['word'] for m in 'CUVQB'}
P=list(dict.fromkeys(tuple(t['p']) for t in D['C']['trace'][:12]))
if len(sys.argv)>1:P=[tuple(p) for p in json.load(open(sys.argv[1]))]
IX={p:i for i,p in enumerate(P)}
def coeff(x,y):return None if (x+y)%2 else ((x+y)//2,(x-y)//2)
def pose(head):
 a,b,h=head;f=DIR[h];r=DIR[(h+1)%4]
 return ((-1+2*a+2*b-f[0]+r[0])//2,(1+2*a-2*b-f[1]+r[1])//2,h)
def coord(x,y,h):
 f=DIR[h];r=DIR[(h+1)%4];c=coeff((2*x+f[0]-r[0]+1)//2,(2*y+f[1]-r[1]-1)//2)
 assert c is not None;return (*c,h)
def trace(head,m):
 x,y,h=pose(head);tr=[]
 for c in WORDS[m]:
  tr.append(((x,y),c));h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 return tr,coord(x,y,h)
ZERO={(h,m):trace((0,0,h),m) for h in range(4) for m in WORDS}
CS=set()
for px,py in P:
 for tr,end in ZERO.values():
  for (x,y),c in tr:
   z=coeff(px-x,py-y)
   if z is not None:CS.add(z)
HS={(*c,h) for c in CS for h in range(4)};OUT=None;TRANS={};BOUND=set()
for head in HS:
 a,b,h=head
 for m in WORDS:
  tr,to=trace(head,m);know=black=odd=0
  for q,c in tr:
   if q not in IX:continue
   bit=1<<IX[q]
   if not know&bit:know|=bit;black|=bit if c=='L' else 0
   else:assert bool((black^odd)&bit)==(c=='L')
   odd^=bit
  TRANS[head,m]=(to if to in HS else OUT,know,black,odd,to)
  for oldh in range(4):
   _,(da,db,eh)=ZERO[oldh,m]
   if eh==h and (a-da,b-db) not in CS:BOUND.add(head)
N=[];Q=deque();SEEN={};limit=int(sys.argv[2]) if len(sys.argv)>2 else 1000000

def add(h,k,b,parent,letter):
 for old in SEEN.get(h,[]):
  _,ok,ob,_,_=N[old]
  if ok&k==ok and (ob^b)&ok==0:return
 i=len(N);N.append((h,k,b,parent,letter));SEEN.setdefault(h,[]).append(i);Q.append(i)
for m in WORDS:
 to,k,b,o,_=TRANS[(0,0,0),m];add(to,k,b^o,-1,m)
print('PATCH',len(P),'HEADS',len(HS)+1,'INITIAL',len(N),flush=True);t0=time.time()
while Q:
 i=Q.popleft();head,k,b,prev,letter=N[i]
 if len(N)>limit:print('STATE CAP',len(N));break
 if head is OUT:
  for h in BOUND:add(h,k,b,i,'REENTER')
  continue
 for m in WORDS:
  to,gk,gb,odd,true_to=TRANS[head,m]
  if (b^gb)&k&gk:continue
  if head==(0,0,0):
   path=[];j=i
   while j>=0:
    H,K,B,J,M=N[j];path.append(dict(head=H,known=K,black=B,letter=M));j=J
   path.reverse();out=dict(patch=P,target=m,states=len(N),path=path)
   print('ABSTRACT RETURN',len(N),'time',time.time()-t0,'word',''.join(p['letter'] for p in path)+m,flush=True)
   print(json.dumps(out));sys.exit(0)
  nk=k|gk;nb=((b&k)|(gb&~k))^odd
  add(to,nk,nb,i,m)
else:print('EXCLUDED',len(N),'time',time.time()-t0)
