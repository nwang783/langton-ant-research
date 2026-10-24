"""Literal all-length packet geometry after the separately proved saturated
LL/RR matching. Controls check formulas; they are not a period/length scan.
"""
from pathlib import Path
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def move(word):
 p=(0,0);h='N';trail=[p]
 for t in word:
  h=H[(H.index(h)+(1 if t=='R'else-1))%4];p=p[0]+V[h][0],p[1]+V[h][1];trail.append(p)
 return p,h,trail
rows=[]
for name,w,target in [('passive','RRLL',(2,0)),('genuine','RLLR',(0,2)),('singleton','RL',(1,1))]:
 p,h,tr=move(w);assert(p,h)==(target,'N');rows.append(dict(name=name,word=w,displacement=p,ending_heading=h,trail=tr))
for q in [0,1,2,7]:
 w='RLRLR'+'LLRR'*q+'L';p,h,tr=move(w);assert(p,h)==((3,3+2*q),'N');rows.append(dict(name='high',later_RR=q,word=w,displacement=p,ending_heading=h,trail=tr))
# Symbolic induction: each inserted LLRR before final L adds exactly(0,2).
# Compare prefixes, whose final heading is E for every q; LLRR at E adds(0,2).
p,h,_=move('RLRLR');assert h=='E'
for q in range(3):
 pp,hh,_=move('RLRLR'+'LLRR'*q);nn,nh,_=move('RLRLR'+'LLRR'*(q+1));assert hh==nh=='E'and(nn[0]-pp[0],nn[1]-pp[1])==(0,2)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,packets=rows,all_q_induction='RLRLR ends E; LLRR at E returns E and adds(0,2); final L adds(0,1)',full_drift_formula=['Dx=2p+s+3h','Dy=2g+s+3h+2q','ell=4p+4g+2s+6h+4q'],warning='This certifies literal geometry only. The exact cyclic partition and axis exclusions require the named signed dependencies; no actual factor or complete front constructed.'),indent=2)+'\n');print('PASS packet displacements, shared heading, symbolic all-q high rail')
