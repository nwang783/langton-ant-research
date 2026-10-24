from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'F_D15_V_rail_C_cohort_lock_2026-10-24';p=SELF.with_name('check_F_first_C_cohort_lock_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('suffixcuts=[]')[0],ns)
W,M,walk,xy,raw,I,O,K,ctx,mins=[ns[k]for k in('W','M','walk','xy','raw','I','O','K','ctx','mins')]
F=2-5j;cp=-2-3j;tags={'T':-2-5j,'Q':-1-5j};births=[];south=[];west=[];east=[];last=[];cnt=Counter()
for n in['DC','VC']:
 source=-1-3j-raw[n]['p']*(-1j);assert source+raw[n[0]]['p']*(-1j)==cp
 assert -1-3j+raw['V']['p']==0
 for label,tag in tags.items():
  v=(tag-source)*1j;assert v in O[n];firstCslot=(tag-cp)*1j;assert firstCslot==({'T':2,'Q':2+1j}[label])
  occ=[(t,c)for t,(q,h,c)in enumerate(raw[n]['reads'])if q==v];assert occ[-1]==(len(W[n[0]])+{'T':8,'Q':7}[label],'R');births.append((n,xy(source),label,xy(v),occ[-1],-1,-1,0))
for n in['V','VC']:
 entry=tags['Q']-3j*1j;assert entry==2-5j and entry.imag<2;west.append((n,xy(entry),mins[n,3j]))
for label,tag in tags.items():
 for n in['D','V','U']:
  for slot in I[n]:
   entry=tag+slot;end=entry-raw[n]['p'];assert end.imag<=tag.imag and end.imag-2<F.imag;south.append((label,n,xy(slot),xy(entry),xy(end),int(end.imag-2)))
held=set()
for label,tag in tags.items():
 for n in['D','V','U']:
  for slot in I[n]:
   entry=tag-slot*(-1j);end=entry+raw[n]['p']*(-1j);hit=held&{entry+q*(-1j)for q in ctx[n]['req']};minimum=mins[n,slot]
   if(int(entry.real+entry.imag)+1)%2:reason='sector'
   elif minimum>4:assert minimum==5;reason='upper_min5'
   elif hit:reason='prior_current'
   else:
    assert label=='T'and n=='U'and end==1-6j and end.imag<F.imag;reason='endpoint'
   cnt[reason]+=1;east.append((label,n,xy(slot),minimum,xy(entry),xy(end),reason,sorted(map(xy,hit))))
 held.add(tag)
for n,label in[('V','Q'),('U','T')]:
 entry=F-raw[n]['p']*(-1j);local=(tags[label]-entry)*1j;assert local in K and ctx[n]['req'][local]
 first=next((t,c)for t,(q,h,c)in enumerate(raw[n]['reads'])if q==local);assert first==((5,'L')if n=='V'else(0,'L'));last.append((n,xy(entry),label,xy(local),first))
assert len(east)==len(south)==16 and len(west)==len(last)==2
cuts=[]
for n in['DC','VC','VCC','UC','UCC']:
 x=walk(''.join(W[c]for c in n)+W['F']+M);assert not x['feasible'];cuts.append((n,x['i'],xy(x['q'])))
assert not walk(W['C']+W['U']+M)['feasible']and walk(W['C']+W['F']+M)['feasible']
# Literal translation of the actual earlier plain D for DD/DDD; no word substitution.
long=[]
for n in['DC','VC']:
 for nd in(2,3):
  source=-nd-nd*1j-raw[n]['p']*(-1j);oldC=source+raw[n[0]]['p']*(-1j);anchor=-1-1j;k=nd-1
  assert oldC-anchor==-k-1-k*1j and F-anchor==3-4j
  assert source+raw[n]['p']*(-1j)+(nd-1)*raw['D']['p']==anchor
  tagold=[oldC+q*(-1j)for q in(2,2+1j,1+2j)];tagnew=[q-anchor for q in tagold];assert tagnew==[-k-1-(k+2)*1j,-k-(k+2)*1j,1-k-(k+1)*1j]
  long.append((n,'D'*nd,xy(source),xy(anchor),xy(oldC-anchor),k,list(map(xy,tagnew)),xy(F-anchor),'actual_contact_remains_later_D'))
# Eight source-typed empty/oneD lifts of the older ORIGINAL-bud first-consumer lemma.
short=[]
for n in['DC','VC']:
 for nd in(0,1):
  anchor=-nd-nd*1j;source=anchor-raw[n]['p']*(-1j);slot=2 if n=='DC'else 2+2j;tag=source+slot*(-1j);assert tag-anchor==-2-1j
  assert source+raw[n]['p']*(-1j)==anchor
  normalizedF=F-anchor;local=(tag-F)*1j;tr=walk(W['F']+W['C']+M);assert local not in walk(W['F'])['req']and local not in K and not tr['req'][local]
  first=next((t,c)for t,(q,h,c)in enumerate(tr['reads'])if q==local);assert first==((68,'R')if nd==0 else(78,'R'))
  owner=('returnedC',12,13)if nd==0 else('following_actual_word',7,8)
  for chosen in['D','DC']:
   short.append((n,'D'*nd,chosen,xy(anchor),xy(source),xy(tag),xy(normalizedF),xy(local),first,owner,0,1,4))
assert len(long)==4 and len(short)==8
manifests=[(D/'manifest.json','d005eb49404de804e70ec09e65276f6e4741fef0d731b5d3dea399d546c7342d'),(R/'D15_long_D_run_local_gate_lift_2026-10-24/manifest.json','372a183dff5cf5f23f4d878c70a12a6f43215684a832c64c81dc36473819d041'),(R/'seven_word_spatial_return_2026-10-23/D15_empty_D_older_bud_lifts_manifest.json','aa285e603a9b0fed0bf64ebcb1f3e28b59c3ad2813cfda22afc77a9552ca6596')];bound={}
for mp,mh in manifests:
 assert hashlib.sha256(mp.read_bytes()).hexdigest()==mh;mf=json.loads(mp.read_text());bound[str(mp.relative_to(R))]=mh
 files=mf['files'].items()if isinstance(mf['files'],dict)else[(x['file'],x['sha256'])for x in mf['files']]
 for f,h in files:assert hashlib.sha256((mp.parent/f).read_bytes()).hexdigest()==h
 for f,h in mf.get('dependencies',{}).items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
for filename in['check_C75_immediate_ancestor_bud_independent','check_F_first_C_cohort_lock_independent']:
 p=SELF.with_name(filename+'.json');bound[filename]=hashlib.sha256(p.read_bytes()).hexdigest()
out={'status':'PASS three complementary guards eliminate all10 remaining D15 parent/run interfaces, subject to signed horizon; no post-return iteration','bound_manifests_and_independent_dependencies':bound,'V_run_four_source_tag_roles':births,'V_run_S16':south,'V_run_W2':west,'V_run_E16':east,'V_run_E_counts':dict(cnt),'V_run_last_core2':last,'actual_full_tail_F_conflicts':cuts,'four_genuine_longD_gate_lifts':long,'eight_source_typed_empty_oneD_bud_lifts':short,'analytic_review':[
'The D15 V-run case reconstructs a genuine FIRST C(-2,-3,E) of DC/VC, exit(-1,-3,N), then actualplainV to selectedD0N. FreshT/Q fulloutputs at(-2,-5)/(-1,-5), atomic/full entryclock-1, exit0 and foreign3 preserve exactly the signed maturity distinctions. Vupper0,3 has minimum2; Uupper5 is excluded atfullage4. All16S/16E/2W/2core obligations are independently reconstructed. The unique E firstT lower-a consumer ends(1,-6), already belowF; Q meets already-currentT. Mandatory full-tail/F and rawC/U conflicts give the additional E vertical drop, while rawCF remains feasible.',
'The no-first-core-capture argument is the same precise fullI proof as the signed cohort lock: any first later entryK absorption of a current original must be a BLACK before-context input of the preceding full old packet, including its actual marker-only owner. It is not an assumption that residual-only output masks cover arbitrary fresh core writes. Thus neither required lastV norU can have its actualK, independent of returned reader/contact owner.',
'For DD/DDD the earlier D at(-1,-1,N) is an ACTUAL plain packet. Translating by(1,1) gives precisely the already signedk1/k2 FIRST-C cohort and F3,-4 at the sameCclock3. All original tags and words are unchanged. The actual first-contact owner remains the later outgoingD, not an inventedC1. This valid BEFORE-F predicate lift does not contradict the earlier failed same-contact-map assessment.',
'For empty/oneD runs, the independently signed849d first-consumer lemma uses ONLY the prior real DC/VC full output, fullage4 deadline and the actual olderD/C chords. It does not use a selectedD ownC, a returnedV/C input, or C75 ownership. The four surviving V/VC consumer candidates are excluded by the same preforeign U-entry strict midpoint crossings. Translating the oneD case to its actual earlierplainD preserves all230 query premises and clocks.',
'Fresh actual suffix masks establish the needed different WHITE premises: emptyrun firstR68 belongs to returnedC12/read13; onerun firstR78 belongs to following actualword7/read8. FRAW misses the current original in both. Both chosen selectedfullD/DC types are retained in eight typed rows. Existing genuine finite clearing controls remain valid outside U-entry simplicity, so no source-free permanence theorem is claimed.',
'Under the signed D15 lastC horizon these scopes partition all10 parent/run rows: two V, four DD/DDD, four empty/D. Combined with previously signed D30/C75 elimination they close the coarse first-returned-contact frontier. A separate geometric assembly should state the precise first-returned-atom simplicity consequence; no second returned packet or secondforeign extension follows automatically.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(dict(cnt))
