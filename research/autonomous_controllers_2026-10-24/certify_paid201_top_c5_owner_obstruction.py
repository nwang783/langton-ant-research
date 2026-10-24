#!/usr/bin/env python3
"""All-period exclusion of the supplied201 factor in the a=c=5 middle-short inventory.
A derived upper cover leaves no earlier L owner before its required T29 block.
Omitted lower levels remain UNKNOWN. No period, visit or search cap is imposed.
"""
from pathlib import Path
from collections import Counter
import hashlib,json
from certify_drift31_refined_top_odd_gap import complete_words
from certify_drift31_read_minimum import depart,returns_to
from partial_drift31_graph import graph
R=Path(__file__).resolve().parent

def fmt(H):return{str(t):list(h)for t,h in sorted(H.items())}
def main():
 O={0,1,2,6,7,31,32,34};states=[{34:(0,),35:(),36:(),37:()}];records=[];counts={}
 for t in range(33,28,-1):
  out=[];co=Counter()
  for H in states:
   lev=sorted(H);kind,G=graph([H[z]for z in lev],lev);assert kind=='open';_,paths=returns_to([H[z]for z in lev],G,t)
   if t%2==0:ih,I,oh,J=2,len(depart(H[t+3],2)),3,H[t+1].count(3)
   else:ih,I,oh,J=1,len(depart(H[t+1],1)),0,H[t+3].count(0)
   bound=2*(I+J)+1;domain=[h for h in complete_words(t%2,bound,ih,I,oh,J)if len(h)%2==(t in O)]
   rec={'level':t,'complete_upper_before':fmt(H),'incoming_heading_count':[ih,I],'outgoing_heading_count':[oh,J],'derived_bound':bound,'required_parity':int(t in O),'actual_first_return_paths':paths,'complete_domain':[list(h)for h in domain],'outcomes':[]}
   for h in domain:
    row={'word':list(h)};fail=None
    for a,p in enumerate(paths):
     dest=[j for j,v in enumerate(h)if v==p['incoming_heading']][p['incoming_ordinal']];src=depart(h,p['outgoing_heading'])[p['outgoing_ordinal']]
     if dest!=src+1:fail={'path_index':a,'source_rank':src,'target_rank':dest,'required_target_rank':src+1};break
    if fail is not None:
     row|={'outcome':'first_return_rank','witness':fail};co['first_return_rank']+=1
    else:
     HH=H|{t:h};ll=sorted(HH);kk,gg=graph([HH[z]for z in ll],ll);row['outcome']=kk;co[kk]+=1
     if kk=='open':out.append(HH)
     else:row['witness']=gg
    rec['outcomes'].append(row)
   records.append(rec)
  counts[t]=dict(co);states=out
  print(t,len(states),dict(co),flush=True)
 assert counts[30]=={'first_return_rank':54,'open':3}
 assert counts[29]=={'first_return_rank':121,'open':8,'skipped_rank':5,'positive_rank_clock_cycle':4}
 ownership=[]
 for H in states:
  h=H[29];block=[]
  for j in range(len(h)-3):
   if j%2==1 and h[j:j+4]==(3,3,3,1):block.append(j)
  earlier={j:[k for k in range(j)if k%2==1 and h[k]==3]for j in block}
  assert all(not ls for ls in earlier.values())
  assert not block or block==[1]
  ownership.append({'complete_upper_histories':fmt(H),'T29_word':' '.join('NESW'[v]for v in h),'possible_WL_WR_WL_ER_block_start_ranks':block,'earlier_W_L_ranks_for_each_block':earlier,'contradiction':'No complete rank placement for the additional earlier W/L read. The only surviving block placement starts at rank1.'if block else'The four consecutive observed physical reads have no rank placement at all.'})
 # Bind the actual two prepared BLACK lifetime observations, not a guessed word.
 F=json.load(open(R/'open79_paid_chain201_certificate.json'));E=F['events'];p=(0,6);q=(-3,5)
 assert p==(q[0]+3,q[1]+1)
 assert [(e['time'],e['incoming_heading'],e['turn'])for e in E if tuple(e['position'])==p]==[(87,3,'L')]
 assert [(e['time'],e['incoming_heading'],e['turn'])for e in E if tuple(e['position'])==q]==[(93,3,'L'),(105,3,'R'),(109,3,'L'),(117,1,'R')]
 assert [o['owner_R_time']for o in F['all_L_lifetime_owners']if o['time']in[87,93]]==['initial BLACK','initial BLACK']
 out={'scope':__doc__,'full_odd_inventory':sorted(O),'max_complete_read_level':34,'upper_start':{'34':[0],'35':[],'36':[],'37':[]},'lower_exterior':'All levels <=28 omitted and UNKNOWN.','records':records,'counts':counts,'eight_open_upper_interfaces_and_owned_read_failures':ownership,'physical_lifetime_observations':{'earlier_lifted_read':{'point':p,'time':87,'incoming':'W','turn':'L'},'later_block':{'point':q,'times':[93,105,109,117],'incoming':'WWWE','turns':'LRLR'},'full_translation':[3,1],'earlier_read_clock_at_later_cell':'87-P','strict_order_for_every_positive_period':'87-P < 93','reason':'The same full-drift class must include the translated earlier L at a strictly smaller ordinal. Each complete history starts R, so no L can precede the only possible block starting at rank1.'},'limits':'Excludes this supplied factor from the exact a=c=5 inventory, not all a=c fronts. The a=5,c=3 inventory and general family remain OPEN. No initial BLACK is automatically rejected; its observed lifetime is compared with exact complete port/rank obligations.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['OPEN79_PAID_CHAIN201_AND_UNPAID67_CONTRAST.md','open79_paid_chain201_certificate.json','DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md','certify_drift31_refined_top_odd_gap.py','partial_drift31_graph.py','certify_drift31_read_minimum.py']}}
 (R/'paid201_top_c5_owner_obstruction_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('PASS eight complete upper interfaces, no full-rank embedding of the two supplied BLACK lifetime observations')
if __name__=='__main__':main()
