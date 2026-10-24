#!/usr/bin/env python3
"""Author controls for the physical interval-deficiency lemma, not a word scan."""
import itertools,json,random,pathlib,hashlib
from bulk_black_deficiency import *
from bulk_standard_compatibility import criterion,H
HERE=pathlib.Path(__file__).resolve().parent
V=''.join('L' if c=='R' else 'R' for c in H[::-1]);P=V[:31]+'LRRRR'+V[32:]
Q=''.join('L' if c=='R' else 'R' for c in P[::-1])
cases=[('H',H),('H2',H*2),('reverse104',V),('P108',P),('forward108',Q),
       ('reverse104x2',V*2),('D10','LLLLRLRRRR'),('odd_LR','LR'),('odd_LR3','LR'*3)]
records=[]
for name,word in cases:
 for h in range(4):
  r=criterion(word,h);d=supplied_profile_deficiency(r)
  assert d['status']=='EXACT_BLACK_DEFICIENCY'
  if name=='P108':assert d['black_deficiency']==11
  if name=='forward108':assert d['black_deficiency']==3
  records.append(dict(name=name,heading=h,deficiency=d))
# Separate exhaustive subset maximization on physical point/interval instances.
rng=random.Random(231326);synthetic=0
for _ in range(500):
 b=rng.randrange(8);normals=[rng.randrange(-4,17) for j in range(b)];n=rng.randrange(12);cs=[]
 for i in range(n):
  lo=rng.randrange(-5,18);hi=lo+rng.randrange(6)
  mask=sum((1<<j) for j,t in enumerate(normals) if lo<=t<=hi and rng.randrange(2))
  cs.append(dict(band=[lo,hi],cover_mask=mask,polluted_white=[]if rng.randrange(4)else[0]))
 got=interval_black_deficiency(cs,normals);maximum=0
 for selected in itertools.product((False,True),repeat=n):
  chosen=[i for i,t in enumerate(selected) if t]
  if any(cs[i]['polluted_white'] for i in chosen):continue
  if any(max(cs[i]['band'][0],cs[j]['band'][0])<=min(cs[i]['band'][1],cs[j]['band'][1])
         for i,j in itertools.combinations(chosen,2)):continue
  mask=0
  for i in chosen:mask|=cs[i]['cover_mask']
  maximum=max(maximum,mask.bit_count())
 assert maximum==got['maximum_standard_covered'];synthetic+=1
# The mask/band physical condition may NOT be omitted: this abstract set-cover
# instance repeats one class in disjoint bands and would overcount its weight.
invalid=[dict(band=[0,1],cover_mask=1,polluted_white=[]),
         dict(band=[2,3],cover_mask=1,polluted_white=[])]
try:interval_black_deficiency(invalid,[0])
except ValueError:pass
else:raise AssertionError('accepted unphysical interval cover')
out=dict(status='PASS author physical interval-deficiency controls',supplied_profiles=records,
         synthetic_exhaustive_maxima=synthetic,unphysical_masks_rejected=True,
         source_sha256=hashlib.sha256((HERE/'bulk_black_deficiency.py').read_bytes()).hexdigest(),
         scope='No consumer search. Independent implementation audit separate.')
(HERE/'bulk_black_deficiency_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(supplied_profiles=len(records),synthetic_exhaustive_maxima=synthetic,
                     deficiencies={x['name']:x['deficiency']['black_deficiency'] for x in records if x['heading']==0},
                     source_sha256=out['source_sha256']),indent=2))
