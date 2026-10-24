"""All-epoch certificate: W104 requires infinitely many black first-read cosets.
The finite cross-epoch check is exhaustive by the syllable-length bound below.
"""
import json
from pathlib import Path
from itertools import groupby
P=Path(__file__).resolve().parent
W=json.loads((P.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
def mul(x,y):
 s=list(x)
 for a,e in y:
  if s and s[-1][0]==a:
   _,f=s.pop();e=(e+f)%4
   if e:s.append((a,e))
  else:s.append((a,e))
 return tuple(s)
def inv(x):return tuple((a,4-e) for a,e in reversed(x))
def power(q,n):
 if n<0:q,n=inv(q),-n
 z=()
 for _ in range(n):z=mul(z,q)
 return z
u=((0,1),(1,3));ui=inv(u)
def canon(x):
 while True:
  cs=[x,mul(x,u),mul(x,ui)];m=min(map(len,cs));best=min(y for y in cs if len(y)==m)
  if m==len(x):return best
  x=best
prefix=[];q=()
for a in W:prefix.append(q);q=mul(q,((int(a=='L'),1),))
assert q[0][0]!=q[-1][0] and any(e==2 for _,e in q)
# q^n has no cancellations between copies. H\{1} has only exponents 1 and 3.
# In p_j^-1 q^n p_i, end multiplication can alter/remove at most
# len(p_j)+len(p_i)+2 syllables of the middle q^n block. If the remaining
# unmodified block is longer than the longest run without exponent 2,
# membership in H is impossible.
z=[e!=2 for _,e in q+q]
M=max((len(list(g)) for a,g in groupby(z) if a),default=0)
D=max(map(len,prefix));N=(2*D+2+M)//len(q)+1
assert N*len(q)-2*D-2>M
for n in range(1,N):
 qn=power(q,n)
 for i,a in enumerate(prefix):
  for j,b in enumerate(prefix):
   assert canon(mul(mul(inv(b),qn),a))!=(),(n,i,j)
# Thus no cell in epoch k can equal a cell in any other epoch.
seen={};black=[];white=[]
for i,(a,s) in enumerate(zip(W,prefix)):
 c=canon(s)
 if c in seen:assert seen[c]!=a,(i,a)
 elif a=='L':black.append(i)
 else:white.append(i)
 seen[c]=a
assert len(black)==19 and len(white)==31
out={'word_length':len(W),'reduced_word':''.join(('L' if a else 'R')*e for a,e in q),
 'reduced_syllables':len(q),'max_prefix_syllables':D,'max_non2_run':M,
 'large_epoch_gap_threshold':N,'checked_positive_epoch_gaps':list(range(1,N)),
 'cross_epoch_coset_collisions':0,'new_black_cosets_per_epoch':len(black),
 'new_white_cosets_per_epoch':len(white),'black_first_read_phases':black}
print(json.dumps(out,indent=2));(P/'certify_standard_lift_seed.json').write_text(json.dumps(out,indent=2)+'\n')
