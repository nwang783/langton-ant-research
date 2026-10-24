"""Exact finite guard obstruction for UNION, not XOR, of standard wake rails."""
import importlib.util,json
from pathlib import Path
here=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('rg',here/'reverse_wake_guard.py');m=importlib.util.module_from_spec(spec)
# Import computes the exact base guards and retains the source constants.
import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(m)
T=m.wake
# Normalize the reverse front to q0+(0,-1), hence same sector as the writer.
G={(t+m.q0[0]-m.q0[1]+1,(a+m.q0[0])%2):b for (t,a),b in m.guard.items()}
black=sorted(k for k,b in G.items() if b);white=sorted(k for k,b in G.items() if not b)
rails=[]
# Only offsets with overlap with a required-black class are useful in a union.
# Range is derived, not a spatial cutoff.
for rot in (0,2):
 base={(t if rot==0 else -t,a) for t,a in T}
 lo=min(t for t,a in black)-max(t for t,a in base)
 hi=max(t for t,a in black)-min(t for t,a in base)
 for delta in range(lo,hi+1):
  if delta%2:continue # even translation parity preserves writer sector
  for parity in (0,1):
   S={(t+delta,(a+parity)%2) for t,a in base}
   bm=sum(1<<i for i,k in enumerate(black) if k in S)
   wm=sum(1<<i for i,k in enumerate(white) if k in S)
   if bm:rails.append({'rotation':rot,'delta':delta,'x_parity':parity,'black_mask':bm,'white_mask':wm})
assert all(r['white_mask'] for r in rails)
checks=[];best=100;witness=None
for allowed in range(1<<len(white)):
 cov=bad=0;used=[]
 for j,r in enumerate(rails):
  if r['white_mask']&~allowed==0:
   cov|=r['black_mask'];bad|=r['white_mask'];used.append(j)
 cost=len(black)-cov.bit_count()+bad.bit_count()
 checks.append(cost)
 if cost<best:best=cost;witness={'rails':used,'covered_black_mask':cov,'covered_white_mask':bad}
# Why this exhausts all unions: any union has a white-error set A. Adding every
# rail with white_mask subset A cannot introduce a new white error and can only
# improve black coverage. The checked maximal union dominates that union.
assert best==4
out={'status':'exact guard theorem for unions; XOR superpositions are NOT covered',
     'required_black':black,'required_white':white,'rails':rails,
     'white_subset_cases':len(checks),'minimum_guard_mismatches':best,
     'minimum_witness':witness,'costs':checks}
here.joinpath('reverse_wake_union_guard.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ('rails','costs')},indent=2))
