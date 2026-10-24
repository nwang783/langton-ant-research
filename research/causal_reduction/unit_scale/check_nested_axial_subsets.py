"""Complete fixed eight-slot perpendicular hierarchy interface, not arbitrary images."""
from pathlib import Path
import json,hashlib,itertools
from probe_nested_axial_hairpin import MacroModel,physical_trace,states,check,U,V,W
P=Path(__file__).parent
rows=physical_trace(W,0)[0]
slots=[j for j,(p,t,h) in enumerate(rows) if h%2]

def build(selected):
 bases=[(h,t) for h in range(4) for t in 'RL'];images=[[s] for s in range(8)]
 b=8;bases.append((0,'R'));images.append([])
 bi=states(W,0);bi[8]=b
 for j in selected:
  p,t,h=rows[j];c=len(bases);bases.append((h,'L' if t else 'R'))
  cw=W.translate(str.maketrans('RL','LR')) if t else W
  ci=states(cw,h);ci[8]=c;images.append(ci);bi[j]=c
 images[b]=bi
 return MacroModel(bases,images,b)

out=[]
for mask in range(1,1<<len(slots)):
 selected=[j for i,j in enumerate(slots) if mask>>i&1];m=build(selected);tests=[]
 for r in range(2,7):
  z=check(m,r);tests.append(z)
  if 'conflict' in z:break
 out.append(dict(mask=mask,slots=selected,tests=tests))
result=dict(scope=__doc__,slots=slots,cases=out,survivors=[x['mask'] for x in out if 'conflict' not in x['tests'][-1]],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'nested_axial_subsets.json').write_text(json.dumps(result,indent=2)+'\n')
from collections import Counter
print(dict(cases=len(out),conflict_depths=Counter(x['tests'][-1]['depth'] for x in out if 'conflict' in x['tests'][-1]),survivors=result['survivors']))
