#!/usr/bin/env python3
"""Discovery of the next complete derived C row; unbounded region remains open."""
import enumerate_g8_cycle_two_outer_rows as core
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json,time

def c_words():
 out=[];allwords=[]
 for n in range(5,22):
  z=10-n//2
  if z%2:continue
  a=z//2;b=5-a
  if not 0<=a<=(n+1)//2 or not 0<=b<=n//2:continue
  for rr,ll in product(combinations(range(0,n,2),a),combinations(range(1,n,2),b)):
   E=set(rr)|set(ll);hs=tuple(1 if j in E else 3 for j in range(n));ee=sorted(E);ss=[j for j,h in enumerate(hs)if(h+(1 if j%2==0 else-1))%4==2];assert len(ss)==5
   allwords.append(hs)
   if ee[1]==ss[0]+1 and ee[3]==ss[2]+1:out.append(hs)
 return out,allwords

def main():
 core.PTS=[(r,t-r)for t in range(-1,4)for r in(0,1)];core.IX={p:i for i,p in enumerate(core.PTS)};words,allwords=c_words();stats=Counter();survivors=[];rejects=[];start=time.time()
 for mode in(1,2):
  for a,b in product(range(len(words)),repeat=2):
   aa,bb=words[a],words[b];H=[(3,),(3,),(2,2,0),(2,2,0),core.A_MODES[mode],core.A_MODES[mode],(2,2,2,0,0,2,0,2),(2,2,2,0,0,2,0,2),aa,bb]
   if len(aa)%2+len(bb)%2==2:
    kind='odd_budget_exhausted_before_upper_exit';wit={'row3_odd_classes':2,'odd_classes_already_fixed_below':6,'each_upper_outgoing_count':[len(aa)-5,len(bb)-5]}
   else:kind,wit=core.assess(H)
   stats[kind]+=1
   if kind=='open_survivor':survivors.append(dict(wit,case=[mode,a,b]))
   else:rejects.append({'case':[mode,a,b],'reason':kind,'witness':wit})
 result={'scope':__doc__,'all_single_cell_count_words':len(allwords),'first_return_filtered_words':len(words),'C_words':words,'paired_cases':sum(stats.values()),'outcomes':dict(stats),'survivors':survivors,'seconds':time.time()-start}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');Path(__file__).with_name('g8_next_c_row_rejection_certificate.json').write_text(json.dumps(rejects,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('C_words','survivors')},indent=2))
if __name__=='__main__':main()
