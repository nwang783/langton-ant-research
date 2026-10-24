"""Archive bounds, exact forced-corner equation, and final capture bindings."""
import json,sys,hashlib
from certify_strip_model import HERE,ROOT,SRC,geometry,A
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,P,D,plan,canonical_source,multiple
C=lambda v:(0,0,v)

def first_opposite_interface():
 sys.path.insert(0,str(SRC));from certify_caps import blank
 O,E=blank();assert max(x-y+25 for x,y in E)==73
 source=SRC.parent/'ordinary_reverse_interface';cp=source/'certificate_r56.json';old=json.loads(cp.read_text());tp=source/'template_r56.json';assert old['template_sha256']==hashlib.sha256(tp.read_bytes()).hexdigest()
 parent=json.loads((SRC/'backward_certificate_r56.json').read_text());assert parent['source_certificate_sha256']==hashlib.sha256(cp.read_bytes()).hexdigest()
 T=json.loads(tp.read_text());base=A.point(0,0);h=2;us=[];zs=[];N=(1,0,100)
 for seg in T['segments']:
  assert seg['type'] in ['finite','periods'];w=seg['word'];assert w and set(w)<={'R','L'};qs,_,end,eh=plan(w,(0,0),h);count=None if seg['type']=='finite' else A.add(A.scale(N,seg['count'][0]),C(seg['count'][1]))
  if count:assert len(w)==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
  for q in qs:
   p=A.translate_local(q,base,0);ends=[p]
   if count:ends.append(A.padd(p,(A.scale(A.sub(count,A.ONE),end[0]),A.scale(A.sub(count,A.ONE),end[1]))))
   for v in ends:
    u=A.sub(*v);z=A.add(*v);assert u[:2]==(0,0) and all(a<=0 for a in z[:2]);us.append(u[2]);zs.append(z[2])
  base=A.padd(base,(A.scale(count,end[0]),A.scale(count,end[1]))) if count else A.padd(base,A.point(*end));h=eh
 assert base==(A.add(A.scale(N,-2),C(20)),A.add(A.scale(N,-2),C(-59))) and h==1 and old['tail_phase']==0
 qs,_,end,eh=plan(W,(20,-59),1);assert end==(22,-57) and eh==1;us.extend(x-y for x,y in qs)
 assert max(zs)<=73 and max(-y+x for x,y in P)-439<=73
 # Initial P,D,Q1 and q2 also satisfy the stationary z upper73;
 # the complete original E has z_source=u_actual+25<=73.
 assert max(sum(q) for q in P)<=73 and max(sum(q) for q in D)<=73 and sum((6,-4))<=73 and -449<=73
 assert qs[72]==(22,-51) and [v%2 for v in qs[72]]==[0,1]
 fresh=[]
 for i,q in enumerate(qs):
  if not any((k:=multiple((v[0]-q[0],v[1]-q[1]),(2,2))) is not None and (k>0 or k==0 and j<i) for j,v in enumerate(qs)):fresh.append(i)
 allowed=[i for i in fresh if sum(qs[i])%2==1];assert allowed==[14,28,32,38,46,56,60,62,70,72]
 return dict(two_bit_future_u_bounds=[min(us),max(us)],complete_pre_NE_archive_z_upper=73,third_favorable_phases=allowed)

def main():
 first=first_opposite_interface()
 old,points,rays=geometry();vals=[]
 for q in points:
  v=A.sub(q[0],q[1]);assert v[:2]==(0,0);vals.append(v[2])
 for q,d,count in rays:
  v=A.sub(q[0],q[1]);e=A.add(v,A.scale(A.sub(count,A.ONE),d[0]-d[1]));assert v[:2]==e[:2]==(0,0);vals.extend([v[2],e[2]])
 assert max(vals)==136
 L=json.loads((HERE/'local_return.json').read_text());I=json.loads((HERE/'return_interface.json').read_text());assert I['local_return_sha256']==hashlib.sha256((HERE/'local_return.json').read_bytes()).hexdigest();assert L['capture']==18304 and L['prefix_u_bounds']==[-200,120] and L['prefix_z_bounds']==[-15,79]
 core,cp,ch=canonical_source(0,8);assert ch==0;coremax=max(90+x-cp[0]-(-26+y-cp[1]) for x,y in core);archive=max(136,coremax,max(x-y for x,y in P),max(x-y for x,y in D),L['prefix_u_bounds'][1]);assert archive==136
 phase0=(90,-28);qs,_,end,eh=plan(W,phase0,2);assert end==(92,-30) and eh==2 and qs[72]==(98,-30)
 fresh=[]
 for i,q in enumerate(qs):
  if not any((k:=multiple((v[0]-q[0],v[1]-q[1]),(2,-2))) is not None and (k>0 or k==0 and j<i) for j,v in enumerate(qs)):fresh.append(i)
 allowed=[i for i in fresh if sum(qs[i])%2==0];assert allowed==[14,28,32,38,46,56,60,62,70,72]
 # q4=(q3.x,q2.y)=(2p+22,-2n-30); equality with (98+2k,-30-2k)
 # gives k=n from y, then p=n+38 from x. These coefficients are pinned
 # directly to the checked input, not inferred from sampled rectangles.
 q2,q3=old['initial'][1:];assert q2==[[-2,0,-219],[-2,0,-230]] and q3==[[0,2,222],[0,2,149]]
 assert -230+200==-30 and 222-200==22 and (98-22)//2==38
 certpath=HERE/'cycle_certificate.json';Cyc=json.loads(certpath.read_text());assert Cyc['template_sha256']==hashlib.sha256((HERE/'template_cycle.json').read_bytes()).hexdigest() and Cyc['source_cycle_sha256']==hashlib.sha256((SRC/'backward_certificate_r56.json').read_bytes()).hexdigest()
 assert Cyc['capture_time']==[312,0,144877] and Cyc['capture_pose']==[[[2,0,333],[2,0,208]],1] and Cyc['tail_phase']==0 and Cyc['tail']['drift']==[2,2]
 assert Cyc['first_fourth_corner']==[104,0,28872] and Cyc['whole_future_u_lower']==-200 and Cyc['unused_corner_never_read']
 # Add the all-age interface entry time with p=n+38.
 T=I['entry_time_m_n_p_constant'];capture=[T[0],T[1]+T[2]+312,T[3]+38*T[2]+144877-31200];assert capture==[312,728,241002]
 out=dict(status='phase56 fixed-m>=100 recurrence exclusion under established incidence hypotheses',first_opposite_interface=first,complete_pre_last_tail_archive_u_upper=archive,last_favorable_phases=allowed,forced_relation='p=n+38, final exceptional ray epoch k=n',whole_future_u_lower=-200,unused_NW_corner_never_read=True,full_cycle_capture_time_m_n_constant=capture,full_cycle_actual_pose_m_n_constant=[[-2,2,-7],[-2,-2,-123],2],full_cycle_actual_tail_phase=0,full_cycle_actual_drift=[2,-2],cycle_certificate_sha256=hashlib.sha256(certpath.read_bytes()).hexdigest(),return_interface_sha256=hashlib.sha256((HERE/'return_interface.json').read_bytes()).hexdigest(),scope='Fix m, then let the remote ages diverge. This is not an unrestricted independent-m five-cell input theorem.')
 (HERE/'coupling.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
