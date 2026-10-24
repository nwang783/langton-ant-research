from pathlib import Path
from itertools import combinations
import random,json,hashlib,sys
R=Path(__file__).resolve().parents[1];G=R/'global_architecture_2026-10-23';sys.path.insert(0,str(G));import bulk_black_deficiency as tested
assert hashlib.sha256((G/'bulk_black_deficiency.py').read_bytes()).hexdigest()=='fe2c418e60a947fc4a52118df3435568e5416e096aeed74361a848fafe4fb582'
rng=random.Random(231305);cases=0
for trial in range(1000):
 b=rng.randrange(8);norms=[rng.randrange(-5,6)for _ in range(b)];cs=[]
 for i in range(rng.randrange(11)):
  lo=rng.randrange(-7,8);hi=lo+rng.randrange(6);mask=sum(1<<j for j,n in enumerate(norms)if lo<=n<=hi and rng.randrange(2));cs.append(dict(band=[lo,hi],cover_mask=mask,polluted_white=[]if rng.randrange(3)else[0]))
 best=0
 for bits in range(1<<len(cs)):
  used=[i for i in range(len(cs))if bits>>i&1]
  if any(cs[i]['polluted_white']for i in used):continue
  if any(max(cs[i]['band'][0],cs[j]['band'][0])<=min(cs[i]['band'][1],cs[j]['band'][1])for i,j in combinations(used,2)):continue
  union=0
  for i in used:union|=cs[i]['cover_mask']
  best=max(best,union.bit_count())
 got=tested.interval_black_deficiency(cs,norms);assert got['maximum_standard_covered']==best and got['black_deficiency']==b-best;cases+=1
bad=[([dict(band=[1,2],cover_mask=1,polluted_white=[])],[0]),([dict(band=[0,2],cover_mask=2,polluted_white=[])],[0]),([dict(band=[2,1],cover_mask=0,polluted_white=[])],[])]
for cs,ns in bad:
 try:tested.interval_black_deficiency(cs,ns)
 except ValueError:pass
 else:raise AssertionError('malformed physical profile admitted')
records=[]
for name in('generic_bulk_P108','forward108_bulk_author','generic_bulk_standard','generic_bulk_odd_LR','generic_bulk_odd_scale3','generic_bulk_reverse_scale4','generic_bulk_standard_scale4'):
 j=json.loads((G/(name+'.json')).read_text());r=tested.supplied_profile_deficiency(j);records.append([name,r['status'],r.get('black_deficiency')])
 if name=='generic_bulk_P108':assert r['black_deficiency']==11
 if name=='forward108_bulk_author':assert r['black_deficiency']==3
 if name=='generic_bulk_standard':assert r['black_deficiency']==0
out=dict(status='PASS independent exhaustive physical interval-union optimum controls',source_sha256=hashlib.sha256((G/'bulk_black_deficiency.py').read_bytes()).hexdigest(),note_sha256=hashlib.sha256((G/'bulk_black_deficiency_lemma.md').read_bytes()).hexdigest(),exhaustive_cases=cases,malformed_rejections=len(bad),retained_instances=records,scope='Exact relaxed white-clean standard-bundle coverage deficit, not attained minimum fuel. Multiplying the signed good-level count by delta is a necessary preparation bound only; no general nonstandard preparation or global budget.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
