from itertools import product
import json
from pathlib import Path
from verify_macro_word import check,rot
allowed={'QCV':['','C','U','V'],'QCCV':[''],'BCV':['','C','U'],'BCCV':['','C']}
results=[]
for suffix,prefixes in allowed.items():
 for n in range(3):
  for letters in product('CUVQB',repeat=n):
   pre=''.join(letters);word=pre+suffix
   try:r=check(word)
   except AssertionError as e:
    assert pre not in prefixes,(word,e)
    results.append({'word':word,'feasible':False,'conflict':e.args[0]})
   else:
    assert pre in prefixes,word
    j=len(pre)+1;pose=r['blocks'][j]['pose'];dx,dy=rot((-1,0),pose[2]);q=(pose[0]+dx,pose[1]+dy)
    assert not any((z[1],z[2])==q for z in r['trace'] if z[4]<j),(word,q)
    results.append({'word':word,'feasible':True,'fuel':r['fuel']})
Path(__file__).with_name('fold_turn_prefix_certificate.json').write_text(json.dumps(results,indent=2))
print('Exact literal cases:',len(results),'feasible:',sum(r['feasible']for r in results))
