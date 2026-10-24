"""One geometrically derived fixed-mass ring assembly, not a controller search.
The52-cell clockwise ring is followed by three retained exterior corners.
Every initial black is inferred from the FULL proposed prefix, then the same
single ant continues without resets. Exact finite-board104-tail checks are used.
"""
from pathlib import Path
import json,time
from probe_perpendicular_highway_wake import H,step
from certify_highway_wake_reflector import trace
from probe_thin_loop_scattering import R,check,G as GUARD
from probe_clockwise_fiftytwo_loop import loop_word,make
P=Path(__file__).resolve().parent
B=make(50)[1];p=(0,0);h=2;Z=''
for _ in range(314):p,h,c=step(B,p,h);Z+=c
assert(p,h)==((3,-1),2)
connector=Z+H*60+H[:68]+'R'+H*80+H[:68]+'R'+H*160+H[:68]+'R'+H*10

def prepared(n):
 w=loop_word(n)+connector;rr,p,h=trace(w,(0,0),2)
 first={};last={};odd=set()
 for t,(q,hh,c)in enumerate(rr):
  if q in last:assert last[q]!=c,('prefix conflict',n,t,q,c)
  else:first[q]=c
  last[q]=c;odd.symmetric_difference_update({q})
 seed={q for q,c in first.items()if c=='L'};old=make(n)[0]
 assert old<=seed
 return seed,seed^odd,p,h,len(w),sorted(seed-old)

def run(n,limit=1500000):
 seed,B,p,h,t0,extra=prepared(n);chars=[];segments=[];attempts=0;seenphase=None
 for t in range(limit):
  p,h,c=step(B,p,h);chars.append(c)
  if t>=104 and t%104==0:
   phase=R.get(''.join(chars[-104:]))
   if phase is not None:
    good=check(B,p,phase,h);d=GUARD[phase,h][0];attempts+=1
    sig=(phase,h)
    if seenphase!=sig:segments.append(dict(t=t+1,absolute_time=t0+t+1,p=p,h=h,phase=phase,drift=d,exact_tail=good));seenphase=sig
    if good:return dict(n=n,status='EXACT_LITERAL_TAIL',initial_mass=len(seed),extra=extra,prefix_length=t0,continuation_time=t+1,pose=[p,h],phase=phase,drift=d,mass=len(B),segments=segments,word=''.join(chars))
   else:seenphase=None
 return dict(n=n,status='UNKNOWN_HORIZON',initial_mass=len(seed),extra=extra,prefix_length=t0,continuation_time=limit,pose=[p,h],segments=segments,word=''.join(chars))
if __name__=='__main__':
 st=time.monotonic();out=[]
 for n in[300,600,1200]:
  z=run(n);out.append(z);print({k:v for k,v in z.items()if k not in('word','extra')},flush=True)
 (P/'phase_repaired_wake_ring_v2_controls.json').write_text(json.dumps(dict(scope=__doc__,connector_word=connector,cases=out,seconds=time.monotonic()-st),indent=2)+'\n')
