"""Opposite-side collision controls. Finite repeat observations only, not proof."""
from pathlib import Path
import json,time
from probe_perpendicular_highway_wake import H,shifted_seed,step
P=Path(__file__).resolve().parent
def run(n,m,delta):
 old=shifted_seed(2,(-2*n,-2*n));p=(-2*n,-2*n);h=1
 for c in H*(2*n):p,h,a=step(old,p,h);assert a==c
 start=(2*m+delta[0],-2*m+delta[1]);B=old|shifted_seed(3,start);p=start;h=0;out=[];poses=[];first=None
 for t in range(100000):
  poses.append((p,h))
  if first is None and p in old:first=t
  p,h,c=step(B,p,h);out.append(c)
  if first is not None and t>first+1040 and t%104==0:
   z=''.join(out[-1040:]);w=z[-104:]
   if z==w*10:
    p0,h0=poses[-104];return dict(n=n,m=m,delta=delta,same_original_pose_sector=(sum(delta)%2==1),first_old=first,status='SAMPLED_104_NOT_PROOF',time=t+1,pose=[p,h],drift=[p[0]-p0[0],p[1]-p0[1]],word=''.join(out))
 return dict(n=n,m=m,delta=delta,status='UNKNOWN_HORIZON',word=''.join(out))
if __name__=='__main__':
 R=[run(30,30,(x,y))for x in range(4)for y in range(2)];P.joinpath('highway_wake_backside.json').write_text(json.dumps(R,indent=2)+'\n')
 for z in R:print({k:v for k,v in z.items()if k!='word'})
