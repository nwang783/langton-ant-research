"""One canonical opposite-heading mature104-wake input.
The old NE front ends at0,E. The new prepared initial ant is at0,W, in the
SAME pose sector. This does not supply a physical turnaround or reversal.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
from probe_perpendicular_highway_wake import H,shifted_seed,step
from certify_highway_wake_reflector import trace

def run(n=30):
 B=shifted_seed(2,(-4*n,-4*n));p=(-4*n,-4*n);h=1
 for c in H*(2*n):p,h,a=step(B,p,h);assert a==c
 assert(p,h)==((0,0),1)
 initial=sorted(B);h=3;w=[];events=[];check_after=500;st=time.monotonic();done=False
 for t in range(300000):
  p,h,c=step(B,p,h);w.append(c)
  if t>=check_after and t%100==0:
   tail=''.join(w[-2080:])
   for size in range(2,209,2):
    if len(tail)<10*size or tail[-10*size:]!=tail[-size:]*10:continue
    period=tail[-size:];_,ep,eh=trace(period,p,h)
    if eh!=h or ep==p:continue
    bad=first_mismatch(State(frozenset(B),p,h),period)
    event=dict(time=t+1,pose=[p,h],period=period,period_length=size,drift=[ep[0]-p[0],ep[1]-p[1]],first_later_mismatch=bad,mass=len(B));events.append(event);print(event,flush=True)
    if bad is None:done=True
    else:check_after=t+1+bad+500
    break
   if done:break
 out=dict(scope=__doc__,n=n,initial_mass=len(initial),initial_black=initial,initial_pose=[0,0,'W'],status='EXACT_PERIODIC_CAPTURE'if done else'UNKNOWN_HORIZON',time=t+1,pose=[p,h],events=events,word=''.join(w),final_black=sorted(B),seconds=time.monotonic()-st)
 P.joinpath(f'same_sector_wake_return_n{n}.json').write_text(json.dumps(out,indent=2)+'\n');print('FINISH',out['status'],out['time'],flush=True)
if __name__=='__main__':run()
