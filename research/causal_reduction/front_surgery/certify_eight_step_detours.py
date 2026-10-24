"""Certify every legal pose-return insertion of length at most eight is finite-fuel.
The common exact open-window generator supplies constraints. Six failed-literal
checks supplement unconditional implication propagation. No complete SAT solver.
"""
import itertools,json,time
from collections import defaultdict
from window_library_rigidity import build_window,closure,known,HERE,walk,cl_rank,d,standard

def all_short_loops():
 out=[]
 for n in range(1,9):
  for z in itertools.product('RL',repeat=n):
   w=''.join(z);ev,end=walk(w)
   if end!=(0,0,0):continue
   seen={};ok=True
   for p,h,c in ev:
    if seen.get(p)==c:ok=False;break
    seen[p]=c
   if ok:out.append(w)
 return out

def certify():
 start=time.time();lib=all_short_loops();assert len(lib)==10
 N,eq,g,central,cells,opts=build_window(4,lib)
 b,rounds=closure(N,eq,g);assert b is not None
 direct=[q for q in central if known(q,b)==0]
 branches=[]
 for i,q in enumerate(central):
  v=known(q,b);assert v!=1
  if v is None:
   b2,rr=closure(N,list(b.values())+[(1<<q,1)],g)
   assert b2 is None, (i,opts[i])
   branches.append(dict(variable=q,option=opts[i],contradiction=True,rounds=rr))
 assert len(direct)+len(branches)==len(central)==520
 classes=defaultdict(list)
 for p in cells:classes[cl_rank(p,d)[0]].append(p)
 mult=max(map(len,classes.values()))
 assert len(cells)==206 and mult==8 and len(direct)==514 and len(branches)==6
 # Zero choices must satisfy every original white-history equation.
 assert all(rhs==0 for mask,rhs in eq)
 cert=dict(standard=standard,drift=d,library=lib,radius_periods=4,variables=N,original_equations=len(eq),complete_cells=cells,complete_cell_count=len(cells),direct_central_zero=len(direct),central_option_count=len(central),base_rank=len(b),base_rounds=rounds,failed_literal_certificates=branches,window_multiplicity=mult,finite_fuel_bound='4+8m decorated periods',seconds=time.time()-start)
 (HERE/'eight_step_detour_certificate.json').write_text(json.dumps(cert,indent=2));return cert
if __name__=='__main__':
 c=certify();print(json.dumps({k:v for k,v in c.items() if k not in ['complete_cells','standard']},indent=2))
