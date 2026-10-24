"""Literal wake profile and exact scalar-clock value; general ordering is analytic."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import hashlib,json
R=Path(__file__).resolve().parents[1];H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];p=0j;d=1;hist=defaultdict(list)
for t,c in enumerate(H):
 x,y=int(p.real),int(p.imag);hist[x-y,x%2].append((t-104*(x//2),c));d*=(-1j if c=='R'else 1j);p+=d
assert(p,d)==(2+2j,1)
W=[]
for q,h in hist.items():
 h.sort();assert h[0][1]=='R'and all(a[1]!=b[1]for a,b in zip(h,h[1:]))
 if len(h)%2:W.append(q)
# Rotate physical coordinates clockwise: (x',y')=(y,-x), producer heading S,
# sector sign+1, a=b=4, M=6, w=4^(y-x). f is reciprocal-symmetric.
phi=-sum(F(-1)**gap*(6*(F(4)**gap+F(4)**(-gap))-2)for gap,parity in W)
assert phi==F(733866133,4096)and phi>=208
note=R/'causal_reduction/unit_scale/oblique_wake_irreversibility.md'
out=dict(status='PASS exact literal104 profile functional; general common-period order and finite endpoint argument analytically reviewed',wake_orbits=len(W),clock_parameters=dict(a=4,b=4,M=6,rotated_sector_sign=1),profile_gain=str(phi),necessary_gain=208,note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),scope='Same-sector complete parallel oblique profile restorations are impossible. Finite-length corollary needs uniformly bounded endpoint repair/residue count and normal coordinate. No arbitrary output, changed direction/sector, or universal eraser/capture theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
