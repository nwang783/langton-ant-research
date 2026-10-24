"""One east-core cut, plus genuine q ancestry and exact second-V reset."""
from pathlib import Path
import hashlib,json,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;BP=R/'U_star_one_foreign_return_transfer_2026-10-24/check_U_star_corner_transfer.py';n={'__file__':str(BP)};exec(BP.read_text().split('# Exactly twelve constant local suffixes.')[0],n)
W=n['W'];mp=n['mp'];M=n['M'];K=n['K'];L=n['L'];LEFT=n['PORTS']['LEFT'];at=n['at'];rot=n['rot'];sub=n['sub'];literal=n['literal'];center=n['center'];meet=n['meet'];q=(-1,2);gA=(-1,4)
P=R/'U_second_contact_creator_bud_guards_2026-10-24/creator_bud_guards.json';j=json.loads(P.read_text());rows=j['remaining12_necessary_states'];assert len(rows)==12
CP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';sp=importlib.util.spec_from_file_location('owner',CP);co=importlib.util.module_from_spec(sp);sp.loader.exec_module(co)
# Literal UCC successors are exhaustive G8 words, not a depth scan.
pairs=[]
for b in('D','DC','V','VC','VCC','U','UC','UCC'):
 raw=''.join(W[mp[z]]['word']for z in'UCC'+b);d=literal(raw+M)
 pairs.append(dict(source='UCC',next_full=b,feasible=d['feasible'],conflict=d if not d['feasible']else None))
assert [z['next_full']for z in pairs if z['feasible']]==['V','VC']
# Signed q cleanup is V/VC at(-1,5,S), source-entry clock2.
# Its genuine V-base A output is(-1,4), at V RAW R11.
vp=(-1,5);vh=2;vd=literal(W[mp['V']]['word']);aloc=(0,1);assert at(aloc,vp,vh)==gA and vd['reads'][aloc][-1]==[11,'R']
for b in('V','VC'):
 d=literal(''.join(W[mp[z]]['word']for z in b));assert d['reads'][aloc][-1]==[11,'R']
# A's only all-age first retirement V/VC at relative(0,4,S) maps to(-1,1,N).
helper=at((0,4),vp,vh);hh=(vh+2)%4;assert helper==(-1,1)and hh==0
helpend=at(tuple(vd['endpoint'][:2]),helper,hh);helph=(hh+vd['endpoint'][2])%4
hc=(center(helper,hh),center(helpend,helph));contact=meet((-1,-1),(-1,7),*hc)
assert contact==(__import__('fractions').Fraction(1),__import__('fractions').Fraction(1))
result=[];one=[];remaining=[]
for old in rows:
 a,b1,b2=old['foreign'],old['first'],old['second'];p=tuple(old['foreign_pose'][:2]);h=old['foreign_pose'][2];clock=old['true_preforeign_age'];assert b2=='V'and old['second_pose']==[0,4,2]
 raw=''.join(W[mp[z]]['word']for z in(a,b1,b2));d=literal(raw+M);fd=literal(W[mp[a]]['word']+M);r1=literal(W[mp[a]]['word']+W[mp[b1]]['word']);s=rot(sub(gA,p),-h);assert d['requirements'][s]is False and d['reads'][s][0][1]=='R'
 initialK={at(z,p,h)for z in K};east={(2,0),(2,1)}&initialK
 row=dict(foreign=a,first=b1,second=b2,foreign_pose=old['foreign_pose'],second_pose=old['second_pose'],true_preforeign_clock=clock,cleanup_A_required_before_WHITE=True,cleanup_A_cell=gA,cleanup_A_first_combined_R_tick0=d['reads'][s][0][0],q_must_be_SAME_original_at_foreign_entry=True,q_cannot_have_had_preforeign_cleanup=True,creating_full_type_UCC_excluded=True,allowed_creating_full_types=['U','UC'])
 if east:
  assert(a,p,h,b1,clock)==('F',(3,0),1,'C',3)and east=={(2,0),(2,1)}
  row.update(classification='excluded_before_foreign_by_original_east_pair_in_entry_core',east_pair_in_actual_FOREIGN_entryK=sorted(east),earliest_possible_east_pair_retirement_clock=4);one.append(row)
 else:
  row['classification']='necessary_only_remaining_with_original_q_and_creator_U_or_UC';remaining.append(row)
  # All five original identities are unchanged/current at second-V entry.
  for tag in L|{q}:
   z=rot(sub(tag,p),-h);assert z not in r1['reads']
   if tag in L:assert z not in fd['requirements']
  Ventry=(0,4);Vh=2;K2={at(z,Ventry,Vh)for z in K};assert not(L|{q})&K2
  row['CUT2_same_original_CURRENT_ids']=sorted(L|{q})
 result.append(row)
