"""Bounded negative-control search, NOT a freshness certificate.
Literal macro words only; geometry and complete prefix consistency rebuilt.
Every prefix starts non-C. At each possible first C, test CV and CCV now.
"""
import sys,time,json,hashlib
from pathlib import Path
WORDS={
 'C':'LLLLRLRRRRLRRRR',
 'V':'LLLLRLRRRRLRRLRRRR',
 'U':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR',
 'Q':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRRLRRRR',
 'B':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR'}
DIRS=((0,1),(1,0),(0,-1),(-1,0))
def rotate(p,h):
 x,y=p
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h]
DATA={}
for a,w in WORDS.items():
 first={};last={};x=y=h=0
 for c in w:
  p=(x,y);v=(c=='L')
  if p in last:assert last[p]!=v
  first.setdefault(p,v);last[p]=v
  h=(h+(1 if c=='R'else-1))%4;dx,dy=DIRS[h];x+=dx;y+=dy
 for h0 in range(4):
  DATA[a,h0]=(tuple((rotate(p,h0),v,last[p])for p,v in first.items()),rotate((x,y),h0),(h+h0)%4)
MARKS=json.load(open(Path(__file__).with_name('cfree_kernel_current_marks.json')))
centers={(-1,1)}
def center(p):
 x,y,h=p;dx,dy=rotate((-1,1),h);return(2*x+dx,2*y+dy)
last={};nodes=0;tests=0;terminal_old=0;witness=None
DEPTH=int(sys.argv[1])if len(sys.argv)>1 else 18
CAP=int(sys.argv[2])if len(sys.argv)>2 else 2000000
start=time.monotonic();counts=[0]*(DEPTH+1)
def apply(a,pose):
 x,y,h=pose;items,d,nh=DATA[a,h];undo=[]
 added=None
 if a=='C':
  for (dx,dy),first,end in items:
   p=(x+dx,y+dy);old=last.get(p)
   if old is not None and old==first:return None
 else:
  for q in MARKS[a]:
   dx,dy=rotate(q,h)
   if(x+dx,y+dy)in last:return None
  added=center((x+d[0],y+d[1],nh))
  if added in centers:return None
  centers.add(added)
 for (dx,dy),first,end in items:
  p=(x+dx,y+dy);undo.append((p,last.get(p)));last[p]=end
 return((x+d[0],y+d[1],nh),(undo,added))
def rollback(undo):
 undo,added=undo
 if added is not None:centers.remove(added)
 for p,old in undo:
  if old is None:del last[p]
  else:last[p]=old

def completion(prefix,pose):
 global tests,terminal_old,witness
 dx,dy=rotate((-1,0),pose[2]);q=(pose[0]+dx,pose[1]+dy)
 if q not in last:return False
 z=apply('C',pose)
 if z is None:return False
 terminal_old+=1;p1,u1=z
 witness={'word':prefix+'C','marker':q,'first_C_index':len(prefix),'end_pose':p1};print('RELAXED WITNESS',json.dumps(witness),flush=True)
 rollback(u1);return True
 for suffix in ('V','CV'):
  p=p1;undos=[];okay=True
  for a in suffix:
   z=apply(a,p)
   if z is None:okay=False;break
   p,undo=z;undos.append(undo)
  tests+=1
  if okay:witness={'word':prefix+'C'+suffix,'marker':q,'first_C_index':len(prefix),'end_pose':p};print('RELAXED WITNESS',json.dumps(witness),flush=True)
  for undo in reversed(undos):rollback(undo)
  if okay:rollback(u1);return True
 rollback(u1);return False

def search(prefix,pose):
 global nodes
 nodes+=1;counts[len(prefix)]+=1
 if nodes>CAP:raise RuntimeError('resource cap')
 if prefix and prefix[-1]!='C' and completion(prefix,pose):return True
 if len(prefix)==DEPTH:return False
 for a in 'VUQB':
  if any(w in prefix+a for w in BAD):continue
  z=apply(a,pose)
  if z is None:continue
  p,undo=z
  yes=search(prefix+a,p);rollback(undo)
  if yes:return True
 return False
BAD=json.load(open(Path(__file__).with_name('literal_short_grammar_8.json')))['forbidden']
status='bounded relaxed search exhausted'
try:
 if search('',(0,0,0)):status='relaxed constraint witness, not physical'
except RuntimeError:status='resource cap; no conclusion'
out={'status':status,'max_prefix_macros':DEPTH,'node_cap':CAP,'nodes':nodes,'feasible_prefix_counts':counts,'reused_feasible_first_Cs':terminal_old,'completion_tests':tests,'witness':witness,'seconds':time.monotonic()-start,'words_sha256':hashlib.sha256(json.dumps(WORDS,sort_keys=True).encode()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
