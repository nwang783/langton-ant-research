"""Independent symbolic seed extrema, mature occupied normals, and weighted transport controls."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];B=ROOT/'nonlinear_global_budget_2026-10-23';D=json.loads((ROOT/'deliverables/constant_184_capturing_family/family_data.json').read_text());S=D['family']['seed_families'];H=D['standard_word'];assert len(S)==184
sub=lambda a,b:(a[0]-b[0],a[1]-b[1]);add=lambda a,b:(a[0]+b[0],a[1]+b[1]);neg=lambda a:(-a[0],-a[1]);positive=lambda a:a[0]>=0 and sum(a)>=0
def extremal(L):
 low=min(L,key=sum);high=max(L,key=sum)
 assert all(positive(sub(a,low))and positive(sub(high,a))for a in L)
 return low,high
hulls={name:extremal(L)for name,L in [('x',[q[0]for q in S]),('y',[q[1]for q in S]),('u',[add(*q)for q in S]),('t',[sub(*q)for q in S])]}
assert hulls=={'x':([-56,-213],[56,228]),'y':([-56,-225],[56,209]),'u':((-112,-408),(112,414)),'t':((0,-71),(0,51))}
start=([14,33],[14,70]);relative=[sub(q[i],start[i])for q in S for i in(0,1)];radius=extremal(relative+list(map(neg,relative)))[1];assert radius==(70,295)
assert all(q[0][0]==q[1][0] and q[0][0]%2==0 and (q[0][0]-14)%14==0 for q in S)
profiles=Counter((q[0][1]-q[1][1],q[0][1]%2)for q in S);assert len(profiles)==126
waves=json.loads((ROOT/'audits/check_wave_complete_bulk_matrix_independent.json').read_text())['waves'];occupied={}
for p,lo,hi in [('1564',-54,30),('4352',-16,40)]:
 ns={q[0]for q in waves[p]['complete_output_profiles']};assert ns==set(range(lo,hi+1));occupied[p]=[lo,hi]
V=(1j,1,-1j,-1)
def trace(w,p=0j,h=0):
 rows=[]
 for c in w:rows.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return rows,p,h
def seed(rows):
 req={};par=set()
 for p,h,c in rows:
  want=(c=='L')^(p in par)
  if p in req:assert req[p]==want
  req[p]=want;par.symmetric_difference_update({p})
 return {p for p,b in req.items()if b}
weight_delta=lambda rows,center:sum((1 if c=='R'else-1)*(20000000+10000-abs((p-center).real)-abs((p-center).imag))for p,h,c in rows)
factors={''.join(H[(i+j)%104]for j in range(10))for i in range(104)}
for n in(1,2,3,11,50):
 rows,p,h=trace('RLLR'*n);assert seed(rows)=={1+y*1j for y in range(2*n)};assert weight_delta(rows,1+n*1j)==-2*n
 w='RLLR'*n;interior=sum(w[i-10:i]not in factors and w[i-9:i+1]not in factors for i in range(10,len(w)))
 assert interior>=4*n-10
spirals=[]
for n in(2,4,11,30):
 p=0j;h=0;whole=[]
 for k in range(n):
  for a,corner in enumerate(('L','RLL','L','L')):
   rows,p,h=trace('RLLR'*(n-k),p,h);assert weight_delta(rows,-n-1+n*1j)==2*(n-k)
   if a==3 and k>=1:assert weight_delta(rows,0j)==-2*(n-k)
   whole+=rows;rr,p,h=trace(corner,p,h);whole+=rr
 assert len(seed(whole))==11*n+2;spirals.append(n)
canon,dp,dh=trace(H,h=1);assert dp==2+2j and dh==1
spans=[]
for s in range(104):
 p,h,_=canon[s];rows,_,_=trace(H[s:]+H[:s],p,h);g=defaultdict(list)
 for p,h,c in rows:
  x,y=int(p.real),int(p.imag);g[x-y,x%2].append(x//2)
 spans.append(max(max(v)-min(v)for v in g.values()))
assert Counter(spans)=={2:58,3:46}and 20000000>=4352**2+4352
out=dict(status='PASS independent spatial extrema and local weighted-capacity controls',hulls=hulls,head_radius=radius,black_diameter=(112,441),fixed_profile_classes=len(profiles),occupied_wave_output_normals=occupied,cyclic_H_spans=dict(Counter(spans)),physical_spiral_controls=spirals,note_hashes={n:hashlib.sha256((B/n).read_bytes()).hexdigest()for n in ['spatial_budget_boundary_after_184_family.md','longitudinal_interval_amortization_candidate.md','head_radius_budget_computability_equivalence.md']},scope='Exact affine extrema; literal anchor countercontrols; conditional weighted finite-region telescoping and complete-history mature refill only. No global anchor, confinement, profile atlas or cap-debt bound.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
