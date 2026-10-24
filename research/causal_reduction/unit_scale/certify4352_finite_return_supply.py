"""All-M finite-original supply for the opposite15324 output-consumer wave.
Set the signed394-cell producer's parameter N=3M+C. Compare its ENTIRE
normalized checkpoint field against the source-end ray field in a growing
window covering the actual transition and M return periods. Every field
coefficient is an XOR of exact integer intervals with affine-M endpoints.
"""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction
import json,hashlib
from probe4352_source_endpoint_limit import build,trace,key,z,V
from check4352_noncrossing_producer import W
P=Path(__file__).resolve().parent
J=json.loads((P/'prepared4352_uniform_support_manifest.json').read_text())
A=json.loads((P/'prepared4352_output_return_wave.json').read_text())
C=4
# Checkpoint limit BEFORE the three extra waves and the partial fourth.
b,p,h=build();extra=W*3+W[:2331]
for _,q,hh,c in list(trace(extra,(-2,3),3))[:-1]:b.toggle(q)
# Current normalized window: -156M-26 <= u <=291, -100<=t<=110.
events=defaultdict(Counter);background=Counter();families=0

def add_interval(k,lo,hi):
 global families
 # inclusive endpoints, both affine-M pairs(slope,constant)
 events[k][lo]^=1;events[k][(hi[0],hi[1]+1)]^=1;families+=1

def add_point_family(q,a):
 # q+a*N, then subtract(26N,26N), with N=3M+C.
 ax=a[0]-26;ay=a[1]-26;assert ax==ay and (3*ax)%26==0
 qq=(q[0]+C*ax,q[1]+C*ay);k=key(qq);line=(3*ax//26,z(qq));add_interval(k,line,line)

for st in J['stages']:
 start=(st['start_x_N_constant'][1],st['start_y_N_constant'][1]);a=(st['start_x_N_constant'][0],st['start_y_N_constant'][0]);cc,cd=st['count_N_constant'];rr=list(trace(st['word'],start,st['heading']));d=rr[-1][1][0]-start[0]
 if(cc,cd)==(0,1):
  for _,q,hh,c in rr[:-1]:add_point_family(q,a)
  continue
 assert rr[-1][1][1]-start[1]==d and d in(-2,2,26)
 residues=26//abs(d);assert (3*cc)%residues==0
 for _,q,hh,c in rr[:-1]:
  ax=a[0]-26;ay=a[1]-26;assert ax==ay and 3*ax%26==0
  for r in range(residues):
   qq=(q[0]+C*ax+d*r,q[1]+C*ay+d*r);k=key(qq);startline=(3*ax//26,z(qq))
   # l=0,...,floor((count-1-r)/residues).
   ls=3*cc//residues;lc=(cc*C+cd-1-r)//residues;assert ls+lc>=0
   sign=1 if d>0 else-1;endline=(startline[0]+sign*ls,startline[1]+sign*lc)
   add_interval(k,startline if sign>0 else endline,endline if sign>0 else startline)
for x,y in J['seed_families']:add_point_family((x[1],y[1]),(x[0],y[0]))
# XOR with the exact infinite checkpoint board.
for k in b.full:background[k]^=1
for k,cuts in b.rays.items():
 for cut in cuts:background[k]^=1;events[k][(0,cut+1)]^=1
for q in b.F:add_interval(key(q),(0,z(q)),(0,z(q)))

reports=[];tests=0;max_break=1
for k in sorted(set(events)|set(background)):
 t,a=k
 if not(-100<=t<=110):continue
 # ceil((-26-2a+t)/52)-3M.
 low=(-3,-((26+2*a-t)//52))
 high=(0,(291-2*a+t)//52+1) # exclusive upper bound
 lines=[line for line,bit in events[k].items()if bit]+[low,high]
 cuts={1}
 for i,l in enumerate(lines):
  for r in lines[:i]:
   den=l[0]-r[0]
   if not den:continue
   f=Fraction(r[1]-l[1],den);n=f.numerator//f.denominator
   if n>=1:cuts.add(n)
   if n+1>=1:cuts.add(n+1)
 cuts.add(max(cuts)+1);max_break=max(max_break,max(cuts));tests+=len(cuts)
 for m in sorted(cuts):
  lo=low[0]*m+low[1];hi=high[1];changes=Counter()
  for (s,c),bit in events[k].items():
   if bit:changes[s*m+c]^=1
  bit=bool(background[k]);previous=None
  for at in sorted(changes):
   if bit and (previous is None or max(previous,lo)<min(at,hi)):
    # The preceding half-infinite interval also needs lo<at.
    if previous is None and lo>=min(at,hi):pass
    else:raise AssertionError(('field mismatch',k,m,previous,at,lo,hi))
   bit^=bool(changes[at]);previous=at
  assert not(bit and max(previous if previous is not None else lo,lo)<hi),('tail mismatch',k,m,lo,hi)
 reports.append([list(k),len(lines),sorted(cuts)])
# Check the finite transition on the exact limit checkpoint board.
p=(-2,3);h=3;transition=extra+A['prefix_word']
for i,c in enumerate(transition):
 assert b.color(p)==(c=='L'),(i,p,h,c)
 b.toggle(p);h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
assert(p,h)==((13,7),0)
rr=list(trace(A['word'],p,h));assert rr[-1][1]==(-65,-71)and rr[-1][2]==0
transrows=list(trace(transition,(-2,3),3))[:-1];assert min(sum(q)for _,q,hh,c in transrows)>=-26 and max(sum(q)for _,q,hh,c in transrows)<=291
assert min(sum(q)for _,q,hh,c in rr[:-1])>=-182 and max(sum(q)for _,q,hh,c in rr[:-1])<=21
assert min(q[0]-q[1]for _,q,hh,c in transrows+rr[:-1])>=-100 and max(q[0]-q[1]for _,q,hh,c in transrows+rr[:-1])<=110
out={'scope':__doc__,'status':'ALL-M COMPLETE-FIELD SUPPLY PASS','domain':'M>=1, producer N=3M+4','producer_N_M_constant':[3,C],'original_mass':394,'transition_after_N_waves':transition,'transition_length':len(transition),'return_word':A['word'],'return_periods':'M','return_entry_pose_normalized':[[13,7],0],'end_pose':[[0,26*C+13],[0,26*C+7],0],'end_time_M_constant':[129780,302553+38152*C],'comparison_window':{'u_low_M_constant':[-156,-26],'u_high':291,'t_range':[-100,110]},'affine_interval_families':families,'checked_orbit_classes':len(reports),'order_chambers_checked':tests,'largest_integer_order_break':max_break,'proof_digest':hashlib.sha256(json.dumps(reports,separators=(',',':')).encode()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_finite_return_supply.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('transition_after_N_waves','return_word')},indent=2))
