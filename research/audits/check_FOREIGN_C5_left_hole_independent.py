from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_C5_left_hole_frontier_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='f01a99e7c429acdda9d3f451007151493b2e8efb86783feb4af1fa21f0e4f714';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'C5_left_hole.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};pose=lambda p,h:[*xy(p),h];a=-3+3j;r=-4+3j;old13={-1-1j,-1+0j,-1+1j,0j,1j,1+0j,1+1j,1+2j,-4+1j,-4+2j,-3+2j,-2+1j,-2-1j};assert old13=={complex(*q)for q in J['always_CURRENT_through_C3_old13']}and max(q.imag for q in old13)==2
for A in'FQB':
 assert G[A]['last'][a]==('L',34)and G[A]['last'][r]==('L',35);assert G[A]['h']==2 and G[A]['p'].imag<=-2
 ek={G[A]['p']+rot(G[A]['h'])*q for q in K};assert all(q not in ek and G[A]['last'][q][0]=='R'for q in old13)
# Enumerate ALL physical RAW final-R origins, including actual CORE writes.
RR={A:{q:t for q,(c,t)in z['last'].items()if c=='R'}for A,z in G.items()};counts={};keep={};allrows=[]
for hole in[a,r]:
 for h in[0,3,2]:
  cc=Counter();kk=[]
  for A in'DCVU':
   for q,t in RR[A].items():
    p=hole-rot(h)*q;ep=p+rot(h)*G[A]['p'];eh=(h+G[A]['h'])%4;au=next(v for v in J['all216_CORE_inclusive_last_RAW_R_roles']if v['hole']==xy(hole)and v['epoch_heading']==h and v['producer']==A and v['ENTRY']==pose(p,h));assert au['RAW_EXIT']==pose(ep,eh)and au['final_R_slot']==xy(q)and au['hole_in_EXIT_CORE']==((hole-ep)/rot(eh)in K)
    if(int(p.real+p.imag)+h)%2:why='sector'
    else:
     bad={g for g in old13 if(g-p)/rot(h)in K or C[A]['req'].get((g-p)/rot(h))is False};assert bad=={complex(*v['SAME_current_original'])for v in au['current_conflicts']};why='held_old13'if bad else'possible_funder'
    assert au['route']==why;cc[why]+=1;allrows.append((xy(hole),h,A,pose(p,h),pose(ep,eh),why))
    if why=='possible_funder':kk.append((A,p,ep,eh))
  assert sum(cc.values())==36;counts[str((xy(hole),h))]=cc;keep[hole,h]=kk
assert len(allrows)==216
for hole in[a,r]:
 assert len(keep[hole,0])==4
 for A,p,ep,eh in keep[hole,0]:
  assert p==-5+3j;qq=(r-p);first=next((i,c)for i,(v,h,c)in enumerate(C[A]['reads'])if v==qq);assert first==(5,'L')
assert {(A,p,ep,eh)for A,p,ep,eh in keep[r,3]}=={('V',-2+3j,-5+4j,3),('U',-1+4j,-5+4j,3)}
for A,p,ep,eh in keep[r,3]:assert(r-ep)/rot(eh)==-1-1j and p.real>ep.real
for A in'DCVU':assert [(i,c)for i,(q,h,c)in enumerate(G[A]['reads'])if q==-1-1j]==[(2,'L')]
assert len(keep[a,3])==3 and all(ep.real<=-5 for A,p,ep,eh in keep[a,3])
assert not keep[a,2]and keep[r,2]==[('U',-4+4j,-4+0j,2)]
qq=(a-(-4+4j))/rot(2);assert next((i,c)for i,(q,h,c)in enumerate(C['U']['reads'])if q==qq)==(14,'L')
# Generic CORE loss completeness and all-eight S exit inequalities.
inputs={A:{q for q,b in C[A]['req'].items()if b and q not in K}for A in W};assert not inputs['C'];lossexits=[];marker=[]
for A in'DCVU':
 ek={G[A]['p']+rot(G[A]['h'])*q for q in K}
 for q in ek-K:assert q in C[A]['req']
 for q in inputs[A]:
  if q not in G[A]['req']:assert q in ek;marker.append((A,xy(q)))
  if A=='C':raise AssertionError('unexpected C external input')
  dy=q.imag-G[A]['p'].imag;assert dy<=0;lossexits.append((A,xy(q),int(dy)))
