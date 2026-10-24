"""Independent literal component-count controls, not the unbounded proof."""
import json,itertools
from pathlib import Path
R=Path('/workspace/shared/langton');D=json.loads((R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text());V=((0,1),(1,0),(0,-1),(-1,0))
def run(word):
 colors={};tokens={};roots=[0];sizes={0:1};node=0;p=(0,0);h=0
 for m in word:
  for c in D[m]['word']:
   b=c=='L'
   if p in colors and colors[p]!=b:return None
   colors[p]=not b
   if b:
    owner=tokens.pop(p,None);node=len(roots)
    root=node if owner is None else roots[owner];roots.append(root)
    if owner is None:sizes[root]=1
   else:
    assert p not in tokens;tokens[p]=node;sizes[roots[node]]+=1
   h=(h+(1 if c=='R' else -1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 return max(sizes.values())
assert [run(w) for w in ['B','CB','CCCC']]==[12,19,36]
feasible=0;maximum=0
for k in range(9):
 for word in itertools.product('CVB',repeat=k):
  s=run(word)
  if s is not None:feasible+=1;maximum=max(maximum,s);assert s<=36
out=dict(status='PASS: literal finite controls',feasible_words=feasible,maximum_component_size=maximum,prefixes={w:run(w) for w in ['B','CB','CCCC']},scope='Unbounded-word theorem requires the separately audited seam/grammar proof, not this enumeration.')
(R/'audits/cvb_component_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
