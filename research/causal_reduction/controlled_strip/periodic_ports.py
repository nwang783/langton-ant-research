"""Search periodic external entry controllers on an initially white half-strip.
Finite survival is not an infinite certificate. Vertical exits reject; spatial
or step caps are UNKNOWN and retain the exact controller for further analysis.
"""
import sys,time,json,heapq,itertools,pathlib
from functools import lru_cache
HERE=pathlib.Path(__file__).resolve().parent
H=int(sys.argv[1]) if len(sys.argv)>1 else 12
DEPTH=int(sys.argv[2]) if len(sys.argv)>2 else 6
CAP=4096;XCAP=512;STEPCAP=200000
@lru_cache(maxsize=200000)
def visit(mask,y):
 x=0;dx=1;steps=0;mx=0
 while x>=0:
  i=x*H+y;a=1-2*((mask>>i)&1);mask^=1<<i;z=y-dx*a;steps+=1
  if z<0 or z>=H:return 'VERTICAL',mask,z,steps,mx
  j=x*H+z;b=1-2*((mask>>j)&1);mask^=1<<j;dx=-dx*a*b;y=z;x+=dx;steps+=1;mx=max(mx,x)
  if x>=XCAP or steps>=STEPCAP:return 'UNKNOWN',mask,y,steps,mx
 return 'LEFT',mask,y,steps,mx
best=[];tested=0;unknown=[];start=time.time();maxdepth=0

def evaluate(w,B):
 global tested,maxdepth
 tested+=1;seen={B};count=len(w);mx=(B.bit_length()+H-1)//H;steps=0;status='CAP'
 for j in range(CAP-len(w)):
  status,B,y,n,r=visit(B,w[j%len(w)]);steps+=n;mx=max(mx,r);count+=1
  if status!='LEFT':break
  # Full board repetition at this phase would contradict the finite-domain rank;
  # phase repetition is checked only at controller-period boundaries.
  if (j+1)%len(w)==0:
   if B in seen:raise AssertionError(('controlled finite-field cycle',w,B))
   seen.add(B)
 else:status='SURVIVAL_CAP'
 rec=dict(ports=w,excursions=count,max_x=mx,status=status,last_exit=y,board_hex=hex(B),steps_after_prefix=steps)
 key=(count,mx,w)
 if len(best)<20:heapq.heappush(best,(key,rec))
 elif key>best[0][0]:heapq.heapreplace(best,(key,rec))
 if status in('UNKNOWN','SURVIVAL_CAP'):unknown.append(rec);print('PROMISING',rec,flush=True)
 if count>maxdepth:maxdepth=count;print('BEST',count,mx,w,status,'tested',tested,flush=True)

def dfs(w,B):
 if w:evaluate(w,B)
 if len(w)==DEPTH:return
 for y in range(1,H,2):
  st,C,z,n,m=visit(B,y)
  if st=='LEFT':dfs(w+(y,),C)
  elif st=='UNKNOWN':unknown.append(dict(ports=w+(y,),status=st))

dfs((),0)
out=dict(height=H,max_controller_period=DEPTH,tested=tested,top=[r for k,r in sorted(best,reverse=True)],unknown=unknown,seconds=time.time()-start,cache=str(visit.cache_info()))
(HERE/f'periodic_ports_h{H}_k{DEPTH}.json').write_text(json.dumps(out,indent=2));print('DONE',tested,out['seconds'],out['cache'],flush=True)
