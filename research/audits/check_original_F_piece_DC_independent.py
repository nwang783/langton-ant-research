from pathlib import Path
from fractions import Fraction
from collections import Counter
from math import floor,ceil
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'original_F_piece_firstpost_DC_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='143d03405324ce9d064042ecd0ecf3e4877b7bbf8a078d75d8c5cdd7adbbeff2';mf=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in mf[k].items():assert sha(b/f)==h
J=json.loads((D/'F_piece_DC.json').read_text());ns={'__file__':str(S.with_name('check_first_Q_B_DC_source_independent.py'))};exec(Path(ns['__file__']).read_text().split('oldD=R/')[0],ns)
W,M,K,tr,rot,xy,center,meet,pieces,raw,ctx,I,first,bad,bindbad=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces','raw','ctx','I','first','bad','bindbad')]
ch=lambda a,p,h:(center(p,h),center(p+rot(h)*raw[a]['p'],(h+raw[a]['h'])%4))
FV=(-7-3j,-1-1j);common=2+0j;CO={2+0j,2+1j,1+2j};FT={-3-1j,-2-1j};windows=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
closed={};proper={};aliases={}
for a in 'DCVU':
 for h in range(4):
  c,d=ch(a,0j,h);corners=[(u-v)/2 for u in FV for v in (c,d)]
  for x in range(floor(min(z.real for z in corners)),ceil(max(z.real for z in corners))+1):
   for y in range(floor(min(z.imag for z in corners)),ceil(max(z.imag for z in corners))+1):
    if (x+y+h)%2:continue
    p=complex(x,y);hit=meet(*FV,*ch(a,p,h))
    if hit is None:continue
    ss,tt=hit;assert ss!='OVERLAP'
    if tt<=0:continue
    key=(a,x,y,h);row=dict(actor=a,pose=[x,y,h],old_F_parameter=str(ss),new_parameter=str(tt));closed[key]=row
    if ss==1:row['route']='FOREIGN_EXIT_has_outgoing_b1_owner';aliases[key]=row
    else:
     win=next(r['allowed_C_counts_before_contact_ENTRY']for r in windows if r['source_class']=='Fprefix'and r['contact_atom']==a);ks=[k for k in win if (-k)%4==h];assert len(ks)==1;row['K']=ks[0];proper[key]=row
assert len(closed)==62 and len(proper)==42 and len(aliases)==20 and not J['all_piece_angle_impossible_rows']
for name,got in [('all62_closed_F_contact_heads',closed),('all42_genuine_proper_F_owned_angle_labels',proper),('all_foreign_EXIT_owner_aliases',aliases)]:assert { (r['actor'],*r['pose']):r for r in J[name]}==got
assert all(r['K']in (2,3,4,5) and (r['pose'][0]<=1 and r['pose'][1]<=-1 if r['K']==4 else True) and (r['pose'][1]<=-1 if r['K']==5 else True)for r in proper.values())
# Exact sourceD/DC common minimum-three residuals from literal input slots and signed COUNT5.
cp=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';counted={tuple(map(int,line.split()[:8]))for line in cp.read_text().splitlines()};refs={tuple(r['original_signed_row']['key']):r for r in J['fresh_D_common_entry_reserve']['all16_plain_E3_sourceD_DC_common_queries']};seen=set();cc=Counter()
for si,src in enumerate(['D','DC']):
 for a in 'DVU':
  for slot in I[a]:
   p=common-rot(1)*slot;key=(si,{'D':0,'V':2,'U':5}[a],int(p.real),int(p.imag),1,2,0,3);seen.add(key);r=refs[key];old=r['original_signed_row'];assert old['pose']==xy(p)+[1]and old['input_cell']==xy(slot)and old['actual_full_source']==src
   if int(p.real+p.imag+1)%2:why='sector'
   elif key in counted:why='signed_existing_COUNT5'
   elif p==1:assert a=='D'and center(p,1)==center(raw['D']['p'],0);why='actual_old_D_EXIT_entry_repeat'
   elif p==-1:assert a=='V'and meet(*ch('D',0j,0),*ch(a,p,1))==(Fraction(1,2),Fraction(1,2));why='strict_old_D_midpoint_contact'
   else:assert a=='V'and p==1j;why='strict_contact_with_genuine_actual_NEXT_N_atom'
   assert r['route']==why;cc[why]+=1
assert seen==set(refs)and len(seen)==16
for row in J['fresh_D_common_entry_reserve']['all4_genuine_NEXT_N_atom_strict_crossings']:
 a=row['actual_next_atom'];hit=meet(*ch(a,1+1j,0),*ch('V',1j,1));assert all(0<t<1 for t in hit);assert row['strict_chord_contact']==dict(old_s=str(hit[0]),new_t=str(hit[1]))
