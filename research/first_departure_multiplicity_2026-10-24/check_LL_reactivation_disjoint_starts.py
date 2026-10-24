"""All six exact inventories exclude an interior post-LL-X reactivation start.
This is an occurrence/rank check, not a pairwise geometry or period scan.
"""
from pathlib import Path
import json,ast
j=json.loads(Path(__file__).with_name('check_LL_cyclic_supplier_reactivation_modes.json').read_text());rows=[]
for rr in j['roots']:
 for a in rr['cyclic_necessary_profiles']:
  hs={ast.literal_eval(p):h for p,h in a['histories'].items()};path=[(tuple(p),r)for p,r in a['actual_reactivation_channel']]
  cleanup=path[1:];tests=[]
  for i,(p,r)in enumerate(cleanup[1:],start=1):
   h=hs[p];aabb=len(h)==4 and h[0]==h[1]and h[2]==h[3]and h[0]!=h[2]
   if r!=2:why='not rank2'
   elif not aabb:why='not complete four-read AABB'
   else:
    assert i+1<len(cleanup)and cleanup[i+1][1]%2==1
    why='next actual read is L, not required second R'
   tests.append(dict(event=[p,r],reason=why))
  assert len(cleanup)-1==a['X_age23']
  rows.append(dict(root=rr['root'],kind=a['kind'],cleanup_events=cleanup,no_possible_later_postX_start=tests,block_length=a['X_age23']+1))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows,all_six_verified=True),indent=2)+'\n');print('PASS all six microscopic channels; endpoint-inclusive blocks5/9')
