"""Exact physical D control, explicitly artificial historical-color assignment."""
from pathlib import Path
import json,hashlib
from collections import defaultdict
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new/D_core_graft_noninductivity_frozen_20261023_1814';M=json.loads((D/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((D/f['file']).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items()if b};C={-2+0j,-2j};seed=K|{1j}|C;assert len(seed)==8
B=set(seed);p=0j;h=0;V=(1j,1,-1j,-1);rows=[];exitstate=None
for n,c in enumerate(raws[0]+mark):
 assert(p in B)==(c=='L');rows.append((xy(p),h,c));B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 if n+1==len(raws[0]):exitstate=set(B),p,h
E,e,g=exitstate;newK={e+rotation(q,g)for q in K};assert e==1+1j and g==0 and E==newK|{2+0j}|C
# The graph convention is doubled-coordinate even-checkerboard dual.
def endpoints(q):
 x,y=xy(q)
 return ((2*x-1,2*y-1),(2*x+1,2*y+1))if (x+y)%2==0 else((2*x-1,2*y+1),(2*x+1,2*y-1))
def components(S):
 G=defaultdict(set)
 for q in S:a,b=endpoints(q);G[a].add(b);G[b].add(a)
 todo=set(G);out=[]
 while todo:
  work=[todo.pop()];seen=set(work)
  while work:
   for q in G[work.pop()]:
    if q not in seen:seen.add(q);todo.discard(q);work.append(q)
  out.append(sorted(seen))
 return out
assert len(components(K))==1 and sum(len(x)for x in components(K))==6
assert len(components(C))==2 and len(components(C|K))==1 and len(components(C|newK))==3
oldvertices={v for q in K for v in endpoints(q)};newvertices={v for q in newK for v in endpoints(q)}
assert {v for q in C for v in endpoints(q)}&oldvertices=={(-3,1),(1,-3)}and not({v for q in C for v in endpoints(q)}&newvertices)
out=dict(status='PASS literal eight-cell D control and artificial-color noninductivity',manifest_sha256=hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),seed=sorted(map(xy,seed)),raw_reads=len(raws[0]),marker_reads=len(mark),raw_exit=(xy(e),g),initial_grafted_components=1,final_grafted_components=3,scope='The common component color of the two untouched cells is ARTIFICIAL. This refutes only local inductivity of that predicate from itself and the D guard, not reachable historical connectivity or the U-merger conjecture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
