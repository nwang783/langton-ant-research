"""Exact joining of the physically realized LL-drop mode to an even portal.
One specified shared-history interface, not a length or period scan.
"""
from pathlib import Path
from collections import Counter
import json
b = Path(__file__).parent
L = {'__file__':str(b/'explore_two_flat_pair_reader_closure.py')}
exec((b/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0], L)
V,dom,propagate,check = L['V'],L['dom'],L['propagate'],L['check']
fixed = {(1,0):'WWEW',(1,1):'SSN',(2,0):'SNNN',(2,1):'EE',
         (0,1):'WE',(0,2):'SNNS',(-1,2):'EEWW',(-1,1):'SS',(1,2):'WWEE'}
pts = set(fixed)
while True:
    cand = {(p[0]+v[0],p[1]+v[1]) for p in pts for v in V.values()}-pts
    add = {q for q in cand if sum((q[0]+v[0],q[1]+v[1]) in pts for v in V.values()) >= 2}
    if not add: break
    pts |= add
ds = propagate({p:[fixed[p]] if p in fixed else dom(p) for p in sorted(pts)})
counts = Counter()
open_rows = []
if ds is None: counts['initial_PORT'] += 1
else:
    print('domains',{p:w for p,w in ds.items() if len(w)>1},flush=True)
    def rec(ds):
        if all(len(w)==1 for w in ds.values()):
            hs = {p:w[0] for p,w in ds.items()}
            result = check(hs)
            counts[result] += 1
            if result == 'open': open_rows.append({str(p):h for p,h in hs.items()})
            return
        p = min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
        for h in ds[p]:
            nd = propagate(ds | {p:[h]})
            if nd is not None:rec(nd)
    rec(ds)
print('cells',len(pts),'counts',counts,'open',len(open_rows),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,fixed={str(p):h for p,h in fixed.items()},cells=sorted(pts),counts=dict(counts),open=open_rows,warning='Necessary local composition only; no physical factor or complete front.'),indent=2)+'\n')
