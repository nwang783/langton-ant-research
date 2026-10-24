"""Independent verifier of fresh V-tip theorem for C/V concatenations.
Only two literal turn strings, integer geometry, and a 3x3 tracked patch are used.
State bits encode CURRENT colors, not previous turn letters. Outside is a single
nondeterministic cursor with every geometrically possible reentry allowed.
"""
from collections import deque
import json,sys
WORDS={'C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'}
DIR=((0,1),(1,0),(0,-1),(-1,0))
PATCH=[(x,y) for x in (0,1,2) for y in (1,2,3)]
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

# The maximum relative trace coordinate is at most 4. Any pose reading PATCH
# has |p_x|<=6,|p_y|<=7, hence |a|,|b|<=4. Searching [-10,10] is ample.
for w in WORDS.values():
 tt,_=trace((0,0,0),w);assert max(max(abs(x),abs(y)) for (x,y),_ in tt)<=4
centers=set()
for a in range(-10,11):
 for b in range(-10,11):
  if any(any(q in IDX for q,c in trace(start_pose(a,b,h),w)[0]) for h in range(4) for w in WORDS.values()):centers.add((a,b))
assert all(abs(a)<=4 and abs(b)<=4 for a,b in centers)
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
 # A V from outside can enter head iff its predecessor coarse center is outside.
 a,b,h=head;da,db=((1,0),(0,-1),(-1,0),(0,1))[h]
 if (a-da,b-db) not in centers:BOUNDARY.add(head)

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
 assert not bad,('OLD-NOSE ABSTRACT WITNESS',s)
 for t in nxt:
  if t not in SEEN:SEEN.add(t);todo.append(t)
print(json.dumps({'result':'old V nose reuse excluded','tracked_cells':len(PATCH),'coarse_centers':sorted(centers),'head_states':len(HEADS)+1,'initial_states':len(INITIAL),'reachable_states':len(SEEN),'outside_color_states':sum(s[0]==OUT for s in SEEN)}))
# Repeat the finite inductive-closure check separately from exploration order.
assert INITIAL<=SEEN
for s in SEEN:
 nxt,bad=successors(s);assert not bad and all(t in SEEN for t in nxt)
if '--certificate' in sys.argv:
 payload={'patch':PATCH,'centers':sorted(centers),'initial_states':sorted(INITIAL,key=repr),'reachable_states':sorted(SEEN,key=repr)}
 with open('/workspace/shared/langton/word_stabilization/cv_nose_certificate.json','w') as f:json.dump(payload,f,indent=2)
