"""Exact ownership/first-letter composition; no new word search."""
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
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def k(r):return r['foreign'],r['atom'],tuple(r['head']),r['h']
# Real FOREIGN-EXIT chart, not the first laterBASE chart. In particular a
# genuine leadingC is b1=C at0N; its later W/N stages stay in this chart.
normal=[]
for A in'FQB':
 ep=after(W[A]);assert ep[2]==2
 norm=lambda p:(*l.rot(sub(p[:2],ep[:2]),-ep[2]),(p[2]-ep[2])%4)
 cuts=[(0,0,0)]+([after(W['F'])]if A in'QB'else[])+[ep]
 pieces=[z(norm(p))for p in cuts]
 assert pieces=={'F':[( -7,-3),(-1,-1)],'Q':[(-7,-7),(-1,-5),(-1,-1)],'B':[(-5,-9),(1,-7),(-1,-1)]}[A]
 assert norm(ep)==(0,0,0)
 normal.append(dict(actual_FOREIGN=A,actual_RAW_EXIT_in_source_ENTRY_chart=ep,actual_repaired_pieces_in_EXIT_N_chart=pieces,first_ordinary_ENTRY_in_same_chart=(0,0,0),all_possible_actual_first_ordinary_RAWs=list('DCVU'),leadingC_remains_first_C_at0N_not_first_later_BASE=True,kink_is_real_F56_fine_cut_not_marked_CORE=A in'QB'))
# Q/B closed universe and exact owner-aware split. Hook CURRENT applies
# at GLOBAL-first actorENTRY only, and all true hook input actors remain
# in LOSS rather than being incorrectly called entry colour conflicts.
split=json.loads((R/'Q_B_foreign_first_contact_hook_split_2026-10-24/hook_split.json').read_text());flat=[r for a in split['foreign_cases']for r in a['all_colour_compatible_earliest_contact_owners_and_clock_routes']]
assert len(flat)==41 and sum(a['exact_geometry_head_count']for a in split['foreign_cases'])==184
cols=Counter()
for a in split['foreign_cases']:
 cols.update(a['held_hook_context_classification']);assert a['exact_geometry_head_count']==sum(a['held_hook_context_classification'].values())
assert cols=={'WHITE':78,'CORE':65,'compatible':41}
terminal=[r for r in flat if r['actual_outgoing_owner']=='outgoing_first_postFOREIGN_atom_b1'];proper=[r for r in flat if r not in terminal]
assert len(terminal)==20 and len(proper)==21
loss=[r for r in proper if r['hook_inputs']];miss=[r for r in proper if not r['hook_inputs']];assert(len(loss),len(miss))==(16,5)
loss_add=json.loads((R/'Q_B_foreign_first_contact_hook_split_2026-10-24/hook_loss_closure_addendum.json').read_text())['all16_original_foreign_hook_loss_geometries_and_routes']
miss_add=json.loads((R/'Q_B_hook_MISS_first_contact_2026-10-24/five_MISS.json').read_text())['all5_exact_owner_aware_targets']
assert{k(r)for r in loss}=={k(r)for r in loss_add}and{k(r)for r in miss}=={k(r)for r in miss_add}
QB=[]
for r in proper:
 route='independently_signed_16_hook_LOSS_join'if r['hook_inputs']else'independently_signed_5_full_context_hook_MISS_closure'
 QB.append(dict(exact_signed_owner_aware_foreign_contact=r,route=route,true_hook_inputs_not_mislabeled_as_colour_conflicts=bool(r['hook_inputs'])))
assert Counter(r['route']for r in QB)=={'independently_signed_16_hook_LOSS_join':16,'independently_signed_5_full_context_hook_MISS_closure':5}
# F head universe. All four actual first-ordinary letters are covered.
# For V/U, 37 proper-head colour cuts +5 lower output guards are the same
# 42 proper geometric heads. For D/C, use only corrected84, never original
# rejected143d or its universalF-pair claim.
fo=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json').read_text());fc=json.loads((R/'original_F_piece_firstpost_DC_corrected_join_2026-10-24/corrected_join.json').read_text());fv=json.loads((R/'firstpostV_F_piece_first_contact_2026-10-24/F_piece_contact.json').read_text());fu=json.loads((R/'firstpostU_F_piece_first_contact_2026-10-24/F_piece_firstpostU.json').read_text());Fheads=fo['all42_genuine_proper_F_owned_angle_labels'];aliases=fo['all_foreign_EXIT_owner_aliases'];assert len(Fheads)==42 and len(aliases)==20 and not fo['all_piece_angle_impossible_rows']
Fkey=lambda r:(r['actor'],tuple(r['pose']))
assert len({Fkey(r)for r in Fheads})==42
D_C=fc['all84_disjoint_corrected_case_ledger'];assert len(D_C)==84
for first in'DC':assert{Fkey(r['actual_geometry'])for r in D_C if r['key'][0]==first}=={Fkey(r)for r in Fheads}
assert fc['original143d_full84_and_universal_pair_proof_remain_rejected']
held={(0,0),(0,1),(-3,-1),(-2,-1)};guards={}
for first,data,field in[('V',fv,'all5_proper_Fsource_lower_output_guards'),('U',fu,'all5_proper_F_source_coordinate_guards')]:
 rows=[];guard=data[field];assert len(guard)==5;gkeys={(r['atom'],tuple(r['head']),r['h'])for r in guard};assert data['all62_closed_contact_head_count']==62 if first=='V'else data['all62_F_closed_contact_heads']==62
 for r in Fheads:
  p=tuple(r['pose']);tr=l.trace(W[r['actor']]+l.M);bad=[]
  for q in sorted(held):
   loc=l.rot(sub(q,p[:2]),-p[2]);f=tr['first'].get(loc)
   if loc in l.K or f and f[0]=='R':bad.append(dict(SAME_CURRENT_at_entry=q,local=loc,role='ENTRY_CORE'if loc in l.K else'first_WHITE',actual_first=f,owner=o.describe(r['actor'],f[1])if f else None))
  if bad:route='signed_current_four_tag_colour_cut'
  else:assert(r['actor'],p[:2],p[2])in gkeys;route='signed_actual_negative_y_FOREIGN_output_guard'
  rows.append(dict(first_actual_ordinary=first,proper_F_head=r,route=route,actual_colour_conflicts=bad))
 assert Counter(r['route']for r in rows)=={'signed_current_four_tag_colour_cut':37,'signed_actual_negative_y_FOREIGN_output_guard':5};guards[first]=rows
