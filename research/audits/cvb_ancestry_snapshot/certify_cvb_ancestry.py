"""Explicit complete-color checker for C/V/B genealogy restrictions.
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
P=[(x,y) for x in range(0,3) for y in range(-1,2)];IX={q:i for i,q in enumerate(P)};q=(1,0);QB=1<<IX[q]

def coeff(x,y):
 if (x+3*y)%10 or (-3*x+y)%10:return None
 return ((x+3*y)//10,(-3*x+y)//10)
def pose(head):
 a,b,h=head;f=DIR[h];r=DIR[(h+1)%4]
 return ((-1+2*a-6*b-f[0]+r[0])//2,(1+6*a+2*b-f[1]+r[1])//2,h)
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
BOUNDARY=set();TRANS={};INITIAL_BAD=set();INITIAL_C11=set();ALLOWED={('C',11),('V',14),('B',70)}
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
    target=head==(0,0,0) and m in 'CV' and (flag or not separated)
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
    to,known,black,odd,touches=TRANS[head,m];target=head==(0,0,0) and m in 'CV' and (flag or not separated)
    if color&known!=black:continue
    assert not target
    if not touches:assert (to,color^odd,int(flag or m!='C') if separated else 0) in reached
 return reached
BAD=closure(INITIAL_BAD,False);SEP=closure(INITIAL_C11,True)

def same_cell_conflict(w):
 x=y=h=0;last={};t=0
 for m in w:
  for c in WORDS[m]:
   q=(x,y)
   if q in last and last[q][1]==c:return dict(cell=q,earlier=last[q][0],later=t,letter=c)
   last[q]=(t,c);h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy;t+=1
 return None
CONFLICT_WORDS=['CCB','CCCB']+[a+'C'*k+'B' for a in 'VB' for k in range(4)]+['CCCC'+m for m in WORDS]+[a+'CCC'+'V' for a in 'VB']+[a+'CCCC' for a in 'VB']
CONFLICTS={w:same_cell_conflict(w) for w in CONFLICT_WORDS};assert all(CONFLICTS.values())
# Geometry-only producer restrictions for positive child nodes in C/V.
# Child4 can have no positive child in a later C/V macro; child11 is internal.
for source in 'CV':
 tr,_=ZERO[0,source]
 assert tr[4]==((0,0),'R')
 for target in 'CV':
  targettr,_=ZERO[0,target]
  first={}
  for j,(cell,c) in enumerate(targettr):first.setdefault(cell,j)
  for j,(cell,c) in enumerate(targettr):
   if c!='L' or j+1>=len(targettr) or targettr[j+1][1]!='R' or first[cell]!=j:continue
   for h in range(4):
    srctr,_=ZERO[h,source];sq=srctr[4][0];assert coeff(cell[0]-sq[0],cell[1]-sq[1]) is None

# A V11 token cannot be the input of a later C/V node4 either.
for target in 'CV':
 cell=ZERO[0,target][0][3][0]
 for h in range(4):
  tr,_=ZERO[h,'V']
  for i in (11,12):
   sq=tr[i][0];assert coeff(cell[0]-sq[0],cell[1]-sq[1]) is None

def forest(w):
 x=y=h=0;last={};tokens={};parent=[None];depth=[0];node=0;meta=[('entry',0)];r=[0];at=0
 for m in w:
  for i,c in enumerate(WORDS[m]):
   q=(x,y);assert q not in last or last[q]!=c;last[q]=c
   if c=='R':tokens[q]=node;r[node]+=1
   else:
    par=tokens.pop(q,None);node=len(parent);parent.append(par);depth.append(0 if par is None else depth[par]+1);meta.append((m,i+1));r.append(0)
   h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy;at+=1
 return dict(parent=parent,depth=depth,meta=meta,r=r,tokens=tokens)
PREFIX={}
for w in ['B','CB']:
 f=forest(w);assert max(d for d,r in zip(f['depth'],f['r']) if r)>0
 assert max(d for d,r in zip(f['depth'],f['r']) if r)<=4
 assert all(f['depth'][i]==0 for i,z in enumerate(f['meta']) if z==('B',70))
 PREFIX[w]=dict(max_depth=max(f['depth']),max_positive_depth=max(d for d,r in zip(f['depth'],f['r']) if r),B70_depth=0)
WIT=forest('CCCVV');assert max(WIT['depth'])==8
out=dict(status='Finite local exclusion certificate; combine with audited V-tip freshness for depth theorem.',patch=P,heads=len(HEADS),bad_initial=len(INITIAL_BAD),bad_reachable=len(BAD),separated_initial=len(INITIAL_C11),separated_reachable=len(SEP),allowed_cross_producer_nodes=sorted(ALLOWED),short_conflicts=CONFLICTS,prefix_checks=PREFIX,sharp_depth_witness='CCCVV',
 bad_closure=sorted(BAD,key=lambda t:(str(t[0]),t[1],t[2])),separated_closure=sorted(SEP,key=lambda t:(str(t[0]),t[1],t[2])))
Path(__file__).with_name('cvb_ancestry_certificate.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if 'closure' not in k},indent=2))
