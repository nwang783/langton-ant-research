"""Literal cohort universe and dependency-bound all-age minimum-clock assembly.
No author code is imported. Earlier independently signed proofs are dependencies.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_max_three_cohort_frozen_20261023_1805'
M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
ids=(0,1,4,5,6,7,8,9);K={q for q,b in walk(mark)[2].items()if b};I=(-1+1j,-1+2j,-1+4j,2j,3j);outputs={}
for src in ids:
 e,h,_,flip=walk(raws[src]);req=walk(raws[src]+mark)[2];before={q for q,b in req.items()if b}
 outputs[src]=(before^flip)-{e+rotation(q,h)for q in K}
 if src in (7,8,9):assert before-K==set(I)
# Align a target input with any source output. This is a complete finite placement list.
universe={};five=[]
for src in ids:
 for h in range(4):
  for p in {q-rotation(o,h)for q in I for o in outputs[src]}:
   if (sum(xy(p))+h)%2:continue
   O={p+rotation(o,h)for o in outputs[src]};mask=sum(1<<i for i,q in enumerate(I)if q in O)
   if mask.bit_count()>=4:universe[src,*xy(p),h]=mask
   if mask==31:five.append((src,*xy(p),h))
assert len(universe)==24 and not five
S=json.loads((B/'dependency_first_shadow.json').read_text());O=json.loads((B/'dependency_two_cohorts.json').read_text());T=json.loads((B/'dependency_second_shadow.json').read_text())
rows={}
for r in S['four_cohort_templates']:
 src=r['source_packet'];x,y,h=r['consumer_pose'];hh=(-h)%4;p=rotation(-complex(x,y),hh);key=(src,*xy(p),hh)
 assert key in universe and key not in rows
 if r['previous_outcome']=='excluded_all_ages':reason='old_seven'
 elif r['new_retirement_exclusion']:reason='first_shadow_twelve'
 elif key[0] in (8,9)and key[1:]==(1,5,2):
  assert any(a['packet']==src and a['head']==list(key[1:])for a in O['source_rows']);reason='own_U_suffix_two'
 else:
  assert key in {(s,-1,1,0)for s in (7,8,9)}
  assert any(a['source']==src and a['source_pose']==list(key[1:])and a['old_inventory_row']==r['signed_inventory_row']for a in T['three_remaining_four_cohort_cuts']);reason='second_shadow_three'
 rows[key]=dict(mask=universe[key],reason=reason)
assert set(rows)==set(universe)
counts=dict(Counter(r['reason']for r in rows.values()));assert counts==dict(old_seven=7,first_shadow_twelve=12,own_U_suffix_two=2,second_shadow_three=3)
D=json.loads((B/'dependency_minclock.json').read_text());phases=[]
for ph in D['phases']:
 h=ph['heading'];keep=[];cut=[]
 for c in ph['completed_abstract_states']:
  r=c['last_producer'];x,y,hh=r['head'];assert hh==h
  p=complex(x,y);OO={p+rotation(o,h)for o in outputs[r['packet']]}
  mask=sum(1<<i for i,q in enumerate(I)if q in OO);assert mask==r['output_mask']
  old=c['older_input_mask'];young=c['minimum_age_input_mask'];assert old^young==31 and old&young==0 and mask&old==0 and mask&young==mask
  if c['birth_packets']==1:assert mask==young
  entry=dict(older=old,youngest=young,last_mask=mask,birth_packets=c['birth_packets'],source=(r['packet'],x,y,h))
  if mask.bit_count()>=4:
   assert (r['packet'],x,y,h)in universe;entry['reason']='max_three';cut.append(entry)
  elif h==2:
   assert (r['packet'],x,y,h,mask)in {(s,1,3,2,26)for s in (7,8,9)};entry['reason']='signed_phase_two';cut.append(entry)
  else:
   assert old&16 and (old&28).bit_count()>=2;keep.append(entry)
 phases.append(dict(heading=h,raw_count=len(keep)+len(cut),kept=keep,cut=cut,older_masks=sorted({r['older']for r in keep})))
assert [p['older_masks']for p in phases]==[[24,28],[20,28],[],[28]]
assert [len(p['kept'])for p in phases]==[14,5,0,6]
author=json.loads((B/'02_U_max_three_producer_cohort.json').read_text())
assert {(r['source_packet'],*r['source_in_goal'])for r in author['all24_exclusion_rows']}==set(universe)
assert author['strictly_older_masks_by_phase']==[p['older_masks']for p in phases]
out=dict(status='PASS independent literal 24-row/no-five universe and signed-dependency all-age assembly',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),four_cohort_count=24,five_cohort_count=0,exclusion_counts=counts,cohort_rows=[dict(source=k,**v)for k,v in sorted(rows.items())],phase_rows=phases,scope='Earlier genuine full producers inside one complete-eight factor only; entry origins are not merged. Youngest produced q of positive finite C age has strictly older d and another of b/c. Distinct producers can share a historical incidence component; no merger or U budget follows.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in ('cohort_rows','phase_rows')})
