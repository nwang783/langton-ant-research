"""Generalized finite-patch last-writer overapproximation for C/U/V macro words.
Independent extension of cv_local_trap.py; a WITNESS is abstract, not a real word.
The reachable center lattice is {(x,y): x+y even}, relative to (-1/2,1/2).
"""
import sys, collections, json, time
D=json.load(open('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'))
ALPH=sys.argv[1] if len(sys.argv)>1 else 'CUV'
GOAL=sys.argv[2] if len(sys.argv)>2 else 'V'
R=int(sys.argv[3]) if len(sys.argv)>3 else 1
CAP=int(sys.argv[4]) if len(sys.argv)>4 else 1000000
q=(int(sys.argv[5]),int(sys.argv[6])) if len(sys.argv)>6 else {'V':(1,2),'U':(0,2),'Q':(0,2),'B':(0,2)}[GOAL]
def rot(p,h):
 x,y=p
 for _ in range(h): x,y=y,-x
 return x,y
p0=[(0,0),(-1,0),(-1,1),(0,1)]
shift={'C':(0,0),'V':(1,3),'U':(0,4),'Q':(-3,-5),'B':(-2,-6)}
turn={'C':3,'V':0,'U':0,'Q':2,'B':2}
P=[(x,y) for x in range(q[0]-R,q[0]+R+1) for y in range(q[1]-R,q[1]+R+1)]
ix={p:i for i,p in enumerate(P)};qb=1<<ix[q]
occ=[]
for x,y in P:
 for k in ALPH:
  for h in range(4):
   for z in D[k]['trace']:
    dx,dy=rot(z['p'],h)
    cx,cy=x-dx-p0[h][0],y-dy-p0[h][1]
    if (cx+cy)%2==0: occ.append((cx,cy,h))
loX=min(x[0] for x in occ)-1;hiX=max(x[0] for x in occ)+1
loY=min(x[1] for x in occ)-1;hiY=max(x[1] for x in occ)+1
states=[(x,y,h) for x in range(loX,hiX+1) for y in range(loY,hiY+1) if (x+y)%2==0 for h in range(4)]
si={s:i for i,s in enumerate(states)};out=len(states)
trans={};start=[];boundary=set()
for sid,(cx,cy,h) in enumerate(states):
 px,py=cx+p0[h][0],cy+p0[h][1]
 for k in ALPH:
  seq=[]
  for z in D[k]['trace']:
   x,y=rot(z['p'],h);j=ix.get((px+x,py+y))
   if j is not None: seq.append((1<<j,z['c']=='L'))
  dx,dy=rot(shift[k],h); to=si.get((cx+dx,cy+dy,(h+turn[k])%4),out)
  trans[sid,k]=(to,seq)
  if any(bit==qb for bit,val in seq) and [val for bit,val in seq if bit==qb][-1]==False:
   known=val=0
   for bit,v in seq: known|=bit;val=(val|bit) if v else (val&~bit)
   start.append(((to,known,val),(sid,k)))
  ph=(h-turn[k])%4; dx,dy=rot(shift[k],ph)
  if (cx-dx,cy-dy,ph) not in si: boundary.add(sid)
Q=collections.deque();prev={};src={}
for st,origin in start:
 if st not in prev: prev[st]=None;src[st]=origin;Q.append(st)
visited=0;goal=None;beg=time.time()
print('CONFIG',ALPH,GOAL,R,'patch',len(P),'poses',len(states),'boundary',len(boundary),'starts',len(start),flush=True)
while Q:
 st=Q.popleft();sid,known,val=st;visited+=1
 if len(prev)>CAP: print('CAP',visited,len(prev),'seconds',time.time()-beg,flush=True);break
 if sid==out:
  for to in boundary:
   ns=(to,known,val)
   if ns not in prev: prev[ns]=(st,'OUT');Q.append(ns)
  continue
 for k in ALPH:
  to,seq=trans[sid,k];isgoal=(states[sid]==(0,0,0) and k==GOAL)
  if not isgoal and any(bit==qb for bit,v in seq):continue
  nk,nv=known,val;valid=True
  for bit,v in seq:
   if nk&bit and bool(nv&bit)==v:valid=False;break
   nk|=bit;nv=(nv|bit) if v else (nv&~bit)
  if not valid:continue
  if isgoal:goal=(st,k);break
  ns=(to,nk,nv)
  if ns not in prev:prev[ns]=(st,k);Q.append(ns)
 if goal:break
else:print('EXCLUDED',visited,len(prev),'seconds',time.time()-beg,flush=True)
if goal:
 st,k=goal;path=[(states[st[0]],k)]
 while prev[st] is not None:
  pst,k=prev[st];path.append(('OUT' if pst[0]==out else states[pst[0]],k));st=pst
 path.append((states[src[st][0]],src[st][1]));path.reverse()
 print('WITNESS',visited,len(prev),'seconds',time.time()-beg,path,flush=True)
