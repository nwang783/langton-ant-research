#!/usr/bin/env python3
"""A genuine finite prepared67 factor realizes the entire local repair/consume motif.
Not a completed OPEN79 history, complete WHITE front, or regenerative controller.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;D=((0,1),(1,0),(0,-1),(-1,0));T=lambda p:3*p[1]-p[0]+11
WORD='RLRRLLRRLRRLRRLRRRRLRLLRLLRLLLLRLLRLRLLRLLLLRRRRLRLLRLLRRRRLLRLLLLR'
SEED={(-5,2),(-5,3),(-4,1),(-4,4),(-3,0),(-3,5),(-2,1),(-2,2),(-2,4),(-2,5),(-1,1),(-1,2),(-1,5),(0,1),(0,5),(1,1),(1,3),(1,4)}
X=(2,1);A=(1,0);B=(0,0);U=(0,1);V=(-1,1);C=(-1,0)
def main():
 assert len(WORD)==67 and len(SEED)==18
 black=SEED.copy();p=X;h=2;events=[];last={};owners=[]
 for t,c in enumerate(WORD):
  assert c==('L'if p in black else'R')
  events.append({'time':t,'position':p,'normal_level':T(p),'incoming_heading':h,'turn':c})
  if c=='L':owners.append({'L_time':t,'position':p,'owner':last.get(p,'initial BLACK input')})
  last[p]=t;black.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 def reads(q):return [(e['time'],e['incoming_heading'],e['turn'])for e in events if e['position']==q]
 assert reads(C)==[(6,2,'R'),(62,2,'L'),(66,2,'R')]
 assert reads(B)==[(3,3,'R'),(63,1,'L')]
 assert reads(U)==[(4,0,'L'),(16,2,'R'),(64,0,'L')]
 assert reads(V)==[(5,3,'L'),(17,3,'R'),(53,1,'L'),(61,1,'R'),(65,3,'L')]
 assert reads(X)==[(0,2,'R')] and reads(A)==[(2,2,'R')]
 assert all(e['normal_level']>=13 for e in events[7:62])
 assert set(SEED)<=set(e['position']for e in events) # None of the supplied fuel is omitted from replay.
 assert len(black)==15 and p==(-2,0)and h==3
 assert next(o for o in owners if o['L_time']==63)['owner']==3
 assert next(o for o in owners if o['L_time']==64)['owner']==16
 assert next(o for o in owners if o['L_time']==65)['owner']==61
 assert next(o for o in owners if o['L_time']==53)['owner']==17
 initial_consumed=[o for o in owners if o['owner']=='initial BLACK input'];assert len(initial_consumed)==18
 out={'scope':__doc__,'word':WORD,'initial_position':X,'initial_heading':2,'complete_initial_black':sorted(SEED),'events':events,'complete_final_black':sorted(black),'final_position':p,'final_heading':h,'all_L_lifetime_owners':owners,'U_reads':reads(U),'V_reads':reads(V),'C_reads':reads(C),'higher_V_first_return_lengths':[36,8],'initial_fuel_consumptions':initial_consumed,'net_black_mass_change':len(black)-len(SEED),'anchored_named_reads':{'X_T12_rank0':0,'A_T10_rank2':2,'B_T11_rank8':3,'C_T12_rank8':6,'C_T12_rank9':62,'B_T11_rank9':63,'C_T12_rank10':66},'limits':'The anchored reads match the supplied local histories, but earlier/later named reads and full-drift higher-class ordering are not completed. The period and full odd output inventory remain unspecified. The factor consumes18 prepared BLACK lifetimes and finishes at a different position and heading; no repeatable relation is claimed.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['OPEN79_MANDATORY_GUIDE_PAIR_AND_UNIT_RETURN.md','open79_pair_beam_completion_discovery.json']}}
 (R/'open79_joint_repair67_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('PASS actual67, full18->15 BLACK fields, U/V restorations,36/8 V returns and exact4 C loop; all18 prepared owners retained')
if __name__=='__main__':main()
