"""Existing genuine U exit-bud law, applied only BEFORE first foreign."""
from pathlib import Path
import json,hashlib,importlib.util
from collections import Counter
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;BP=R/'U_star_one_foreign_return_transfer_2026-10-24/check_U_star_corner_transfer.py'
n={'__file__':str(BP)};exec(BP.read_text().split('# Exactly twelve constant local suffixes.')[0],n)
W=n['W'];mp=n['mp'];M=n['M'];rot=n['rot'];sub=n['sub'];literal=n['literal'];K=n['K'];L=n['L'];at=n['at']
FP=R/'second_ordinary_after_first_foreign_2026-10-24/old_U_second_contact_LEFT_frontier.json';F=json.loads(FP.read_text());s=(1,3);g=(0,2)
CP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';sp=importlib.util.spec_from_file_location('owner',CP);co=importlib.util.module_from_spec(sp);sp.loader.exec_module(co)
# Source actual last reads and genuine C-tail preservation.
sources=[]
for t in('U','UC','UCC'):
 d=literal(''.join(W[mp[a]]['word']for a in t));assert d['reads'][s][-1]==[26,'R'];assert d['reads'][g][-1]==[20,'L'];sources.append(dict(creating_full_type=t,same_original_s_birth_tick0=26,all_s_reads=d['reads'][s],g_last_deletion_tick0=20,all_g_reads=d['reads'][g]))
# Reconstruct signed992's 38 residual-output origins rather than importing
# an asserted surviving-port list. These are only BEFORE foreign clock3.
AT=[]
for a in'DCVU':
 raw=literal(W[mp[a]]['word']);ctx=literal(W[mp[a]]['word']+M);ep=tuple(raw['endpoint'][:2]);eh=raw['endpoint'][2]
 outs={q for q,b in raw['requirements'].items()if b^(q in raw['parity'])}-{at(q,ep,eh)for q in K};assert all(q[1]>=0 and sum(q)>=0 for q in outs);AT.append((a,outs,ctx,ep,eh))
origin=[];ports=[]
for h in(2,1):
 for a,outs,ctx,ep,eh in AT:
  for slot in sorted(outs):
   p=sub(g,rot(slot,h));end=at(ep,p,h);hits={at(q,p,h)for q in ctx['requirements']}&L
   if(sum(p)+h)%2:why='sector'
   elif hits:why='held_genuine_star_context_conflict'
   elif h==1 and a=='C':why='E_C4_not_complete_before_foreign_clock3'
   else:
    assert h==1;why='old_signed_three_E3_origins';z=rot(sub(s,p),-h);req=ctx['requirements'].get(z);rr=ctx['reads'].get(z);assert req is not None
    if req:
     assert(a,z)in(('V',(1,2)),('U',(0,3)));guard='would_retire_original_s_at_source_clock3_before_min5'
    else:assert(a,p)==('U',(-1,4));guard='before_WHITE_conflicts_with_genuine_current_BLACK_s'
    ports.append(dict(atom=a,output_slot=slot,entry=[*p,h],exit=[*end,(h+eh)%4],s_local_cell=z,s_before_BLACK=req,s_reads=rr,first_s_owner=co.describe(a,rr[0][0]),exclusion=guard))
   origin.append(dict(atom=a,output_slot=slot,pose=[*p,h],reason=why))
