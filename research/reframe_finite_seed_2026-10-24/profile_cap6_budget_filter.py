"""Apply the general forced-output import-budget trap to exact profile lifts.
Trap lemma is a separate proof artifact; no pairwise composability is inferred.
"""
from active_flight import *
from pathlib import Path
import json
p=Path(__file__).parent;C=json.loads((p/'kernel_M6_compact_returns.json').read_text())['returns'];F=json.loads((p/'cap6_physical_return_filter.json').read_text());yes=[];no=[];proof=[]
for i in F['feasible_indices']:
 B=set(map(tuple,F['minimal_finite_seeds'][str(i)]));pp=(0,0);h=0
 for c in C[i]['word']:
  assert ('L'if pp in B else'R')==c;pp,h=step(B,pp,h)
 w=cursor(pp,h);d=rot((-2,2),h);first=w[0]+d[0],w[1]+d[1];U=set()
 for z in range(4):
  d=rot((-2,2),(h+z)%4);U|=comp(B,1,(w[0]+d[0],w[1]+d[1]))
 trap=len(U)>=3 or len(U)==2 and first not in vertices(U,1)
 if trap:
  no.append(i);proof.append({'index':i,'final_pose':[pp,h],'mandatory_field':sorted(B),'neighbor_component_union':sorted(U),'first_tip':first,'first_tip_in_union':first in vertices(U,1)})
 else:yes.append(i)
out={'scope':'Author exact full-profile mandatory-output budget filter; requires separately proved arbitrary-exterior trap lemma. Not cross-block realizability.','surviving_indices':yes,'trapped_indices':no,'trap_witnesses':proof};(p/'cap6_profile_budget_filter.json').write_text(json.dumps(out,indent=2)+'\n');print('survive',len(yes),'trapped',len(no))
from collections import Counter
print('surviving words',dict(Counter(C[i]['word']for i in yes)))
