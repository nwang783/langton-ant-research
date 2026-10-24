"""Explicit complete-color checker for five-macro common-star genealogy restrictions.
Literal turn blocks, no BDD or recovered simulator import. No global proof.
"""
from collections import deque,Counter
from pathlib import Path
import json
DIR=((0,1),(1,0),(0,-1),(-1,0))
WORDS={
'C':'LLLLRLRRRRLRRRR',
'V':'LLLLRLRRRRLRRLRRRR',
'B':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR'}
WORDS['U']='LLLLRLRRRRLRLLLLRRRRLRRLRRRR'
WORDS['Q']='LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRRLRRRR'
P=[(x,y) for x in range(0,3) for y in range(-1,2)];IX={q:i for i,q in enumerate(P)};q=(1,0);QB=1<<IX[q]

def coeff(x,y):
 if (x+y)%2:return None
 return ((x+y)//2,(x-y)//2)
def pose(head):
 a,b,h=head;f=DIR[h];r=DIR[(h+1)%4]
 return ((-1+2*a+2*b-f[0]+r[0])//2,(1+2*a-2*b-f[1]+r[1])//2,h)
def coord(x,y,h):
 f=DIR[h];r=DIR[(h+1)%4];c=coeff((2*x+f[0]-r[0]+1)//2,(2*y+f[1]-r[1]-1)//2)
 assert c is not None;return (*c,h)
def motion(head,m):
 x,y,h=pose(head);tr=[]
 for c in WORDS[m]:
  tr.append(((x,y),c));h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 return tr,coord(x,y,h)
ZERO={(h,m):motion((0,0,h),m) for h in range(4) for m in WORDS}
CENTERS=set()
for px,py in P:
 for tr,end in ZERO.values():
  for (x,y),c in tr:
   v=coeff(px-x,py-y)
   if v is not None:CENTERS.add(v)
HEADS=[(*c,h) for c in sorted(CENTERS) for h in range(4)];HS=set(HEADS);OUT=None;HEADS.append(OUT)
BOUNDARY=set();TRANS={};INITIAL_BAD=set();INITIAL_C11=set();ALLOWED={('C',11),('V',14),('B',70),('U',24),('Q',60)}
for head in HEADS[:-1]:
 a,b,h=head
 for m in WORDS:
  tr,to=motion(head,m);to=to if to in HS else OUT;known=black=odd=0
  for cell,c in tr:
   if cell not in IX:continue
   bit=1<<IX[cell]
   if not known&bit:known|=bit;black|=bit if c=='L' else 0
   else:assert bool((black^odd)&bit)==(c=='L')
   odd^=bit
  touches=any(cell==q for cell,c in tr);TRANS[head,m]=(to,known,black,odd,touches)
  hits=[i for i,(cell,c) in enumerate(tr) if cell==q]
  if hits and tr[hits[-1]][1]=='R':
   j=hits[-1];owner=max(i for i,c in enumerate(WORDS[m][:j]) if c=='L')+1
   posts=[color for color in range(1<<len(P)) if color&known==(black^odd)&known]
   assert all(color&QB for color in posts)
   if (m,owner) not in ALLOWED:INITIAL_BAD.update((to,color,0) for color in posts)
   if (m,owner)==('C',11):INITIAL_C11.update((to,color,0) for color in posts)
  for oldh in range(4):
   _,(da,db,eh)=ZERO[oldh,m]
   if eh==h and (a-da,b-db) not in CENTERS:BOUNDARY.add(head)

def closure(initial,separated):
 reached=set(initial);queue=deque(initial)
 while queue:
  head,color,flag=queue.popleft()
  if head is OUT:
   images=[(h,color,f) for h in BOUNDARY for f in ((flag,1) if separated else (0,))]
  else:
   images=[]
   for m in WORDS:
    to,known,black,odd,touches=TRANS[head,m]
    target=head==(0,0,0) and m in WORDS and (flag or not separated)
    if touches and not target:continue
    if color&known!=black:continue
    assert not target,('counterexample in conservative abstraction',head,color,flag,m)
    images.append((to,color^odd,int(flag or m!='C') if separated else 0))
  for st in images:
   if st not in reached:reached.add(st);queue.append(st)
 # Independently recheck inductive closure and target exclusion.
 for head,color,flag in reached:
  if head is OUT:
   for h in BOUNDARY:
    for f in ((flag,1) if separated else (0,)):assert (h,color,f) in reached
  else:
   for m in WORDS:
    to,known,black,odd,touches=TRANS[head,m];target=head==(0,0,0) and m in WORDS and (flag or not separated)
    if color&known!=black:continue
    assert not target
    if not touches:assert (to,color^odd,int(flag or m!='C') if separated else 0) in reached
 return reached
print('GEOMETRY',len(HEADS),'initials',len(INITIAL_BAD),len(INITIAL_C11),flush=True)
BAD=closure(INITIAL_BAD,False);print('BAD EXCLUDED',len(BAD),flush=True)
SEP=closure(INITIAL_C11,True);print('SEPARATED EXCLUDED',len(SEP),flush=True)

out=dict(patch=P,head_count=len(HEADS),producer_types_allowed=sorted(ALLOWED),forbidden_producer_initials=len(INITIAL_BAD),forbidden_producer_reachable=len(BAD),separation_initials=len(INITIAL_C11),separation_reachable=len(SEP),forbidden_producer_closure=sorted(BAD,key=lambda z:(str(z[0]),z[1],z[2])),separation_closure=sorted(SEP,key=lambda z:(str(z[0]),z[1],z[2])))
Path(__file__).with_name('five_macro_phase6_certificate.json').write_text(json.dumps(out,separators=(',',':')))
