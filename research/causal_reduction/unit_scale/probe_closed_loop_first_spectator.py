"""Geometrically first unread-white spectator after the43-cell closed loop.
Adds(1,-2), leaves the complete intended loop unchanged, then follows actual
behavior without resetting any cell or pose. A sample is not an all-r claim.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
from certify_highway_wake_reflector import trace
from probe_perpendicular_highway_wake import H,step
S=json.loads((P/'four_corner_loop_certificate.json').read_text())['seed_families_ax_bx_ay_by']
def run(r,limit=1000000):
 seed={(a*r+b,c*r+d)for a,b,c,d in S};assert(1,-2)not in seed;seed.add((1,-2));B=set(seed);p=(0,0);h=0
 word=('R'+H*r+H[:68])*3+'R'+H*r+H[:60];t0=len(word)
 for t,c in enumerate(word):
  assert p!=(1,-2);p,h,actual=step(B,p,h);assert actual==c
 assert(p,h)==((0,0),0)
 outword=[];events=[];check_after=1000;st=time.monotonic();done=False
 for t in range(limit):
  p,h,c=step(B,p,h);outword.append(c)
  if t+1>=check_after and(t+1)%200==0 and len(outword)>=1040:
   w=''.join(outword[-104:])
   if ''.join(outword[-1040:])!=w*10:continue
   rows,ep,eh=trace(w,p,h)
   if eh!=h or ep==p:continue
   bad=first_mismatch(State(frozenset(B),p,h),w)
   e=dict(time_after_loop=t+1,total_time=t0+t+1,pose=[*p,h],period=w,drift=[ep[0]-p[0],ep[1]-p[1]],bad=bad,mass=len(B));events.append(e);print(e,flush=True)
   if bad is None:done=True;break
   check_after=t+1+bad+1000
 out=dict(scope=__doc__,r=r,initial_mass=len(seed),marker=[1,-2],loop_length=t0,status='EXACT_CAPTURE'if done else'UNKNOWN_HORIZON',time_after_loop=t+1,events=events,actual_continuation=''.join(outword),final_black=sorted(B),seconds=time.monotonic()-st)
 (P/f'closed_loop_first_spectator_r{r}.json').write_text(json.dumps(out,indent=2)+'\n')
 print('FINISH',r,out['status'],t+1,flush=True)
 return out
if __name__=='__main__':run(int(sys.argv[1])if len(sys.argv)>1 else 50)
