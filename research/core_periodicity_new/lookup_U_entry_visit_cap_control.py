"""Existing-corpus check for a >4 physical-read U-entry control, not a cap proof."""
import json
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parent
D=json.loads((R/'chronology_dcuv/literal_factor_dfa_k7.json').read_text());G=json.loads((R/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
words=[tuple(w) for w in D['states'] if w and w[0] in (7,8,9)]
for i,w in enumerate(D['states']):
 if len(w)==6 and w[0] in (7,8,9):words.extend(tuple(w+[a]) for a,t in zip(IDS,D['transitions'][D['state_to_class'][i]]) if t>=0)
words=sorted(set(words),key=lambda w:(len(w),w));st=((0,1),(1,0),(0,-1),(-1,0));best=None;hit=None
for wi,w in enumerate(words):
 p,h=(0,0),0;c=Counter()
 for a in w:
  for t in G[a]['word']:
   c[p]+=1;h=(h+(-1 if t=='L' else 1))%4;p=p[0]+st[h][0],p[1]+st[h][1]
 m=max(c.values())
 if best is None or m>best['raw_max_visits']:
  best={'word':w,'names':[G[a]['name'] for a in w],'raw_max_visits':m,'max_cells':[q for q,n in c.items() if n==m]}
 if m>4:hit=best;break
out={'scope':'Existing fixed k7 corpus, raw reads only; no negative visit-cap theorem.','total_saved_U_entry_words':len(words),'checked':wi+1,'best':best,'countercontrol_to_cap_four':hit}
(R/'chronology_dcuv/U_entry_raw_visit_cap_lookup.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
