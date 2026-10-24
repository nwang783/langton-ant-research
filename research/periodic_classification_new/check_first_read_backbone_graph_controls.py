#!/usr/bin/env python3
"""Synthetic CELL-graph controls only; not port-balanced ant fronts."""
from pathlib import Path
import json
from first_read_backbone_frontier import transition
from frontier_drift_geometry import Geometry
from check_first_read_backbone_positive import row
D=((0,1),(1,0),(0,-1),(-1,0));g=Geometry(4,0)
def replay(hs):
 lo=min(y for x,y in hs);hi=max(y for x,y in hs);state=();old=row([()]*4);C=0
 for y in range(lo,hi+2):
  new=row([tuple(hs.get((c,y),())) for c in range(4)])
  state,z,bad=transition(state,old,new,(y-1)%2,g,120)
  if bad:return dict(status='REJECT',reason=bad,row=y)
  C=max(C,z);old=new
 return dict(status='ACCEPT',final_state=state,period_lower=C)
unit={(0,0):(3,),(1,0):(2,),(0,1):(0,),(1,1):(1,)}
assert replay(unit)['reason']=='first_cycle_wrong_winding'
results=dict(contractible=replay(unit))
for sign in(1,-1):
 dirs=([1,0,1,2]*2) if sign==1 else([3,0,3,2]*2)
 p=(1,0);hs={}
 for i,d in enumerate(dirs):
  h=dirs[i-1];assert h%2==1-(sum(p)%2)
  hs[p[0]%4,p[1]]=(h,) if d==(h+1)%4 else(h,h)
  dx,dy=D[d];p=p[0]+dx,p[1]+dy
 assert p==(1+4*sign,0)
 result=replay(hs);results[str(sign)]=result
 if sign==1:
  assert result['status']=='ACCEPT' and result['period_lower']==24
  hs[1,1]=(1,1);hs[1,2]=(0,);branch=replay(hs);results['branch_after_cycle']=branch
  assert branch['status']=='ACCEPT' and branch['period_lower']==24
 else:assert result['reason']=='first_cycle_wrong_winding'
Path(__file__).with_name('first_read_backbone_graph_controls.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results))
