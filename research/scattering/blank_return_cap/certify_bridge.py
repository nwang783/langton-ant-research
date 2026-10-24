"""All m,k>=100 complete-history transfer to five fixed blank endcaps."""
import json,hashlib
from pathlib import Path
from discover import ROOT,HERE,initial
import sys
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import P,D,W,plan,step
S=ROOT/'scattering/ordinary_reverse_interface';BAD=[13,14,27,28,60,70,75,89]
u=lambda p:p[0]-p[1];z=lambda p:sum(p)
rot=lambda p:(p[1],-p[0])
def main():
 interfaces=json.loads((S/'interfaces.json').read_text());assert interfaces['unprotected_backward_phases']==BAD
 C=json.loads((HERE/'fixed_caps.json').read_text());caps={r['phase']:r for r in C['rows']};rows=[]
 B=set();p=(0,0);h=0
 for _ in range(9977):p,h,ch=step(B,p,h)
 assert p==(-15,10) and h==3
 E=B^{(p[0]+rot(q)[0],p[1]+rot(q)[1]) for q in P};assert min(map(z,E))==-21
 # Old SW deposits are all parallel to (-2,-2), with u<=-18. Their
 # omitted index j>=m portion lies strictly below the comparison half-plane.
 old_u_max=-25+max(u(rot(q)) for q in D);assert old_u_max==-18
 old_omission_z_max=-5-4*100+max(z(rot(q)) for q in D);assert old_omission_z_max<-250
 for r in BAD:
  R=json.loads((S/f'certificate_r{r}.json').read_text());assert R['capture_time'][0]==104 and R['tail_phase']==0 and R['tail']['drift']==[-2,2]
  (px,py),h=R['capture_pose'];assert h==0 and px[0]==2 and py[0]==-2
  kind=13 if r in (13,14,27,89) else r;extra=1 if r==27 else 0;cap=caps[kind]
  target=(-55+py[1]+2*extra,-30-px[1]+2*extra);assert list(target)==cap['start'][0] and cap['start'][1]==1
  # All local packet writes, initial active P, and missing old SW deposits
  # are below z=-250, independently of both parameters.
  packet_z_upper=-5-4*100-R['prefix_u_lower'];assert packet_z_upper<-250
  active_core_z_upper=-5-4*100+max(z(rot(q)) for q in P);assert active_core_z_upper<-250
  Jmin=100+100-20+extra;assert Jmin>=180
  qs,_,end,eh=plan(W,target,1);assert end==(target[0]+2,target[1]+2) and eh==1
  # The entire NE flight before the fixed cap misses E and every omitted
  # old SW deposit. Existing local packet debris is handled by the exact
  # full-kernel infinite-tail theorem, rather than a spatial guess.
  assert max(map(z,qs))-4 < min(map(z,E))
  assert min(map(u,qs))>old_u_max
  # Canonical P/odd-write identity: after J periods, all missing incoming
  # NE-past deposits and the start P lie below the comparison half-plane.
  rotNE=lambda q:(-q[1],q[0])
  omitted_incoming_z_max=z(target)+max(z(rotNE(q)) for q in D)-4*(Jmin+1);assert omitted_incoming_z_max<-250
  initial_incoming_z_max=z(target)-4*Jmin+max(z(rotNE(q)) for q in P);assert initial_incoming_z_max<-250
  entry_constant=9977+R['capture_time'][1]+104*(-20+extra)
  permanent=cap['full_halfplane_transfer']
  if permanent:assert cap['entire_future_z_lower']>=-125
  rows.append(dict(phase=r,cap_type=kind,extra_NE_period=extra,cap_entry_time_m_k_constant=[208,208,entry_constant],cap_start=[target,1],complete_history_comparison='exact on z>=-250',local_packet_write_z_upper_at_m100=packet_z_upper,permanent_transfer=permanent,capture_time_m_k_constant=[208,208,entry_constant+cap['capture']] if permanent else None,final_pose=cap['pose'] if permanent else None,final_phase=cap['tail_phase'] if permanent else None,drift=cap['drift'] if permanent else None,packet_certificate_sha256=hashlib.sha256((S/f'certificate_r{r}.json').read_bytes()).hexdigest()))
 assert [r['phase'] for r in rows if r['permanent_transfer']]==[13,14,27,60,70,75,89]
 out=dict(status='all eight complete inputs reach the exact fixed-cap interface; seven permanent captures',domain='independent integers m,k>=100',rows=rows,scope='The r28 SW cap output can re-enter old finite debris; its infinite model is not transferred without a further proof.',ordinary_interfaces_sha256=hashlib.sha256((S/'interfaces.json').read_bytes()).hexdigest(),fixed_caps_sha256=hashlib.sha256((HERE/'fixed_caps.json').read_bytes()).hexdigest())
 (HERE/'bridge.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
