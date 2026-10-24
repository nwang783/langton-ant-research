"""Coupled ten-output first-loss and real hole-restoration transfer,
ANY sourceFOREIGN followed onlyordinaryRAW throughtwoCs. No simple/history
premise or unbounded-rail truncation; dormant identities are explicit.
"""
from pathlib import Path
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def spell(s):return ''.join(W[a]for a in s)
NE={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)};hole=(0,2);gate=(3,-1,0);gateexit=(3,3,0);sources=[]
for A in'FQB':
 tr=l.trace(W[A]);O=set(map(tuple,l.literal_geometry(W[A])['outputs']));assert NE<=O and tr['last'][hole]==('L',28)
 sources.append(dict(source_foreign=A,ENTRY=(0,0,0),actual_EXIT=after(W[A]),hole_last_L=dict(cell=hole,own_tick0=28,WHITE_after_source_RAW=True),all10_output_lastR=[dict(cell=q,own_R_tick0=tr['last'][q][1])for q in sorted(NE)]))
# With all10 CURRENT at entry, keep TRUE simultaneous inputs; only actual
# entryCORE / initial-WHITE conflicts are rejected, not BLACK inputs.
loss=[]
for g in sorted(NE):
 for a in'DVU':
  tr=l.trace(W[a]+l.M)
  for slot in map(tuple,l.literal_geometry(W[a])['inputs']):
   p=(*sub(g,slot),0);row=dict(original=g,consumer=a,true_input=slot,entry=p,physical_L=o.describe(a,tr['first'][slot][1]))
   if(sum(p[:2]))%2:why='sector'
   else:
    bad=[]
    for held in sorted(NE):
     q=sub(held,p[:2]);f=tr['first'].get(q)
     if q in l.K or f and f[0]=='R':bad.append(dict(original=held,local=q,role='ENTRY_CORE'if q in l.K else'initial_WHITE',first=f))
    if bad:why='held_NE_CORE_WHITE';row['conflicts']=bad
    else:why='sole_U_pair_breaker'
   row['classification']=why;loss.append(row)
assert len(loss)==80 and Counter(q['classification']for q in loss)=={'sector':40,'held_NE_CORE_WHITE':38,'sole_U_pair_breaker':2}
keep=[q for q in loss if q['classification']=='sole_U_pair_breaker'];assert{tuple(q['original'])for q in keep}=={(2,0),(2,1)}and all(q['consumer']=='U'and tuple(q['entry'])==gate for q in keep)
ug=l.literal_geometry(W['U']);ur=l.trace(W['U']);assert after(W['U'],gate)==gateexit
for g in NE-{(2,0),(2,1)}:
 local=sub(g,gate[:2]);assert local not in l.trace(W['U']+l.M)['first']
assert ur['last'][(-1,1)]==('L',14)and ur['last'][(-1,2)]==('R',21); assert sub(hole,gate[:2])not in l.trace(W['U']+l.M)['first']
newO={add(gate[:2],tuple(q))for q in ug['outputs']};assert len(newO)==9 and max(q[1]for q in newO)==2 and max(q[1]for q in NE)==2
# Completed ordinary input/R supports after the paired loss: N headsY>=3,
# all inputsY>=headY+1>=4 and all physical R haveY>=headY>=3.
allR=[]
for a in'DCVU':
 p=(0,0,0);r=[]
 for t,c in enumerate(W[a]):
  if c=='R':r.append(p[:2])
  p=after(c,p)
 assert min(q[1]for q in r)>=0 and min(q[0]for q in r)>=-1;allR.append(dict(atom=a,all_actual_R_cells=r,min_R_y=0))
 if a!='C':assert all(q[1]>=1 for q in l.literal_geometry(W[a])['inputs'])
# Every hole BLACK funding at a later completed RAW cut has a last actual
# R, insideCORE or external. Before firstNE loss all10 are current at its
# entry. After that loss headY>=3, so holey2 has no later physical R.
repairs=[]
for a in'DVU':
 tr=l.trace(W[a]);ct=l.trace(W[a]+l.M)
 for slot,(c,t)in tr['last'].items():
  if c!='R':continue
  p=(*sub(hole,slot),0);row=dict(producer=a,RAW_last_R_slot=slot,R_own_tick0=t,entry=p,RAW_EXIT=after(W[a],p))
  if(sum(p[:2]))%2:why='sector'
  else:
   bad=[]
   for held in sorted(NE):
    q=sub(held,p[:2]);f=ct['first'].get(q)
    if q in l.K or f and f[0]=='R':bad.append(dict(original=held,local=q,role='ENTRY_CORE'if q in l.K else'initial_WHITE',first=f))
   if bad:why='held_NE_CORE_WHITE';row['conflicts']=bad
   else:why='three_common_R8_funders'
  row['classification']=why;repairs.append(row)
