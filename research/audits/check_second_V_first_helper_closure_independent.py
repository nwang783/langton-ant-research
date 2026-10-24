from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'U_second_V_first_helper_cohort_closure_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='1be7fb2eb1418a230bb16641411d2734eefef052256095d34ecf54377470ab47';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
ref=json.loads((P/'first_helper_cohort_closure.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_U_second_creator_bud_guards_independent.py'))};exec(Path(ns['__file__']).read_text().split('\nsource=[]')[0],ns)
W,M,K,L,walk,xy,raw=[ns[k]for k in('W','M','K','L','walk','xy','raw')];center=lambda p,h:2*p+(-1-1j)*(-1j)**h;full=lambda w:walk(''.join(W[a]for a in w));words=('D','DC','V','VC','VCC','U','UC','UCC');q=-1+2j;g=-1+4j;r=4j;AA=5j;CUT=center(4j,2);assert CUT==1+9j
old=json.loads((R/'U_second_V_original_q_frontier_2026-10-24/original_q_frontier.json').read_text());rows=[z for z in old['remaining11_necessary_states']if z['true_preforeign_clock']==4];assert len(rows)==9
# Literal creator/full-tail geometry, not a changed contact-owner label.
uc=full('UC');assert(uc['p'],uc['h'])==(5j,3)and center(uc['p'],uc['h'])==CUT
u=full('U');assert(u['p'],u['h'])==(4j,0)
ud=full('UD');assert(ud['p'],ud['h'])==(1+5j,0)and center(ud['p'],ud['h'])==CUT
newstar={a+4j for a in L};K2={4j-a for a in K};assert newstar<=K2 and{4j,5j}<=K2
first=[]
for b in('V','VC','VCC'):
 rr=full(b);hist=lambda p:[(i,c)for i,(z,h,c)in enumerate(rr['reads'])if z==p]
 assert hist(0j)[-1]==(4,'R')and hist(1j)[-1]==(11,'R')and hist(-1)==[(1,'L')]
 # Full first P begins after plainU RAW28, so deleted g read is actual global29.
 assert 28+1==29
 first.append({'full_source':b,'fresh_r_R_tick0':4,'fresh_A_R_tick0':11,'g_only_read_tick0':1,'own_C_tails_preserve_all_three_statements':True})
mins=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text())
for k in('0:(0, 1)','1:(0, 1)'):
 z=mins['slots'][k];assert z['certified_minimum_C_age']==3 and z['unexcluded_counts_0_to_4'][:3]==[0,0,0]and len(z['rows'])==132
 assert all('OPEN'not in x['reasons_0_through_4'][:3]for x in z['rows'])
cleanup=[]
for b in('V','VC'):
 rr=full(b);p=8j-rr['p'];h=(2+rr['h'])%4;clock=2+b.count('C');assert(p,h,clock)==((-1+5j,2,2)if b=='V'else(-1+4j,1,3))
 cleanup.append({'word':b,'entry':[0,8,2],'exit':[*xy(p),h],'clock':clock})
continuations=[]
for b in words:
 rr=walk(''.join(W[a]for a in b)+M);head=-1+5j;rot=-1
 if b.startswith('D'):
  loc=(g-head)/rot;assert loc==1j and loc not in K and rr['req'][loc]is True;want=11
 else:
  loc=(q-head)/rot;assert loc==3j and rr['req'][loc]is True;want=23 if b.startswith('U')else 19
 hist=[(i,c)for i,(z,h,c)in enumerate(rr['reads'])if z==loc];assert hist[0]==(want,'L')
 owner=('next actual word RAW'if want>=len(''.join(W[a]for a in b))else'own C-tail 1 RAW'if want>=len(W[b[0]])else'own U-base RAW')
 rec=next(x for x in ref['plain_V_A_cleanup_all8_continuations']if x['next_full']==b)['guard'];key='first_input_L'if b.startswith('D')else'first_q_L';assert rec[key]['context_tick0']==want and rec[key]['owner']==owner
 # Different plain/C-tail ownership is material, not hidden marker execution.
 if owner=='next actual word RAW':assert rec[key]['owner_tick0']==1 and rec[key]['owner_read_number1']==2
 loc=(q-(-1+4j))/(-1j);assert loc==2 and rr['req'][loc]is False
 assert[(i,c)for i,(z,h,c)in enumerate(rr['reads'])if z==loc][0]==(8,'R')
 continuations.append({'next_full':b,'plain_cleanup_cut':('deleted_g_min3'if b.startswith('D')else'original_q_input'),'first_L_tick0':want,'owner':owner,'VC_cleanup_original_q_first_R_tick0':8})
