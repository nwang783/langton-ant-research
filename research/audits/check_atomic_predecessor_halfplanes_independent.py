from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_predecessor_halfplanes_frozen_20261023_1505';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_predecessor_bud_halfplanes.json').read_text());roles=[]
for a in ids:
 p,h=G[base[a]][:2]
 for j in range(counts[a]+1):
  bud=p+rotation(1-1j,h);assert bud in G[a][4]
  roles.append((a,j,(*xy(p),h),xy(bud)))
  p+=rotation(1j,h);h=(h-1)%4
assert len(roles)==15
assert set(roles)=={(r['full_producer'],r['atomic_prefix_C'],tuple(r['atomic_exit']),tuple(r['bud_full_output_slot']))for r in J['all_15_predecessor_atomic_roles']}
ends=[]
for h in(0,1):
 for a in(0,4,7):
  step=rotation(G[a][0],h);assert step.real>=0
  for z in G[a][3]:
   p=1-1j-rotation(z,h);e=p+step;assert e.real>=1
   ends.append((a,xy(z),h,xy(p),xy(e)))
# Author table fields are checked without executing its endpoint code.
assert len(ends)==16
R=J['all_16_retiring_base_endpoints'];assert len(R)==16
assert set(ends)=={(r['retiring_base'],tuple(r['input_slot']),r['heading'],tuple(r['base_entry']),tuple(r['base_exit'])) for r in R}
assert all(r['retirement_C_gap_after_A']==(3 if r['heading']==1 else 4) for r in R)
assert rotation(walk(C)[0],1)==1
assert walk(C+mark)[2][2]is False
out=dict(status='PASS independent predecessor atomic roles and halfplane endpoints',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),roles=roles,endpoints=ends,scope='1325 post-exit maturity plus actual consuming BASE cones. Target may split full consumer C tails. Noninitial actual atomic source; 4C first contact must start at factor-first D, with real initial exception.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
