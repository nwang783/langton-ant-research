from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'returned_D_last_C_parent_reduction_2026-10-24';p=SELF.with_name('check_returned_V_source_reduction_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
W,M,walk,xy,raw,I,O,K=[ns[k]for k in('W','M','walk','xy','raw','I','outputs','K')];names=['D','DC','V','VC','VCC','U','UC','UCC'];author=json.loads((D/'D_last_C_parent_reduction.json').read_text());refs={(r['catalogue_id'],r['last_positive_C_full_packet'],r['actual_pre_D_zero_C_word']):r for r in author['all40_actual_last_positive_C_interfaces']};rows=[];counts=Counter();bud=[]
fences={(15,'DDD'),(15,'V'),(30,'DD'),(15,'DD'),(30,'D')}
for ix,runs in[(15,['','D','DD','DDD','V']),(30,['','D','DD'])]:
 for parent in['DC','VC','VCC','UC','UCC']:
  h=parent.count('C');r0=raw[parent];assert(r0['h']+h)%4==0
  for run in runs:
   r=walk(''.join(W[a]for a in run));p=-r['p']-r0['p']*(-1j)**h;ref=refs[ix,parent,run];assert[ *xy(p),h]==ref['packet_entry']
   seq=parent+run+'D';test=walk(''.join(W[a]for a in seq)+M)
   if not test['feasible']:kind='literal';detail={'tick0':test['i'],'cell':xy(test['q'])}
   elif ix==30 and not run:assert parent in['DC','VC','UC'];kind='prior_C_guard';detail=None
   elif parent=='UCC':assert(ix,run)==(15,'V');kind='UCC_V_guard';detail=None
   elif parent=='UC'and(ix,run)in fences:kind='current_fence';detail=None
   elif parent=='UC':
    assert ix==15 and run in['','D'];tag=p+(1+3j)*(-1j)**h;goal=2-5j;local=(tag-goal)*1j;tr=walk(W['F']+W['C']+M);fr=walk(W['F']);assert not tr['req'][local]and local not in fr['req']and local not in K
    first=next((i,c)for i,(q,hh,c)in enumerate(tr['reads'])if q==local);assert first[1]=='R';tick=first[0]-len(W['F']);owner=('returnedC',tick,tick+1)if tick<len(W['C'])else('following_actual_word',tick-len(W['C']),tick-len(W['C'])+1)
    assert owner==(('returnedC',12,13)if not run else('following_actual_word',7,8));bud.append((run,xy(p),xy(tag),first,owner));kind='UC_bud';detail=owner
   else:assert parent in['DC','VC'];kind='necessary_open';detail=None
   counts[kind]+=1;rows.append((ix,parent,run,xy(p),h,kind,detail))
assert len(rows)==40 and counts=={'literal':15,'UCC_V_guard':1,'prior_C_guard':3,'current_fence':5,'UC_bud':2,'necessary_open':14}
remain={(ix,p,r)for ix,p,r,_,_,kind,_ in rows if kind=='necessary_open'};assert remain=={(15,p,r)for p in['DC','VC']for r in['','D','DD','DDD','V']}|{(30,p,r)for p in['DC','VC']for r in['D','DD']}
# Reconstruct the exact UC full-source original base bud queries, no shifted atomic clock.
slot=1+3j;assert slot in O['UC'];assert[(i,c)for i,(q,h,c)in enumerate(raw['U']['reads'])if q==slot]==[(i,c)for i,(q,h,c)in enumerate(raw['UC']['reads'])if q==slot]
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};queries=[];qc=Counter()
for age in range(5):
 h=(-age)%4
 for ci,cn in enumerate(names):
  for v in I[cn]:
   p=slot-v*(-1j)**h;key=(6,ci,*xy(p),h,*xy(slot),age);reason='sector'if(int(p.real+p.imag)+h)%2 else'COUNT5'
   if reason=='COUNT5':assert key in COUNT
   qc[reason]+=1;queries.append((key,reason))
assert qc=={'sector':63,'COUNT5':52}
mp=D/'manifest.json';mf=json.loads(mp.read_text());mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='1905984f564c64c2377b45c50bb5bf7965a79560fd9fcab8431ebb22962bd106'
for f in mf['files']:assert hashlib.sha256((D/f['file']).read_bytes()).hexdigest()==f['sha256']
for f,h in author['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS40 actual last-positive-C D interfaces reduce to14 necessaryDC/VC cases','manifest_sha256':mh,'fresh40_interfaces':rows,'classification_counts':dict(counts),'two_actual_UC_original_bud_WHITE_reads':bud,'fresh115_UC_bud_queries':queries,'query_counts':dict(qc),'analytic_review':[
'The independently signed Jordan horizon supplies the EXISTENCE of the real last positive-C fullpacket and only the displayed short zero-C N words. Fresh literal full endpoints solve each of40 actual parent poses; no earlier history is bounded or recursively given these same constraints.',
'All15 literal cuts are checked on the necessary parent+Nrun+selectedD+actualM11 prefix. This is valid for either selected fullD or ownDC base: the real following raw word suppliesM11. Passing this prefix is not a positive foreign-return control.',
'The other fixed cuts use their independently signed scopes exactly: UCC,V only; any immediate priorC for all three empty-run D30 cases; and the five specific current-star/intact-cycle support fences. The superseded specificVC note is not used.',
'The two remaining UC rows have the same genuine full-source-to-foreign age4, since the optional D adds no C. Fresh all115 sourceUC base-bud input queries give63 sector/52 COUNT5, preserving the same original output. Its ownC tail does not revisit it. F RAW misses this current cell, and the combined actual suffix first requiresWHITE: returnedC tick12/read13 for empty run, but FOLLOWING actual word tick7/read8 for oneD. This owner distinction is explicitly retained, with no postforeign lifetime law.',
'ExactlyD15 ten DC/VC x empty,D,DD,DDD,V andD30 four DC/VC x D,DD remain. They are necessary interfaces only, not attained histories, all-target exclusion, a recursive parent law, or returned simplicity.'
],'scope':mf['scope'],'dependencies':author['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
