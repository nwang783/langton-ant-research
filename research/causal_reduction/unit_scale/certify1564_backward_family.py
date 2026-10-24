"""Exact all-N backward capture of the unmodified184-cell family.
The backward ant is the ordinary ant at(p-d_h,-h), board unchanged. A canonical
13-cell source captures; ALL other171 affine cells miss its complete finite
prefix and every infinite tail read, with no radius/time cutoff.
"""
from pathlib import Path
import json,hashlib,sys
from check_prepared1564_router_geometry import trace
P=Path(__file__).resolve().parent
M=json.loads((P/'prepared1564_uniform_support_manifest.json').read_text())
S=json.loads((P/'prepared1564_reverse_source.json').read_text())
# Normalize by the ORIGINAL head(33+14N,70+14N), rather than by wave-end shift.
source={tuple(q)for q in S['source_seed']};families=[];matched=[]
for j,(xx,yy)in enumerate(M['seed_families']):
 a=(xx[0]-14,yy[0]-14);b=(xx[1]-33,yy[1]-70)
 if a==(0,0)and b in source:matched.append(b)
 else:families.append((a,b,j))
assert len(matched)==13 and set(matched)==source and len(families)==171
Q={q for _,q,h,c in list(trace(S['word'],(1,0),1))[:-1]}
pp=tuple(S['capture_pose'][0]);hh=S['capture_pose'][1]
tail=[q for _,q,h,c in list(trace(S['capture_word'],pp,hh))[:-1]];d=tuple(S['capture_drift'])
assert d==(2,-2)
checks=[]
def fixed(a,b,q):
 n=None
 for j in range(2):
  if not a[j]:
   if b[j]!=q[j]:return None
  else:
   if(q[j]-b[j])%a[j]:return None
   x=(q[j]-b[j])//a[j]
   if n is not None and n!=x:return None
   n=x
 return n
for a,b,j in families:
 assert a[0]==a[1]and a[0]!=0
 for q in Q:
  n=fixed(a,b,q);assert n is None or n<1,('prefix collision',j,q,n)
 for i,q in enumerate(tail):
  # a*N - d*k = q-b. Sum determines N because sum(d)=0.
  delta=q[0]+q[1]-b[0]-b[1];den=a[0]+a[1]
  if delta%den:continue
  n=delta//den
  if n<1:continue
  dx=a[0]*n+b[0]-q[0];dy=a[1]*n+b[1]-q[1]
  if dx%d[0]:continue
  k=dx//d[0]
  assert k<0 or dy!=d[1]*k,('tail collision',j,i,n,k)
 checks.append({'seed_family':j,'slope':a,'offset':b,'prefix_cells':len(Q),'tail_slots':len(tail)})
# Independent exact finite-tail validator on canonical final board.
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
black=frozenset(tuple(q)for q in S['final_field']);assert first_mismatch(State(black,pp,hh),S['capture_word'])is None
out={'scope':__doc__,'status':'EXACT BACKWARD CAPTURE FOR ALL N >= 1','source_mass':13,'other_seed_cells':171,'prefix_reads':len(S['word']),'prefix_distinct_cells':len(Q),'affine_cap_checks':checks,
 'reverse_start_pose_N_constant':[[14,34],[14,70],1],'reverse_capture_time':S['capture_time'],'reverse_capture_pose_N_constant':[[14,42],[14,45],2],'reverse_capture_mass':457,'reverse_capture_drift':[2,-2],
 'canonical_source_sha256':hashlib.sha256((P/'prepared1564_reverse_source.json').read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256((P/'prepared1564_uniform_support_manifest.json').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared1564_backward_family.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='affine_cap_checks'},indent=2))