ends=[];negends=[]
for a in 'DVU':
 for slot in I[a]:
  assert slot.imag>=1 and slot.real>=-1
  for h in (0,3):
   p=common-rot(h)*slot;z=tr(W[a],p,h);assert z['p'].imag>=0 and(h!=0 or z['p'].real>=2);ends.append((a,tuple(xy(slot)),tuple(xy(p)+[h]),tuple(xy(z['p'])+[z['h']])))
  se=tr(W[a],-rot(2)*slot,2);ee=tr(W[a],-rot(1)*slot,1);assert se['p'].imag<=0 and ee['p'].imag<=0;negends.append((a,tuple(xy(slot)),tuple(xy(se['p'])+[se['h']]),tuple(xy(ee['p'])+[ee['h']])))
assert set(ends)=={(r['atom'],tuple(r['input']),tuple(r['pose']),tuple(r['RAW_EXIT']))for r in J['fresh_D_common_entry_reserve']['all16_N4_W5_plain_input_RAW_endpoint_inequalities']}
assert set(negends)=={(r['atom'],tuple(r['input']),tuple(r['S_RAW_exit_relative_tag']),tuple(r['E_RAW_exit_relative_tag']))for r in J['all8_universal_negative_y_current_input_RAW_exit_bounds']}
refs={(r['source'],tuple(r['F_tag']),r['consumer'],tuple(r['input']),tuple(r['pose'])):r for r in J['all128_coupled_F46_F47_source_current_first_loss_rows']};seen=set();pc=Counter()
for src,anchors in [('D',{common}),('C',CO)]:
 for tag in FT:
  for a in 'DVU':
   for slot in I[a]:
    for h in range(4):
     p=tag-rot(h)*slot;key=(src,tuple(xy(tag)),a,tuple(xy(slot)),tuple(xy(p)+[h]));seen.add(key);r=refs[key];z=tr(W[a],p,h);assert r['RAW_EXIT']==xy(z['p'])+[z['h']]and r['owner']['context_tick0']==first(ctx[a],slot)[1]
     touch={q for q in anchors if(q-p)/rot(h)in ctx[a]['req']}
     if int(p.real+p.imag+h)%2:why='sector'
     elif touch:assert touch=={complex(*q)for q in r['independently_CURRENT_source_outputs']};why='touches_independent_source_CURRENT_identity_before_target'
     elif bad(a,p,h,FT):why='other_held_F_tag_CORE_or_first_WHITE';bindbad(r['held_F_conflicts'],bad(a,p,h,FT),a)
     elif meet(*FV,*ch(a,p,h))is not None or meet(*ch(src,0j,0),*ch(a,p,h))is not None:why='earlier_actual_F_or_ordinary_source_contact'
     else:assert h==0 and(a,p)in {('D',-2-2j),('V',-2-4j),('U',-1-5j)}and z['p']==-1-1j;why='N0_unreachable_or_N4_exit_y_minus1_cannot_reach_lower_N4_or_W5_target'
     assert r['route']==why;pc[why]+=1
assert seen==set(refs)and len(seen)==128 and sorted(pc.values())==[3,6,21,34,64]
fg=tr(W['F']);guards={}
for g in J['all5_reused_literal_F_negative_output_guards']:
 a=g['atom'];p=complex(*g['head']);h=g['h'];tag=complex(*g['initial_SAME_FOREIGN_output_reserve']['postforeign_cell']);q=fg['p']+rot(fg['h'])*tag;loc=(tag-p)/rot(h);assert tag.imag<0 and p.imag>tag.imag and fg['last'][q]==('R',g['initial_SAME_FOREIGN_output_reserve']['last_R_tick0'])and tag not in K and first(ctx[a],loc)==('R',26 if h==2 else 6);guards[(a,*xy(p),h)]=g
