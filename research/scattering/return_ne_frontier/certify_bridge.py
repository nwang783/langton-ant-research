"""Five complete q_n+s_m histories reach fixed central endcaps.

The proof uses an exact decomposition of every old field component, then
whole-half-plane agreement, not an extrapolation of local model repetitions.
"""
import json,hashlib,gzip,sys
from pathlib import Path
from discover_caps import initial,ROOT,HERE,BAD,CAPS
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import P,D,W,plan,step
SRC=ROOT/'scattering/far_se_core/last_frontier';INTER=ROOT/'scattering/far_sw_core';TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
u=lambda p:p[0]-p[1];z=lambda p:sum(p)
def rot(q,r):
 for _ in range(r%4):q=(q[1],-q[0])
 return q
def plus(p,q):return tuple(a+b for a,b in zip(p,q))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 assert sha(INTER/'return_interface.json')=='ef89eaee1bc786c91a0e330b54cd09f04757f71b754dec7ad486e02f7f66aac8';assert sha(SRC/'parallel_model_certificate.json')=='6567c62a4b67a42d66d40c34bada6d468d1dd4e0ccca3101be1b1093b587455f';I=json.loads((INTER/'return_interface.json').read_text());models=json.loads((SRC/'parallel_model_certificate.json').read_text());caps=json.loads((HERE/'fixed_caps.json').read_text());assert I['source_template_sha256']==sha(TFILE)=='16246ec40cbdd4ad94c35698992582b27a942dc7d539683f1b3684892cd5687d';assert I['old_SE_rail_offset']==[3,-77] and I['model_strip_u']==[-200,200]
 T=json.loads(TFILE.read_text());assert T['segments'][1]['word']==W and T['segments'][1]['count']==[1,8] and T['segments'][3]['word']==W and T['segments'][3]['count']==[1,7]
 B=set();p=(0,0);h=0
 for _ in range(9977):p,h,ch=step(B,p,h)
 assert p==(-15,10) and h==3;E=B^{plus(p,rot(q,1)) for q in P};assert len(E)==702 and (min(map(z,E)),max(map(z,E)))==(-21,35) and (min(map(u,E)),max(map(u,E)))==(-34,48)
 # Complete finite packet G_n is translate_{(-2n,-2n)} G0, after
 # subtracting BOTH canonical cores, not just its freshly visited cells.
 assert T['segments'][2]['type']=='finite';word=T['segments'][2]['word'];assert word and set(word)<={'R','L'};reads,_,end,eh=plan(word,(-31,-6),3);assert end==(6,-43) and eh==1
 G={plus((-31,-6),rot(q,1)) for q in P}^{(-33,-14)}^{plus((6,-43),rot(q,3)) for q in P}
 for q in reads:G.symmetric_difference_update({q})
 assert max(map(z,G))==7
 sw_u=(min(u(plus((-15,10),rot(d,1))) for d in D),max(u(plus((-15,10),rot(d,1))) for d in D));assert sw_u==(-28,-18)
 incoming_omitted_z_constant=-37-4+max(z(rot(d,3)) for d in D);assert incoming_omitted_z_constant==-32
 rows=[]
 for r in BAD:
  row=next(q for q in models['records'] if q['phase']==r);cap=next(q for q in caps['rows'] if q['phase']==r);assert cap['start']==[list(CAPS[r]),1] and cap['full_halfplane_transfer'];assert cap['drift']==[2,2]
  word=gzip.open(SRC/f'word_r{r}_mature1.txt.gz','rt').read();assert len(word)==row['local_capture'] and hashlib.sha256(word.encode()).hexdigest()==row['word_sha256'];model_reads,_,mp,mh=plan(word,(0,0),0);assert [list(mp),mh]==row['local_pose'];phase=row['word_phase'];assert row['drift']==[-2,2]
  advance=(-phase)%104;extra,_,mp,mh=plan((W[phase:]+W[:phase])[:advance],mp,mh);local=[plus((6,-43),rot(q,1)) for q in model_reads+extra];p0=plus((6,-43),rot(mp,1));assert (mh+1)%4==1
  cp=CAPS[r];a,b=(cp[0]-p0[0]),(cp[1]-p0[1]);assert a==b and a%2==0;c=a//2;Jmin=100+c;assert Jmin>=1
  qs,_,end,eh=plan(W,cp,1);assert end==plus(cp,(2,2)) and eh==1
  start_reads,_,_,_=plan(W,p0,1)
  lower_z_constant=min(map(z,local+start_reads));local_z_max=max(map(z,local));future_u_min=min(min(map(u,local)),min(map(u,qs)))
  # Actual-minus-model is E, two omitted SW half-rays, G_n, and
  # incoming NE deposits j>=n-m+1. The latter two are below ALL
  # post-core model reads; the SW discrepancy misses them by u.
  assert future_u_min>sw_u[1]
  assert -4*100+max(7,incoming_omitted_z_constant)<lower_z_constant
  assert local_z_max-400 < min(map(z,E))
  assert max(map(z,qs))-4 < min(map(z,E))
  # The strip theorem supplies local color validity; these guards extend
  # it to every pre-cap NE read even after leaving that strip.
  assert all(-200<=u(q)<=200 for q in model_reads)
  # Whole cap half-plane equality. Every term not retained by the cap
  # model is strictly below z=-250, including both start cores.
  bounds={
   'old_SW_omissions':-5-4*(200+8)+max(z(rot(d,1)) for d in D),
   'q_packet':-4*200+max(map(z,G)),
   'old_NE_deposits':-4*100+incoming_omitted_z_constant,
   'local_initial_core':-4*100-37+max(z(rot(q,3)) for q in P),
   'local_recovery_writes':local_z_max-400,
   'new_flight_start_core':z(cp)-4*Jmin+max(z(rot(q,3)) for q in P),
   'new_flight_omitted_past':z(cp)-4*(Jmin+1)+max(z(rot(d,3)) for d in D)}
  assert max(bounds.values())<-250
  entry_constant=61927+len(word)+advance+104*c
  assert entry_constant=={28:66185,60:62313,61:92097,70:67647,75:63171}[r]
  assert cap['entire_future_z_lower']>=-125
  rows.append(dict(phase=r,NE_phase_zero_pose_before_flight_constant=p0,advance_to_phase_zero=advance,NE_flight_count_m_constant=[1,c],cap_start=cap['start'],cap_entry_time_n_constant=[208,entry_constant],capture_time_n_constant=[208,entry_constant+cap['capture']],capture_pose=cap['pose'],capture_phase=cap['tail_phase'],drift=cap['drift'],comparison='complete finite field equals cap field on all z>=-250',discarded_component_z_upper=bounds,pre_cap_model_read_z_lower_m_constant=[-4,lower_z_constant],pre_cap_model_u_lower=future_u_min,model_word_sha256=row['word_sha256']))
 out=dict(status='five exact complete finite q_n+s_m captures via a whole-half-plane endcap interface',domain='m>=100,n-m>=100, independently',rows=rows,q_packet_size=len(G),q_packet_z_upper_n_constant=[-4,7],old_SW_u_bounds=sw_u,interface_sha256=sha(INTER/'return_interface.json'),model_certificate_sha256=sha(SRC/'parallel_model_certificate.json'),fixed_caps_sha256=sha(HERE/'fixed_caps.json'),scope='Other remote corners may still interrupt the final NE fronts; their recurrence coupling is separate.')
 (HERE/'bridge.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
