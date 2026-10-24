"""Complete finite checks for the heading-free scale-nine record obstruction.
All initial colors are free except explicitly pristine y>=0 in the record pair.
No import from the general inflation search or its inventories.
"""
import itertools,json,pathlib,collections
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0));A='RRLRRRRLR'
def read(w,H=0,origin=(0,0)):
 x,y=origin;events=[]
 for z in w:
  events.append((x,y,H,z));H=(H+(1 if z=='R'else-1))%4;dx,dy=D[H];x+=dx;y+=dy
 return events,(x,y,H)
def legal(events,white_upper=False):
 last={}
 for x,y,h,z in events:
  if last.get((x,y))==z:return False
  if white_upper and (x,y)not in last and y>=0 and z=='L':return False
  last[x,y]=z
 return True
words=[''.join(w)for w in itertools.product('RL',repeat=9)if legal(read(''.join(w))[0])]
inv=[]
for Hc in range(4):
 for c in 'RL':
  dx,dy=D[(Hc+(1 if c=='R'else-1))%4];target=3*dx,3*dy
  for Hf in range(4):
   if (Hf-Hc)%2:continue
   for w in words:
    events,end=read(w,Hf)
    if end[:2]!=target:continue
    top=max(y for x,y,h,z in events)
    assert top<=4 and (dy==1 or top<=2)
    inv.append(dict(Hc=Hc,c=c,Hf=Hf,word=w,top=top,dy=dy))
assert len(inv)==240
pairs=[]
for Hf in (1,3):
 for u in words:
  e,end=read(u,Hf,(0,-3))
  if end[:2]!=(0,0):continue
  for v in words:
   f,end2=read(v,end[2])
   if end2[:2]!=(3,0):continue
   if not legal(e+f,white_upper=True):continue
   assert end[2]==0 and v==A
   assert max(y for x,y,h,z in e)<0
   pairs.append(dict(previous_heading=Hf,previous_word=u,record_heading=end[2],record_word=v))
assert len(pairs)==6
# Exhaust every nine-macro refinement of coarse A with the same first image A.
coarse,ep=read(A);coarse_poses=[(x,y,h)for x,y,h,c in coarse]+[ep]
last={};nodes=collections.Counter();conflicts=0;leaves=[]
def dfs(n,H,chosen):
 global conflicts
 nodes[n]+=1
 if n==9:leaves.append(chosen);return
 x,y,h=coarse_poses[n];tx,ty,th=coarse_poses[n+1]
 for w in ([A]if n==0 else words):
  events,end=read(w,H,(3*x,3*y))
  if end[:2]!=(3*tx,3*ty):continue
  undo=[];okay=True
  for X,Y,hh,z in events:
   old=last.get((X,Y))
   if old==z:conflicts+=1;okay=False;break
   undo.append(((X,Y),old));last[X,Y]=z
  if okay:dfs(n+1,end[2],chosen+[w])
  for p,old in reversed(undo):
   if old is None:del last[p]
   else:last[p]=old

dfs(0,0,[])
assert not leaves
result=dict(internally_legal_words=len(words),oriented_inventory_count=len(inv),top_bound=4,non_north_top_bound=2,record_pairs=pairs,root_word=A,root_refinement_status='EXHAUSTED',nodes_by_depth=dict(nodes),nodes=sum(nodes.values()),chronology_conflicts=conflicts,full_refinements=0)
(HERE/'position_k9_record_certificate.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
