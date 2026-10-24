"""Exact RL/LR one-use joins:16 full products, actual eight-cycle failures,
and explicit disjoint-component clocks for the four necessary RL controls.
Not a period/length scan, prepared factor or full front.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
base=Path(__file__).parent;lib={'__file__':str(base/'check_even_reader_rail_and_merge_reset.py')};exec((base/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0],lib)
V,out,check,graph=[lib[k]for k in ['V','out','check','graph']];rows=[];ct=Counter()
for join,up,lo,opt in product(['RL','LR'],['EWW','EWWE'],['EWW','EWWE'],[False,True]):
 b=(0,-2)if join=='RL'else(2,-2);x,y=b
 hs={(1,1):'SN',(0,1):up,(0,0):'NNSS',(1,0):'EE',(x,y):'SN',(x-1,y):lo,(x-1,y-1):'NNSS',(x,y-1):'EE'}
 if join=='RL':hs|={(1,-1):'S',(0,-1):'EEWE'if opt else'EEW'}
 else:hs|={(1,-1):'NNSN'if opt else'NNS',(2,-1):'E'}
 ans=check(hs);data=None
 if ans=='open':
  assert join=='RL'and not opt
  su,cs,order,times=graph(hs);data=dict(components=cs,whole_component_order=order,injective_mod4_calendar={str(e):t for e,t in times.items()},events=len(times))
 elif ans=='skipped_rank':
  assert join=='LR'and lo=='EWWE'and not opt
  su={}
  for p,h in hs.items():
   for d,v in V.items():
    q=p[0]+v[0],p[1]+v[1]
    if q not in hs:continue
    sr=[r for r in range(len(h))if out(h,r)==d];tr=[r for r,z in enumerate(hs[q])if z==d];assert len(sr)==len(tr)
    su.update({(p,r):(q,s)for r,s in zip(sr,tr)})
  path=[((1,-1),0),((2,-1),0),((2,-2),0),((1,-2),1),((1,-3),3),((2,-3),1),((2,-2),1),((1,-2),2),((1,-1),0)]
  assert all(su[e]==f for e,f in zip(path,path[1:]));data=dict(actual8_event_cycle=path)
 else:assert ans=='port'
 ct[ans]+=1;rows.append(dict(join=join,upper_root=up,lower_root=lo,LEFTfour=opt,result=ans,histories={str(p):h for p,h in sorted(hs.items())},certificate=data))
assert ct=={'open':4,'port':10,'skipped_rank':2}
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(ct),rows=rows,warning='Only two specified two-vertex joins; no arbitrary connector odd-charge or full-orbit realization.'),indent=2)+'\n');print('PASS16:10ports+2actualcycles+4necessaryRL controls with injective clocks')
