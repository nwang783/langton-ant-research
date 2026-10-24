"""Exact bounded-period dense-to-sparse westgoing rail-front enumeration.

This is a periodic-background transducer problem, NOT a finite-support
counterexample. All binary necklaces of each even period are considered;
heading and vertical offsets are solved without a finite-board truncation.
"""
import json,sys,time
from collections import defaultdict,Counter
from loop_decoration_solver import walk,HERE

def necklaces(n):
 a=[0]*(n+1)
 def rec(t,p):
  if t>n:
   if n%p==0:yield ''.join('RL'[z] for z in a[1:])
  else:
   a[t]=a[t-p];yield from rec(t+1,p)
   for j in range(a[t-p]+1,2):a[t]=j;yield from rec(t+1,t)
 yield from rec(1,1)

def dense(x,y):return y in (0,-2) or (y==-1 and x%2==1)
def sparse(x,y):return y==-1 and x%2==1

def check(w):
 ev,end=walk(w);x,y,h=end
 if h or (x==0)==(y==0):return []
 p=abs(x+y)
 if p%2 or w.count('R')-w.count('L')!=-2*p:return []
 # Rotate the nonzero axial displacement to west.
 for h in range(4):
  es,en=walk(w,(0,0,h))
  if en[:2]==(-p,0):break
 groups=defaultdict(list)
 for i,((x,y),hh,c) in enumerate(es):groups[(x%p,y)].append((-(x//(-p)),i,c,x))
 for g in groups.values():g.sort()
 lo=min(q[1] for q in groups);hi=max(q[1] for q in groups);valid=[]
 for dy in range(-hi,-2-lo+1):
  # All and only the two solid rails must have odd visit parity.
  odd={(r,y+dy) for (r,y),g in groups.items() if len(g)%2}
  if odd!={(r,y) for r in range(p) for y in (0,-2)}:continue
  for sigma in (0,1):
   dx=(sigma-dy-h)%2
   good=True
   for (r,y),g in groups.items():
    c=bool(dense(r+dx,y+dy))
    for _,i,turn,x in g:
     if c!=(turn=='L'):good=False;break
     c=not c
    if not good or c!=bool(sparse(r+dx,y+dy)):
     good=False;break
   if good:valid.append(dict(word=w,pose=[dx,dy,h],sector=sigma,drift=[-p,0],period=len(w)))
 return valid

if __name__=='__main__':
 hi=int(sys.argv[1]) if len(sys.argv)>1 else 24;out=[];t=time.time()
 controls=check('RLLLLRLL');assert any(r['sector']==1 for r in controls) and not any(r['sector']==0 for r in controls)
 print('CONTROL',json.dumps(controls),flush=True)
 for n in range(2,hi+1,2):
  start=time.time();cnt=Counter();sol=[]
  for w in necklaces(n):
   cnt['necklaces']+=1
   for v in check(w):sol.append(v);cnt['valid_sector'+str(v['sector'])]+=1;print('FRONT',json.dumps(v),flush=True)
  r=dict(length=n,counts=dict(cnt),fronts=sol,seconds=time.time()-start);out.append(r);print('LENGTH',json.dumps(r),flush=True)
  (HERE/f'reverse_rail_fronts_{hi}.json').write_text(json.dumps(dict(seconds=time.time()-t,results=out),indent=2))
