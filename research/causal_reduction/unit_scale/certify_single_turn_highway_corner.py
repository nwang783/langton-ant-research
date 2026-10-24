"""Exact all-length prepared ten-cell right-angle standard104 interface.
No finite-repeat inference. Whole finite input and output fields are retained.
"""
from pathlib import Path
import json,sys,hashlib,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,xor
from probe_perpendicular_highway_wake import H,shifted_seed,step
st=time.monotonic();ctx=Context(max_operations=100000000)
def S(c):return ctx.set('[m]->{[x,y]:m>=3 and ('+c+')}')
def pts(ps):return S(' or '.join(f'(x={x} and y={y})'for x,y in ps)or'false')
# Exact board/pose after68 reads of the SE canonical front, normalized to0.
base=shifted_seed(1,(0,0));p=(0,0);h=2
for c in H[:68]:p,h,a=step(base,p,h);assert a==c
base={(x-p[0],y-p[1])for x,y in base};assert h==0 and len(base)==23
F=H[68:]+H[:68];rows,end,hh=trace(F,(0,0),h);assert(end,hh)==((2,-2),0)
K=[(1,4),(1,5),(1,6),(2,0),(2,1),(2,2),(2,5),(3,0),(3,3),(3,4)]
markers=S(' or '.join(f'(x=2*m+{x} and y=-2*m+{y})'for x,y in K))
parity=S('false');reads=S('false')
for q,hh,c in rows:
 f=S(f'exists(i:0<=i<m and x={q[0]}+2*i and y={q[1]}-2*i)')
 parity=xor(parity,f);reads=reads.union(f)
assert markers.intersect(reads).is_empty();assert markers.intersect(pts(base)).is_empty()
initial=pts(base).union(markers);before=xor(initial,parity)
cap=S('x=2*m and y=-2*m');assert before.intersect(cap).is_empty()
after=xor(before,cap)
# Output canonical104 starts at(2m+1,-2m,E), with NE drift(2,2).
rows,ep,eh=trace(H,(1,0),1);assert(ep,eh)==((3,2),1)
Fams=[]
for j,(q,hh,c)in enumerate(rows):
 f=S(f'exists(i:i>=0 and x=2*m+{q[0]}+2*i and y=-2*m+{q[1]}+2*i)')
 Fams.append((f,j-52*q[0],c))
prior=0
for f,tf,c in Fams:
 ctx.reset_operations();black=after.intersect(f)
 for g,tg,cg in Fams:
  if tg>=tf:continue
  old=f.intersect(g)
  if not old.is_empty():prior+=1;black=xor(black,old)
 bad=f.subtract(black)if c=='L'else black
 assert bad.is_empty(),str(bad)
# Describe the finite corner changes to K under the first complete outgoing block.
cut={};odd=set()
for q,hh,c in rows:cut.setdefault(q,c);odd.symmetric_difference_update({q})
used=[q for q in K if q in cut];erased=[q for q in K if q in odd];unread=[q for q in K if q not in cut]
out=dict(status='EXACT_ALL_M_PREPARED_QUARTER_TURN',domain='integer m>=3',input_phase=68,input_word=F,input_heading='N',input_drift=[2,-2],base_seed=sorted(base),base_mass=len(base),corner_relative_black=K,corner_translate=['2*m','-2*m'],corner_mass=10,total_initial_mass=33,word='F^m R H^infinity',output_time='104*m+1',output_pose=['2*m+1','-2*m','E'],output_drift=[2,2],initial_relation=str(initial),entry_before_R_relation=str(before),output_relation=str(after),tail_prior_relations=prior,corner_read_in_first_outgoing_block=used,corner_erased_after_first_outgoing_block=erased,corner_unread_in_first_outgoing_block=unread,complete_outgoing_first_block_xor_relative_cap=sorted(odd),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-st)
(P/'single_turn_highway_corner_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('initial_relation','entry_before_R_relation','output_relation','input_word','base_seed','complete_outgoing_first_block_xor_relative_cap')})
