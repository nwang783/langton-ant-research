from pathlib import Path
import hashlib,json
from collections import Counter
S=Path(__file__);R=S.parents[1];D=R/'F_firstD_N4_active_CORE_gate_repair_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='aa803f94b58ed324bf9e7439526b67414fdcd3423bb07d046fc27b38fcdba7e3';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet')];J=json.loads((D/'D_N4_gate_repair.json').read_text());F=tr(W['F']);assert F['h']==2;g=-3-3j;hole=-1-2j;fp=lambda q:(q-F['p'])*rot(2);actual=lambda q:F['p']+rot(2)*q
assert F['last'][actual(g)]==('R',30)and F['last'][actual(hole)]==('L',49);FK={F['p']+rot(F['h'])*q for q in K};assert actual(g)not in FK and hole not in K and hole not in tr(W['D']+M)['req']
# Corrected actualF chord in exit-normalized coordinates.
fv=tuple((q-2*F['p'])*rot(2)for q in(center(0j,0),center(F['p'],F['h'])));assert fv==(-7-3j,-1-1j)
full=[]
for a in('D','DC','V','VC','VCC','U','UC','UCC'):
 z=tr(''.join(W[c]for c in a));ek={z['p']+rot(z['h'])*q for q in K};O={q for q,(c,t)in z['last'].items()if c=='R'and q not in ek};assert min(q.imag for q in O)>=0 and min(q.real for q in O)>=-2
 author=next(r for r in J['all8_actual_full_output_N_W_lower_bounds']if r['actual_full_packet']==a);assert sorted(map(xy,O))==sorted(author['all_outputs'])
 if a in('D','DC'):assert hole not in O
 full.append(dict(packet=a,O=sorted(map(xy,O)),min_N_y=int(min(q.imag for q in O)),min_W_y_offset=int(min(q.real for q in O))))