n4=J['extra_N4_actual_sourceD_hole_guard'];assert tr(W['D'])['last'][-1]==tr(W['D']+W['C'])['last'][-1]==('L',1)and first(ctx['U'],3j)==('L',23)and 3j not in K
jo={tuple(r[:3]):r[3]for r in json.loads((R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text())};assert jo[7,0,3]==4==n4['actual_produced_input_minimum']
for rr in n4['all8_zero_clock_N_FULL_output_y_bounds']:
 w=''.join(W[a]for a in rr['packet']);z=tr(w);oo={q for q,(c,t)in z['last'].items()if c=='R'and(q-z['p'])/rot(z['h'])not in K};assert sorted(map(xy,oo))==rr['all_full_outputs']and min(q.imag for q in oo)==rr['minimum_full_output_y']==0
 if rr['packet']in ('D','DC'):assert -1 not in oo
beta=1-1j;assert(beta+1j)/rot(3)in K and W['U'][:11]==W['C'][:11]==M
refs={(r['first_post_RAW'],r['actor'],*r['pose']):r for r in J['all84_firstpostD_C_proper_F_contact_closures']};seen=set();cl=Counter()
for src,anchors in [('D',{common}),('C',CO)]:
 for key,geom in proper.items():
  a,x,y,h=key;p=complex(x,y);k=(src,*key);seen.add(k);r=refs[k];assert all(r[q]==v for q,v in geom.items())
  if bad(a,p,h,anchors|FT):why='CURRENT_source_outputs_and_coupled_F46_F47_CORE_or_WHITE';bindbad(r['guards'],bad(a,p,h,anchors|FT),a)
  elif key in guards:why='actual_negative_y_F_output_coordinate_reserve';assert r['signed_literal_guard']==guards[key]
  elif src=='D'and key==('U',-1,-3,0):why='actual_sourceD_L1_deleted_upper_input_no_clock0_rebirth_then_min4';assert r['guard']==n4
  else:assert key==('U',0,-1,3);why='SAME_incoming_FOREIGN_beta_at_same_W5_ENTRY_CORE';assert r['guard']==J['extra_W5_beta_same_ENTRY_reader_lift']
  assert why==r['route'];cl[why]+=1
assert seen==set(refs)and len(seen)==84 and sorted(cl.values())==[1,2,10,71]
exceptions=[]
for rr in J['all128_coupled_F46_F47_source_current_first_loss_rows']:
 if rr['route'].startswith('N0_'):
  pp=complex(*rr['pose'][:2]);aa=rr['consumer'];assert rr['F_tag']==[-2,-1]and rr['owner']['context_tick0']==len(W[aa])+1
  for target in 'VU':assert tr(W[aa]+W[target]+M,pp,0)['bad']is None
  exceptions.append(rr)
assert len(exceptions)==6
out={'status':'HOLD three N4 typed residues lack the claimed pair-current reserve; finite inventories verified','manifest':sha(MF),'script':sha(S),'equal_entry_marker_loss_rows':exceptions,'unclosed_typed_residues':[['D','V',-1,-1,0],['D','U',-1,-1,0],['C','U',-1,-1,0]],'closed_heads':62,'outgoing_b1_aliases':20,'proper_heads':42,'source_queries':dict(cc),'pair_roles':dict(pc),'typed_closures':dict(cl),'analytic_review':['Exact rational endpoint parallelograms, sector and positive-newtime checks reconstruct62 closed heads. Twenty old-exit aliases belong to actual outgoing b1 D/C and are separately signed; no foreign window is applied to them. The42 proper labels include old entry, new terminal and unique C2..5 windows. No ordinary chord is parallel to this F chord; pre-entry onset is excluded only by GLOBAL-first stopping.','Fresh sourceD common reserve is invoked on sourceD-to-hypothetical earlier BASE consumer with real following RAW supplyingM11. Actual precedingF is enough for the base-cut grammar; no foreign age law or terminalC parsing is used. Sixteen exact D/DC E3 rows give4sector7COUNT5 and5 actual nonadjacent source/next-N contacts. The genuine nextN atom exists and may be ownC or D/V/U. All16 N4/W5 RAW-exit inequalities retain marker-owned inputs and arbitrary zero-C runs.','The128 pair roles omit beta entirely. Independent source anchors are current through the actual target; true anchor input is therefore excluded as a prior loss, not mislabelled a color conflict. Simultaneous F-tag inputs remain. ERROR: the six residual N gates exit(-1,-1,N), exactly equal to two genuine N4 heads. They consume F47 in the next-word marker, so F47 may be alive in CORE rather than CURRENT at target entry. Only sourceC/V has an independent anchor cut; D/V,D/U,C/U remain unclosed. The claimed universal y<=-2 bound is false. Source/F contact alternatives require the actually simple prefix and are not literal field cuts.','All five lower-F output guards are genuine actual lastR identities; eight independent source input-to-RAW-exit inequalities prove the negative-y endpoint reserve without firstV/U or postforeign ages. Actual own R6/R26 supplies the contradiction.','N4 U upper-input minimum is FOUR, not five. SourceD L1 physically deletes the old initial identity. Every actual clock0 later full N producer begins y>=1; all eight full output sets have ymin0, and ownD/DC misses the hole. Any surviving replacement external input thus has actual producer clock>=1 and age<=3. The real BASE-cut G8 residual theorem rules out silent CORE export bypasses; arbitrary CORE R writes are not assumed absent.','W5 beta transfer is at exactly the previously signed target-entry pose(0,-1,W), with identical actual firstM11 and universal entryCORE. Earlier helper factors still end at BASE and use the actual next word, nowU, for M. No targetC-specific body or terminalDCC parsing enters the proof.','The author84 syntactic split is71 current masks10 lower-output guards1 min4 hole2 beta-entry lifts, but three of those current-mask cases lack a valid currentness premise. Do not promote the original-F closure until a separately frozen correction closes them. The intended originalF ownership theorem under actual U-entryG8/FIRSTF/immediateD/C/global-first/actualM is NOT signed because of those residues. No later-source, arbitrary-tail simplicity, secondforeign or attraction theorem follows.']};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
