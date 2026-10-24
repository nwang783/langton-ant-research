from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_D_first_W5_gate_independent.py');exec(compile(S.read_text().split('rows=[];late=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/three_C_left_boundary_frozen_20261023_1516';M=json.loads((B/'manifest.json').read_text())
for z in M['files']:assert hashlib.sha256((B/z['frozen']).read_bytes()).hexdigest()==z['sha256']
J=json.loads((B/'02_three_C_left_step_boundary.json').read_text());auth={(r['previous_full'],r['target_full']):r for r in J['all24_previous_packet_target_tail_queries']};rows=[]
for a in ids:
 c=counts[a];ph=c;p=-rotation(G[a][0],ph);bud=rotation(1-1j-p,-ph);assert bud in G[a][4]
 rel=rotation(-1-p,-ph);dh=(1-ph)%4
 for b in(4,5,6):
  assert -1+rotation(1+2j,1)==1-1j
  hb=(a,b,*xy(rel),dh,*xy(bud));cq=(mp[a],mp[b],*xy(rel),dh,*xy(bud),3+c)
  if hb in HB:why='SIGNED_HB'
  elif cq in C5:why='SIGNED_COUNT5'
  elif c==2:
   at=p+rotation(G[base[a]][0],ph);hh=ph
   at+=rotation(1j,hh);hh=(hh-1)%4
   assert(at,hh)==(-1,1);assert -c+1==-1 and 3-(-1)==4
   why='SIGNED_ATOMIC_FOUR_C_FULL_POSE_NONRETURN'
  else:
   assert a==0 and b in(4,5)and(p,ph)==(-1-1j,0);why='PLAIN_D_PREDECESSOR_MUST_BE_FACTOR_FIRST'
  rr=auth[a,b];assert tuple(rr['HB_key'])==hb and tuple(rr['count5_key'])==cq and rr['reason']==why
  assert tuple(rr['previous_pose'])==(*xy(p),ph)and tuple(rr['target_relative_pose'])==(*xy(rel),dh)
  rows.append((a,b,why))
for b in(4,5,6):assert G[b][2][2+1j]is False and -1+rotation(2+1j,1)==-2j
assert len(rows)==24
out=dict(status='PASS independent general three-C complete-boundary left-step law',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),queries=rows,scope='ANY outgoing source type at A0,N; V-family B(-1,0,E) at3C forces A first or second, second preceded by factor-first plain D and targetV/VC. Actual last-C nonreturn and predecessor-bud interfaces retained. No funding/first-contact premise or global closure.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
