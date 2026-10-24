"""Continue one geometrically specified loop family member with exact tail tests.
Every proposed period is checked on the COMPLETE finite board; if a later
mismatch exists, simulation continues through it rather than reporting capture.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
from probe_perpendicular_highway_wake import step

def run(r,horizon=2000000):
 st=time.monotonic();J=json.loads((P/f'four_corner_seam_r{r}.json').read_text());B=set(map(tuple,J['final_black']));p=tuple(J['sample_pose'][0]);h=J['sample_pose'][1];w=list(J['word']);poses=[];events=[];check_after=len(w);done=False
 for t in range(len(w),horizon):
  poses.append((p,h));p,h,c=step(B,p,h);w.append(c)
  if len(w)>=check_after and t%104==0 and ''.join(w[-1040:])==''.join(w[-104:])*10:
   period=''.join(w[-104:]);bad=first_mismatch(State(frozenset(B),p,h),period)
   e=dict(time=t+1,pose=[p,h],period=period,first_later_mismatch=bad,mass=len(B));events.append(e);print(e,flush=True)
   if bad is None:done=True;break
   check_after=t+1+bad+1040
 out=dict(scope=__doc__,r=r,status='EXACT_EVENTUAL_PERIOD'if done else'UNKNOWN_HORIZON',time=len(w),pose=[p,h],events=events,word=''.join(w),final_black=sorted(B),seconds=time.monotonic()-st)
 P.joinpath(f'four_corner_actual_exact_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print('FINISH',r,out['status'],out['time'],out['seconds'],flush=True)
if __name__=='__main__':run(int(sys.argv[1])if len(sys.argv)>1 else 100)