maskrows=[]
for z in rows:
 a,b1,b2=z['foreign'],z['first'],z['second'];p=complex(*z['foreign_pose'][:2]);h=z['foreign_pose'][2];assert h==0 and b1 in'DVU'and b2=='V'
 prefix=full(a+b1);secondp=p+prefix['p'];secondh=(h+prefix['h'])%4;assert(secondp,secondh)==(4j,2)and center(secondp,secondh)==CUT
 ctx=walk(W[a]+W[b1]+W[b2]+M);loc=(r-p)/((-1j)**h);assert ctx['req'][loc]is False
 hist=[(i,c)for i,(pp,hh,c)in enumerate(ctx['reads'])if pp==loc];assert hist[0][1]=='R'
 target=next(t for t in ref['all9_exact_terminal_before_masks']if(t['foreign'],t['first'])==(a,b1));assert list(map(list,hist))==target['all_combined_r_reads']
 maskrows.append({'foreign':a,'first':b1,'actual_foreign_pose':z['foreign_pose'],'combined_r_initial_required_BLACK':False,'all_r_reads_tick0':hist})
assert len({(z['foreign'],z['first'])for z in maskrows})==9
out={'status':'PASS nine exact clock4 second-V residues excluded; closes old-U outgoing-source SECOND-contact branch only','manifest':sha(mf),'dependencies':ref['dependencies'],'actual_creator_and_first_D_repeated_center':xy(CUT),'following_U_genuine_star_in_second_entry_core':sorted(map(xy,newstar)),'first_V_family_histories':first,'all_age_A_law_cleanup_exits':cleanup,'all16_forced_full_continuation_checks':continuations,'nine_fresh_combined_before_masks':maskrows,'analytic_review':[
'All9 targets have actual first-returned endpoint center(1,9). Genuine creatorUC/UCC ownC1 and firstfollowingD/DC D-base already visit that center, so signed one-return simplicity excludes them. This is actual old vertex geometry, not replacing D ownership by C. PlainU is forced.',
'A firstfollowing U-family at(0,4,N), clock0, is a NEW genuine producer with new four source-R identities. The signed oneforeign+oneRAW current-pair transfer applies again to that subfactor; all four lie in actual secondV entryK. Equivalently true foreign age4 is below firststar-effect5, so foreignCTXmiss and fixed LEFT apply. This contradicts CURRENT-outsideK, not merely physical black. Hence firstfollowing packet is a genuine V/VC/VCC at(0,4,N).',
'Fresh literal histories verify r R4, A R11, and g(-1,4) physical L1/global29, with no own-tail rebirth. The signed all-age A law applies inside the actual simple old complete-eight factor, retaining full source tail clocks and true immediateVCC-toV adjacency. Its only first retirement/core absorption is V/VC(0,8,S), entryclock2.',
'PlainV cleanup ends(-1,5,S), clock2. AllD/DC next inputs require deletedg outside entryK, and therefore a genuine replacement residual birth. No old identity survives L29; every subsequent fullproducer entry clock is>=0. Exact produced-D input min3 conflicts with age<=2. Core-writing is not an export loophole: a current external input must be a full residual output, and any such producer after deletion also has entryclock>=0.',
'AllV/U next families instead absorb SAME-originalq, held CURRENT by the independently signed preforeign q guard. PlainV marker L19 and plainD markerL11 belong NEXT actual word tick1/read2; VC/DC ownCtail tick1/read2 and U ownL23 are separately preserved. No marker is physically executed early. Current residual absorption already violates held-currentness, and clock/heading ensures neither cleanup can directly be the targetforeign.',
'VC cleanup ends(-1,4,E), clock3; all8 nextfullpackets have actual common R8 at originalq, requiringWHITE while qBLACK. Standalone C is not inserted outside the retained fullpacket grammar; the VC consumer already includes its true ownCtail. This exhausts forced continuations, not a bounded search.',
'Thus originalA is CURRENT atforeignentry; preforeign r-lock keeps originalrBLACK there. Each exact full A+b1+secondV+actualfollowingM before-mask independently requires rWHITE. No A/r lifetime law is continued through foreign and no final mask is transplanted to arbitrary longer tails. This closes only the oldU outgoing-source second-contact branch; oldD/C/V sources and all-source second simplicity remain open.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
