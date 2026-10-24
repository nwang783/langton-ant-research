"""A complete whole-half-plane identity removing the original blank-core age."""
import json,gzip,hashlib,sys
from pathlib import Path
from certify_strip_model import HERE,ROOT,SRC
sys.path.insert(0,str(SRC));from certify_caps import blank
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,P,D,plan
u=lambda p:p[0]-p[1];z=lambda p:sum(p)
def main():
 B=json.loads((SRC/'cap_bridge.json').read_text());bridge=next(r for r in B['rows'] if r['phase']==56);caps=json.loads((SRC/'caps.json').read_text());cap=next(r for r in caps['rows'] if r['phase']==56);assert B['caps_sha256']==hashlib.sha256((SRC/'caps.json').read_bytes()).hexdigest();assert bridge['packet_certificate_sha256']==hashlib.sha256((SRC/'backward_certificate_r56.json').read_bytes()).hexdigest()
 assert bridge['cap_entry_time_m_n_p_constant']==[208,208,208,120573] and bridge['entry_NE_count_m_constant']==[1,-35] and bridge['cap_start']==[[-61,-62],1]
 assert cap['capture']==4264 and cap['pose']==[[11,-26],1] and cap['tail_phase']==8 and cap['drift']==[-2,-2]
 word=gzip.open(SRC/'cap_r56.txt.gz','rt').read();assert hashlib.sha256(word.encode()).hexdigest()==cap['word_sha256'];reads,_,end,eh=plan(word,(-61,-62),1);assert end==(11,-26) and eh==1
 partial=(W[8:]+W[:8])[:96];rr,_,actualstart,ah=plan(partial,end,eh);assert actualstart==(9,-26) and ah==3
 # Under the inverse original-front coordinate change, actual(x,y) is
 # source(10-2m-y,x+15+2m). The new source SE phase0 pose is therefore
 # (36-2m,24+2m), with u=12-4m and z=60.
 source_start_constant=(10-actualstart[1],actualstart[0]+15);assert source_start_constant==(36,24)
 entry=(-70,130);Kconst=-53;assert (source_start_constant[0]+2*Kconst,source_start_constant[1]-2*Kconst)==entry and 100+Kconst>=47
 # Every difference between the true post-cap field and the completed
 # three-rail field lies belowu=-250. Each displayed maximum is at m=100;
 # its coefficient of m is -4, so it decreases for every larger m.
 O,E=blank();assert min(map(z,E))==-21
 original_error=max(-405-min(map(z,E)),max(map(u,D))-400)
 old_NW_core_max=118-400-min(map(u,P))
 old_NW_omission_max=118-400-min(map(u,D))
 cap_write_max=-405-min(map(z,reads+rr))
 new_SE_start_core_max=12-400+max(map(u,P))
 new_SE_omission_max=u(entry)-4*(100+Kconst+1)+max(map(u,D))
 errors=dict(original_blank_residual=original_error,old_NW_end_core=old_NW_core_max,old_NW_omitted_deposits=old_NW_omission_max,cap_and_partial_writes=cap_write_max,new_SE_start_core=new_SE_start_core_max,new_SE_omitted_deposits=new_SE_omission_max)
 assert max(errors.values())<-250
 # Until entry, the actual standard SW return also follows the cap model.
 # Every extra local packet, active core, or infinite-rail extension of
 # that model starts to the right ofu=-52, whereas all pre-entry reads
 # lie to its left. Thus no unproved step crosses an unguarded boundary.
 C=json.loads((SRC/'backward_certificate_r56.json').read_text());assert C['prefix_u_bounds'][0]==-52
 assert min(map(u,P))>=-52 and all(q[0][2]-q[1][2]>=-52 for q in C['initial'])
 assert -22-max(map(u,P))>=-52 and -22-max(map(u,D))>=-52 and min(map(u,D))>=-52
 qs,_,nxt,nh=plan(W,entry,2);assert nxt==(-68,128) and nh==2 and max(map(u,qs))-4<-52
 entrytime=[312,208,208,120573+4264+96+104*Kconst];assert entrytime==[312,208,208,119421]
 L=json.loads((HERE/'local_return.json').read_text());assert L['strip_model_sha256']==hashlib.sha256((HERE/'strip_model.json').read_bytes()).hexdigest() and L['capture']==18304 and L['whole_future_u_lower']>=-250 and L['whole_future_z_bounds'][0]>=-100 and L['whole_future_z_bounds'][1]<=100
 capture=entrytime.copy();capture[3]+=L['capture'];assert capture==[312,208,208,137725]
 out=dict(status='exact complete-field identity on all source cells u>=-250',domain='independent original-core m and remote ages n,p, all>=100',entry=[entry,2],entry_time_m_n_p_constant=entrytime,difference_u_upper_at_m100=errors,difference_u_m_coefficient=-4,reference_field='full canonical packet plus completed old SE rail, completed NW rail from(2,24), and new SE core/past at(-70,130)',three_cell_capture_time_m_n_p_constant=capture,three_cell_capture_actual_pose_affine_m=[[-2,-41],[-2,-80],1],three_cell_capture_phase=8,three_cell_capture_actual_drift=[-2,-2],cap_bridge_sha256=hashlib.sha256((SRC/'cap_bridge.json').read_bytes()).hexdigest(),local_return_sha256=hashlib.sha256((HERE/'local_return.json').read_bytes()).hexdigest(),scope='Full three-cell finite-seed capture. Two additional remote cycle corners require the separately stated fixed-m coupling.')
 (HERE/'return_interface.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
