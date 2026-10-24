"""Reconstruct universal U input birth covers and every four-output cohort."""
import itertools,json,hashlib,collections
from pathlib import Path
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/u_middle_origin_frozen_20261023_1013';j=json.loads((B/'02_u_middle_input_origin_order.json').read_text())
manifest=json.loads((B/'manifest.json').read_text())
for f in manifest['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
for f in manifest['dependencies']:
 p=ROOT/f['file'];p=p if p.exists()else ROOT/'core_periodicity_new'/f['file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
ids=(0,1,4,5,6,7,8,9);K={z for z,b in walk(mark)[2].items()if b};G={}
for a in ids:
 e,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,b in req.items()if b};core={e+rotation(z,h)for z in K};O=(black^flip)-core;I=black-K
 G[a]=(I,sorted(O,key=xy),req,{z:b^(z in flip)for z,b in req.items()},core)
I=G[7][0];assert all(G[a][0]==I for a in(8,9));q=-1+2j;P=sorted(I-{q},key=xy)
def producers(z,protected):
 rows={}
 for a in ids:
  for oi,o in enumerate(G[a][1]):
   for h in range(4):
    p=z-rotation(o,h)
    if(sum(xy(p))+h)%2:continue
    hits=tuple(sorted((xy(t)for t in protected if rotation(t-p,-h)in G[a][2])))
    rows[a,*xy(p),h,oi]=hits
 assert len(rows)==136
 return rows
def recorded(rows):return {(r['packet'],*r['head'],r['output_index']):tuple(map(tuple,r['context_hits']))for r in rows}
can=producers(q,P);assert can==recorded(j['canonical_producers'])
covers=[]
for n in range(1,5):
 for c in itertools.combinations(P,n):
  C=set(map(xy,c))
  if all(C&set(h)for h in can.values())and not any(set(d)<=C for d in covers):covers.append(sorted(C))
assert covers==j['minimal_producer_cover_sets']or sorted(covers)==sorted([list(map(tuple,c))for c in j['minimal_producer_cover_sets']])
records={};maximum=0
for a in ids:
 _,O,req,post,core=G[a];O=set(O)
 poses={(o-rotation(v,h),h)for o in O for v in I for h in range(4)}
 for p,h in poses:
  if(sum(xy(p))+h)%2:continue
  target={p+rotation(v,h)for v in I};cohort=O&target;maximum=max(maximum,len(cohort))
  if len(cohort)<4:continue
  assert len(cohort)==4;z,=target-cohort
  origin='unseen_possible_older_residual'if z not in post else 'post_core_nonresidual'if post[z] else 'known_white'
  assert origin!='post_core_nonresidual'or z in core
  candidates=producers(z,cohort);safe=sum(not v for v in candidates.values());outcome='not_excluded_by_this_static_test'if safe else 'excluded_all_ages'if z in post else 'older_identity_required'
  records[a,*xy(p),h]=(cohort,z,rotation(z-p,-h),origin,outcome,candidates,safe)
assert maximum==4 and len(records)==24
counts=collections.Counter(v[4]for v in records.values())
classified={k:v[4]for k,v in records.items()}
for r in j['four_cohort_templates']:
 key=(r['source_packet'],*r['consumer_pose']);cohort,z,local,origin,outcome,candidates,safe=records.pop(key)
 assert sorted(map(xy,cohort))==list(map(tuple,r['matched_source_outputs']))
 assert xy(z)==tuple(r['missing_input'])and xy(local)==tuple(r['missing_target_offset'])
 assert (origin,outcome,safe)==(r['postsource_origin'],r['outcome'],r['surviving_producer_count'])
 assert candidates==recorded(r['producer_placements'])
assert not records and dict(counts)==j['summary']['outcomes']
ages=json.loads((ROOT/'audits/dcuv_count5_replay/queries.json').read_text())['slots']
for a in(7,8,9):
 assert ages[f'{a}:(0, 2)']['certified_minimum_C_age']>=5
 assert ages[f'{a}:(0, 3)']['certified_minimum_C_age']>=5
 assert ages[f'{a}:(-1, 1)']['certified_minimum_C_age']>=3
 assert ages[f'{a}:(-1, 2)']['certified_minimum_C_age']>=3
assert ages['9:(-1, 2)']['unexcluded_counts_0_to_4'][4]==0
out={'status':'PASS independent literal covers, complete cohort enumeration, postsource classification and age premises','canonical_producers':136,'minimal_cover_sets':covers,'max_same_producer_inputs':maximum,'four_cohort_templates':24,'outcomes':dict(counts),'classified_templates':[{'source_and_pose':k,'outcome':v}for k,v in sorted(classified.items())], 'manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'scope':'Factor-relative current-identity birth/age correlations. Entry births virtual-old. No global fuel or record closure.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
