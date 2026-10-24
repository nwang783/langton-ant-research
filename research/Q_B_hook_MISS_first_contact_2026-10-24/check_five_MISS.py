"""Five proper Q/B-tail hook-MISS GLOBAL-first contacts, arbitrary ordinary length.
Actual final-R/CORE funding, fresh donor guards, and explicit Q V extra C-reader.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def raw(T):return ''.join(W[a]for a in T)
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  s,t=Q(det(q,v),de),Q(det(q,u),de)
  return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(Q(0),lo)),str(min(Q(1),hi))])if max(0,lo)<=min(1,hi)else None
HOOK={'Q':{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},'B':{(-2,-4),(-1,-4),(0,-4),(0,-3)}};VERTS={'Q':[(-7,-7),(-1,-5),(-1,-1)],'B':[(-5,-9),(1,-7),(-1,-1)]};HOLE=(0,-2)
SP=R/'Q_B_foreign_first_contact_hook_split_2026-10-24/hook_split.json';sj=json.loads(SP.read_text());targets=sj['all5_genuine_FOREIGN_owned_W5_hook_MISS_tail_gates'];assert{(q['foreign'],q['atom'],tuple(q['head']),q['h'])for q in targets}=={('Q','V',(0,-1),3),('B','V',(0,-1),3),('B','V',(1,-2),3),('B','U',(0,-1),3),('B','U',(2,-1),3)}
for t in targets:
 assert t['heading_compatible_C_counts']==[5]and t['actual_outgoing_owner']==t['foreign']+'tail'and t['all4_hook_complete_RAW_plus_actual_M11_context_MISS']
 tr=l.trace(W[t['atom']]+l.M);p=(*t['head'],t['h']);assert all(l.rot(sub(q,p[:2]),-p[2])not in tr['first']for q in HOOK[t['foreign']])
# A real last-R producer cover, including every final RAW R at active CORE
# cells. All clocks are actual postFOREIGN ENTRY clocks; SOURCE C completion
# consumes one more C. A C atK5 cannot complete before targetENTRY5.
origins={};birthfacts=[]
for A in'QB':
 ep=after(W[A]);ft=l.trace(W[A]);old=add(ep[:2],l.rot(HOLE,2));last=ft['last'][old];assert last==('L',56 if A=='Q'else 66)and list(old)not in l.literal_geometry(W[A])['outputs']and HOLE not in l.K;birthfacts.append(dict(foreign=A,hole_postEXIT=HOLE,actual_FOREIGN_cell=old,last_L_tick0=last[1],last_L_read_number1=last[1]+1,WHITE_after_actual_FOREIGN=True,outside_FOREIGN_EXIT_CORE=True))
 rows=[]
 for atom in'DCVU':
  tr=l.trace(W[atom]+l.M);wt=l.trace(W[atom]);writes=[(p,t)for p,(c,t)in wt['last'].items()if c=='R']
  for K in range(6):
   if atom=='C'and K==5:continue
   hd=(-K)%4
   for slot,tick in writes:
    p=(*sub(HOLE,l.rot(slot,hd)),hd);q=dict(foreign=A,producer=atom,true_producer_ENTRY_C_clock=K,true_producer_RAW_EXIT_C_clock=K+int(atom=='C'),pose=p,actual_final_R_local=slot,R_tick0=tick,R_read_number1=tick+1,RAW_EXIT=after(W[atom],p),CORE_R_writes_included=True)
    if(sum(p[:2])+hd)%2:q['classification']='sector'
    elif K==0 and p[1]<0:q['classification']='initial_N0_head_below0'
    elif K==1 and p[1]<1:q['classification']='initial_W1_head_below1'
    else:
     touches=[]
     for tag in sorted(HOOK[A]):
      loc=l.rot(sub(tag,p[:2]),-hd);f=tr['first'].get(loc)
      if f:touches.append(dict(SAME_hook=tag,local=loc,actual_first=f,owner=o.describe(atom,f[1])))
     hits=[contact(a,b,*chord(atom,p))for a,b in zip(VERTS[A],VERTS[A][1:])]
     if touches:q.update(classification='would_touch_CURRENT_original_hook_before_target',hook_touches=touches)
     elif any(hits):q.update(classification='earlier_actual_FOREIGN_proxy_contact',contacts=hits)
     else:q['classification']='last_R_endpoint_obligation'
    rows.append(q)
 assert len(rows)==208;origins[A]=rows
qkeep=[q for q in origins['Q']if q['classification']=='last_R_endpoint_obligation'];bkeep=[q for q in origins['B']if q['classification']=='last_R_endpoint_obligation'];assert len(qkeep)==5 and len(bkeep)==10
assert Counter(q['classification']for q in origins['Q'])=={'sector':104,'would_touch_CURRENT_original_hook_before_target':59,'initial_N0_head_below0':18,'initial_W1_head_below1':18,'earlier_actual_FOREIGN_proxy_contact':4,'last_R_endpoint_obligation':5}
assert Counter(q['classification']for q in origins['B'])=={'sector':104,'would_touch_CURRENT_original_hook_before_target':54,'initial_N0_head_below0':18,'initial_W1_head_below1':18,'earlier_actual_FOREIGN_proxy_contact':4,'last_R_endpoint_obligation':10}
# Q V target: explicit lift of three signed non-C predecessor branches. The
# only old U-specific step was CU prohibition; retain and handle prior C here.
QP=R/'foreign_Q_W5_deleted_core_guard_2026-10-24/Q_W5_deleted_core_guard.json';qj=json.loads(QP.read_text());oldprec=qj['all3_actual_immediate_previous_RAW_BLACK_hole_obligations'];assert len(oldprec)==3 and len(qj['all9_S2_donor_by_actual_predecessor_cases'])==9
assert W['V'][:11]==W['U'][:11]==l.M
qV=(0,-1,3);qprec=[]
for atom in'DCVU':
 hd=(qV[2]+1)%4 if atom=='C'else qV[2];ep=after(W[atom],(0,0,hd));p=(qV[0]-ep[0],qV[1]-ep[1],hd);assert after(W[atom],p)==qV
 if atom!='C':
  oldrow=next(q for q in oldprec if q['actual_previous_RAW']==atom);assert tuple(oldrow['actual_previous_head'])==p
  loc=l.rot(sub(HOLE,p[:2]),-hd);assert l.trace(W[atom]+l.M)['first'][loc]==('L',len(W[atom])+1)
  qprec.append(dict(actual_previous_RAW=atom,pose=p,requires_hole_BLACK_before_previous_RAW=True,physical_hole_read=o.describe(atom,len(W[atom])+1),signed_exact_3reader_funding_proof_applies=True,premise_lift='TargetV and targetU have identical entrypose0,-1W and actualfirstM11. All origin/deadline/source-reader facts precede targetENTRY; no body after first11 is used in these3 branches.'))
 else:
  assert p==(0,-2,0)and HOLE in {add(p[:2],l.rot(q,hd))for q in l.K};qprec.append(dict(actual_previous_RAW='C',pose=p,hole_in_actual_ENTRY_CORE=True,needs_new_below_source_reader_extension=True))
assert l.trace(W['C']+W['V']+l.M)['feasible']and not l.trace(W['C']+W['U']+l.M)['feasible']
Q_C_READER=(0,-2,0);Q_C_KINK=z(Q_C_READER);assert Q_C_KINK==VERTS['Q'][1]==(-1,-5)
Q_C_REPEAT=dict(actual_previous_C_entry=Q_C_READER,actual_C_entry_C_clock=4,corrected_ENTRY=Q_C_KINK,genuine_old_Q_F56_fine_cut_vertex=VERTS['Q'][1],old_vertex_is_NOT_assigned_a_MARKED_CORE=True,cut='Earlier nonadjacent corrected vertex repeat before C RAW, already at preceding ordinary RAW END. Not legitimate adjacency to oldFORE because oldFORE ended at(-1,-1) and fourCs elapsed.')
# All five Q origin obligations remain a conservative cover for funding h at
# the earlier C readerENTRY4. Fresh source C keeps its own +1 clock shift.
qC=[];reader=(0,-2,0)
for q in qkeep:
 K=q['true_producer_ENTRY_C_clock'];a=q['producer'];p=tuple(q['pose']);ep=tuple(q['RAW_EXIT'])
 if K==4:
  assert a in'VU'and ep==(1,-1,0);assert ep[0]>reader[0]and ep[1]>reader[1];cut='sameK4_N_zeroC_cannot_move_back_to_readerC'
  rec=dict(origin=q,cut=cut,zero_remaining_C_before_reader=True)
 else:
  assert K==2 and p==(2,-2,2)and tuple(q['actual_final_R_local'])==(2,0);rel=(*l.rot(sub(reader[:2],p[:2]),-p[2]),(reader[2]-p[2])%4);assert rel==(2,0,2)
  tag=(2,0)if a=='C'else(1,0);Kentry={add(rel[:2],l.rot(x,rel[2]))for x in l.K};assert tag in Kentry
  rec=dict(origin=q,cut='fresh_donor_CURRENT_output_inside_C_reader_ENTRY_CORE',source_relative_reader=rel,true_SOURCE_ENTRY_age=2,true_C_SOURCE_postEXIT_age=1 if a=='C'else None,guard_tag=tag,guard='freshC O3 postEXIT1'if a=='C'else'freshV_B_or_U_a_R9_throughC3')
 qC.append(rec)
assert len(qC)==5
# B three h-required targets. Keep all10 origins, actual completion clocks,
# CORE births and the exact candidate first-R readers of fresh donors.
bh_targets=[('V',(0,-1,3)),('U',(0,-1,3)),('U',(2,-1,3))];bproof=[]
for atom,tp in bh_targets:
 loc=l.rot(sub(HOLE,tp[:2]),-tp[2]);tr=l.trace(W[atom]+l.M);fr=tr['first'][loc];assert fr[0]=='L';assert loc in l.K if tp[0]==0 else fr==('L',13)
 rec=dict(target=atom,pose=tp,hole_local=loc,hole_first_demand=o.describe(atom,fr[1]),needs_BLACK_at_target_ENTRY=True,all10_last_R_origin_cuts=[])
 for q in bkeep:
  a=q['producer'];K=q['true_producer_ENTRY_C_clock'];p=tuple(q['pose']);ep=tuple(q['RAW_EXIT']);co=q['true_producer_RAW_EXIT_C_clock'];item=dict(origin=q)
  if K==2:
   assert a in'DVU'and ep==(0,-2,2);assert ep[:2]==HOLE and ep!=tp;assert all(l.trace(W[x])['first'][(0,0)]==('L',0)for x in'DCVU');item.update(cut='R_birth_at_actual_EXIT_HEAD_CORE_dies_next_real_L0',next_actual_L_tick0=0,next_read_number1=1,at_least_one_intervening_RAW_before_W5_target=True,no_hidden_CORE_export=True)
  elif co==4 and ep[2]==0:
   assert ep[1]>=-1;item.update(cut='remaining_N_to_W_C_raises_y_above_target',post_producer_N_EXIT_y=ep[1],minimum_later_W_head_y=ep[1]+1);assert ep[1]+1>tp[1]
  elif a=='C'and K==4:
   assert co==5 and ep==(-2,-1,3);assert tp[0]>ep[0];item.update(cut='zero_remaining_C_W_cannot_move_right_from_x_minus2')
  else:
   assert a in'VU'and K==3 and p==(-1,0,1);rel=(*l.rot(sub(tp[:2],p[:2]),-p[2]),(tp[2]-p[2])%4);tag=(0,0);qloc=l.rot(sub(tag,rel[:2]),-rel[2]);rf=l.trace(W[atom]+l.M)['first'][qloc];assert rf[0]=='R'and rf[1]in(6,26);item.update(cut='fresh_V_r_or_U_LEFT_r_BLACK_vs_target_first_WHITE',source_relative_target=rel,true_source_ENTRY_age=2,SAME_donor_r=(0,0),target_local=qloc,actual_first_required_WHITE=o.describe(atom,rf[1]),fresh_guard='signed9cf freshV r through4 or freshU LEFT through3')
  rec['all10_last_R_origin_cuts'].append(item)
 bproof.append(rec)
assert len(bproof)==3 and all(len(q['all10_last_R_origin_cuts'])==10 for q in bproof)
# B V1,-2W requires original B g(-1,-2) WHITE. Its first CURRENT loss must
# happen earlier; candidate's own first g read is R12, not an earlier L.
BG=(-1,-2);bp=after(W['B']);gphysical=add(bp[:2],l.rot(BG,2));assert l.trace(W['B'])['last'][gphysical]==('R',67)and list(gphysical)in l.literal_geometry(W['B'])['outputs'];gloss=[]
for atom in'DCVU':
 geo=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
 for slot in map(tuple,geo['inputs']):
  for hd in range(4):
   p=(*sub(BG,l.rot(slot,hd)),hd);q=dict(consumer=atom,slot=slot,pose=p,RAW_EXIT=after(W[atom],p))
   if(sum(p[:2])+hd)%2:q['classification']='sector'
   elif any(l.rot(sub(tag,p[:2]),-hd)in tr['first']for tag in HOOK['B']):q['classification']='would_retire_or_contradict_held_hook_before_target'
   else:
    hs=[contact(a,b,*chord(atom,p))for a,b in zip(VERTS['B'],VERTS['B'][1:])]
    if any(hs):q.update(classification='earlier_actual_B_proxy_contact',contacts=hs)
    else:q['classification']='S2_marker_g_loss_funder'
   gloss.append(q)
gk=[q for q in gloss if q['classification']=='S2_marker_g_loss_funder'];assert len(gloss)==32 and {(q['consumer'],tuple(q['pose']))for q in gk}=={('V',(-1,1,2)),('U',(-2,2,2))}
gshadow=[];target=('V',(1,-2,3));tr=l.trace(W['V']+l.M);tg=l.rot(sub(BG,target[1][:2]),-3);assert tr['first'][tg]==('R',12)
for q in gk:
 a=q['consumer'];p=tuple(q['pose']);assert p[2]==2 and tuple(q['RAW_EXIT'])==(-2,-2,2);rel=(*l.rot(sub(target[1][:2],p[:2]),-p[2]),(target[1][2]-p[2])%4);tag=(1,0)if a=='V'else(0,1);actual_shadow=add(p[:2],l.rot(tag,p[2]));assert actual_shadow==(-2,1);local=l.rot(sub(tag,rel[:2]),-rel[2]);rr=l.trace(W['V']+l.M)['first'][local];assert rr==('R',26)
 btr=l.trace(W[a]);birth=btr['last'][tag];assert birth==('R',9 if a=='V'else 19)
 gshadow.append(dict(g_loss_consumer=q,true_postFOREIGN_ENTRY_clock=2,heading_deadline_reason='S withK<=5 impliesK2; K6 is beyond target.',actual_source_relative_target=rel,true_fresh_source_ENTRY_age=3,SAME_fresh_guard_cell=tag,guard_R_birth_tick0=birth[1],physical_new_shadow=actual_shadow,actual_target_first_WHITE=o.describe('V',26),cut='freshV_B_R9_or_U_LEFT_w_R19_CURRENT_BLACK_vs_actual_next_word_R8_read9',guard='freshV right throughC3'if a=='V'else'freshU LEFT throughC3',old_FOREIGN_g_may_really_die=True))
# Scope-preserving route set equality, not closed FOREEXIT source aliases.
routes=[]
for t in targets:
 A,a,p=t['foreign'],t['atom'],(*t['head'],t['h'])
 route='Q_same_entry_3reader_lift_plus_fresh_C_reader'if A=='Q'else'B_original_g_spend_creates_fresh_shadow'if a=='V'and p==(1,-2,3)else'B_deleted_hole_last_R_funding_obstruction'
 routes.append(dict(original_owner_aware_case=t,route=route,GLOBAL_first_contact_required=True,ordinary_suffix_only=True))
paths=[SP,R/'Q_B_foreign_first_contact_hook_split_2026-10-24/manifest.json',QP,R/'foreign_Q_W5_deleted_core_guard_2026-10-24/manifest.json',R/'audits/check_Q_W5_core_funding_independent.json',R/'foreign_Q_B_hook_contact_reserve_2026-10-24/manifest.json',R/'audits/check_foreign_hook_reserve_independent.json',R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'fresh_RAW_donor_right_C_ports_2026-10-24/manifest.json',R/'audits/check_fresh_donor_right_C_ports_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FIVE_Q_B_HOOK_MISS_GLOBAL_FIRST_CONTACT_CLOSURE_PENDING_REVIEW',scope='Only the five genuine outgoing Q/B-tail hook-MISS candidates atK5, under actual U-entry complete8 then FIRSTQ/B then arbitrary ordinary RAW suffix with actual markers, and GLOBAL FIRST-contact choice. No earlier ordinary selfcontacts. Full candidate context MISSES SAME hook; marker CORE loss is NOT aMISS. No F/other-source/arbitrary-tail/secondFOREIGN/capture result.',all5_exact_owner_aware_targets=targets,actual_FOREIGN_L_deleted_hole_births=birthfacts,all208_Q_CORE_inclusive_last_R_origins=origins['Q'],all208_B_CORE_inclusive_last_R_origins=origins['B'],Q_V_same_entry_three_predecessor_scope_lifts=qprec,Q_V_actual_C_V_feasible_so_C_U_prohibition_NOT_used=True,Q_V_all5_funding_origins_for_extra_C_reader=qC,Q_V_extra_C_reader_direct_fine_kink_repeat=Q_C_REPEAT,Q_V_lift_statement='Signed Q-U proof excludes all three actual nonC predecessors by the identical ENTRYpose/actualM11 and preENTRY funding clauses. No targetbody beyond sharedfirst11 is used. The additional actualC predecessor is retained; its ENTRY exactly repeats genuine oldQ F56 finecut vertex, already an earlier GLOBAL contact. Independently all five lastR origins are excluded by N4 backward cones or sourceC/V/U CURRENT-in-C-readerCORE at trueage2. Never lift the old CU prohibition to CV.',all3_B_hole_required_targets_and30_origin_cuts=bproof,all32_B_g_first_CURRENT_loss_roles=gloss,both_B_g_loss_creates_fresh_shadow_cuts=gshadow,all5_disjoint_case_routes=routes,last_R_completeness='A FORE-L-deleted WHITE cell requiredBLACK at targetENTRY must have a later actualR. Choose the lastR: it lies at a finalR coordinate of a completed earlier RAW, including CORE writes. All ordinary producers through clock5 are covered; C at5 cannot complete before target5. A CORE R subsequently deleted by next actualL cannot fund; a laterR would be a different already-enumerated origin.',hook_replacement_qualification='Before GLOBALfirstcontact all four SAME hooks remain CURRENT. Every earlier producer/consumer COMPLETEcontext mustMISS them: firstWHITE/core conflict invalid; a TRUE input would retire an originalhook and force an earlierFOREcontact. Recolored same-cell replacements do not restore the original ID.',fresh_guard_qualification='Only new RAW donors born AFTERFOREIGN use the signed fresh guards, with actual sourceENTRY-to-reader clock2or3 and SIMPLE ordinary source-prefix supplied by GLOBALfirst choice. OwnC tails are counted as actual laterC atoms. No old8 age is transported acrossFOREIGN.',CORE_and_marker_qualification='All R origins inside activeCORE are enumerated. CURRENT absorption is not physicaldeath; next actualL deaths are explicitly timed. Candidate firstWHITE guards may be marker-owned and therefore require actualM11 completion, not RAW-only completion.',conclusion='All five genuinely FOREIGN-owned hook-MISS tail candidates are excluded without a word-depth or rail-count cap. FOREEXIT terminal returns remain owned by outgoingb1 and are NOT removed by this theorem. TRUE hook-loss targets remain the separate signed archive lane.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'five_MISS.json').write_text(json.dumps(out,indent=2)+'\n');print('Five proper Q/B-tail hookMISS W5 cases: Q V uses explicit3-reader lift +C-reader; B three h targets use10 CORE-inclusive origins each; B V1,-2 g loss creates fresh V/U shadow. All clocks/CORE/actualM11 retained, arbitrary ordinary length only.')
