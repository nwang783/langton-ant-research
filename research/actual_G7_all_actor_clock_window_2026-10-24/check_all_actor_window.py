"""All 49 source/actor piece windows for the GLOBAL first new contact.
The actor may now be a genuine foreign prefix or tail, not only ordinary.
"""
from pathlib import Path
import json,hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
# Intrinsic alpha coefficients in units (pi/4,beta). For a source tail the
# source heading is rebased to its real tail-entry S orientation; its own
# F-prefix is not counted again. This is audited3117's piece convention.
alpha={'D':(1,0),'C':(1,0),'V':(2,-1),'U':(2,0),'F_prefix':(4,1),'Q_tail':(2,0),'B_tail':(2,1)}
classes=tuple(alpha)
def form(source,target,L):
 source_bonus=2 if source=='F_prefix'else 0
 actor_bonus=2 if target in('Q_tail','B_tail')else 0
 sa,sb=alpha[source];ta,tb=alpha[target]
 return 2*(L+source_bonus+actor_bonus)+ta-sa,tb-sb

def inside(A,B):
 return min(A,A+B)>=4 and max(A,A+B)<=12 and not(B==0 and A in(4,12))
def outside(A,B):return max(A,A+B)<=4 or min(A,A+B)>=12
rows=[]
for source in classes:
 for target in classes:
  allowed=[];bounds=[]
  for L in range(8):
   A,B=form(source,target,L)
   assert inside(A,B)or outside(A,B),(source,target,L,A,B)
   if inside(A,B):allowed.append(L)
   bounds.append(dict(L=L,T_coeff_pi_over4=A,T_coeff_beta=B,in_strict_Jordan_window=inside(A,B)))
  for L in range(8,12):
   A,B=form(source,target,L);assert min(A,A+B)>12
  pairs=[]
  for L in allowed:
   for f in range(L//2+1):
    K=L-2*f
    if source=='C'and K<1:continue
    prefix_count=f+int(source=='F_prefix')+int(target in('F_prefix','Q_tail','B_tail'))
    touched_word_count=f+int(source not in'DCVU')+int(target not in'DCVU')
    assert prefix_count<=3 and touched_word_count<=4 and K+f+1<=7
    pairs.append(dict(L=L,actual_C_count_K=K,strictly_intervening_complete_foreigns_f=f,foreign_Fprefix_pieces_touched=prefix_count,foreign_WORDS_touched=touched_word_count,max_ordinary_monotone_epochs=K+f+1))
  assert allowed and pairs
  rows.append(dict(source_piece=source,actor_piece=target,allowed_L=allowed,all8_exact_angle_bounds=bounds,all_necessary_K_f_pairs=pairs,max_f=max(p['strictly_intervening_complete_foreigns_f']for p in pairs),source_C_own_interval_required=source=='C'))
assert len(rows)==49
ordinary=[r for r in rows if r['actor_piece']in'DCVU']
foreign=[r for r in rows if r['actor_piece']not in'DCVU']
assert len(ordinary)==28 and len(foreign)==21
assert max(r['max_f']for r in ordinary)==3
assert max(r['max_f']for r in foreign)==2
assert all(max(r['allowed_L'])<=4 for r in foreign)
assert max(p['foreign_Fprefix_pieces_touched']for r in rows for p in r['all_necessary_K_f_pairs'])==3
assert max(p['foreign_WORDS_touched']for r in rows for p in r['all_necessary_K_f_pairs'])==4
old=json.loads((ROOT/'actual_G7_positive_clock_contact_window_2026-10-24/positive_clock_window.json').read_text())
old_windows={(r['source'],r['ordinary_contact_actor']):r['allowed_effective_L'] for r in old['all28_source_ordinary_actor_windows']}
assert {(r['source_piece'],r['actor_piece']):r['allowed_L'] for r in ordinary}==old_windows
D=['actual_G7_positive_clock_contact_window_2026-10-24/manifest.json','audits/check_positive_G7_clock_window_independent.json','foreign_interval_packet_grammar_2026-10-24/manifest.json','audits/check_foreign_interval_grammar_independent.json','seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json','audits/check_foreign_kinked_barrier_turn_independent.json','one_foreign_first_contact_compression_2026-10-24/manifest.json','audits/check_one_foreign_contact_C_window_independent.json']
result=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual finite U-entry G7 RAW factor with actual full words and real final M11; chronological GLOBAL first nonadjacent new proxy contact. Actor may be ordinary D/C/V/U, an actual foreign F56 prefix, Q tail or B tail. No mixed simplicity is assumed before choosing the global first contact, no age or identity law crosses a foreign, and no contact is excluded by this necessary angular theorem.',
 actual_grammar_and_clock='Signed0edd gives b=0 in audited3117. Thus J=C+2FORE is the exact positive marked-word proxy clock with the existing terminal-piece and intrinsic alpha offsets. Every actual adjacent join is nonreversing, and each full foreign is internally injective.',
 count_conventions='K counts actual Cs after source ENTRY and before the actor WORD ENTRY, including source C own interval and excluding target C own interval. If source is a foreign piece, its own foreign is excluded from f. If actor is a foreign piece, its own candidate foreign is excluded from f. Thus f counts full foreign words strictly between the source word and actor word. Source and actor foreign words are distinct: a single Q/B is internally injective and its only prefix/tail adjacency is legitimate, so it cannot own its own first nonadjacent positive contact.',
 exact_all_piece_turn='Let L=K+2f. Then T=(pi/2)*(L+2*1[source=F_prefix]+2*1[actor=Q_tail or B_tail])+alpha_actor-alpha_source. A source F-prefix retains its own heading contribution; a source tail does not count its earlier F-prefix. An actor F-prefix is terminal in the selected partial subarc, so its own +2 is subtracted by terminal e_F. An actor tail has already traversed its genuine F56 prefix, so +2 remains. No fine kink is treated as a marked core.',
 earliest_contact_ownership='Old vertices belong to their outgoing piece. The new actor is the earliest piece reaching the first contact; a contact at a foreign F-prefix END is assigned to that prefix, not retrospectively to its outgoing tail t0. A tail actor therefore starts with no earlier prefix contact and has positive new parameter. Collinear same-direction onset and terminal endpoints are included; opposite closing tangents would overlap earlier.',
 Jordan_correction='The already drawn proxy is simple by GLOBAL-first choice, not by an induction hypothesis. Closing its source-to-contact subarc with the partial actor gives a simple closed curve and delta in(-pi,pi). Every source/actor turn form is >-pi/2 for nonnegative K,f. Thus negative Jordan orientation is impossible; T+delta=+2pi and pi<T<3pi. The 49 symbolic beta-interval checks impose exactly this strict window.',
 all49_source_actor_windows=rows,
 compression='Any global first-contact loop crosses at most three genuine foreign F-prefix PIECES and at most seven ordinary monotone epochs. It can touch four foreign WORDS, because a source tail may belong to a fourth word whose F-prefix lies before the loop. An ordinary actor permits at most three strictly intervening complete foreigners; a foreign actor permits at most two. Epoch lengths, spatial gaps, dormant ports and full color/identity records remain unbounded.',
 not_claimed=['No first-contact exclusion or arbitrary-tail/global simplicity theorem.','No semantic use of geometric L as a producer maturation clock.','No finite-state or bounded-field quotient, fuel/energy decrease or capture.','No new foreign-prefix CURRENT barrier or source identity survival.','Raw CF/CQ/CB prepared controls outside the actual preceding grammar still have their real wrap.','All real SOURCE/actor FOREIGN kinks remain actual fine cuts, not packet births or cores.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'all_actor_window.json').write_text(json.dumps(result,indent=2)+'\n')
print('GLOBAL-first all49 actor windows: ordinary28 f<=3; FOREIGN21 f<=2. At most3 actual foreign-prefix pieces and7 ordinary epochs; up to4 touched FOREIGN WORDS. No contact exclusion.')
