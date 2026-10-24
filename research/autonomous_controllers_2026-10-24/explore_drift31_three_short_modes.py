#!/usr/bin/env python3
"""Discovery only: derived T9 interfaces for three short all-quad modes."""
import json
from collections import Counter
import explore_drift31_inventory20 as m
from pathlib import Path
R=Path(__file__).resolve().parent
q=json.load(open(R/'drift31_circle_T8_discovery.json'));out=[];total=Counter()
for c in q['cases'][1:4]:
 H0={t:tuple(h)for t,h in enumerate(c['histories'])};S=Counter();opens=[];outcomes=[]
 for h in c['survivors']:
  H=H0|{8:tuple(h)};k,G,rp=m.paths(H,9);I=len(m.depart(h,3));J=H0[6].count(2);dd=[]
  for parity in[0,1]:dd+=list(m.generated(1,2*(I+J)+1,3,I,2,J,parity,rp[0]))
  T=Counter()
  for w in dd:
   kind,g=m.Gof(H|{9:w});S[kind]+=1;T[kind]+=1
   if kind=='open':opens.append({'T8':h,'T9':w})
  outcomes.append({'T8':h,'domain_count':len(dd),'outcomes':dict(T)})
 out.append({'T6':H0[6],'T7':H0[7],'counts':dict(S),'T8_details':outcomes,'open_interfaces':opens});total.update(S)
 print('CASE', ''.join('NESW'[x]for x in H0[6]),''.join('NESW'[x]for x in H0[7]),dict(S),flush=True)
 (R/'drift31_three_short_T9_discovery.json').write_text(json.dumps({'scope':__doc__,'cases':out,'total':dict(total)}))
