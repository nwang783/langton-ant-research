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
SOURCES={}
F={};initial={};T={};BOUND={(h,k):[] for h in range(4) for k in ALPHA}
def put_initial(head,ctx,root,origin):
 root=bb.intersect(root,color_guard(head,ctx))
 if root:
  key=(head,ctx);initial[key]=bb.union(initial.get(key,0),root);SOURCES.setdefault(key,[]).append((root,origin))

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
   for ctx in SOURCE_CTX[k]:put_initial(to,ctx,root,(head,k))
  for oldh in range(4):
   _,(da,db,endh)=zero[oldh,k]
   if endh==h and (a-da,b-db) not in centers:BOUND[oldh,k].append(head)
# Version DAG retains a constructive abstract path for every added color.
F=dict(initial);versions=[];VID={}
for key,root in F.items():
 VID[key]=len(versions);versions.append((key,root,None))
def pick(root):
 color=0
 while root>=2:
  v,l,h=bb.nodes[root]
  if l:root=l
  else:color|=1<<v;root=h
 assert root==1
 return color

def witness(key,color):
 ver=VID[key];back=[]
 while True:
  key,root,event=versions[ver]
  assert bb.evaluate(root,color)
  if event is None:
   source=next(origin for r,origin in SOURCES[key] if bb.evaluate(r,color))
   sh,sk=source
   back.append({'from':sh,'to':key[0],'macro':sk,'color_after':color,'source':True})
   break
  old,src,k=event
  if old is not None and bb.evaluate(versions[old][1],color):ver=old;continue
  skey,sroot,_=versions[src]
  back.append({'from':skey[0],'to':key[0],'macro':k,'color_after':color,'source':False})
  if skey[0][0]!='OUT':color^=T[skey[0],k][2]
  assert bb.evaluate(sroot,color)
  ver=src
 steps=list(reversed(back));word=''.join(x['macro'] for x in steps)+TARGET
 actual=tuple(steps[0]['from']);mismatches=[]
 for i,step in enumerate(steps):
  tr,actual=trace(actual,step['macro'])
  expected=tuple(step['to'])
  if expected[0]!='OUT' and actual!=expected:mismatches.append([i,actual,expected])
 print('ABSTRACT WORD',word,'steps',len(steps),'POSE MISMATCHES',mismatches,flush=True)
 out={'alphabet':ALPHA,'target':TARGET,'q':q,'patch':P,'word':word,'steps':steps,'mismatches':mismatches}
 path='/workspace/shared/langton/word_stabilization/abstract_witness_'+TARGET+'_'+str(len(P))+'.json'
 json.dump(out,open(path,'w'),indent=2)
 print('SAVED',path,flush=True)

queue=deque(F);queued=set(queue);iters=0;t0=time.time()
while queue:
 key=queue.popleft();queued.remove(key);head,ctx=key;iters+=1;svid=VID[key];source_root=F[key]
 if len(bb.nodes)>LIMIT:
  print('NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
 images=[]
 for k in ALPHA:
  nc=CT.get((ctx,k))
  if nc is None:continue
  if head[0]=='OUT':
   oldh=head[1];_,(_,_,newh)=zero[oldh,k]
   images.append(((('OUT',newh),nc),source_root,k))
   images.extend(((to,nc),source_root,k) for to in BOUND[oldh,k])
  else:
   to,guard,odd,touches=T[head,k];target=head==(0,0,0) and k==TARGET
   if touches and not target:continue
   pre=bb.intersect(source_root,guard)
   if target and pre:
    print('ABSTRACT WITNESS',ALPHA,TARGET,R,q,'iterations',iters,'bddnodes',len(bb.nodes),'time',time.time()-t0,flush=True)
    witness(key,pick(pre));break
   if pre:images.append(((to,nc),bb.flip(pre,odd),k))
 else:
  for to,img,k in images:
   img=bb.intersect(img,color_guard(*to))
   if not img:continue
   old=F.get(to,0);new=bb.union(old,img)
   if new!=old:
    oldvid=VID.get(to);VID[to]=len(versions);versions.append((to,new,(oldvid,svid,k)));F[to]=new
    if to not in queued:queued.add(to);queue.append(to)
  continue
 break
else:print('EXCLUDED',ALPHA,TARGET,R,q,'cells',len(P),'heads',len(heads),'contexts',len(contexts),'iterations',iters,'bddnodes',len(bb.nodes),'fullcolorstates',sum(bb.count(v) for v in F.values()),'time',time.time()-t0,flush=True)
