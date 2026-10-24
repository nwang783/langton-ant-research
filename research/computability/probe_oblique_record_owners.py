"""Exploratory exact owner-cone test; no exclusion without full record phases."""
import sys,json,pathlib,math
sys.path.insert(0,'/workspace/shared/langton/causal_reduction/morphic_candidates')
from position_only_ownership import check
out=[]
for a in [(2,2),(2,-2)]:
 for theta in (0,1):
  z=check(8,a,theta)
  tests=[]
  for u,v in [(u,v)for u in range(-8,9)for v in range(1,9)if math.gcd(u,v)==1]:
   missing=[]
   for target in z['target_images']:
    protected=any(all(u*x+v*y>=0 for x,y in w['owners'])for w in target['witnesses'])
    if not protected:missing.append([target['word'],target['fine_heading']])
   tests.append(dict(normal=[u,v],missing=missing))
  z['cone_tests']=tests;out.append(z)
  best=sorted(tests,key=lambda t:len(t['missing']))[:5]
  print(a,theta,'targets',len(z['target_images']),'best',[(t['normal'],len(t['missing']))for t in best],flush=True)
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
