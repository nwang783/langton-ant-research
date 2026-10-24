from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];P=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
notes={'staircase_triple_cycles_have_finite_singleton_output_chains.md':'9190569aa32c2299bedaeed4fbf156068d60775c8450ad880ccd78767c999f11','triple_circle_local_extrema_force_axis_or_singleton_ports.md':'2b33fcceaa79d33e70dde88d0b3812eca81fef25b9cc454ede44516334496909'}
for f,h in notes.items():assert sha(P/f)==h
H='NESW';V=(1j,1,-1j,-1);out=lambda h,j:(h+(1 if j%2==0 else-1))%4
xy=lambda z:(int(2*z.real),int(2*z.imag))
faces={'.5,.5':.5+.5j};named={'NW':-.5+.5j,'NE':.5+.5j,'SW':-.5-.5j,'SE':.5-.5j}
def levels(w,anchor):
 # Full directed-edge stream equation: right face minus left face equals port multiplicity.
 relations=[]
 for h in range(4):
  ni=sum(x==(h+2)%4 for x in w);no=sum(out(x,j)==h for j,x in enumerate(w));v=V[h]
  relations.append((v/2-1j*v/2,v/2+1j*v/2,no-ni))
 val={named[anchor]:0}
 for _ in range(4):
  for a,b,n in relations:
   if a in val:val.setdefault(b,val[a]-n)
   if b in val:val.setdefault(a,val[b]+n)
 assert len(val)==4 and all(val[a]-val[b]==n for a,b,n in relations)
 return{k:val[v]for k,v in named.items()}
def words(axis,requirements):
 ans=[]
 for n in range(1,5):
  for w in product(axis,repeat=n):
   inc=Counter(w);dep=Counter(out(h,j)for j,h in enumerate(w))
   if all((inc if kind=='in'else dep)[h]==n for kind,h,n in requirements):ans.append(w)
 return ans
A=words((0,2),[('in',0,3),('out',1,3)]);B=words((1,3),[('in',1,3),('out',0,3)]);U=words((0,2),[('in',2,1),('out',3,1)]);W=words((1,3),[('in',3,1),('out',2,1)])
string=lambda w:''.join(H[h]for h in w)
assert set(map(string,A))=={'NNNS','NSNN'} and set(map(string,B))=={'EEWE','WEEE'}
assert set(map(string,U))=={'S','NNNS','NSNN'} and set(map(string,W))=={'EEW','WEE','EEWE','WEEE'}
levU={string(w):levels(w,'NW')for w in U};levW={string(w):levels(w,'SE')for w in W}
for w in U:
 z=levU[string(w)];assert z['NE']==z['SW']==-1 and z['SE']==(-1 if len(w)==1 else 2)
for w in W:
 z=levW[string(w)];assert z['NE']==z['SW']==1 and z['NW']==(2-len(w))
# Both complete corner signs give the same one-use opposite-square ports.
for a,b in product(A,B):
 assert sum(out(h,j)==2 for j,h in enumerate(b))==b.count(3)==1
 assert sum(out(h,j)==2 for j,h in enumerate(a))==a.count(3)==0
for u in U:
 if len(u)>1:assert u.count(0)==sum(out(h,j)==1 for j,h in enumerate(u))==3
# All four whole-state rotations preserve literal incidence and relative heights.
rotated=[]
for r in range(4):
 for w in U+W:
  ww=tuple((h+r)%4 for h in w);assert all(out(ww[j],j)==(out(w[j],j)+r)%4 for j in range(len(w)))
  rotated.append(string(ww))
# Finite sanity controls of the analytic cyclic run argument, not its proof.
cyclic_counts={}
for n in range(4,17,2):
 good=[]
 for w in product('LR',repeat=n):
  if w.count('L')!=n//2:continue
  tr=[''.join(w[(i+j)%n]for j in range(3))for i in range(n)]
  if any(t in('LLL','RRR','RLR')for t in tr):continue
  assert n%4==0 and all(w[(i+4)%n]==w[i]for i in range(n));good.append(''.join(w))
 cyclic_counts[n]=len(good)
 assert len(good)==(4 if n%4==0 else 0)
# Concrete RRLL blocks all rotate to displacement length2 along one coordinate.
displacements=[]
for h0 in range(4):
 p=0j;h=h0
 for t in'RRLL':h=(h+(1 if t=='R'else -1))%4;p+=V[h]
 assert h==h0 and abs(p.real)+abs(p.imag)==2 and (p.real==0 or p.imag==0);displacements.append((int(p.real),int(p.imag)))
res={'status':'PASS staircase terminal chains and local-extrema axis/singleton implications','notes':notes,'A':list(map(string,A)),'B':list(map(string,B)),'U':levU,'W':levW,'rotated_local_controls':len(rotated),'cyclic_turn_controls':cyclic_counts,'RRLL_displacements':displacements,'analytic_review':[
'All one-to-four WHITE histories were rebuilt from literal R/L turns, and face heights independently solved from full directed port flow. An LRL unit-square gap has shared NW C=c and opposite SE C=c-1 for singleton S, c+2 for either four-read mode; both L=c-1. A RLR gap shares SE L=m=c-3 and has opposite NW L=m-1 or m-2 for every allowed complete WHITE history, including the odd triples.',
'For a whole NE staircase, every B has exactly one S departure and W arrival, hence each outer U is singleton S or one of the original A modes. If none is singleton, both three-use ports force every V to one of the original B modes. Thus the ENTIRE next row and its unchanged full drift and orientation persist, not merely a height or one port. It raises C by2 and shifts spatially by(1,-1). Normal x-y changes by2 while full diagonal drift preserves it; no quotient row recycling. Finite global C maximum forces a terminal singleton within floor((M-c)/2)+1 outward checks.',
'A row has at most one full geometric successor and predecessor, with signs allowed to change freely at each row. A terminal singleton heading fixes the rotated frame; its physical class, shared C face, and position recover its unique immediate inner row modulo full drift. Therefore only distinct maximal row-chain components inject into singleton classes. Different starting rows on one chain share payment; no addition to previous singleton reservations, initial-fuel charge, or recurrence bound follows.',
'At a locally maximal C component the higher-C alternative is impossible, hence every LRL triple gives its actual singleton output. At a locally minimal low-L component the strictly lower diagonal neighbor forbids RLR even if other Q corners are odd. These are same-component adjacent faces, not unrelated global heights.',
'A simple essential unit-edge physical circle cannot have three equal consecutive turns, as the four involved edges return to their initial physical vertex. Its total signed turn is zero. No RLR forces every L run length2; equal L/R totals and equal numbers of runs force all R runs length2 as well. Thus RRLL repeats, ell=4a, full drift is an axis vector of infinity norm2a, with sign handled by actual winding. This applies only to G3 cycles beside local L minima. General G3 paths, arbitrary minima, mixed fronts, and global attraction remain open.'
]};S.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(res['status'])