assert len(repairs)==28 and Counter(q['classification']for q in repairs)=={'sector':14,'held_NE_CORE_WHITE':11,'three_common_R8_funders':3}
rkeep=[q for q in repairs if q['classification']=='three_common_R8_funders'];assert{(q['producer'],tuple(q['entry']),tuple(q['RAW_EXIT']))for q in rkeep}=={('D',(-2,2,0),(-1,3,0)),('V',(-2,2,0),(-1,5,0)),('U',(-2,2,0),(-2,6,0))};assert all(tuple(q['entry'])!=gate for q in repairs)
# For a black hole at target3,3, every candidate R-funder needs to complete
# before target; endpoints cannot reach it with a no-C N tail. Nor can a
# funder occur BEFORE pair-breaker head3,-1.
for q in rkeep:
 ep=tuple(q['RAW_EXIT']);assert ep[1]>=3 and(ep[1]>3 or ep[:2]!=(3,3));assert ep[1]>gate[1]
whitelist=[]
for A in'FQB':
 for B in'FQB':
  tr=l.trace(W[B]+l.M);local=sub(hole,gateexit[:2]);assert local==(-3,-1)and tr['first'][local]==('L',42)
  whitelist.append(dict(source_foreign=A,next_foreign=B,target_relative_source_ENTRY=gateexit,source_hole=hole,source_hole_L_tick0=28,actual_target_first_L=o.describe(B,42),contradiction='WHITE sourcehole cannot be funded before target by any completed ordinaryR role.'))
# Real genuine-U prefix attains the paired-loss branch. Two distinct
# complete fields distinguish a full context from a longer fine attempt.
prefix='UFCDDVCDUU';raw=spell(prefix);pt=l.trace(raw+l.M);ready=l.trace(raw+W['Q'][:42]);assert pt['feasible']and ready['feasible']and len(raw)==218 and after(raw)==(3,7,0)
seed35={q for q,(c,t)in pt['first'].items()if c=='L'};seed45={q for q,(c,t)in ready['first'].items()if c=='L'};assert len(seed35)==35 and len(seed45)==45 and seed35<=seed45 and all(q not in pt['first']for q in seed45-seed35)
sourceFOREentry=(0,4,0);oldids={add(sourceFOREentry[:2],g):28+l.trace(W['F'])['last'][g][1]for g in NE};oldhole=(0,6);attempts=[]
for label,seed in [('35_cell_complete_prefix',seed35),('45_cell_fine_attempt',seed45)]:
 B={q:('initial',q)for q in seed};p=(0,0,0);tick=0;records=[]
 for i,a in enumerate(prefix):
  for k,c in enumerate(W[a]):
   q=p[:2];assert(q in B)==(c=='L')
   if c=='L':del B[q]
   else:B[q]=tick
   p=after(c,p);tick+=1
  if i>=1:
   K={add(p[:2],l.rot(q,p[2]))for q in l.K};state=[dict(cell=g,source_FOREIGN_R_birth=bid,SAME_physically_BLACK=B.get(g)==bid,CURRENT=B.get(g)==bid and g not in K,actual_present_R_identity=B.get(g))for g,bid in sorted(oldids.items())];records.append(dict(after_atom_index0=i,atom=a,RAW_cut_tick0=tick,actual_head=p,all10_original_source_FOREIGN_ID_states=state))
 assert B.get((2,4))is None and B.get((2,5))==211 and oldhole not in B
 assert all(B.get(g)==bid for g,bid in oldids.items()if g not in{(2,4),(2,5)})
 assert all(B.get(add((3,3),tuple(q)))==190+ur['last'][tuple(q)][1]for q in ug['outputs'])
 start=tick;fine=[];fail=None
 for k,c in enumerate(W['Q']):
  q=p[:2]
  if(q in B)!=(c=='L'):
   fail=dict(candidate_Q_own_tick0=k,candidate_Q_read_number1=k+1,global_tick0=tick,cell=q,required_turn=c,actual_turn='L'if q in B else'R',canonical_owner=o.describe('Q',k));break
  destroyed=[dict(cell=g,source_FOREIGN_R_birth=bid)for g,bid in oldids.items()if q==g and B.get(q)==bid and c=='L']
  if destroyed:fine.append(dict(candidate_Q_own_tick0=k,actual_destroyed_source_FOREIGN_originals=destroyed))
  if c=='L':del B[q]
  else:B[q]=tick
  p=after(c,p);tick+=1
 if label=='45_cell_fine_attempt':assert fail['candidate_Q_own_tick0']==42 and tuple(fail['cell'])==oldhole and fail['required_turn']=='L'and fail['actual_turn']=='R'
 else:assert fail['candidate_Q_own_tick0']>=11
 attempts.append(dict(label=label,complete_seed=sorted(seed),seed_mass=len(seed),prefix_word=prefix,prefix_RAW_length=218,actual_prefix_M11_feasible=True,source_foreign_ENTRY=sourceFOREentry,new_U_pair_breaker_ENTRY=(3,3,0),after_new_U_ENTRY=(3,7,0),all_actual_marked_NE_ID_cut_states=records,old_FOREIGN_common_death_global_tick0=204,old_FOREIGN_q_death_global_tick0=203,new_U_q_rebirth_global_tick0=211,source_hole_WHITE_before_attempt=True,partial_actual_Q_identity_deletions=fine,first_unmatched_Q_request=fail))