assert len(lossexits)==8
assert {(a,tuple(q),d)for a,q,d in lossexits}=={(v['atom'],tuple(v['true_input']),v['S_RAW_EXIT_y_minus_old_tag_y'])for v in J['all8_S_first_CURRENT_loss_EXIT_inequalities']}
# Physical support covers EVERY R, not just final outputs, for all endpoint cones.
support=[]
for A in'DCVU':
 for t,(q,h,c)in enumerate(G[A]['reads']):
  if c!='R':continue
  assert q.imag>=0 and q.real>=-1
  if A=='C':assert q.real>=0
  else:assert q.imag<=G[A]['p'].imag
  support.append((A,t,xy(q),pose(G[A]['p'],G[A]['h'])))
assert support==[(v['atom'],v['own_tick0'],v['local_R'],v['N_RAW_EXIT'])for v in J['all_ordinary_physical_R_supports']]
# S0 and C1 heads cannot raise y. E1/C2 physical writes remain <= -2.
for A in'DVU':assert (rot(2)*G[A]['p']).imag<=0 and(rot(1)*G[A]['p']).imag<=0
assert(rot(2)*G['C']['p']).imag==-1 and(rot(1)*G['C']['p']).imag==0
# W, C4, and S never increase x. This is NOT a y-frontier.
for A in'DVU':assert(rot(3)*G[A]['p']).real<=0 and(rot(2)*G[A]['p']).real<=0
assert(rot(3)*G['C']['p']).real==-1
# Every S4 physical final-R origin head has y>=the hole y=3, irrespectivefield.
for hole in[a,r]:
 for A in'DCVU':
  for q in RR[A]:assert(hole-rot(2)*q).imag>=3
# C5 and E5 r birth exits all have x>=-4, preventing target x=-5.
post=[]
for A,h in[('C',2)]+[(A,1)for A in'DVU']:
 for q in RR[A]:
  p=r-rot(h)*q;ep=p+rot(h)*G[A]['p'];assert ep.real>=-4;post.append((A,h,xy(p),xy(ep)))
for A in'DVU':assert(rot(1)*G[A]['p']).real>0
for A in'FQB':
 p=-5-2j;qq=(r-p)/rot(1);assert qq==-5+1j and qq not in K;assert next((t,c)for t,(q,h,c)in enumerate(C[A]['reads'])if q==qq)==(38,'L')and len(W[A])>38
# Full prepared20-cell transient CORE repair, with every actual field retained.
reg=J['prepared_transient_CORE_repair_regression'];seed={complex(*q)for q in reg['complete_seed']};z=tr(W['V']+W['C']+M,-2+3j,3);assert z['bad']is None and seed==({q for q,b in z['req'].items()if b}|old13)and len(seed)==20 and a not in seed and r not in seed;B=set(seed);ids={q:('initial',q)for q in seed};fields=[];cuts=[]
for t,(q,h,c)in enumerate(z['reads']):
 au=reg['all_actual_reads'][t];assert au['cell']==xy(q)and au['turn']==c and au['tick0']==t;assert(q in B)==(c=='L');assert q not in old13
 if c=='L':B.remove(q);ids.pop(q)
 else:B.add(q);ids[q]=('R',t)
 fields.append(sorted(map(xy,B)))
 if t+1 in[18,33,44]:
  hh=(h+(1 if c=='R'else-1))%4;p=q+ns['V'][hh];au=next(v for v in reg['actual_cuts']if v['actual_read_count']==t+1);assert au['pose']==pose(p,hh)and au['complete_BLACK']==sorted(map(xy,B));assert a in B and(a-p)/rot(hh)not in K
  if t+1==18:assert ids[r]==('R',12)and(r-p)/rot(hh)in K
  else:assert r not in B
  cuts.append(dict(cut=t+1,pose=pose(p,hh),a_CURRENT=True,r_alive_CORE=t+1==18))
