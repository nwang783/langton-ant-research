from pathlib import Path
import json,hashlib
from certified_comparison_perturbation import *
P=Path(__file__).parent;D=json.loads((P/'PHASE13_DOUBLE_SCATTER_CHECKED.json').read_text())
ref=reference(set(map(tuple,D['kernel'])),(0,0),0,D['post_word'],D['tail_word']);tests=[]
for A in [{(2*a,2*a)}for a in range(2,7)]+[{(14,14),(16,16),(2*10**9,2*10**9)}, {(-100,-100),(4,4),(2*10**9,2*10**9)}]:
 r=perturbation_event(ref,A)
 if r['kind'].startswith('EXACT'):
  B=ref['seed']|A;p=(0,0);h=0
  for t in range(r['time']+1):
   if p in B:B.remove(p);h=(h-1)%4
   else:B.add(p);h=(h+1)%4
   p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
  assert(p,h)==r['new_pose']and B==materialize(r['new_full_field_terms'])
  r['literal_final_black']=sorted(B)
 tests.append(dict(extra=sorted(A),result=r))
# Huge first-contact control. Choose a tail point with exact first encounter in period>=10^9.
huge=None
for q in ref['Q']:
 v=(q[0]+10**9*ref['dr'][0],q[1]+10**9*ref['dr'][1])
 if v not in ref['seed']:
  r=perturbation_event(ref,{v})
  if r['kind'].startswith('EXACT')and r['time']>=ref['L']+104*(10**9-2):huge=dict(extra=[v],result=r);break
assert huge is not None and len(huge['result']['new_full_field_terms'])<1000
out=dict(status='AUTHOR exact generic comparison event controls; independent audit requested',scope='Total first event for a supplied checked complete future. Not total iteration/capture on arbitrary perturbations; finite control does not remove unbounded geometry.',reference_source='PHASE13_DOUBLE_SCATTER_CHECKED.json',reference_source_sha256=hashlib.sha256((P/'PHASE13_DOUBLE_SCATTER_CHECKED.json').read_bytes()).hexdigest(),controls=tests,huge_control=huge)
(P/'COMPARISON_PERTURBATION_EVENT_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('literal events',len(tests),'huge time',huge['result']['time'],'terms',len(huge['result']['new_full_field_terms']))
