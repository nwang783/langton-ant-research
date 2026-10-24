"""Conservative local last-R monitor for C-free U/V/Q/B words.
Exact new invariant: headings N/S and physical entry x+y=0 modulo4.
Unknown patch colors are retained explicitly. OUT allows arbitrary reentry.
A witness is abstract only. Non-goal blocks must have fresh marked inputs.
No-hit closure is conditional on this being the first macro with any reused
non-seam first-L input; all goal types must be excluded for a joint induction.
"""
from collections import deque
from pathlib import Path
import sys,json,time,os
from verify_macro_word import D,rot
A='UVQB';GOAL=sys.argv[1] if len(sys.argv)>1 else 'V';R=int(sys.argv[2])if len(sys.argv)>2 else 1
CAP=int(sys.argv[3])if len(sys.argv)>3 else 1000000
q=tuple(map(int,sys.argv[4:6]))if len(sys.argv)>5 else {'V':(1,2),'U':(0,3),'Q':(-4,-3),'B':(-3,-4)}[GOAL]
P=[(x,y)for x in range(q[0]-R,q[0]+R+1)for y in range(q[1]-R,q[1]+R+1)];ix={p:i for i,p in enumerate(P)};qb=1<<ix[q]
heads=set()
for p in P:
 for a in A:
  for h in(0,2):
   for z in D[a]['trace']:
    x,y=rot(z['p'],h);px,py=p[0]-x,p[1]-y
    if (px+py)%4==0:heads.add((px,py,h))
heads=sorted(heads);hi={p:i for i,p in enumerate(heads)};OUT=len(heads)
trans={};sources=[];reentry=set();markbits={}
seam={(0,0),(-1,-1),(0,-1),(1,0)}
MARKSETS=None
if os.environ.get('CFREE_MARKS'):
 MARKSETS={a:set(map(tuple,ps))for a,ps in json.load(open(os.environ['CFREE_MARKS'])).items()}
for sid,(px,py,h)in enumerate(heads):
 for a in A:
  dx,dy,dh=D[a]['end_pose'];dx,dy=rot((dx,dy),h);end=(px+dx,py+dy,(h+dh)%4)
  assert sum(end[:2])%4==0 and end[2]in(0,2)
  seq=[]
  for z in D[a]['trace']:
   xx,yy=rot(z['p'],h);bit=ix.get((px+xx,py+yy))
   if bit is not None:seq.append((1<<bit,z['c']=='L'))
  to=hi.get(end,OUT);trans[sid,a]=(to,seq)
  first={}
  for z in D[a]['trace']:first.setdefault(tuple(z['p']),z['c'])
  mb=0
  for local,c in first.items():
   if c!='L' or local in seam or MARKSETS is not None and local not in MARKSETS[a]:continue
   xx,yy=rot(local,h);bit=ix.get((px+xx,py+yy))
   if bit is not None:mb|=1<<bit
  markbits[sid,a]=mb
  if [v for b,v in seq if b==qb][-1:]==[False]:
   known=val=0
   for b,v in seq:known|=b;val=val|b if v else val&~b
   sources.append(((to,known,val),(sid,a)))
  ph=(h-dh)%4;dx,dy=rot(D[a]['end_pose'][:2],ph)
  if (px-dx,py-dy,ph)not in hi:reentry.add(sid)
sid=hi[(0,0,0)]
seq=[(1<<ix[tuple(z['p'])],z['c']=='L')for z in D['C']['trace']if tuple(z['p'])in ix]
trans[sid,'C']=(OUT,seq);markbits[sid,'C']=0
Q=deque();parent={};orig={};start=time.time()
for s,o in sources:
 if s not in parent:parent[s]=None;orig[s]=o;Q.append(s)
print('CONFIG',GOAL,q,'patch',len(P),'heads',len(heads),'sources',len(sources),'reentry',len(reentry),flush=True)
goal=None
while Q:
 s=Q.popleft();sid,known,val=s
 if len(parent)>CAP:print('CAP',len(parent),'pending',len(Q),'seconds',time.time()-start,flush=True);break
 if sid==OUT:
  for to in reentry:
   t=(to,known,val)
   if t not in parent:parent[t]=(s,'OUT');Q.append(t)
  continue
 for a in A+('C'if heads[sid]==(0,0,0)else''):
  to,seq=trans[sid,a];isgoal=heads[sid]==(0,0,0)and a==GOAL
  if not isgoal and (any(b==qb for b,v in seq)or known&markbits[sid,a]):continue
  nk,nv=known,val
  for b,v in seq:
   if nk&b and bool(nv&b)==v:break
   nk|=b;nv=nv|b if v else nv&~b
  else:
   if isgoal:goal=(s,a);break
   t=(to,nk,nv)
   if t not in parent:parent[t]=(s,a);Q.append(t)
 if goal:break
else:print('EXCLUDED',len(parent),'seconds',time.time()-start,flush=True)
if goal:
 s,a=goal;path=[(heads[s[0]],a)]
 while parent[s]is not None:
  old,a=parent[s];path.append(('OUT'if old[0]==OUT else heads[old[0]],a));s=old
 sid,a=orig[s];path.append((heads[sid],a));path.reverse()
 print('ABSTRACT WITNESS',len(parent),'seconds',time.time()-start,path,flush=True)
