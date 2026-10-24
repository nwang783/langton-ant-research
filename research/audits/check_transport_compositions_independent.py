"""No author imports: regenerate unit-nine palette and every exact composition."""
from pathlib import Path
from itertools import product
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'causal_reduction/unit_scale/transport_composition_all.records.json'
def replay(w):
 z=0j;heading=1j;last={}
 for t,ch in enumerate(w):
  previous=last.get(z)
  if previous is not None and previous[0]==ch:
   return {'cell':[int(z.real),int(z.imag)],'conflict':t,'previous':previous[1],'turn':ch}
  last[z]=(ch,t)
  heading*= -1j if ch=='R' else 1j
  z+=heading
 return (z,heading)
palette={'R':['R'],'L':['L']}
for letters in product('RL',repeat=9):
 w=''.join(letters);charge=sum(1 if c=='R' else -1 for c in w)
 if charge not in(-1,1):continue
 trace=replay(w)
 if isinstance(trace,dict):continue
 if trace==(complex(charge),complex(charge)):
  palette['R' if charge==1 else 'L'].append(w)
assert all(len(v)==7 for v in palette.values())
phases=list(product(palette['R'],palette['L']))
def apply(f,w):return ''.join(f[c=='L'] for c in w)
J=json.loads(P.read_text());assert J['palette']==palette and J['phases']==[list(f)for f in phases]
assert [s['images']for s in J['states']]==[list(f)for f in phases]
expected_bad=[];expected_edges=[];maximum=0
for i,f in enumerate(phases):
 for j,g in enumerate(phases):
  words=[apply(f,w)for w in g];bad=None
  for a,w in enumerate(words):
   v=replay(w)
   if isinstance(v,dict):bad=(a,v);break
  if bad is None:
   assert i==0 or j==0
   expected_edges.append([i,j,j if i==0 else i])
  else:
   assert i!=0 and j!=0
   expected_bad.append([i,j,bad[0],bad[1]])
   maximum=max(maximum,bad[1]['conflict'])
assert J['edges']==expected_edges and J['conflicts']==expected_bad and not J['caps']
primitive=[]
for i,f in enumerate(phases[1:],1):
 for sign in ('R','L'):
  for w in palette[sign][1:]:
   v=replay(apply(f,w));assert isinstance(v,dict)
   primitive.append([i,w,v])
assert len(primitive)==576
out={'status':'PASS independent complex-heading literal compositions','palette':palette,'phases':49,'legal_edges':len(expected_edges),'nonidentity_pair_conflicts':len(expected_bad),'primitive_conflicts':len(primitive),'latest_primitive_conflict':max(x[2]['conflict']for x in primitive),'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'scope':'All two-turn maps from identity plus six legal charge-preserving unit-nine images per turn. No larger-image or independent-heading conclusion.'}
(ROOT/'audits/transport_composition_primitive_independent.records.json').write_text(json.dumps(primitive,sort_keys=True,separators=(',',':'))+'\n')
(ROOT/'audits/transport_composition_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
