"""Reuse an identical certified one-rail model under exact rotation."""
import json,hashlib,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];OLD=ROOT/'scattering/far_se_core/last_frontier'
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan
PH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 I=json.loads((HERE/'return_interface.json').read_text());P=json.loads((OLD/'parallel_model_certificate.json').read_text());J=json.loads((OLD/'strip_interface.json').read_text())
 assert I['old_SE_rail_offset']==J['old_SE_rail_offset']==[3,-77] and P['strip_interface_sha256']==h(OLD/'strip_interface.json')
 assert I['fresh_phases']==J['fresh_phases']==PH and len(P['records'])==22
 rows=[]
 for r in P['records']:
  if r['finite_history_transfer']!='permanent':continue
  assert -200<=r['source_u_bounds'][0]<=r['source_u_bounds'][1]<=200
  assert -200<=r['tail_source_u_bounds'][0]<=r['tail_source_u_bounds'][1]<=200
  x,y=r['local_pose'][0];heading=(r['local_pose'][1]+1)%4;dx,dy=r['drift'];drift=(dy,-dx);assert drift in ((2,-2),(-2,2))
  phase=r['word_phase'];qs,_,d,eh=plan(W[phase:]+W[:phase],(0,0),r['local_pose'][1]);assert list(d)==r['drift'] and eh==r['local_pose'][1]
  e=qs[(72-phase)%104];ex=(6+y+e[1],-43-x-e[0]);target=(1,1) if drift==(-2,2) else (0,0)
  rows.append(dict(phase=r['phase'],capture_n_m_constant=[208,-104,61927+r['local_capture']],pose_constant=[[6+y,-43-x],heading],translation_per_m=[-2,-2],drift=drift,tail_phase=phase,actual_postcore_z_bounds_m=[-4,-37-max(r['source_u_bounds'][1],r['tail_source_u_bounds'][1]),-37-min(r['source_u_bounds'][0],r['tail_source_u_bounds'][0])],exceptional_ray_base=ex,exceptional_target_parity=target,exceptional_parity_matches=tuple(v%2 for v in ex)==target))
 assert [r['phase'] for r in rows]==[15,29,32,38,45,46,47,55,56,57,62,71,72]
 out=dict(status='thirteen complete finite q_n+s_m parent captures by identical-model rotation',domain='m>=100,n-m>=100',interface_sha256=h(HERE/'return_interface.json'),model_certificate_sha256=h(OLD/'parallel_model_certificate.json'),rows=rows,scope='No assertion that the other three mass-five remote markers are absent from the subsequent NW/SE rays. Their scattering remains a separate obligation.')
 (HERE/'return_transfers.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
