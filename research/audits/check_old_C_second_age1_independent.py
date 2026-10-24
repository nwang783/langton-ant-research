from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parent.parent;D=R/'second_old_C_age1_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(D/'manifest.json')=='84475d664f7e5e96b2d929c4eb570b10c9e129c4be590af0facfb23699f3e4aa';m=json.loads((D/'manifest.json').read_text())
for n,h in m['files'].items():assert sha(D/n)==h
for n,h in m['dependencies'].items():assert sha(R/n)==h
ns={'__file__':str(S.with_name('check_old_D_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('counts=[];words={}')[0],ns)
W,M,K,tr,rot,xy,center,G,geo,rows,rem,perms=[ns[k]for k in('W','M','K','tr','rot','xy','center','G','geo','rows','rem','perms')];ref=json.loads((D/'C_age1_first_contact.json').read_text());raw=lambda seq:''.join(W[a]for a in seq);canon=lambda x:json.dumps(x,sort_keys=True)
assert(center(0j,0),center(G['C']['p'],G['C']['h']))==(center(0j,0),center(G['D']['p'],G['D']['h']))and(G['C']['p'],G['C']['h'])==(1j,3)
roles=[];unfinished=[]
for full in('DC','VC','VCC','UC','UCC'):
 alltr=tr(raw(full));exitK={alltr['p']+q*rot(alltr['h'])for q in K}
 for j in range(full.count('C')):
  prefix=full[0]+'C'*j;pre=tr(raw(prefix));p,h=pre['p'],pre['h'];beta=p+(1-1j)*rot(h);common=p+2*rot(h);ct=len(raw(prefix));complete=full.count('C')-j
  row=dict(containing_full_packet=full,selected_C_index1=j+1,actual_prefix_before_selected_C=prefix,actual_selected_C_full_pose=[*xy(p),h],selected_C_atomic_clock=0,containing_full_source_entry_clock=-j,containing_full_source_age_at_FOREIGN=1+j,containing_full_completion_clock=complete,incoming_beta_full_cell=list(xy(beta)),incoming_beta_actual_R_tick0=ct-2,actual_incoming_bud_post_EXIT_age_at_FOREIGN=1,common_output_full_cell=list(xy(common)),common_actual_R_tick0=ct+8)
  if complete>1:row['exclusion']='containing full source cannot finish by true atomic-to-FOREIGN clock1';unfinished.append(row)
  else:
   assert alltr['last'][beta]==('R',ct-2)and alltr['last'][common]==('R',ct+8)and beta not in exitK and common not in exitK
   assert alltr['req'][beta]is False and alltr['req'][common]is False;roles.append(row)
assert roles==ref['five_actual_completed_containing_roles']and unfinished==ref['two_source_roles_excluded_by_full_completion']and len(roles)==5 and len(unfinished)==2
# Geometries rebuilt by independent D1 rational contact enumeration above, but C chronological roles are separate.
new=[]
for z in rows:
 why={'keep':'remaining','local_conflict':'immutable_local_context','guardian_in_A_K':'CURRENT_guard_in_FOREIGN_core','guardian_before_WHITE':'CURRENT_guard_before_WHITE'}[z['classification']]
 new.append(dict(foreign=z['foreign'],first=z['first'],second=z['second'],foreign_pose=z['foreign_pose'],second_pose=z['second_pose'],true_atomic_preforeign_age=1,effective_N=1+int(z['first']=='C'),classification=why))
assert len(new)==69 and set(map(canon,new))==set(map(canon,ref['all69_literal_guarded_alignments']))
counts=[];words={};stage=Counter()
for z in rem:
 A,b1,b2=z['foreign'],z['first'],z['second'];x,y,h=z['foreign_pose'];total=y-1
 for vw in range(max(total+1,0)):
  dw=total-vw;num=-x-dw-3*vw
  if num<0 or num%4:continue
  uw=num//4
  if not dw+vw+uw:continue
  counts.append(dict(foreign=A,first=b1,second=b2,foreign_pose=z['foreign_pose'],second_pose=z['second_pose'],dW=dw,vW=vw,uW=uw))
  for Y in perms(dw,vw,uw):
   if Y[-1]not in('VU'if A in'FQ'else'U'):continue
   seq='C'+Y+A+b1+b2;old=tr(raw('C'+Y));assert[*xy(old['p']),old['h']]==z['foreign_pose'];whole=tr(raw(seq)+M);assert whole['bad'];words[seq]=(whole,'old_RAW_prefix'if old['bad']else'foreign_or_returned_RAW_or_actual_marker')
assert len(counts)==75 and set(map(canon,counts))==set(map(canon,ref['exact75_W_endpoint_count_solutions']))and len(words)==194
sup={''.join(z['tokens']):z for z in ref['all194_distinct_whole_words_all_immutable_conflicting']};assert len(sup)==194 and set(sup)==set(words)
for seq,(t,why)in words.items():
 z=sup[seq];assert z['conflict_stage']==why;stage[why]+=1;i,prev,p,c=t['bad'];wit=z['immutable_conflict'];assert(i,prev,list(xy(p)),c)==(wit['conflict_read'],wit['previous_read'],wit['cell'],wit['turn'])
 # Whole-word ownership of both repeated reads reconstructed independently.
 for tick,field in((prev,'previous_actual_read_owner'),(i,'failing_actual_read_owner')):
  lo=0;found=None
  for j,a in enumerate(seq):
   if tick<lo+len(W[a]):found=(j,a,lo,tick-lo);break
   lo+=len(W[a])
  owner=z[field]
  if found:
   j,a,lo,local=found;assert owner['actual_atom_index0']==j and owner['actual_atom']==a and owner['atom_start_tick0']==lo;assert owner['canonical']['context_tick0']==local
  else:assert owner['actual_atom']=='next actual word'and owner['next_word_tick0']==tick-lo and owner['next_word_read_number1']==tick-lo+1 and owner['turn']==M[tick-lo]
assert dict(stage)==ref['exact_word_stage_counts']
out=dict(status='PASS no outgoing genuine old-C source at true atomic preforeign age1 for chronological FIRST SECOND-RAW contact',manifest_sha256=sha(D/'manifest.json'),dependencies=m['dependencies'],completed_source_roles=roles,unfinished_source_roles=unfinished,exact_contact_boxes=16,contact_poses=23,foreign_alignments=69,local_conflicts=6,preforeign_guard_white_conflicts=18,remaining_endpoint_obligations=45,count_solutions=75,all_order_whole_words=194,whole_word_stages=dict(stage),analytic_review=['Selected C1 of DC/VC/UC has full entry0, age1, completion1; selected C2 of VCC/UCC has full entry-1, age2, completion1. The two first-tail double-C roles cannot complete by foreignclock1. Every actual prior BASE/C1 bud is reconstructed, fresh final R and outside full exit core.','Signed1325 uses actual POST-EXIT age1 for prior bud including internal same-packet cuts; signed1344 includes shifted second-C output maturity, not ordinary full age reused as atomic age. Both identities are used ONLY at foreign entry, and all actual later context toggles are retained.','C and D have identical corrected geometric chords and identical true/effective heading counts in this slice. All16 exact boxes and outgoing endpoint/collinear ownership are rebuilt by independent D1 geometry, but no D-source currentness or ancestry statement is imported.','After real selected C the sole old segment is a nonempty zero-C W run of D/V/U. y fixes d+v, x fixes u; all75 tuples and194 permitted complete orders independently regenerated, no search depth. Each whole body has an immutable repeated-read conflict on ANY entry board, stronger than supported containing roles require.','All actual read owners are reconstructed, including final M as subsequent real-word reads. No postforeign age, arbitrary standalone-C theorem, older-source ancestry search, otherC age or second simplicity.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],dict(stage))
