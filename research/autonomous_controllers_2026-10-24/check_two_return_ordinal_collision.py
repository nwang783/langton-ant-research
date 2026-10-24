#!/usr/bin/env python3
"""Reconstruct two exact open-interface return paths; all-cap ordinal contradiction."""
import json
from pathlib import Path
from check_extremal_read_coupling import D,quotient
BASE=Path(__file__).parent
H=[tuple('NESW'.index(x)for x in w)for w in ['W','','N','SS','WE','WWE','SNN','SSNS','EEWE','WWEW']]
PTS=[(r,t-r)for t in range(-1,4)for r in(0,1)];IX={p:i for i,p in enumerate(PTS)};DRIFT=(2,-2);Q=(2,2)
PATHS=[[(1,2,1),(1,1,0),(0,1,0),(0,2,1),(-1,2,1),(-1,1,0),(-2,1,0),(-2,2,0),(-1,2,2),(-1,1,1),(0,1,1),(0,2,2),(1,2,2),(1,1,1),(2,1,0),(2,0,0),(1,0,0),(1,1,2),(2,1,1)],[(1,2,3),(1,1,3),(2,1,3)]]

def main():
 records=[]
 for raw,wo,ni in zip(PATHS,(1,2),(0,2)):
  events=[]
  for x,y,j in raw:
   p=(x,y);r,k=quotient(p,DRIFT);i=IX[r];h=H[i][j];ho=(h+(1 if j%2==0 else-1))%4
   events.append({'physical_cell':p,'class_index':i,'complete_rank':j,'incoming_heading':h,'outgoing_heading':ho,'turn':'R'if j%2==0 else'L','full_drift_lift':k})
  assert Q not in[e['physical_cell']for e in events]
  assert events[0]['physical_cell']==(Q[0]-1,Q[1]) and events[0]['incoming_heading']==3
  first=events[0];assert [j for j,h in enumerate(H[first['class_index']])if h==3].index(first['complete_rank'])==wo
  last=events[-1];assert last['outgoing_heading']==0 and tuple(last['physical_cell'][z]+D[0][z]for z in(0,1))==Q
  hh=H[last['class_index']];assert [j for j,h in enumerate(hh)if(h+(1 if j%2==0 else-1))%4==0].index(last['complete_rank'])==ni
  for a,b in zip(events,events[1:]):
   p=a['physical_cell'];ho=a['outgoing_heading'];assert tuple(p[z]+D[ho][z]for z in(0,1))==b['physical_cell'] and ho==b['incoming_heading']
   src=[j for j,h in enumerate(H[a['class_index']])if(h+(1 if j%2==0 else-1))%4==ho];dst=[j for j,h in enumerate(H[b['class_index']])if h==ho]
   assert len(src)==len(dst)and src.index(a['complete_rank'])==dst.index(b['complete_rank'])
  records.append({'source_and_target_physical_cell':Q,'outgoing_W_ordinal':wo,'incoming_N_ordinal':ni,'duration':len(events)+1,'internal_events':events,'necessary_rank_identity':f'n{ni}=w{wo}+1'})
 result={'scope':__doc__,'full_drift':DRIFT,'complete_named_histories':{str(p):''.join('NESW'[x]for x in H[i])for i,p in enumerate(PTS)},'returns':records,'abstract_contradiction':'n0=w1+1 implies firstN cannot turnR because its preceding L/W would already arriveN. Hence n0 turnsL and is w2. Then n2=w2+1=n0+1 skips n1.','claim':'This ONE24-event named interface has no alternating upper completion at ANY visit cap, period or width.','not_claimed':'No exclusion of its whole six-cell boundary interface or the full216-case diagonal remainder.'}
 (BASE/'two_return_ordinal_collision.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('returns','complete_named_histories')},indent=2))
if __name__=='__main__':main()
