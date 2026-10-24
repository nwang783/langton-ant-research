"""The four SAME-sector opposite-incidence phases of the retained wake reflector.
Targeted finite complete-board controls, not a parameter-uniform classification.
"""
import json,time
from pathlib import Path
from probe_perpendicular_highway_wake import H,shifted_seed,step
from probe_thin_loop_scattering import R,check
P=Path(__file__).resolve().parent

def run(n,m,delta,limit=300000):
 old=shifted_seed(2,(-2*n,-2*n));p=(-2*n,-2*n);h=1
 for c in H*(2*n):p,h,a=step(old,p,h);assert a==c
 start=(2*m+delta[0],-2*m+delta[1]);inc=shifted_seed(3,start);assert not old&inc
 B=old|inc;p=start;h=0;word=[];first=None;samples=[]
 for t in range(limit):
  if first is None and p in old:first=t
  p,h,c=step(B,p,h);word.append(c)
  if first is not None and t>first+104 and t%104==0:
   phase=R.get(''.join(word[-104:]))
   if phase is not None:
    good=check(B,p,phase,h)
    if not samples or (samples[-1]['h'],samples[-1]['phase'])!=(h,phase):samples.append(dict(t=t+1,p=p,h=h,phase=phase,exact_tail=good))
    if good:
     return dict(n=n,m=m,delta=delta,status='EXACT_LITERAL_TAIL',first_old=first,time=t+1,pose=[p,h],phase=phase,seed_mass=len(old|inc),mass=len(B),old_erased=len(old-B),old_retained=len(old&B),segments=samples,word=''.join(word),final_black=sorted(B))
 return dict(n=n,m=m,delta=delta,status='UNKNOWN_HORIZON',first_old=first,time=limit,pose=[p,h],segments=samples,word=''.join(word),final_black=sorted(B))
if __name__=='__main__':
 out=[];st=time.monotonic()
 for delta in[(0,1),(1,0),(2,1),(3,0)]:
  z=run(80,50,delta);out.append(z);print({k:v for k,v in z.items()if k not in('word','final_black')},flush=True)
 (P/'opposite_wake_incidence_controls.json').write_text(json.dumps(dict(cases=out,seconds=time.monotonic()-st),indent=2)+'\n')