D=[R/'foreign_two_C_north_frontier_2026-10-24/manifest.json',R/'audits/check_foreign_two_C_frontier_independent.json',R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='ANY actual sourceF/Q/B ENTRY0N, then only ordinary RAW with atmost2Cs and actualmarker contexts. The ten-source-NE firstloss is exactly a coupled N2 U3,-1 paired-loss gate; after its actual completion, eight SAME originals and nine newU outputs are CURRENT throughout remaining N tail. SOURCEFOREIGN L28 hole0,2 has the stated three last-R funding alternatives only. No U/prehistory/simple or railbound premise.',all3_source_fields=sources,all80_N2_NE_first_loss_roles=loss,unique_coupled_loss_gate=dict(atom='U',ENTRY=gate,RAW_EXIT=gateexit,old_common2_0_death_owner=o.describe('U',14),old_q2_1_death_owner=o.describe('U',13),new_q2_1_different_ID_R21=True),post_breaker_STATE=dict(eight_original_NE_CURRENT=sorted(NE-{(2,0),(2,1)}),old_common_cell_2_0_WHITE=True,old_q_original_dead_replaced_at2_1=True,new_U_all9_CURRENT=sorted(newO),N_input_y_min_after_EXIT=4,all_old_and_new_output_y_max=2,dormant_originals_retained=True),all_plain_physical_R_supports=allR,all28_CORE_inclusive_hole_last_R_roles=repairs,three_possible_hole_funders=rkeep,hole_funding_logic='S0/E1 physicalR cones misshole0,2; all4 plainRAW R minx>=-1 handles sourceS and minR_y>=0/rotatedE maxdy1 handles E. In N2, before firstNE loss both10held at producerENTRY;28 actualLAST-RAW-R roles leave3 commonwriters. A repair simultaneous with firstNE loss is impossible because none is U3,-1. After paired loss headY>=3 and physicalR_y_offset>=0, soholey2 cannot be repaired. If earlierfunding preceded pairedloss, all3 funderEXITY>=3 cannot reach gateHEADy-1. Thus the hole staysWHITE after the pairedloss. Moregenerally at target3,3 no3 funderexit can reach it by remainingzeroC N, soholeWHITEwhether pairedloss occurredornot.',all9_portable_next_FOREIGN_3_3_gate_exclusions=whitelist,all2_actual_genuine_U_entry_fields=attempts,unread_extension=sorted(seed45-seed35),extension_cells_genuinely_unread_through_35_field_prefix_M=True,not_claimed=['No completedsecondQ in this illustration; the45-field actual candidate diverges at ownL42.','No throughFOREIGN persistence is inferred from entryCURRENT; this recorded partialQ deletes none of the remaining8 originals before its hole failure.','No arbitrarytwoC hookerosion classification or tagseal, allother nextFOREIGN poses remain open.','The coupled transfer is a source-tag projection, not a finite-state fullfield quotient or strict port-consumption order.','No global proxy simplicity, coverage or capture.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'pair_hole_transfer.json').write_text(json.dumps(out,indent=2)+'\n');print('Coupled80=40sector+38field+2U3,-1 pair; remaining8+newU9 frozen under Ntail. Hole28=14sector+11field+3 funders; all9 nextFORE3,3 blockedL42. Real35/45 fields attain pair loss/newq, partialQ not completed.')
