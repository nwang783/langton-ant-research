"""Literal finite controls for the all-R-on-one-parity normal form."""
import itertools,json,pathlib
from free_inflation_generic_csp import trace,seed
HERE=pathlib.Path(__file__).resolve().parent
out=[]
for N in range(1,17):
 legal=[]
 for odd in itertools.product('RL',repeat=N):
  s=''.join(odd);w=''.join('R'+c for c in s);B=seed(w)
  if B is None:continue
  # One horizontal L run, with at most one leading and two trailing R's.
  is_form=(s.strip('R')=='L'*s.count('L') and s.count('R')<=3)
  if 'L' in s:
   first=s.index('L');last=s.rindex('L')
   is_form=is_form and first<=1 and len(s)-last-1<=2
  else:is_form=is_form and len(s)<=2
  assert is_form,(N,s)
  assert N<=len(B)+3,(N,s,B)
  legal.append(s)
 out.append(dict(pairs=N,legal_count=len(legal),odd_words=legal))
for m in range(1,21):
 w='RR'+'RL'*m+'RRRR';B=seed(w)
 assert B is not None and len(B)==m and len(w)//2==m+3
 assert all((x+y)%2==1 for x,y in B)
(HERE/'checkerboard_turn_fuel_controls.json').write_text(json.dumps(dict(all_R_first_pair_controls=out,sharp_witness_m=list(range(1,21))),indent=2))
print('PASS',sum(z['legal_count']for z in out),'legal controls, 20 sharp witnesses')
