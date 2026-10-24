"""Extend exact clean-crossing half-ray guards to the COMPLETE715-cell blank cap.
Uses sibling's audited all-time checker, changing only the full incoming finite seed.
"""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'scattering/transverse'
sys.path.insert(0,str(SRC))
import certify_finite_transfer as f
B=set();p=(0,0);h=0;prefix=[]
for _ in range(9977):
 prefix.append(p);p,h,_=f.step(B,p,h)
assert p==(-15,10) and h==3 and len(B)==715
A={(x-p[0],y-p[1]) for x,y in B}
assert A==set(map(tuple,json.loads((HERE/'blank_standard_entry.json').read_text())['black']))
assert (min(x-y for x,y in prefix),max(x-y for x,y in prefix))==(-34,48)
assert (min(x+y for x,y in prefix),max(x+y for x,y in prefix))==(-21,35)
qs,ep,eh=f.c.trace(f.c.WORD,h,p)
assert min(x-y for x,y in qs)>=-34 and max(x-y for x,y in qs)<=48
assert max(x+y for x,y in qs)<=35
assert f.c.minus(ep,p)==(-2,-2) and eh==h
f.SEED=A
f.MINS=f.discrepancy_minima()
assert f.certify_period(A,(0,0),3,f.c.WORD)
rows=json.loads((SRC/'crossings_discovery.json').read_text())
expected_classes={(r,a,s) for r in (1,3) for a in (0,1) for s in (1,3)}
assert {(r['rotation'],r['a'],r['s']) for r in rows if r['s']%2}==expected_classes
assert sum(r['s']%2 for r in rows)==8
reference_reads,_,_=f.c.trace(f.c.WORD,f.c.H0,(0,0))
reference_min_z=min(map(sum,reference_reads))
out=[]
for row in rows:
 if row['s']%2:
  static=f.c.first_contact(row['rotation'],row['a'],row['s'])[3]
  # Earlier reference epochs translate the incoming read set by -D,
  # increasing z by4. These remote static lines lie below even epoch0.
  assert all(sum(e)==0 and sum(b)<reference_min_z for b,e,lo,hi in static)
  got=f.required_guard(row)
  # Correct inherited metadata to bind the actual replacement SEED.
  got['minimum_input_mass']=len(A)+12*(2*got['minimum_symmetric_rail_half_length']+1)
  got['scope']='all integer gap k>=K and half-length M>=M0; pristine crossing data, complete715-cell blank cap as actual SEED'
  got['reference_min_incoming_read_z']=reference_min_z
  got['reference_max_static_line_z']=max(sum(b) for b,e,lo,hi in static)
  out.append(got)
  print(row['rotation'],row['a'],row['s'],got['minimum_certified_gap_periods'],flush=True)
assert len(out)==8 and max(r['minimum_certified_gap_periods'] for r in out)==25
res={'scope':'Audited transverse-template transfer recomputed for complete blank715-cell cap; all initial black-field differences retained.',
     'incoming_black_mass':len(A),'class_minima':[(k,v)for k,v in sorted(f.MINS.items())],
     'uniform_gap_K':max(r['minimum_certified_gap_periods'] for r in out),'records':out}
(HERE/'blank_crossing_transfer.json').write_text(json.dumps(res,indent=2))
