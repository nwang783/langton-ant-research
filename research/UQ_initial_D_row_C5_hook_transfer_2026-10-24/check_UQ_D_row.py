"""All-m>=6 initial D-row barrier at the OPEN Q C5 next-FOREIGN head.
No finite-prefix exhaustion, ordinary length cap, or transfer iteration.
"""
from pathlib import Path
import json,hashlib,importlib.util
from fractions import Fraction as F
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return (*q,h)
def local(g,p):return l.rot(sub(g,p[:2]),(-p[2])%4)
def relative(p,source):return(*local(p[:2],source),(p[2]-source[2])%4)
T=(-4,-7,1);qexit=after(W['Q']);assert qexit==(-4,-4,2)
row=[]
for i in range(6):
 p=(-4-i,-4-i,2);g=(-6-i,-4-i)
 assert p==after(W['D']*i,qexit)and add(p[:2],l.rot((2,0),2))==g
 assert l.trace(W['D'])['last'][(2,0)]==('R',8)
 row.append(dict(zero_based_initial_D_index=i,actual_D_ENTRY=p,SAME_common_cell=g,own_R_birth=o.describe('D',8),source_ENTRY_C_clock=0,actual_preceding_RAW='Q'if i==0 else'D'))
# Parity-refined N4 half-plane: CURRENT through source C3 is a separately
# retained theorem. Only TWO N4 first-loss ports are in the actual sector.
ports=[]
for A in'DVU':
 ct=l.trace(W[A]+l.M)
 for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
  p=(*sub((2,0),slot),0);ep=after(W[A],p);active=(sum(p[:2])%2==0)
  assert not active or ep[1]>=2
  ports.append(dict(consumer=A,input=slot,ENTRY=p,RAW_EXIT=ep,active_sector=active,actual_first_L=o.describe(A,ct['first'][slot][1])))
assert len(ports)==8 and sum(z['active_sector']for z in ports)==2
# Relative x+y+heading parity is invariant at EVERY physical step; this is
# not a cap/heuristic atomic-sector assumption.
for A in'DCVUFQB':
 p=(0,0,0)
 for c in W[A]:p=after(c,p);assert(sum(p[:2])+p[2])%2==0
# E5 has at least one BASE and last plainV/U by actual interval grammar.
# If it has exactly one BASE it cannot be U (literal CU); soleV fixes C5.
cu=l.trace(W['C']+W['U']+l.M);assert not cu['feasible']
pv=after(W['V'],(0,0,1));lastV=(*sub(T[:2],pv[:2]),1)
C5= (lastV[0],lastV[1]+1,2);assert after(W['C'],C5)==lastV
single_tag=row[1];rel=relative(C5,tuple(single_tag['actual_D_ENTRY']))
assert rel==(2,0,0)and local(tuple(single_tag['SAME_common_cell']),C5)==(0,0)
single=dict(last_BASE='V',actual_C5_ENTRY=C5,held_initial_D_index=1,reader_in_D_frame=rel,old_common_in_C5_ENTRY_CORE=True,exclusion='Parity-refined N4 guard retains common at y0<=1, but it is in C5 entryCORE before execution.')
# All SIX possible penultimate/last BASE pairs. Their coordinates alone
# choose one of the first six genuine old D common identities.
interfaces=[]
for last in'VU':
 dl=after(W[last],(0,0,1));lp=(*sub(T[:2],dl[:2]),1)
 for pen in'DVU':
  dp=after(W[pen],(0,0,1));pp=(*sub(lp[:2],dp[:2]),1)
  slot=(1,0)if pen=='D'else(2,1);g=add(pp[:2],l.rot(slot,1));i=-6-g[0]
  assert 0<=i<6 and g==tuple(row[i]['SAME_common_cell'])
  sp=tuple(row[i]['actual_D_ENTRY']);rel=relative(pp,sp)
  assert rel==((2,-1,3)if pen=='D'else(3,-2,3))
  assert rel[1]<0
  ct=l.trace(W[pen]+l.M)
  if pen=='D':assert slot in l.K and ct['first'][slot]==('L',5)
  else:assert ct['first'][slot]==('R',7)
  interfaces.append(dict(penultimate_BASE=pen,last_BASE=last,penultimate_ENTRY=pp,last_ENTRY=lp,FOREIGN_ENTRY=T,held_initial_D_index=i,SAME_old_common_cell=g,producer_ENTRY=sp,reader_in_D_frame=rel,source_ENTRY_C_clock=5,reader_slot=slot,actual_first_requirement=o.describe(pen,ct['first'][slot][1]),route='CURRENT_ENTRY_CORE'if pen=='D'else'CURRENT_first_WHITE',guard='Independently qualified fresh-D W5 targety<0 guard on a SIMPLE executed ordinary source-prefix. Every earlier/own full C-tail offset is counted from the actual RAW D ENTRY, not full EXIT.'))
