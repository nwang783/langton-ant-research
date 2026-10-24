"""Exact translating-profile controls: standard104 positive, corner writer negative.
No candidate cycle or cap table enumeration is performed.
"""
from pathlib import Path
import json,hashlib
from translating_component_profile_lift import lift,kinematics,required_initial
from finite_component_profile_lift import transform
from active_flight import comp,cursor,sector,step,ray_epoch,rot
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
STD=ROOT/'recovered_bundle/ant_global/root/standard.json'
FRONT=ROOT/'standard_unread_cap_2026-10-23/standard_w_frontier_certificate.json'
WRITER=ROOT/'reframe_finite_seed_2026-10-24/cap6_resource_obstruction.json'
s=json.loads(STD.read_text());f=json.loads(FRONT.read_text());W=s['word'];C=[]
for a in f['phases']:
 p,h=a['pose'];C.append(comp(set(map(tuple,a['black_frontier'])),0,tuple(a['w_cursor'])))
x=lift(W,C,(0,0),3);assert x['status']=='ACTUAL_FINITE_INPUT_TRANSLATING_FULL_PROFILE'
seed=set(map(tuple,x['initial_black']));extra={(1000,1000)}
for q in extra:
 assert all((n:=ray_epoch(q,g['cell'],tuple(x['drift'])))is None or n<0 for g in x['guards'])
B=seed|extra;p=(0,0);h=3;checks=0
for t in range(104*8):
 n,i=divmod(t,104);d=tuple(x['drift']);expected={(q[0]+n*d[0],q[1]+n*d[1])for q in C[i]}
 assert comp(B,0,cursor(p,h))==expected and W[i]==('L'if p in B else'R') and extra<=B
 p,h=step(B,p,h);checks+=1
# Rigid-motion covariance is an exact additional control, not a new candidate.
pbase=(31,-18);hh=1;Cr=[]
for a in C:Cr.append({(pbase[0]+v[0],pbase[1]+v[1])for q in a for v in[rot(q,hh)]})
y=lift(W,Cr,pbase,(3+hh)%4);assert y['status']==x['status']
assert set(map(tuple,y['initial_black']))=={(pbase[0]+v[0],pbase[1]+v[1])for q in seed for v in[rot(q,hh)]}
a=json.loads(WRITER.read_text())['cycles'][0];p=(0,0);h=0;CW=[]
for t in a['transitions']:
 CW.append(transform(t['input_component'],p,h));v=rot(tuple(t['output_pose'][0]),h);p=(p[0]+v[0],p[1]+v[1]);h=(h+t['output_pose'][1])%4
z=lift(a['word'],CW);assert z['status'].startswith('NO_')
for name,v in [('standard104',x),('standard104_rigid_motion',y),('corner_writer',z)]:
 (OUT/f'translating_profile_{name}_certificate.json').write_text(json.dumps(v,indent=2)+'\n')
res=dict(status='PASS supplied translating full-profile controls',standard_seed_size=len(seed),standard_seed=sorted(seed),standard_drift=x['drift'],maximum_active=x['maximum_complete_active_mass'],whole_board_literal_phase_checks=checks,remote_unread_extra=sorted(extra),rigid_motion_status=y['status'],corner_writer_status=z['status'],corner_writer_first_black_tail=z.get('first_black_tail'),source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [STD,FRONT,WRITER]},scope='The all-time lift follows from the symbolic drift-ray proof.832literal phases and rigid covariance are controls only. The corner-writer negative certificate is a necessary initial-color obstruction, not automatically the strongest finite-prefix obstruction.')
(OUT/'translating_profile_lift_controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
