from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'old_U_all_tail_S_V_foreign_effect_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='0aad196bcda89e6bede118b32d36d21f587cda6584bd5e24d31be8d5e885c0f9';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
J=json.loads((D/'S_V.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
N={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(N['__file__']).read_text().split('# Universal')[0],N);W,M,K,tr,rot,center,xy=[N[k]for k in('W','M','K','tr','rot','center','xy')];G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};I={a:{q for q,b in C[a]['req'].items()if b and q not in K}for a in W};pose=lambda p,h:[*xy(p),h];ff=lambda a,q:next(([c,i]for i,(v,h,c)in enumerate(C[a]['reads'])if v==q),None);sort=lambda z:sorted(z,key=lambda q:(q.real,q.imag));star={0j,1j,1+0j,1+1j};bud=1+3j;arm=1+2j;r=4j;q=-1+2j;hole=-1+4j;target=4j
assert center(target,2)==1+9j
for a in'CD':assert center(4j+G[a]['p'],G[a]['h'])==center(target,2)
assert all((g-target)/rot(2)in K for g in[4j,5j]);assert G['V']['last'][0j]==('R',4)
for word in['V','VC','VCC']:
 z=tr(''.join(W[a]for a in word),4j,0);assert z['last'][r]==('R',4)and(r-z['p'])/rot(z['h'])not in K
# All235 FOREIGN true-input roles. Complete CURRENT contact includes CORE.
fr=[];fg=[];counts=Counter()
for n in range(5):
 h=(-n)%4
 for atom in'FQB':
  for slot in sort(I[atom]):
   p=r-rot(h)*slot;au=next(z for z in J['all235_actual_FOREIGN_first_V_r_TRUE_input_roles']if z['FOREIGN']==atom and z['ENTRY']==pose(p,h)and z['true_old_U_and_first_V_ENTRY_to_FOREIGN_ENTRY_C_clock']==n);assert au['old_first_V_r_TRUE_input']==xy(slot)and au['actual_owner']['context_tick0']==ff(atom,slot)[1]
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif any((g-p)/rot(h)in C[atom]['req']or(g-p)/rot(h)in K for g in star):why='forbidden_complete_initial_U_STAR_context_hit_at_age_le4'
   elif (bud-p)/rot(h)in K or C[atom]['req'].get((bud-p)/rot(h))is False:why='pre_FOREIGN_original_U_bud_BLACK_CORE_or_WHITE_contradiction'
   else:
    ep=p+rot(h)*G[atom]['p'];eh=(h+G[atom]['h'])%4;fg.append((n,atom,pose(p,h),pose(ep,eh)))
    if n==0:assert atom=='F'and p in[4+4j,3+5j]and p.imag<7
    if n==1:assert p in[2+9j,3+8j,-3+6j]and(p.imag<8 or p.imag-p.real<=7)
    if n==2:assert p in[-5+5j,-3+7j,-2+6j,6j]
    if n==3:assert eh==3 and ep.real<=0
    if n==4:assert atom=='F'and eh==2 and ep.imag<4
    why=au['route']
   assert why==au['route'];counts[why]+=1;fr.append((n,atom,pose(p,h),xy(slot),why))
assert len(fr)==235 and len(fg)==33 and Counter(n for n,a,p,e in fg)=={0:2,1:7,2:12,3:10,4:2};assert sum(len(I[a])for a in'FQB')==47
# Directional support justifies every unbounded rail endpoint exclusion.
for a in'DVU':
 assert G[a]['p'].imag>0 and(rot(3)*G[a]['p']).imag>=0 and(rot(2)*G[a]['p']).real<=0 and(rot(2)*G[a]['p']).imag<=0
 z=rot(3)*G[a]['p'];assert z.imag-z.real>=2
assert 4j+G['V']['p']==1+7j and tr(W['V']+W['C'],4j,0)['p']==1+8j;assert(rot(3)*G['C']['p']).real==-1
# G was truly alive in the old U marker core, then deleted by actual next V.
assert(hole-G['U']['p'])in K and hole in C['U']['req'];z=tr(W['U']+W['V']);assert z['reads'][29][0]==hole and z['reads'][29][2]=='L'and z['last'][hole]==('L',29)and z['p']==1+7j
hold=star|{arm,bud};RR={a:{p:t for p,(c,t)in G[a]['last'].items()if c=='R'}for a in'DCVU'};origins=[];keepers=[];gc=Counter()
for n in range(3):
 h=(-n)%4
 for atom in'DCVU':
  for slot,tick in RR[atom].items():
   p=hole-rot(h)*slot;ep=p+rot(h)*G[atom]['p'];eh=(h+G[atom]['h'])%4;au=next(z for z in J['all108_pre_FOREIGN_physical_CORE_inclusive_G_first_BLACK_cut_origins']if z['earlier_RAW']==atom and z['actual_clock']==n and z['ENTRY']==pose(p,h));first=next([c,i]for i,(v,hh,c)in enumerate(G[atom]['reads'])if v==slot);assert au['physical_final_R']==dict(slot=xy(slot),last_R_tick0=tick,first=first,EXIT_CORE=(slot-G[atom]['p'])/rot(G[atom]['h'])in K);assert au['RAW_EXIT']==pose(ep,eh)
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif first[0]=='L':why='firstL_requires_an_earlier_BLACK_cut_after_actual_G_deletion'
   elif any((g-p)/rot(h)in C[atom]['req']or(g-p)/rot(h)in K for g in hold):why='old8_earlier_writer_hits_independently_CURRENT_initial_STAR_arm_or_bud'
   else:
    keepers.append((n,atom,pose(p,h),pose(ep,eh)))
    if n==0:assert p.imag<7;why='N0_head_below_actual_firstV_RAW_EXIT_y7'
    elif n==1:assert p.imag<8;why='W1_head_below_actual_firstV_first_C_W_start_y8'
    elif atom=='C':assert eh==1;why='S2_C_writer_completes3_after_FOREIGN_n2'
    else:assert ep.imag<=4;why='S2_writer_RAW_EXIT_y_le4_cannot_reach_FOREIGN_y6_by_zeroS'
   assert why==au['route'];gc[why]+=1;origins.append((n,atom,pose(p,h),pose(ep,eh),why))
assert len(origins)==108 and len(keepers)==13
# All true marker inputs really capture into RAW EXIT CORE, never an
# intrinsic first-color conflict when their first requirement is L.
markers=[]
for atom in'DCVU':
 ek={G[atom]['p']+rot(G[atom]['h'])*k for k in K}
 for z in ek-K:assert z in C[atom]['req']
 for z in I[atom]:
  if z not in G[atom]['req']:assert z in ek;markers.append((atom,xy(z),ff(atom,z)))
assert not I['C']
# The four distinct n2 guards and their exact target/core interfaces.
guards=[]
for atom in'FQB':
 p=-2+6j;loc=(hole-p)/rot(2);assert loc==-1+2j and ff(atom,loc)==['L',13]
 p=-5+5j;loc=(q-p)/rot(2);assert G[atom]['last'][loc]==('L',35);ep=p+rot(2)*G[atom]['p'];assert ep.imag>=7
 for lead in['','C']:
  zz=tr(''.join(W[a]for a in lead),ep,0);assert(q-zz['p'])/rot(zz['h'])not in K
  if lead:assert q not in{v for v,h,c in zz['reads']if c=='R'}
 assert(q-target)/rot(2)==1+2j and ff('V',1+2j)==['L',13]
 p=-3+7j;tag=p+rot(2)*(-4+2j);assert tag==1+5j and G[atom]['last'][-4+2j]==('R',36);ep=p+rot(2)*G[atom]['p'];assert ep.imag>=9 and(tag-target)/rot(2)in K
 p=6j;tag=p+rot(2)*(1+2j);assert tag==hole and G[atom]['last'][1+2j]==('R',25)and(tag-target)/rot(2)in K
 guards.append(dict(FOREIGN=atom,spent_G_first_L13=True,spent_q_LAST_L35=True,new_R36=[1,5],new_R25=[-1,4]))
# Exact eight possible S CURRENT-loss endpoints for new R36.
def models(ep):
 dx=int(ep.real);dy=int(ep.imag-4);ans=[]
 if dx<0 or dy<0:return ans
 for v in range(dx+1):
  d=dx-v;rest=dy-d-3*v
  if rest>=0 and rest%4==0:ans.append((d,v,rest//4))
 return ans
srows=[]
for atom in'DVU':
 for slot in sort(I[atom]):
  assert slot.imag>=1 and slot.real>=-1
  p=1+5j+slot;ep=p-G[atom]['p'];assert not models(ep);au=next(z for z in J['all8_R36_S_CURRENT_loss_endpoint_exclusions']if z['S_loss_RAW']==atom and z['ENTRY']==pose(p,2));assert au['RAW_EXIT']==pose(ep,2)and au['true_input']==xy(slot)and au['actual_owner']['context_tick0']==ff(atom,slot)[1]and not au['all_zeroC_S_endpoint_models_to_target'];srows.append((atom,xy(slot),pose(p,2),pose(ep,2)))
assert len(srows)==8
# Generic NE3 theorem really retains this source-relative NEW R25 tag.
ne=json.loads((R/'foreign_three_C_NE_reserve_2026-10-24/three_C_NE_reserve.json').read_text());assert[1,2]in ne['transfer_dichotomy']['nine_retained_originals']
ages=json.loads((R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text());assert[4,1,2,3]in ages and[4,0,3,2]in ages
# Literal ordered residual identity covers all8 full packets, including
# temporary CORE R writes and a recycled input/output. The target q starts
# WHITE outside initial core, so no initial residual origin is available.
ledger=[]
for letters in['D','DC','V','VC','VCC','U','UC','UCC']:
 raw=tr(''.join(W[x]for x in letters));ctx=tr(''.join(W[x]for x in letters)+M);assert raw['bad']is None and ctx['bad']is None;F=set(ctx['req']);B0={q for q,b in ctx['req'].items()if b};assert K<=B0;delta={q for q in raw['last']if sum(v==q for v,h,c in raw['reads'])%2};ek={raw['p']+rot(raw['h'])*k for k in K};out=(B0^delta)-ek;assert K|ek|set(raw['last'])<=F and all(raw['last'][q][0]=='R'for q in out);ledger.append(dict(packet=letters,inputs=sorted(map(xy,B0-K)),outputs=sorted(map(xy,out))))
# Portable conditional source-r clock has exactly the stated W loss exits.
rports=[]
for atom,p in[('D',1+0j),('V',3+0j),('U',4+1j)]:
 ep=p+rot(3)*G[atom]['p'];assert ep==1j;loc=(0j-p)/rot(3);assert loc not in G[atom]['last']and(loc-G[atom]['p'])/rot(G[atom]['h'])in K;rports.append((atom,pose(p,3),pose(ep+4j,3)))
O=dict(status='FINITE INTERFACES PASS; overall all-tail S4 V scope PENDING immediate U-to-FOREIGN funnel branch',manifest=sha(mf),script=sha(S),all235_FOREIGN_roles=fr,necessary33=fg,FOREIGN_counts=dict(counts),all108_CORE_inclusive_G_origins=origins,G_counts=dict(gc),G_keepers=keepers,marker_inputs=markers,all4_n2_guards=guards,all8_new_R36_loss_endpoints=srows,actual_full_packet_residual_ledger=ledger,portable_r_loss_ports=rports,dependencies=J['dependencies'],scope_obligation='The frozen funnel enumerates ordinary D/V/U full successors but the theorem as stated appears also to allow the selected oldU immediately followed by FIRST F/Q/B. Then P=V0,4N need not exist. Author clarification or an independently checked direct guard is required before the full result is signed.',conditional_analytic_review=[
'Conditional on an actual ordinary full successor beforeFOREIGN, corrected-center repetition excludes ownC and nextD; a genuinely NEW nextU is blocked by its own signed early-star/LEFT interface. Thus the only remaining successor isV/VC/VCC at0,4N with genuine rR4, preserved through its source tails and CURRENT at every preFOREIGN age<=4 by the strictly preFOREIGN fresh-r minimumfive theorem.',
'All235 actualFOREIGN input alignments and33 necessary cases reconstruct. Complete STAR contact is excluded by its preFOREIGN foreign-MISS theorem, while bud is used as CURRENT beforeFOREIGN only. N/W endpoints, the actual non-C predecessor requirement and exact zero-C direction monotonicity close all n0/1/3/4 cases at arbitrary rail length.',
'Atn2 head(-5,5,S), actual FORE L35 deletes selectedq. Zero/one leadingC preserves qWHITE outside the first subsequentBASEcore; signed leadingCC grammar makes two leadingCs terminal. The actual firstpostFOREIGNBASE-to-targetBASE factor has genuine incomingRAW and parsesG8. Its ordered residual ledger assigns any targetq to a full output born in that factor, including CORE-originR; every producer entryclock>=2 gives targetage<=2<selectedLOWERmin3. No uppermin2 or age forFOREIGN is used.',
'The other n2 heads use respectively a NEW FORE R36(1,5) protected by N/W cones and all8 exactS endpoint equations; the G hole actually deleted by nextV L1/global29 and all108 CORE-inclusive earliestBLACKcut origins; and NEW FORE R25(-1,4), one of the exact retainedNE9 in both signedNE3 branches. No oldV cohort is presumed to surviveFOREIGN.',
'Only after complete actualFOREIGN MISS of genuine r is established may signed277 portable firstlossK3 be invoked. Every actual Wloss RAW exits oldUchart0,5W, possibly with r still physicallyaliveCORE; one remainingC lowersx and S cannotreturntargetx0. This contradicts CURRENT r in targetENTRYCORE, but nothing is asserted through a partial target.',
'All computations are conditional on the unresolved first-successor funnel scope. D0,2S, a secondFOREIGN, arbitrarytail simplicity and globalattraction are outside.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(counts,gc);print(sha(S.with_suffix('.json')))
