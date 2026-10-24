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

coarse4=('C' not in ALPHA)
ORIENTS=range(4) if 'C' in ALPHA else ([0,2] if any(k in ALPHA for k in 'QB') else [0])
def coeff(x,y):
 if coarse4:
  if (y-3*x)%4:return None
  return x,(y-3*x)//4
 if coarse10:
  if (x+3*y)%10 or (-3*x+y)%10:return None
  return (x+3*y)//10,(-3*x+y)//10
 if (x+y)%2:return None
 return (x+y)//2,(x-y)//2

def pose(a,b,h):
 f=DIR[h];r=DIR[(h+1)%4];x,y=((a,3*a+4*b) if coarse4 else ((a-3*b,3*a+b) if coarse10 else (a+b,a-b)))
 return ((-1+2*x-f[0]+r[0])//2,(1+2*y-f[1]+r[1])//2,h)
def coord(x,y,h):
 f=DIR[h];r=DIR[(h+1)%4];X=(2*x+f[0]-r[0]+1)//2;Y=(2*y+f[1]-r[1]-1)//2;c=coeff(X,Y);assert c is not None;return (*c,h)
def trace(head,k):
 x,y,h=pose(*head);tr=[]
 for c in D[k]['word']:
  tr.append(((x,y),c=='L'));h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 return tr,coord(x,y,h)
zero={(h,k):trace((0,0,h),k) for h in ORIENTS for k in ALPHA};centers=set()
for qx,qy in P:
 for tr,end in zero.values():
  for (rx,ry),c in tr:
   v=coeff(qx-rx,qy-ry)
   if v is not None:centers.add(v)
# Rectangular compactification. Each extreme coordinate denotes an entire
# unbounded half-line, not one lattice point. Every far region misses P.
amin=min(a for a,b in centers);amax=max(a for a,b in centers)
bmin=min(b for a,b in centers);bmax=max(b for a,b in centers)
def isfar(head):
 a,b,h=head;return not(amin<=a<=amax and bmin<=b<=bmax)
def clip(a,b,h):return (max(amin-1,min(amax+1,a)),max(bmin-1,min(bmax+1,b)),h)
def dim_image(c,lo,hi,d):
 if lo<=c<=hi:return [max(lo-1,min(hi+1,c+d))]
 if c==lo-1:
  end=lo-1+d;return [lo-1]+list(range(lo,min(hi,end)+1))+([hi+1] if end>hi else [])
 assert c==hi+1
 start=hi+1+d;return ([lo-1] if start<lo else [])+list(range(max(lo,start),hi+1))+[hi+1]
heads=[(a,b,h) for a in range(amin-1,amax+2) for b in range(bmin-1,bmax+2) for h in ORIENTS]
print('COMPACT BOX',amin,amax,bmin,bmax,'heads',len(heads),flush=True)
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
 if isfar(head):return 1
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
T={};NEXT={};SOURCE={}
INCOMING={c:[] for c in contexts}
for (c,k),nc in CT.items():INCOMING[nc].append((c,k))
for head in heads:
 a,b,h=head
 for k in ALPHA:
  _,(da,db,eh)=zero[h,k]
  if isfar(head):
   T[head,k]=(1,0,False)
   NEXT[head,k]=[(aa,bb,eh) for aa in dim_image(a,amin,amax,da) for bb in dim_image(b,bmin,bmax,db)]
   continue
  tr,to=trace(head,k);NEXT[head,k]=[clip(*to)]
  seq=[(1<<ix[p],c) for p,c in tr if p in ix]
  known=black=odd=0
  for bit,c in seq:
   if not known&bit:known|=bit;black|=bit if c else 0
   else:assert bool((black^odd)&bit)==c
   odd^=bit
  guard=bb.cube(known,black);T[head,k]=(guard,odd,any(bit==qb for bit,c in seq))
  nr=[c for p,c in tr if p==q]
  if nr and not nr[-1]:
   to=NEXT[head,k][0]
   for (pc,letter),nc in CT.items():
    if letter!=k:continue
    pre=bb.intersect(guard,color_guard(head,pc))
    root=bb.intersect(bb.flip(pre,odd),color_guard(to,nc))
    key=(to,nc);SOURCE[key]=bb.union(SOURCE.get(key,0),root)
REV={(head,k):[] for head in heads for k in ALPHA}
for head in heads:
 for k in ALPHA:
  guard,odd,touch=T[head,k]
  if touch:continue
  for to in NEXT[head,k]:REV[to,k].append((head,guard,odd))
F={};target=(0,0,0);tg,to,tt=T[target,TARGET]
for c in contexts:
 if (c,TARGET) in CT:
  nc=CT[c,TARGET];dest=NEXT[target,TARGET][0]
  root=bb.intersect(tg,color_guard(target,c))
  root=bb.intersect(root,bb.flip(color_guard(dest,nc),to))
  if root:F[target,c]=root
queue=deque(F);queued=set(queue);iters=0;t0=time.time()
while queue:
 key=queue.popleft();queued.remove(key);head,ctx=key;iters+=1
 if bb.intersect(F[key],SOURCE.get(key,0)):
  print('ABSTRACT WITNESS COMPACT',ALPHA,TARGET,R,q,'iterations',iters,'bddnodes',len(bb.nodes),'time',time.time()-t0,flush=True);break
 if len(bb.nodes)>100000 and iters%500==0:
  before=len(bb.nodes);roots=list(F.values())+list(SOURCE.values())+list(G.values())+[x[0] for x in T.values()]
  mp=bb.collect(roots)
  F={h:mp[v] for h,v in F.items()};SOURCE={h:mp[v] for h,v in SOURCE.items()};G={h:mp[v] for h,v in G.items()}
  T={hk:(mp[g],odd,t) for hk,(g,odd,t) in T.items()}
  REV={hk:[(ph,mp[g],odd) for ph,g,odd in prev] for hk,prev in REV.items()}
  print('GC',iters,before,'->',len(bb.nodes),'elapsed',round(time.time()-t0,1),flush=True)
  if len(bb.nodes)>LIMIT:print('LIVE NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
 for pc,k in INCOMING[ctx]:
  for ph,guard,odd in REV[head,k]:
   root=bb.intersect(bb.flip(F[key],odd),guard)
   root=bb.intersect(root,color_guard(ph,pc))
   if not root:continue
   pkey=(ph,pc);old=F.get(pkey,0);new=bb.union(old,root)
   if new!=old:
    F[pkey]=new
    if pkey not in queued:queued.add(pkey);queue.append(pkey)
else:print('EXCLUDED COMPACT',ALPHA,TARGET,R,q,'cells',len(P),'heads',len(heads),'contexts',len(contexts),'iterations',iters,'bddnodes',len(bb.nodes),'fullcolorstates',sum(bb.count(v) for v in F.values()),'time',time.time()-t0,flush=True)
