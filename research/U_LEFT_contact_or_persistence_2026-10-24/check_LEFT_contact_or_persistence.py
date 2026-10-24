"""A conditional contact-or-persistence lemma, not global simplicity."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib,json,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;BP=R/'U_star_one_foreign_return_transfer_2026-10-24/check_U_star_corner_transfer.py'
n={'__file__':str(BP)};exec(BP.read_text().split('# Exactly twelve constant local suffixes.')[0],n)
W=n['W'];mp=n['mp'];M=n['M'];K=n['K'];L=n['L'];at=n['at'];rot=n['rot'];sub=n['sub'];literal=n['literal'];center=n['center'];meet=n['meet'];LEFT={(0,0),(0,1)};a=(1,0);z=(1,1)
CP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';spec=importlib.util.spec_from_file_location('owner',CP);co=importlib.util.module_from_spec(spec);spec.loader.exec_module(co)
# All first losses of either LEFT original from an ordinary RAW+actualM11.
un=set();loc={}
for b in 'DCVU':
 raw=literal(W[mp[b]]['word']);full=literal(W[mp[b]]['word']+M);loc[b]=raw,full
 for slot,v in full['requirements'].items():
  if v:
   for tag in LEFT:
    for h in range(4):un.add((b,*sub(tag,rot(slot,h)),h))
lossrows=[];lc=Counter();surv=[]
for b,x,y,h in sorted(un):
 pp=(x,y);raw,d=loc[b];row=dict(atom=b,entry=[x,y,h])
 if (x+y+h)%2:why='wrong_active_sector'
 elif LEFT&{at(q,pp,h)for q in K}:why='LEFT_original_in_entry_core'
 elif any(d['requirements'].get(rot(sub(q,pp),-h))is False for q in LEFT):why='LEFT_BLACK_vs_before_WHITE'
 else:
  end=at(tuple(raw['endpoint'][:2]),pp,h);eh=(h+raw['endpoint'][2])%4;kout={at(q,end,eh)for q in K};keep={q for q in LEFT if rot(sub(q,pp),-h)not in raw['reads']and q not in kout}
  assert len(keep)<2
  contact=meet((-1,-1),(-1,7),center(pp,h),center(end,eh))
  if contact is not None:why='atom_chord_contacts_creating_U_chord'
  else:
   why='sole_no_old_U_contact_LEFT_loss';row.update(exit=[*end,eh],remaining_original_LEFT=sorted(keep),other_original_star_before_requirements=[dict(cell=q,BLACK=d['requirements'].get(rot(sub(q,pp),-h)))for q in(a,z)],LEFT_physical_first_reads=[dict(cell=q,word_tick0=d['reads'][rot(sub(q,pp),-h)][0][0],owner=co.describe(b,d['reads'][rot(sub(q,pp),-h)][0][0]))for q in sorted(LEFT)]);surv.append(row)
 row['reason']=why;lc[why]+=1;lossrows.append(row)
assert len(surv)==1 and surv[0]['atom']=='U'and surv[0]['entry']==[1,-1,0]
assert surv[0]['other_original_star_before_requirements']==[dict(cell=a,BLACK=False),dict(cell=z,BLACK=True)]
# First loss of original a while both LEFT originals remain CURRENT, prior
# to the above U. Entry-core capture by a previous atom is counted as that
# previous atom's loss; it is not allowed as a hidden first-L escape here.
au=set()
for b,(raw,d)in loc.items():
 for slot,v in d['requirements'].items():
  if v:
   for h in range(4):au.add((b,*sub(a,rot(slot,h)),h))
arows=[];ac=Counter();aport=[]
for b,x,y,h in sorted(au):
 pp=(x,y);raw,d=loc[b];row=dict(atom=b,entry=[x,y,h])
 if (x+y+h)%2:why='wrong_active_sector'
 elif(LEFT|{a})&{at(q,pp,h)for q in K}:why='genuine_held_original_in_entry_core'
 elif any(rot(sub(q,pp),-h)in d['requirements']for q in LEFT):why='does_not_MISS_both_held_LEFT_originals'
 else:
  end=at(tuple(raw['endpoint'][:2]),pp,h);eh=(h+raw['endpoint'][2])%4
  if meet((-1,-1),(-1,7),center(pp,h),center(end,eh))is not None:why='atom_chord_contacts_creating_U_chord'
  else:
   why='possible_first_a_loss_port';slot=rot(sub(a,pp),-h);rr=d['reads'][slot];assert rr[0][1]=='L';row.update(exit=[*end,eh],first_a_physical_L=co.describe(b,rr[0][0]),all_a_reads=rr);aport.append(row)
 row['reason']=why;ac[why]+=1;arows.append(row)
assert [(q['atom'],q['entry'],q['exit'])for q in aport]==[('D',[1,-1,0],[2,0,0]),('U',[2,-4,0],[2,0,0]),('U',[2,-2,0],[2,2,0]),('V',[1,-3,0],[2,0,0])]
assert all(q['exit'][0]>=2 and q['exit'][1]>=0 and q['exit'][2]==0 for q in aport)
# Source/full-tail/consumer-half bridge, with no guessed internal foreign K.
B=(-1,3);E=(1,1);Ustart=(1,-3);Uend=(1,5);wedge=(B,E)
assert meet(B,(-1,7),*wedge)==(Fraction(0),Fraction(0))
source=[]
for typ in('U','UC','UCC'):
 atoms=n['walk'](typ)
 for aa in atoms[1:]:assert meet(aa['start'],aa['end'],*wedge)is None
 raw=literal(''.join(W[mp[t]]['word']for t in typ));rr=raw['reads'][(0,1)];assert rr[-1]==[19,'R']
 source.append(dict(creating_full_type=typ,all_w_reads=rr,actual_tail_chords=[dict(atom=q['atom'],start=q['start'],end=q['end'])for q in atoms[1:]],last_w_birth_tick0=19,no_later_source_tail_read=True))
assert meet(Ustart,E,*wedge)==(Fraction(1),Fraction(1))
# Exact angle units in pi/4: open sourceU->consumerU =2(n+2), bridge
# joins +1,-1. Jordan +/-8 gives n2 only for nonnegative integer n.
clock=[n for n in range(20)if 2*(n+2)in(-8,8)];assert clock==[2]
# Not a finite sampling claim: 2(n+2)=+/-8 solves algebraically n2 or-6.
D=[BP,CP,R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/current_residual_barrier_frozen_20261023_1822/manifest.json',R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Actual U-entry complete-eight prefix, FIRST foreign A whose complete context MISSES all4 original U-star IDs, then ANY finite ordinary RAW tail. Conditional on expanded proxy remaining simple, SAME original LEFT pair remains CURRENT at every ordinary cut. Equivalently any first LEFT loss forces a prior/within-loss-atom proxy contact. Not a global simplicity or foreign-star-erosion theorem.',current_convention='Physical same source-R BLACK label outside actual ordinary cut canonicalK. CORE absorption counts loss before later physical deletion. Replacements never count.',all_LEFT_first_loss_rows=lossrows,LEFT_classification=dict(lc),sole_no_creating_U_contact_loss_gate=surv,all_original_a_first_loss_rows=arows,a_first_loss_classification=dict(ac),four_possible_a_first_loss_ports=aport,source_C_tail_bridge_interfaces=source,held_bridge=dict(source_chord_midpoint=B,consumer_U_first_half_endpoint=E,current_w_edge=[B,E],consumer_U_entry=[1,-1,0],consumer_U_chord=[Ustart,Uend],bridge_join_turns_pi_over_4=[1,-1],open_turn_pi_over_2='n_C+2',Jordan_clock_algebra='n_C+2=+4 or -4; n_C>=0 leaves n_C=2 only',first_a_loss_heading_clock='N after exactly one foreign means m_C+2 divisible by4. With0<=m_C<=n_C=2, m_C=2.',last_step='All four a-loss atoms complete at N head x>=2,y>=0. No C remains before U(1,-1,N). Every actual following N zero-C atom D/V/U has nonnegative x/y increment, impossible to reach target.'),outside_return_interface='A complete-context MISS all4, and actual previously executed expanded proxy simple up to the next ordinary atom entry. No assertion that this interface is automatically preserved; a first contact is an allowed explicit alternative.',low_foreign_age_corollary='Signed9fdb first-effect bound supplies A-context-MISS all4 whenever actual sourceENTRY-to-A C age<=4. This is a funding-cut fact, NOT postforeign age.',not_claimed=['No unconditional arbitrary-tail permanence.','No persistence if A actually erodes an original star ID.','No contact is called a current physical barrier unless a held identity supplies it.','A contact with any earlier proxy segment is allowed; it need not be with the creating U itself.','No actual erosion-free/genuine-U construction is asserted.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'LEFT_contact_or_persistence.json').write_text(json.dumps(o,indent=2)+'\n')
print('LEFT no-old-U loss: soleU(1,-1,N); a-loss4 N ports; exact held-w Jordan n2 + N monotonic contradiction. Conditional on A-star MISS and simple proxy.')
