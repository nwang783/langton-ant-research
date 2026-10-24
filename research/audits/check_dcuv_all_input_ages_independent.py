#!/usr/bin/env python3
"""Independent complete alignment query of the already certified IE kernel."""
from pathlib import Path
import json,hashlib
from collections import Counter
from check_dcuv_producer_model_independent import geometry,rotation,xy,walk,raws,ordinary,protected,ROOT
D=ROOT/'core_periodicity_new/chronology_dcuv/recurrent8_counted';ids=(0,1,4,5,6,7,8,9);mp={v:i for i,v in enumerate(ids)};cc=(0,1,0,1,2,0,1,2)
cp=D/'closure.tsv';assert hashlib.sha256(cp.read_bytes()).hexdigest()=='e8ad57fc2f640f31e4ab0493440089418248dc03f8575dbb71b2d85bf4dcc4e4'
clauses={tuple(map(int,l.split()[:8])) for l in cp.read_text().splitlines()}
author=ROOT/'core_periodicity_new/chronology_dcuv/counted_all_input_queries.json';J=json.loads(author.read_text());ans={};queries=0
# Use doubled integral centers, rather than the author's half-integer arithmetic.
def cone(source,p,h,count):
 rem=count-cc[mp[source]]
 if rem>=2:return True
 if rem<0:return False
 end,heading,*_=walk(raws[source]);c=-1-1j
 vector=rotation(2*p+rotation(c,h)-2*end-rotation(c,heading),-heading)
 X,Y=xy(vector);assert vector==complex(X,Y)
 if X%2 or Y%2:return False
 X//=2;Y//=2
 if rem:
  X-=1;Y-=1
  return Y>=0 and X<=Y and (X+Y)%2==0 and (Y!=0 or X%4==0)
 return X>=0 and Y>=X and (X+Y)%2==0 and (X!=0 or Y%4==0)
for target in ids:
 for slot in sorted(geometry[target]['inputs'],key=xy):
  rows={}
  for heading in range(4):
   displacement=rotation(slot,heading)
   for source in ids:
    for output in geometry[source]['outputs']:
     p=output-displacement;r=(source,target,*xy(p),heading,*xy(output))
     if (sum(xy(p))+heading)%2 or r[:5] in ordinary or r in protected:continue
     status=[]
     for k in range(4):
      reason='heading' if k<cc[mp[source]] or (heading+k)%4 else 'kinematic' if not cone(source,p,heading,k) else 'signed_clause' if (mp[source],mp[target],*r[2:],k) in clauses else 'OPEN'
      status.append(reason);queries+=1
     assert r not in rows;rows[r]=status
  key=f'{target}:{xy(slot)}';old=J['queries'][key]
  assert rows=={tuple(r['tuple']):r['statuses'] for r in old['rows']}
  opens=[sum(row[k]=='OPEN' for row in rows.values()) for k in range(4)]
  assert len(rows)==old['admitted_alignments'] and opens==old['open_counts']
  minimum=next((k for k,c in enumerate(opens) if c),4)
  ans[key]={'admitted_alignments':len(rows),'unexcluded_counts_0_to_3':opens,'certified_minimum_C_age':minimum}
assert set(ans)==set(J['queries'])
assert min(v['certified_minimum_C_age'] for v in ans.values())==2
result={'status':'PASS complete signed-kernel consequences for every recurrent-eight residual input','queries':queries,'slots':ans,'scope':'Every produced residual identity, complete recurrent-eight interval; count includes source packet C macros and strict intermediates, excludes consumer. Unexcluded counts are not asserted realizable. Initial residual identities have no such age requirement.','hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (cp,author,Path(__file__))}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
