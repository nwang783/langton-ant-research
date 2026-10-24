import json,random
from pathlib import Path
from black_core_probe_global import bridges,core
from verify_macro_word import D
rng=random.Random(9327);out={}
for k,d in D.items():
 first={};odd=set()
 for z in d['trace']:
  q=tuple(z['p']);first.setdefault(q,z['c']=='L');odd.symmetric_difference_update([q])
 best={};witness={}
 for i in range(3000):
  B={q for q,v in first.items() if v};density=rng.choice([.05,.15,.3,.5,.8])
  for x in range(-9,10):
   for y in range(-9,10):
    if (x,y) not in first and rng.random()<density:B.add((x,y))
  BB=B^odd
  f={'bridges':len(bridges(BB))-len(bridges(B)), 'outside_core':len(BB-core(BB))-len(B-core(B))}
  for name,v in f.items():
   if v>best.get(name,-1000):best[name]=v;witness[name]={'delta':v,'seed':sorted(B)}
 out[k]={'largest_increase':best,'witnesses':witness};print(k,best,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
