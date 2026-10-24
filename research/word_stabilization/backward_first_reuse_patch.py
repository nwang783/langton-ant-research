"""Backward local first-marked-reuse overapproximation.
Marked inputs in earlier macros prohibit every still-earlier patch read.
Forbidden-past cells need no retained current-color constraint: their initial
black color can be chosen freely, and no earlier macro is allowed to read them.
This is research code pending independent audit; abstract witnesses are not physical.
"""
from collections import deque,defaultdict
from pathlib import Path
import sys,json,time,os
from verify_macro_word import D,rot
A=os.environ.get('MACRO_ALPHABET','CUVQB');GOAL=sys.argv[1]if len(sys.argv)>1 else'V';R=int(sys.argv[2])if len(sys.argv)>2 else 2
CAP=int(sys.argv[3])if len(sys.argv)>3 else 1000000
q=tuple(map(int,sys.argv[4:6]))if len(sys.argv)>5 else{'V':(1,2),'U':(0,3),'Q':(-4,-3),'B':(-3,-4)}[GOAL]
P=[(x,y)for x in range(q[0]-R,q[0]+R+1)for y in range(q[1]-R,q[1]+R+1)];ix={p:i for i,p in enumerate(P)};qb=1<<ix[q]
seam={(0,0),(-1,-1),(0,-1),(1,0)};S={}
for a in A:
 first={}
 for z in D[a]['trace']:first.setdefault(tuple(z['p']),z['c'])
 S[a]={p for p,c in first.items()if c=='L'and p not in seam}if a!='C'else set()
if os.environ.get('FRESH_MARKS'):
 S.update({a:set(map(tuple,p))for a,p in json.load(open(os.environ['FRESH_MARKS'])).items()})
cfree='C'not in A;H=(0,2)if cfree else range(4)
def allowed(px,py,h):return (px+py)%4==0 if cfree else(px+py-h)%2==0
heads=set()
for p in P:
 for a in A:
  for h in H:
   for z in D[a]['trace']:
    dx,dy=rot(z['p'],h);px,py=p[0]-dx,p[1]-dy
    if allowed(px,py,h):heads.add((px,py,h))
heads=sorted(heads);hi={p:i for i,p in enumerate(heads)};OUT=len(heads);incoming=defaultdict(list);empty_predecessors=set();data={}
for sid,(px,py,h)in enumerate(heads):
 for a in A:
  first={};last={};mb=0
  for z in D[a]['trace']:
   dx,dy=rot(z['p'],h);j=ix.get((px+dx,py+dy))
   if j is not None:first.setdefault(1<<j,z['c']=='L');last[1<<j]=z['c']=='L'
  mask=sum(first);pre=sum(b for b,c in first.items()if c);post=sum(b for b,c in last.items()if not c)
  for p in S[a]:
   dx,dy=rot(p,h);j=ix.get((px+dx,py+dy))
   if j is not None:mb|=1<<j
  dx,dy,dh=D[a]['end_pose'];dx,dy=rot((dx,dy),h);to=hi.get((px+dx,py+dy,(h+dh)%4),OUT)
  islastR=bool(mask&qb and post&qb)
  row=(sid,a,mask,pre,post,mb,islastR);incoming[to].append(row);data[sid,a]=row
  ph=(h-dh)%4;dx,dy=rot(D[a]['end_pose'][:2],ph)
  if (px-dx,py-dy,ph)not in hi:empty_predecessors.add(sid)
sid=hi[0,0,0];_,_,known,val,_,_,_=data[sid,GOAL];start=(sid,known,val,0)
Q=deque([start]);parent={start:None};beg=time.time();hit=None;processed=0
print('CONFIG',A,GOAL,q,'patch',len(P),'heads',len(heads),'markers',sum(map(len,S.values())),flush=True)
while Q:
 s=Q.popleft();sid,known,val,forbid=s;processed+=1
 if len(parent)>CAP:print('CAP',len(parent),'pending',len(Q),'seconds',time.time()-beg,flush=True);break
 for old,a,mask,pre,post,mb,islastR in incoming[sid]:
  if mask&forbid or (val^post)&known&mask:continue
  if islastR:hit=(s,old,a);break
  if mask&qb:continue
  nf=forbid|mb;nk=(known|mask)&~nf;nv=((val&~mask)|pre)&nk;t=(old,nk,nv,nf)
  if t not in parent:parent[t]=(s,a);Q.append(t)
 if hit:break
 if sid in empty_predecessors:
  t=(OUT,known,val,forbid)
  if t not in parent:parent[t]=(s,'OUT');Q.append(t)
else:print('EXCLUDED',len(parent),'seconds',time.time()-beg,flush=True)
if hit:
 s,old,a=hit;path=[(heads[old],a)]
 while parent[s]is not None:
  after,a=parent[s];path.append(('OUT'if s[0]==OUT else heads[s[0]],a));s=after
 path.append((heads[s[0]],GOAL));print('ABSTRACT WITNESS',len(parent),'seconds',time.time()-beg,path,flush=True)
