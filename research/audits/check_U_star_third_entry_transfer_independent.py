from pathlib import Path
from collections import Counter
import json,hashlib,importlib.util
S=Path(__file__).resolve();R=S.parents[1];D=R/'U_star_second_ordinary_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'manifest.json';assert sha(man)=='c5a00c92d2e9eb1b2dea3a36791ab5af0b6f76d9a1c600aa9be756d1ab58ad70';mf=json.loads(man.read_text())
for p,h in mf['files'].items():assert sha(D/p)==h
ref=json.loads((D/'second_ordinary_transfer.json').read_text())
for p,h in ref['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_foreign_kinked_barrier_turn_independent.py'))};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns);W,M,walk,center,xy,meet=[ns[k]for k in['W','M','walk','center','xy','meet']];V=(1j,1,-1j,-1);K={-1-1j,-1,-1j,0j,1};star={0j,1j,1+0j,1+1j};four={'LEFT':{0j,1j},'TOP':{1j,1+1j},'RIGHT':{1+0j,1+1j},'BOTTOM':{0j,1+0j}};cx=lambda q:complex(*q);tr={a:walk(W[a])for a in'DCVUFQB'};old=((-1,-1),(-1,7));local={};universe=set()
for A in'FQB':
 for b1 in'DCVU':
  for b2 in'DCVU':
   word=W[A]+W[b1]+W[b2];full=walk(word+M);local[A,b1,b2]=(walk(word),full,word)
   if not full['feasible']:continue
   for q,black in full['req'].items():
    if black:
     for tag in star:
      for h in range(4):universe.add((A,b1,b2,*xy(tag-q*(-1j)**h),h))
rr={(z['foreign'],z['first_ordinary'],z['SECOND_ordinary'],*z['foreign_pose']):z for z in ref['all9912_aligned_states']};assert set(rr)==universe;counts=Counter();stats=Counter();new=bottom=0
prior=json.loads((R/'U_star_one_foreign_return_transfer_2026-10-24/U_star_corner_transfer.json').read_text());oldkeep={(z['foreign'],z['first_returned_raw_atom'],*z['foreign_entry_in_creator_U_frame']):{cx(q)for q in z['same_original_CURRENT_cells']}for z in prior['all262_necessary_three_corner_states']}
for A,b1,b2,x,y,h in sorted(universe):
 p=complex(x,y);rot=(-1j)**h;raw,full,word=local[A,b1,b2];row=rr[A,b1,b2,x,y,h]
 if(x+y+h)%2:why='wrong_active_sector'
 elif star&{p+rot*q for q in K}:why='original_CURRENT_inside_FOREIGN_entryK'
 elif any(full['req'].get((q-p)/rot)is False for q in star):why='original_BLACK_vs_combined_before_WHITE'
 else:
  assert(p,h)!=(4j,0);f56=p+rot*tr['F']['p'];fh=(h+tr['F']['h'])%4;pa=p+rot*tr[A]['p'];ha=(h+tr[A]['h'])%4;cut2=walk(W[A]+W[b1]);p2=p+rot*cut2['p'];h2=(h+cut2['h'])%4
  pieces=[(xy(center(p,h)),xy(center(f56,fh)))]
  if A!='F':pieces.append((pieces[-1][1],xy(center(pa,ha))))
  pieces.append((xy(center(pa,ha)),xy(center(p2,h2))))
  if any(meet(*old,*pc)is not None for pc in pieces):why='old_U_chord_contact_through_FIRST_return'
  else:
   why='compatible_necessary_four_corner_state';p3=p+rot*raw['p'];h3=(h+raw['h'])%4;k3={p3+q*(-1j)**h3 for q in K};k2={p2+q*(-1j)**h2 for q in K};seen3={p+rot*q for q,hh,ch in raw['reads']};seen2={p+rot*q for q,hh,ch in cut2['reads']};alive=star-seen3;keep=alive-k3;keep2=star-seen2-k2;ports=[k for k,pair in four.items()if pair<=keep];assert len(keep)>=2 and ports
   assert keep=={cx(q)for q in row['same_original_CURRENT_cells']}and alive=={cx(q)for q in row['same_original_physically_alive_cells']}and alive-keep=={cx(q)for q in row['same_original_alive_CORE_cells']};assert keep2=={cx(q)for q in row['inherited_CUT2_current_originals']};assert ports==row['four_corner_ports'];assert len(word)==row['physical_cut_tick0']and[*xy(p3),h3]==row['THIRD_atom_entry']
   for q in keep:assert(q-p)/rot not in full['req']
   for q in star&seen3:assert next(ch for r,hh,ch in raw['reads']if p+rot*r==q)=='L'
   if len(keep2)==4:new+=1;assert row['CUT2_was_all4_current']
   else:assert oldkeep[A,b1,x,y,h]==keep2 and not row['CUT2_was_all4_current']
   bottom+=ports==['BOTTOM'];stats[b2,len(keep),len(alive),len(keep2)]+=1
 counts[why]+=1;assert why==row['reason']
assert len(universe)==9912 and dict(counts)==ref['classification']and counts['compatible_necessary_four_corner_state']==1093 and new==119 and bottom==12
assert {k:v for k,v in stats.items()}=={(z['second'],z['current'],z['physically_alive'],z['CUT2_current']):z['count']for z in ref['CURRENT_and_physical_alive_counts']}
# All true original/source adjacent cases outside alignment need no artificial exclusion.
for key,(raw,full,word)in local.items():
 if full['feasible']:assert all((q-4j)not in full['req']for q in star)
