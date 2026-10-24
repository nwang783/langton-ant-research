"""Conservative local last-R monitor for C-free U/V/Q/B words.
Exact new invariant: headings N/S and physical entry x+y=0 modulo4.
Unknown patch colors are retained explicitly. OUT allows arbitrary reentry.
A witness is abstract only. Non-goal blocks must have fresh marked inputs.
Uses the unconditional29 C-free fresh inputs and the independently proved
C-free boundary-center self-avoidance theorem. The terminal P C suffix
is fixed, so all earlier starts avoid both its known boundary centers.
"""
from collections import deque
from pathlib import Path
import sys,json,time,os
from verify_macro_word import D,rot,check
A='UVQB';T=sys.argv[1] if len(sys.argv)>1 else 'V';GOAL='C'
R=int(sys.argv[2])if len(sys.argv)>2 else 2;CAP=int(sys.argv[3])if len(sys.argv)>3 else 1000000
q=(-1,0)
h=(-D[T]['end_pose'][2])%4;dx,dy=rot(D[T]['end_pose'][:2],h);target=(-dx,-dy,h)
def center(p):
 x,y,h=p;dx,dy=rot((-1,1),h);return(2*x+dx,2*y+dy)
forbidden_centers={(-1,1),center(target)}
P=[(x,y)for x in range(q[0]-R,q[0]+R+1)for y in range(q[1]-R,q[1]+R+1)];ix={p:i for i,p in enumerate(P)};qb=1<<ix[q]
heads=set()
for p in P:
 for a in A:
  for h in(0,2):
   for z in D[a]['trace']:
    x,y=rot(z['p'],h);px,py=p[0]-x,p[1]-y
    if (px+py)%4==0:heads.add((px,py,h))
for cx,cy in forbidden_centers:
 for h in(0,2):
  dx,dy=rot((-1,1),h);heads.add(((cx-dx)//2,(cy-dy)//2,h))
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
  if [v for b,v in seq if b==qb][-1:]==[False] and center((px,py,h))not in forbidden_centers:
   known=val=0
   for b,v in seq:known|=b;val=val|b if v else val&~b
   sources.append(((to,known,val),(sid,a)))
  ph=(h-dh)%4;dx,dy=rot(D[a]['end_pose'][:2],ph)
  if (px-dx,py-dy,ph)not in hi:reentry.add(sid)
goal_sid=hi[target]
assert not any(b==qb for b,v in trans[goal_sid,T][1])
cseq=[(1<<ix[tuple(z['p'])],z['c']=='L')for z in D['C']['trace']if tuple(z['p'])in ix]
bad=json.load(open(os.environ.get('EXTRA_FORBIDDEN','literal_short_grammar_6.json')))['forbidden']
for w in bad:
 try:check(w)
 except AssertionError:pass
 else:raise AssertionError(('invalid forbidden factor',w))
prefix=sorted({w[:i]for w in bad for i in range(len(w))},key=lambda w:(len(w),w));pi={p:i for i,p in enumerate(prefix)};gtrans={}
for g,p in enumerate(prefix):
 for a in A+'C':
  w=p+a;gtrans[g,a]=-1 if any(w.endswith(b)for b in bad)else pi[max((z for z in prefix if w.endswith(z)),key=len)]
Q=deque();parent={};orig={};start=time.time()
for s,o in sources:
 s=(*s,gtrans[0,o[1]])
 if s not in parent:parent[s]=None;orig[s]=o;Q.append(s)
print('CONFIG',T+'C',q,'patch',len(P),'heads',len(heads),'sources',len(sources),'reentry',len(reentry),flush=True)
goal=None
while Q:
 s=Q.popleft();sid,known,val,g=s
 if len(parent)>CAP:print('CAP',len(parent),'pending',len(Q),'seconds',time.time()-start,flush=True);break
 if sid==OUT:
  for a in A:
   ng=gtrans[g,a]
   if ng>=0:
    t=(sid,known,val,ng)
    if t not in parent:parent[t]=(s,'OUT'+a);Q.append(t)
  for to in reentry:
   t=(to,known,val,g)
   if t not in parent:parent[t]=(s,'OUT');Q.append(t)
  continue
 for a in A:
  isgoal=sid==goal_sid and a==T
  if not isgoal and center(heads[sid])in forbidden_centers:continue
  ng=gtrans[g,a]
  if ng<0:continue
  if isgoal:
   ng=gtrans[ng,'C']
   if ng<0:continue
  to,seq=trans[sid,a]
  if any(b==qb for b,v in seq)or known&markbits[sid,a]:continue
  if isgoal:seq=seq+cseq
  nk,nv=known,val
  for b,v in seq:
   if nk&b and bool(nv&b)==v:break
   nk|=b;nv=nv|b if v else nv&~b
  else:
   if isgoal:goal=(s,a);break
   t=(to,nk,nv,ng)
   if t not in parent:parent[t]=(s,a);Q.append(t)
 if goal:break
else:print('EXCLUDED',len(parent),'seconds',time.time()-start,flush=True)
if goal:
 s,a=goal;path=[(heads[s[0]],a+'C')]
 while parent[s]is not None:
  old,a=parent[s];path.append(('OUT'if old[0]==OUT else heads[old[0]],a));s=old
 sid,a=orig[s];path.append((heads[sid],a));path.reverse()
 print('ABSTRACT WITNESS',len(parent),'seconds',time.time()-start,path,flush=True)