assert len(interfaces)==6
# Explicit SPECIAL-prefix SAME-hook persistence lift, not a generic claim
# across arbitrary foreign histories. 488 makes UQ/UB ordinary tails simple;
# 715 makes any first CURRENT loss cause a contact with that actual FOREIGN.
hook_json=json.loads((R/'foreign_Q_B_hook_contact_reserve_2026-10-24/hook_contact_reserve.json').read_text())
ordinary_hooks=[]
for A in'QB':
 c=next(z for z in hook_json['foreign_cases']if z['foreign']==A)
 born=c['guaranteed_same_original_hook_tags']
 assert{tuple(z['original_A_cell'])for z in born}=={(-1,-1),(-2,-1),(-3,-1),(-3,-2)}
 for z in born:assert l.trace(W[A])['last'][tuple(z['original_A_cell'])]==('R',z['last_R_tick0'])
 ordinary_hooks.append(dict(selected_prefix='U'+A,all4_actual_same_R_births=born,statement='At every completed ordinary cut of ANY actual U A ordinary*+realM factor these four SAME sourceA hook IDs remain CURRENT. A first CURRENT loss would create a forbidden nonadjacent contact with the originalFOREIGN by signed715 and signed488. No nextFOREIGN is included by this lemma.'))
# Ordinary E5 hook rewrite in signedff4 directly crosses the original Q tail,
# so the newly signed special UQ ordinary-tail simplicity excludes it.
oldA=(-7,-3);oldB=(-7,-7);newA=(-9,-5);newB=(-1,-5)
assert add(oldA,(0,-2))==add(newA,(2,0))==(-7,-5)
rewrite_contact=dict(old_Q_tail=(oldA,oldB),new_U_E5_segment=(newA,newB),old_s='1/2',new_t='1/4',strict_nonadjacent_contact=True)
# Reader-independent FOREIGN exitCORE capture completeness: an external
# CURRENT old tag can be silently captured only by a true BLACK input which
# is physically read within this actual RAW+M. All15 literal sites included.
capture=[]
for A in'FQB':
 ep=after(W[A]);raw=l.trace(W[A]);ctx=l.trace(W[A]+l.M);I=set(map(tuple,l.literal_geometry(W[A])['inputs']))
 for q in sorted({add(ep[:2],l.rot(k,ep[2]))for k in l.K}):
  if q in l.K:route='already_ENTRY_CORE_not_an_external_CURRENT_tag'
  elif q in raw['first']:
   route='actual_RAW_first_'+raw['first'][q][0]
  else:
   assert q in I and ctx['first'][q][0]=='L';route='unread_RAW_external_BLACK_input_physically_read_in_actual_M'
  capture.append(dict(actor=A,RAW_EXIT_CORE_cell=q,route=route,actual_first=ctx['first'].get(q)))
