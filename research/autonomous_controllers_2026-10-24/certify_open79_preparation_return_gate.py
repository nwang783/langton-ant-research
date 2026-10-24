#!/usr/bin/env python3
"""Complete small physical-factor cover for the conditional OPEN79 preparation debt.
All two-return layouts of total<=16 are covered; no arbitrary outer cap is used.
"""
from itertools import product
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0));X=(2,1);C=(-1,0)
def geometry(w,p=(0,0),h=2):
 ev=[]
 for t,c in enumerate(w):
  ev.append({'time':t,'position':p,'incoming_heading':h,'turn':c});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return ev,p,h

def main():
 programs={};palettes=[]
 for n in(4,8,12):
  for first in'RL':
   words=[]
   for suffix in product('RL',repeat=n-1):
    w=first+''.join(suffix);ev,p,h=geometry(w)
    if p==(0,0)and h==2 and all(e['position']!=(0,0)for e in ev[1:]):words.append(w)
   assert len(words)=={4:1,8:5,12:44}[n];programs[n,first]=words;palettes.append({'length':n,'first_turn':first,'all_geometric_first_return_words':words})
 layouts=[(4,4),(4,8),(8,4),(4,12),(8,8),(12,4)];cases=[];counts=Counter();survivors=[]
 for n,m in layouts:
  for u in programs[n,'R']:
   for v in programs[m,'L']:
    w='RLRRLL'+u+v+'R';ev,p,h=geometry(w,X);assert ev[6]['position']==ev[6+n]['position']==ev[-1]['position']==C
    prev={};bad=None;initial=set()
    for e in ev:
     pos=e['position']
     if pos not in prev:
      if e['turn']=='L':initial.add(pos)
     elif prev[pos]['turn']==e['turn']and bad is None:bad={'earlier_read':prev[pos],'later_read':e}
     prev[pos]=e
    z={'return_lengths':[n,m],'word':w,'events':ev}
    if bad is not None:z['outcome']='physical_color_contradiction';z['witness']=bad
    else:
     old=[e for e in ev if e['position']==X];assert len(old)==2 and old[0]['time']==0 and old[1]['incoming_heading']==0
     z['outcome']='supplied_first_R_rank1_heading_contradiction';z['witness']={'physical_cell':X,'first_read':old[0],'next_read':old[1],'required_incoming_heading_at_rank1':2,'reason':'X is complete T12 rank0 at the first read; its next physical read must be supplied rank1 S, not N.'}
     B=set(initial)
     for e in ev:assert e['turn']==('L'if e['position']in B else'R');B.symmetric_difference_update({e['position']})
     z['prepared_positive_factor']={'initial_position':X,'initial_heading':2,'initial_black':sorted(initial),'complete_final_black':sorted(B),'final_position':p,'final_heading':h,'warning':'Genuine arbitrary-input finite factor, but incompatible with complete T12 rank1. Not a full interface or controller.'};survivors.append(z)
    counts[z['outcome']]+=1;cases.append(z)
 assert len(cases)==124 and counts=={'physical_color_contradiction':123,'supplied_first_R_rank1_heading_contradiction':1}
 assert survivors[0]['word']=='RLRRLLRRRRLLRRLLLLRRLLR'
 assert len(survivors[0]['prepared_positive_factor']['initial_black'])==4 and len(survivors[0]['prepared_positive_factor']['complete_final_black'])==5
 out={'scope':__doc__,'palettes':palettes,'complete_two_return_layouts':layouts,'cases':cases,'outcome_counts':dict(counts),'conditional_conclusion':'After the signed OPEN79 gap3 preparation fork, t12,10-t12,8>=20. Combining t12,8-t12,0=P+6 and t12,11-t12,3=P-34 gives t12,3-t12,0 =40+(t12,11-t12,8)>=64.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['OPEN79_SHORT_GAP_FORCES_PREPARATION_AGE.md','RETURN_DEBT_OPEN79_CANONICAL_AGE_ADDENDUM.md','physical_return_debt_certificate.json']},'limits':'Conditional on the supplied complete histories and gap3 branch. Larger return spans and longer outer gaps remain OPEN; no period bound, arbitrary gap growth or controller is proved.'}
 (R/'open79_preparation_return_gate_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('PASS124 exact factors:123 color conflicts,1 complete-rank mismatch; two-return>=20, early-span>=64')
if __name__=='__main__':main()
