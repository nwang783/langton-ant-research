"""Eight lattice phases of perpendicular certified104 versus mature104 wake.
Finite controls only; repeated104 detection is NOT an infinite-tail certificate.
"""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent
standard=json.loads(Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json').read_text())
H=standard['word'];D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,k):
 x,y=p
 for _ in range(k):x,y=-y,x
 return x,y
def shifted_seed(k,p):
 return {(rot(q,k)[0]+p[0],rot(q,k)[1]+p[1])for q in standard['seed']}
def step(B,p,h):
 c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);return p,h,c

def run(n,m,delta):
 # Old front travels NE, from(-2n,-2n)to(2n,2n), then its ant is omitted.
 oldpose=(-2*n,-2*n);old=shifted_seed(2,oldpose);p=oldpose;h=1
 for c in H*(2*n):
  p,h,a=step(old,p,h);assert a==c
 assert(p,h)==((2*n,2*n),1)
 # New front travels SE across the old wake. These are finite prepared seeds.
 start=(-2*m+delta[0],2*m+delta[1]);B=old|shifted_seed(1,start);p=start;h=2
 out=[];poses=[];first_old=None
 for t in range(100000):
  poses.append((p,h))
  if first_old is None and p in old:first_old=t
  p,h,c=step(B,p,h);out.append(c)
  if first_old is not None and t>first_old+1040 and t%104==0:
   tail=''.join(out[-1040:]);w=tail[-104:]
   if tail==w*10:
    p0,h0=poses[-104];drift=(p[0]-p0[0],p[1]-p0[1])
    return dict(n=n,m=m,delta=delta,same_original_pose_sector=(sum(delta)%2==1),old_mass=len(old),seed_mass=len(old|shifted_seed(1,start)),first_old=first_old,status='SAMPLED_104_NOT_PROOF',time=t+1,pose=[p,h],drift=drift,word=''.join(out),final_black=sorted(B))
 return dict(n=n,m=m,delta=delta,first_old=first_old,status='UNKNOWN_HORIZON',time=100000,pose=[p,h],word=''.join(out),final_black=sorted(B))
if __name__=='__main__':
 start=time.time();R=[run(30,30,(x,y))for x in range(4)for y in range(2)]
 P.joinpath('perpendicular_highway_wake.json').write_text(json.dumps(dict(scope=__doc__,cases=R,seconds=time.time()-start),indent=2)+'\n')
 for r in R:print({k:v for k,v in r.items()if k not in('word','final_black')})
