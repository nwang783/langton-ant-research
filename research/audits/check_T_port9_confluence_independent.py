from pathlib import Path
import json,hashlib
S=Path(__file__);D=S.parents[1]/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'T_PORT9_SINGLE_EXTRA_MANIFEST.json';assert sha(MF)=='6266c400717005e0a901c61d586e59d41cebefd0a41466e5d56ed223da3c8a57';mf=json.loads(MF.read_text())
for kind in('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h,(f,sha(D/f),h)
J=json.loads((D/'T_PORT9_CONFLUENCE_CHECKED.json').read_text());MJ=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());TJ=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,xy,geometry,sim,cert,key=[ns[k]for k in('K','xy','geometry','sim','cert','key')];enc=lambda q:sorted(map(xy,q));dec=lambda q:{complex(*p)for p in q};d=2+2j;W=sim(K,104)['word'];Q,H,_,_=geometry(0j,1,W)
# Full mature southern field independently from every earlier phase ray.
B=set()
for i,p in enumerate(Q):
 q=p-Q[13]
 for k in range(-((int(q.imag)+15)//2),1 if i<13 else 0):B.symmetric_difference_update({q+k*d})
packet={a*d for a in(0,1,3,5,6,9)};assert not B&packet;kernel=B|packet;assert enc(kernel)==J['T9_kernel']and len(kernel)==118
word=(D/'T_PORT9_RECOVERY_WORD.txt').read_text().strip();assert word==J['T9_word']and len(word)==11336 and word[:6496]==TJ['T_recovery'][:6496]and(word[6496],TJ['T_recovery'][6496])==('L','R')
assert word[6600:]==TJ['T_recovery'][6516:]+TJ['T_tail_word'][:20]
zt=sim(kernel-{9*d},6516,0j,0,TJ['T_recovery'][:6516]);z9=sim(kernel,6600,0j,0,word[:6600]);assert(zt['p'],zt['h'])==(z9['p'],z9['h'])==(16+18j,2);patch=set(zt['B'])^set(z9['B']);add=set(z9['B'])-set(zt['B']);remove=set(zt['B'])-set(z9['B']);assert(len(patch),len(add),len(remove))==(23,18,5)
con=J['confluence'];assert enc(zt['B'])==con['complete_T_field']and enc(z9['B'])==con['complete_T9_field']and enc(patch)==con['patch']and enc(add)==con['added']and enc(remove)==con['removed'];assert(min(q.real for q in patch),max(q.real for q in patch),min(q.imag for q in patch),max(q.imag for q in patch))==(14,21,15,22)
old=cert(sim(zt['B'],len(TJ['T_recovery'])-6516,zt['p'],zt['h'],TJ['T_recovery'][6516:]),TJ['T_tail_word']);assert not patch&set(old['pts']);tq,_,_,_=geometry(old['p'],old['h'],old['tail']);raychecks=0
for p in patch:
 for q in tq:
  u=p-q;dd=old['d'];raychecks+=1
  assert not(u.real%dd.real==0 and u.imag==int(u.real//dd.real)*dd.imag and u.real//dd.real>=0)
z=cert(sim(kernel,len(word),0j,0,word),J['T9_tail_word']);assert z['tail']==W[85:]+W[:85]and(z['p'],z['h'],z['d'])==(-34-10j,2,-2-2j)and len(z['B'])==820 and enc(z['B'])==J['T9_output_black']and z['tests']==J['T9_parity_tests'];tq,_,_,_=geometry(z['p'],z['h'],z['tail']);assert min(q.imag for q in z['pts'])==-15
C={q for i,q in enumerate(sorted(kernel,key=key))if-i-1 in z['dead']};oldC=dec(TJ['exact_entry_pruning']['local']);assert C==oldC|{9*d}and len(C)==100 and enc(C)==J['local_T9_pruning']and max(max(abs(q.real),abs(q.imag))for q in C)==18
first={}
for i,q in enumerate(z['pts']):
 if q.real==q.imag and q.real>=0 and q.real%2==0:first.setdefault(int(q.real)//2,i)
# SW displacement preserves x-y, so no missed diagonal phase may later meet the input ray.
assert all(q.real!=q.imag for q in tq);assert set(first)==set(range(11))and first[9]==6496 and first[10]==6540 and sorted([[a,t]for a,t in first.items()])==J['T9_ray_first_reads']
# Retained registered future has exact quadrant bounds; the patch is strictly east for every D>=114.
base=TJ['controls'][0];baseM=202+201j;remote={q-baseM for q in dec(TJ['exact_entry_pruning']['remote'])};baseQ={q-baseM for q in dec(base['whole_post_event_black'])if q.real<=baseM.real+38 and q.imag>=baseM.imag-43};assert enc(remote)==J['remote_last_M_pruning']and len(remote)==786 and enc(baseQ)==J['registered_quadrant']
post=TJ['postcollision_word'];pp,_,ep,eh=geometry(5+28j,1,post);tail=base['complete_future_certificate']['tail_word'];pt,_,_,_=geometry(ep,eh,tail);assert(ep,eh)==(-47+14j,1)and max(q.real for q in pp+pt)==38 and min(q.imag for q in pp+pt)==-43 and 2*114+min(q.real for q in patch)>38
# Local half-plane transfer, previously independently signed, keeps both actual and omitted-past bodies below.
for lab,m in MJ['modes'].items():
 v=complex(*m['output_pose'][0]);phase=m['output_phase'];actual=max(q.imag for q in dec(m['complete_output_black']));synthetic=v.imag+max(Q[i].imag-Q[phase].imag+(0 if i<phase else-2)for i in range(104));step=206 if lab=='S' else 228;assert step-15>max(actual,synthetic)
controls=[];reads=0
for row in J['controls']:
 labels=list(row['prior_modes'])+['T9'];seed=set(K);seq='';p=0j;phase=0;packets=[]
 for lab,n in zip(labels,row['gaps']):
  assert n>=100;q=p+(n+int(13<phase))*d+Q[13]-Q[phase];w=W[phase:]+W[:phase];seq+=w*n+w[:(13-phase)%104];inds=[0,1,3,5,6,9]if lab=='T9'else MJ['modes'][lab]['packet_black_indices'];bits={q+a*d for a in inds};assert not seed&bits;seed|=bits;packets.append(dict(mode=lab,origin=xy(q),time=len(seq),indices=inds))
  if lab=='T9':break
  m=MJ['modes'][lab];seq+=m['recovery_word'];p=q+complex(*m['output_pose'][0]);phase=m['output_phase']
 assert packets==row['packets']and enc(seed)==row['seed'];entry=len(seq);qT=q;seq+=word;lastM=next((a for a in reversed(packets)if a['mode']=='M'),None);event=None
 if lastM:
  qM=complex(*lastM['origin']);delta=qT-qM;dd=int(delta.real)//2;assert delta==dd*d and dd>=114;seq+=z['tail']*(dd-21)+z['tail'][:80];event=len(seq);assert event-entry==104*dd+9232;seq+='L'+post
 assert seq==row['complete_word']and len(seq)==row['terminal_cut']and entry==row['T_contact']and event==row['marked_event'];zz=cert(sim(seed,len(seq),expected=seq,cuts={entry}|({event,event+1}if event is not None else set())),row['tail_word']);field,p,h=zz['snap'][entry];assert(p,h)==(qT,0)and{u-qT for u in field if u.imag>=qT.imag-15}==kernel and sorted([[xy(u),i]for u,i in field.items()])==row['T_full_black']
 actualC={u for u,i in field.items()if i in zz['dead']};expect={qT+u for u in C}
 if lastM:
  expect|={qM+u for u in remote};bf,p,h=zz['snap'][event];assert(p,h)==(qM+4+28j,2)and bf[p]==lastM['time']+9752 and zz['dead'][bf[p]]==event and enc(bf)==row['event_full_black'];aft,p,h=zz['snap'][event+1];inside={u-qM for u in aft if u.real<=qM.real+38 and u.imag>=qM.imag-43};assert inside==baseQ and enc(inside)==row['post_event_quadrant']and(p,h)==(qM+5+28j,1)and(zz['p'],zz['h'],zz['d'])==(qM-47+14j,1,-2+2j);assert zz['tail']==tail and len(actualC)==886
 else:assert len(actualC)==100 and zz['tail']==z['tail']and zz['d']==-2-2j
 assert actualC==expect and enc(actualC)==row['T_entire_pruning'];rho=max(max(abs((u-qT).real),abs((u-qT).imag))for u in actualC);assert rho==row['T_entire_radius']==(2*dd+44 if lastM else 18)
 for a in packets:
  oq=complex(*a['origin']);assert all(zz['first'][oq+k*d]>=a['time']for k in a['indices'])
 assert enc(zz['B'])==row['terminal_full_black']and[xy(zz['p']),zz['h']]==row['terminal_pose']and xy(zz['d'])==row['tail_drift']and zz['tests']==row['parity_tests'];reads+=len(seq);controls.append(dict(modes=row['prior_modes']+'T9',seed=len(seed),reads=len(seq),relevant=len(actualC),event=event,rho=int(rho)))
assert reads==644854
O={'status':'PASS exact T9 finite confluence and complete single-extra ORIGINAL-ray cover','manifest':sha(MF),'script':sha(S),'T7_selected_audit':sha(S.with_name('check_T_port7_absorber_independent.json')),'T7_selected_proof':'V1_0e8dbf82 plus provenancecae3dfd6, not alternate branch proof','kernel_mass':118,'canonical_phase':85,'confluence_patch':{'size':23,'added':18,'removed':5,'infinite_ray_systems':raychecks},'local_pruning':100,'remote_pruning':786,'controls':controls,'full_reads':reads,'analytic_review':['Independent whole mature y>=-15 XOR field and11336 actual reads give118 input cells,820 output cells, explicit canonicalW phase85 SW future and exact100 initial future-consumed lifetimes. No merely period104-to-canonical inference.','At cuts6516/6600 the complete fields have identical pose16,18,S and exactly23 signed differences18add/5remove. Every remaining finite read and2392 infinite ray systems misses that patch. The84 extra steps therefore delay the actual full future without deleting archive.','For any protected finite S/M prefix and D>=114, the entire later registered future lies x<=qM+38 while every new patch point lies x>=qT+14>=qM+242. The already signed latest-M first-event/quadrant theorem therefore transfers unchanged, including older outputs, the SAME R9752 identity, full postL field and48464 continuation. This is not inference from ideal word agreement or finite samples.','Entire T9 entry pruning is the independently reconstructed100 local set plus exactly the same786 latest-M set when present. Extra earlier input lifetimes are not silently removed. Six complete original seeds644854 reads reconstruct every contact/terminal field, original first reads and infinite tails.','At mostONE extra initially BLACK ray indexa>=7, with lower colors includingWHITE2/4 fixed, has exhaustive cases7,8,9 or>=10neverread. This combines separately signed T7,T8,T9 and whole T exposure, not arbitrary seed perturbations. Additional finite indices>=19 are separately neverread by all four selected complete futures. Arbitrary simultaneous multiple near extras, western archives, autonomous recurrence and universal capture remain unclaimed.']}
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