assert len(capture)==15
# Bind actual large control rather than counting failed finite models.
control=json.loads((R/'fresh_D_negative_N4_common_guard_2026-10-24/negative_N4_common.json').read_text())['selected_actual_UQ_control']
assert control['mass']==80 and control['failed_GLOBAL_tick0']==570 and control['source_common_birth_tick0']==130
D=['foreign_Q_B_hook_contact_reserve_2026-10-24/manifest.json','audits/check_foreign_hook_reserve_independent.json','original_F_piece_firstpost_DC_2026-10-24/manifest.json','original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification_manifest.json','audits/check_F_DC_partial_qualification_independent.json','immediate_U_FOREIGN_ordinary_tail_simplicity_2026-10-24/manifest.json','audits/check_immediate_U_FOREIGN_tail_independent.json','Q_C5_next_FOREIGN_loss_frontier_2026-10-24/manifest.json','audits/check_Q_C5_frontier_independent.json','foreign_C5_joint_rewrite_frontier_2026-10-24/manifest.json','audits/check_FOREIGN_C5_rewrite_independent.json','foreign_interval_packet_grammar_2026-10-24/manifest.json','audits/check_foreign_interval_grammar_independent.json','fresh_D_negative_N4_common_guard_2026-10-24/manifest.json','audits/check_fresh_D_negative_N4_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual finite factor U Q D^m w A +actual finalM11, m>=6, w an arbitrary ordinary D/C/V/U word, exactly5 actual Cs total in D^m w, A a complete NEXT F/Q/B and no otherFOREIGN in w. All four SAME sourceQ hook originals remain CURRENT through the ordinary prefix and at A RAW EXIT, and physically SAME BLACK through actual M. No bound on m, any middle epoch, total word length or seed mass. Earlier physical history before selectedplainU is arbitrary. This is one named special-prefix C5 transfer, not a generic-sourceQ or repeatedFOREIGN theorem.',special_UQ_UB_all_length_ordinary_same_hook_lift=ordinary_hooks,all6_real_initial_D_common_births=row,all8_parity_refined_N4_first_CURRENT_loss_ports=ports,N4_extension='Signed qualified fresh-D common-through-C3 plus exact relative parity leaves only U(3,-1,N) and U(2,-2,N) N4 loss ports; both complete at y>=2. Subsequent N motion cannot reach a target y<=1. Thus SAME common CURRENT at every N4 target heady<=1 under original simple-prefix/preceding-RAW premises. This is a new literal endpoint refinement, not an old-age law after a FOREIGN.',sole_E5_V_case=single,sole_E5_U_literal_conflict=cu,all6_penultimate_last_E5_BASE_interfaces=interfaces,Q_ordinary_E5_rewrite_nonadjacent_contact=rewrite_contact,all15_next_FOREIGN_exitCORE_capture_sites=capture,actual_80_cell_control_dependency=dict(file='fresh_D_negative_N4_common_guard_2026-10-24/negative_N4_common.json',all570_reads_and_fields_retained_there=True,source_R130_staysSAME_current=True,interpretation='This real candidate fails already atC5 R12. It does not reach the counterfactual final-interface readers or complete anotherFOREIGN; the seven interface rows prove the arbitrary-length family separately.'),proof_steps=[
 'Apply signed488 only to the actually completed UQ ordinary prefix, ending at its last ordinary RAW with real M supplied by nextA first11. That entire auxiliary prefix is simple; every selected initial D producer-to-reader ordinary subarc is therefore simple too. Each of the first6 D RAWs has an actual preceding Q/D RAW and creates its common at source-entry clock0. Real D/DC containing-tail cases are covered by qualified45, never reset at full EXIT.',
 'The explicit special-prefix715+488 lift retains all four SAME Q hook identities through the arbitrary ordinary prefix, without a C-count bound. Thus they are CURRENT at nextA ENTRY. The separately checked ff4 E5 rewrite crossing at old s1/2,newt1/4 is a consistent narrower check, not the basis of a generic FOREIGN permanence assertion. No nextFOREIGN is crossed by this intermediate lemma.',
 'If A physically first-deletes any oldhook, signed1c2 forces A ENTRY T=(-4,-7,E). Actual interval grammar makes the last ordinary RAW a plainV/U and makes E5 nonempty. If E5 has one BASE, soleU fails CU and soleV forces C5 ENTRY(-7,-5,S), containing second-D common in ENTRY CORE. The parity-refined N4 guard retains that exact original at this cut, contradiction.',
 'If E5 has at least2 BASEs, its last two are precisely pen inD/V/U and last inV/U. Their exact inverse endpoints select old D indices2..5. Every selected common is CURRENT by the qualified W5 negative-y source guard and signed488 simplicity. PenD puts it in ENTRY CORE; penV/U firstR7 wants it WHITE. These contradictions occur in the ordinary prefix, before any candidate nextA execution. No depth or count bound was used.',
 'Therefore T cannot be attained by a completed nextA. No oldhook can physically first-delete in actual A RAW+M. Because the hooks were CURRENT at A ENTRY and every possible silent exitCORE capture is covered by actual RAW/marker BLACK input, all four remain CURRENT at A RAW EXIT and physically SAME BLACK through actual M. This invokes the genericC4/E5 facts on their original source only once; no new source field is identified or iterated.'
 ],limits=['The selected prefix is specifically plain U then immediate firstQ and an initial D run m>=6. Initial mixed D/V/U rails and m<6 remain outside this theorem.','Original143d universal F-pair/full84 remains rejected. Only mandatory45 qualified fresh-D common components are used.','No ordinary fine-path simplicity, physical-WHITE permanence, SOURCE-U-star transfer, complete-field equality, all-C5/generalQ result, thirdFOREIGN induction, language coverage or capture.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'UQ_D_row.json').write_text(json.dumps(out,indent=2)+'\n')
print('All-m>=6 UQ initial-D row:8 N4 ports,one soleV+six penultimate interfaces,15 CORE sites. One named nextFOREIGN C5 hook transfer, no middle length cap.')
