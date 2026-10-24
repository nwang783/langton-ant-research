"""No-age consumer-cover and complete four-cohort enumeration from literal words."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_white_shadow_frozen_20261023_1709';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
ids=(0,1,4,5,6,7,8,9);K={q for q,c in walk(mark)[2].items()if c};G={}
for src in ids:
 e,h,_,flip=walk(raws[src]);req=walk(raws[src]+mark)[2];before={q for q,c in req.items()if c};I=before-K;O=(before^flip)-{e+rotation(q,h)for q in K};G[src]=I,O,set(req)
I=G[7][0];z=-1+3j;assert I=={-1+1j,-1+2j,-1+4j,2j,3j}
assert all(G[t][0]==I and walk(raws[t]+mark)[2][z] is False for t in (7,8,9))
rows=[];good=[]
for src in ids:
 for slot in G[src][0]:
  for h in range(4):
   p=z-rotation(slot,h);hits={q for q in I if rotation(q-p,-h)in G[src][2]};sector=(sum(xy(p))+h)%2
   rows.append(dict(packet=src,slot=xy(slot),pose=(*xy(p),h),wrong_sector=bool(sector),hits=sorted(map(xy,hits))))
   if not sector:good.append(hits)
assert len(rows)==92 and len(good)==46
covers=[];subsets=0
for n in range(6):
 for cc in combinations(sorted(I,key=xy),n):
  subsets+=1;c=set(cc)
  if all(c&hit for hit in good)and not any(old<=c for old in covers):covers.append(c)
expected=[{-1+1j,-1+4j},{-1+1j,3j},{-1+2j,-1+4j},{-1+2j,3j}];assert set(map(frozenset,covers))==set(map(frozenset,expected))and subsets==32
cohorts={}
for src in ids:
 O=G[src][1]
 for p,h in {(o-rotation(i,h),h)for o in O for i in I for h in range(4)}:
  if (sum(xy(p))+h)%2:continue
  T={p+rotation(i,h)for i in I};shared=O&T;assert len(shared)<5
  if len(shared)!=4:continue
  local={rotation(q-p,-h)for q in shared};shadow=p+rotation(z,h);blocked=shadow in O and any(c<=local for c in covers)
  cohorts[src,*xy(p),h]=dict(shared=sorted(map(xy,shared)),shadow=xy(shadow),shadow_is_output=shadow in O,blocked=blocked)
assert len(cohorts)==24
old=json.loads((B/'dependency_old_inventory.json').read_text())['four_cohort_templates'];assert set(cohorts)=={(x['source_packet'],*x['consumer_pose'])for x in old}
for r in old:
 key=r['source_packet'],*r['consumer_pose'];assert cohorts[key]['shared']==sorted(map(tuple,r['matched_source_outputs']));cohorts[key]['old_outcome']=r['outcome']
blocked={key for key,r in cohorts.items()if r['blocked']}
assert blocked=={(src,*p)for src in (7,8,9)for p in [(2,-2,0),(-1,0,1),(0,4,2),(4,1,3)]}
assert all(cohorts[k]['old_outcome']=='not_excluded_by_this_static_test'for k in blocked)
survivors={k:r for k,r in cohorts.items()if not r['blocked']and r['old_outcome']!='excluded_all_ages'}
assert set(survivors)=={(7,1,-1,0),(8,1,-1,0),(9,1,-1,0),(8,1,5,2),(9,1,5,2)}
out=dict(status='PASS independent all-age U white-shadow consumer cover and twelve cohort exclusions',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),raw_alignments=92,sector_valid=46,minimal_covers=[sorted(map(xy,c))for c in covers],all_subsets=32,complete_four_cohort_templates=24,new_all_age_exclusions=sorted(blocked),remaining_static_templates=[dict(source_and_pose=k,**r)for k,r in sorted(survivors.items())],rows=rows,scope='Protected CURRENT identities, complete-eight true inputs and contexts only. No age, center, record, boundary or mass premise. No component-merger budget or global U exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='rows'})
