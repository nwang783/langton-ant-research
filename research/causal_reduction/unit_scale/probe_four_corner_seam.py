"""One geometric four-quarter-turn loop and its forced return seam.
The seed is the exact minimal first-L set of the maximal internally legal
prescribed prefix. Actual continuation is followed without repair or reset.
"""
from pathlib import Path
import json
from certify_highway_wake_reflector import trace
from probe_perpendicular_highway_wake import H,step
P=Path(__file__).resolve().parent
def run(r):
 W=('R'+H*r+H[:68])*4
 rr,ep,eh=trace(W,(0,0),0);assert(ep,eh)==((0,0),0)
 first={};last={}
 for cut,(q,h,c)in enumerate(rr):
  if q in last and last[q][1]==c:break
  last[q]=(cut,c);first.setdefault(q,c)
 else:raise AssertionError('No expected seam')
 seed={q for q,c in first.items()if c=='L'};B=set(seed);p=(0,0);h=0;w=[];poses=[]
 for t in range(250000):
  poses.append((p,h));p,h,c=step(B,p,h);w.append(c)
  if t<cut:assert c==W[t]
  if t==cut:assert c!=W[t]
  if t>cut+2080 and t%104==0 and ''.join(w[-2080:])==''.join(w[-104:])*20:
   d=(p[0]-poses[-104][0][0],p[1]-poses[-104][0][1]);break
 else:d=None
 out=dict(scope=__doc__,r=r,seed=sorted(seed),seed_mass=len(seed),intended_length=len(W),first_bad_prescribed=cut,bad_cell=rr[cut][0],bad_incoming=rr[cut][1],sample_time=t+1,sample_pose=[p,h],sample_drift=d,word=''.join(w),final_black=sorted(B))
 P.joinpath(f'four_corner_seam_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('word','final_black','seed','scope')})
if __name__=='__main__':run(10)
