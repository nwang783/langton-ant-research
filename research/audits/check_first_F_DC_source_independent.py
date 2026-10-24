from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_post_F_DC_source_closure_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='8b58ee7afefa87a471e153ed80a6c16bfd90fcb50dce565318fdd07c6515ea0a';mf=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in mf[k].items():assert sha(b/f)==h
J=json.loads((D/'F_DC_closure.json').read_text())
ns={'__file__':str(S.with_name('check_first_Q_B_DC_source_independent.py'))};exec(Path(ns['__file__']).read_text().split('oldD=R/')[0],ns)
W,M,K,tr,rot,xy,center,meet,pieces,raw,ctx,I,first,bad,bindbad,geos=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces','raw','ctx','I','first','bad','bindbad','geos')]
# Independently rerun the retained exact retirement generator through its two
# source-D main tables. Its preceding-beta1104 rows are NOT lifted as premises.
n2={'__file__':str(S.with_name('check_five_C_endpoint_boundary_independent.py'))};exec(Path(n2['__file__']).read_text().split('# Reconstruct the full-source')[0],n2)
assert n2['helper_rows']==552
old5=json.loads((R/'core_periodicity_new/five_C_endpoint_boundary_frozen_20261023_1557/02_five_C_endpoint_boundary.json').read_text());tabs=old5['last_clock_helper_main_retirement_tables'];assert len(tabs)==2
for r,t in zip(J['all552_reader_specific_sourceD_main_guard_lift'],tabs):
 assert r['all276_reader_specific_main_first_retirement_rows']==t['rows'];a=t['helper_atom'];p=complex(*t['helper_pose'][:2]);h=t['helper_pose'][2];assert a==r['actual_late_helper']and r['pose']==t['helper_pose']and ctx[a]['req'][(2-p)/rot(h)]is False
 residues=[q for q in t['rows']if q['reason']=='FRESH_V_EXIT_BUD_STILL_CURRENT_WHITE_OR_TOO_YOUNG_AT_HELPER'];assert len(residues)==4 and all(q['full_source']in(0,1)and q['consumer']in(4,5)and q['consumer_pose']==[0,1,1]and q['atomic_entry_C_gap']==3 for q in residues)
beta=1-1j;common=2+0j;O={2+0j,2+1j,1+2j};FT={-3-1j,-2-1j};fraw=tr(W['F']);Fpieces=[((a-2*fraw['p'])/rot(fraw['h']),(b-2*fraw['p'])/rot(fraw['h']))for a,b in pieces('F')];assert Fpieces==[(-7-3j,-1-1j)]
for r in J['genuine_FOREIGN_R_births']:
 tag=complex(*r['post_F_EXIT_tag']);cell=fraw['p']+rot(fraw['h'])*tag;assert tag in FT|{beta}and r['actual_F_cell']==xy(cell)and fraw['last'][cell]==('R',r['R_tick0'])and r['R_read_number1']==r['R_tick0']+1 and r['genuine_external_output']
assert {r['R_tick0']for r in J['genuine_FOREIGN_R_births']}=={46,47,54}
for src in'DC':assert beta not in ctx[src]['req']and(beta-raw[src]['p'])/rot(raw[src]['h'])not in K
commonrows={}
for a in'DVU':
 for slot in I[a]:
  p=common-rot(1)*slot;z=tr(W[a],p,1);assert z['p'].real>=2;commonrows[(a,tuple(xy(slot)))]=(p,z)
assert len(commonrows)==8
for r in J['all8_E3_common_input_RAW_endpoints']:
 p,z=commonrows[(r['atom'],tuple(r['input']))];assert r['pose']==xy(p)+[1]and r['RAW_EXIT']==xy(z['p'])+[1]
