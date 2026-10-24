"""Exact positive proxy clock and ordinary-actor first-contact windows.
No arbitrary-tail simplicity, maturity transfer or language coverage result.
"""
from pathlib import Path
import importlib.util,json,hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
o=load('owner',ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS
clock={'D':0,'C':1,'V':0,'U':0,'F':2,'Q':2,'B':2}
heading=[]
for a in'DCVUFQB':
 h=0
 for c in W[a]:h=(h+(1 if c=='R'else-1))%4
 assert h==(-clock[a])%4
 heading.append(dict(atom=a,clock_increment=clock[a],actual_RAW_EXIT_headingCW=h))
# a(atom), in units (pi/4,beta); beta/(pi/4) lies strictly in (0,1).
deflection={'D':(1,0),'C':(1,0),'V':(0,1),'U':(0,0)}
# Exact internal-turn expression from audited3117 after signed0edd removes b.
# n_C includes a terminal target C, which e_C subtracts. A source C itself
# remains in actual K because it has executed before the target entry.
def form(source,target,L):
 A,B=deflection[target]
 if source in'DCVU':
  X,Y=deflection[source];return 2*L+X-A,Y-B
 if source=='F_prefix':return 2*L+2-A,-1-B
 if source=='Q_tail':return 2*L-A,-B
 if source=='B_tail':return 2*L-A,-1-B
 raise AssertionError(source)
def inside(A,B):
 # Strict 4<A+B*x<12 for every 0<x<1. Equality at x=0 or1 is
 # harmless; an identically-boundary expression is excluded.
 lo,hi=min(A,A+B),max(A,A+B)
 return lo>=4 and hi<=12 and not(B==0 and A in(4,12))
def outside(A,B):
 lo,hi=min(A,A+B),max(A,A+B)
 return hi<=4 or lo>=12
windows=[]
for source in('D','C','V','U','F_prefix','Q_tail','B_tail'):
 for target in'DCVU':
  allowed=[];all_bounds=[]
  # For L>=8, T/(pi/4)>=2L-2>12 for every source/target;
  # the finite list is a derived angular bound, not a word-length cap.
  for L in range(8):
   A,B=form(source,target,L)
   assert inside(A,B)or outside(A,B),('unresolved beta threshold',source,target,L,A,B)
   all_bounds.append(dict(effective_clock=L,T_coeff_pi_over4=A,T_coeff_beta=B,strict_Jordan_window=inside(A,B)))
   if inside(A,B):allowed.append(L)
  for L in range(8,12):
   A,B=form(source,target,L);assert min(A,A+B)>12
  assert allowed
  # Record all numerical K/f possibilities. K is actual C count from
  # source ENTRY to target ENTRY; f is intervening complete foreign count.
  pairs=[]
  for L in allowed:
   for f in range(L//2+1):
    K=L-2*f
    if source=='C'and K<1:continue
    assert K>=0 and K+f+1<=7
    pairs.append(dict(effective_L=L,actual_C_count_K=K,intervening_complete_foreigns_f=f,max_ordinary_monotone_epochs=K+f+1))
  windows.append(dict(source=source,ordinary_contact_actor=target,allowed_effective_L=allowed,all8_exact_angle_bounds=all_bounds,all_necessary_K_f_pairs=pairs,source_C_own_interval_required=source=='C',max_f=max(q['intervening_complete_foreigns_f']for q in pairs)))
assert len(windows)==28
ordinary=[r for r in windows if r['source']in'DCVU']
common=[r for r in windows if r['source']=='F_prefix']
qtail=[r for r in windows if r['source']=='Q_tail']
btail=[r for r in windows if r['source']=='B_tail']
assert all(set(r['allowed_effective_L'])<=set(range(2,7))for r in ordinary)
assert all(set(r['allowed_effective_L'])<=set(range(2,6))for r in common)
assert all(set(r['allowed_effective_L'])<=set(range(3,7))for r in qtail+btail)
assert max(r['max_f']for r in windows)==3
assert all(r['max_f']<=2 for r in common)
assert all(6 not in r['allowed_effective_L']for r in qtail if r['ordinary_contact_actor']=='U')
# Preserve a real wrap regression. This is a coefficient comparison, not
# a new rejection of the complete prepared CF history.
raw_CF=dict(actual_CF_feasible=l.trace(W['C']+W['F']+l.M)['feasible'],actual_T_coeff_pi_over4=-3,actual_T_coeff_beta=1,incorrect_unsigned_T_coeff_pi_over4=5,difference_pi_over4=8)
assert raw_CF['actual_CF_feasible']
D=['foreign_interval_packet_grammar_2026-10-24/manifest.json','audits/check_foreign_interval_grammar_independent.json','seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json','audits/check_foreign_kinked_barrier_turn_independent.json','one_foreign_first_contact_compression_2026-10-24/manifest.json','audits/check_one_foreign_contact_C_window_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
result=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual finite RAW G7 factor beginning at a genuine U, with complete actual words and actual final M11. The exact proxy clock needs no simplicity. The contact windows require the chosen actor be ordinary D/C/V/U and its contact be the chronological GLOBAL first new proxy contact. Arbitrarily many foreigners may precede that contact; no field or maturity law is transported through them.',all7_actual_heading_clock_interfaces=heading,
 exact_open_turn='Expand Q/B at actual F56 fine cuts. Set J=n_C+2*n_FORE, e_C=1 if last piece C, e_F=1 if last piece is terminal standalone F, and alpha_D=alpha_C=pi/4, alpha_V=pi/2-beta, alpha_U=alpha_Qtail=pi/2, alpha_Btail=pi/2+beta, alpha_F=pi+beta. Signed0edd gives b=#C-to-foreign boundaries=0 on this actual factor. Audited3117 therefore gives T_open=(pi/2)*(J-e_C-2*e_F)+alpha_last-alpha_first. This is an exact principal-turn identity with endpoint offsets, not positivity of every individual join.',
 monotone_marked_word_clock='At actual RAW boundaries J increases by1 on C, by2 on F/Q/B, and by0 on D/V/U. Actual headingCW is entry_headingCW-J modulo4. J is a proxy-word clock, not the physical fine-step R-minus-L rotation or a mass/energy budget.',
 source_to_ordinary_actor_definitions='Let K count actual C intervals from source ENTRY up to but excluding target ordinary ENTRY, including a source C own interval. For an ordinary source, f counts complete foreigners after its entry and before target entry. For a foreign-piece source, f counts complete foreigners strictly AFTER its own source foreign and before target entry; the remaining source kink/half-turn is retained separately. Put L=K+2f.',
 all28_source_ordinary_actor_windows=windows,
 source_turn_forms=dict(ordinary='T=L*pi/2+a(source)-a(target)',F_prefix='T=(L+1)*pi/2-beta-a(target)',Q_tail='T=L*pi/2-a(target)',B_tail='T=L*pi/2-beta-a(target)'),
 Jordan_bridge='At chronological GLOBAL first contact, the already drawn proxy is simple by definition. Every actual adjacent join is nonreversing (audited3117, RAW FF infeasible); each foreign is internally injective. Select earliest positive onset and give old vertices to their outgoing piece. The old subarc plus the new partial ordinary chord is a simple closed curve. The closing principal angle delta is strictly between -pi and pi: opposite tangents would overlap earlier, while same-direction collinear onset has delta0 and is retained. All displayed T forms exceed -pi/2 for K,f>=0, so T+delta cannot be -2pi. Jordan forces +2pi, hence pi<T<3pi. Replacing one-foreign K+2 by general L is justified by the now signed b0 grammar and exact open-turn identity, not by iterating one-foreign simplicity.',
 compression='The effective clocks are ordinary source L2..6, common F-prefix L2..5, Q/B tails L3..6, with the exact endpoint refinements in all28 rows. Thus f<=3; a common F-prefix source has f<=2. Every source-to-ordinary-contact arc has at most K+f+1<=7 ordinary monotone epochs. Their lengths, dormant ports and field resources remain unbounded. A tail source may touch its own source foreign plus three subsequent full foreigners; this is not a claim that at most three foreign WORDS are touched in every source class.',
 raw_CF_wrap_scope_control=raw_CF,
 not_claimed=['A GLOBAL first contact whose actor lies inside a foreign F-prefix/tail is not covered by these28 windows.','No first-contact exclusion, arbitrary-tail simplicity or induction through a second foreign.','No replacement of actual producer C age by L=K+2f for identity maturation.','No bounded field/port state, finite automaton, decreasing mass resource, full ant-language coverage or capture.','No no-wrap formula for a prepared raw CF/CQ/CB factor outside the actual U-entry grammar.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'positive_clock_window.json').write_text(json.dumps(result,indent=2)+'\n')
print('Actual U-entry G7: b0, J=C+2FORE exact with terminal offsets. Global-first ordinary actor:28 exact L windows, f<=3 and at most7 ordinary monotone epochs. No foreign actor or contact exclusion.')
