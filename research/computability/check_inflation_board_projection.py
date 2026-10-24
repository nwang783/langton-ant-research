#!/usr/bin/env python3
"""Exact finite checks of the board-projection lemmas; no ant conjecture claim."""
import json
from pathlib import Path
from probe_inflation_projection import R,D,poly,mul,pw

def xor(items):
 s=set()
 for x in items:
  if x in s:s.remove(x)
  else:s.add(x)
 return s

def project(s):return xor(((x+1)//3,(y+1)//3)for x,y in s)
def plaque(x,y):return {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}
def vector(w):
 out=[0]*9
 for x,y in poly(w):
  a,r=divmod(x+1,3);b,s=divmod(y+1,3)
  out[3*r+s]^=mul(pw(2,a),pw(2,b))
 return out

def check():
 exceptions={'RRLRRRRLR':(0,-1),'RLRLLLLRL':(0,0),'LRLRRRRLR':(-1,0),'LLRLLLLRL':(-1,-1)}
 rows=[];guards=[]
 for c,ws in R['images'].items():
  for w in ws:
   error=project(poly(w))^{(0,0)}
   assert error==(plaque(*exceptions[w])if w in exceptions else set())
   rows.append(dict(coarse=c,word=w,toggle=sorted(poly(w)),block_toggle=sorted(project(poly(w))),error=sorted(error)))
   x=y=h=0;reads={}
   for turn in w:
    reads.setdefault((x,y),turn)
    h=(h+(1 if turn=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
   guards.append((c,reads))
 common=set.intersection(*(set(g)for c,g in guards));assert common=={(0,0)}
 assert {(c,g[(0,0)])for c,g in guards}=={('R','R'),('R','L'),('L','R'),('L','L')}
 pair='RRLRRRRLRRLRLLLLRL';error=project(poly(pair))^{(0,0),(1,0)}
 assert error=={(0,-1),(0,0),(2,-1),(2,0)}
 witness=[('RRRLRRLRL',1),('RRLRRRRLR',3),('RLRRLRRRR',1),('LLLRLLRLR',2),('RLLLLRLLR',1),('LRRLRRLRL',3)]
 total=[0]*9;rhs=0;parts=[]
 for w,c in witness:
  v=vector(w);total=[a^mul(c,b)for a,b in zip(total,v)];rhs^=c
  parts.append(dict(word=w,coefficient=c,vector=v))
 assert total==[0]*9 and rhs==3
 return dict(status='PASS exact finite auxiliary certificates, not an inflation exclusion',image_rows=rows,exception_count=len(exceptions),record_pair_error=sorted(error),six_image_witness=parts,weighted_vector=total,rhs=rhs,common_guard_cells=sorted(common))
if __name__=='__main__':
 out=check();Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('image_rows','six_image_witness')},indent=2))
