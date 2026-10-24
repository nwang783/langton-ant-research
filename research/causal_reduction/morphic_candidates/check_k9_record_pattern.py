"""Finite inputs to the k9,a3 late outward-record normal form."""
import json,itertools
from check_private_macro_fuel import HERE,reads,rot,ownership
from renormalize_macro_grammar import feasible
r=next(z for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);O=r['images'];owner=ownership(3,0,O['R']+O['L'])
pairs=[];protected=[];top=[]
for a,b in itertools.product(O['R'],repeat=2):
 w=a+b
 if not feasible(w):continue
 first={}
 for x,y,c in reads(w):first.setdefault((x,y),c)
 witnesses=[p for p,c in first.items()if c=='L'and all(y>=0 for x,y in owner(*p))]
 if witnesses:protected.append(dict(words=[a,b],witnesses=witnesses))
 else:pairs.append([a,b])
for typ in'RL':
 for w in O[typ]:
  for h in range(4):
   pts=[(*rot(x,y,h),c)for x,y,c in reads(w)]
   assert max(y for x,y,c in pts)<=3
   if max(y for x,y,c in pts)==3:
    # Any such previous macro ends by taking the coarse northward step.
    assert(h+(1 if typ=='R'else-1))%4==0
    top.append(dict(type=typ,word=w,entry_heading=h,top_reads=[(x,c)for x,y,c in pts if y==3]))
expected=[['RRLRRRRLR','RLRLLLLRL'],['LLLRLLRLR','RLRRLRRRR'],['LLLRLLRLR','RLRLLLLRL'],['LLLLRRLLR','RLRRLRRRR'],['LLLLRRLLR','RLRLLLLRL']]
assert pairs==expected
assert len(top)==4
assert sorted(z['top_reads']for z in top)==[[(-0,'L'),(-1,'L')],[(-0,'L'),(-1,'L')],[(0,'R'),(1,'R')],[(0,'R'),(1,'R')]]
for w in('LLLRLLRLR','LLLLRRLLR'):
 first={}
 for x,y,c in reads(w):first.setdefault((x,y),c)
 assert first[0,0]==first[-1,0]=='L'
out=dict(scale=[3,0],k=9,unprotected_pairs=pairs,protected_pairs=protected,top_reachers=top,forced_late_record_pair=pairs[0],forced_word=''.join(pairs[0]),status='finite geometry checked; global inference in k9_record_normal_form.md')
(HERE/'k9_record_pattern.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