# Exact complete first-CURRENT-loss domain includes true marker input slots.
targets={'D':[(3,-1+0j,1),(4,-1-1j,0),(5,-1j,3)],'C':[(3,-1+0j,1),(3,-3+0j,1),(3,-4-1j,1),(3,-2-1j,1),(4,-1-1j,0),(5,-1j,3)]}
refs={(r['source'],r['target_C_clock'],tuple(r['target_pose']),r['consumer_ENTRY_C_clock'],r['consumer'],tuple(r['input'])):r for r in J['all336_beta_first_loss_target_source_interfaces']};seen=set();counts=Counter()
for src,ts in targets.items():
 for deadline,target,th in ts:
  for k in range(deadline+1):
   h=(-k)%4
   for a in'DVU':
    for slot in I[a]:
     key=(src,deadline,tuple(xy(target)+[th]),k,a,tuple(xy(slot)));seen.add(key);r=refs[key];p=beta-rot(h)*slot;z=tr(W[a],p,h);ep=z['p'];assert r['pose']==xy(p)+[h]and r['RAW_EXIT']==xy(ep)+[z['h']]and r['actual_input']==list(first(ctx[a],slot))and r['owner']['context_tick0']==first(ctx[a],slot)[1]
     sourcehit=meet(center(0j,0),center(raw[src]['p'],raw[src]['h']),center(p,h),center(ep,z['h']))
     if int(p.real+p.imag+h)%2:why='sector'
     elif src=='C'and k==0:why='before_selected_C_RAW_completes_at1'
     elif k in(0,1):assert p.imag<1;why='initial_N0_head_below_actual_sourceD_EXIT_y1'if k==0 else'initial_W1_head_below_sourceC_y1_or_sourceD_y2'
     elif k==2:
      if sourcehit is not None:why='earlier_actual_source_EXIT_vertex_repeat'
      else:assert(a,p)==('U',1+1j)and(common-p)/rot(h)in I[a];why='young_D_common_atomic_min3_inside_actual_G8'if src=='D'else'sourceC_genuine_O3_reserve_CURRENT_through_target'
     elif k==3:
      if sourcehit is not None:why='earlier_actual_source_contact_or_repeated_entry'
      elif deadline==3:assert ep.real>=1>target.real;why='same_E3_remaining_zeroC_cannot_move_left_to_target'
      elif deadline==4:assert ep.real>=1;why='one_E_to_N_C_adds_x1_then_N_cannot_move_left_to_target_x_minus1'
      elif p==-1-2j:assert a=='U'and p+rot(h)*1j==-2j and(-2j-target)/rot(th)in K;why='new_U_permanent_RAW_star_inside_final_C5_ENTRY_CORE'
      else:assert(a,p)in{('V',-2-1j),('U',-3-2j)}and center(ep,z['h'])==center(target,th);why='earlier_consumer_RAW_EXIT_is_the_final_C5_ENTRY_vertex'
     elif k==4:
      if deadline==4:assert ep.real>=1>target.real;why='N4_RAW_exit_x_ge1_cannot_move_left_to_target'
      else:assert ep.imag>=-1;why='one_N_to_W_C_raises_y_to_ge0_then_W_cannot_lower_to_minus1'
     else:
      assert k==deadline==5
      if ep.imag>target.imag:why='same_W5_RAW_exit_y_above_target'
      elif ep.real<target.real:why='same_W5_RAW_exit_x_left_of_target_and_W_cannot_move_right'
      else:
       assert ep==target and(a,p)in{('V',3-2j),('U',4-1j)}and ctx[a]['req'][(common-p)/rot(h)]is False;why='sourceD_reader_independent_552_main_guard_in_actual_G8'if src=='D'else'sourceC_genuine_O3_CURRENT_reserve_at_final_W5_y_minus1'
     assert why==r['route'];counts[why]+=1
assert seen==set(refs)and len(seen)==336
refs={(r['source'],tuple(r['SAME_F_tag']),r['consumer'],tuple(r['input']),tuple(r['pose'])):r for r in J['all128_coupled_F46_F47_first_loss_roles']};seen=set();paircount=Counter()
for src,anchors in [('D',{common,beta}),('C',O|{beta})]:
 for tag in FT:
  for a in'DVU':
   for slot in I[a]:
    for h in range(4):
     p=tag-rot(h)*slot;key=(src,tuple(xy(tag)),a,tuple(xy(slot)),tuple(xy(p)+[h]));seen.add(key);r=refs[key];z=tr(W[a],p,h);assert r['RAW_EXIT']==xy(z['p'])+[z['h']]and r['owner']['context_tick0']==first(ctx[a],slot)[1]
     touch={q for q in anchors if(q-p)/rot(h)in ctx[a]['req']}
     if int(p.real+p.imag+h)%2:why='sector'
     elif touch:
      rr=r['independently_CURRENT_to_target_anchor_touches'];assert touch=={complex(*t['anchor'])for t in rr}
      for t in rr:loc=(complex(*t['anchor'])-p)/rot(h);assert t['local']==xy(loc)and t['actual_first']==list(first(ctx[a],loc))and t['owner']['context_tick0']==first(ctx[a],loc)[1]
      why='would_lose_or_violate_independent_CURRENT_anchor_before_target'
     elif bad(a,p,h,FT):why='other_SAME_held_F_tag_ENTRY_CORE_or_first_WHITE';bindbad(r['held_F_conflicts'],bad(a,p,h,FT),a)
     else:
      ch=(center(p,h),center(z['p'],z['h']));assert any(meet(*q,*ch)is not None for q in Fpieces+[(center(0j,0),center(raw[src]['p'],raw[src]['h']))]);why='earlier_actual_FOREIGN_or_source_proxy_contact'
     assert r['route']==why;paircount[why]+=1
assert seen==set(refs)and len(seen)==128 and sorted(paircount.values())==[17,17,30,64]
pre={}
for a in'DCVU':
 h=2 if a=='C'else 1;p=-1-rot(h)*raw[a]['p'];assert tr(W[a],p,h)['p']==-1 and tr(W[a],p,h)['h']==1;loc=(-2-1j-p)/rot(h);f=first(ctx[a],loc);assert f[0]=='R'and f[1]<len(W[a]);pre[a]=(p,h,loc,f)
