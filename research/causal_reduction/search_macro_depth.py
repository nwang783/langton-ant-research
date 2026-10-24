from probe_macro_ancestry import macros,trace
from itertools import product
import json
best=0;record=None;tested=0;rows=[]
for n in range(1,9):
 for letters in product('CVB',repeat=n):
  w=''.join(letters)
  if 'CCCC' in w or 'BB' in w:continue
  o=trace(w*2)
  if o is None:continue
  o=trace(w*10)
  if o is None:continue
  tested+=1
  if o['maxdepth']>best:
   best=o['maxdepth'];record=w;print('BEST',best,w,flush=True);rows.append([best,w,o['fuel']])
 print('LEVEL',n,'tested',tested,'best',best,record,flush=True)
open('/workspace/shared/langton/causal_reduction/macro_depth_periodic_search.json','w').write(json.dumps(rows,indent=2))
