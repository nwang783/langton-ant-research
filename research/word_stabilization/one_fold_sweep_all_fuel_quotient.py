"""Finite conservative signed-separation quotient of the exact one-fold sweep.
Far distances keep residue mod4 and may return to the near band prematurely.
No-hit exhaustive closure can therefore certify the original unbounded sweep.
"""
from collections import deque,Counter
from pathlib import Path
import json,sys,time
import one_fold_sweep_all_fuel as S
ROOT=Path(__file__).parent
D=8

def shift_new(s,amount):
 dx,dy,flags,items=s;out=[]
 for x,y,v in items:
  assert not v&S.F,('fold read in far band',s)
  old=bool(v&S.X);new=bool(v&S.Y)
  assert old!=new,('mixed/unassigned far cell',s)
  if old:assert -2<=x<=3,('old support bound',x,s)
  else:assert -2<=x-dx<=3,('new support bound',x-dx,s)
  out.append((x+(amount if new else 0),y,v))
 return(dx+amount,dy,flags,tuple(sorted(out)))

def canonical(s):
 dx=s[0]
 if dx<=-D:return shift_new(s,-D-((-dx-D)%4)-dx)
 if dx>=D:return shift_new(s,D+((dx-D)%4)-dx)
 return s

def successors(s):
 if abs(s[0])>=D:shift_new(s,0) # Check the finite symbolic support invariant.
 for a,t,hit in S.steps(s):
  if hit:yield a,t,True;continue
  if s[0]==-D and t[0]==-D+1:
   yield a,canonical(shift_new(t,-4)),False
  if s[0]==D and t[0]==D-1:
   yield a,canonical(shift_new(t,4)),False
  yield a,canonical(t),False

def main():
 todo=deque();seen={};edges=[];start=time.time()
 for f in'QB':
  s=S.initialize(f);seen[s]=len(seen);todo.append(s)
 while todo:
  s=todo.popleft();sid=seen[s]
  for a,t,hit in successors(s):
   if hit:print('ABSTRACT HIT',sid,a,flush=True);return
   if t not in seen:seen[t]=len(seen);todo.append(t)
   edges.append((sid,a,seen[t]))
  if len(seen)>1000000:print('CAP',len(seen));return
 print('EXHAUSTED NO HIT',len(seen),'states',len(edges),'edges','elapsed',time.time()-start,flush=True)
 out={'status':'no hit in finite conservative quotient','far_threshold':D,'states':list(seen),'edges':edges,'initial_ids':[seen[S.initialize(f)]for f in'QB']}
 (ROOT/'one_fold_sweep_all_fuel_certificate.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':main()
