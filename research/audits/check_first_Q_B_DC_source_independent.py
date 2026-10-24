from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'first_post_Q_B_DC_source_closure_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='1b59508fd7e74428f092ed44e72b5d0a6ad1164e97ad5e4932820f068fa9df7f';mf=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in mf[k].items():assert sha(b/f)==h
J=json.loads((D/'Q_B_DC_closure.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet,pieces=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces')]
raw={a:tr(W[a])for a in'DCVU'};ctx={a:tr(W[a]+M)for a in'DCVU'};I={a:{q for q,v in ctx[a]['req'].items()if v and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
first=lambda z,q:next(((c,t)for t,(p,h,c)in enumerate(z['reads'])if p==q),None)
def bad(a,p,h,black=(),white=()):
 out=[]
 for q in black:
  loc=(q-p)/rot(h)
  if loc in K or ctx[a]['req'].get(loc)is False:out.append(('b',q,loc,'ENTRY_CORE'if loc in K else'first_WHITE'))
 for q in white:
  loc=(q-p)/rot(h)
  if loc in K or ctx[a]['req'].get(loc)is True:out.append(('w',q,loc,'ENTRY_CORE_requires_BLACK'if loc in K else'first_BLACK'))
 return out
def bindbad(rows,actual,a):
 ref=set()
 for r in rows:
  ch='b'if 'SAME_CURRENT_BLACK'in r else'w';tag=complex(*(r['SAME_CURRENT_BLACK']if ch=='b'else r['physical_WHITE']));loc=complex(*r['local']);ref.add((ch,tag,loc,r['role']));f=first(ctx[a],loc);assert r['actual_first']==(list(f)if f else None)
  if f:assert r['owner']['context_tick0']==f[1]and r['owner']['turn']==f[0]
 assert ref==set(actual)
# New C output reserve: no prior complete-eight producer relation.
O={2+0j,2+1j,1+2j};c=raw['C'];assert(c['p'],c['h'])==(1j,3);cK={c['p']+rot(c['h'])*q for q in K};assert {q for q,(ch,t)in c['last'].items()if ch=='R'and q not in cK}==O
for q in O:
 row=next(r for r in J['fresh_C_portable_coupled_reserve']['all3_actual_output_births']if r['tag']==xy(q));assert c['last'][q]==('R',row['last_R_tick0'])and row['last_R_read_number1']==row['last_R_tick0']+1
refs={(tuple(r['SAME_output']),r['consumer'],tuple(r['true_input_local']),tuple(r['pose'])):r for r in J['fresh_C_portable_coupled_reserve']['all96_plain_true_input_first_loss_roles']};seen=set();counts=Counter()
for q in O:
 for a in'DVU':
  for slot in I[a]:
   for h in range(4):
    p=q-rot(h)*slot;key=(tuple(xy(q)),a,tuple(xy(slot)),tuple(xy(p)+[h]));seen.add(key);r=refs[key];f=first(ctx[a],slot);assert r['actual_input']==list(f)and r['owner']['context_tick0']==f[1];z=tr(W[a],p,h);assert r['RAW_EXIT']==xy(z['p'])+[z['h']]
    if int(p.real+p.imag+h)%2:why='sector'
    else:
     cuts=bad(a,p,h,O)
     if cuts:why='held_three_CURRENT_CORE_or_WHITE';bindbad(r['held_conflicts'],cuts,a)
     elif h==2:assert p.real>=0;why='S2_head_x_positive_but_actual_heads_x_le_minus1'
     elif h==3:assert a=='U'and p in{3+2j,2+3j}and z['p'].imag>=2;why='W1_head_x_positive_but_actual_heads_x_le0_or_W5_exit_y_ge2'
     elif h==1:assert meet(center(0j,0),center(c['p'],c['h']),center(p,h),center(z['p'],z['h']))is not None;why='E3_actual_earlier_source_C_contact'
     else:assert a=='U'and p in{2-2j,3-1j}and z['p'].imag>=2;why='N4_loss_exits_y_ge2'
    assert r['route']==why;counts[why]+=1
assert seen==set(refs)and len(seen)==96 and list(sorted(counts.values()))==[3,4,5,8,28,48]
# Every ordinary CORE-only loss is an input role; C cannot absorb an old external ID.
assert {q for q,b in ctx['C']['req'].items()if b}==K
for q in cK-K:assert c['last'][q][0]=='R'and ctx['C']['req'][q]is False
for a in'DVU':
 for h in(0,1,2,3):
  z=tr(W[a],0j,h);assert z['h']==h
  if h==0:assert z['p'].imag>0
  if h==3:assert z['p'].real<0 and z['p'].imag>=0
  if h==2:assert z['p'].imag<0
assert tr(W['C'],0j,3)['p']==-1 and tr(W['C'],0j,0)['p']==1j
# Physical source-C hole and full last-R producer domain, including CORE R writes.
hole=-1j;assert c['last'][hole]==('L',3)and hole not in cK;writes=[]
for a,z in raw.items():
 for q,(ch,t)in z['last'].items():
  if ch!='R':continue
  assert q.real>=-1
  if a in'DVU':assert z['p'].imag>=q.imag
  writes.append((a,tuple(xy(q)),t))
wr=J['fresh_C_S2_physical_WHITE_hole_guard']['all36_actual_RAW_final_R_slots_CORE_included'];assert len(writes)==36 and set(writes)=={(r['atom'],tuple(r['RAW_final_R_local']),r['tick0'])for r in wr}
for r in wr:
 a=r['atom'];q=complex(*r['RAW_final_R_local']);assert r['RAW_EXIT']==xy(raw[a]['p'])+[raw[a]['h']]and r['in_actual_EXIT_CORE']==((q-raw[a]['p'])/rot(raw[a]['h'])in K)
for r in J['fresh_C_S2_physical_WHITE_hole_guard']['all2_S2_U_guards']:
 p=complex(*r['pose'][:2]);h=r['pose'][2];assert p in{-1+1j,-1+3j}and h==2;loc=(hole-p)/rot(h);assert first(ctx['U'],loc)[0]=='L'and r['actual_first']==list(first(ctx['U'],loc))and r['local']==xy(loc)
# Q's target-reader lift: same PRE-target obligations, retaining the real C predecessor.
oldQ=json.loads((R/'foreign_Q_W5_deleted_core_guard_2026-10-24/Q_W5_deleted_core_guard.json').read_text());oldpre={r['actual_previous_RAW']:r for r in oldQ['all3_actual_immediate_previous_RAW_BLACK_hole_obligations']};qr=J['Q_C5_negative_port_reader_lift'];assert qr['same5_CORE_inclusive_last_R_origins']==[r for r in oldQ['all208_last_RAW_R_origin_deadline_and_hook_FOREIGN_constraints']if r.get('why')=='NECESSARY']
qraw=tr(W['Q']);Qpieces=[((a-2*qraw['p'])/rot(qraw['h']),(b-2*qraw['p'])/rot(qraw['h']))for a,b in pieces('Q')];assert Qpieces[0][1]==Qpieces[1][0]==-1-5j
seen=set()
for r in qr['all16_target_by_actual_previous_RAW_interfaces']:
 a,prev=r['target_RAW'],r['actual_previous_RAW'];seen.add((a,prev));assert(W[a]+M)[:11]==M;h=(3-raw[prev]['h'])%4;p=-1j-rot(h)*raw[prev]['p'];assert r['previous_pose']==xy(p)+[h]
 if prev=='C':assert p==-2j and h==0 and center(p,h)==Qpieces[0][1]
 else:
  assert oldpre[prev]['actual_previous_head']==xy(p)+[h];loc=(-2j-p)/rot(h);assert loc not in raw[prev]['last']and loc not in K and first(ctx[prev],loc)==('L',len(W[prev])+1)
assert seen=={(a,b)for a in'DCVU'for b in'DCVU'}
# Rebuild exact bounded contact parallelograms from actual corrected chords.
rank={'U':0,'V':1,'D':2,'C':2};det=lambda a,b:int(a.real*b.imag-a.imag*b.real);geos={}
for src in'DC':
 u=(center(raw[src]['p'],raw[src]['h'])-center(0j,0))/2;rows=[]
 for k in range(2,7):
  h=(-k)%4
  for a in'DCVU':
   if k==2 and rank[src]<=rank[a]or k==6 and rank[src]>=rank[a]:continue
   v=(center(raw[a]['p'],raw[a]['h'])-center(0j,0))*rot(h)/2;cor=(center(0j,0)-center(0j,h))/2;corn=[cor+s*u-t*v for s in(0,1)for t in(0,1)]
   for x in range(math.ceil(min(q.real for q in corn)),math.floor(max(q.real for q in corn))+1):
    for y in range(math.ceil(min(q.imag for q in corn)),math.floor(max(q.imag for q in corn))+1):
     if(x+y+h)%2:continue
     p=complex(x,y);w=p-cor;dd=det(u,v)
     if dd:
      ss=F(det(w,v),dd);tt=F(det(w,u),dd)
      if not(0<=ss<1 and 0<tt<=1):continue
     else:
      if det(w,u):continue
      ss=F(0);tt=F(-int(w.real),int(v.real))if v.real else F(-int(w.imag),int(v.imag))
      if not(0<tt<=1 and w+float(tt)*v==0):continue
     rows.append((k,a,x,y,h,str(ss),str(tt)))
 ref=J['all40_source_D_C_geometry_rows'][src];assert set(rows)=={(r['K'],r['actor'],*r['pose'],r['old_s'],r['new_t'])for r in ref}and len(rows)==20;geos[src]=rows
oldD=R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616';om=json.loads((oldD/'manifest.json').read_text())
for f in om['files']:assert sha(oldD/f['frozen'])==f['sha256']
canon=json.loads((oldD/'02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases'];oldmap={(r['earlier_atom'],r['entry_C_gap'],r['later_atom'],*r['later_pose']):r for r in canon}
hooks={'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}};refs={(r['foreign'],r['source'],r['K'],r['actor'],*r['pose']):r for r in J['all80_foreign_typed_contact_closures']};seen=set();closures=Counter()
for src,rows in geos.items():
 for k,a,x,y,h,ss,tt in rows:
  p=complex(x,y);signed=oldmap[(src,k,a,x,y,h)];assert signed['earlier_parameter']==ss and signed['later_parameter']==tt
  for fore in'QB':
   key=(fore,src,k,a,x,y,h);seen.add(key);r=refs[key]
   if src=='D'and a in'DVU'and not signed['surviving_allowed_first_full_packet_ids']:
    why='actual_BASE_cut_G8_parse_and_signed129_exclusion';assert r['signed129']==signed
   else:
    if src=='D'and a in'DVU':assert(a,p,h,k)==('V',-1+0j,1,3)
    black=set(hooks[fore]);white=set()
    if fore=='B'and k<=5:black.add(-1-2j);white.add(-2j)
    if src=='C':assert k<=3 or k==4 and y<=1 or k==5 and y<=0;black|=O
    cuts=bad(a,p,h,black,white)
    if cuts:why='actual_CURRENT_or_physical_WHITE_entry_context';bindbad(r['guards'],cuts,a)
    elif src=='C'and k==2:assert a=='U'and p in{-1+1j,-1+3j}and h==2;why='source_C_actual_L3_hole_WHITE_at_S2_U'
    else:
     assert fore=='Q'and k==5 and a in'DC'and p==-1j and h==3;why='Q_hole_port_lift_to_same_pose_C5_reader';bindbad(r['guards'],bad(a,p,h,white={-2j}),a)
   assert r['route']==why;closures[why]+=1
assert seen==set(refs)and len(seen)==80 and sorted(closures.values())==[2,3,32,43]
for rr in J['actual_terminal_DCC_regressions']:
 z=tr(''.join(W[a]for a in rr['word'])+M);assert not z['bad']and sorted(map(xy,{q for q,v in z['req'].items()if v}))==rr['seed']
out=dict(status='PASS outgoing first post-Q/B D/C source exclusion for GLOBAL first ordinary contact',manifest=sha(MF),script=sha(S),fresh_C_roles=96,C_role_counts=dict(counts),physical_last_R_slots=36,Q_reader_interfaces=16,source_geometries={'D':20,'C':20},all80_routes=dict(closures),analytic_review=[
'Fresh C creates three actual SAME outputs and completes clock1 facingW. All96 marker-inclusive firstCURRENT-loss roles are independently regenerated:48sector/28held-three conflicts,8S2 positive-x inaccessible,3W1 positive-x inaccessible orW5 exits>=2,4E3 earlier-source contacts,5N4 exits>=2. C itself has no external input or silent CORE capture. The coupled earliest-loss argument preserves all three throughclock3 and at stipulatedN4 heady<=1/W5 heady<=0; N/W endpoint inequalities include arbitrarily long zeroC rails. TRUEinputs during the contact are not rejected.',
'Source C actually lastL3 deletes0,-1 outsideexitCORE. All36 finalRAW R slots, includingCORE writes, have localx>=-1; W1 heady>=1 preventsrepair. A completing S2C would exceed the readerclock. Any S2base writer exits at/below the hole, and remaining Srail cannot rise to either Ureader. This is endpoint-conditioned physical whiteness, not residualabsence or all-age permanence.',
'At Q clock5 target0,-1W the three nonC previousRAWs are exactly signed d3f pre-entry funding obligations and all ordinary targets share the physically executedM11. RAWmiss/markerL ownership is checked, so targetU body/CU prohibition is not imported. The real fourth predecessorC0,-2N repeats Q actualF56 kink at itsENTRY, already before target; no virtual markedCORE is assigned at the kink.',
'Exact affine first-contact geometry independently gives20D+20C rows, outgoingold_s<1 and positivetime including collinear onset; signed zero-foreign source-relative turn windows supplyK2..6 and strict endpoint alpha filters. The80 Q/B typed rows partition32actualbasecutG8/43actualfield/3Qhole/2Cdeletedhole cuts.',
'Only sourceD-to-BASE actors use RAW-to-G8 with its actual precedingQ/B and actual terminalM. Signed129 assembly has arbitrary actual complete8 entry fields; its empty rows exclude these firstcontacts, leaving only V(-1,0,E) atclock3 for directforeignguard. TargetC remains handled geometrically, not by falsely parsing terminalDCC. FreshC is never assigned a nonexistent containingfullpacket.',
'Complete real terminalUDCC/UQUDCC+M positives remain valid. Scope requires actual U-entry complete8 thenFIRSTQ/B, no laterforeign, and GLOBALfirst stopping with precedingprefixsimple. Originaloutputs stayCURRENT only atENTRY; FfirstD/C, laterordinarysource owners, unrestrictedtail simplicity and capture remain open.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
