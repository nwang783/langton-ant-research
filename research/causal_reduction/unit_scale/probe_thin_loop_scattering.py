"""Targeted minimum-width corridor controls, with exact finite-board104-tail tests.
Not an all-parameter theorem. The complete loop output is never discarded.
"""
from pathlib import Path
import json
from unequal_loop_geometry import execute,H,step
from certify_highway_wake_reflector import trace
P=Path(__file__).resolve().parent

def tail_guard(w,h):
 rr,d,h1=trace(w,(0,0),h);assert h1==h and abs(d[0])==abs(d[1])==2
 def key(q):
  # Remove an integral multiple of d, making x 0 or1.
  n=q[0]//d[0] if d[0]>0 else -((-q[0]+1)//2)
  # the direct floor qx/2 gauge is simpler regardless of the sign.
  n=(q[0]//2)*(1 if d[0]>0 else -1)
  return(q[0]-n*d[0],q[1]-n*d[1]),n
 orbits={}
 for j,(q,hh,c)in enumerate(rr):
  a,n=key(q);orbits.setdefault(a,[]).append((n,j-104*n,c))
 black=set();starts={}
 for a,L in orbits.items():
  lo=min(n for n,t,c in L);hi=max(n for n,t,c in L);starts[a]=lo
  for k in range(lo,hi+1):
   first=min((t,c)for n,t,c in L if n<=k)
   if first[1]=='L':black.add((a[0]+k*d[0],a[1]+k*d[1]))
  assert min((t,c)for n,t,c in L)[1]=='R'
 return d,key,starts,black
G={(phase,h):tail_guard(H[phase:]+H[:phase],h)for phase in range(104)for h in range(4)}
R={H[i:]+H[:i]:i for i in range(104)}
def check(B,p,phase,h):
 d,key,starts,required=G[phase,h]
 if any((p[0]+q[0],p[1]+q[1])not in B for q in required):return False
 for x,y in B:
  q=(x-p[0],y-p[1]);a,n=key(q)
  if a in starts and n>=starts[a] and q not in required:return False
 return True

def run(r,s,limit=300000):
 B=execute(r,s);p=(0,0);h=0;chars=[];samples=[]
 for t in range(limit):
  p,h,c=step(B,p,h);chars.append(c)
  if len(chars)>=104 and t%104==0:
   last=''.join(chars[-104:]);phase=R.get(last)
   if phase is not None:
    good=check(B,p,phase,h)
    if not samples or samples[-1]['phase']!=phase or samples[-1]['h']!=h:samples.append(dict(t=t+1,p=p,h=h,phase=phase,exact_tail=good))
    if good:return dict(r=r,s=s,status='EXACT_LITERAL_TAIL',time=t+1,pose=[p,h],phase=phase,mass=len(B),segments=samples,word=''.join(chars))
 return dict(r=r,s=s,status='UNKNOWN_HORIZON',time=limit,pose=[p,h],mass=len(B),segments=samples,word=''.join(chars))
if __name__=='__main__':
 out=[]
 for r,s in[(50,3),(100,3),(200,3),(3,50),(3,100),(3,200)]:
  v=run(r,s);out.append(v);print({k:v for k,v in v.items()if k!='word'},flush=True)
 (P/'thin_loop_scattering_controls.json').write_text(json.dumps(out,indent=2)+'\n')