# Fresh complete physical controls, including exact untouched remote cells.
co_path=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';spec=importlib.util.spec_from_file_location('owner',co_path);co=importlib.util.module_from_spec(spec);spec.loader.exec_module(co)
controls=[]
for long in(False,True):
 a=ref['actual_29_cell_prepared_tail_erosion_control'if long else'prepared_BOTTOM_boundary_control'];packets=a['actual_complete_packets']if long else['F','D','U'];word=''.join(W[z]for packet in packets for z in packet);seed={cx(q)for q in a['complete_initial_BLACK_board']};B=set(seed);original=set(star);p=cx(a['initial_head'][:2]);h=a['initial_head'][2];logs=a['all_fine_reads'if long else'all_actual_fine_reads'];snaps={};spans=[];offset=0
 for i,packet in enumerate(packets):
  end=offset+sum(len(W[z])for z in packet);spans.append((offset,end,packet,i));offset=end
 marks={z['tick0']:z for z in a['physical_boundary_snapshots']}if long else{a[k]['tick0']:a[k]for k in('CUT2','CUT3')}
 for t,ch in enumerate(word+M):
  if t in marks:
   k={p+q*(-1j)**h for q in K};alive=set(original);current=alive-k;snaps[t]=(alive,current);r=marks[t];assert r['head']==[*xy(p),h]
   for st in r['old_star'if long else'original_statuses']:
    q=cx(st['cell']);assert st['original_physically_alive'if long else'same_original_physically_alive']==(q in alive);assert st['original_CURRENT'if long else'same_original_CURRENT']==(q in current);assert st['original_CORE'if long else'same_original_CORE']==(q in alive&k)
  assert (p in B)==(ch=='L');log=logs[t];assert log['cell']==list(xy(p))and log['turn']==ch
  if long:
   found=next(((lo,packet,i)for lo,hi,packet,i in spans if lo<=t<hi),None)
   if found:
    lo,packet,i=found;owner=co.describe(packet,t-lo);owner['actual_packet_index0']=i;assert owner==log['physical_owner']
   else:assert log['physical_owner']['owner_tick0']==t-len(word)
  if ch=='L':B.remove(p);original.discard(p)
  else:B.add(p)
  h=(h+(1 if ch=='R'else-1))%4;p+=V[h]
 assert snaps[94][1]==four['BOTTOM']
 if long:
  assert len(seed)==29 and len(logs)==173 and snaps[142][1]==four['BOTTOM']and snaps[152][0]==four['BOTTOM']and snaps[152][1]=={1+0j}and snaps[162][0]=={1+0j};assert logs[153]['cell']==[0,0]and logs[153]['turn']=='L'and logs[153]['physical_owner']['owner_tick0']==1
 # Second U geometry in both controls, with no assumed earlier ancestry.
 start=complex(4,-3);h0=1;ff=start+(-1j)**h0*tr['F']['p'];hf=(h0+tr['F']['h'])%4;dd=ff+(-1j)**hf*tr['D']['p'];hd=hf;ue=dd+(-1j)**hd*tr['U']['p'];assert xy(center(dd,hd))==(3,3)and xy(center(ue,hd))==(-5,3);hit=meet(*old,xy(center(dd,hd)),xy(center(ue,hd)));assert hit[:2]==(1/2,1/2)
 controls.append(dict(initial_mass=len(seed),fine_reads=len(logs),cut94_current=sorted(map(xy,snaps[94][1])),second_U_strict_old_U_crossing=True,later_one_survivor=long))
out={'status':'PASS two-ordinary same-original four-corner transfer at CUT3 plus literal prepared non-iteration control','author_manifest':sha(man),'aligned_states':len(universe),'filters':dict(counts),'new_default_CUT2_states':new,'BOTTOM_only_states':bottom,'controls':controls,'analytic_review':[
'48fixedsuffixesallactualRAW+realnextM11, alignedagainstallTRUEbeforecells/fourtags/fourheadings, cover everyphysicalolddeath orCUT3COREcapture. FirstphysicalLrequiresTRUEinitialblack; unreadoriginalinK3requiresTRUEfutureM. OutsidealignmentallfourstayCURRENT. No chosenheadbox orprefixscan.',
'OnlyA+b1+b2RAWdeterminesphysicalsurvival atCUT3. FutureMnotexecuted. AreadoriginaldiesatitsFIRSTL regardlesslaterrecolor; survivors are originalsourceRlabels. CURRENT=aliveoutsideactualCUT3K; aliveCOREkeptseparate. AnyintermediateordinaryKentry isphysicallyreadinfirstsix ofthatordinary, so an unreadoriginalcannot secretlyhavebeenretired earlier.',
'Fresh9912fullmaskalignments yield1093 necessaryonlystates, including119previouslyall4currentCUT2cases. Prior262nontrivialstates alonewouldnotcoversecondtouches. Onlysignedone-returngeometry A+b1 versusoldU isused; b2simplicitynotassumed.12BOTTOM-onlystatesgenuinelyretained.',
'Fresh27blackFDU+M and29blackF,D,UCC,V,D,D+M fullboardreplays retainallunlistedWHITE, everyphysicalread andcanonicalowner. At94BOTTOMcurrent;142bothcurrent;152original0,0aliveCOREonly1,0current;153actuallastDrawtick1/read2deletes0,0;162only1,0alive. No futuremarkerreadassignedtoearliercut.',
'Bothpreparedcontrols have secondU strictmidpointcrossingwithhypotheticaloldUchord. TheirinitialstarlabelsarePREPAREDnotgenuineUbirths; nooldcomplete8historysupplied. Theyrefuteunconditionalcorner-onlyiteration butnotgenuineUancestry/no-contacterosiontheorems. Noarbitrarytailinvariantorboundedarchiveclosurefollows.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts,controls)