JO={tuple(r[:3]):r[3]for r in json.loads((R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text())};readers=[]
for a,p,slot,typ,t in [('V',-2-4j,1+2j,4,13),('U',-1-5j,3j,7,23)]:
 assert hole-p==slot and slot not in K;first=next((c,i)for i,(q,hh,c)in enumerate(tr(W[a]+M)['reads'])if q==slot);assert first==('L',t)and 2<JO[typ,int(slot.real),int(slot.imag)];readers.append(dict(reader=a,pose=xy(p),slot=xy(slot),first=list(first),minimum=JO[typ,int(slot.real),int(slot.imag)]))
rows=[];counts=Counter();target=-2-2j
for clock in range(5):
 h=(-clock)%4
 for a in'DVU':
  z=tr(W[a]+M);first={}
  for t,(q,hh,c)in enumerate(z['reads']):first.setdefault(q,(c,t))
  for q,(c,t)in first.items():
   if c!='L'or q in K:continue
   p=g-rot(h)*q;end=tr(W[a],p,h);e,eh=end['p'],end['h'];co=None
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif clock==0:assert p.imag<1;why='initial_N0_head_below_sourceD_EXIT_y1'
   elif clock==1:assert p.imag<2;why='initial_W1_head_below_y2'
   elif clock==2:
    co=meet(*fv,center(p,h),center(e,eh));assert co is not None;why='S2_already_contacts_actual_F_piece_or_entry'
   elif clock==3:
    if e.real+1>target.real:why='remaining_E_to_N_C_then_nonnegative_x_cannot_reach_lossD'
    else:
     assert(e,eh)==(-3-4j,1);cstep=tr(W['C'],e,eh);assert(cstep['p'],cstep['h'])==(-2-4j,0);assert target.real==cstep['p'].real and (target.imag-cstep['p'].imag)%4!=0;why='exact_remaining_x_forces_empty_E_and_only_N_U_but_needed_y2_not_multiple4'
   else:assert e.imag>target.imag;why='N4_RAW_exit_y_above_lossD_and_N_cannot_descend'
   row=next(r for r in J['F30_CURRENT_endpoint_guard']['all40_first_loss_clock_input_roles']if r['consumer']==a and r['ENTRY_C_clock']==clock and r['input']==xy(q));assert row['pose']==[*xy(p),h]and row['RAW_EXIT']==[*xy(e),eh]and row['route']==why;rows.append(dict(clock=clock,consumer=a,pose=[*xy(p),h],input=xy(q),read=t,exit=[*xy(e),eh],route=why,contact=repr(co)));counts[why]+=1
assert len(rows)==40 and g-target in K
# Exact all-length endpoint semigroup premises, not a searched rail bound.
assert [(tr(W[a])['p'],tr(W[a])['h'])for a in'DVU']==[(1+1j,0),(1+3j,0),(4j,0)];assert tr(W['C'])['p']==1j
losses={('D',-2-2j),('V',-2-4j),('U',-1-5j)};pairs=[]
for a,p in sorted(losses,key=lambda r:r[0]):
 z=tr(W[a],p,0);assert(z['p'],z['h'])==(-1-1j,0)
 for b in'VU':assert not tr(W[a]+W[b]+M)['bad'];pairs.append((a,b))
assert len(J['all6_typed_gate_by_final_actor_closures'])==6 and len(pairs)==6
O={'status':'PASS separate sourceD N4 V/U active-CORE ancestry repair ONLY; original143d proof remains rejected','manifest':sha(MF),'script':sha(S),'full_producer_outputs':full,'two_true_hole_readers':readers,'forty_first_loss_roles':rows,'counts':dict(counts),'preserved_literal_pairs':pairs,'analytic_review':['The original shared-entry activeCORE mechanism is retained: earliest F47 loss can occur in oneofthree complete N4 lossRAWs ending exactly at(-1,-1,N), then die at finalV/U read2. Since noCs remain and every N BASE strictly raisesy, these lossRAWs must immediately precede the proposed finalactor; all six localpairs remain feasible.','LossV/U has OTHER externaltrueinputh=(-1,-2), actualF L49-deleted and entirely missed by initialD+M. Actual sourceD-to-lossBASE G8 with real priorF and finalactor supplying the realM removes any entryresidual exemption. Full eight produceroutput masks, includingtails, have localy>=0 and localx>=-2. N0 starts after sourceD at y>=1, sourceownD/DC misses h; W1heads y>=2 yield alloutputy>=0. Thus any replacement fullproducer startsatC>=2, too young age<=2 for selectedV minimum3 orU upperminimum4. All physical CORE repairs remain allowed and are classified by actual fullproducer if externally supplied at this reader.','LossD would absorb originalF30 into entryCORE. All40 actual plaininput roles includingmarker currentloss are independently rebuilt. SourceDmisses this tag; N0/W1heads belowreachablecones; sector-validS2roles alreadycontactactualF beforetheproposedglobalfirstentry, including nonadjacent entryvertex returns. This uses exact stopped-simpleprefix, not blanket global simplicity.','E3 earlierloss exits are(-3,-4),(-2,-3),(-1,-4). Exactlyone remainingC adds(1,0); zeroC E motion increasesx and N D/V addsx. Two exits alreadyovershootx. From(-3,-4), exactx forces noE and onlyN U, whoseverticalincrements4 cannot supplyneeded2. This is a nonnegative semigroup argument over arbitraryrails. N4losses finishabove targety andcannotdescend. C externalinput/silentCORE capture exclusion is retained fromsignedactualCinterface.','Thus SAMEF30 is CURRENT at lossDentry, incompatiblewithitsCORE. The two holeguards excludeV/Ulosses; the earlier signedpairtable and independent sourceDcommonreserve then closeexactlythetwo pending sourceD/V,U labels. No FOREIGN age isused and no universalpairCURRENT statement atsharedentry is restored.','Combinedwith separatelysignedfirstC repair, allthree formerlyOPEN labels have distinct ancestry repairs, but original143d full84 argument remains NOTPASSED. Any later geometric join must explicitly bind partial81 plus bothrepairs and original GLOBALfirst/U-entry/FIRSTF scope; no arbitrarytail or universalcapture theorem is inferred.']}
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
