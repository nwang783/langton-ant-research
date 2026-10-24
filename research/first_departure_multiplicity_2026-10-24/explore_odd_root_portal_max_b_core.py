"""Discovery: local GLOBAL-M first-R incidence core of odd-root completions.
External predecessor ports remain open. Survivors are not b-cycles/fronts.
"""
from pathlib import Path
from collections import Counter
import json,ast
b=Path(__file__).parent;S={'__file__':str(b/'check_even_root_portal_incoming_predecessor.py')};exec((b/'check_even_root_portal_incoming_predecessor.py').read_text().split('# Derive every possible')[0],S)
at_F,out,V,fp=[S[k] if k!='fp' else S['S'][k] for k in ['at_F','out','V','fp']]
raw=json.loads((b/'explore_odd_root_portal_upper_completion.json').read_text())['open'];ans=[];counts=Counter();profiles=Counter()
for row in raw:
 hs={ast.literal_eval(p):h for p,h in row['histories'].items()};res,cert=at_F(hs);assert res=='open'
 val={tuple(p):z for p,z in cert['face_values']};val={(p[0]+1,p[1]+1):z for p,z in val.items()}
 allowed={p for p,h in hs.items() if h and val[fp(p,out(h,0))[0]]==0};removed=[]
 while True:
  remove=[]
  for p in allowed:
   possible=False
   for dr in set(hs[p]):
    q=p[0]-V[dr][0],p[1]-V[dr][1]
    if val[fp(q,dr)[0]]!=0:continue
    if q not in hs:possible=True;continue
    if q not in allowed:continue
    if out(hs[q],0)==dr:possible=True
   if not possible:remove.append(p)
  if not remove:break
  allowed-=set(remove);removed.append(remove)
 required={(1,1),(0,1),(0,2),(-1,2),(-1,1)}
 ok=required<=allowed;counts['open' if ok else 'no_max_b_predecessor']+=1
 if ok:
  profiles[hs[(1,1)],hs[(1,0)],hs[(2,0)],hs[(2,1)]]+=1
  ans.append(row|{'remaining_known_max_b_vertices':sorted(allowed),'removed_rounds':removed})
print(dict(counts),dict(profiles))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,counts=dict(counts),profiles={str(k):v for k,v in profiles.items()},open=ans),indent=2)+'\n')
