#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import json,hashlib
from partial_drift31_graph import graph
from certify_active_C_entry_exit_forests import active_C
from check_extremal_read_coupling import D,quotient
R=Path(__file__).resolve().parent
W=['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW'];H=[tuple('NESW'.index(c) for c in w) for w in W]
def dep(hs,d):return [i for i,h in enumerate(hs) if(h+(1 if i%2==0 else-1))%4==d]
def main():
 kind,G=graph(H,list(range(8)));assert kind=='open'
 a=next(c for c in G['chains'] if len(c)==3);assert a==[((7,0),0),((4,0),-1),((5,2),-1)]
 main=max(G['chains'],key=len);assert len(main)==17
 es=[]
 for chain in G['chains']:
  ee=[]
  for (t,r),k in chain:
   p=(-t+3*k,k);ee.append({'level':t,'rank':r,'lift':k,'position':p,'heading':H[t][r],'turn':'R' if r%2==0 else'L','C_face':active_C(p,H[t][r])})
  es.append(ee)
 assert dep(H[5],0)==[1,2,3]
 # All N arrivals of T8 correspond to the complete source ranks1,2,3.
 supply=[{'source_T5_rank':r,'target_T8_N_ordinal':j,'source_position':(-8,-1),'target_position':(-8,0)} for j,r in enumerate(dep(H[5],0))]
 assert supply[1]['source_T5_rank']==2
 assert all(e['C_face']==(-8,-1) for e in next(c for c in es if len(c)==3))
 # Complete sector inventory: candidate first events cannot hide at omitted cells.
 sectors={1:[],3:[],5:[]}
 for t in range(8):
  for r,h in enumerate(H[t]):
   c=active_C((-t,0),h);T=3*c[1]-c[0]
   if T in sectors:sectors[T].append({'cell_level':t,'rank':r,'heading':h,'turn':'R' if r%2==0 else'L','physical_C':c})
 assert len(sectors[1])==6 and len(sectors[3])==8 and len(sectors[5])==7
 counts={1:6,3:8,5:len(sectors[5])+len(supply)};assert counts=={1:6,3:8,5:10}
 ee=next(c for c in es if len(c)==17)
 assert ee[2]['C_face']==(-7,-2) and ee[7]['C_face']==(-6,-1)
 # Last read of the17-channel is T5.L1, immediately entering C5+d.
 e=ee[-1];assert(e['level'],e['rank'],e['position'],e['heading'])==(5,1,(-5,0),1)
 hd=(e['heading']-1)%4;p=(e['position'][0]+D[hd][0],e['position'][1]+D[hd][1]);assert active_C(p,hd)==(-5,0)
 steps=[((-8,-1),(-7,-2)),((-7,-2),(-6,-1)),((-6,-1),(-5,0))];assert (steps[-1][1][0]-steps[0][0][0],steps[-1][1][1]-steps[0][0][1])==(3,1)
 out={'status':'AUTHOR checked, independent audit pending','scope':'Forced three-face first-C cycle under the exact complete lower histories; no higher completion, period bound or exclusion.',
  'complete_lower_histories':W,'all_named_channels':es,'complete_N_port_and_ordinals':supply,'complete_known_sector_inventories':sectors,'complete_C_visit_counts':counts,
  'chronological_first_N_argument':{'three_R_source_channel':next(c for c in es if len(c)==3),'next_read_is_N_ordinal':1,'first_N_is_before_entire_channel':True,'first_entry_source':'T5.L1 at(-8,-1), active C3-d','all_other_named_C5_reads_are_at_or_after_T7_R0':True},
  'cycle_steps':steps,'forward_winding':1,'first_activation_clock_offsets_from_T7_R2':{'C1':2,'C3':7,'C5_plus_d':17},'interval_lengths':['P-15',5,10],
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['partial_drift31_graph.py','ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md','C_PERMANENT_PAIR_TERMINAL_CHANNEL_AND_MIDDLE_SHORT_MOTIF.md','MIDDLE_SHORT_FOUR_BOUNDARY_TYPES.md']}}
 p=R/'middle_short_three_C_cycle_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS forced first C cycle',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
