"""Complete LL3/4->LEFT3 joins to the specified even-root endpoint portal.
Full locally allowed helper profiles, then exact corner closure; no age bound.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b = Path(__file__).parent
L = {'__file__':str(b/'explore_two_flat_pair_reader_closure.py')}
exec((b/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0], L)
V,dom,propagate,check = L['V'],L['dom'],L['propagate'],L['check']
profiles = []
for a,x,y in product(['WWE','WWEW'],dom((2,0)),dom((2,1))):
    if check({(1,0):a,(1,1):'SSN',(2,0):x,(2,1):y}) == 'open':
        profiles.append((a,x,y))
assert len(profiles) == 13
rows = []
total = Counter()
for a,x,y in profiles:
    fixed = {(1,0):a,(1,1):'SSN',(2,0):x,(2,1):y,
             (0,1):'WE',(0,2):'SNNS',(-1,2):'EEWW',(-1,1):'SS',(1,2):'WWEE'}
    pts = set(fixed)
    while True:
        cand = {(p[0]+v[0],p[1]+v[1]) for p in pts for v in V.values()} - pts
        add = {q for q in cand if sum((q[0]+v[0],q[1]+v[1]) in pts for v in V.values()) >= 2}
        if not add: break
        pts |= add
    ds = propagate({p:[fixed[p]] if p in fixed else dom(p) for p in sorted(pts)})
    counts = Counter()
    opened = []
    if ds is None:
        counts['primary_PORT'] += 1
    else:
        def rec(ds):
            if all(len(v) == 1 for v in ds.values()):
                hs = {p:v[0] for p,v in ds.items()}
                result = check(hs)
                counts[result] += 1
                if result == 'open': opened.append({str(p):h for p,h in hs.items()})
                return
            p = min((p for p in ds if len(ds[p]) > 1), key=lambda p:len(ds[p]))
            for h in ds[p]:
                nd = propagate(ds | {p:[h]})
                if nd is not None: rec(nd)
        rec(ds)
    print(a,x,y,dict(counts),'open',len(opened),flush=True)
    total.update(counts)
    rows.append(dict(A=a,X=x,Y=y,closure_cells=sorted(pts),counts=dict(counts),open=opened))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,local_profile_count=13,summary=dict(total),rows=rows,warning='Exact specified local joins only, not a full front or general no-LL theorem.'),indent=2)+'\n')
print('TOTAL',dict(total))
