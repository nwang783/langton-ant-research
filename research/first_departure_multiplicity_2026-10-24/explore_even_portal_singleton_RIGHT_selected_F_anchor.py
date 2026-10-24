"""Complete terminal LL supplier cover at the specified even-root portal.
All local WHITE cap-four histories, exact corner closure, and literal clocks.
A failed constructive guide attempt is NOT an impossibility certificate.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b = Path(__file__).parent
L = {'__file__':str(b/'explore_two_flat_pair_reader_closure.py')}
exec((b/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0], L)
VEC, dom, propagate, check = L['V'], L['dom'], L['propagate'], L['check']
Q = {}
exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0], Q)
exact = Q['exact']
raw_check=check
def check(hs): return raw_check({(p[0]-1,p[1]-1):h for p,h in hs.items()})
local = []
local_counts = Counter()
for a,x,y in product(['W'],dom((2,0)),dom((2,1))):
    result = check({(1,0):a,(1,1):'SSN',(2,0):x,(2,1):y})
    local_counts[result] += 1
    if result == 'open': local.append((a,x,y))
print('local',dict(local_counts),local)
rows = []
counts = Counter()
open_profiles = Counter()
for a,x,y in local:
    fixed = {(1,0):a,(1,1):'SSN',(2,0):x,(2,1):y,
             (0,1):'WE',(0,2):'SNNS',(-1,2):'EEWW',(-1,1):'SS',(1,2):'WWEE'}
    points = set(fixed)
    while True:
        candidates = {(p[0]+v[0],p[1]+v[1]) for p in points for v in VEC.values()} - points
        added = {q for q in candidates if sum((q[0]+v[0],q[1]+v[1]) in points for v in VEC.values()) >= 2}
        if not added: break
        points |= added
    assert len(points) == 12
    domains = propagate({p:[fixed[p]] if p in fixed else dom(p) for p in sorted(points)})
    assert domains is not None
    def visit(ds):
        if all(len(h) == 1 for h in ds.values()):
            hs = {p:h[0] for p,h in ds.items()}
            result = check(hs)
            raw, certificate = exact(hs)
            if result == 'skipped_rank': assert raw == 'rank'
            else: assert raw == 'open'
            counts[result] += 1
            row = dict(A=a,X=x,Y=y,histories={str(p):h for p,h in hs.items()},result=result,physical_certificate=certificate)
            if result == 'open':
                open_profiles[a,x,y] += 1
                pass
            rows.append(row)
            return
        p = min((p for p in ds if len(ds[p]) > 1),key=lambda p:len(ds[p]))
        for h in ds[p]:
            nxt = propagate(ds | {p:[h]})
            if nxt is not None: visit(nxt)
    visit(domains)
print('CLOSURE',dict(counts),dict(open_profiles)); Path(__file__).with_suffix('.json').write_text(json.dumps(dict(local=local,counts=dict(counts),profiles={str(k):v for k,v in open_profiles.items()},rows=rows),indent=2)+'\n')
