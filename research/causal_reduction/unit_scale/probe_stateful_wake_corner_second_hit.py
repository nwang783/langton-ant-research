"""One stateful second-hit test with complete first-output ownership.
The second incoming ant is a supplied interface, NOT an executed return route.
Its lane15 is the nearest larger same phase disjoint from the first lane3 reads.
"""
from pathlib import Path
import json,time,hashlib
from probe_perpendicular_highway_wake import H,shifted_seed,step
from probe_thin_loop_scattering import R,check,G
P=Path(__file__).resolve().parent
C=json.loads((P/'opposite_wake_quarter_turn_word.json').read_text())['word']
def run(n=100,m=100,l=100,M=150,limit=500000):
 B=shifted_seed(2,(-2*n,-2*n));p=(-2*n,-2*n);h=1
 for c in H*(2*n):p,h,a=step(B,p,h);assert a==c
 old=set(B);S=shifted_seed(3,(2*m+3,-2*m));assert not B&S;B|=S;p=(2*m+3,-2*m);h=0
 for c in H*(m-10)+C+H*l:p,h,a=step(B,p,h);assert a==c
 first_output=set(B);first_pose=(p,h)
 p=(2*M+15,-2*M);h=0;S=shifted_seed(3,p);assert not B&S;B|=S;initial=set(B);word=[];segments=[];sig=None
 for t in range(limit):
  p,h,c=step(B,p,h);word.append(c)
  if t>=104 and t%104==0:
   phase=R.get(''.join(word[-104:]))
   if phase is not None:
    d=G[phase,h][0];good=check(B,p,phase,h)
    if sig!=(phase,h):segments.append(dict(t=t+1,p=p,h=h,phase=phase,drift=d,exact_tail=good));sig=phase,h
    if good:
     return dict(status='EXACT_LITERAL_TAIL',scope=__doc__,n=n,m=m,first_tail_periods=l,first_ant_departure_pose=first_pose,second_M=M,second_start=[2*M+15,-2*M,'N'],first_output_mass=len(first_output),total_initial_mass=len(initial),time=t+1,pose=[p,h],phase=phase,drift=d,mass=len(B),first_output_erased=len(first_output-B),second_full_xor_count=len(initial^B),segments=segments,word=''.join(word),first_output_black=sorted(first_output),second_initial_black=sorted(initial),second_output_black=sorted(B),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
   else:sig=None
 return dict(status='UNKNOWN_HORIZON',time=limit,pose=[p,h],segments=segments,word=''.join(word))
if __name__=='__main__':
 z=run();(P/'stateful_wake_corner_second_hit.json').write_text(json.dumps(z,indent=2)+'\n');print({k:v for k,v in z.items()if k not in('word','first_output_black','second_initial_black','second_output_black')})
