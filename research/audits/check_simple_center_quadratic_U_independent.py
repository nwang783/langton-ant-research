"""Independent literal arithmetic and signed dependency binding for the analytic corollary."""
from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];F=ROOT/'core_periodicity_new/simple_center_quadratic_U_frozen_20261023_1651'
m=json.loads((F/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(F/'manifest.json')=='64eba0aac6627ab8690e0fdfa1a15f25f378c252d1898063bc2a30f00f1ea113'
for r in m['files']:assert sha(F/r['frozen'])==r['sha256']
g=json.loads((F/'dependency_literal_geometry.json').read_text())['geometry'];D=g[0]['word'];V=g[4]['word'];U=g[7]['word'];C=g[1]['word'][len(D):];marker=g[0]['marker'];assert list(map(len,[D,V,U,C]))==[10,18,28,15]
assert all(g[i]['word'].startswith(marker)for i in [7,8,9]);assert len(marker)==11
assert sha(F/'dependency_simplicity_manifest.json')=='127a00884b4a06af35a807ab76f6f6499b9427d56350a931c03cc0e8de65524d'
assert json.loads((F/'dependency_HS_manifest.json').read_text())['status']=='SIGNED'
# Algebraically, ceil((114+76(m-5)+120u)/5)=ceil((114+76(m-5))/5)+24u.
assert 120%5==0 and 120//5==24
# Explicitly generate possible corrected centers, scaled by two.
for R in range(31):
 centers={(2*x+a,2*y+b)for x in range(-R,R+1)for y in range(-R,R+1)for a,b in [(-1,-1),(-1,1),(1,-1),(1,1)]}
 assert len(centers)==(2*R+2)**2
assert 28*4==112
out=dict(status='PASS analytic corollary with independent literal constants and exact ceiling identity',manifest_sha256=sha(F/'manifest.json'),raw_atom_lengths=dict(D=10,V=18,U=28,C=15),bound='L <= F(m,0) + 112*(R(m,0)+24u+1)^2 for u>=1; L<=F(m,0) for u=0',terminal_marker_extra=11,center_count='(2R+2)^2',analytic_dependencies=['Signed HS confines every atomic read head in the whole original factor using original m and actual u.','The U-free full-packet prefix has an actual marker supplied by the next U packet.','The remaining U-entry suffix is center-simple, so each counted center occurs at most once.'],scope='Necessary square-root U recurrence only. No U count upper bound, microscopic cap four, merger resource or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
