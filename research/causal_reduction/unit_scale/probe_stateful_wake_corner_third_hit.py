"""One predicted third hit, with EVERY prior cell retained and a supplied new incoming interface.
Not a single-ant route, not a renewable certificate.
"""
from pathlib import Path
import json,hashlib
from probe_perpendicular_highway_wake import H,shifted_seed,step
from probe_thin_loop_scattering import R,check,G
P=Path(__file__).resolve().parent
z=json.loads((P/'stateful_wake_corner_second_hit.json').read_text())
B=set(map(tuple,z['second_output_black']));p=tuple(z['pose'][0]);h=z['pose'][1]
for c in H[z['phase']:]+H*100:
 p,h,a=step(B,p,h);assert a==c
previous=set(B);oldpose=(p,h)
p=(327,-300);h=0;S=shifted_seed(3,p);assert not B&S;B|=S;initial=set(B)
chars=[];segments=[];sig=None;out=None
for t in range(500000):
 p,h,c=step(B,p,h);chars.append(c)
 if t>=104 and t%104==0:
  phase=R.get(''.join(chars[-104:]))
  if phase is not None:
   d=G[phase,h][0];good=check(B,p,phase,h)
   if sig!=(phase,h):segments.append(dict(t=t+1,p=p,h=h,phase=phase,drift=d,exact_tail=good));sig=phase,h
   if good:
    out=dict(status='EXACT_LITERAL_TAIL',time=t+1,pose=[p,h],phase=phase,drift=d);break
  else:sig=None
if out is None:out=dict(status='UNKNOWN_HORIZON',time=500000,pose=[p,h])
out.update(scope=__doc__,previous_departure_pose=oldpose,incoming_start=[327,-300,'N'],previous_mass=len(previous),initial_mass=len(initial),output_mass=len(B),previous_black_erased=len(previous-B),full_xor_count=len(initial^B),segments=segments,word=''.join(chars),initial_black=sorted(initial),output_black=sorted(B),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'stateful_wake_corner_third_hit.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items()if k not in('word','initial_black','output_black')})
