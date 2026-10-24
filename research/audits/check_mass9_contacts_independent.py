"""Independent all-length mass-nine closure, physical cores and virgin-cohort interfaces."""
from pathlib import Path
from collections import deque,Counter
import json,hashlib
import check_actual_reconvergence_independent as A
R=A.ROOT;F=R/'core_periodicity_new/mass9_contacts_frozen_20261023_1000';M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f.get('frozen',f.get('file'))).read_bytes()).hexdigest()==f['sha256']
J=json.loads((F/'mass9_reconvergence_contacts.json').read_text());Q=deque([()]);accepted=[()];cycles=[];extensions=0
while Q:
 w=Q.popleft()
 for a in A.IDS:
  extensions+=1;v=w+(a,);B=A.seed(v)
  if B is None or len(B)>9:continue
  accepted.append(v);Q.append(v);beta,hist,res,components=A.graph(v,B)
  report=next(q for q in J['all_nonempty_incidence_summaries']if tuple(q['word'])==v)
  assert beta==report['beta']and len(components)==report['component_count']and sorted(map(A.xy,B))==list(map(tuple,report['initial_black_cells']))
  if beta:cycles.append(v);assert beta==1 and len(components)==2
assert set(accepted)==set(map(tuple,J['accepted_words']))and len(accepted)==87 and extensions==696
assert cycles==[(1,6,4,4),(1,6,4,5)]
contacts=[]
for w in cycles:
 B=A.seed(w);p=0j;h=0;t=0
 for a in w:
  for c in A.raws[a]:
   assert(c=='L')==(p in B);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=A.rotation(1j,h);t+=1
   if t in(43,91,109):
    core={p+A.rotation(z,h)for z in A.K};assert core<=B
    required={43:{-2+2j,-1+3j},91:{-1+1j,2j},109:{3+1j,2+0j}}[t];assert required<=core
    contacts.append([w,t,*A.xy(p),h])
for q in J['virgin_D_DC_immediate_successor_disjointness']:
 b,a=q['producer'],q['successor'];Ib,Ob,e,h=A.G[b];I={e+A.rotation(z,h)for z in A.G[a][0]};assert not Ob&I and sorted(map(A.xy,I))==list(map(tuple,q['successor_inputs']))
out=dict(status='PASS independent complete mass-nine closure and literal black-core contacts',accepted=len(accepted),extensions=extensions,depth_distribution=dict(Counter(map(len,accepted))),cycle_words=cycles,contacts=contacts,virgin_interface_cases=16,manifest_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),scope='Incidence reset at complete factor entry; no global seed-mass bound, inherited-component labels or repeated fresh-helper budget.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
