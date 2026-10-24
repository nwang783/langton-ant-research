"""Concrete four phase-compatible right-turn interfaces, not a generic corner scan.
Full literal first-color inference constructs each finite seed.
"""
from pathlib import Path
import json
from probe_perpendicular_highway_wake import H,step
from certify_highway_wake_reflector import trace
from probe_thin_loop_scattering import R,check,G as GUARD
P=Path(__file__).resolve().parent
G=H
def loop_word(n):return('R'+G*n+G[:14])*4

def make(n):
 w=loop_word(n);rr,p,h=trace(w,(0,0),2);assert(p,h)==((0,0),2)
 first={};last={};odd=set()
 for t,(q,hh,c)in enumerate(rr):
  if q in last:assert last[q]!=c,(n,t,q)
  else:first[q]=c
  last[q]=c;odd.symmetric_difference_update({q})
 seed={q for q,c in first.items()if c=='L'};return seed,seed^odd

def run(n,limit=500000):
 seed,B=make(n);p=(0,0);h=2;word=[];samples=[]
 for t in range(limit):
  p,h,c=step(B,p,h);word.append(c)
  if t>=104 and t%104==0:
   phase=R.get(''.join(word[-104:]))
   if phase is not None:
    good=check(B,p,phase,h);d=GUARD[phase,h][0]
    if not samples or (samples[-1]['phase'],samples[-1]['h'])!=(phase,h):samples.append(dict(t=t+1,p=p,h=h,phase=phase,drift=d,exact_tail=good))
    if good:return dict(n=n,status='EXACT_LITERAL_TAIL',initial_mass=len(seed),loop_length=len(loop_word(n)),postloop_mass=len(make(n)[1]),origin_postloop_black=(0,0)in make(n)[1],time=t+1,pose=[p,h],phase=phase,drift=d,mass=len(B),segments=samples,word=''.join(word))
 return dict(n=n,status='UNKNOWN_HORIZON',time=limit,pose=[p,h],segments=samples,word=''.join(word))
if __name__=='__main__':
 out=[]
 for n in[50,100,200]:
  z=run(n);out.append(z);print({k:v for k,v in z.items()if k!='word'},flush=True)
 (P/'clockwise_fiftytwo_loop_controls.json').write_text(json.dumps(out,indent=2)+'\n')
