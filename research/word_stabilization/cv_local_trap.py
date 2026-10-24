"""Sound finite-patch overapproximation of old V nose reuse in CV words.
Outside cursor may reenter at any boundary state; no outside color constraints.
An abstract witness does NOT establish a physically feasible ant word.
An exhaustive failure to reach target would prove fixed-nose freshness for CV.
"""
import sys,collections,json
from verify_macro_word import D,rot
from cv_lattice import pose,occurrences
R=int(sys.argv[1]) if len(sys.argv)>1 else 2
CAP=int(sys.argv[2]) if len(sys.argv)>2 else 1000000
q=(1,2);P=[(x,y) for x in range(q[0]-R,q[0]+R+1) for y in range(q[1]-R,q[1]+R+1)];ix={p:i for i,p in enumerate(P)};qb=1<<ix[q]
# Every macro state that can read the patch is explicitly covered.
occ=[x for p in P for x in occurrences(p)]
loA=min(x[0] for x in occ)-1;hiA=max(x[0] for x in occ)+1;loB=min(x[1] for x in occ)-1;hiB=max(x[1] for x in occ)+1
states=[(a,b,h) for a in range(loA,hiA+1) for b in range(loB,hiB+1) for h in range(4)];si={s:i for i,s in enumerate(states)};out=len(states)
boundary=set();trans={};start=[]
for sid,(a,b,h) in enumerate(states):
 for k in 'CV':
  px,py=pose(a,b,h);seq=[]
  for z in D[k]['trace']:
   x,y=rot(z['p'],h);j=ix.get((px+x,py+y))
   if j is not None:seq.append((1<<j,z['c']=='L'))
  if k=='C':end=(a,b,(h-1)%4)
  else:
   da,db=[(1,0),(0,-1),(-1,0),(0,1)][h];end=(a+da,b+db,h)
  to=si.get(end,out)
  if to==out:boundary.add(si[(a,b,(h+2)%4)]) # reverse outside V enters this state
  trans[sid,k]=(to,seq)
  if any(bit==qb for bit,val in seq) and [val for bit,val in seq if bit==qb][-1]==False:
   known=val=0
   for bit,v in seq:known|=bit;val=(val|bit) if v else (val&~bit)
   start.append(((to,known,val),(sid,k)))
# Directed boundary formula verified by explicit predecessor outside.
boundary={si[(a,b,h)] for a,b,h in states if not (loA<=a-[1,0,-1,0][h]<=hiA and loB<=b-[0,-1,0,1][h]<=hiB)}
Q=collections.deque();prev={};src={}
for st,origin in start:
 if st not in prev:prev[st]=None;src[st]=origin;Q.append(st)
visited=0;goal=None
while Q:
 st=Q.popleft();sid,known,val=st;visited+=1
 if len(prev)>CAP:print('CAP',R,visited,len(prev),flush=True);break
 if sid==out:
  for to in boundary:
   ns=(to,known,val)
   if ns not in prev:prev[ns]=(st,'OUT');Q.append(ns)
  continue
 for k in 'CV':
  to,seq=trans[sid,k]
  isgoal=(states[sid]==(0,0,0) and k=='V')
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
else:print('EXCLUDED',R,visited,len(prev),flush=True)
if goal:
 st,k=goal;path=[(states[st[0]],k)]
 while prev[st] is not None:
  pst,k=prev[st];path.append(('OUT' if pst[0]==out else states[pst[0]],k));st=pst
 path.append((states[src[st][0]],src[st][1]));path.reverse()
 print('WITNESS',R,visited,len(prev),path,flush=True)
