"""Four full-field clean-SE rejoins and all-parameter future transparency."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,step,plan,canonical_source,multiple
M=(1,0,100);N=(1,1,200);C=lambda v:(0,0,v)
OLD=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
def nn(a,b):return A.add(A.scale(N,a),C(b))
def main():
 interface=json.loads((HERE/'clean_interface.json').read_text());ordinary=json.loads((HERE/'ordinary_interfaces.json').read_text());assert ordinary['interface_sha256']==hashlib.sha256((HERE/'clean_interface.json').read_bytes()).hexdigest()
 oldscars={r['phase']:r for r in json.loads((ROOT/'scattering/retained_frontier/localized_scars.json').read_text())['rows']};rows=[];scarpoints={}
 for r in (13,14,27,89):
  row=next(q for q in ordinary['rows'] if q['phase']==r);age=row['source_age'];phase=row['tail_phase'];steps=row['capture_time_n_m_constant'][2]-146044-r
  B,p,h=canonical_source(age,r);B.symmetric_difference_update({p})
  for _ in range(steps):p,h,_=step(B,p,h)
  assert hashlib.sha256(repr(sorted(B)).encode()).hexdigest()==row['source_record_field_sha256']
  _,q,hh=canonical_source(0,phase);j=multiple((p[0]-q[0],p[1]-q[1]),(2,-2));assert j is not None and h==hh and j>=0
  ref,qq,hq=canonical_source(age+j,phase);ref={(x+2*j,y-2*j) for x,y in ref};assert (qq[0]+2*j,qq[1]-2*j)==p and hq==h
  scar=B^ref;physical={(40+x,-52+y) for x,y in scar};assert physical=={(25-x,-23-y) for x,y in oldscars[r]['scar_base']}
  geo=104*j+phase;delay=r+steps-geo;assert delay=={13:20,14:120,27:132,89:32}[r]
  # The extra old deposits in both age-m states are the identical untouched
  # copies indexed age+1..m; E_n is likewise unchanged, so all cancel.
  assert age<M[2] and oldscars[r]['source_age']==age
  assert A.negative(A.sub(C(geo),A.add(A.scale(A.sub(N,M),104),C(-2084))))
  assert A.negative(A.sub(A.add(A.scale(M,4),C(row['full_prefix_u_upper_m'][1])),nn(4,22)))
  assert A.negative(A.sub(C(row['full_prefix_z_upper']),nn(4,49)))
  tw=W[phase:]+W[:phase];qs,_,end,eh=plan(tw,p,h);assert (end[0]-p[0],end[1]-p[1])==(2,-2) and eh==h
  for target in scar:
   for q in qs:
    k=multiple((target[0]-q[0],target[1]-q[1]),(2,-2));assert k is None or k<0
  scarpoints[r]=[(A.add(A.scale(M,2),C(x)),A.add(A.scale(M,-2),C(y))) for x,y in physical]
  rows.append(dict(phase=r,source_age=age,source_recovery=steps,geometric_reference_time=geo,time_delay=delay,scar_base=sorted(physical),scar_size=len(scar)))
 T=json.loads(OLD.read_text());p=A.point(0,0);h=0;elapsed=C(0);checks=0
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'};qs,_,end,eh=plan(word,(0,0),h)
  count=None if s['type']=='finite' else nn(*s['count'])
  if count is not None:assert len(word)==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
  if i>=10:
   for q in set(qs):
    q=A.translate_local(q,p,0)
    for points in scarpoints.values():
     for target in points:
      if count is None:assert A.no_point_collision(q,target)
      else:assert not A.ray_membership(target,q,end,count)
      checks+=1
  if count is None:p=A.translate_local(end,p,0);elapsed=A.add(elapsed,C(len(word)))
  else:p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,104))
  h=eh
 assert p==(nn(-2,-58),nn(2,98)) and h==0 and elapsed==nn(728,200304)
 tw=T['infinite_tail_word'];assert tw==W[100:]+W[:100];qs,_,end,eh=plan(tw,(0,0),h);assert end==(-2,2) and eh==h
 for q in set(qs):
  q=A.translate_local(q,p,0)
  for points in scarpoints.values():
   for target in points:
    k=A.line_coordinate(A.psub(target,q),end);assert k is None or A.negative(k);checks+=1
 out=dict(status='four exact full-field rejoins, untouched remote markers and permanent transparency',domain='m>=100,n-m>=100',rows=rows,read_scar_nonincidences=checks,full_five_cell_capture='728n+200304+delta_r',full_five_cell_pose=[['-2n-58','2n+98'],0],interface_sha256=hashlib.sha256((HERE/'clean_interface.json').read_bytes()).hexdigest(),template_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest())
 (HERE/'scar_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
