from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'Q_B_hook_MISS_first_contact_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='e3294b325563a406d474fea145799ced6f254a47a10a0a2e873e83afea12fcf5'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'five_MISS.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet,pieces=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces')]
hooks={'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}};hole=-2j;BG=-1-2j;I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
fore={}
for A in'QB':
 z=tr(W[A]);fore[A]=[((u-2*z['p'])/rot(z['h']),(v-2*z['p'])/rot(z['h']))for u,v in pieces(A)]
def chord(a,p,h):z=tr(W[a],p,h);return center(p,h),center(z['p'],z['h'])
def first(a,q):return next((t,c)for t,(p,h,c)in enumerate(tr(W[a]+M)['reads'])if p==q)
def owner(o,a,t,c):
 assert o['context_tick0']==t and o['context_read_number1']==t+1 and o['turn']==c
 if t<len(W[a]):assert o['owner_tick0']==t
 else:assert o['owner']=='next actual word RAW'and o['owner_tick0']==t-len(W[a])and o['owner_read_number1']==t-len(W[a])+1
old=json.loads((R/'Q_B_foreign_first_contact_hook_split_2026-10-24/hook_split.json').read_text());assert J['all5_exact_owner_aware_targets']==old['all5_genuine_FOREIGN_owned_W5_hook_MISS_tail_gates'];targetkeys=set()
for t in J['all5_exact_owner_aware_targets']:
 A=t['foreign'];a=t['atom'];p=complex(*t['head']);h=t['h'];assert t['actual_outgoing_owner']==A+'tail'and t['heading_compatible_C_counts']==[5];targetkeys.add((A,a,p,h));ctx=tr(W[a]+M);assert all((q-p)/rot(h)not in ctx['req']and(q-p)/rot(h)not in K for q in hooks[A])
assert targetkeys=={('Q','V',-1j,3),('B','V',-1j,3),('B','V',1-2j,3),('B','U',-1j,3),('B','U',2-1j,3)}
counts={};kept={}
for A in'QB':
 z=tr(W[A]);q=z['p']+rot(z['h'])*hole;assert z['last'][q]==('L',56 if A=='Q'else 66)and hole not in K
 rows=J['all208_'+A+'_CORE_inclusive_last_R_origins'];bykey={(r['producer'],r['true_producer_ENTRY_C_clock'],tuple(r['actual_final_R_local'])):r for r in rows};seen=set();cc=Counter();rem=[]
 for a in'DCVU':
  raw=tr(W[a]);ctx=tr(W[a]+M)
  for clock in range(6):
   if a=='C'and clock==5:continue
   h=(-clock)%4
   for slot,(c,t)in raw['last'].items():
    if c!='R':continue
    key=(a,clock,tuple(xy(slot)));seen.add(key);r=bykey[key];p=hole-rot(h)*slot;exit=tr(W[a],p,h);assert r['pose']==xy(p)+[h]and r['R_tick0']==t and r['RAW_EXIT']==xy(exit['p'])+[exit['h']]and r['true_producer_RAW_EXIT_C_clock']==clock+(a=='C')
    touch={q for q in hooks[A]if(q-p)/rot(h)in K or(q-p)/rot(h)in ctx['req']};hits=[meet(*f,*chord(a,p,h))for f in fore[A]]
    if(int(p.real+p.imag)+h)%2:cl='sector'
    elif clock==0 and p.imag<0:cl='initial_N0_head_below0'
    elif clock==1 and p.imag<1:cl='initial_W1_head_below1'
    elif touch:
     cl='would_touch_CURRENT_original_hook_before_target';assert sorted(map(xy,touch))==sorted(z['SAME_hook']for z in r['hook_touches'])
     for z in r['hook_touches']:
      loc=(complex(*z['SAME_hook'])-p)/rot(h);tt,ch=first(a,loc);assert z['local']==xy(loc)and z['actual_first']==[ch,tt];owner(z['owner'],a,tt,ch)
    elif any(v is not None for v in hits):
     cl='earlier_actual_FOREIGN_proxy_contact'
     for hh,rr in zip(hits,r['contacts']):
      if hh is None:assert rr is None
      else:assert str(hh[0])==rr['old_s']and str(hh[1])==rr['new_t']
     if A=='Q':assert clock==3 and p==-1j and h==1 and hits[-1]==(1,0)
     else:assert hits[-1][1]>0
    else:cl='last_R_endpoint_obligation';rem.append(r)
    assert cl==r['classification'];cc[cl]+=1
 assert seen==set(bykey)and len(seen)==208;counts[A]=dict(cc);kept[A]=rem
assert len(kept['Q'])==5 and len(kept['B'])==10
# Explicit Q target lift: same entry and actual first11, but real C predecessor retained.
assert W['V'][:11]==W['U'][:11]==M;assert tr(W['C']+W['V']+M)['bad']is None and tr(W['C']+W['U']+M)['bad']is not None
qold=json.loads((R/'foreign_Q_W5_deleted_core_guard_2026-10-24/Q_W5_deleted_core_guard.json').read_text());pre={}
for a in'DCVU':
 raw=tr(W[a]);h=(3-raw['h'])%4;p=-1j-rot(h)*raw['p'];r=next(z for z in J['Q_V_same_entry_three_predecessor_scope_lifts']if z['actual_previous_RAW']==a);assert r['pose']==xy(p)+[h];pre[a]=(p,h)
 if a!='C':
  rr=next(z for z in qold['all3_actual_immediate_previous_RAW_BLACK_hole_obligations']if z['actual_previous_RAW']==a);assert r['pose']==rr['actual_previous_head'];loc=(hole-p)/rot(h);assert loc not in K and loc not in tr(W[a])['last']and first(a,loc)==(len(W[a])+1,'L');owner(r['physical_hole_read'],a,len(W[a])+1,'L')
 else:assert(p,h)==(-2j,0)and center(p,h)==fore['Q'][0][1]==-1-5j and hole-p in K
# Every old nine donor-reader fact precedes target ENTRY and is unchanged by V/U shared M.
assert len(qold['all9_S2_donor_by_actual_predecessor_cases'])==9
for row in J['Q_V_all5_funding_origins_for_extra_C_reader']:
 r=row['origin'];assert r in kept['Q'];a=r['producer'];c=r['true_producer_ENTRY_C_clock'];p=complex(*r['pose'][:2]);h=r['pose'][2];e=complex(*r['RAW_EXIT'][:2])
 if c==4:assert a in'VU'and e==1-1j and r['RAW_EXIT'][2]==0 and e.real>0 and e.imag>-2
 else:
  assert c==2 and p==2-2j and h==2;rp=(-2j-p)/rot(h);rh=(-h)%4;assert rp==2 and rh==2;tag=2+0j if a=='C'else 1+0j;assert(tag-rp)/rot(rh)in K and row['guard_tag']==xy(tag)and row['true_SOURCE_ENTRY_age']==2
  assert tr(W[a])['last'][tag]==('R',8 if a=='C'else 9)
  if a=='C':assert row['true_C_SOURCE_postEXIT_age']==1
# B thirty endpoint/fresh-donor obligations independently evaluate physical positions and clocks.
for row in J['all3_B_hole_required_targets_and30_origin_cuts']:
 atom=row['target'];p=complex(*row['pose'][:2]);h=row['pose'][2];loc=(hole-p)/rot(h);t,c=first(atom,loc);assert c=='L'and(p,h)in[(-1j,3),(2-1j,3)];owner(row['hole_first_demand'],atom,t,c)
 assert len(row['all10_last_R_origin_cuts'])==10 and [r['origin']for r in row['all10_last_R_origin_cuts']]==kept['B']
 for rr in row['all10_last_R_origin_cuts']:
  r=rr['origin'];a=r['producer'];clock=r['true_producer_ENTRY_C_clock'];sp=complex(*r['pose'][:2]);sh=r['pose'][2];ep=complex(*r['RAW_EXIT'][:2]);eh=r['RAW_EXIT'][2];co=r['true_producer_RAW_EXIT_C_clock']
  if clock==2:
   assert a in'DVU'and(ep,eh)==(hole,2)and(ep,eh)!=(p,h)
   for nxt in'DCVU':assert first(nxt,0j)==(0,'L')
  elif co==4 and eh==0:assert ep.imag>=-1 and ep.imag+1>p.imag
  elif a=='C'and clock==4:assert co==5 and(ep,eh)==(-2-1j,3)and ep.real<p.real
  else:
   assert a in'VU'and clock==3 and(sp,sh)==(-1+0j,1);rel=(p-sp)/rot(sh);rh=(h-sh)%4;tag=0j;local=(tag-rel)/rot(rh);tt,ch=first(atom,local);assert ch=='R'and tt in(6,26);owner(rr['actual_first_required_WHITE'],atom,tt,ch);assert rr['source_relative_target']==xy(rel)+[rh]and 5-clock==rr['true_source_ENTRY_age']==2;assert tr(W[a])['last'][0j]==('R',4)
# B original g first CURRENT-loss is external input or marker-owned capture, not death-only.
z=tr(W['B']);physical=z['p']+rot(z['h'])*BG;assert z['last'][physical]==('R',67)and BG not in K;gg=J['all32_B_g_first_CURRENT_loss_roles'];bykey={(r['consumer'],tuple(r['slot']),r['pose'][2]):r for r in gg};gc=Counter();survive=[]
for a in'DCVU':
 ctx=tr(W[a]+M)
 for slot in I[a]:
  for h in range(4):
   p=BG-rot(h)*slot;r=bykey[a,tuple(xy(slot)),h];assert r['pose']==xy(p)+[h]
   if(int(p.real+p.imag)+h)%2:cl='sector'
   elif any((q-p)/rot(h)in K or(q-p)/rot(h)in ctx['req']for q in hooks['B']):cl='would_retire_or_contradict_held_hook_before_target'
   elif any(meet(*f,*chord(a,p,h))is not None for f in fore['B']):cl='earlier_actual_B_proxy_contact'
   else:cl='S2_marker_g_loss_funder';survive.append((a,p,h))
   assert r['classification']==cl;gc[cl]+=1
assert len(bykey)==32 and set(survive)=={('V',-1+1j,2),('U',-2+2j,2)}
assert first('V',(BG-(1-2j))/rot(3))==(12,'R')
for r in J['both_B_g_loss_creates_fresh_shadow_cuts']:
 old=r['g_loss_consumer'];a=old['consumer'];p=complex(*old['pose'][:2]);h=old['pose'][2];tag=1+0j if a=='V'else 1j;sp=p+rot(h)*tag;assert sp==-2+1j and tr(W[a])['last'][tag]==('R',9 if a=='V'else 19);ex=tr(W[a],p,h);assert(ex['p'],ex['h'])==(-2-2j,2)
 assert (BG-ex['p'])/rot(ex['h'])in K and first(a,(BG-p)/rot(h))==(len(W[a])+1,'L')
 local=(sp-(1-2j))/rot(3);assert first('V',local)==(26,'R');owner(r['actual_target_first_WHITE'],'V',26,'R');assert r['true_fresh_source_ENTRY_age']==3 and r['true_postFOREIGN_ENTRY_clock']==2
assert len(J['all5_disjoint_case_routes'])==5 and{json.dumps(r['original_owner_aware_case'],sort_keys=True)for r in J['all5_disjoint_case_routes']}=={json.dumps(r,sort_keys=True)for r in J['all5_exact_owner_aware_targets']}
out=dict(status='PASS all five proper Q/B tail hook-MISS GLOBAL-first-contact targets only',manifest=sha(MF),script=sha(S),origin_counts=counts,B_g_loss_counts=dict(gc),Q_reader_types=4,B_hole_targets=3,B_hole_origin_cuts=30,B_new_shadow_donors=2,analytic_review=['Exact signed owner-aware five-target set is preserved; candidate COMPLETE RAW+actualM misses all hook IDs, including CORE. FOREEXIT is outgoingb1 and not included. GLOBAL-first choice supplies an executed SIMPLE source-relative ordinary prefix, not merely no earlier FOREIGN contact.','A deleted physical hole needed BLACK at target ENTRY has a LAST earlier R in a completed RAW, necessarily at a final-R coordinate. All208 roles per foreign include CORE writes and actual Ccompletion deadline. Earlier hook TRUE inputs are excluded by SAME CURRENT identity loss before candidate ENTRY, even when physical death is a marker read. The four Q geometric origins are laterclock3 nonadjacent FOREIGN EXIT repeats; the four B origins have positive-time proper or terminal contacts. None is legitimate initial adjacency.','For Q V0,-1W, the three nonC immediate predecessor poses, unread BLACK input and actual followingM11 are identical to signed Q U. Every funding clause precedes target ENTRY, so it lifts; the old CU contradiction does NOT. Real prior C0,-2N is explicitly retained and repeats genuine Q F56 kink at ENTRYclock4. This is a proxy vertex, not a marked core. Independent fresh-C/V/U C-reader guards use true sourceENTRYage2 and CpostEXITage1.','For B h-targets, three CORE-head R births die at actual nextL0 before any W5 target. N4 completed exits havey>=-1 and the remaining C raisesy; C4 finishesW5atx-2 and cannot move right. Actual E3 V/U fresh donors have SAME r CURRENT through trueage2 and the candidate firstR conflicts. No old-eight age is carried through the foreign.','For B V1,-2W, actual oldg R67 can really leave CURRENT via the two S2 V/U gates, remainaliveCORE, then die nextread2. Each genuine donor writes a DIFFERENT shadow at-2,1, VrightR9 or ULEFTwR19. It remains CURRENT through donorage3 and conflicts with candidate contextR26, actually nextwordtick8/read9. Actual terminalM is essential. No oldg permanence, cleanupA assumption or replacement-identity conflation occurs.','All five targets close for arbitrary ordinary suffix lengths under the stated U-entry/FIRSTQ/B/globalfirst assumptions. The proof does not establish arbitrary-tail simplicity, F/ordinary source closure, another foreign or no later contact after earlier selfcontact.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
