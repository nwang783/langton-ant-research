"""Independent literal six-consumer classification and actual-head clock bounds."""
from pathlib import Path
from itertools import permutations,product
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
F=ROOT/'core_periodicity_new/dc_unary_preclearance_frozen_20261023_0932';M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f['frozen']).read_bytes()).hexdigest()==f['sha256']
K={p for p,b in walk(mark)[2].items()if b};entry=walk(raws[1]+mark)[2];end,h,_,flips=walk(raws[1]);O=sorted(({p for p,b in entry.items()if b}^flips)-{end+rotation(p,h)for p in K},key=xy)
assert O==[2+0j,2+3j,3+1j,3+2j]
context=walk(raws[0]+mark)[2];consumers={};records=[]
for j in(1,2,3):
 choices=[]
 for h in range(4):
  p=O[j]-rotation(1j,h)
  if(sum(xy(p))+h)%2:continue
  blockers=[]
  for k,z in enumerate(O):
   if k==j:continue
   local=rotation(z-p,-h)
   if local in context:
    assert local in K or not context[local]
    blockers.append(dict(source_output_index=k,reason='core'if local in K else'white'))
  q=dict(retired_index=j,pose=[*xy(p),h],blockers=blockers);records.append(q);choices.append(q)
 consumers[j]=choices
paths=[]
for order in permutations((1,2,3)):
 for choices in product(*(consumers[j]for j in order)):
  live={0,1,2,3};ok=True
  for c in choices:
   if any(b['source_output_index']in live for b in c['blockers']):ok=False;break
   live.remove(c['retired_index'])
  if ok:paths.append(list(choices))
J=json.loads((F/'dc_unary_cleanup_order.json').read_text());assert records==J['all_six_sector_D_consumer_poses']and paths==[J['unique_original_identity_clearance_order']]
poses=[(complex(*c['pose'][:2]),c['pose'][2])for c in paths[0]];assert poses==[(2+4j,2),(3+3j,2),(4+1j,3)]
outpoint={p for p,b in context.items()if b}^walk(raws[0])[3];e,dh,*_=walk(raws[0]);outpoint-={e+rotation(p,dh)for p in K};assert outpoint=={2+0j}
outputs=[p+rotation(2,h)for p,h in poses]
for i,z in enumerate(outputs):
 for p,h in poses[i+1:]:assert rotation(z-p,-h)not in context
 assert rotation(z-1,-1)not in entry
exit1=poses[0][0]+rotation(e,poses[0][1]);delta=poses[1][0]-exit1;assert(exit1,delta)==(1+3j,2+0j)
zero=[rotation(walk(raws[a])[0],2)for a in(0,4,7)];assert all(v.real<=0 for v in zero)
# Heading at C clock n is -n modulo4; the first produced D input requires n>=3.
first=next(n for n in range(3,7)if(-n)%4==poses[0][1]);second=first+4;third=second+3;continuation=third+2
assert(first,second,third,continuation)==(6,10,13,15)
out=dict(status='PASS complete independent conditional unary-D preclearance geometry',manifest_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),unique_order=[c['retired_index']for c in paths[0]],poses=[[*xy(p),h]for p,h in poses],replacement_outputs=list(map(xy,outputs)),required_clock_lower_bounds=[first,second,third,continuation],scope='All three ORIGINAL DC spare identities retire by D packets before main A is consumed; arbitrary other support/replacements permitted. Lower bounds only, no equality realization, fresh fuel, arbitrary-chain or capture conclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
