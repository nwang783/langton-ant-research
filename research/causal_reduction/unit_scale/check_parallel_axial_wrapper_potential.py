"""Literal field controls for the remote-column contract used in the analytic wrapper theorem."""
from pathlib import Path
import json,collections,hashlib
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent;U='RRLRRRRL';V='LLRLLRLL'
checks=0
for n in range(2,33):
 for h in(0,2):
  rr,e,g=core.trace(U*n+'R'+V*n,(0,0),h);d={};I=set();B=set()
  for t,(p,hh,c)in enumerate(rr):
   if p not in d:
    if c=='L':I.add(p);B.add(p)
   else:assert (p in B)==(c=='L')
   d[p]=c
   if p in B:B.remove(p)
   else:B.add(p)
  if h==0:
   for X in range(2,2*n):
    delta={p:int(p in B)-int(p in I)for p in I|B if p[0]==X and (p in B)!=(p in I)}
    assert delta=={(X,-2):1,(X,2):-1};assert sum(p[1]*v for p,v in delta.items())==-4;checks+=1
  else:assert max(p[0]for p in d)<=0;checks+=1
# A resource-balanced illustrative emitter: its first growing prefix is the
# literal blank52 return, and the next root layer uses opposed b+/b- shuttles.
p=(0,0);h=0;B=set();blank='';D=((0,1),(1,0),(0,-1),(-1,0))
for t in range(52):
 c='L'if p in B else'R';blank+=c
 if p in B:B.remove(p)
 else:B.add(p)
 h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];p=(p[0]+dx,p[1]+dy)
assert(p,h)==((0,0),0);A='RRRR';w=blank[4:];rows,_,_=core.trace(w,(0,0),0)
plus=next(t for t,(p,h,c)in enumerate(rows)if(h,c)==(0,'R'));minus=next(t for t,(p,h,c)in enumerate(rows)if(h,c)==(2,'R'))
def layer(n):return ''.join((U*n+'R'+V*n)if t in(plus,minus)else c for t,(p,h,c)in enumerate(rows))
seen={};first=None;word=A+layer(0)+layer(1)
for t,(p,h,c)in enumerate(core.trace(word,(0,0),0)[0]):
 if p in seen and seen[p][1]==c:first=dict(cell=p,previous=seen[p],current=[t,c]);break
 seen[p]=(t,c)
assert first
out=dict(scope=__doc__,column_controls=checks,root_base=A,emitter_word=w,emitter_charge=w.count('R')-w.count('L'),selected_plus_phase=plus,selected_minus_phase=minus,depth_two_conflict=first,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'parallel_axial_wrapper_potential_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
