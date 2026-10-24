"""Discovery: upper physical completion of the exact odd-root portal.
Necessary complete cap-four local histories only, not an attained factor.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,ast
b=Path(__file__).parent;S={'__file__':str(b/'check_even_root_portal_incoming_predecessor.py')};exec((b/'check_even_root_portal_incoming_predecessor.py').read_text().split('# Derive every possible')[0],S)
words,dom,propagate,at_F,analyze=[S[k] for k in ['words','dom','propagate','at_F','analyze']]
core=json.loads((b/'explore_odd_root_portal_incoming_modes.json').read_text())['open'];tops={};top_counts={}
for c,r in [('WWE','SNN'),('WWE','SNNS'),('WWEW','SSSN')]:
 tops[c,r]=[];cc=Counter()
 for a,z in product(words('NS'),words('EW')):
  hs={(0,-1):c,(1,-1):r,(0,0):a,(1,0):z};res,_=analyze(hs);cc[res]+=1
  if res=='open':tops[c,r].append((a,z))
 top_counts[c,r]=dict(cc)
ct=Counter();ans=[];pr=Counter()
for row in core:
 hs0={ast.literal_eval(p):h for p,h in row['histories'].items()}
 for a,z in tops[hs0[(1,2)],hs0[(2,2)]]:
  fixed=hs0|{(1,3):a,(2,3):z};pts=set(fixed)|{(0,3),(-1,3)}
  ds=propagate({p:[fixed[p]] if p in fixed else dom(p) for p in pts})
  if ds is None:ct['empty']+=1;continue
  def visit(ds):
   if all(len(h)==1 for h in ds.values()):
    hs={p:h[0] for p,h in ds.items()};res,cert=at_F(hs);ct[res]+=1
    if res=='open':
     pr[hs[(1,1)],hs[(1,0)],hs[(2,0)],hs[(2,1)],hs[(2,2)],a,z,hs[(0,3)],hs[(-1,3)]]+=1
     ans.append(dict(histories={str(p):z for p,z in sorted(hs.items())},incoming_predecessors=row['incoming_predecessors']))
    return
   p=min((p for p,h in ds.items() if len(h)>1),key=lambda p:len(ds[p]))
   for candidate in ds[p]:
    nd=propagate(ds|{p:[candidate]})
    if nd is not None:visit(nd)
  visit(ds)
print('TOP',top_counts,'MODES',tops);print('CLOSURE',dict(ct),'OPEN',len(ans));print('profiles',dict(pr))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,top_counts={str(k):v for k,v in top_counts.items()},top_modes={str(k):v for k,v in tops.items()},counts=dict(ct),profiles={str(k):v for k,v in pr.items()},open=ans),indent=2)+'\n')
