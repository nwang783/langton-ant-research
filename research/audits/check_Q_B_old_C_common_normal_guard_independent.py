from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';p=SELF.with_name('check_returned_V_source_reduction_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
W,M,walk,xy,raw,I,O=[ns[k]for k in('W','M','walk','xy','raw','I','outputs')];names=['D','DC','V','VC','VCC','U','UC','UCC']
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,s.split()[:8])) for s in CP.read_text().splitlines()}
roles=[];young=[];reasons=Counter()
for n,j in [('DC',1),('VC',1),('VCC',1),('VCC',2),('UC',1),('UCC',1),('UCC',2)]:
 prefix=W[n[0]]+W['C']*(j-1);tr=walk(prefix);p,h=tr['p'],tr['h'];q=p+2*(-1j)**h
 assert q in O[n];occ=[(i,c) for i,(z,hh,c) in enumerate(raw[n]['reads']) if z==q];assert occ[-1]==(len(prefix)+8,'R')
 roles.append((n,j,xy(p),h,xy(q),occ[-1]))
 for age in range(3):
  fullage=age+j-1;hh=(h-age)%4
  for ci,cn in enumerate(names):
   for v in I[cn]:
    entry=q-v*(-1j)**hh;key=(names.index(n),ci,*xy(entry),hh,*xy(q),fullage)
    reason='sector' if(int(entry.real+entry.imag)+hh)%2 else 'incomplete' if n.count('C')>fullage else 'COUNT5'
    if reason=='COUNT5':assert key in COUNT
    young.append((n,j,age,key,reason));reasons[reason]+=1
assert len(young)==483 and reasons=={'sector':280,'incomplete':76,'COUNT5':127}
exits=[];steps=[]
for n in ['D','V','U']:
 step=raw[n]['p']*(-1j);steps.append((n,xy(step),int(step.real+step.imag)));assert step in [1-1j,3-1j,4]
 for v in I[n]:
  entry=2-v*(-1j);end=entry+step;normal=int(end.real+end.imag);assert normal>=1
  first=next((i,c)for i,(q,hh,c)in enumerate(ns['ctx'][n]['reads'])if q==v);assert first[1]=='L'
  owner=('own RAW',first[0],first[0]+1)if first[0]<len(W[n])else('next actual word',first[0]-len(W[n]),first[0]-len(W[n])+1)
  exits.append((n,xy(v),xy(entry),xy(end),normal,owner))
assert len(exits)==8;mini=[z for z in exits if z[4]==1];assert len(mini)==3 and all(z[3]==(2,-1)for z in mini)
checks=[]
for n,p,tick in [('Q',4-5j,53),('B',5-4j,63)]:
 local=(2-p)*1j;tr=walk(W[n]);first=next((i,c)for i,(q,hh,c)in enumerate(tr['reads'])if q==local);assert first==(tick,'R')
 if n=='Q':assert p.real+p.imag==-1
 else:assert p-(2-1j)==3*(1-1j)
 checks.append((n,xy(p),xy(local),first))
f=walk(W['F']+W['C']+M);assert (2-(2-5j))*1j not in f['req']
mp=D/'Q_B_old_C_common_normal_guard_manifest.json';mf=json.loads(mp.read_text());mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='fd25e1ae3e8e5cf54c9dfc3f0d5421656c791db7a36dec692719ab6ba178abb8'
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in mf['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS target-level C76/C77 common-current-output normal guard','manifest_sha256':mh,'fresh_seven_source_roles':roles,'fresh_483_young_queries':young,'query_counts':dict(reasons),'fresh_all_eight_age3_plain_E_exits':exits,'E_steps':steps,'foreign_first_reads':checks,'analytic_review':[
'Each of seven actual containing full sources exports the old C common cell as a genuine fresh O identity. Its last actual read is exactly own C tick8/read9, including C2 roles and preservation by any subsequent own tail. Full-entry age is atomic age+j-1; every possible earlier full consumer is sector-inactive, before genuine full source completion, or an exact signed COUNT5 exclusion.',
'The first retiring full consumer, if any before the age-three foreign, must enter at age3 headingE and complete by that same clock. Positive-tail packets cannot do so. Earlier full consumers whose physical retirement occurs in a tail or following marker were already included using their true full entry, so no boundary-absorption exception is dropped.',
'All eight plain D/V/U true inputs, including three marker-owned inputs, have physical full RAW exits with x+y>=1. Subsequent zero-C E steps change x+y by0,2,4. Q target normal-1 is unreachable. B normal1 forces one of three common exits(2,-1) followed by exactlyD^3, so its actual last preceding packet isD, contradicting the independently signed required plainU predecessor.',
'These endpoint contradictions also cover a hypothetical marker-owned consumer immediately before the foreign: no candidate exits at the foreign entry. No physical L is incorrectly assigned to the old packet; D/V/U marker-only reads remain next-word tick1/read2.',
'Without a first fullconsumer the same source identity is BLACK at foreign entry, while the FIRST foreign reads at Q53/B63 requireWHITE. No earlier foreign toggle repairs it, and no postforeign maturation law is used. F plus returnedC context misses the cell and is explicitly not excluded.'
],'scope':mf['scope'],'remaining_coarse_labels':[15,30,75],'dependencies':mf['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],dict(reasons))
