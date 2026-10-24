"""Coverage, exact interfaces, and forced-corner formula bindings."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A
M=(1,0,100);N=(1,1,200);C=lambda v:(0,0,v)
PH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def nm(v):a,b,c=v;return [b,a-b,c-100*a-100*b]
def main():
 F=HERE/'first_frontier';L=HERE/'last_frontier';I=read(F/'clean_interface.json');O=read(F/'ordinary_interfaces.json');S=read(F/'scar_certificate.json');J=read(L/'strip_interface.json');P=read(L/'parallel_model_certificate.json');Q=read(L/'localized_scars_certificate.json')
 assert I['fresh_phases']==J['fresh_phases']==PH and O['interface_sha256']==S['interface_sha256']==h(F/'clean_interface.json')
 assert P['strip_interface_sha256']==Q['strip_interface_sha256']==h(L/'strip_interface.json')
 assert len(O['rows'])==21 and {r['phase'] for r in O['rows']}==set(PH)-{72}
 easy={15,28,29,32,38,45,55,56,60,61,62,71};scars={r['phase'] for r in S['rows']};remaining={46,47,57,70,72,75}
 assert scars=={13,14,27,89} and len(easy|scars|remaining)==22 and len(easy)+len(scars)+len(remaining)==22
 parents=[]
 expected={72:[520,208,203112],70:[624,0,212085],75:[728,0,199716],46:[624,312,215346],47:[624,312,215390],57:[624,312,215658]}
 for r in sorted(remaining):
  d=read(F/f'remaining_certificate_r{r}.json');assert d['phase']==r and d['domain']=='m>=100,n-m>=100' and nm(d['total_capture_time'])==expected[r]
  assert d['interface_sha256']==h(F/'clean_interface.json') and d['template_sha256']==h(F/f'full_remaining_template_r{r}.json')
  if r==72:assert d['initial_cell_count']==3 and d['tail_phase']==100 and d['whole_trajectory_upper']=={'u_minus_4m':178,'z':75}
  else:
   o=next(q for q in O['rows'] if q['phase']==r);e=o['exceptional_ray_base'];drift=o['outgoing_drift'];base=(A.add(A.scale(M,2),C(e[0])),A.add(A.scale(M,-2),C(e[1])))
   k=A.add(A.sub(N,M),C(-34 if r==70 else -29)) if r in (70,75) else A.add(A.add(N,M),C(42 if r==57 else 40))
   assert A.nonneg(k);target=A.padd(base,(A.scale(k,drift[0]),A.scale(k,drift[1])))
   x=A.add(A.add(A.scale(N,2),A.scale(M,4)),C(138 if r==57 else 134)) if r in (46,47,57) else A.add(A.scale(N,2),C(-8 if r==70 else 4))
   y=A.add(A.scale(N,-2 if r in (70,75) else 2),C(-14 if r in (70,75) else 41));assert target==(x,y)
   hit=A.add(A.scale(k,104),C(o['capture_time_n_m_constant'][2]-146044+(72-o['tail_phase'])%104));assert hit==tuple(d['forced_corner_source_hit_time'])
   assert d['remote_never_read']==(['d'] if r in (70,75) else ['c'])
   assert A.negative(A.sub(A.add(A.scale(M,4),C(o['full_prefix_u_upper_m'][1])),A.add(x,A.add(A.scale(N,2),C(14)))))
   assert A.negative(A.sub(C(o['full_prefix_z_upper']),A.add(x,A.add(A.scale(N,2),C(41)))))
  parents.append(dict(phase=r,capture_nm=nm(d['total_capture_time']),tail_phase=d['tail_phase']))
 permanent={r['phase'] for r in P['records'] if r['finite_history_transfer']=='permanent'};lastscars={r['phase'] for r in Q['rows']};lastreturns={28,60,61,70,75}
 assert len(P['records'])==22 and {r['phase'] for r in P['records']}==set(PH)
 assert len(permanent)==13 and lastscars==scars and len(permanent|lastscars|lastreturns)==22 and len(permanent)+len(lastscars)+len(lastreturns)==22
 expectedlast={28:[728,0,203308],60:[728,0,210340],61:[624,-104,227540],70:[728,0,212536],75:[728,0,200172]};last=[]
 for r in sorted(lastreturns):
  d=read(L/f'full_return_certificate_r{r}.json');assert nm(d['total_capture_time'])==expectedlast[r] and d['phase']==r and d['remote_d_never_read']
  assert d['template_sha256']==h(L/f'full_return_template_r{r}.json');last.append(dict(phase=r,capture_nm=nm(d['total_capture_time']),tail_phase=d['tail_phase']))
 files={str(p.relative_to(HERE)):h(p) for p in sorted(HERE.rglob('*')) if p.is_file() and p.suffix in ('.py','.json','.md','.gz') and p.name!='manifest.json' and '__pycache__' not in str(p)}
 out=dict(status='all exact executables passed; independent audit pending',domain='each fixed retained core with u>=502; parameter n sufficiently large depending on that core',first_frontier=dict(easy=sorted(easy),scars=sorted(scars),full_history=parents),last_frontier=dict(permanent=sorted(permanent),scars=sorted(lastscars),full_history=last),artifact_sha256=files,scope='Mass-five recurrence exclusion under the established incidence and ordinary-channel lemmas; not a universal highway theorem or a mass-six theorem.')
 (HERE/'manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='artifact_sha256'},indent=2))
if __name__=='__main__':main()
