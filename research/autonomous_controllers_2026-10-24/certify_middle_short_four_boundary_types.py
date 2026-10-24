#!/usr/bin/env python3
"""Complete middle-short core forces two output pairs in the all-cap boundary graph."""
from pathlib import Path
import json,hashlib
from certify_lifetime_boundary_graph import middle28
from check_extremal_read_coupling import D
R=Path(__file__).resolve().parent
CORE={0:'S',1:'W',2:'S',3:'EEWE',4:'SSNS',5:'EEWE',6:'NNNSS',7:'EEEWW'}
def main():
 pairs=[]
 for source,target in [(0,1),(6,7)]:
  h=CORE[source];g=CORE[target];j=len(h)-1;k=len(g)-1;assert j%2==k%2==0
  direction=('NESW'.index(h[j])+1)%4;dx,dy=D[direction];assert target==source+3*dy-dx and dy==0
  src=[r for r,c in enumerate(h)if('NESW'.index(c)+(1 if r%2==0 else-1))%4==direction]
  dst=[r for r,c in enumerate(g)if'NESW'.index(c)==direction]
  assert len(src)==len(dst)and list(zip(src,dst))[-1]==(j,k)
  pairs.append({'source_level':source,'source_R_rank':j,'target_level':target,'target_R_rank':k,'direction':'NESW'[direction],'complete_source_port_ranks':src,'complete_target_port_ranks':dst,'physical_voltage':0,'explanation':'Actual ordinal last-R to last-R horizontal move. Both lifetime half-edges are missing, so this move is the whole horizontal output component.'})
 original=middle28();keep=[];discard=[]
 for t in original['all28_types']:
  H=[tuple(e['ends'])for e in t['edges']if e['axis']=='H'];miss=[p for p in [(0,1),(3,4)]if p not in H]
  if miss:discard.append({'horizontal_choice':t['horizontal_choice'],'vertical_choice':t['vertical_choice'],'missing_required_index_pairs':miss})
  else:keep.append(t)
 assert [(r['horizontal_choice'],r['vertical_choice'])for r in keep]==[(2,0),(2,1),(3,0),(3,1)]
 expected={(2,0):[[0,0,0],[0,-2,1]],(2,1):[[0,-2,1]],(3,0):[[0,0,0],[-4,2,-1]],(3,1):[[4,-2,1]]}
 for r in keep:assert [c['winding_coefficients_a_c_constant']for c in r['unoriented_cycles_with_one_declared_orientation']]==expected[r['horizontal_choice'],r['vertical_choice']]
 out={'status':'AUTHOR CHECK PASS; independent audit pending','scope':'Necessary four boundary types for the exact signed full(3,1) middle-short growth8 branch. No type excluded or realized.','complete_lower_histories':CORE,'full_odd_levels':original['full_odd_levels'],'parameter_domain':'odd 3<=c<=a','actual_forced_horizontal_output_components':pairs,'all24_excluded_types':discard,'four_necessary_open_types':keep,'essential_absolute_windings':['2c-1','2c-1','4a-2c+1','4a-2c+1'],'derived_minimum_absolute_essential_winding':5,'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['certify_lifetime_boundary_graph.py','lifetime_boundary_graph.py','DRIFT31_MIDDLE_SHORT_FULL_ODD_REDUCTION.md']}}
 (R/'middle_short_four_boundary_types_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: 28 -> 4 necessary types; essential absolute winding >=5')
if __name__=='__main__':main()
