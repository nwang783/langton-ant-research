"""One rigorous finite-input counterexample to a clockwise-only scattering rule.

The infinite opposed-wake reference is converted to a complete finite seed,
then to an all-gap/all-length finite family by explicit future-read guards.
"""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import model as m
c=m.c
sys.path.insert(0,str(HERE.parent/'transverse'))
from certify_crossings import background_intervals,literal_step,finite_tail
from certify_finite_transfer import MINS,BACK,SEED

def main():
 row=next(r for r in json.loads((HERE/'discovery.json').read_text()) if (r['a'],r['z'])==(0,-6))
 assert row['sector']=='same' and row['n']==20
 assert set(row['word'])<={'R','L'} and set(c.WORD)<={'R','L'}
 static=m.abandoned(0,-6,20)
 assert m.first_contact(static)==row['t0']==1797
 f=c.Field(c.incoming_past()+static);initial=c.Field(f.rays)
 p=(0,0);h=c.H0;reads=[];word=[];KERNEL=set()
 for t in range(row['capture']):
  reads.append(p);direct=False
  for b,e,lo,hi in f.rays:
   j=c.multiple(c.minus(p,b),e)
   direct^=j is not None and j>=lo and (hi is None or j<=hi)
  assert direct==initial.color(p)
  if direct:KERNEL.add(p)
  p,h,ch=f.step(p,h);word.append(ch)
  assert ch==(c.WORD[t%104] if t<row['t0'] else row['word'][t-row['t0']])
 assert (list(p),h)==(row['pose'][0],row['pose'][1])
 w=''.join(word[-104:]);assert w in c.PHASES and c.PHASES[w]==9
 proof=c.tail(f,p,h,w);assert proof and proof['drift']==(2,-2)
 qs,ep,eh=c.trace(w,h,p);d=c.minus(ep,p)
 for q in qs:
  for lo,hi in background_intervals(initial,q,d):
   assert hi is not None
   for j in range(lo,hi+1):KERNEL.add(c.plus(q,c.times(j,d)))
 B=set(KERNEL);bp=(0,0);bh=c.H0
 for ch in word:
  bp,bh,actual=literal_step(B,bp,bh);assert actual==ch
 assert (bp,bh)==(p,h) and finite_tail(B,bp,bh,w)
 # Uniform guards. Incoming missing-cap support after k extra clean periods
 # is D0+k*BACK; the union for k>=K is the exact per-class half-ray.
 gap=0;maxold=-1;minimumold=0
 def inspect(q):
  nonlocal gap,maxold,minimumold
  key,z=c.orbitkey(q,BACK)
  if key in MINS:gap=max(gap,z-MINS[key]+1)
  for b,e,lo,hi in static:
   j=c.multiple(c.minus(q,b),e)
   if j is not None and j>=lo:
    assert hi is None
    maxold=max(maxold,j);minimumold=min(minimumold,j)
 for q in reads:inspect(q)
 for q in qs:
  for key,lower in MINS.items():
   hit=c.intersect(q,d,key,BACK,None,None)
   if hit:
    assert hit[0]==hit[1]
    inspect(c.plus(q,c.times(hit[0],d)))
  for b,e,lo,hi in static:
   hit=c.intersect(q,d,b,e,lo,hi)
   if hit:
    assert hit[0]==hit[1]
    inspect(c.plus(q,c.times(hit[0],d)))
 length=maxold+1
 assert finite_tail(SEED,(0,0),c.H0,c.WORD)
 assert all(sum(e)==-4 for _,e,_,_ in static)
 assert max(sum(b) for b,_,_,_ in static)-4*gap<min(map(sum,SEED))
 # All reference static first-contact intervals start nonnegative; translating
 # by kD adds exactly k to every epoch boundary, hence104k to first contact.
 for q in c.READS:
  for b,e,lo,hi in static:
   assert e==c.D and lo==0 and hi is None
   start=c.multiple(c.minus(b,q),c.D)
   if start is not None:assert start>=0
 # Replay the complete finite seed at the least guarded parameters.
 old=set()
 for b,e,lo,hi in static:
  for j in range(length):old.symmetric_difference_update({c.plus(c.plus(b,c.times(gap,c.D)),c.times(j,e))})
 assert not old&SEED
 actualseed=old|SEED;B=set(actualseed);bp=(0,0);bh=c.H0
 allword=c.WORD*gap+''.join(word)
 for ch in allword:
  bp,bh,got=literal_step(B,bp,bh);assert got==ch
 assert bp==c.plus(p,c.times(gap,c.D)) and bh==h and finite_tail(B,bp,bh,w)
 out={'status':'exact left-turn finite kernel and uniform finite transfer certified',
  'reference':{'a':0,'z':-6,'n':20,'rotation':2,'sector':'same'},
  'first_contact':1797,'recovery':5201,'capture_time':[104,len(word)],
  'capture_pose_constant':[p,h],'capture_pose_k_coefficient':c.D,
  'outgoing_drift':d,'canonical_incoming_drift':c.D,
  'kernel_mass':len(KERNEL),'finite_kernel':sorted(KERNEL),
  'uniform_parameter_domain':{'integer_gap_k_at_least':gap,'integer_old_period_count_M_at_least':length},
  'least_input_mass':len(actualseed),'least_complete_input':sorted(actualseed),
  'word_sha256':hashlib.sha256(row['word'].encode()).hexdigest(),
  'finite_prefix_reads':len(reads),'infinite_phase_rays_checked':len(qs)}
 (HERE/'left_turn_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('finite_kernel','least_complete_input')},indent=2))
if __name__=='__main__':main()