assert len(one)==1 and len(remaining)==11
# Exact conditional reset inside second V. No age/permanence through foreign.
Ventry=(0,4);Vh=2;vr=literal(W[mp['V']]['word']);vc=literal(W[mp['V']]['word']+M);Vend=at(tuple(vr['endpoint'][:2]),Ventry,Vh);Vouth=(Vh+vr['endpoint'][2])%4;K3={at(z,Vend,Vouth)for z in K}
qlocal=rot(sub(q,Ventry),-Vh);wlocal=rot(sub((0,1),Ventry),-Vh);assert qlocal==(1,2)and wlocal==(0,3)
assert vc['reads'][qlocal]==[[13,'L'],[17,'R'],[21,'L']] and vc['reads'][wlocal]==[[19,'L']]
assert q in K3 and(0,1)in K3 and not{(0,0),(1,0),(1,1)}&K3
reset=dict(actual_second_V_entry=[0,4,2],actual_RAW_exit=[*Vend,Vouth],q_cell=q,q_selected_local=qlocal,q_old_original_death=co.describe('V',13),q_new_fine_R_into_EXIT_CORE=co.describe('V',17),q_replacement_next_actual_word_death=co.describe('V',21),w_cell=(0,1),w_old_original_still_physically_alive_at_RAW_exit=True,w_alive_but_EXIT_CORE_not_CURRENT=True,w_actual_next_word_death=co.describe('V',19),same_original_star_CURRENT_after_SECOND_RAW=[(0,0),(1,0),(1,1)],scope='Conditional on one of the11 genuine histories existing. Exact physical local transfer, not attained ancestry and not a postforeign age law.')
D=[BP,CP,P,R/'U_second_contact_creator_bud_guards_2026-10-24/manifest.json',R/'core_periodicity_new/U_recycled_q_consumer_frozen_20261023_1954/manifest.json',R/'core_periodicity_new/U_q_source_history_frozen_20261023_2027/manifest.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Remaining12 old-U secondV(0,4,S) typed states: one actual preforeign east-pair/core exclusion; all others need SAME original q and creator U/UC, not UCC. Exact selected-q/core reset conditional on attainment. No global second-step simplicity or genuine positive control.',all8_literal_UCC_next_full_contexts=pairs,q_cleanup_companion_guard=dict(q_first_preforeign_cleanup='Signed1954/2027: genuine V/VC(-1,5,S) at source clock2.',new_A_cell=gA,new_A_actual_V_birth_tick0=11,new_A_source_entry_clock=2,only_A_first_consumer='Signed2043: V/VC at relative(0,4,S), source-age2, global source clock4.',mapped_consumer_pose=[*helper,hh],actual_consumer_V_chord=hc,old_creating_U_chord=[(-1,-1),(-1,7)],contact_source_parameter='1',contact_consumer_parameter='1',contact_is_not_true_adjacency='Old creating U base lies before twoCs and the genuine cleanupV; helper is later atclock4.',conclusion='A cannot retire before these clock3/4 foreign entries in a simple old complete8 prefix. All12 combined contexts require A WHITE before foreign. Therefore q cannot have retired/recolored preforeign; it is SAME original CURRENT.',no_postforeign_A_age=True),all12_cases=result,one_coarse_state_excluded=one,remaining11_necessary_states=remaining,conditional_genuine_original_q_second_V_core_transfer=reset,not_claimed=['The11 states are not attained.','No assumption that original q lower/upper old8 rules continue after foreign.','The new q R17 is EXITCORE, not a fresh residual output at that cut.','Originalw is aliveCORE at RAW exit; physical deletion is only next-word read2.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'original_q_frontier.json').write_text(json.dumps(o,indent=2)+'\n');print('12→11 coarse: F3,0E core cut; originalq forced, UCC excluded; exact qL13/R17 EXITCORE/nextL3 and originalw CORE/nextL1.')
