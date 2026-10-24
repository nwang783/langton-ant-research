from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'old_U_S4_V_immediate_FOREIGN_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='1d47beeee63435ae2901b11560d301e4ce89b76c95b0aa12db80e9594d2d9f41';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'adjacency.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
# Rebuild the already independently reviewed source-D/source-C normal reserves
# and ALL128 first-loss roles. Stop before the original overbroad target claim.
lib=S.parent/'check_original_F_piece_DC_independent.py';ns={'__file__':str(lib)};exec(lib.read_text().split("fg=tr(W['F'])")[0],ns);W,M,K,tr,rot,xy,I,ctx,raw,first=[ns[k]for k in('W','M','K','tr','rot','xy','I','ctx','raw','first')]
raw={a:tr(W[a])for a in W};ctx={a:tr(W[a]+M)for a in W};orig=ns['J'];assert J['all128_independently_retained_first_D_C_F_pair_roles']==orig['all128_coupled_F46_F47_source_current_first_loss_rows'];pc=ns['pc'];assert dict(pc)=={'sector':64,'other_held_F_tag_CORE_or_first_WHITE':34,'earlier_actual_F_or_ordinary_source_contact':21,'touches_independent_source_CURRENT_identity_before_target':3,'N0_unreachable_or_N4_exit_y_minus1_cannot_reach_lower_N4_or_W5_target':6}
pose=lambda p,h:[*xy(p),h];target=4j;th=2;hooks={'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}};qb=[]
assert raw['U']['p']==4j and raw['U']['h']==0
for a,hook in hooks.items():
 ep=4j+raw[a]['p'];eh=raw[a]['h'];cuts=[]
 for tag in hook:
  physical=ep+rot(eh)*tag;loc=(physical-target)/rot(th);f=first(ctx['V'],loc)
  if f and f[0]=='R':cuts.append(dict(physical=xy(physical),post_FORE_EXIT_local=xy(tag),target_local=xy(loc),first=list(f)));assert f[1]<len(W['V'])
 assert {tuple(z['physical'])for z in cuts}=={(-1,3),(-2,3)}and sorted(z['first'][1]for z in cuts)==[6,7]
 au=next(v for v in J['all2_actual_U_Q_B_adjacency_hook_guards']if v['actual_adjacent_words']=='U'+a);assert au['actual_FOREIGN_RAW_EXIT']==pose(ep,eh)
 assert {(tuple(z['physical']),tuple(z['post_FORE_EXIT_local']),tuple(z['target_local']),tuple(z['first']))for z in cuts}=={(tuple(z['SAME_CURRENT_hook']),tuple(z['post_FOREIGN_EXIT_N_chart']),tuple(z['target_local']),tuple(z['actual_FIRST_WHITE']))for z in au['guarded_same_hook_FIRST_WHITE']};qb.append(dict(word='U'+a,EXIT=pose(ep,eh),actual_own_RAW_conflicts=cuts))
ep=4j+raw['F']['p'];eh=raw['F']['h'];ft=(target-ep)/rot(eh);fh=(th-eh)%4;assert pose(ep,eh)==[-4,2,2]and pose(ft,fh)==[-4,-2,0]==J['actual_post_F_EXIT_N_chart_actor']
fchecks=[]
for tag in[-3-1j,-2-1j]:
 original=raw['F']['p']+rot(raw['F']['h'])*tag;birth=raw['F']['last'][original];assert birth[0]=='R'and birth[1]in[46,47]and tag not in K;loc=tag-ft;f=first(ctx['V'],loc);assert f in[('R',6),('R',7)];fchecks.append(dict(postF_tag=xy(tag),actual_F_R_birth=birth[1],target_local=xy(loc),actual_first=list(f)))
# Enumerate every sector-correct first-loss slot with the specific residual
# endpoint, including actual marker capture into the loss RAW exit core.
ports=[]
for a in'DVU':
 for slot in I[a]:
  for tag in[-3-1j,-2-1j]:
   p=tag-slot
   if int(p.real+p.imag)%2:continue
   zz=tr(W[a],p,0)
   if zz['p']==-1-1j:
    assert zz['h']==0 and tag==-2-1j and slot not in raw[a]['req']and first(ctx[a],slot)==('L',len(W[a])+1)
    assert(tag-zz['p'])in K and tag not in{q for q,h,c in zz['reads']};assert zz['p'].imag>ft.imag
    ports.append(dict(actor=a,ENTRY=pose(p,0),input=xy(slot),RAW_EXIT=pose(zz['p'],zz['h']),physical_first_L=first(ctx[a],slot),alive_CORE_at_EXIT=True))
assert len(ports)==3 and {(z['actor'],tuple(z['ENTRY']))for z in ports}=={('D',(-2,-2,0)),('V',(-2,-4,0)),('U',(-1,-5,0))}
assert {(z['actor'],tuple(z['ENTRY']),tuple(z['RAW_EXIT']))for z in ports}=={(z['actor'],tuple(z['ENTRY']),tuple(z['RAW_EXIT']))for z in J['all3_N4_pair_loss_actors_per_actual_first_D_or_C']}
for a in'DVU':assert raw[a]['p'].imag>0 and raw[a]['p'].real>=0
assert ft.real<=1 and ft.imag<=-2
# Real first postF U misses both tags; its NEW same-star is the input to the
# separate first-U pair argument, not the old preF U star.
assert {-3-1j,-2-1j}.isdisjoint(ctx['U']['req'])and {-3-1j,-2-1j}.isdisjoint({raw['U']['p']+rot(raw['U']['h'])*k for k in K})
base=S.parent/'check_old_U_all_tail_S_V_independent.json';assert sha(base)=='960e5da95b6048c6c0e091249b0041369bc9547c8335f29746c4d3e0bd0b3076'
O=dict(status='PASS missing immediate U-to-FIRST-FOREIGN adjacency; together with conditional960e5da9 proves only the old-U all-tail S4 V target guard',manifest=sha(MF),script=sha(S),conditional_original_report=sha(base),original_0aad_remains_incomplete_alone=True,dependencies=J['dependencies'],Q_B_actual_conflicts=qb,F_target=pose(ft,fh),F_actual_conflicts=fchecks,all128_pair_counts=dict(pc),all3_residual_marker_capture_ports=ports,analytic_review=[
'The omitted adjacency is real and is now treated separately: actual plainU ends0,4N and can be followed immediately byFIRSTF/Q/B. No ordinary successorV is assumed in this branch. The original0aad proof remains unchanged and incomplete in isolation; its separately checked conditional remainder is composed only after these three adjacency cases are excluded.',
'For UQ/UB, the exact SAME four-hook reserve stops at the first contact with that actual foreign proxy. GLOBAL-first stopping at the candidate oldU actor entails no earlier foreign contact and retains the hooks at ENTRY, regardless of which old piece owns the later contact. Two genuine hook identities at oldU coordinates(-1,3),(-2,3) conflict with targetV ownR6/R7. No contact-body persistence or new output identity is used.',
'For UF the actual RAW exit is(-4,2,S), making the stopped target(-4,-2,N) in the actual postF chart. SAME F46/F47 are genuine external outputs(-3,-1),(-2,-1), again at target ownR6/R7. All four possible first ordinary letters D/C/V/U are explicitly covered, rather than an assumed containingfullpacket.',
'FirstV invokes signed source-owner-independent15e: every earlier simple cut has its real immediate next ordinary RAW plus actualM, so nonterminal25a supplies its own r/A. This reserve has no eventual-old-owner, target-coordinate or fixed-index premise. FirstU invokes the independently reconstructed64-role a08 table with the NEW sourceU SAMELEFT; the stronger signed RAW-star theorem supplies it throughout this ordinary-only suffix, without transporting oldU identities acrossF.',
'FirstD common2,0 is independently current throughclock3 by the actual sourceD/DC-to-hypothetical-earlierBASE G8 factor, with real incomingF and real nextM. Source/next-atom intersections remove E3 losses; all N4 loss exits x>=2 cannot reach targetx=-4 by N motion. FirstC O3 is independently current because its N4 loss exits y>=2 cannot reach targety=-2. Both source-normal proofs are reader/owner independent under these coordinate and GLOBAL-simple-prefix conditions; neither requires a properF contact target.',
'The independently rebuilt128 coupled F-pair roles use those actual independent source anchors. After sector, held-pair and strictly earlier F/source-contact cuts, only D(-2,-2,N),V(-2,-4,N),U(-1,-5,N) remain, once per source. Each exits(-1,-1,N); no remaining zero-C N motion can reach lower y=-2. Their SAME F47 is physically alive in exitCORE and only dies at the actual next read2, which is retained rather than mislabelled an earlier physical death.',
'Only the mandatory45abc strict-lower N4 pair scope is used. The original143d universal-pair assertion remains rejected, including all genuine prepared y=-1 activeCORE controls. No targetC or terminalDCC is parsed in this argument; hypothetical earlier BASE consumers alone supply the G8 maturity premise.',
'With adjacency excluded, the conditional ordinary-successor funnel and all235FOREIGN/108physicalCORE-origin interfaces in960e5da9 now cover every allowed source continuation. The resulting conclusion excludes only V(0,4,S) at totalC4 for the selected oldU under oneFIRSTFOREIGN/GLOBAL-first stopping. D(0,2,S), arbitrary-tail simplicity, secondFOREIGN and universal attraction remain outside.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
