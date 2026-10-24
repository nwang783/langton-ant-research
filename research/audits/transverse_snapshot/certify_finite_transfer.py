"""Uniform mature-gap and finite-rail transfer for the8same-sector crossings.

For base static lines (b,e), put their finite black segments at
b+k*D+j*e, -M<=j<=M, and add the supplied13cell standard seed at0.
The theorem quantifies all integers k>=K and M>=M0, with per-class K,M0
computed by exact infinite-read geometry. No parameter sampling proves it.
"""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation')))
from ant_exact import step,certify_period
import crossing as c
BACK=c.times(-1,c.D)
SEED=set(map(tuple,c.DATA['seed']))

def discrepancy_minima():
 # D0=H0 XOR canonical13cellseed, partitioned by BACK translation classes.
 f=c.Field(c.incoming_past());edges={key:set(v[1]) for key,v in f.index.items()}
 assert all(not v[0] for v in f.index.values())
 for q in SEED:
  key,z=c.orbitkey(q,BACK);s=edges.setdefault((BACK,key),set())
  s.symmetric_difference_update({z,z+1})
 return {key[1]:min(v) for key,v in edges.items() if v}

MINS=discrepancy_minima()

def replay(row):
 _,p,h,static=c.first_contact(row['rotation'],row['a'],row['s'])
 f=c.Field(c.incoming_past()+static);p=(0,0);h=c.H0;reads=[]
 for t in range(row['capture']):
  reads.append(p);p,h,ch=f.step(p,h)
  assert ch==(c.WORD[t%104] if t<row['t0'] else row['word'][t-row['t0']])
 w=row['word'][-104:];qs,end,eh=c.trace(w,h,p);d=c.minus(end,p)
 assert c.tail(f,p,h,w)
 return static,reads,qs,d,w

def required_guard(row):
 static,reads,qs,d,w=replay(row)
 max_need=-1;worst=None;static_indices=[];probes=0
 # For every class, union_{k>=K}(D0+k*BACK) is exactly the half-ray
 # starting at class_min+K. This uses support union, NOT XOR.
 def inspect(q,label):
  nonlocal max_need,worst
  key,z=c.orbitkey(q,BACK)
  if key in MINS:
   need=z-MINS[key]+1
   if need>max_need:max_need=need;worst=(q,key,z,MINS[key],label)
  for b,e,lo,hi in static:
   j=c.multiple(c.minus(q,b),e)
   if j is not None:static_indices.append(j)
 for q in reads:inspect(q,'finite read')
 for q in qs:
  # Inspect all tail visits that can fall on a discrepancy translation class.
  for key,lower in MINS.items():
   if d==BACK:
    k,z=c.orbitkey(q,BACK)
    assert k!=key,('no uniform incoming-gap bound; tail meets moving old cap',row['rotation'],row['a'],row['s'],q,key)
   elif d==c.times(-1,BACK):
    k,z=c.orbitkey(q,BACK)
    if k==key:inspect(q,'backward parallel maximum')
   else:
    hit=c.intersect(q,d,key,BACK,None,None)
    if hit is not None:
     assert hit[0]==hit[1];inspect(c.plus(q,c.times(hit[0],d)),'transverse tail hit')
   probes+=1
  # Static-rail truncation must preserve every old-rail read, not merely
  # net XOR black values, because incoming rail can cancel a crossing cell.
  for b,e,lo,hi in static:
   hit=c.intersect(q,d,b,e,None,None)
   if hit is not None:
    assert hit[1] is not None and hit[0]==hit[1],('infinite static rail required',q,b,e)
    r=c.plus(q,c.times(hit[0],d));j=c.multiple(c.minus(r,b),e)
    assert j is not None;static_indices.append(j)
 K=max(0,max_need);M=max(abs(j) for j in static_indices)
 # Static e has zero coordinate sum, while increasing gap reduces it by4.
 assert all(sum(e)==0 for _,e,_,_ in static)
 assert max(sum(b) for b,_,_,_ in static)-4*K < min(map(sum,SEED))
 # Reconstruct the COMPLETE actual finite input at the least protected gap.
 # This is an additional independent control; coverage is the guard above.
 rail={c.plus(c.plus(b,c.times(K,c.D)),c.times(j,e)) for b,e,_,_ in static for j in range(-M,M+1)}
 assert len(rail)==12*(2*M+1) and not rail&SEED
 B=SEED|rail;p=(0,0);h=c.H0;t0=row['t0']+104*K
 for t in range(t0+len(row['word'])):
  p,h,ch=step(B,p,h)
  expected=c.WORD[t%104] if t<t0 else row['word'][t-t0]
  assert ch==expected,('finite physical transfer mismatch',row['rotation'],row['a'],row['s'],K,M,t)
 assert certify_period(B,p,h,w)
 delta=c.times(K,c.D)
 assert p==c.plus(tuple(row['pose'][0]),delta) and h==row['pose'][1]
 return dict(rotation=row['rotation'],a=row['a'],s=row['s'],
  minimum_certified_gap_periods=K,minimum_symmetric_rail_half_length=M,
  minimum_input_mass=13+12*(2*M+1),
  first_contact_time=[104,row['t0']],capture_time=[104,row['capture']],
  capture_pose_constant=row['pose'],capture_pose_k_coefficient=c.D,
  outgoing_drift=row['cert']['drift'],recovery=row['recovery'],
  static_line_bases=[b for b,_,_,_ in static],static_direction=static[0][1],
  gap_guard_witness=worst,static_index_range=[min(static_indices),max(static_indices)],
  infinite_ray_class_tests=probes,
  scope='all integer gap k>=K and half-length M>=M0; pristine crossing data, complete13cell incoming seed')

def main():
 assert certify_period(SEED,(0,0),c.H0,c.WORD)
 rows=json.loads((HERE/'crossings_discovery.json').read_text())
 odd=[r for r in rows if r['s']%2]
 assert len(odd)==8 and {(r['rotation'],r['a'],r['s']) for r in odd}=={(r,a,s) for r in (1,3) for a in (0,1) for s in (1,3)}
 out=[]
 for r in rows:
  if r['s']%2:
   result=required_guard(r);out.append(result);print(json.dumps(result),flush=True)
 result={'status':'uniform exact finite-support transfer passed',
  'input_discrepancy_class_minima':[(k,v) for k,v in sorted(MINS.items())],
  'uniform_gap_K':max(r['minimum_certified_gap_periods'] for r in out),
  'uniform_half_length_M':max(r['minimum_symmetric_rail_half_length'] for r in out),
  'records':out}
 (HERE/'finite_transfer_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
