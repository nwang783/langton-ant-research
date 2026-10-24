from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/six_C_successor_frozen_20261023_1505';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_six_C_gate_first_successor.json').read_text());u,h=G[7][:2];assert(u,h)==(4j,0)
center2=lambda p,h:2*p+rotation(-1-1j,h)
target=center2(4j,2);assert target==1+9j
rows=[]
for a,wrd in [('D',raws[0]),('C',C)]:
 e,dh=walk(wrd)[:2];p=u+e;assert center2(p,dh)==target
 rows.append((a,(*xy(p),dh),xy(target),int(a=='C')))
assert set(rows)=={(r['next_atom'],tuple(r['next_exit']),(1,9),r['next_exit_C_clock'])for r in J['actual_next_atom_exit_checks']}
assert all(r['has_immediate_C']==(counts[r['full_source']]>0)for r in J['full_source_cases'])
assert all(r['excluded_after_plain_U']==(base[r['next_full_packet']]==0)for r in J['next_full_packet_cases'])
out=dict(status='PASS independent exact center-vertex successor reduction',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),doubled_center_equalities=rows,scope='Only remaining six-C FIRST-contact gate: source plain U, following base V/U. Old static UC eligibility is not a first-contact history; no gate exclusion or attainment.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