F=dict(all42_proper_F_owned_heads=Fheads,all84_actual_first_D_C_corrected_routes=D_C,all42_actual_first_V_proper_routes=guards['V'],all42_actual_first_U_proper_routes=guards['U'],all_four_first_letters_are_actual_b1_not_first_BASE_after_leadingC=True,original143d_universal_pair_proof_remains_rejected=True,first_D_C_corrected_route_counts=fc['exact_disjoint_counts'])
# EXIT aliases are not foreign sources. Exact outgoing ordinary owner
# theorem a213 handles them for ANY actual b1 including leadingC. No
# foreign-piece angle window is ever applied to these terminal returns.
exit_routes=dict(all20_F_closed_EXIT_alias_geometries=aliases,all20_Q_B_colour_compatible_closed_EXIT_aliases=terminal,route='signed_a213_all_postFOREIGN_ordinary_outgoing_old_owners',applies_to_any_actual_first_ordinary_b1='D/C/V/U including actual leadingC',no_FOREIGN_piece_clock_on_outgoing_b1_alias=True)
S=[('Q_B_foreign_first_contact_hook_split_2026-10-24/manifest.json','audits/check_Q_B_hook_owner_split_independent.json'),('Q_B_foreign_first_contact_hook_split_2026-10-24/hook_loss_closure_addendum_manifest.json','audits/check_Q_B_hook_loss_join_independent.json'),('Q_B_hook_MISS_first_contact_2026-10-24/manifest.json','audits/check_five_hook_MISS_independent.json'),('firstpostV_F_piece_first_contact_2026-10-24/manifest.json','audits/check_F_piece_firstpostV_independent.json'),('firstpostU_F_piece_first_contact_2026-10-24/manifest.json','audits/check_F_piece_firstpostU_independent.json'),('original_F_piece_firstpost_DC_corrected_join_2026-10-24/manifest.json','audits/check_original_F_DC_corrected_join_independent.json'),('one_foreign_all_ordinary_owners_2026-10-24/manifest.json','audits/check_all_ordinary_owner_join_independent.json')]
binds=[]
for mp,ap in S:
 p,a=R/mp,R/ap;assert p.exists()and a.exists(),(mp,ap);m=json.loads(p.read_text());au=json.loads(a.read_text());sha=hashlib.sha256(p.read_bytes()).hexdigest();assert au['status'].startswith('PASS')and sha in json.dumps(au),(mp,ap)
 for fn,want in m['files'].items():assert hashlib.sha256((p.parent/fn).read_bytes()).hexdigest()==want
 binds.append(dict(manifest=mp,manifest_sha256=sha,independent_report=ap,independent_report_sha256=hashlib.sha256(a.read_bytes()).hexdigest(),independent_status=au['status']))
D=[R/mp for mp,_ in S]+[R/ap for _,ap in S]+[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_COMPOSITION_REVIEW',theorem='Under actual U-entry completeG8 prefix then FIRST completeF/Q/B and arbitrary ordinary-only suffix with actual finalM11, GLOBAL first new ordinary proxy contact cannot be outgoing-old-owned by any proper piece of that originalFOREIGN. Source-EXIT aliases are routed to their actual outgoingb1 ordinary owner and separately excluded bya213. PreFOREIGN old sources remain OPEN; no arbitrary-tail simplicity.',all3_actual_FOREIGN_EXIT_N_normalizations=normal,Q_B_184_closed_contact_head_counts=dict(cols),all21_proper_Q_B_FOREIGN_owned_compatible_contact_routes=QB,F_all_four_first_ordinary_source_cover=F,actual_FOREIGN_EXIT_alias_owner_routes=exit_routes,all7_independently_signed_dependency_bindings=binds,strict_scope=['GLOBAL-first chronological SIMPLE stopping, not merely firstFOREIGN contact after earlier ordinary selfcontacts','one FIRSTFOREIGN, no laterFOREIGN','firstordinaryC is actually0N atFOREIGNEXIT, not renormalized at its laterBASE','all oldsource kink vertices use actual outgoing piece ownership','SAME CURRENT reserves only at actorENTRY; LOSS actors may consume tags during attemptedcontact but have separate causal cuts','actual finalM11 retained, no completednextG7 assumption','corrected81+1+2 F/DC proof, not rejected original143d universalpair','preFOREIGN sources and arbitrarytail simplicity remain separate'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'FOREIGN_join.json').write_text(json.dumps(out,indent=2)+'\n');print('OriginalFORE proper owners covered:QB143 CURRENTcuts+16LOSS+5MISS;F42 properheads for each actualb1 D/C/V/U. EXITaliases routea213; leadingC retained.')
