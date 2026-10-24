from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'leading_C_ordinary_owner_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='594a14f35ca48a2f27760d51e33945dc18ef15bc7a7d53b4db162162a1b73342'
m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet=[ns[k]for k in ('W','M','K','tr','rot','xy','center','meet')];G={a:tr(W[a])for a in W};CT={a:tr(W[a]+M)for a in W};J=json.loads((D/'leading_C.json').read_text());gram=J['exact_leading_C_grammar']
I={a:{q for q,b in CT[a]['req'].items()if b and q not in K}for a in W};assert not I['C']and sum(len(I[a])for a in 'DVU')==8
failures=[]
for ar in gram['all3_FOREIGN_CCC_actual_marker_conflicts']+gram['both_universal_CC_to_D_or_U_conflicts']+gram['all3_foreign_CC_to_V_exclusions']+[gram['universal_C_to_U_conflict']]:
 seq=ar['word'];t=tr(''.join(W[a]for a in seq)+M);assert t['bad'];b=t['bad'];assert b[0]==ar['conflict']['conflict_read']and b[1]==ar['conflict']['previous_read'];failures.append((seq,b[0],b[1],xy(b[2]),b[3]))
assert {r[0]for r in failures}=={'FCCC','QCCC','BCCC','CCD','CCU','FCCV','QCCV','UBCCV','CU'}and tr(''.join(W[a]for a in 'BCCV')+M)['bad']is None
pairs=json.loads((R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency.json').read_text())['rows'];legal={(z['source'],z['foreign'])for z in pairs if z['status']!='IMPOSSIBLE_LITERAL_PAIR'};assert legal=={('V','F'),('V','Q'),('U','F'),('U','Q'),('U','B')}
controls=[]
for ar in gram['all2_genuine_U_entry_terminal_CC_positive_controls']:
 seq=ar['word'];raw=''.join(W[a]for a in seq)+M;t=tr(raw);assert t['bad']is None;seed={q for q,b in t['req'].items()if b};assert sorted(map(xy,seed))==ar['actual_finite_black_seed'];B=set(seed);p=0j;h=0
 for i,c in enumerate(raw):
  assert(p in B)==(c=='L');r=ar['all_actual_RAW_and_given_M11_reads'][i];assert r['cell']==xy(p)and r['turn']==c
  B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 controls.append(dict(word=seq,seed=sorted(map(xy,seed)),final=sorted(map(xy,B)),pose=[*xy(p),h],reads=len(raw)))
# Literal leadingC->firstD chart transform and genuine output birth.
beta=1-1j;common=2+0j;ep=G['C']['p'];eh=G['C']['h'];assert ep==1j and eh==3 and ep+rot(eh)*beta==1+2j and G['C']['last'][1+2j]==('R',13)
assert beta not in CT['D']['req'];target=-1j;th=3;assert(beta-target)/rot(th)in K
oldch=(center(0j,0),center(G['D']['p'],0));rows=[];cnt=Counter();AR={(z['source_D_ENTRY_to_consumer_ENTRY_C_clock'],z['actual_consumer'],tuple(z['actual_input'])):z for z in J['new_C_preceded_sourceD_terminal_C5_beta_guard']['all48_actual_first_CURRENT_beta_loss_roles']}
for n in range(6):
 h=(-n)%4
 for a in 'DVU':
  for q in I[a]:
   p=beta-rot(h)*q;en=p+rot(h)*G[a]['p'];key=(n,a,tuple(xy(q)));ar=AR[key];assert ar['pose']==[*xy(p),h]and ar['RAW_EXIT']==[*xy(en),h]
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif n==0:assert p.imag<1;why='N0 cone'
   elif n==1:assert p.imag<2;why='W1 cone'
   elif n==2:
    co=meet(*oldch,center(p,h),center(en,h))
    if co is not None:assert a=='U'and p==0j;why='nonadjacent sourceD exit repeat'
    else:assert a=='U'and p==1+1j and(common-p)/rot(h)in I[a];why='genuine BASE factor common min3'
   elif n==3:
    co=meet(*oldch,center(p,h),center(en,h))
    if co is not None:why='earlier sourceD chord contact'
    elif p==-1-2j:
     assert a=='U';star=p+rot(h)*1j;assert star==-2j and(star-target)/rot(th)in K;why='new U originalstar in final C CORE'
    else:
     assert(a,p)in[('V',-2-1j),('U',-3-2j)]and center(en,h)==center(target,th);why='earlier RAW exit is final repeated corrected vertex'
   elif n==4:
    assert en.imag>=-1 and en.imag+1>target.imag and all((rot(3)*G[b]['p']).imag>=0 for b in 'DVU');why='N plus C plus W y cone'
   else:
    if en.imag>target.imag:why='W y cone'
    elif en.real<target.real:why='W x cone'
    else:
     assert en==target and(a,p)in[('V',3-2j),('U',4-1j)]and CT[a]['req'][(common-p)/rot(h)]is False;assert p.imag<0;why='independently current common at W5 negative head'
   rows.append((key,[*xy(p),h],[*xy(en),h],why));cnt[why]+=1
assert len(rows)==48 and {r[0]for r in rows}==AR.keys()
# Explicitly select only the independently retained sourceD common sublemma,
# never the rejected original143d universal F-pair reserve.
commonres=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json').read_text())['fresh_D_common_entry_reserve'];assert commonres==J['new_C_preceded_sourceD_terminal_C5_beta_guard']['independently_retained_fresh_D_common_reserve']
assert len(commonres['all16_plain_E3_sourceD_DC_common_queries'])==16 and len(commonres['all16_N4_W5_plain_input_RAW_endpoint_inequalities'])==16
cp=json.loads((R/'first_post_Q_B_DC_source_closure_2026-10-24/Q_B_DC_closure.json').read_text())['fresh_C_portable_coupled_reserve'];assert len(cp['all96_plain_true_input_first_loss_roles'])==96 and cp['statement']==J['fresh_C_portable_reserve_scope']
bd=json.loads((R/'ordinary_boundary_owner_beta_2026-10-24/boundary_beta.json').read_text())['all7_possible_boundary_position_branches'];CO={2+0j,2+1j,1+2j};branches=[]
for b in bd:
 q=complex(*b['actual_later_pose'][:2]);h=b['actual_later_pose'][2];p=1j+rot(3)*q;hh=(h+3)%4;clock=b['actual_global_C_clock']+1;a=b['later_atom']
 au=next(z for z in J['all7_actual_BASE_boundary_branches_with_genuine_preceding_C_guard']if z['signed_actual_boundary_branch']==b)
 assert au['actual_target_in_leading_C_chart']==[*xy(p),hh]and au['actual_leading_C_ENTRY_to_target_ENTRY_C_clock']==clock
 if clock==6:assert a=='C'and q==target and h==th;route='new betaW5'
 else:
  assert clock==4 and hh==0 and p.imag<=1 or clock==5 and hh==3 and p.imag<=0
  bad={z for z in CO if(z-p)/rot(hh)in K or CT[a]['req'].get((z-p)/rot(hh))is False};assert bad
  assert bad=={complex(*z['SAME_CURRENT_BLACK'])for z in au['actual_CURRENT_CORE_or_first_WHITE']};route='preceding C three outputs'
 branches.append(dict(source=b['earlier_atom'],target=a,pose=[*xy(p),hh],clock=clock,route=route))
assert Counter(z['route']for z in branches)=={'preceding C three outputs':6,'new betaW5':1}
old=json.loads((R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases'];ledger=J['all129_actual_BASE_factor_geometry_source_position_routes'];assert len(old)==len(ledger)==129
for r,ar in zip(old,ledger):
 assert ar['signed129']==r
 if r['surviving_allowed_first_full_packet_ids']:
  matches=[b for b in bd if b['earlier_atom']==r['earlier_atom']and b['later_atom']==r['later_atom']and b['actual_global_C_clock']==r['entry_C_gap']];assert matches and {json.dumps(b,sort_keys=True)for b in matches}=={json.dumps(z['signed_actual_boundary_branch'],sort_keys=True)for z in ar['all_actual_position_branches']}
O=dict(status='PASS leading-C postFOREIGN ordinary-owner lane only',manifest=sha(mf),script=sha(S),literal_grammar_failures=failures,positive_terminal_CC=controls,all48_beta_roles=rows,beta_route_counts=cnt,all7_boundary_branches=branches,analytic_review=['Every earlier actual RAW has its realM11 supplied by the nextRAW; D contributes10 then actual nextL. FinalM11 is given, never promoted to a new completeG7. Literal CCC/CCD/CCU/FCCV/QCCV and actualU-beforeFIRSTB UBCCV leave real terminalCC or exactlyC followedfirstD/V. PreparedBCCV and UQCC/UBCC remain legal controls.','LeadingC really creates betaC(1,2) atR13 outsideEXITCORE, transported to firstD chart(1,-1). New48 loss roles retain marker-only/core inputs. SourceD min3 is used solely on its actual earlier BASE-ending G8 factor with precedingC and real nextmarker. No terminalC/DCC parsing occurs.','At E3, newU originalstar persists by the signed allordinaryRAW theorem; other two loss exits repeat the future correctedENTRY vertex nonadjacently across two Cs. N4/W5 cones use actual +x/+y endpoints. Last twoW5 clearers demand sourceD commonWHITE at negativey, inside the independently retained freshD common reserve, not the rejected universal F-pair proof.','All129 previously signed G8 geometric rows and actual1607 boundary positions are reused only when the actual BASE-start factor genuinely parsesG8. Seven true branches transform with leadingC clock+1; six use genuine precedingC O3 reserve at N4y<=1/W5y<=0, one uses the newC-preceded betaW5. C1 withinfirstDC remains source-entry clock0, not a second-C shift.','Only source beforefirstBASE is actualb1C, covered separately by signed1b595 or8b58+mandatory5e243. TerminalDCC secondC is covered directly by signed366d, while its firstC gives genuineDC. All guards stop at global-firstENTRY or actual ownRAW reads.'],scope=m['scope'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
