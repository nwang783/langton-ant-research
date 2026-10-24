"""Complete original-history transfer and opposite-corner recurrence guards."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'));from bivariate import A
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,P,plan
K=(1,0,100);N=(0,1,200);C=lambda x:(0,0,x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lin(a,b,c):return A.add(A.add(A.scale(K,a),A.scale(N,b)),C(c))
def point(p):return tuple(tuple(x) for x in p)
def rot(q,r):
 for _ in range(r%4):q=(q[1],-q[0])
 return q
def main():
 B=json.loads((HERE.parent/'bridge.json').read_text());I=json.loads((HERE.parent/'mass5_interfaces.json').read_text());CAP=json.loads((HERE.parent/'fixed_caps.json').read_text());assert I['bridge_sha256']==sha(HERE.parent/'bridge.json') and B['fixed_caps_sha256']==sha(HERE.parent/'fixed_caps.json');rows=[]
 for r in [70,75]:
  cert=json.loads((HERE/f'certificate_r{r}.json').read_text());T=json.loads((HERE/f'template_r{r}.json').read_text());assert cert['template_sha256']==sha(HERE/f'template_r{r}.json') and cert['cap_certificate_sha256']==sha(HERE.parent/'fixed_caps.json');br=next(x for x in B['rows'] if x['phase']==r);old=next(x for x in I['rows'] if x['phase']==r);cap=next(x for x in CAP['rows'] if x['phase']==r)
  D=point(cert['initial_marker']);expectedD=(lin(2,0,-10),lin(2,0,-69)) if r==70 else (lin(2,0,48),lin(2,0,9));assert D==expectedD
  # Before the cap, the entire previous field is retained by the inherited
  # half-plane identity. D lies above every earlier read, not merely the cap.
  assert A.nonneg(A.sub(A.add(*D),C(old['complete_archive_z_upper']+1)))
  assert max(br['discarded_component_z_upper'].values())<-250
  assert cert['whole_future_z_lower']==-105 and -105>=-125>-250
  assert cert['first_contact']==list(A.add(A.scale(K,104),C(cap['capture']+72)))
  assert cert['tail']['drift']==[-2,2]
  p,h=cert['capture_pose'];p=point(p);phase=cert['tail_phase'];tw=T['infinite_tail_word'];assert tw==W[phase:]+W[:phase]
  qs,_,delta,h=plan(tw[:(-phase)%104],(0,0),h);p=A.translate_local(delta,p,0);assert h==0
  reads=plan(W,(0,0),0)[0];fresh=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
  target=A.translate_local(reads[72],p,0);assert all(v[0]%2==v[1]%2==0 for v in target)
  if r==70:assert tuple(v[2]%2 for v in target)==(0,0)
  assert [j for j in fresh if sum(A.translate_local(reads[j],p,0)[i][2] for i in [0,1])%2==0]==[14,28,32,38,46,56,60,62,70,72]
  core=[A.translate_local(rot(q,2),p,0) for q in P];ub=[A.sub(*q) for q in core];assert all(u[:2]==(0,0) for u in ub)
  lo=min(old['complete_archive_u_bounds'][0],cert['finite_prefix_u_bounds'][0],min(u[2] for u in ub));hi=max(old['complete_archive_u_bounds'][1],cert['whole_future_u_upper'],max(u[2] for u in ub));assert (lo,hi)==(-82,{70:122,75:142}[r])
  Q=(lin(0,-2,-33),lin(0,-2,-14));NW=(Q[0],D[1]);SE=(D[0],Q[1]);au=A.sub(*NW);cu=A.sub(*SE);assert A.nonneg(A.sub(C(lo-1),au)) and A.nonneg(A.sub(cu,C(hi+1)))
  # C misses the finite prefix and the entire outgoing NW tail.
  assert A.nonneg(A.sub(cu,C(cert['whole_future_u_upper']+1)))
  if r==70:
   assert au==lin(-2,-2,36) and cu==lin(2,2,4)
   assert all((a[0]%2,a[1]%2,a[2]%2)==(0,0,1) for a in NW)
   assert A.nonneg(A.sub(C(lo-1),A.add(au,C(58))))
   result='A either misses the final NW front or is an ordinary favorable impact; its entire recovery lies below the complete archive. C never read.'
  else:
   assert au==lin(-2,-2,-42) and cu==lin(2,2,62)
   lower=tuple(cert['tail_z_bounds'][0]);assert lower==lin(4,0,45);assert A.nonneg(A.sub(lower,A.add(A.add(*NW),C(1))))
   result='Both unused A and C miss every read, including the final infinite NW tail; complete five-cell capture for independent m,n-m,k>=100.'
  entry=br['cap_entry_time_n_constant'][1];total=A.add(A.scale(N,208),A.add(C(entry),tuple(cert['capture_time'])));first=A.add(A.scale(N,208),A.add(C(entry),tuple(cert['first_contact'])))
  assert total==lin({70:208,75:312}[r],208,{70:127655,75:219742}[r]);assert first==lin(104,208,{70:68135,75:113683}[r])
  rows.append(dict(phase=r,marker=D,three_cell_capture_time_n_k_constant=[208,{70:208,75:312}[r],{70:127655,75:219742}[r]],first_D_time_n_k_constant=[208,104,{70:68135,75:113683}[r]],capture_pose=cert['capture_pose'],tail_phase=phase,complete_archive_u_bounds=[lo,hi],A_u=au,C_u=cu,phase72_ray=target,unused_A=NW,unused_C=SE,result=result,certificate_sha256=sha(HERE/f'certificate_r{r}.json')))
 out=dict(status='two complete-history all-age transfers and fixed-core mass-five opposite-corner exclusions',domain='m>=100,n-m>=100,k>=100; mass-five recurrence fixes m before remote ages diverge',rows=rows,bridge_sha256=sha(HERE.parent/'bridge.json'),archive_sha256=sha(HERE.parent/'mass5_interfaces.json'))
 (HERE/'interface.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
