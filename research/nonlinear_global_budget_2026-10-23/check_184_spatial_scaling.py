#!/usr/bin/env python3
"""Exact all-N hull/profile extrema for the signed184-cell seed family."""
from pathlib import Path
import json,hashlib
P=Path(__file__).parent
J=json.loads((P/'constant_mass_184_geometric_gluing.json').read_text());S=J['seed_families'];start=((14,33),(14,70))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def val(a,n):return a[0]*n+a[1]
def le(a,b):d=sub(b,a);return d[0]>=0 and val(d,1)>=0
def extrema(A):
 lo=min(A,key=lambda a:val(a,1));hi=max(A,key=lambda a:val(a,1))
 assert all(le(lo,a)and le(a,hi)for a in A)
 return lo,hi
D={}
for label,A in [('x',[q[0]for q in S]),('y',[q[1]for q in S]),('u',[add(*q)for q in S]),('t',[sub(*q)for q in S])]:
 lo,hi=extrema(A);D[label]={'min':lo,'max':hi,'width':sub(hi,lo)}
rad=[]
for q in S:
 for a,b in zip(q,start):rad.extend([sub(a,b),sub(b,a)])
D['initial_radius_from_head']=extrema(rad)[1]
profiles={(q[0][1]-q[1][1],q[0][1]%2)for q in S}
assert all(q[0][0]-q[1][0]==0 and q[0][0]%2==0 for q in S)
assert all((q[0][0]-start[0][0])%14==0 for q in S)
D.update({'scope':__doc__,'fixed_initial_drift_orbit_classes':len(profiles),
 'fixed_initial_t_values':sorted({t for t,a in profiles}),'fixed_initial_drift_profiles':sorted(profiles),
 'head_relative_mod14_seed_projection_is_constant':True,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
(P/'constant_mass_184_spatial_scaling.json').write_text(json.dumps(D,indent=2)+'\n')
print('PASS: mass184, fixed normal hull[-71,51],126 standarddrift profiles; radius70N+295, diameter112N+441')
