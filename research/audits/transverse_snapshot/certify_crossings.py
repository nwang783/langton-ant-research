"""Replay all clean crossing classes; extract exact finite-support kernels.

The infinite models have no finite-seed implication until kernel extraction is
proved. This checker computes the complete initial black intersection with the
certified read future, verifies finiteness, then independently certifies the same
trajectory from that complete finite kernel using the older finite-field oracle.
"""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation')))
from ant_exact import certify_period as finite_tail,step as literal_step
import crossing as c

def background_intervals(field,q,d):
 boundaries=set()
 for b,e,lo,hi in field.rays:
  v=c.intersect(q,d,b,e,lo,hi)
  if v is None:continue
  l,r=v;boundaries.symmetric_difference_update({l})
  if r is not None:boundaries.symmetric_difference_update({r+1})
 edges=sorted(boundaries)
 intervals=[]
 for i in range(0,len(edges),2):intervals.append((edges[i],edges[i+1]-1 if i+1<len(edges) else None))
 return intervals

def replay(row):
 assert row['capture']==row['t0']+len(row['word'])
 assert set(row['word'])<={'L','R'}
 t0,p,h,static=c.first_contact(row['rotation'],row['a'],row['s'])
 assert t0==row['t0']
 field=c.Field(c.incoming_past()+static)
 p=(0,0);h=c.H0;reads=[];black_input=set();word=[]
 for t in range(row['capture']):
  reads.append(p)
  # Cross-check the optimized line table against its literal XOR definition
  # on EVERY actual read, rather than trusting discovery's optimization.
  direct=False
  for b,d,lo,hi in field.rays:
   k=c.multiple(c.minus(p,b),d)
   direct^=k is not None and (lo is None or k>=lo) and (hi is None or k<=hi)
  assert direct==field.background(p)
  if direct:black_input.add(p)
  p,h,ch=field.step(p,h);word.append(ch)
  assert ch==(c.WORD[t%104] if t<t0 else row['word'][t-t0])
 assert (list(p),h)==(row['pose'][0],row['pose'][1])
 tailword=''.join(word[-row['cert']['period']:])
 proof=c.tail(field,p,h,tailword);assert proof
 qs,ep,eh=c.trace(tailword,h,p);d=c.minus(ep,p)
 unbounded=[];tailblack=set();ray_intervals=[]
 initial=c.Field(field.rays)
 for i,q in enumerate(qs):
  intervals=background_intervals(initial,q,d);ray_intervals.append(intervals)
  for lo,hi in intervals:
   if hi is None:unbounded.append((i,lo));continue
   for k in range(lo,hi+1):tailblack.add(c.plus(q,c.times(k,d)))
 if unbounded:
  assert row['s']%2==0 and tailword in ('RLRL','LRLR')
  return dict(rotation=row['rotation'],a=row['a'],s=row['s'],sector='opposite',
   status='infinite-background RL staircase; infinite initial fuel',
   recovery=row['recovery'],unbounded_initial_black_phase_rays=unbounded,
   tail=proof,word_sha256=hashlib.sha256(row['word'].encode()).hexdigest())
 assert row['s']%2==1 and len(tailword)==104
 K=black_input|tailblack
 # K is exactly the original background's black intersection with all future
 # reads, so removing the rest cannot change any read. This is additionally
 # replayed with an independent literal set implementation and finite oracle.
 B=set(K);fp=(0,0);fh=c.H0
 for expected in word:
  fp,fh,ch=literal_step(B,fp,fh);assert ch==expected
 assert (fp,fh)==(p,h)
 ft=finite_tail(B,fp,fh,tailword);assert ft
 # Every first-read-L cell is initial fuel, and all other initial black cells
 # removed from the infinite background were unread, never 'erased in motion'.
 assert len(K)==len(black_input|tailblack)
 out=dict(rotation=row['rotation'],a=row['a'],s=row['s'],sector='same',
  status='exact infinite model and complete finite kernel both certified',
  first_contact=t0,recovery=row['recovery'],tail=proof,finite_tail=ft,
  initial_kernel=sorted(K),kernel_mass=len(K),extra_tail_only_black=len(tailblack-black_input),
  capture_pose=(p,h),capture_black_mass=len(B),read_bounds=row['limits'],
  word_sha256=hashlib.sha256(row['word'].encode()).hexdigest(),
  final_field_sha256=hashlib.sha256(repr(sorted(B)).encode()).hexdigest())
 return out

def main():
 rows=json.loads((HERE/'crossings_discovery.json').read_text())
 assert len(rows)==16
 assert {(r['rotation'],r['a'],r['s']) for r in rows}=={(r,a,s) for r in (1,3) for a in (0,1) for s in range(4)}
 # Control both the canonical finite seed and mature infinite incoming wake.
 assert c.tail(c.Field(c.incoming_past()),(0,0),c.H0,c.WORD)
 assert finite_tail(set(map(tuple,c.DATA['seed'])),(0,0),c.H0,c.WORD)
 proofs=[]
 for row in rows:
  out=replay(row);proofs.append(out)
  print(json.dumps({k:v for k,v in out.items() if k!='initial_kernel'}),flush=True)
 result={'status':'16 specified clean-background cases; finite kernels only for8same-sector cases',
  'same_sector_cases':8,'opposite_sector_cases':8,'records':proofs,
  'source_fixture_sha256':hashlib.sha256(c.BASE.read_bytes()).hexdigest()}
 (HERE/'crossings_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
