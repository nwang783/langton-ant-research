"""Literal canonical reversal and exact affine exclusion from its full backward read set."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';V=((0,1),(1,0),(0,-1),(-1,0));M=json.loads((U/'prepared1564_uniform_support_manifest.json').read_text());J=json.loads((U/'prepared1564_reverse_source.json').read_text());H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
canonical=set();remote=[]
for xx,yy in M['seed_families']:
 a=(xx[0]-14,yy[0]-14);b=(xx[1]-33,yy[1]-70)
 if a==(0,0):canonical.add(b)
 else:remote.append((a,b))
assert len(canonical)==13 and canonical==set(map(tuple,J['source_seed']))and len(remote)==171
B=set(canonical);p=(1,0);h=1;read=set()
for c in J['word']:
 read.add(p);assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;d=V[h];p=p[0]+d[0],p[1]+d[1]
assert len(J['word'])==2589 and len(read)==527 and(p,h)==((9,-25),2)and len(B)==286 and B==set(map(tuple,J['final_field']))
tail=J['capture_word'];assert tail in {H[i:]+H[:i]for i in range(104)}
source=SELF.with_name('check_prepared1564_connected_capture_independent.py').read_text();exec(compile(source[source.index('def periodic('):source.index('reports=[]')],str(SELF),'exec'))
mm,d,groups,critical=periodic(B,p,h,tail);assert mm is None and d==(2,-2)
q=p;hh=h;tailreads=[]
for c in tail:
 tailreads.append(q);hh=(hh+(1 if c=='R'else-1))%4;v=V[hh];q=q[0]+v[0],q[1]+v[1]
prefix_checks=tail_checks=0
for a,b in remote:
 assert a[0]==a[1]and a[0]!=0
 for q in read:
  n=Fraction(q[0]-b[0],a[0]);assert not(n.denominator==1 and n>=1 and b[1]+a[1]*n==q[1]);prefix_checks+=1
 for q in tailreads:
  # Solve a*n - d*k = q-b by the nonzero two-by-two determinant.
  v=(q[0]-b[0],q[1]-b[1]);det=a[1]*d[0]-a[0]*d[1];assert det
  n=Fraction(-v[0]*d[1]+v[1]*d[0],det);k=Fraction(a[0]*v[1]-a[1]*v[0],det)
  assert not(n.denominator==k.denominator==1 and n>=1 and k>=0);tail_checks+=1
for q in groups:
 far=q[0]+2000000,q[1]-2000000;assert periodic(B^{far},p,h,tail)[0]is not None
out=dict(status='PASS original184-cell family is bi-standard for EVERY N>=1',note_sha256=hashlib.sha256((U/'prepared1564_original_bistandard_family.md').read_bytes()).hexdigest(),canonical_source_sha256=hashlib.sha256((U/'prepared1564_reverse_source.json').read_bytes()).hexdigest(),source_mass=13,remote_initial_cells=171,reverse_prefix_updates=2589,reverse_prefix_distinct_cells=527,exact_prefix_affine_nonintersections=prefix_checks,exact_tail_affine_nonintersections=tail_checks,reverse_capture_pose=[[14,42],[14,45],2],reverse_capture_mass=457,reverse_capture_drift=[2,-2],tail_orbits=len(groups),critical_levels=critical,far_flip_rejections=len(groups),scope='Combined with the separately signed all-N forward capture, this proves the original184-cell family bi-standard. It does not classify any other finite seed.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
