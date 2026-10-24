"""Concrete two-corner routing controls for the prepared1564 five-band target.
Only the retained one-turn phase inventory is used. Finite controls are not
an all-parameter connected preparation proof.
"""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H']
V=((0,1),(1,0),(0,-1),(-1,0))

def corner(a,c,b):return H[:a]+c+(H[b:] if b else '')
ROUTES=[('initial_to_A',corner(68,'R',0),18,corner(68,'R',0),(-41,45,3)),
 ('A_to_B',corner(24,'L',30),15,corner(24,'L',30),(35,-31,3)),
 ('B_to_C',corner(68,'R',0),5,corner(68,'R',102),(-16,18,3))]

def trace(w,p=(0,0),h=1):
 for i,c in enumerate(w):
  yield i,p,h,c
  h=(h+(1 if c=='R' else -1))%4;dx,dy=V[h];p=(p[0]+dx,p[1]+dy)
 yield len(w),p,h,None

def infer(w,p=(0,0),h=1):
 first={};last={};B=set();xor=set();bad=None
 for i,q,g,c in trace(w,p,h):
  if c is None:break
  if q in last and last[q][1]==c:
   bad=[q,last[q],[i,c]];break
  if q not in first:
   first[q]=(i,c)
   if c=='L':B.add(q)
  last[q]=(i,c);xor.symmetric_difference_update({q})
 return dict(bad=bad,input=B,xor=xor,first=first,end=[q,g],reads=i)

def main():
 out=[]
 for name,a,k,b,end in ROUTES:
  w=a+H*k+b;ev=list(trace(w));assert tuple(ev[-1][1])+(ev[-1][2],)==end
  c=infer(H*30+w+H*30);S=infer(H*30)['input'];assert len(S)==13
  extra=c['input']-S
  out.append(dict(name=name,middle_periods=k,word=w,router_length=len(w),endpoint=end,
    finite_control_bad=c['bad'],finite_input_mass=len(c['input']),extra_count=len(extra),
    extra_relative_router=sorted((x-60,y-60)for x,y in extra),finite_reads=c['reads']))
 (P/'prepared1564_router_geometry.json').write_text(json.dumps(out,indent=2)+'\n')
 for z in out:print({k:v for k,v in z.items()if k not in('word','extra_relative_router')})
if __name__=='__main__':main()
