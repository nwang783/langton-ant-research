"""Local last-writer verifier for fresh V-tip in C/V/B concatenations.
Only three literal turn strings, integer geometry, and a finite patch are used.
State bits encode CURRENT colors, not previous turn letters. Outside is a single
nondeterministic cursor with every geometrically possible reentry allowed.
"""
from collections import deque
import json,sys
WORDS={'C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR','B':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR'}
DIR=((0,1),(1,0),(0,-1),(-1,0))
R=int(sys.argv[1]) if len(sys.argv)>1 else 1
PATCH=[(0,0),(0,2),(1,2),(2,0),(2,1)]
IDX={p:i for i,p in enumerate(PATCH)}
NOSE=(1,2);NOSEBIT=1<<IDX[NOSE]

def start_pose(a,b,h):
 # doubled center=(-1,1)+a*(2,6)+b*(-6,2); 2p=2z-f+r.
 f=DIR[h];r=DIR[(h+1)%4]
 return ((-1+2*a-6*b-f[0]+r[0])//2,(1+6*a+2*b-f[1]+r[1])//2,h)

def trace(pose,word):
 x,y,h=pose;out=[]
 for c in word:
  out.append(((x,y),c=='L'))
  h=(h+(1 if c=='R' else -1))%4
  dx,dy=DIR[h];x+=dx;y+=dy
 return out,(x,y,h)

def coarse(pose):
 x,y,h=pose;f=DIR[h];r=DIR[(h+1)%4]
 X=2*x+f[0]-r[0]+1;Y=2*y+f[1]-r[1]-1
 assert (X+3*Y)%20==0 and (-3*X+Y)%20==0
 return ((X+3*Y)//20,(-3*X+Y)//20,h)

# Exact inverse lattice equations: enumerate every way a macro can read any
# tracked cell. This is finite and does not use a guessed spatial cutoff.
centers=set()
for qx,qy in PATCH:
 for h in range(4):
  px,py,_=start_pose(0,0,h)
  for word in WORDS.values():
   tr,_=trace((px,py,h),word)
   for (rx,ry),read_black in tr:
    X,Y=qx-rx,qy-ry
    if (X+3*Y)%10==0 and (-3*X+Y)%10==0:
     centers.add(((X+3*Y)//10,(-3*X+Y)//10))
HEADS=[(a,b,h) for a,b in sorted(centers) for h in range(4)]
OUT='outside';heads=set(HEADS)
TRANS={};INITIAL=set();BOUNDARY=set()
for head in HEADS:
 for k,w in WORDS.items():
  tr,end=trace(start_pose(*head),w);to=coarse(end);to=to if to in heads else OUT
  seq=[(1<<IDX[q],black) for q,black in tr if q in IDX]
  TRANS[head,k]=(to,seq)
  # Colors immediately after a possible last R-writing macro.
  nose_reads=[black for q,black in tr if q==NOSE]
  if nose_reads and nose_reads[-1]==False:
   known=blackmask=0
   for bit,read_black in seq:
    known|=bit
    if read_black:blackmask&=~bit
    else:blackmask|=bit
   INITIAL.add((to,known,blackmask))
 # V and B predecessor centers are respectively one and two forward units back.
 # The predecessor B heading is reversed, but only its center membership matters.
 a,b,h=head;da,db=((1,0),(0,-1),(-1,0),(0,1))[h]
 if (a-da,b-db) not in centers or (a-2*da,b-2*db) not in centers:BOUNDARY.add(head)

def successors(state):
 head,known,blackmask=state
 if head==OUT:
  return [(h,known,blackmask) for h in BOUNDARY],False
 out=[]
 for k in WORDS:
  to,seq=TRANS[head,k];target=(head==(0,0,0) and k=='V')
  if not target and any(bit==NOSEBIT for bit,c in seq):continue
  nk,nb=known,blackmask
  for bit,read_black in seq:
   if nk&bit and bool(nb&bit)!=read_black:break
   nk|=bit
   if read_black:nb&=~bit
   else:nb|=bit
  else:
   if target:return [],True
   out.append((to,nk,nb))
 return out,False

SEEN=set(INITIAL);todo=deque(INITIAL)
while todo:
 s=todo.popleft();nxt,bad=successors(s)
 if bad: print('ABSTRACT WITNESS',s,len(SEEN));sys.exit(0)
 if len(SEEN)>2000000:print('CAP',len(SEEN));sys.exit(0)
 for t in nxt:
  if t not in SEEN:SEEN.add(t);todo.append(t)
print('EXCLUDED',R,'headstates',len(HEADS)+1,'reachable',len(SEEN))
