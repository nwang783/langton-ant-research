from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'T_PORT7_ABSORBER_MANIFEST_V1_0e8dbf82.json';assert sha(MF)=='0e8dbf82450a2109fc466a200dab7ec181603179f2397a979d8889cb532abaed';mf=json.loads(MF.read_text())
for kind in ('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h
PR=D/'T_PORT7_PROVENANCE_RECONCILIATION.json';assert sha(PR)=='cae3dfd6e7e36b2a86f736b49cf3af53adf460442abec02d08c626c59dd52506'
for f,h in json.loads(PR.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'T_PORT7_ABSORBER_CHECKED.json').read_text());MJ=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());TJ=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text())
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,V,xy,future,phases,geometry,sim,cert,key=[ns[k]for k in('K','V','xy','future','phases','geometry','sim','cert','key')];enc=lambda q:sorted(map(xy,q));dec=lambda q:{complex(*p)for p in q};d=2+2j
W=sim(K,104)['word'];assert W==MJ['W'];Q,H,_,_=geometry(0j,1,W);assert Q[13]==2+1j and H[13]==0
B=set()
for i,p in enumerate(Q):
 q=p-Q[13]
 for k in range(-((int(q.imag)+27)//2),1 if i<13 else 0):B.symmetric_difference_update({q+k*d})
packet={a*d for a in(0,1,3,5,6,7)};assert not B&packet;kernel=B|packet;assert len(kernel)==190 and enc(kernel)==J['kernel']and enc(packet)==J['packet']
word=(D/'T_PORT7_RECOVERY_WORD.txt').read_text().strip();assert word==J['word']and len(word)==37440 and word[:6044]==TJ['T_recovery'][:6044]and(word[6044],TJ['T_recovery'][6044])==('L','R')
z=cert(sim(kernel,len(word),0j,0,word),J['tail_word']);assert z['tail']==W[92:]+W[:92];assert(z['p'],z['h'],z['d'])==(-32+34j,2,-2+2j)and enc(z['B'])==J['output_full_black']and z['tests']==J['infinite_parity_tests'];tq,_,_,_=geometry(z['p'],z['h'],z['tail'])
assert min(q.imag for q in z['pts']+tq)==-27 and (min(q.real for q in z['pts']),max(q.real for q in z['pts']),min(q.imag for q in z['pts']),max(q.imag for q in z['pts']))==(-34,37,-27,40)
C={q for i,q in enumerate(sorted(kernel,key=key))if-i-1 in z['dead']};assert len(C)==157 and enc(C)==J['whole_comparison_pruning']and max(max(abs(q.real),abs(q.imag))for q in C)==26==J['local_radius'];assert max(z['dead'][-i-1]for i,q in enumerate(sorted(kernel,key=key))if q in C)==36168
assert [z['first'][a*d]for a in(0,1,3,5,6,7)]==[0,124,672,5984,6000,6044]
assert [dict(cell=xy(q),time=z['first'].get(q))for q in sorted(kernel,key=key)]==J['initial_first_reads']and [dict(cell=xy(q),time=z['dead'].get(-i-1))for i,q in enumerate(sorted(kernel,key=key))]==J['initial_consumption_fates']
# Full actual/synthetic old-body bounds. No output cropping or west-archive import.
for row in J['interfaces']:
 lab=row['previous'];m=MJ['modes'][lab];old=dec(m['complete_output_black']);v=complex(*m['output_pose'][0]);phase=m['output_phase'];actual=max(q.imag for q in old);synthetic=v.imag+max(Q[i].imag-Q[phase].imag+(0 if i<phase else-2)for i in range(104));step=206 if lab=='S'else 228;guard=step-27
 assert actual==row['previous_full_output_max_y']and synthetic==row['omitted_synthetic_max_y']and guard==row['new_southern_boundary']and guard-max(actual,synthetic)==row['strict_slack']
 assert (max(actual,synthetic),guard)==((11,179)if lab=='S'else(31,201))and guard>max(actual,synthetic)
assert max(max(q.imag for q in K),max(q.imag for q in Q)-2)==6<201-27
controls=[];reads=0
for row in J['controls']:
 labs=list(row['prefix'])+['T7'];seed=set(K);seq='';p=0j;phase=0;pk=[]
 for lab,n in zip(labs,row['gaps']):
  assert n>=100;q=p+(n+int(13<phase))*d+Q[13]-Q[phase];tail=W[phase:]+W[:phase];seq+=tail*n+tail[:(13-phase)%104];inds=[0,1,3,5,6,7]if lab=='T7'else MJ['modes'][lab]['packet_black_indices'];bits={q+a*d for a in inds};assert not bits&seed;seed|=bits;pk.append(dict(mode=lab,origin=xy(q),time=len(seq),indices=inds))
  if lab=='T7':break
  mm=MJ['modes'][lab];seq+=mm['recovery_word'];p=q+complex(*mm['output_pose'][0]);phase=mm['output_phase']
 assert pk==row['packets']and enc(seed)==row['seed'];entry=len(seq);seq+=word;assert entry==row['entry']and hashlib.sha256(seq.encode()).hexdigest()==row['complete_word_sha256'];zz=cert(sim(seed,len(seq),expected=seq,cuts={entry}),z['tail']);field,p,h=zz['snap'][entry];assert(p,h)==(q,0)and{u-q for u in field if u.imag>=q.imag-27}==kernel
 assert sorted([[xy(u),i]for u,i in field.items()])==row['entry_full_black'];actual={u for u,i in field.items()if i in zz['dead']};assert actual=={q+u for u in C}and enc(actual)==row['entry_entire_pruning']
 for pkt in pk:
  oq=complex(*pkt['origin']);assert all(zz['first'][oq+a*d]>=pkt['time']for a in pkt['indices'])
  if pkt['mode']=='M':assert pkt['time']+9752 not in zz['dead']and all(not(pkt['time']<=i<pkt['time']+10712)for u,i in field.items()if i in zz['dead'])
 assert zz['first'][q+7*d]==entry+6044 and enc(zz['B'])==row['terminal_full_black']and[xy(zz['p']),zz['h']]==row['terminal_pose']and zz['tests']==row['parity_tests'];reads+=len(seq);controls.append(dict(modes=row['prefix']+'T7',reads=len(seq),seed=len(seed),relevant=len(actual),tail_checks=zz['tests']))
 if row['prefix']=='M'and row['gaps']==[100,100]:
  old=next(r for r in TJ['controls']if r['n']==100);oldB={complex(*p)for p,i in old['whole_contact_black']};assert set(field)^oldB=={q+7*d};assert len(actual&{complex(*p)for p in old['actual_entire_entry_pruning']})==99
oldC=dec(TJ['exact_entry_pruning']['local']);assert oldC<=C and len(C-oldC)==58 and 7*d in C-oldC and len((C-oldC)-{7*d})==57;contrast=J['contrast'];assert contrast['shared_local_count']==99 and contrast['T_only_local']==[]and enc(C-oldC)==contrast['T7_only_local']
assert json.loads(S.with_name('check_last_M_register_independent.json').read_text())['status'].startswith('PASS')
out=dict(status='PASS all-prefix first-extra-port7 southern absorber with exact157 local inputs',manifest=sha(MF),selected_manifest=MF.name,provenance_addendum=sha(PR),alternate_branch_proof_status='NOT REVIEWED OR SIGNED',script=sha(S),latest_M_signed_dependency=sha(S.with_name('check_last_M_register_independent.json')),kernel_mass=190,entire_pruning=157,pruning_radius=26,last_initial_consumption=36168,controls=controls,total_reads=reads,analytic_review=['Complete mature phase13 past above y=-27 is reconstructed as finite XOR of all earlier phase rays. The six paid packet cells are genuinely absent from that past. Full37440 literal reads and all infinite104 parity conditions certify NW future entirely above the boundary, retaining every arbitrary actual cell below it.','The original WHITE port7 is first read6044, and the BLACK alternative agrees on every earlier read. It is a different initially supplied board, not a mid-orbit modification. All six first-read times and all190 initial fates are independently reconstructed; exactly157 are future-consumed, all by36168, radius26.','For every preceding protectedS/M packet, actual complete output and omitted formal past have ymax11/31. At min gap100 the next southern guard is179/201, strictslack168/170; earlier packet bodies are farther southwest. The final canonical flight supplies the entire upperhalfplane and increasing gaps only separates it farther. This proves transfer for any finite protected prefix, not the five sample jobs. Arbitrary initial western archive is not covered.','No current input born in an earlierM recovery can be consumed by the terminalT7 future, since every such body is below its infinite southern guard. Whole entryC* is therefore exactly the translated157 local set. The now-signed latestM T branch gives99local+786remote when anM exists; in the two different boards port7 eliminates all786 remote inputs while adding57 existing local wake lifetimes and one new original bit. No single-orbit rho jump, permanence resurrection or free retirement claim follows.','Five full finite fields, all original input first reads, actual entryC*, complete terminal states and infinite futures replay. Exactlythis T7 terminal branch, not arbitrary extra ports, universal finite mode/register coverage or global attraction.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')));print(controls)
