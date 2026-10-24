from pathlib import Path
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
if len(sys.argv)>6:P=[tuple(p) for p in json.load(open(sys.argv[6]))]
ix={p:i for i,p in enumerate(P)};qb=1<<ix[q];bb=BDD(len(P));coarse10=not any(k in ALPHA for k in 'UQ')
def feasible(mword):
 last={};x=y=h=0
 for k in mword:
  for c in D[k]['word']:
   if last.get((x,y))==c:return False
   last[x,y]=c;h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 return True
# Exact recovered H-port graph, minimized by future macro language.
PORT_FILE=sys.argv[7] if len(sys.argv)>7 else '/workspace/shared/langton/word_stabilization/minimized_actual_ports.json'
port=json.load(open(PORT_FILE))
contexts=port['states']
CT={(a,k):b for a,k,b in port['transitions'] if k in ALPHA}
SOURCE_CTX={k:set(port['source_contexts'][k]) for k in ALPHA}
print('ACTUAL PORT GRAMMAR',len(contexts),'states',len(CT),'transitions',flush=True)

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
# For each exact port, its final marker begins at the current physical head.
# Remove that marker and transport the post-read colors of its 137-turn past
# to a frame whose final head is (0,0,N). A minimized class is a union, never
# an intersection, over its exact ports. Outside-state colors stay unconstrained.
def rot(x,y,h):
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
TEMPLATES={c:[] for c in contexts}
for word,c in port['port_classes']:
 assert word.endswith('LLLLRLRRRRLR')
 past=word[:-12];x=y=h=0;last={}
 for letter in past:
  last[x,y]=(letter=='R')
  h=(h+(1 if letter=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 template={rot(px-x,py-y,-h):black for (px,py),black in last.items()}
 TEMPLATES[c].append(template)
G={}
def color_guard(head,ctx):
 if head[0]=='OUT':return 1
 key=(head,ctx)
 if key in G:return G[key]
 x,y,h=pose(*head);root=0
 for template in TEMPLATES[ctx]:
  known=black=0
  for (px,py),value in template.items():
   dx,dy=rot(px,py,h);j=ix.get((x+dx,y+dy))
   if j is not None:
    bit=1<<j;known|=bit
    if value:black|=bit
  root=bb.union(root,bb.cube(known,black))
  if root==1:break
 G[key]=root
 return root
F={};initial={};T={};BOUND={(h,k):[] for h in range(4) for k in ALPHA}
def put_initial(head,ctx,root):
 root=bb.intersect(root,color_guard(head,ctx))
 if root:
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
   for ctx in SOURCE_CTX[k]:put_initial(to,ctx,root)
  for oldh in range(4):
   _,(da,db,endh)=zero[oldh,k]
   if endh==h and (a-da,b-db) not in centers:BOUND[oldh,k].append(head)
# Backward closure of the SAME finite overapproximation used by the forward
# checker. The forward source cubes are now the accepting last-R states.
SOURCE=initial
RC={c:[] for c in contexts}
for (c,k),to in CT.items():RC[to].append((c,k))
REV={}
for head in heads:
 for k in ALPHA:
  pre=[]
  if head[0]=='OUT':
   for oldh in range(4):
    if zero[oldh,k][1][2]==head[1]:pre.append((('OUT',oldh),1,0))
   for ph in inside:
    to,g,odd,touch=T[ph,k]
    if to==head and not touch:pre.append((ph,g,odd))
  else:
   a,b,h=head
   for oldh in range(4):
    _,(da,db,eh)=zero[oldh,k]
    if eh!=h:continue
    ph=(a-da,b-db,oldh)
    if ph in HS:
     to,g,odd,touch=T[ph,k];assert to==head
     if not touch:pre.append((ph,g,odd))
    else:
     assert head in BOUND[oldh,k]
     pre.append((('OUT',oldh),1,0))
  REV[head,k]=pre
F={};VERS=[];FV={}
target_guard=T[(0,0,0),TARGET][1]
for c in contexts:
 if (c,TARGET) in CT:
  root=bb.intersect(target_guard,color_guard((0,0,0),c))
  if root:
   key=((0,0,0),c);F[key]=root;FV[key]=len(VERS);VERS.append((root,key,None,None,None))
queue=deque(F);queued=set(queue);iters=0;t0=time.time()
def member(root,color):
 while root>1:
  var,lo,hi=bb.nodes[root];root=hi if (color>>var)&1 else lo
 return bool(root)
def sample(root):
 color=0
 while root>1:
  var,lo,hi=bb.nodes[root]
  if lo:root=lo
  else:color|=1<<var;root=hi
 return color
def witness(key):
 color=sample(bb.intersect(F[key],SOURCE.get(key,0)));v=FV[key];steps=[]
 start=[key,color]
 while True:
  root,node,old,child,act=VERS[v];assert member(root,color)
  if act is None:break
  if old is not None and member(VERS[old][0],color):v=old;continue
  k,odd=act;nextkey=VERS[child][1];steps.append([node,nextkey,k,color,color^odd]);color^=odd;v=child
 out={'status':'Abstract backward witness, not a physical counterexample','start':start,'steps':steps,'final':VERS[v][1],'intermediate_word':''.join(x[2] for x in steps),'target':TARGET,'patch':P}
 path=Path(__file__).with_name('backward_witness_'+TARGET+'_'+str(len(P))+'_'+Path(PORT_FILE).stem+'.json');path.write_text(json.dumps(out,indent=2));print('WITNESS',out['intermediate_word']+TARGET,'file',path,flush=True)
while queue:
 key=queue.popleft();queued.remove(key);head,ctx=key;iters+=1
 if bb.intersect(F[key],SOURCE.get(key,0)):
  witness(key);print('ABSTRACT WITNESS BACKWARD',ALPHA,TARGET,R,q,'iterations',iters,'bddnodes',len(bb.nodes),'time',time.time()-t0,flush=True);break
 if len(bb.nodes)>LIMIT:print('CREATED NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
 for pc,k in RC[ctx]:
  for ph,guard,odd in REV[head,k]:
   root=bb.intersect(bb.flip(F[key],odd),guard)
   root=bb.intersect(root,color_guard(ph,pc))
   if not root:continue
   pkey=(ph,pc);old=F.get(pkey,0);new=bb.union(old,root)
   if new!=old:
    oldver=FV.get(pkey);FV[pkey]=len(VERS);VERS.append((new,pkey,oldver,FV[key],(k,odd)));F[pkey]=new
    if pkey not in queued:queued.add(pkey);queue.append(pkey)
else:print('EXCLUDED BACKWARD',ALPHA,TARGET,R,q,'cells',len(P),'heads',len(heads),'contexts',len(contexts),'iterations',iters,'bddnodes',len(bb.nodes),'fullcolorstates',sum(bb.count(v) for v in F.values()),'time',time.time()-t0,flush=True)
