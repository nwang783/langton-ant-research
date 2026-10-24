"""Discovery: full mixed incoming predecessor at the exact ODD-root portal.
Selected F=(1,0) maximum, complete WHITE cap-four readers, no age bound.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b=Path(__file__).parent;S={'__file__':str(b/'check_even_root_portal_incoming_predecessor.py')}
exec((b/'check_even_root_portal_incoming_predecessor.py').read_text().split('# Derive every possible')[0],S)
words,out,dom,propagate,at_F,V,H=[S[k] for k in ['words','out','dom','propagate','at_F','V','H']]
vs=[h for h in words('EW') if h and out(h,0)=='N' and sum(out(h,r)=='N' for r in range(len(h)))==1]
localct=Counter();ct=Counter();ans=[];profiles=Counter()
for q,c in [('SSN','WWE'),('SSNS','WWEW')]:
 for v,x,h in product(vs,dom((2,0)),dom((2,1))):
  fixed={(1,0):v,(1,1):q,(2,0):x,(2,1):h,(0,1):'WE',(0,2):'SNN',(-1,2):'EEWW',(-1,1):'SS',(1,2):c}
  res,cert=at_F({p:fixed[p] for p in [(1,0),(1,1),(2,0),(2,1)]});localct[res]+=1
  if res!='open':continue
  pts=set(fixed)|{(-1,0),(0,0),(2,2)}
  ds=propagate({p:[fixed[p]] if p in fixed else dom(p) for p in pts})
  if ds is None:ct['empty_closure']+=1;continue
  def visit(ds):
   if all(len(h)==1 for h in ds.values()):
    hs={p:h[0] for p,h in ds.items()};res,cert=at_F(hs);ct[res]+=1
    if res=='open':
     pred=[]
     for z in [(0,0),(2,0)]:
      hh=hs[z]
      if hh:
       dr=out(hh,0);dest=z[0]+V[dr][0],z[1]+V[dr][1]
       if dest==(1,0):pred.append(z)
     ct['incoming_b_available' if pred else 'no_incoming_b']+=1
     if pred:
      profiles[q,v,x,h,hs[(2,2)]]+=1
      ans.append(dict(histories={str(p):z for p,z in sorted(hs.items())},incoming_predecessors=pred))
    return
   p=min((p for p,h in ds.items() if len(h)>1),key=lambda p:len(ds[p]))
   for candidate in ds[p]:
    nd=propagate(ds|{p:[candidate]})
    if nd is not None:visit(nd)
  visit(ds)
print('LOCAL',dict(localct),'CORE',dict(ct));print('PROFILES',dict(profiles))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,local_counts=dict(localct),closure_counts=dict(ct),profiles={str(k):v for k,v in profiles.items()},open=ans),indent=2)+'\n')
