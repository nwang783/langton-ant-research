#!/usr/bin/env python3
"""Exact uncapped obstruction to one specified near-minimum last-spine placement."""
from itertools import product
from pathlib import Path
import json,hashlib
from certify_drift31_read_minimum import words,depart
from partial_drift31_graph import graph,D
R=Path(__file__).resolve().parent

def concrete(H,seq):
 out=[]
 for level,rank,k in seq:
  h=H[level][rank];turn='R'if rank%2==0 else'L';ho=(h+(1 if turn=='R'else-1))%4;p=(-level+3*k,k)
  out.append({'level':level,'rank':rank,'lift':k,'position':p,'heading':h,'turn':turn,'outgoing_heading':ho})
 for a,b in zip(out,out[1:]):assert tuple(a['position'][i]+D[a['outgoing_heading']][i]for i in range(2))==b['position']and a['outgoing_heading']==b['heading']
 assert out[0]['position']==out[-1]['position']and all(x['position']!=out[0]['position']for x in out[1:-1])
 return out

def main():
 h3=[v for v in words(1,4,3,1,2,1)if len(v)%2==0 and v[-1]==1];assert set(h3)=={(1,1,3,1),(3,1,1,1)}
 v4=[v for v in words(0,10,0,2,1,3)if len(v)%2==0 and v[-1]==2];assert len(v4)==12
 cover=[];survive=[]
 for h in h3:
  sr=depart(h,2)[0];a=[r for r,x in enumerate(h)if x==1].index(sr)
  for v in v4:
   er=depart(v,1)[a];nr=v.index(0);H={0:(2,),1:(3,1),2:(2,2),3:h,4:v};path=concrete(H,[(4,er,0),(3,sr,0),(0,0,-1),(1,0,-1),(4,nr,0)])
   ok=nr==er+1;cover.append({'H3':h,'V4':v,'E_ordinal':a,'source_E_rank':er,'first_N_rank':nr,'necessary_consecutive_rank':ok,'actual_four_step_first_return':path})
   if ok:survive.append((h,v))
 assert survive==[((1,1,3,1),(2,2,0,0,2,2))]
 h5=[v for v in words(1,6,3,3,2,2)if len(v)%2==0 and v[-1]==3];assert len(h5)==3
 final=[]
 for h in h5:
  H={0:(2,),1:(3,1),2:(2,2),3:survive[0][0],4:survive[0][1],5:h}
  assert max(r for r,x in enumerate(h)if x==3)==5
  assert len(depart(H[4],3))==3 and depart(H[4],3)[2]==4
  assert [r for r,x in enumerate(h)if x==3][2]==5
  assert len(depart(h,2))==2
  assert depart(h,2)[1]==5 # second S departure feeds T2's L1
  assert depart(H[2],1)[0]==1 and [r for r,x in enumerate(H[1])if x==1][0]==1
  assert depart(H[1],0)[1]==1 and [r for r,x in enumerate(H[4])if x==0][1]==3
  path=concrete(H,[(4,4,0),(5,5,0),(2,1,-1),(1,1,-1),(4,3,0)])
  final.append({'H5':h,'complete_named_histories':H,'actual_forbidden_four_step_return':path,'clock_contradiction':'tau(T4,L3)=tau(T4,R4)+4 but tau(T4,R4)>=tau(T4,L3)+4'})
 # Existing open prefix remains genuinely open before imposing T5's final port.
 low=[(),(),(),(2,),(3,1),(2,2),(1,1,3,1),(2,2,0,0,2,2)];kind,witness=graph(low);assert kind=='open'
 # Derive the same unique low prefix from the retained complete25 cover.
 old=json.loads((R/'drift31_read_minimum_certificate.json').read_text());filtered=[]
 for x in old['all25_open_interfaces']:
  hh=x['complete_histories'][3:]
  if all(hh[i]and len(hh[i])%2==0 and(hh[i][-1]-1)%4==out for i,out in[(1,0),(2,1),(3,0),(4,1)]):filtered.append(x)
 assert len(filtered)==1 and filtered[0]['complete_histories']==[list(v)for v in low]
 deps=['DRIFT31_UNCONDITIONAL_READ_MINIMUM_INTERFACE.md','drift31_read_minimum_certificate.json','partial_drift31_graph.py','OUTERMOST_EXIT_BASIN_OUTPUT_TARGET_AND_EXACT_BOUNDARY.md']
 out={'scope':'Complete WHITE full(3,1), global read minimumT0. The stated five selected final-L ports are impossible at arbitrary exterior multiplicity. This excludes one nearest six-edge all-even last-spine placement only, not every short spine or outer basin with <=3 outputs.','minimum_derived_initial_histories':{'T0':'S','T1':'WE','T2':'SS'},'H3_derived_max_reads':4,'all_H3':h3,'V4_derived_max_reads':10,'all_V4_count_domains':v4,'all24_first_N_return_cases':cover,'sole_surviving_H3_V4':survive,'H5_derived_exact_reads':6,'all_three_H5':h5,'three_identical_ordinal_obstructions':final,'initial_OPEN_prefix':{'histories':low,'graph':witness},'unique_retained_minimum_interface':filtered[0],'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in deps}}
 p=R/'outer_all_even_short_spine_obstruction_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS author',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
