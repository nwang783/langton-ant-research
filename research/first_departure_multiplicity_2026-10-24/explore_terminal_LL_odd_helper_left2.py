"""Specified odd-helper terminal LL interface, exact two outward squares.
Discovery only; complete WHITE cap-four necessary data, not a board factor.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,ast,time
b=Path(__file__).parent
Q={'__file__':str(b/'explore_two_flat_pair_reader_closure.py')}
exec((b/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],Q)
V,dom,propagate,check=Q['V'],Q['dom'],Q['propagate'],Q['check']
core=json.loads((b/'check_terminal_LL_even_portal_suppliers.json').read_text())
ct=Counter();ans=[];prim=Counter();t=time.time()
G={};TOP={}
for rr in ['SNN','SNNS']:
 G[rr]=[(u,v) for u,v in product(dom((1,-1)),dom((1,0))) if check({(0,-1):'WEE',(0,0):rr,(1,-1):u,(1,0):v})=='open']
 TOP[rr]=[(a,z) for a,z in product(dom((0,0)),dom((1,0))) if check({(0,-1):'WWEE',(1,-1):rr,(0,0):a,(1,0):z})=='open']
for row in core['rows']:
 if row['result']!='open' or row['Y']!='WEE':continue
 hs0={ast.literal_eval(p):h for p,h in row['histories'].items()}
 for (u,v),(a,z) in product(G[hs0[(2,2)]],TOP[hs0[(2,2)]]):
  fixed=hs0|{(3,1):u,(3,2):v,(1,3):a,(2,3):z}
  # Cheap complete physical-count propagation before any chronology test.
  ds=propagate({p:[h] for p,h in fixed.items()})
  if ds is None:continue
  prim['count_compatible']+=1
  r=check(fixed);prim[r]+=1
  if r!='open':continue
  pts=set(fixed)|{(0,3),(-1,3)}
  ds=propagate({p:[fixed[p]] if p in fixed else dom(p) for p in pts})
  if ds is None:ct['empty_closure']+=1;continue
  def visit(ds):
   if all(len(h)==1 for h in ds.values()):
    hs={p:h[0] for p,h in ds.items()};r=check(hs);ct[r]+=1
    if r=='open':ans.append({str(p):h for p,h in sorted(hs.items())})
    return
   p=min((p for p,h in ds.items() if len(h)>1),key=lambda p:len(ds[p]))
   for h in ds[p]:
    nd=propagate(ds|{p:[h]})
    if nd is not None:visit(nd)
  visit(ds)
print('primary',dict(prim),'closure',dict(ct),'open',len(ans),'seconds',time.time()-t)
#print('profiles',Counter((r['(1, 0)'],r['(2, 2)'],r['(3, 1)'],r['(3, 2)'],r['(1, 3)'],r['(2, 3)'],r['(3, 3)'],r['(0, 3)'],r['(3, 0)']) for r in ans))
Path(__file__).with_name('explore_terminal_LL_odd_helper_left2.json').write_text(json.dumps(dict(scope=__doc__,primary_counts=dict(prim),closure_counts=dict(ct),open=ans),indent=2)+'\n')
