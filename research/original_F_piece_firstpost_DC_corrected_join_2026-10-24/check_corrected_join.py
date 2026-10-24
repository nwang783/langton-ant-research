"""Exact81+1+2 composition, preserving rejected original143d proof."""
from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
paths={
 'original':'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json',
 'partial':'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification.json',
 'C_repair':'F_firstC_N4_U_upper_repair_2026-10-24/C_N4_U_repair.json',
 'D_repair':'F_firstD_N4_active_CORE_gate_repair_2026-10-24/D_N4_gate_repair.json'}
d={k:json.loads((R/p).read_text())for k,p in paths.items()}
def key(r):return r['first_post_RAW'],r['actor'],tuple(r['pose']),r['K']
U={key(r):r for r in d['original']['all84_firstpostD_C_proper_F_contact_closures']};assert len(U)==84
P={key(r['original_row']):r for r in d['partial']['all81_retained_exclusions']};assert len(P)==81
C=key(d['C_repair']['exact_original_residue_lift']['original_row']);assert C==('C','U',(-1,-1,0),4)
D={}
for r in d['D_repair']['all6_typed_gate_by_final_actor_closures']:
 k=key(r['original_OPEN_label']['original_row']);D.setdefault(k,[]).append(r)
assert len(D)==2 and all(len(v)==3 and{r['actual_immediate_loss_RAW']for r in v}==set('DVU')for v in D.values())
assert not set(P)&{C}and not set(P)&set(D)and C not in D
assert set(U)==set(P)|{C}|set(D)
assert {key(r['original_row'])for r in d['partial']['all3_OPEN_N4_restoration_residues']}=={C}|set(D)
ledger=[]
for k in sorted(U):
 if k in P:route='qualified81_partial_theorem';piece=P[k]
 elif k==C:route='separate_actual_firstC_upper_birth_repair';piece=d['C_repair']['exact_original_residue_lift']
 else:route='separate_actual_firstD_all3_active_CORE_gate_repairs';piece=D[k]
 ledger.append(dict(key=k,actual_geometry={x:U[k][x]for x in('actor','pose','old_F_parameter','new_parameter','K')},route=route,dependency_case=piece,original_full_pair_proof_NOT_used=True))
reports=['audits/check_F_DC_partial_qualification_independent.json','audits/check_F_firstC_N4_U_repair_independent.json','audits/check_F_firstD_N4_repair_independent.json']
for p in reports:assert json.loads((R/p).read_text())['status'].startswith('PASS')
deps=[*paths.values(),*reports,'original_F_piece_firstpost_DC_2026-10-24/manifest.json','original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification_manifest.json','F_firstC_N4_U_upper_repair_2026-10-24/manifest.json','F_firstD_N4_active_CORE_gate_repair_2026-10-24/manifest.json','first_post_F_DC_source_closure_2026-10-24/manifest.json','first_post_F_DC_source_closure_2026-10-24/terminal_C_maturity_premise_qualifier_manifest.json','audits/check_first_F_DC_source_independent.json','audits/check_first_F_DC_terminal_C_qualification_independent.json']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_COMPOSITION_REVIEW',scope='Actual U-entry completeG8 prefix,FIRSTF,first ordinaryD/C,arbitrary ordinary suffix and actual finalM11. GLOBAL first new proxy contact cannot be owned by proper originalF piece. This is corrected81+1+2 source-level composition, not original143d pair-current proof or arbitrary-tail simplicity.',all84_disjoint_corrected_case_ledger=ledger,exact_disjoint_counts={'qualified_partial':81,'separate_firstC_repair':1,'separate_firstD_repairs':2},all20_FOREIGN_EXIT_owner_aliases_remain_outgoing_b1=d['original']['all_foreign_EXIT_owner_aliases'],FOREIGN_EXIT_scope='Twenty old s1 labels belong outgoingfirstD/C, whose separate signed8b58+mandatory5e243 source closure applies. They are not properF-piece cases or assigned F-angle windows.',original143d_full84_and_universal_pair_proof_remain_rejected=True,local_ACTIVE_CORE_erosion_pairs_preserved=True,new_hole_guard_scope='Separate repairs do not deny R-restoration. They bind actual first-base entry WHITE/core deletion or companion-port last-L/full-produced-age history; F30 guard follows SAME original physical identity through exact first-loss endpoints.',not_claimed=['No arbitrary-tail proxy simplicity.','No later ordinary outgoing source closure.','No second foreign.','No FORE-born age rule or indefinite pair-current reserve.','No language coverage or capture.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in deps})
(H/'corrected_join.json').write_text(json.dumps(out,indent=2)+'\n');print('Corrected properF firstD/C: exact84=qualified81 + separateC1 + separateD2; original143d staysrejected.')
