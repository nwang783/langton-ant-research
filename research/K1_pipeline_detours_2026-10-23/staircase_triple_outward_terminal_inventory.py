"""Complete WHITE port inventories for one staircase G3 row and its next row.
Fixed local configurations only, no front or period search.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def count(h,p,kind):return sum((x if kind=='in'else out(h,r))==p for r,x in enumerate(h))
def rows(axis,conds):
 z=[]
 for n in range(1,5):
  for hh in product(axis,repeat=n):
   h=''.join(hh)
   if all(count(h,p,k)==f for p,k,f in conds):z.append(h)
 return z
A=rows('NS',[('N','in',3),('E','out',3)])
B=rows('EW',[('E','in',3),('N','out',3)])
U=rows('NS',[('S','in',1),('W','out',1)])
assert set(A)=={'NNNS','NSNN'}and set(B)=={'EEWE','WEEE'}and set(U)=={'S','NNNS','NSNN'}
# Every allowed B has the same two one-use side ports, independent of its sign.
assert all(count(h,'S','out')==count(h,'W','in')==1 for h in B)
# Every nonterminal U has precisely the A triple input/output interface.
assert all(count(h,'N','in')==count(h,'E','out')==3 for h in U if h!='S')
# At the U shared NW C face set c=0; formulas from NS-rotated port counts.
levels={}
for h in U:
 # NS is the +90degree rotation E/W, so N-counts use E formulas.
 rN=sum(x=='N'for x in h[::2]);rS=sum(x=='S'for x in h[::2]);lN=sum(x=='N'for x in h[1::2]);lS=sum(x=='S'for x in h[1::2]);a=-rS
 C=dict(NW=a+rS,SE=a+rN);L=dict(SW=a-lN,NE=a-lS)
 assert C['NW']==0
 levels[h]=dict(C=C,L=L)
assert levels['S']['C']['SE']==-1
assert all(levels[h]['C']['SE']==2 and set(levels[h]['L'].values())=={-1}for h in A)
obj=dict(scope=__doc__,A_profiles=A,B_profiles=B,U_profiles=U,U_face_levels_at_inner_c_zero=levels,forced_extension='If every U is four-read, U becomes the next A row at c+2 and both neighboring triple ports force V to become the next B row.',terminal='U=S is an actual singleton-R odd-output class, not prepared BLACK input.',warning='Only row-chain components, not arbitrary repeated renewals or all G3 circles, may be injected into terminal output classes.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