assert len(origin)==38 and len(ports)==3
# N0 and W1 cones already used in signed992: source exits N y>=4;
# W1 H=y-x>=5; all atomic output local y,x+y nonnegative. g has both2.
assert g[1]<4 and g[1]-g[0]<5
rows=[];counts=Counter();remaining=[]
for old in F['exact60_necessary_only_remaining_states']:
 a,b1,b2=old['foreign'],old['first'],old['second'];p=tuple(old['foreign_pose'][:2]);h=old['foreign_pose'][2];clock=old['true_preforeign_age'];assert clock in(3,4)
 names=(a,b1,b2);raw=''.join(W[mp[q]]['word']for q in names);d=literal(raw+M);assert d['feasible'];z=rot(sub(s,p),-h);req=d['requirements'].get(z)
 row=dict(foreign=a,first=b1,second=b2,foreign_pose=old['foreign_pose'],second_pose=old['second_pose'],true_preforeign_clock=clock,s_before_requirement=req)
 if req is False:
  why='genuine_s_BLACK_vs_combined_before_WHITE';rr=d['reads'][z];t=rr[0][0];assert rr[0][1]=='R'
  offset=0;owner=None
  for stage_i,name in enumerate(names):
   le=len(W[mp[name]]['word'])
   if offset<=t<offset+le:
    owner=dict(actual_stage=('FOREIGN','FIRSTordinary','SECONDordinary')[stage_i],actual_symbol=name,word_tick0=t-offset,word_read_number1=t-offset+1,turn='R');break
   offset+=le
  if owner is None:owner=dict(actual_stage='future actual M11 prefix after SECOND',stream_tick0=t-len(raw),stream_read_number1=t-len(raw)+1,turn='R')
  row.update(s_local=z,all_s_combined_reads=rr,first_s_required_WHITE_owner=owner,guard='s remains genuine current BLACK at FOREIGN entry by signed preforeign min5; combined before-mask accounts for every later toggle')
 else:
  gg=rot(sub(g,p),-h);gr=d['requirements'].get(gg)
  if gr is True:
   assert clock==3 and gg not in K;why='source_deleted_g_no_rebirth_through_clock3';row.update(g_local=gg,g_before_BLACK=True,all_g_combined_reads=d['reads'][gg],g_outside_foreign_entry_core=True,guard='38 old signed atomic origins plus genuine s eliminate all3 residual E3 origins')
  else:why='necessary_only_not_excluded_here';remaining.append(old)
 row['classification']=why;counts[why]+=1;rows.append(row)
assert counts==Counter({'genuine_s_BLACK_vs_combined_before_WHITE':36,'source_deleted_g_no_rebirth_through_clock3':12,'necessary_only_not_excluded_here':12})
assert all(z['second']=='V'and z['second_pose']==[0,4,2]for z in remaining)
# Exact regression/ancestry failure of the actual prepared c5a FDU control.
pp=(4,-3);h=1;dd=literal(W[mp['F']]['word']+W[mp['D']]['word']+W[mp['U']]['word']+M);zz=rot(sub(s,pp),-h);assert dd['requirements'][zz]is False and dd['reads'][zz][0]==[63,'R']
D=[BP,CP,FP,R/'second_ordinary_after_first_foreign_2026-10-24/old_U_second_contact_LEFT_frontier_manifest.json',R/'returned_U_source_deleted_guard_2026-10-23/manifest.json',R/'returned_U_source_deleted_guard_2026-10-23/returned_U_deleted_guard.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Exactly48 of existing60 necessary old-U SECOND-contact typed states excluded by genuine preforeign creator bud s=(1,3). Foreign/returned core rewriting fully retained in combined before-masks. No age law after foreign and no new contact catalogue.',source_fine_birth_and_deletion=sources,signed_source_s_fact='Same original s stays CURRENT through creating-full-entry C clock4 in uninterrupted complete8; used ONLY up to FOREIGN entry at true clock3/4.',all38_reconstructed_preforeign_g_origins=origin,three_E3_g_origins_all_now_excluded_by_s=ports,stronger_reader_independent_g_conclusion='Source-deleted g=(0,2) cannot acquire a current residual BLACK rebirth by preforeign clock3 in uninterrupted complete8. N0/W1 cones, allS2 contexts, E_C4 completion and the three E3 bud conflicts exhaust actual atomic residual output origins; a CORE writer cannot hide because next atomic first6 reads delete its exitK before g could be outside the FOREIGN entryK.',all60_typed_cases=rows,classification_counts=dict(counts),remaining12_necessary_states=remaining,prepared_FDU_missing_ancestry=dict(foreign_pose=[4,-3,1],true_preforeign_clock=3,s_local=zz,source_s_is_genuinely_BLACK=True,prepared_control_requires_s_initial_WHITE=True,first_required_WHITE=dict(combined_tick0=63,actual_owner='FIRST ordinary D RAW',owner_tick0=7,owner_read_number1=8),FOREIGN_RAW_misses_s=True,not_an_unconditional_prepared_control_refutation=True),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'creator_bud_guards.json').write_text(json.dumps(o,indent=2)+'\n');print('Existing60 oldU SECOND-contact typed states:36 direct genuine-bud WHITE conflicts +12 source-deleted-g no-rebirth;12 necessary V(0,4,S) remain.')