for r in J['all4_actual_previous_RAW_F47_WHITE_obligations']:
 p,h,loc,f=pre[r['actual_previous_RAW']];assert r['pose']==xy(p)+[h]and r['local']==xy(loc)and r['actual_first']==list(f)and r['owner']['context_tick0']==f[1]
canon=json.loads((R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases'];cm={(r['earlier_atom'],r['entry_C_gap'],r['later_atom'],*r['later_pose']):r for r in canon}
refs={(r['source'],r['K'],r['actor'],*r['pose']):r for r in J['all40_F_sourceD_C_contact_closures']};seen=set();cl=Counter()
for src,rs in geos.items():
 for k,a,x,y,h,ss,tt in rs:
  key=(src,k,a,x,y,h);seen.add(key);r=refs[key];p=complex(x,y)
  if src=='D'and a in'DVU'and not cm[key]['surviving_allowed_first_full_packet_ids']:why='actual_BASE_cut_G8_and_signed129';assert r['signed129']==cm[key]
  elif src=='C'and bad(a,p,h,O):why='fresh_C_O3_CURRENT_CORE_or_WHITE';bindbad(r['guards'],bad(a,p,h,O),a)
  elif src=='C'and k==2:assert a=='U'and p in{-1+1j,-1+3j};why='fresh_C_L3_hole_WHITE_at_higher_S2_U'
  elif k in(4,5):assert a in'DC'and p==(-1-1j if k==4 else-1j);why='genuine_FOREIGN_beta_CURRENT_until_terminal_C4_or_C5_ENTRY';bindbad(r['guards'],bad(a,p,h,{beta}),a)
  elif p==-1:assert k==3;why='coupled_F46_F47_CURRENT_and_all4_actual_previous_RAW_require_F47_WHITE';assert r['actual_previous_RAWs']==J['all4_actual_previous_RAW_F47_WHITE_obligations']
  else:assert src=='C'and k==3;why='coupled_F46_F47_CURRENT_direct_CORE_or_WHITE';bindbad(r['guards'],bad(a,p,h,FT),a)
  assert why==r['route'];cl[why]+=1
assert seen==set(refs)and len(seen)==40 and sorted(cl.values())==[2,3,4,5,10,16]
for row in J['all6_prescribed_boundary_lift_failures']:assert tr(''.join(W[a]for a in row['prescribed_word'])+M)['bad']
out=dict(status='PASS first post-F D/C outgoing-source GLOBAL first-contact closure',manifest=sha(MF),script=sha(S),beta_roles=336,beta_counts=dict(counts),main_lift_rows=552,F_pair_roles=128,F_pair_counts=dict(paircount),source_closures=dict(cl),analytic_review=[
'Foreign beta is actual F R54, external and missed by D/C plus actual M and exitCORE. No counted producer-age law is assigned to it. All336 firstCURRENT-loss source/target/clock slots are rebuilt from true external firstL slots, including marker-owned CORE absorption. C has no external input/silent CORE capture.',
'Source-D main minimum3 is used on the actual sourceD-to-earlier BASE consumer factor, whose real next word suppliesM11, not by pretending a terminalC target parsesG8. After age3 every E input RAW exits x>=2, so it cannot reach a negative-x E target. This supplies independent common currentness also for the terminalC F-pair argument. The sourceC three-output reserve is separately signed and reader-conditioned.',
'For late W5 V/U helpers only the sourceD-to-helperBASE factor is parsedG8. The firstD has genuine precedingF, sourceD/DC is actual, and its followingC supplies actualM11. The retained exact552 SOURCE-D main rows are freshly regenerated; no preceding-G8 incoming-beta1104 argument is imported. Four residues are genuine V/VC common clearers atE3, whose fresh EXIT bud remains current/too young athelper5 within this actual factor. TerminalDCC remains allowed, no fictitious future packet is supplied.',
'Beta E3 U at-1,-2 creates actual newU star0,-2. Newly signed all-RAW four-star persistence excludes finalC5 CORE without any preforeign-U age. Other E3 clearers repeat finalC5 entry; N4/W5 endpoint cones retain arbitrary zeroC run lengths. Genuine common guards independently close S2 and lateW5 alternatives.',
'The128 coupled F roles retain TRUE simultaneous tag inputs. Independent source anchors are known CURRENT all the way to eventualtarget, so an earlier true anchor input is excluded by that theorem, not by calling it an entry-color conflict. Remaining17 actual F/source contacts are before target and nonadjacent. Four exact previousRAWs of-1,0E require F47 firstWHITE inside their own RAW; physical reads precede the candidate.',
'All40 outgoing source geometries are regenerated from actual closed affine segments and signed turn windows. OnlyBASE actors useG8; targetC and terminalDCC are handled by beta/F reserves. Scope remains actual U-entryG8, FIRSTF, immediateD/C source, ordinary suffix, actual finalM and GLOBALfirst stopping. No originalF-piece closure under D/C, later-owner closure, through-contact persistence, arbitrary-tail simplicity or capture.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
