"""All independent ages m,n,p>=100: exact actual-blank central-cap transfer."""
import json,hashlib,sys
from pathlib import Path
from certify_caps import HERE,ROOT,blank
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,plan
u=lambda p:p[0]-p[1];z=lambda p:sum(p)
rot=lambda p:(p[1],-p[0]);rotNE=lambda p:(-p[1],p[0]);plus=lambda a,b:tuple(x+y for x,y in zip(a,b))
def main():
 O,E=blank();assert min(map(z,E))==-21 and max(map(z,E))==35
 old_us=[u(O)+u(rot(q)) for q in D];assert [min(old_us),max(old_us)]==[-28,-18]
 old_omission_z_max=z(O)-4*100+max(z(rot(q)) for q in D);assert old_omission_z_max<-250
 old_SW_archive_z_upper=z(O)+max(z(rot(q)) for q in D);assert old_SW_archive_z_upper<=35
 caprows=json.loads((HERE/'caps.json').read_text())['rows'];assert [r['phase'] for r in caprows]==[29,32,56,71];rows=[]
 for cap in caprows:
  r=cap['phase'];cp=HERE/f'backward_certificate_r{r}.json';C=json.loads(cp.read_text());assert C['template_sha256']==hashlib.sha256((HERE/f'template_r{r}.json').read_bytes()).hexdigest()
  assert C['canonical_older_deposits_protected'] and C['capture_time'][:2]==[208,208]
  base,h=C['capture_pose'];assert all(v[:2]==[0,0] for v in base);p=tuple(v[2] for v in base);ph=C['tail_phase'];tw=W[ph:]+W[:ph];ell=(-ph)%104;qs,_,p0,h0=plan(tw[:ell],p,h);assert h0==0
  packet_min=min(C['prefix_u_bounds'][0],*(u(q) for q in qs)) if qs else C['prefix_u_bounds'][0]
  for q in C['initial']:
   assert [q[0][i]-q[1][i] for i in range(2)]==[0,0];packet_min=min(packet_min,q[0][2]-q[1][2])
  packet_min=min(packet_min,min(map(u,P)),min(u(plus(p0,(-x,-y))) for x,y in P))
  packet_z_upper=z(O)-400-packet_min;assert packet_z_upper<-250
  target=tuple(cap['start'][0]);constant=plus(O,rot(p0));dx=target[0]-constant[0];dy=target[1]-constant[1];assert dx==dy and dx%2==0;L=dx//2;Jmin=100+L;assert Jmin>=50
  reads,_,end,eh=plan(W,target,1);assert end==plus(target,(2,2)) and eh==1
  # Before the cap, all ordinary NE epochs are below the stationary E.
  # Local packet intersections are handled by the complete all-parameter
  # backward-tail proof, not discarded; the old SW rail is disjoint.
  assert max(map(z,reads))-4<min(map(z,E))
  assert max(max(map(z,E)),old_SW_archive_z_upper,max(map(z,reads)))==35
  incoming_us=[u(q) for q in reads];assert max(incoming_us)<min(old_us) or min(incoming_us)>max(old_us)
  omitted_incoming_z_max=z(target)+max(z(rotNE(q)) for q in D)-4*(Jmin+1);initial_incoming_z_max=z(target)-4*Jmin+max(z(rotNE(q)) for q in P);assert max(omitted_incoming_z_max,initial_incoming_z_max)<-250
  absolute=C['capture_time'][2]-100*sum(C['capture_time'][:2]);entryconstant=9977+absolute+ell+104*L;assert entryconstant=={29:121681,32:116019,56:120573,71:124667}[r];permanent=cap['permanent_halfplane_transfer']
  if permanent:assert cap['entire_future_z_lower']>=-123 and entryconstant+cap['capture']=={29:122097,32:116435,71:132779}[r]
  # q2 and q3 cannot alter the original blank prefix: actual u=z_source-25.
  q2,q3=C['initial'][1:];assert all(q2[0][i]+q2[1][i]<=0 for i in range(2));assert q2[0][2]+q2[1][2]-25<-34
  assert all(q3[0][i]+q3[1][i]>=0 for i in range(2));assert q3[0][2]+q3[1][2]-25>48
  row=dict(phase=r,phase_zero_source=p0,phase_zero_offset=ell,entry_NE_count_m_constant=[1,L],cap_entry_time_m_n_p_constant=[208,208,208,entryconstant],cap_start=cap['start'],local_packet_z_upper_at_m100=packet_z_upper,old_blank_prefix_protected=True,complete_field_comparison='identical on every cell z>=-250, with all omitted history retained outside',permanent_transfer=permanent,capture_time_m_n_p_constant=[208,208,208,entryconstant+cap['capture']] if permanent else None,pose=cap['pose'] if permanent else None,final_phase=cap['tail_phase'] if permanent else None,drift=cap['drift'] if permanent else None,packet_certificate_sha256=hashlib.sha256(cp.read_bytes()).hexdigest())
  rows.append(row)
 out=dict(status='four exact complete-history cap entries; three complete finite three-cell families',domain='independent integers m,n,p>=100',rows=rows,caps_sha256=hashlib.sha256((HERE/'caps.json').read_bytes()).hexdigest(),scope='Phase56 transfers only through the cap prefix. Remaining cross corners require fixed-m recurrence coupling, not an unrestricted five-cell assertion.')
 (HERE/'cap_bridge.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