assert z['reads'][20][0]==r and z['reads'][20][2]=='L'
O=dict(status='PASS generic source-FOREIGN exact-C5 left-hole recipient exclusion, with genuine W CORE repair retained',manifest=sha(mf),script=sha(S),all216_physical_final_R_roles=allrows,group_counts=counts,all8_S_loss_exit_inequalities=lossexits,marker_only_inputs_verified_in_EXIT_CORE=marker,all41_physical_R_supports=support,all_C5_E5_unconditional_r_birth_exit_bounds=post,prepared20_control=dict(all44_postread_fields=fields,cuts=cuts),analytic_review=[
'Actual F/Q/B lastL34/L35 leave a/r WHITE regardless of arbitrary prior archive. Signed b961 supplies the SAME13 originals through ordinaryC3 even after its permitted pairedN2 rewrite. All13 have y<=2. Actual C I0/CORE completeness preserves them to the initialS4 cut; no broaderFORE seal is imported.',
'All216 finalRAW-R alignments includeEXITCORE. S0/E1/C2 supportcones cannotwritey3. Every N2/C3 compatible funder ofeitherhole firstneedsrBLACKatownL5, so the earliestcompleted BLACKrepair cannotoccurthere. AninternalR laterdeleted doesnotfundanotherRAW entry.',
'The W3 r repairs V(-2,3,W),U(-1,4,W) are genuine and retained. BothEXIT(-5,4,W) putr aliveCORE(-1,-1); the NEXT ACTUAL ordinaryRAW has its sole readthere L2, deletingitphysically. Such anextRAW exists beforeexactC5 target. No furtherW r-funder headx>-5 canbereached, and C4 hasno compatiblefinalR. Thusr isWHITE atS4start, not ateveryWcut.',
'All possibleW a-births EXITx<=-5. W,C4,S cannotincreasex, so theycannotfund a atU(-4,4,S). W mayraisey; the discarded y-frontier isnotused. The otherhole mayremainCURRENT externally.',
'At anyS4 holeproducerENTRY, heady>=3. If anold13 taghad firstlostCURRENT earlier, oneoftheeight actualDVU inputs, includingmarkerCOREcapture, wouldgiveRAWEXITy<=tagy<=2; subsequentS cannotclimbback. Hence all13 areCURRENT atthisspecific producerENTRY, not throughoutarbitraryS4. Held-fieldtableseliminatealla producersandleaveonlyr-helperU(-4,4,S), whoseownL14 requiresunfundablea. Itmaypartiallywrite r atR11 beforefailing; no completedrepair follows.',
'AnyC5 physicalr R hasEXITx>=-4, andanyE5 DVU physicalr R alsoEXITx>=-4 bylocalRy<=exitY. With nofurtherC orFORE, subsequentE cannotreach recipientx=-5. Thusr isWHITEat itsENTRY; everyF/Q/B there firstrequests rBLACKatownL38 beforeanyrwrite. Finalcontradictionneeds nofutureM.',
'Completeprepared20-cell VC+M regressionreplays44reads/allfields: rR12 aliveCOREat18, killedbyactualC L2/global20; aR11 staysCURRENT, all13 initialanchorsunread. It hasnoassertedFORE/U ancestry andprevents a falseWHITEpermanence strengthening.',
'Only exactfiveordinaryCs andrecipientENTRY(-5,-2,E) areexcluded, forallnine source/recipientchoices. No Uhistory,simplicity,global-first orrailbound isneeded. Partialrecipient hookloss isallowed; noallC5classification, automaticiteration, arbitrarytail simplicity orcapture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(counts);print(sha(S.with_suffix('.json')))
