"""One geometric same-sector endpoint collision, not a phase/seed scan.
The old NE front's actual final pose is normalized to(0,0,E), then omitted.
An SE standard front approaches the canonical phase x+y=1. Finite controls only.
"""
from pathlib import Path
import json
from probe_perpendicular_highway_wake import shifted_seed,H,step
P=Path(__file__).resolve().parent
def run(n=30,m=30):
 old=shifted_seed(2,(-4*n,-4*n));p=(-4*n,-4*n);h=1
 for c in H*(2*n):p,h,a=step(old,p,h);assert a==c
 assert(p,h)==((0,0),1)
 start=(-2*m+1,2*m);inc=shifted_seed(1,start);assert not(old&inc)
 B=old|inc;p=start;h=2;w=[];poses=[];touch=None
 for t in range(150000):
  poses.append((p,h))
  if p in old and touch is None:touch=t
  p,h,c=step(B,p,h);w.append(c)
  if touch is not None and t>touch+2080 and t%104==0 and ''.join(w[-2080:])==''.join(w[-104:])*20:
   d=(p[0]-poses[-104][0][0],p[1]-poses[-104][0][1]);break
 else:d=None
 out=dict(scope=__doc__,n=n,m=m,first_old=touch,sample_time=t+1,sample_pose=[p,h],sample_drift=d,word=''.join(w),final_black=sorted(B))
 P.joinpath(f'wake_endpoint_control_n{n}_m{m}.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('word','final_black')})
if __name__=='__main__':run()
